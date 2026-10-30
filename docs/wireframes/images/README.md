# SaOr - Sales Order
## Wireframes Conceituais em Imagem — Controle operacional

**Baseline funcional:** `v1.0 — APROVADO / BASELINE FUNCIONAL`  
**Etapa atual:** `Wireframe Conceitual em Imagem`  
**Fonte funcional:** [`docs/Documento_Mestre.md`](../../Documento_Mestre.md)  
**Não regressão funcional:** [`docs/Registro_Fechamento_Documento_Mestre.md`](../../Registro_Fechamento_Documento_Mestre.md)  
**Interfaces:** `71`  
**Variações funcionais obrigatórias:** Claro (`white`) e Escuro (`black`)  
**Viewport lógico oficial:** `360 × 800 px`  
**Canvas técnico das pranchas:** `1280 × 1920 px`  
**Template oficial atualmente vigente:** Modelo C (`white` v02 / `black` v01); arquivos `APROVADO E CONGELADO`, seleção revisável somente por aprovação formal  
**Vigência e histórico das decisões:** [`Registro_Controle_Template_Oficial.md`](Registro_Controle_Template_Oficial.md)

---

# 1. Responsabilidade deste documento

Este README é um **inventário e controle operacional**: diretórios, referências físicas, histórico dos modelos A/B/C, identidade dos arquivos, matriz das 71 interfaces, estados agregados e contadores. Ele **não** define o processo normativo de construção nem seleciona um modelo por conta própria.

Autoridades (caminhos relativos à raiz do repositório):

```text
docs/Documento_Mestre.md — fonte de requisitos funcionais
.specs/wireframes/REGRAS-TECNICAS.md — invariantes de representação
.specs/wireframes/PROCESSO-PRANCHA.md — SPEC 1, Prancha do Template
.specs/wireframes/REFERENCIA-TEMPLATE-OFICIAL.md — SPEC 2, referência selecionada
docs/wireframes/images/Registro_Controle_Template_Oficial.md — vigência/histórico/hashes
.specs/wireframes/PROCESSO-TELA-PRANCHA.md — SPEC 3, fluxo funcional
.specs/wireframes/WIREFRAME-TEXT-TELA.md — contrato do texto individual da Tela
```

Este README não altera a baseline funcional nem os hashes do template. Não devem existir regras concorrentes aqui: quando necessário, a seção operacional aponta para a SPEC competente.

---

# 2. Estrutura da etapa

A estrutura física vigente é:

```text
docs/wireframes/images/
├── README.md
├── Registro_Controle_Template_Oficial.md
├── references/
│   ├── Especificação Técnica - Prancha de Trabalho.png
│   ├── white/
│   │   ├── Especificação Técnica do Viewport Mobile.png
│   │   ├── WF-VIEWPORT-360x800-clean.png
│   │   ├── WF-VIEWPORT-360x800-clean_icone-esquerda.png
│   │   └── WF-VIEWPORT-360x800.png
│   ├── black/
│   │   └── WF-VIEWPORT-360x800.png
│   └── templates/
│       ├── white/
│       │   ├── <pranchas-modelo claras>.png
│       │   └── wiframetext/
│       │       └── <mesmo-nome-base>.md
│       └── black/
│           ├── <pranchas-modelo escuras>.png
│           └── wiframetext/
│               └── <mesmo-nome-base>.md
├── white/
│   ├── template/
│   │   ├── WF-TEMPLATE-C_v02.png
│   │   ├── WF-TEMPLATE-C_v02.md
│   │   └── WF-VIEWPORT-360x800.png
│   ├── telas/
│   │   ├── controle/
│   │   │   └── T00-01-01_v01.md  # Registro, sem aprovação humana presumida
│   │   ├── wiframetext/
│   │   │   └── <TextFrame após aprovação GI-1>
│   │   ├── T00-01-01_v01.png
│   │   └── T00-01-01_v01__estado-desconectada.png
│   ├── wiframetext/      # Registros de composição funcional (futuros)
│   └── <Pranchas de Implementação, futuras>
└── black/
    ├── template/
    │   ├── WF-TEMPLATE-C_v01.png
    │   ├── WF-TEMPLATE-C_v01.md
    │   └── WF-VIEWPORT-360x800.png
    ├── telas/
    │   ├── controle/
    │   │   └── T00-01-01_v01.md  # Registro, sem aprovação humana presumida
    │   ├── wiframetext/
    │   │   └── <TextFrame após aprovação GI-1>
    │   ├── T00-01-01_v01.png
    │   └── T00-01-01_v01__estado-desconectada.png
    ├── wiframetext/      # Registros de composição funcional (futuros)
    └── <Pranchas de Implementação, futuras>
```

