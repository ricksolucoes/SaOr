# SaOr — Contrato técnico de utilização do template oficial: Modelo C

## 1. Natureza e autoridade

**Contrato CONCRETO, versionado pelo conjunto de referências vinculadas abaixo.** Não é uma SPEC geral nem seleciona sozinho outro template. Sua validade é condicionada à seleção expressa registrada em `docs/wireframes/images/Registro_Controle_Template_Oficial.md` e à identidade binária das seis fontes oficiais. Atende à consulta obrigatória de `.specs/wireframes/REFERENCIA-TEMPLATE-OFICIAL.md` §4 e `.specs/wireframes/PROCESSO-TELA-PRANCHA.md` §6.1.

Aplica-se **somente às novas cópias de Prancha de Implementação** derivadas do Modelo C. Os arquivos oficiais congelados e seus Wireframe Text não podem ser editados. Seleção futura de outro modelo exige outro contrato específico comprovado. Este documento não contém componentes obrigatórios de T00, T00.1 ou qualquer outra interface.

## 2. Identidades vinculantes, dois temas

| Tema | Imagem do template oficial | Wireframe Text oficial | ViewPort demonstrativo | SHA-256 PNG / MD / ViewPort |
|---|---|---|---|---|
| white | `docs/wireframes/images/white/template/WF-TEMPLATE-C_v02.png` | `docs/wireframes/images/white/template/WF-TEMPLATE-C_v02.md` | `docs/wireframes/images/white/template/WF-VIEWPORT-360x800.png` | `558d108e3b0fec923e478482749c678f4b50d8b09055441ee52a9392b0f4929d` / `89154c5c1dda6f1aa1a16ac85a641a3ddc3101da8011f727eaec2c68141980c7` / `7de6522e31df89c8925093691442726ef7f72724bcde5905fb3380e4c5c5687c` |
| black | `docs/wireframes/images/black/template/WF-TEMPLATE-C_v01.png` | `docs/wireframes/images/black/template/WF-TEMPLATE-C_v01.md` | `docs/wireframes/images/black/template/WF-VIEWPORT-360x800.png` | `a1c6816cd14e0ea74f1bfb02842581dd7f3fa400c190087cbfa33e93f3b3cb63` / `60e1a8f476fc36233033d3c99f1588f21ee560967c31d6a31f6fb13e43b1892b` / `fde139557c36375f5ce569f4884822d4fd7c8344da1ce777b72873e1885a73fd` |

A documentação de origem das duas composições está integralmente nos respectivos Wireframe Text. Os valores da tabela são conferidos por hash no momento de uso, e não aceitos porque constam do nome do arquivo.

## 3. Geometria efetiva do Modelo C

**Canvas:** 1280 × 1920 px; área útil `x=12,y=12,w=1256,h=1896`; três colunas com início `x=12,w=416`, `x=444,w=360`, `x=820,w=448` e espaçamentos de 16 px. **Cabeçalho:** `x=12,y=12,w=1256,h=96`.

**Inserção obrigatória da Tela aprovada em nova cópia:** `x=40,y=272,w=360,h=800`, escala `1:1`, sem recorte, resize, filtro ou alteração de qualquer pixel. Esta é a **primeira substituição** da cópia de trabalho. Comparar os 288.000 pixels da região com o arquivo de Tela da mesma página e tema.

As coordenadas a seguir são do **Modelo C**, não uma norma universal de interface:

| Região | x | y card | largura | altura card | Conteúdo fixo e uso funcional autorizado |
|---|---:|---:|---:|---:|---|
| 1 ViewPort | 12 | 196 | 416 | 892 | Guias e dimensões fixas; trocar apenas bitmap 360×800 no ponto acima |
| 2 Ícones | 12 | 1136 | 416 | 168 | Demonstrações técnicas; não declarar iconografia usada só por aparecer aqui |
| 3 Regras de componentes | 12 | 1352 | 416 | 104 | Demonstração das regras; preservar sem extrapolar função |
| 4 Radius | 12 | 1504 | 416 | 104 | Demonstrações técnicas vinculadas à norma |
| 5 Canvas e ViewPort | 444 | 196 | 360 | 132 | Medidas do canvas da referência e do ViewPort |
| 6 Cotas do ViewPort | 444 | 376 | 360 | 152 | 360, 336, margens de 12, altura 800, 1:1 |
| 7 Grid e spacing | 444 | 576 | 360 | 112 | Grid 4 px e escala 4/8/12/16/24/32 |
| 8 Tipografia | 444 | 776 | 360 | 152 | Inter técnica do wireframe, não tipografia de marca |
| 9 Paleta temática | 444 | 976 | 360 | 632 | Tokens white §6.5 ou black §6.6 de REGRAS-TECNICAS.md |
| 10 Componentes (medidas) | 820 | 196 | 448 | 848 | **Só os componentes presentes na Tela efetiva**, medidas, rótulos, variantes e AppBar próprios da interface |
| 11 Estados | 820 | 1092 | 448 | 204 | Exemplos técnicos do modelo; não inventar novos estados da Tela |
| 12 Bordas e divisores | 820 | 1344 | 448 | 88 | Amostras técnicas, conforme tema |
| 13 Elevação | 820 | 1480 | 448 | 128 | Demonstrações E0–E3 da referência |
| 14 Observações | 12 | 1696 | 1256 | 208 | **Somente informações técnicas pertinentes à interface/página**, dentro das duas colunas oficiais |

