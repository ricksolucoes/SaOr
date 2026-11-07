#!/usr/bin/env python3
"""Valida a estrutura EDITORIAL rígida dos três Markdown de interface SaOr.

Verifica títulos H1/H2/H3, ausência de H4+, abertura, tabelas, colunas, linhas
fixas, rótulos internos, presença de linhas e placeholders. Não comprova
requisitos, integridade dos artefatos citados, aprovações humanas ou Gates.
Não modifica arquivos. Requer somente a biblioteca-padrão Python 3.10+.
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
MODELOS = {
    "controle": RAIZ / "templates/CONTROLE-GI0-GI1.md",
    "textframe": RAIZ / "templates/TEXTFRAME-GI2.md",
    "composicao": RAIZ / "templates/COMPOSICAO-GI3-GI4.md",
}
RE_TITULO = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*$")
RE_CAMPO = re.compile(r"^\*\*([^*\n]+?:)\*\*", re.M)
RE_PLACEHOLDER = re.compile(r"\{\{[^{}]+\}\}")
RE_SEPARADOR = re.compile(r"^:?-{3,}:?$")


@dataclass
class Tabela:
    colunas: tuple[str, ...]
    linhas: list[tuple[str, ...]]
    linha_inicial: int


@dataclass
class Subtopico:
    nome: str
    linha: int
    tabelas: list[Tabela]
    campos: tuple[str, ...]


def ler(path: Path) -> str:
    return path.read_bytes().decode("utf-8-sig")


def separar_colunas(linha: str) -> tuple[str, ...]:
    """Preserva pipes escapados dentro de células; o separador não os conta."""
    s = linha.strip()
    if not s.startswith("|") or not s.endswith("|"):
        return ()
    partes = re.split(r"(?<!\\)\|", s[1:-1])
    return tuple(p.strip() for p in partes)


def se_tabela(linhas: list[str], k: int) -> bool:
    if k + 1 >= len(linhas):
        return False
    colunas = separar_colunas(linhas[k])
    separadores = separar_colunas(linhas[k + 1])
    return bool(colunas) and len(colunas) == len(separadores) and all(RE_SEPARADOR.fullmatch(x) for x in separadores)


def fragmentos(texto: str):
    linhas = texto.splitlines()
    titulos: list[tuple[int, str, int]] = []
    subtopicos: list[Subtopico] = []
    tabelas_fora: list[int] = []
    em_codigo = False
    delimitador = ""
    inicio_h3: int | None = None
    nome_h3 = ""
    linha_h3 = 0
    indices_titulo = []
    for i, linha in enumerate(linhas):
        stripped = linha.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            prefixo = stripped[:3]
            if not em_codigo:
                em_codigo = True
                delimitador = prefixo
            elif prefixo == delimitador:
                em_codigo = False
            continue
        if em_codigo:
            continue
        m = RE_TITULO.match(linha)
        if not m:
            continue
        nivel = len(m.group(1))
        titulos.append((nivel, m.group(2).strip(), i + 1))
        indices_titulo.append(i)
        if inicio_h3 is not None:
            fim = i
            subtopicos.append(_subtopico(nome_h3, linha_h3, linhas[inicio_h3:fim], inicio_h3, tabelas_fora))
            inicio_h3 = None
        if nivel == 3:
            nome_h3, linha_h3, inicio_h3 = m.group(2).strip(), i + 1, i + 1
    if inicio_h3 is not None:
        subtopicos.append(_subtopico(nome_h3, linha_h3, linhas[inicio_h3:], inicio_h3, tabelas_fora))

    # Tabelas fora de H3 são desvios; para localizá-las, percorrer o texto não
    # atribuído aos trechos H3 (inclui abertura e áreas H2 sem subtópico).
    cobertos = set()
    for h3 in subtopicos:
        a = h3.linha
        proximos = [i for i in indices_titulo if i + 1 > a]
        b = min(proximos) if proximos else len(linhas)
        cobertos.update(range(a, b))
    em_codigo = False
    delimitador = ""
    for k, linha in enumerate(linhas):
        st = linha.lstrip()
        if st.startswith(("```", "~~~")):
            if not em_codigo:
                em_codigo, delimitador = True, st[:3]
            elif st[:3] == delimitador:
                em_codigo = False
            continue
        if not em_codigo and k not in cobertos and se_tabela(linhas, k):
            tabelas_fora.append(k + 1)
    return titulos, subtopicos, tabelas_fora


def _subtopico(nome: str, linha: int, bloco: list[str], offset: int, externos: list[int]) -> Subtopico:
    tabelas: list[Tabela] = []
    campos: list[str] = []
    em_codigo = False
    delimitador = ""
    k = 0
    while k < len(bloco):
        st = bloco[k].lstrip()
        if st.startswith(("```", "~~~")):
            if not em_codigo:
                em_codigo, delimitador = True, st[:3]
            elif st[:3] == delimitador:
                em_codigo = False
            k += 1
            continue
        if em_codigo:
            k += 1
            continue
        mm = RE_CAMPO.match(bloco[k])
        if mm:
            campos.append(mm.group(1))
        if not se_tabela(bloco, k):
            k += 1
            continue
        colunas = separar_colunas(bloco[k])
        linhas_dados: list[tuple[str, ...]] = []
        j = k + 2
        while j < len(bloco):
            celulas = separar_colunas(bloco[j])
            if not celulas:
                break
            linhas_dados.append(celulas)
            j += 1
        tabelas.append(Tabela(colunas, linhas_dados, offset + k + 1))
        k = j
    return Subtopico(nome, linha, tabelas, tuple(campos))


def padrao_variavel(literal: str) -> re.Pattern[str]:
    partes = RE_PLACEHOLDER.split(literal)
    rex = [re.escape(partes[0])]
    for p in partes[1:]:
        rex.append(r".+?")
        rex.append(re.escape(p))
    return re.compile("".join(rex))


def checar(tipo: str, modelo: Path, arquivo: Path, *, template: bool) -> tuple[list[str], int, int]:
    falhas: list[str] = []
    texto_modelo, texto_doc = ler(modelo), ler(arquivo)
    esperado, esp_subs, esp_fora = fragmentos(texto_modelo)
    atual, doc_subs, doc_fora = fragmentos(texto_doc)
    if esp_fora:
        falhas.append(f"modelo inválido: tabela fora de H3 em {esp_fora}")
    if len(esperado) != len(atual):
        falhas.append(f"títulos H1/H2/H3: quantidade esperada {len(esperado)}; encontrada {len(atual)}")
    for i, exp in enumerate(esperado):
        if i >= len(atual):
            falhas.append(f"título ausente na posição {i+1}: {'#'*exp[0]} {exp[1]}")
            continue
        obt = atual[i]
        if obt[0] != exp[0] or not padrao_variavel(exp[1]).fullmatch(obt[1]):
            falhas.append(f"título #{i+1} linha {obt[2]}: esperado {'#'*exp[0]} {exp[1]!r}; obtido {'#'*obt[0]} {obt[1]!r}")
    for extra in atual[len(esperado):]:
        falhas.append(f"título excedente na linha {extra[2]}: {'#'*extra[0]} {extra[1]}")
    if len(esp_subs) != len(doc_subs):
        falhas.append(f"quantidade de H3: esperada {len(esp_subs)}, obtida {len(doc_subs)}")
    for i, exp in enumerate(esp_subs):
        if i >= len(doc_subs):
            break
        doc = doc_subs[i]
        if exp.nome != doc.nome:
            # O erro de título já foi informado; continuar comparando pelo índice.
            pass
        if len(exp.tabelas) != len(doc.tabelas):
            falhas.append(f"{exp.nome}: esperadas {len(exp.tabelas)} tabela(s), encontradas {len(doc.tabelas)}")
        for j, tab in enumerate(exp.tabelas):
            if j >= len(doc.tabelas):
                break
            real = doc.tabelas[j]
            if tab.colunas != real.colunas:
                falhas.append(f"{exp.nome}, tabela {j+1}: colunas diferentes: esperado {tab.colunas}, recebido {real.colunas}")
            if not real.linhas:
                falhas.append(f"{exp.nome}, tabela {j+1}: tabela sem linha de dados")
            for idx, linha in enumerate(real.linhas, 1):
                if len(linha) != len(real.colunas):
                    falhas.append(f"{exp.nome}, tabela {j+1}, linha {idx}: quantidade de células diferente do cabeçalho")
            fixas = [linha[0] for linha in tab.linhas if linha and not RE_PLACEHOLDER.search(linha[0])]
            labels = [linha[0] for linha in real.linhas if linha]
            ultimo = 0
            for fixa in fixas:
                try:
                    ultimo = labels.index(fixa, ultimo) + 1
                except ValueError:
                    falhas.append(f"{exp.nome}, tabela {j+1}: linha fixa ausente ou fora de ordem: {fixa}")
                    break
        if exp.campos != doc.campos:
            falhas.append(f"{exp.nome}: campos rotulados fora do modelo: esperado {exp.campos}; recebido {doc.campos}")
    if doc_fora:
        falhas.append(f"tabela(s) inserida(s) fora de H3 nas linhas {doc_fora}")
    if not texto_doc.startswith("# SaOr —"):
        falhas.append("documento não começa com H1 SaOr")
    if not re.search(r"(?m)^\*\*Estado vigente \(", texto_doc):
        falhas.append("linha inicial Estado vigente ausente ou diferente")
    if not template:
        for valor in sorted(set(RE_PLACEHOLDER.findall(texto_doc))):
            falhas.append(f"placeholder ainda não preenchido: {valor}")
    return falhas, len(esperado), len(esp_subs)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    op = ap.add_mutually_exclusive_group(required=True)
    op.add_argument("--templates", action="store_true")
    op.add_argument("--arquivo", type=Path, help="Markdown que será analisado, sem modificá-lo")
    ap.add_argument("--tipo", choices=tuple(MODELOS))
    args = ap.parse_args()
    if args.arquivo and not args.tipo:
        ap.error("--arquivo requer --tipo")
    if args.templates and args.tipo:
        ap.error("--templates não aceita --tipo")
    casos = [(t, p, p, True) for t,p in MODELOS.items()] if args.templates else [(args.tipo, MODELOS[args.tipo], args.arquivo, False)]
    erros = []
    for tipo, modelo, arquivo, template in casos:
        try:
            falhas, h, subt = checar(tipo, modelo, arquivo, template=template)
        except (OSError, UnicodeError) as exc:
            falhas, h, subt = [f"erro de leitura: {exc}"], 0, 0
        if falhas:
            erros.extend(falhas)
            for f in falhas:
                print(f"DESVIO {tipo}: {f}")
        else:
            print(f"CONFORME ESTRUTURAL: {tipo} — {h} títulos, {subt} subtópicos")
    if erros:
        print(f"Total: {len(erros)} desvio(s). Resultado exclusivamente editorial, não é decisão de Gate.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