Separação de responsabilidade:

```text
references/
→ referências técnicas compartilhadas ou específicas por variação

references/templates/white/
→ pranchas-modelo e Wireframe Text da variação clara

references/templates/black/
→ pranchas-modelo e Wireframe Text da variação escura

white/template/ e black/template/
→ conjunto oficial **atualmente vigente** por tema: Prancha C (PNG + Wireframe Text) + Viewport técnico (PNG), todos congelados; NÃO são interfaces funcionais

white/telas/ e black/telas/
→ telas de referência funcionais independentes e seus Wireframe Text individuais (futuras)

white/wiframetext/ e black/wiframetext/
→ registros textuais de composição da Prancha de Implementação (futuros)

white/ e black/ na raiz de images/ (fora de template/ e telas/)
→ PNGs de Prancha de Implementação (futuros), vinculados à versão oficial exata utilizada
```

A estrutura anterior baseada em pastas de ciclo de vida não faz mais parte da organização vigente.

A evolução de uma prancha-modelo é registrada no próprio Wireframe Text pelos estados definidos em `.specs/wireframes/PROCESSO-PRANCHA.md`.

## 2.1 Estados de construção das pranchas-modelo

Durante a construção de uma prancha-modelo e do PNG correspondente, somente estes estados podem ser usados:

```text
PENDENTE
EM DEFINIÇÃO
AGUARDANDO APROVAÇÃO
APROVADO E CONGELADO
BLOQUEADO POR GATE ANTERIOR
NÃO APLICÁVEL
```

Os Gates 1, 4 e 5 são técnicos.

Os Gates 2, 3 e 6 exigem aprovação humana explícita.

A produção do PNG usa o mesmo conjunto de estados:

```text
BLOQUEADO POR GATE ANTERIOR
→ Gate 6 ainda não aprovado

PENDENTE
→ Gate 6 aprovado; produção ainda não iniciada

EM DEFINIÇÃO
→ imagem em construção ou correção

AGUARDANDO APROVAÇÃO
→ PNG construído e validado contra o Wireframe Text

APROVADO E CONGELADO
→ imagem aprovada explicitamente e congelada
```

Essa classificação pertence às pranchas-modelo e não substitui os estados da matriz funcional das 71 interfaces.

---

# 3. Referências técnicas e pranchas-modelo

`references/` concentra os artefatos de referência usados na etapa.

## 3.1 Referência neutra compartilhada

Arquivo atualmente existente:

```text
references/Especificação Técnica - Prancha de Trabalho.png
```

Esse PNG mede `1280 × 1920 px` e é fisicamente um canvas branco neutro. Ele serve como referência física de prancha, não como fonte normativa de medidas, regras ou conteúdo. As regras permanecem nas specs canônicas.

## 3.2 Referências específicas por variação

Variação clara:

```text
references/white/Especificação Técnica do Viewport Mobile.png
references/white/WF-VIEWPORT-360x800-clean.png
references/white/WF-VIEWPORT-360x800-clean_icone-esquerda.png
references/white/WF-VIEWPORT-360x800.png
```

Os bitmaps `WF-VIEWPORT-360x800*` medem `360 × 800 px` e representam variações físicas diferentes do mesmo viewport demonstrativo; `WF-VIEWPORT-360x800.png` é a variante gerada com a paleta técnica de `REGRAS-TECNICAS.md`, seção 6 (tabela 6.5). O Wireframe Text específico determina qual arquivo deve ser usado. O `clean.png` permanece preservado; não deve ser removido nem substituído silenciosamente pelo arquivo `_icone-esquerda.png`.

As pranchas-modelo white atuais `WF-TEMPLATE-A_v04`, `WF-TEMPLATE-B_v02` e `WF-TEMPLATE-C_v02` usam `WF-VIEWPORT-360x800.png`.

Variação escura:

```text
references/black/WF-VIEWPORT-360x800.png
```