As medidas dos títulos, badges, cards e regiões internas são as dos Wireframe Text oficiais vinculados pela seção 2. Nunca redimensionar regiões para adaptar um conteúdo. Quando Item 10 ou Item 14 não comportar informações obrigatórias, **GI-3 = BLOQUEADO** até decisão formal; criar página de rolagem só quando a própria Tela exigir continuidade real.

## 4. Cabeçalho: estrutura fixa e conteúdo substituível

**Estrutura fixa:** marca, card `x12,y12,w1256,h96`, três regiões MARCA `x12,w156`, IDENTIFICAÇÃO `x168,w384` e METADADOS `x552,w716`, divisores, tipografia e posições. `WIREFRAME`, `PRANCHA TÉCNICA - MODELO C` e a legenda do posicionamento do ViewPort são **texto demonstrativo da referência**, não se tornam obrigatórios nas saídas funcionais.

**Somente na cópia funcional:** omitir `WIREFRAME` e a legenda `(Viewport à esquerda + painel técnico à direita)`; exibir **`PRANCHA TÉCNICA`** como título, no mesmo ponto do título do template, sem reposicionar nada. O `ID` é o ID canônico da ficha; `ETAPA` contém **apenas o nome** da interface (não duplicar ID); `PÁGINA=XX/YY` indica rolagem real; `VERSÃO=vNN` indica revisão da página. DATA, BASELINE, VARIAÇÃO e STATUS correspondem ao artefato e ao Gate comprovado, sem herdar os valores demonstrativos. Valores dos campos individuais são registrados no controle de composição da saída, e não aqui.

**Metadados e medidas fixas:** topo `y=12,h=64`: ID `x552,w164`, PÁGINA `x716,w128`, VERSÃO `x844,w124`, DATA `x968,w140`, STATUS `x1108,w160`; linha inferior `y=76,h=32`: BASELINE `x552,w164`, VARIAÇÃO `x716,w220`, ETAPA `x936,w332`. Estas medidas vêm do Wireframe Text C oficial, seções Cabeçalho, dos dois temas.

## 5. STATUS concreto por tema, sem confusão semântica

- `APROVADO E CONGELADO` somente após comprovar a decisão humana aplicável. Ícone `check_circle` Material Icons Outlined 20 px em `(1120,46)` e texto em `(1146,38)`, largura máxima 114 px, duas linhas, cor **Success** do tema (`white #166534`, `black #A7F3D0`).
- `AGUARDANDO APROVAÇÃO`: ícone `schedule` Material Icons Outlined 20 px na mesma região `(1120,46)`, texto em `(1146,38)` até 114 px, distribuído em duas linhas. Cor do destaque solicitada para a saída funcional: `white Error #991B1B`, `black Error #FCA5A5`. **O estado continua PENDENTE DE APROVAÇÃO, não vira falha funcional.**
- O rótulo `STATUS` permanece na região aprovada; outras situações devem ter fonte normativa específica, sem dedução de cor/ícone.
- Se fonte, texto ou glyph não couberem sem extrapolar `x=1108,w=160`, bloquear GI-3; jamais deslocar campos ou diminuir silenciosamente as fontes do template.

Fonte de tokens: `.specs/wireframes/REGRAS-TECNICAS.md`, tabelas 6.5 e 6.6; fonte de coordenadas/estados históricos: Wireframe Text oficial C white v02 e black v01, sem editá-los. A regra funcional de ícone de espera é um parâmetro autorizado **deste contrato concreto de utilização**, não uma modificação do template congelado.

## 6. Itens 10 e 14: regra concreta de preenchimento

- **Item 10:** representar somente componentes efetivamente usados na Tela em análise, inclusive os estados necessários. A AppBar deve ser cópia fiel da própria Tela, não da amostra do template. Ícones de itens de lista são opcionais caso a ficha e o PNG do item os permitam; nunca copiar automaticamente os exemplos do Modelo C ou de T00.
- **Item 14:** preencher observações específicas da Tela/página, somente as tecnicamente justificadas por ficha, PNG, TextFrame ou comportamento efetivo. Não usar textos demonstrativos genéricos para ocupar espaço.
- As regiões **2–9 e 11–13** permanecem demonstrativas de regras técnicas do Modelo C; sua existência não implica componentes funcionais adicionais. Qualquer alteração de conteúdo além das substituições explicitadas neste contrato exige justificação e autorização específica antes do GI-3.

## 7. Evidências exigidas para utilização

Consultar na ordem: (1) seleção vigente registrada; (2) abrir e conferir as seis fontes da seção 2 por SHA; (3) abrir os respectivos Wireframe Text; (4) conferir este contrato com esses arquivos e a paleta técnica; (5) verificar aprovação GI-1/GI-2 do PNG/WT funcional; (6) montar uma **nova** Prancha; (7) validar ViewPort pixel a pixel; (8) preencher somente campos permitidos; (9) registrar decisão GI-3/GI-4 por tema e versão.

O conjunto histórico V1, as pranchas individuais e os contratos do padrão visual funcional **não selecionam** o template. A falta de qualquer fonte ou parâmetro técnico indispensável bloqueia a composição. O contrato está ligado **aos hashes da seção 2**, e não ao mero nome `Modelo C`.
