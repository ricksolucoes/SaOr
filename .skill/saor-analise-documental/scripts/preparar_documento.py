#!/usr/bin/env python3
"""Cria rascunho local pelo template EXATO, nunca documento aprovado.

Só utilizar após autorização humana específica; --autorizado é confirmação
operacional do operador, não prova de aprovação no repositório.
Não substitui arquivo existente e não preenche requisitos, decisões ou hashes.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
MODELOS = {
    "controle": (RAIZ / "templates/CONTROLE-GI0-GI1.md", r"docs/wireframes/images/(white|black)/telas/controle/[^/]+\.md"),
    "textframe": (RAIZ / "templates/TEXTFRAME-GI2.md", r"docs/wireframes/images/(white|black)/telas/wiframetext/[^/]+\.md"),
    "composicao": (RAIZ / "templates/COMPOSICAO-GI3-GI4.md", r"docs/wireframes/images/(white|black)/telas/pranchas/01_Mobile_360x800/wiframetext/[^/]+\.md"),
}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--tipo", choices=tuple(MODELOS), required=True)
    ap.add_argument("--destino", type=Path, required=True)
    ap.add_argument("--autorizado", action="store_true", help="confirma autorização específica prévia; não substitui evidência humana")
    args = ap.parse_args()
    if not args.autorizado:
        ap.error("criação exige autorização humana prévia e --autorizado")
    modelo, padrao = MODELOS[args.tipo]
    path = args.destino
    path_parts = path.as_posix().replace('\\','/').split('/')
    if 'assets' in path_parts or '..' in path_parts:
        ap.error("destino proibido ou caminho inseguro")
    posix = path.as_posix()
    pos = posix.find('docs/wireframes/images/')
    if pos < 0 or not re.fullmatch(padrao, posix[pos:]):
        ap.error("destino não corresponde ao caminho do documento na SPEC 3")
    if path.exists():
        ap.error("documento já existe: não substituir; atualização exige procedimento próprio")
    if not path.parent.is_dir():
        ap.error("diretório de destino deve existir; criação adicional exige escopo autorizado")
    data = modelo.read_bytes()
    with path.open('xb') as out:
        out.write(data)
    print(f"RASCUNHO INCOMPLETO: {path}; {len(data)} bytes copiados literalmente do template.")
    print("Preencha todos os placeholders a partir das evidências e execute validar_estrutura.py. Nenhum Gate foi aprovado por esta operação.")


if __name__ == '__main__':
    main()