A pasta `black/` recebe somente referências físicas específicas da variação escura. `WF-VIEWPORT-360x800.png` é o viewport black aprovado, gerado com a tabela 6.6 de `REGRAS-TECNICAS.md`.

Não utilizar um bitmap específico de `white` como referência de `black` por inferência.

As dimensões, cotas, grid e demais invariantes continuam pertencendo às specs canônicas, independentemente da existência de um bitmap específico.

## 3.3 Pranchas-modelo

As pranchas-modelo ficam separadas por variação:

```text
references/templates/white/
references/templates/black/
```

O Wireframe Text de cada prancha-modelo fica dentro da mesma variação:

```text
references/templates/<variação>/wiframetext/<nome>.md
```

A variação registrada no Wireframe Text deve coincidir com a pasta onde o artefato está localizado.

A construção e o acompanhamento de cada prancha-modelo obedecem a:

```text
../../../.specs/wireframes/REGRAS-TECNICAS.md
../../../.specs/wireframes/WIREFRAME-TEXT.md
../../../.specs/wireframes/MONTAGEM-IMAGEM.md
```

Este README não redefine dimensões, cotas ou geometria desses arquivos.

## 3.4 Referências históricas e seleção atualmente vigente

Os artefatos completos dos Modelos A/B/C permanecem em `references/templates/`, em `white` e `black`, conforme inventário na seção 3.3. O histórico não é uma lista de modelos intercambiáveis para nova produção funcional. **A vigência é determinada somente pelo registro genérico**, conforme a SPEC 2:

- [`.specs/wireframes/REFERENCIA-TEMPLATE-OFICIAL.md`](../../../.specs/wireframes/REFERENCIA-TEMPLATE-OFICIAL.md)
- [`Registro_Controle_Template_Oficial.md`](Registro_Controle_Template_Oficial.md)

**Seleção atual registrada em 28/10/2026:** Modelo C, `white` v02 e `black` v01. A/B e versões históricas do C permanecem como histórico/contexto; nenhuma substituição pode ser presumida por imagem, nome ou preferência. A referência de uma saída já aprovada é a **versão exata registrada naquela saída**, mesmo após uma eventual mudança de vigência.

### 3.4.1 Inventário visual contextual aprovado e histórico

As pranchas-modelo ainda podem servir como **referências contextuais de linguagem e acabamento**: densidade documental, hierarquia, cabeçalho, metadados, distribuição de regiões, tratamento cromático integral, contrastes, alinhamento, ritmo e qualidade de apresentação. Essa função **não as promove a modelo vigente** e não autoriza copiar sua geometria para uma interface funcional; a cromia normativa continua definida em `REGRAS-TECNICAS.md` e `MONTAGEM-IMAGEM.md`.

```text
white — conjunto contextual atualizado
references/templates/white/WF-TEMPLATE-A_v04.png
references/templates/white/WF-TEMPLATE-B_v02.png
references/templates/white/WF-TEMPLATE-C_v02.png

black — conjunto contextual atualizado
references/templates/black/WF-TEMPLATE-A_v01.png
references/templates/black/WF-TEMPLATE-B_v01.png
references/templates/black/WF-TEMPLATE-C_v01.png
```

Também permanecem as versões históricas white `A_v01`, `A_v02`, `A_v03`, `B_v01` e `C_v01`, preservadas para rastreabilidade de evolução. `white`/`black` são variações técnicas e cromáticas, **não** autorização para converter elementos em escala de cinza. A imagem contextual nunca se sobrepõe às especificações aprovadas.

## 3.5 Arquivos da referência oficial atualmente vigente

| Tema | Prancha aprovada | Wireframe Text da Prancha aprovada | ViewPort demonstrativo |
|---|---|---|---|
| `white` | `white/template/WF-TEMPLATE-C_v02.png` | `white/template/WF-TEMPLATE-C_v02.md` | `white/template/WF-VIEWPORT-360x800.png` |
| `black` | `black/template/WF-TEMPLATE-C_v01.png` | `black/template/WF-TEMPLATE-C_v01.md` | `black/template/WF-VIEWPORT-360x800.png` |

Os seis arquivos e as seis origens estão preservados. **Caminhos e hashes oficiais devem ser conferidos diretamente no registro genérico**, não inferidos desta tabela de estado. O ViewPort demonstrativo não constitui Tela funcional. A produção individual segue a SPEC 3 e não conta nenhum desses arquivos como saída T/M/E.

---

# 4. Viewport e geometria

Fonte canônica:

```text
../../../.specs/wireframes/REGRAS-TECNICAS.md
../../../.specs/wireframes/PROCESSO-PRANCHA.md
```

Este README não replica valores de viewport, canvas, cotas ou safe area.

---

# 5. Grid e espaçamento

Fonte canônica:

```text
../../../.specs/wireframes/REGRAS-TECNICAS.md
```

---

# 6. Tokens e tipografia técnica

Fonte canônica:

```text
../../../.specs/wireframes/REGRAS-TECNICAS.md
```

---

# 7. Componentes técnicos de representação

Fonte canônica:

```text
../../../.specs/wireframes/REGRAS-TECNICAS.md
```

---

# 8. Bordas, radius, elevação e iconografia

Fonte canônica:

```text
../../../.specs/wireframes/REGRAS-TECNICAS.md
```

---

# 9. Estados técnicos

Fonte canônica:

```text
../../../.specs/wireframes/REGRAS-TECNICAS.md
```

---

# 10. Acessibilidade estrutural

Fonte canônica:

```text
../../../.specs/wireframes/REGRAS-TECNICAS.md
```

O Documento Mestre continua sendo a autoridade para conteúdo e comportamento funcional.

---

# 11. Saídas funcionais futuras

Esta seção se aplica somente depois de existir uma prancha-modelo aprovada e congelada para a variação correspondente.

A construção atual das pranchas-modelo ocorre em `references/templates/` e não deve ser confundida com as saídas funcionais em `white/` e `black/`.


Cada uma das 71 interfaces deve possuir, no mínimo, uma representação Claro em `white/` e uma representação Escuro em `black/`.

```text
Mínimo Claro: 71
Mínimo Escuro: 71
Mínimo funcional: 142
```

O total final pode aumentar por paginação.

## 11.1 Localização e nomenclatura operacional

Nomes, páginas, versões, procedimentos de criação/revisão e separação de pastas são definidos **somente** na [SPEC 3](../../../.specs/wireframes/PROCESSO-TELA-PRANCHA.md), seções 3–8. Para cada ID/tema/página/versão, o registro prévio de inventário e aprovação visual GI-0/GI-1 fica em `<tema>/telas/controle/` (diretório futuro), o **PNG da Tela deve existir e receber aprovação visual antes da criação de seu TextFrame**, e o arquivo de Tela fica em `<tema>/telas/` e o PNG da Prancha de Implementação fica diretamente em `<tema>/`; os registros `.md` ficam nos respectivos diretórios `wiframetext/`. Uma aprovação de Prancha não representa aprovação da Tela.

Os arquivos de interface funcional ainda estão pendentes; o esquema de diretórios na seção 2 inclui destinos **planejados**, não declara arquivos físicos já existentes.

## 11.2 Conteúdo e produção

O conteúdo mínimo, a sequência de inventário GI-0 → PNG visual de Tela → aprovação visual GI-1 → TextFrame derivado do PNG → aprovação documental do conjunto GI-2 → Prancha de Implementação → aprovação GI-4, a paginação, a equivalência white/black e os critérios de exportação pertencem exclusivamente à [SPEC 3](../../../.specs/wireframes/PROCESSO-TELA-PRANCHA.md), ao [contrato textual da Tela](../../../.specs/wireframes/WIREFRAME-TEXT-TELA.md) e ao [Gate funcional GI-0 a GI-4](../../../.specs/wireframes/GATE-IMPLEMENTACAO-TELAS.md). Os requisitos funcionais permanecem no Documento Mestre. Não inferir conteúdo da demonstração de ViewPort ou da Prancha do Template. Os campos já existentes `PÁGINA` e `ETAPA` devem ser preenchidos conforme a SPEC 3; a matriz abaixo permanece agregada por ID/tema, não por página.

---

# 14. Estados de controle das interfaces funcionais

Os estados abaixo pertencem à matriz futura das 71 interfaces e permanecem alinhados ao Documento Mestre.

Eles não são os estados usados para acompanhar a construção das pranchas-modelo.


```text
PENDENTE
EM VALIDAÇÃO
AJUSTES NECESSÁRIOS
APROVADO
```

Silêncio não constitui aprovação. Artefato aprovado fica congelado naquela versão; alteração posterior exige nova versão.

---

# 15. Controle das 71 interfaces

O nome e a especificação funcional de cada ID permanecem exclusivamente no Documento Mestre. Este checklist controla apenas o estado resumido da etapa.

Autoridade operacional:

- `white/` e `black/` contêm os arquivos funcionais produzidos;
- o nome físico de cada arquivo é a fonte de verdade para página atual, total de páginas e versão;
- as colunas `Claro` e `Escuro` registram o estado agregado de cada variação;
- `Status geral` deriva do conjunto completo das duas variações;
- uma interface somente pode ficar `APROVADO` quando todas as páginas necessárias de Claro e Escuro estiverem aprovadas e o Gate GI-4 do conjunto estiver concluído;
- o checklist não deve duplicar versão/paginação já expressas nos nomes dos arquivos.

| # | ID | Claro | Escuro | Status geral |
|---:|---|---|---|---|
| 01 | `T00` | EM DEFINIÇÃO | EM DEFINIÇÃO | EM DEFINIÇÃO |

| 02 | `T00.1` | PENDENTE | PENDENTE | PENDENTE |
| 03 | `T00.2` | PENDENTE | PENDENTE | PENDENTE |
| 04 | `T00.3` | PENDENTE | PENDENTE | PENDENTE |
| 05 | `M00.4` | PENDENTE | PENDENTE | PENDENTE |
| 06 | `M00.5` | PENDENTE | PENDENTE | PENDENTE |
| 07 | `E00.6` | PENDENTE | PENDENTE | PENDENTE |
| 08 | `E00.7` | PENDENTE | PENDENTE | PENDENTE |
| 09 | `E00.8` | PENDENTE | PENDENTE | PENDENTE |
| 10 | `E00.9` | PENDENTE | PENDENTE | PENDENTE |
| 11 | `E00.10` | PENDENTE | PENDENTE | PENDENTE |
| 12 | `T01` | PENDENTE | PENDENTE | PENDENTE |
| 13 | `T01.1` | PENDENTE | PENDENTE | PENDENTE |
| 14 | `E01.2` | PENDENTE | PENDENTE | PENDENTE |
| 15 | `E01.3` | PENDENTE | PENDENTE | PENDENTE |
| 16 | `E01.4` | PENDENTE | PENDENTE | PENDENTE |
| 17 | `E01.5` | PENDENTE | PENDENTE | PENDENTE |
| 18 | `T02` | PENDENTE | PENDENTE | PENDENTE |
| 19 | `T02.1` | PENDENTE | PENDENTE | PENDENTE |
| 20 | `T03` | PENDENTE | PENDENTE | PENDENTE |
| 21 | `M03.1` | PENDENTE | PENDENTE | PENDENTE |
| 22 | `E03.2` | PENDENTE | PENDENTE | PENDENTE |
| 23 | `T04` | PENDENTE | PENDENTE | PENDENTE |
| 24 | `T04.1` | PENDENTE | PENDENTE | PENDENTE |
| 25 | `T04.2` | PENDENTE | PENDENTE | PENDENTE |
| 26 | `T04.3` | PENDENTE | PENDENTE | PENDENTE |
| 27 | `T04.4` | PENDENTE | PENDENTE | PENDENTE |
| 28 | `T04.5` | PENDENTE | PENDENTE | PENDENTE |
| 29 | `T05` | PENDENTE | PENDENTE | PENDENTE |
| 30 | `T05.1` | PENDENTE | PENDENTE | PENDENTE |
| 31 | `T05.2` | PENDENTE | PENDENTE | PENDENTE |
| 32 | `T05.3` | PENDENTE | PENDENTE | PENDENTE |
| 33 | `T05.4` | PENDENTE | PENDENTE | PENDENTE |
| 34 | `T06` | PENDENTE | PENDENTE | PENDENTE |
| 35 | `M06.1` | PENDENTE | PENDENTE | PENDENTE |
| 36 | `T06.2` | PENDENTE | PENDENTE | PENDENTE |
| 37 | `E06.3` | PENDENTE | PENDENTE | PENDENTE |
| 38 | `T07` | PENDENTE | PENDENTE | PENDENTE |
| 39 | `M07.1` | PENDENTE | PENDENTE | PENDENTE |
| 40 | `E07.2` | PENDENTE | PENDENTE | PENDENTE |
| 41 | `T08` | PENDENTE | PENDENTE | PENDENTE |
| 42 | `T09` | PENDENTE | PENDENTE | PENDENTE |
| 43 | `M09.1` | PENDENTE | PENDENTE | PENDENTE |
| 44 | `T09.2` | PENDENTE | PENDENTE | PENDENTE |
| 45 | `M09.3` | PENDENTE | PENDENTE | PENDENTE |
| 46 | `T10` | PENDENTE | PENDENTE | PENDENTE |
| 47 | `M10.1` | PENDENTE | PENDENTE | PENDENTE |
| 48 | `T11` | PENDENTE | PENDENTE | PENDENTE |
| 49 | `T12` | PENDENTE | PENDENTE | PENDENTE |
| 50 | `M12.1` | PENDENTE | PENDENTE | PENDENTE |
| 51 | `T13` | PENDENTE | PENDENTE | PENDENTE |
| 52 | `T14` | PENDENTE | PENDENTE | PENDENTE |
| 53 | `M14.1` | PENDENTE | PENDENTE | PENDENTE |
| 54 | `T15` | PENDENTE | PENDENTE | PENDENTE |
| 55 | `T15.1` | PENDENTE | PENDENTE | PENDENTE |
| 56 | `T15.2` | PENDENTE | PENDENTE | PENDENTE |
| 57 | `T16` | PENDENTE | PENDENTE | PENDENTE |
| 58 | `T16.1` | PENDENTE | PENDENTE | PENDENTE |
| 59 | `T16.2` | PENDENTE | PENDENTE | PENDENTE |
| 60 | `M16.3` | PENDENTE | PENDENTE | PENDENTE |
| 61 | `E16.4` | PENDENTE | PENDENTE | PENDENTE |
| 62 | `T17` | PENDENTE | PENDENTE | PENDENTE |
| 63 | `T17.1` | PENDENTE | PENDENTE | PENDENTE |
| 64 | `T17.2` | PENDENTE | PENDENTE | PENDENTE |
| 65 | `T17.3` | PENDENTE | PENDENTE | PENDENTE |
| 66 | `T17.4` | PENDENTE | PENDENTE | PENDENTE |
| 67 | `T17.5` | PENDENTE | PENDENTE | PENDENTE |
| 68 | `M17.6` | PENDENTE | PENDENTE | PENDENTE |
| 69 | `E17.7` | PENDENTE | PENDENTE | PENDENTE |
| 70 | `E17.8` | PENDENTE | PENDENTE | PENDENTE |
| 71 | `E17.9` | PENDENTE | PENDENTE | PENDENTE |

---

# 16. Contadores

```text
Interfaces previstas:              71
Mínimo de imagens Claro:           71
Mínimo de imagens Escuro:          71
Mínimo de imagens funcionais:     142
Total final: variável por paginação
```

Pranchas-modelo de `references/templates/` **e os seis arquivos oficiais de template em `white/template/` e `black/template/`** não entram nessa contagem. Telas isoladas não são Pranchas funcionais; a matriz mantém o controle das saídas funcionais conforme seus critérios próprios.

---

# 17. Autoridade documental

- Documento Mestre: requisitos, fichas funcionais e Textframes das 71 interfaces.
- SPEC 1 `PROCESSO-PRANCHA.md`: definição/construção técnica de uma **Prancha do Template**; não governa saídas T/M/E.
- SPEC 2 `REFERENCIA-TEMPLATE-OFICIAL.md`: contrato permanente da referência oficialmente selecionada.
- [`Registro_Controle_Template_Oficial.md`](Registro_Controle_Template_Oficial.md): única fonte da decisão vigente, histórico das substituições, caminhos e hashes.
- SPEC 3 `PROCESSO-TELA-PRANCHA.md`: produção e aprovação de Wireframe Text da Tela, Tela de Referência e Prancha de Implementação.
- `WIREFRAME-TEXT-TELA.md`: contrato de TextFrame individual **derivado do PNG visual previamente aprovado em GI-1**, com confronto e aprovação documental em GI-2.
- `REGRAS-TECNICAS.md`: invariantes de representação; `WIREFRAME-TEXT.md` e `MONTAGEM-IMAGEM.md`: contratos auxiliares da **Prancha do Template**.
- Este README: **estrutura, inventário, matriz de 71 IDs e contadores**, sem autorização para redefinir qualquer regra anterior.
