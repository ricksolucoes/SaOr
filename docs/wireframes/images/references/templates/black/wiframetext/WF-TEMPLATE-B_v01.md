# WF-TEMPLATE-B_v01 — Reprodução textual fiel da prancha final

```text
CANVAS FINAL — 1280 × 1920 px

┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│SaOr                │WIREFRAME                                       │ID                │PÁGINA       │VERSÃO      │DATA            │STATUS                       │
│Sales Order         │PRANCHA TÉCNICA - MODELO B                      │WF-TEMPLATE-B     │XX / YY   │v01       │DD/MM/AAAA    │[✓] APROVADO E CONGELADO            │
│                    │(Viewport à esquerda + painel técnico à direita)│BASELINE v1.0     │VARIAÇÃO black              │ETAPA Wireframe Conceitual em Imagem        │
├──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│┌ VIEWPORT TÉCNICO 360 x 800 px                ┐  ┌ 1. CANVAS E VIEWPORT                           ┐  ┌ 2. COTAS DO VIEWPORT                                     ┐│
││                    360 px                    │  │  Canvas da prancha      1280 x 1920 px         │  │  Largura total           360 px                          ││
││            12 px | 336 px | 12 px            │  │  Viewport (interface)    360 x 800 px          │  │  Largura útil            336 px                          ││
││                                              │  │  Escala do viewport      1:1                   │  │  Margem esquerda          12 px                          ││
││                                              │  │  Orientação              Retrato               │  │  Margem direita           12 px                          ││
││       ┌────────────────────────────────┐     │  │  Margem horizontal       12 px                 │  │  Altura total            800 px                          ││
││       │  O  Título da Página  [S][M]   │     │  │                                                │  │  Escala                   1:1                            ││
││       │     Subtítulo da página        │     │  └────────────────────────────────────────────────┘  └──────────────────────────────────────────────────────────┘│
││       ├────────────────────────────────┤     │                                                                                                                  │
││       │ Seção de Conteúdo              │     │  ┌ 3. GRID E SPACING                              ┐  ┌ 4. COMPONENTES (MEDIDAS)                                 ┐│
││       │                                │     │  │  Grid base               4 px                  │  │  APP BAR (56 px)                                         ││
││       │ Rótulo do campo                │     │  │  Escala                  4 / 8 / 12 / 16 / 24 /│  │    ┌──────────────────────────────────────────────┐      ││
││       │ ┌────────────────────────┐     │     │  │  Padding-base horizontal 16 px                 │  │    │ [MENU]  Título                    [SEARCH]   │      ││
││       │ │ Texto de exemplo    v  │     │     │  │  Padding-base vertical   12 px                 │  │    └──────────────────────────────────────────────┘      ││
││       │ └────────────────────────┘     │     │  │                                                │  │                                                          ││
││       │ ┌────────────────────────┐     │     │  │                                                │  │  CAMPO OUTLINED (56 px)                                  ││
││       │ │    Botão Primário      │     │     │  └────────────────────────────────────────────────┘  │  Rótulo                                                  ││
││       │ └────────────────────────┘     │     │                                                      │    ┌──────────────────────────────────────────────┐      ││
││       │ ┌────────────────────────┐     │     │  ┌ 5. TIPOGRAFIA (Inter - Wireframe)              ┐  │    │ Texto de exemplo                        v    │      ││
││       │ │   Botão Secundário     │     │     │  │  WF-TITLE        20 px | 28 px | SemiBold 600  │  │    └──────────────────────────────────────────────┘      ││
││       │ └────────────────────────┘     │     │  │  WF-SECTION      14 px | 20 px | SemiBold 600  │  │                                                          ││
││       │                                │     │  │  WF-BODY         16 px | 24 px | Regular 400   │  │  BOTÃO PRIMÁRIO (48 px)                                  ││
││       │       Botão Texto    [G]       │     │  │  WF-LABEL        14 px | 20 px | Medium 500    │  │    ┌──────────────────────────────────────────────┐      ││
││       ├────────────────────────────────┤     │  │  WF-ACTION-TEXT  16 px | 24 px | Medium 500    │  │    │               Botão Primário                 │      ││
││       │ O  Título do item       >      │     │  │  WF-CAPTION      12 px | 16 px | Regular 400   │  │    └──────────────────────────────────────────────┘      ││
││       │    Texto secundário            │     │  │                                                │  │                                                          ││
││       │ ┌────────────────────────┐     │     │  │                                                │  │  BOTÃO SECUNDÁRIO (48 px)                                ││
││       │ │ Título do Card         │     │     │  └────────────────────────────────────────────────┘  │    ┌──────────────────────────────────────────────┐      ││
││       │ │ Texto de exemplo do    │     │     │                                                      │    │                Botão Secundário              │      ││
││       │ │ card com informações.  │     │     │  ┌ 6. PALETA TÉCNICA - ESCURO                     ┐  │    └──────────────────────────────────────────────┘      ││
││       │ └────────────────────────┘     │     │  │ WF-B-BG                                        │  │                                                          ││
││       │ [i] Mensagem informativa       │     │  │ WF-B-SURFACE                                   │  │  BOTÃO TEXTO (mínimo 48 px) + ICON BUTTON (48 x 48 px)   ││
││       │     de exemplo.                │     │  │ WF-B-SURFACE-ALT                               │  │    ┌──────┐                                              ││
││       │ ┌────────────────────────┐     │     │  │ WF-B-BORDER                                    │  │    │ [G]  │  Botão Texto                                 ││
││       │ │           ^            │     │     │  │ WF-B-BORDER-CONTROL                            │  │    └──────┘                                              ││
││       │ │ Área de conteúdo       │     │     │  │ WF-B-TEXT                                      │  │                                                          ││
││       │ │ indicando scroll       │     │     │  │ WF-B-TEXT-2                                    │  │                                                          ││
││       │ │ vertical               │     │     │  │ WF-B-ACTION                                    │  │                                                          ││
││       │ │           v            │     │     │  │ WF-B-DISABLED                                  │  │                                                          ││
││       │ └────────────────────────┘     │     │  │ WF-B-FOCUS                                     │  │  ITEM DE LISTA - simples (56 px)                         ││
││       ├────────────────────────────────┤     │  │ WF-B-STATUS                                    │  │    ┌──────────────────────────────────────────────┐      ││
││       │ Início Pedidos Clientes Mais   │     │  │ ────────────────────────────────────────────── │  │    │ O  Título do item                       >    │      ││
││       ├────────────────────────────────┤     │  │ Primary                                        │  │    └──────────────────────────────────────────────┘      ││
││       │                                │     │  │ On Primary                                     │  │                                                          ││
││       └────────────────────────────────┘     │  │ Secondary                                      │  │  ITEM DE LISTA - secundário (64 px)                      ││
││                                              │  │ Info                                           │  │    ┌──────────────────────────────────────────────┐      ││
││  cota vertical 800 px (à direita do bitmap)  │  │ Error                                          │  │    │ O  Título do item                       >    │      ││
││   texto na vertical: 800 px (viewport total) │  │ Success                                        │  │    │    Texto secundário adicional                │      ││
││                                              │  │ Warning (texto/ícone)                          │  │    └──────────────────────────────────────────────┘      ││
││                                              │  │ Warning (preenchimento)                        │  │                                                          ││
││                                              │  │ On Warning                                     │  │  CARD (radius 16 px)                                     ││
││                                              │  │ Info BG                                        │  │    ┌──────────────────────────────────────────────┐      ││
││                                              │  │ ────────────────────────────────────────────── │  │    │ Título do Card                               │      ││
│└──────────────────────────────────────────────┘  │ BRAND                                          │  │    │ Texto de exemplo do card.                    │      ││
│                                                  │ On Brand                                       │  │    └──────────────────────────────────────────────┘      ││
│┌ 7. ELEVAÇÃO                                  ┐  │ Zebra de tabela                                │  │                                                          ││
││                                              │  │                                                │  │  MODAL / DIALOG (margem lateral 24 px)                   ││
││          ┌────────┐        ┌────────┐        │  │                                                │  │    ┌──────────────────────────────────────────────┐      ││
││          │   E0   │        │   E1   │        │  │                                                │  │    │                  -----                       │      ││
││          └────────┘        └────────┘        │  │                                                │  │    │ Título do Modal                              │      ││
││           0/0/0/0%          0/1/2/12%        │  │                                                │  │    │ Texto de exemplo do modal.                   │      ││
││                                              │  │                                                │  │    │ [ Cancelar ]              [ Confirmar ]      │      ││
││          ┌────────┐        ┌────────┐        │  │                                                │  │    └──────────────────────────────────────────────┘      ││
││          │   E2   │        │   E3   │        │  │                                                │  │                                                          ││
││          └────────┘        └────────┘        │  │                                                │  │  BOTTOM NAVIGATION (64 px)                               ││
││           0/2/6/16%        0/4/12/20%        │  │                                                │  │    ┌──────────────────────────────────────────────┐      ││
││                                              │  │                                                │  │    │ Início | Pedidos | Clientes | Mais           │      ││
││                                              │  │                                                │  │    └──────────────────────────────────────────────┘      ││
││                                              │  │                                                │  │  Somente quando previsto na baseline.                    ││
│└──────────────────────────────────────────────┘  └────────────────────────────────────────────────┘  └──────────────────────────────────────────────────────────┘│
├──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│┌ 8. RADIUS                            ┐  ┌ 9. ÍCONES (Material Icons Outlined)  ┐  ┌ 10. ESTADOS (Componentes)   Hover: documentado; não obrigatório em mobile. ┐│
││                                      │  │                                      │  │  ┌──────────────────────────────────────────────┐                          ││
││  ┌────────────┐    ┌────────────┐    │  │  ┌────────────┐    ┌────────────┐    │  │  │ Default                                      │                          ││
││  │   12 px    │    │   16 px    │    │  │  │   20 px    │    │   24 px    │    │  │  ├──────────────────────────────────────────────┤                          ││
││  └────────────┘    └────────────┘    │  │  │ [AUXILIAR] │    │[AÇÃO / NAV]│    │  │  │ Focus                                        │                          ││
││  Campos e botões   Cards e modais    │  │  └────────────┘    └────────────┘    │  │  ├──────────────────────────────────────────────┤                          ││
││                                      │  │  Ícones auxiliares Ação / navegação  │  │  │ Pressed / Selected                           │                          ││
││                                      │  │                                      │  │  ├──────────────────────────────────────────────┤                          ││
││                                      │  │  Material Icons Outlined:            │  │  │ Disabled                                     │                          ││
││                                      │  │  referência conceitual.              │  │  ├──────────────────────────────────────────────┤                          ││
││                                      │  │                                      │  │  │ Error                                        │                          ││
││                                      │  │                                      │  │  └──────────────────────────────────────────────┘                          ││
││                                      │  │                                      │  │                                                                            ││
││                                      │  │                                      │  │                                                                            ││
│└──────────────────────────────────────┘  └──────────────────────────────────────┘  └────────────────────────────────────────────────────────────────────────────┘│
├──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│┌ 11. REGRAS GERAIS DE COMPONENTES                                                                 ┐  ┌ BORDAS E DIVISORES                                       ┐│
││  Touch target mínimo: 48 x 48 px.                                                                │  │  ┌────────────────────┐  ─────────────────────           ││
││  Aplicável a botões, ícones, itens de lista, navegação                                           │  │  │ Borda de controle  │  Divisor 1 px                    ││
││  e demais áreas interativas.                                                                     │  │  └────────────────────┘                                  ││
││  A área clicável deve respeitar o mínimo mesmo quando                                            │  │  Tokens: WF-B-BORDER-CONTROL | WF-B-BORDER               ││
││  o elemento visual for menor.                                                                    │  │  Uso entre seções e listas quando necessário.            ││
││                                                                                                  │  │                                                          ││
││                                                                                                  │  │                                                          ││
│└──────────────────────────────────────────────────────────────────────────────────────────────────┘  └──────────────────────────────────────────────────────────┘│
├──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│┌ 12. OBSERVAÇÕES TÉCNICAS                                                                                                                                       ┐│
││  1. O viewport representa a tela completa do celular: 360 x 800 px em escala 1:1.                                                                              ││
││  2. Cotas vigentes: largura total 360 px, largura útil 336 px, margens laterais 12 + 12 px e altura total 800 px.                                              ││
││  3. Não existe reserva fixa de faixa superior ou inferior de safe area nesta etapa.                                                                            ││
││  4. Todos os elementos seguem grid e escala de espaçamento conforme REGRAS-TECNICAS.md.                                                                        ││
││  5. Inter é tipografia técnica do wireframe e não tipografia oficial da marca SaOr.                                                                            ││
││  6. Em páginas seguintes, repetir apenas elementos realmente persistentes.                                                                                     ││
││  7. Nomenclatura dos arquivos funcionais: <ID>-<PÁGINA>-<TOTAL>_v<VERSÃO>.png.                                                                                 ││
││  8. Interface multipágina só é aprovada quando todas as páginas Claro e Escuro estiverem aprovadas.                                                            ││
││  9. Cores, ícones e componentes seguem as specs canônicas de wireframe.                                                                                        ││
││  10. Cor nunca deve ser o único indicador de estado.                                                                                                           ││
│└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘│
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

# Especificação de implementação da prancha

## 1. Regra de leitura deste documento

A reprodução textual apresentada no início deste arquivo é a **referência conceitual de composição** da `WF-TEMPLATE-B_v01`.

Ela define:

```text
- ordem visual das regiões;
- relação relativa entre viewport e documentação;
- quais blocos existem nesta prancha-modelo;
- quais blocos ficam lado a lado;
- quais blocos ficam abaixo de outros;
- hierarquia geral da composição.
```

Ela **não deve ser interpretada como escala matemática de caracteres para pixels**.

As medidas em pixels registradas nas seções seguintes foram recalculadas para esta prancha-modelo usando:

```text
canvas vigente:          1280 × 1920 px
margem estrutural:       12 px
grid base:                4 px
escala de spacing:        4 / 8 / 12 / 16 / 24 / 32 px
viewport físico:          360 × 800 px
escala do viewport:       1:1
conteúdo real de cada bloco desta prancha-modelo
```

As coordenadas, larguras e alturas abaixo são **específicas desta prancha-modelo B_v01**.

Elas não são medidas universais dos futuros wireframes funcionais T/M/E.

Ao reutilizar o conceito desta composição em outra prancha, deve-se recalcular as áreas documentais conforme o conteúdo real daquela prancha, preservando as regras técnicas normativas.

### 1.1 Origem e diferenças em relação ao white (WIREFRAME-TEXT.md 7.1)

Origem (WIREFRAME-TEXT.md, 7.1):

```text
Wireframe Text white de origem: WF-TEMPLATE-B_v02 (docs/wireframes/images/references/templates/white/wiframetext/)
Estado do white de origem:      Wireframe Text APROVADO E CONGELADO (Gates 1 a 6, Gates 2, 3 e 6 aprovados pelo responsável em 27/10/2026); PNG da origem e STATUS do cabeçalho APROVADO E CONGELADO em 27/10/2026
Regra: geometria e composição herdadas; mudam apenas paleta, ativos físicos e as decisões que dependem da paleta.
Geometria herdada continua GEOMETRIA DESTA PRANCHA (não passa a regra normativa).
Gates não herdados: o black registra os próprios estados (seção 3); Gates 2, 3 e 6 foram aprovados pelo responsável em 27/10/2026.
Numeração própria: esta é a v01 da variação black.
```

O WIREFRAME-TEXT.md 7.1 prevê a origem `APROVADO E CONGELADO`: o Wireframe Text white de origem está `APROVADO E CONGELADO`; o PNG da origem também está `APROVADO E CONGELADO`. Os estados do black são próprios e a aprovação do white não aprova este documento.

Diferenças em relação ao white de origem (todas DIFERENÇA INTENCIONAL; aprovadas nos Gates 2, 3 e 6 em 27/10/2026):

```text
D1 — Paleta: tokens WF-B-* e semânticas da tabela 6.6 de REGRAS-TECNICAS.md no lugar de WF-W-* e da tabela 6.5; HEX somente no bloco 6.
D2 — Viewport: references/black/WF-VIEWPORT-360x800.png (360 × 800 px, 1:1) no lugar do bitmap white.
D3 — Pares texto/fundo: razões recalculadas para a paleta escura (tabela 6.6); não há exceção de nível (todos os pares de texto em AAA).
D4 — Ícone do cabeçalho: assets/logo/saor-icon-para_fundos_escuros.png (variante preparada para fundos escuros; sem inversão manual nem filtro) no lugar de saor-icon-master.svg; ícone 44 × 44 em (24, 38), com o mesmo centro vertical do white; SaOr e SALES ORDER em BRAND (paleta escura). O ícone consta do PNG white B aprovado e não estava documentado no Wireframe Text (correção registrada em 27/10/2026).
D5 — Elevação (amostras E0 a E3): parâmetros de sombra inalterados (REGRAS-TECNICAS.md); sobre superfície escura a sombra rgba(0,0,0,·) é pouco perceptível. As quatro amostras usam WF-B-SURFACE-ALT (token existente, mais claro que o card WF-B-SURFACE) como preenchimento, conforme a regra de REGRAS-TECNICAS.md, seção 8 (variação black); o nível é identificado pela legenda e pela sombra.
```

Todo o resto (composição, geometria, conteúdo textual, tipografia, componentes, ícones e regras específicas) é o da origem.

---

## 2. Hierarquia de autoridade

Para esta prancha, a ordem de autoridade é:

```text
1. docs/Documento_Mestre.md — somente conteúdo e comportamento funcional quando aplicável
2. .specs/wireframes/REGRAS-TECNICAS.md — invariantes técnicos
3. .specs/wireframes/PROCESSO-PRANCHA.md — sequência e gates
4. .specs/wireframes/WIREFRAME-TEXT.md — contrato documental
5. docs/wireframes/images/README.md — estrutura operacional e separação `white` / `black`
6. este WF-TEMPLATE-B_v01.md — composição específica desta alternativa
7. PNG correspondente — resultado visual, nunca fonte normativa superior
```

Nenhuma prancha histórica ou alternativa anterior é referência de geometria, proporção, posicionamento ou distribuição desta alternativa B.

### Estado dos gates desta B_v01 (black)

```text
Gate 1 — Canvas:                       APROVADO E CONGELADO
Gate 2 — Título / Cabeçalho:           APROVADO E CONGELADO
Gate 3 — Viewport Técnico:             APROVADO E CONGELADO
Gate 4 — Área restante calculada:      APROVADO E CONGELADO
Gate 5 — Demais elementos definidos:   APROVADO E CONGELADO
Gate 6 — Wireframe Text completo:      APROVADO E CONGELADO
Produção do PNG:                       APROVADO E CONGELADO
STATUS no cabeçalho:                   APROVADO E CONGELADO
```

Esta v01 é a primeira versão da variação black e os estados acima são próprios (não herdados da origem white).

Registros:

```text
Gate 1 (técnico): canvas 1280 × 1920 px conforme REGRAS-TECNICAS.md — APROVADO E CONGELADO.
Gate 2: cabeçalho da v01 black, tokens da seção 6 (tabela 6.6) e STATUS (inclui D4) — aprovado em 27/10/2026 e reaberto na mesma data pela correção de D4 e do bloco Marca (ícone do cabeçalho, conforme o PNG white B aprovado; decisão do responsável) — aprovado novamente pelo responsável em 27/10/2026 (aprovação da imagem, resposta registrada na conversa) — APROVADO E CONGELADO.
Gate 3: bitmap references/black/WF-VIEWPORT-360x800.png aprovado em 27/10/2026; posição, cotas e registro do gate aprovados explicitamente pelo responsável em 27/10/2026 (resposta registrada na conversa) — APROVADO E CONGELADO.
Gates 4 e 5 (técnicos): revalidados em 27/10/2026 depois dos Gates 2 e 3 estarem congelados (geometria inalterada pela correção de D4) — APROVADO E CONGELADO.
Gate 6: aprovado em 27/10/2026, reaberto pela correção de D4 e aprovado novamente pelo responsável em 27/10/2026 (aprovação da imagem, resposta registrada na conversa) — APROVADO E CONGELADO.
Produção do PNG: gerado em 27/10/2026 a partir deste Wireframe Text, validado contra ele e aprovado explicitamente pelo responsável em 27/10/2026 (resposta registrada na conversa) — APROVADO E CONGELADO.
STATUS no cabeçalho: registrado como APROVADO E CONGELADO em 27/10/2026; o PNG foi regenerado com o STATUS aprovado (ícone check_circle e texto em Success) e revalidado.
Validação técnica dos Gates 4 e 5:
Validação técnica dos Gates 4 e 5:
  - fechamento horizontal do cabeçalho: 156 + 384 + 716 = 1256 px;
  - fechamento horizontal do corpo principal: 416 + 16 + 360 + 16 + 448 = 1256 px;
  - viewport: 12 + 336 + 12 = 360 px;
  - fechamento vertical do corpo principal: coluna do viewport 132 + 908 + 16 + 180 = 1236; coluna central 132 + 144 + 16 + 112 + 16 + 152 + 16 + 648 = 1236;
    coluna direita 132 + 144 + 16 + 944 = 1236;
  - fechamento horizontal da linha inferior 8 | 9 | 10: 328 + 16 + 328 + 16 + 568 = 1256 px;
  - região inferior: 1260 + 208 + 16 + 144 + 16 + 264 = 1908 (limite inferior do canvas);
  - todas as áreas x/y/w/h permanecem dentro do canvas 1280 × 1920 px.
Cores: as lacunas da seção 6 (marcadas com *) foram aprovadas pelo responsável em 27/10/2026 (comunicado na conversa);
  o registro formal em REGRAS-TECNICAS.md 6.7 é feito pelo responsável.
```

As geometrias documentadas abaixo são desta `B_v01` (black) e foram aprovadas nos Gates 2, 3 e 6 em 27/10/2026.

### Cores usadas e pares texto/fundo

As cores desta prancha são citadas pelo nome do token. O HEX consta somente no bloco 6. Cromia adicional: BRAND, On Brand e Zebra de tabela (esta última registrada na paleta; esta prancha não usa linhas zebradas). Semânticas usadas: Primary, On Primary, Info BG, Error, Success.

Pares texto/fundo usados (razões da tabela 6.6 de `REGRAS-TECNICAS.md`):

| Par | Razão | Nível |
|---|---:|---|
| WF-B-TEXT sobre WF-B-SURFACE | 14,89:1 | AAA |
| WF-B-TEXT-2 sobre WF-B-SURFACE | 9,36:1 | AAA |
| Primary sobre WF-B-SURFACE | 8,65:1 | AAA |
| On Primary sobre Primary | 9,80:1 | AAA |
| Info sobre Info BG | 7,10:1 | AAA |
| Error sobre WF-B-SURFACE | 8,78:1 | AAA |
| Success sobre WF-B-SURFACE | 13,00:1 | AAA |
| Warning (texto/ícone) sobre WF-B-SURFACE | 13,39:1 | AAA |
| On Warning sobre Warning (preenchimento) | 15,17:1 | AAA |
| On Brand sobre BRAND | 16,73:1 | AAA |
| WF-B-TEXT sobre Zebra de tabela | 13,34:1 | AAA |
| WF-B-BORDER-CONTROL sobre WF-B-SURFACE (borda de campo, botão secundário, icon button) | 3,52:1 | OK (≥ 3:1) |
| WF-B-FOCUS sobre WF-B-SURFACE (foco) | 10,81:1 | OK (≥ 3:1) |
| WF-B-TEXT sobre WF-B-SURFACE-ALT (amostras de elevação) | 12,82:1 | AAA |
| WF-B-TEXT-2 sobre WF-B-SURFACE-ALT (legenda e amostras) | 8,06:1 | AAA |

Sem exceção de nível nos pares acima (todos AAA); a seção 6.6 registra os demais pares.

---

## 3. Canvas da prancha

```text
canvas:       1280 × 1920 px
orientação:   retrato
margem externa estrutural: 12 px
```

Área útil entre as margens:

```text
x: 12 px
y: 12 px
w: 1256 px
h: 1896 px
```

Limites:

```text
esquerda: 12 px
direita: 1268 px
topo: 12 px
base: 1908 px
```

---

# Cabeçalho

## Área

```text
x: 12 px
y: 12 px
w: 1256 px
h: 96 px

limite direito: 1268 px
limite inferior: 108 px
```

A altura de `96 px` foi definida para acomodar, nesta prancha-modelo:

```text
- marca;
- identificação da prancha em três linhas;
- metadados superiores;
- metadados inferiores;
- divisores internos;
- padding técnico.
```

## Estrutura horizontal

A proporção é herdada da origem white (WF-TEMPLATE-B_v02).

```text
MARCA
x: 12
y: 12
w: 156
h: 96

IDENTIFICAÇÃO DA PRANCHA
x: 168
y: 12
w: 384
h: 96

METADADOS
x: 552
y: 12
w: 716
h: 96
```

Relação:

```text
156 + 384 + 716 = 1256
```

## Marca

Conteúdo:

```text
SaOr
Sales Order
```

Área:

```text
x: 12
y: 12
w: 156
h: 96
```

Disposição:

```text
padding horizontal: 16 px
alinhamento: esquerda
alinhamento vertical do conjunto: centro
```

Ícone: assets/logo/saor-icon-para_fundos_escuros.png, x 24, y 38, 44 × 44 (proporção original do arquivo; D4).
Textos: "SaOr" em x 76, y 34 (30/34); "SALES ORDER" em x 77, y 70 (10/14, tracking 0.14em).
Cor: SaOr e SALES ORDER em BRAND.

Referências:

```text
assets/logo/README.md
assets/fonts/logo/README.md
```

Aplicação tipográfica:

```text
SaOr:
Google Sans Bold 700

SALES ORDER:
Quicksand Regular 400
uppercase
tracking ampliado
```

Inter não substitui a tipografia oficial da marca.

## Identificação da prancha

Área:

```text
x: 168
y: 12
w: 384
h: 96
```

Conteúdo exato:

```text
WIREFRAME
PRANCHA TÉCNICA - MODELO B
(Viewport à esquerda + painel técnico à direita)
```

Disposição:

```text
padding horizontal: 24 px
alinhamento: esquerda
ordem vertical: 3 linhas
```

## Metadados

Área:

```text
x: 552
y: 12
w: 716
h: 96
```

### Linha superior

```text
y: 12
h: 64
```

Células:

```text
ID
x: 552
w: 164

PÁGINA
x: 716
w: 128

VERSÃO
x: 844
w: 124

DATA
x: 968
w: 140

STATUS
x: 1108
w: 160
```

Conteúdo:

```text
ID
WF-TEMPLATE-B

PÁGINA
XX / YY

VERSÃO
v01

DATA
DD/MM/AAAA

STATUS
APROVADO E CONGELADO
```

### Linha inferior

```text
y: 76
h: 32
```

Células:

```text
BASELINE
x: 552
w: 164

VARIAÇÃO
x: 716
w: 220

ETAPA
x: 936
w: 332
```

Conteúdo:

```text
BASELINE
v1.0

VARIAÇÃO
black

ETAPA
Wireframe Conceitual em Imagem
```

Cor do valor de STATUS: estado atual APROVADO E CONGELADO — Success, com o ícone check_circle 20 px em (1120, 46) e valor em (1146, 38), 2 linhas "APROVADO E / CONGELADO"; enquanto AGUARDANDO APROVAÇÃO (regra de estado, não aplicável a esta versão congelada) — WF-B-TEXT-2, sem ícone, 2 linhas "AGUARDANDO / APROVAÇÃO" em (1120, 38/54). Fundo do campo: WF-B-SURFACE.

---

# Viewport

## Papel na composição

O viewport é o primeiro elemento estrutural montado após o cabeçalho.

Ele deve ser inserido fisicamente antes do cálculo final das áreas documentais.

Arquivo obrigatório:

```text
docs/wireframes/images/references/black/WF-VIEWPORT-360x800.png
```

Este é o bitmap black gerado em 27/10/2026 com a paleta da seção 6 de `REGRAS-TECNICAS.md` (Icon Button à esquerda do Botão Texto). Nenhum bitmap da variação white é usado nesta prancha. O registro do arquivo em `REGRAS-TECNICAS.md` (seção 3.1) é pendência do responsável.

Dimensão obrigatória:

```text
360 × 800 px
```

Uso:

```text
escala de inserção: 100%
escala na prancha: 1:1
```

É proibido:

```text
- redimensionar;
- ampliar;
- reduzir;
- esticar;
- comprimir;
- recortar;
- reproporcionar;
- reconstruir;
- redesenhar;
- adaptar o bitmap para caber em outro bloco.
```

## Área documental do conjunto do viewport nesta prancha-modelo

```text
x: 12 px
y: 132 px
w: 416 px
h: 908 px

limite direito: 428 px
limite inferior: 1040 px
```

O afastamento entre cabeçalho e corpo principal é:

```text
108 → fim do cabeçalho
132 → início do corpo principal

gap = 24 px
```

Esse `24 px` é **spacing documental da prancha**.
Não é safe area.

## Posição física do bitmap

O bitmap é centralizado horizontalmente na coluna esquerda:

```text
x: 40 px
y: 224 px
w: 360 px
h: 800 px

limite direito: 400 px
limite inferior: 1024 px
```

Cálculo horizontal:

```text
largura da coluna: 416 px
largura do bitmap: 360 px
sobra: 56 px
56 / 2 = 28 px

12 + 28 = x 40
```

## Cotas externas do viewport

Referência:

```text
docs/wireframes/images/references/white/
Especificação Técnica do Viewport Mobile.png
(referência dimensional existente somente na pasta white: consultada apenas pelas medidas, não é inserida na prancha black e não há equivalente black)
```

A referência vigente documenta:

```text
largura total:             360 px
largura útil:              336 px
margem esquerda:            12 px
margem direita:             12 px
altura total:              800 px
```

Relação horizontal:

```text
12 + 336 + 12 = 360
```

Não existe reserva fixa de safe area superior ou inferior.

## Posições das cotas nesta prancha-modelo

Cotas em Primary, linha de 1 px, setas de 5 px, rótulos WF-CAPTION 600 com fundo WF-B-SURFACE (padding horizontal 6 px).

```text
TÍTULO DO BLOCO
y: 144–164 px

Linhas de extensão tracejadas (2/2):
  x: 40 e x: 399, de y: 180 a y: 224
  x: 52 e x: 387, de y: 206 a y: 224

COTA 360 px
linha: y: 186, x: 40–399, setas nas pontas
rótulo "360 px (viewport total)": centrado em x: 220, y: 178

COTA 12 / 336 / 12
linha: y: 210, x: 40–399, setas nas pontas; marcas de divisão em x: 52 e x: 387 (y: 206–215)
rótulo "336 px (largura útil)": centrado em x: 220, y: 202
rótulos "12 px" (11 px, 600): x: 13 (w: 26, alinhado à direita) e x: 401 (w: 26, alinhado à esquerda), y: 202

COTA 800 px (vertical, à direita do bitmap)
extensões horizontais tracejadas: x: 400–424 em y: 224 e em y: 1023
linha vertical: x: 414, de y: 225 a y: 1023, setas nas pontas
rótulo "800 px (viewport total)": na vertical (lê-se de baixo para cima), sobre a linha, centrado em x: 415, y: 624

BITMAP
y: 224–1024 px
```

Não há texto de cota abaixo do bitmap. O cartão termina em y = 1040 (16 px abaixo do bitmap); em y = 1056 começa o bloco 7 (ELEVAÇÃO).

---

# Mapa geométrico principal da B_v01

Depois de posicionados cabeçalho e viewport, a região principal restante é recalculada.

## Colunas do corpo principal

```text
COLUNA DO VIEWPORT
x: 12
w: 416

GAP
x: 428
w: 16

COLUNA CENTRAL
x: 444
w: 360

GAP
x: 804
w: 16

COLUNA DIREITA
x: 820
w: 448
```

Verificação:

```text
416 + 16 + 360 + 16 + 448 = 1256
```

Corpo principal:

```text
y: 132
h: 1104
base: 1236
```

## Faixa superior do corpo principal

```text
1. CANVAS E VIEWPORT
x: 444
y: 132
w: 360
h: 144

2. COTAS DO VIEWPORT
x: 820
y: 132
w: 448
h: 144
```

Gap vertical:

```text
16 px
```

## Coluna do viewport

```text
VIEWPORT TÉCNICO 360 x 800 px
x: 12
y: 132
w: 416
h: 908          (base 1040)

7. ELEVAÇÃO
x: 12
y: 1056
w: 416
h: 180          (base 1236)
```

## Coluna central abaixo da faixa superior

```text
3. GRID E SPACING
x: 444
y: 292
w: 360
h: 112

5. TIPOGRAFIA
x: 444
y: 420
w: 360
h: 152

6. PALETA
x: 444
y: 588
w: 360
h: 648          (base 1236)
```

Entre esses cartões:

```text
gap vertical: 16 px
```

## Coluna direita

```text
4. COMPONENTES (MEDIDAS)
x: 820
y: 292
w: 448
h: 944          (base 1236)
```

Base comum:

```text
coluna do viewport (bloco 7), coluna central (bloco 6) e coluna direita (bloco 4) terminam em y = 1236
```

---

# 1. CANVAS E VIEWPORT

## Área desta prancha-modelo

```text
x: 444 px
y: 132 px
w: 360 px
h: 144 px
```

## Conteúdo exato

```text
1. CANVAS E VIEWPORT

Canvas da prancha      1280 × 1920 px
Viewport (interface)    360 × 800 px
Escala do viewport      1:1
Orientação              Retrato
Margem horizontal       12 px
```

## Disposição interna

```text
padding horizontal: 16 px
padding vertical: 12 px

título:
x: 460
y: 144
h: 20

conteúdo:
x: 460
y: 176
w: 328
```

Rótulos e valores ficam em duas colunas internas.

Referências:

```text
.specs/wireframes/REGRAS-TECNICAS.md
2 — Canvas
3 — Viewport
4 — Grid e spacing
```

---

# 2. COTAS DO VIEWPORT

## Área desta prancha-modelo

```text
x: 820 px
y: 132 px
w: 448 px
h: 144 px
```

## Conteúdo exato

```text
2. COTAS DO VIEWPORT

Largura total           360 px
Largura útil            336 px
Margem esquerda          12 px
Margem direita           12 px
Altura total            800 px
Escala                   1:1
```

## Disposição interna

```text
padding horizontal: 16 px
padding vertical: 12 px

título:
x: 836
y: 144
w: 416
h: 20

conteúdo:
x: 836
y: 176
w: 416
line-height: 16 px
```

Referências:

```text
.specs/wireframes/REGRAS-TECNICAS.md
3 — Viewport
3.2 — Cotas
3.3 — Safe area

docs/wireframes/images/references/white/
Especificação Técnica do Viewport Mobile.png
(referência dimensional existente somente na pasta white: consultada apenas pelas medidas, não é inserida na prancha black e não há equivalente black)
```

---

# 3. GRID E SPACING

## Área

```text
x: 444 px
y: 292 px
w: 360 px
h: 112 px
```

## Conteúdo exato

```text
3. GRID E SPACING

Grid base               4 px
Escala                  4 / 8 / 12 / 16 / 24 / 32 px
Padding-base horizontal 16 px
Padding-base vertical   12 px
```

## Disposição

```text
padding horizontal: 16 px
padding vertical: 12 px

título:
x: 460
y: 304
h: 20

conteúdo:
x: 460
y: 336
w: 328
```

Referência:

```text
.specs/wireframes/REGRAS-TECNICAS.md
4 — Grid e spacing
```

---

# 4. COMPONENTES (MEDIDAS)

## Área

```text
x: 820 px
y: 292 px
w: 448 px
h: 944 px
```

Área interna:

```text
x: 836 px
w: 416 px
```

O conteúdo é demonstrativo.
As medidas dos componentes vêm de `.specs/wireframes/REGRAS-TECNICAS.md`; a área deste cartão é específica desta prancha-modelo.

## Distribuição vertical

Passo entre componentes: o intervalo entre a base de um componente e o rótulo do seguinte é 8 px maior que na v01 (4.1 permanece em y 336; 4.2 desce 8 px; 4.3, 16 px; e assim por diante até 4.10, 72 px; a observação desce 80 px).

### 4.1 App Bar

```text
rótulo:
x: 836
y: 336
h: 16

amostra:
x: 836
y: 352
w: 416
h: 56
```

Conteúdo:

```text
[MENU]  Título                         [SEARCH]
```

### 4.2 Campo Outlined

```text
rótulo:
y: 420
h: 16

amostra:
x: 836
y: 436
w: 416
h: 56
borda: 1 px WF-B-BORDER-CONTROL
```

Conteúdo:

```text
Rótulo
Texto de exemplo                              v
```

### 4.3 Botão Primário

```text
rótulo:
y: 504
h: 16

amostra:
x: 836
y: 520
w: 416
h: 48
fundo: Primary; texto: On Primary
```

Texto:

```text
Botão Primário
```

### 4.4 Botão Secundário

```text
rótulo:
y: 580
h: 16

amostra:
x: 836
y: 596
w: 416
h: 48
fundo: WF-B-SURFACE; borda: 1 px WF-B-BORDER-CONTROL
```

Texto:

```text
Botão Secundário
```

### 4.5 Botão Texto + Icon Button

```text
rótulo:
y: 656
h: 16

faixa de demonstração:
x: 836
y: 672
w: 416
h: 48
```

Distribuição (Icon Button à esquerda, Botão Texto colado a ele):

```text
Icon Button:
x: 836
y: 672
w: 48
h: 48
radius: 12, borda 1 px WF-B-BORDER-CONTROL
ícone settings 24 px em (848, 684)

Botão Texto:
x: 900
y: 684 (texto WF-ACTION-TEXT, Primary, alinhado à esquerda)
h: 48 (altura mínima da faixa)

gap: 16 px
```

### 4.6 Item de Lista — simples

```text
rótulo:
y: 732

amostra:
x: 836
y: 748
w: 416
h: 56
```

### 4.7 Item de Lista — secundário

```text
rótulo:
y: 816

amostra:
x: 836
y: 832
w: 416
h: 64
```

### 4.8 Card

```text
rótulo:
y: 908

amostra:
x: 836
y: 924
w: 416
h: 64
```

Conteúdo:

```text
Título do Card
Texto de exemplo do card.
```

### 4.9 Modal / Dialog

```text
rótulo:
y: 1000

área demonstrativa:
x: 836
y: 1016
w: 416
h: 96
```

O modal dentro da área respeita a margem lateral normativa de `24 px`.

### 4.10 Bottom Navigation

```text
rótulo:
y: 1124

amostra:
x: 836
y: 1140
w: 416
h: 64

observação:
y: 1216
h: 16
```

Texto da observação:

```text
Somente quando previsto na baseline.
```

Referências:

```text
.specs/wireframes/REGRAS-TECNICAS.md
7 — Componentes técnicos
```

---

# 5. TIPOGRAFIA (Inter - Wireframe)

## Área

```text
x: 444 px
y: 420 px
w: 360 px
h: 152 px
```

## Conteúdo exato

```text
5. TIPOGRAFIA (Inter - Wireframe)

WF-TITLE        20 px | 28 px | SemiBold 600
WF-SECTION      14 px | 20 px | SemiBold 600
WF-BODY         16 px | 24 px | Regular 400
WF-LABEL        14 px | 20 px | Medium 500
WF-ACTION-TEXT  16 px | 24 px | Medium 500
WF-CAPTION      12 px | 16 px | Regular 400
```

## Disposição

```text
padding horizontal: 16 px
padding vertical: 12 px

título:
x: 460
y: 432

lista:
x: 460
y: 460
w: 328
```

Referência:

```text
.specs/wireframes/REGRAS-TECNICAS.md
5 — Tipografia técnica
```

---

# 6. PALETA TÉCNICA — ESCURO

## Área

```text
x: 444 px
y: 588 px
w: 360 px
h: 648 px          (base 1236)
```

## Conteúdo exato

Cópia da tabela 6.6 de `REGRAS-TECNICAS.md`: lista única de 24 linhas em três grupos (11 neutros, 10 semânticas, 3 de cromia adicional), sem títulos de grupo e sem nota. Cada linha: nome do token e chip preenchido com a cor, com o HEX centrado dentro do chip.

## Disposição

```text
título:
x: 460
y: 600

primeira linha:
y: 632

passo da linha:
24 px (mais 8 px de avanço a cada divisor)

token:
x: 460, y_linha, WF-CAPTION, WF-B-TEXT

chip:
x: 692, y_linha, w: 96, h: 16, borda 1 px WF-B-BORDER
HEX centrado (WF-CAPTION; WF-B-TEXT quando luminância < 0,3; senão WF-B-BG)

divisor:
1 px WF-B-BORDER, x: 460, w: 328, em y: 896 e y: 1144 (= y da primeira linha do grupo − 8)

fim da lista:
y: 1216; margem inferior: 20 px (base 1236)
```

Linhas (y da linha):

```text
Neutros (linhas 1 a 11)
 1. WF-B-BG                   #121212   y 632
 2. WF-B-SURFACE              #1E1E1E   y 656
 3. WF-B-SURFACE-ALT          #2A2A2A   y 680
 4. WF-B-BORDER               #5E5E5E   y 704
 5. WF-B-BORDER-CONTROL       #737373   y 728
 6. WF-B-TEXT                 #F2F2F2   y 752
 7. WF-B-TEXT-2               #C2C2C2   y 776
 8. WF-B-ACTION               #E0E0E0   y 800
 9. WF-B-DISABLED             #777777   y 824
10. WF-B-FOCUS                #D0D0D0   y 848
11. WF-B-STATUS               #A8A8A8   y 872

Semânticas (linhas 12 a 21)
12. Primary                   #8ABEFF   y 904
13. On Primary                #0F1115   y 928
14. Secondary                 #B3B3E5   y 952
15. Info                      #8ABEFF   y 976
16. Error                     #FCA5A5   y 1000
17. Success                   #A7F3D0   y 1024
18. Warning (texto/ícone)     #FDE68A   y 1048
19. Warning (preenchimento)   #FDE68A   y 1072
20. On Warning                #0F1115   y 1096
21. Info BG                   #292E34   y 1120

Cromia adicional (linhas 22 a 24)
22. BRAND                     #F2F2F2   y 1152
23. On Brand                  #121212   y 1176
24. Zebra de tabela           #272727   y 1200
```

Referência:

```text
.specs/wireframes/REGRAS-TECNICAS.md
6 — Tokens técnicos / Escuro
```

---

# 7. ELEVAÇÃO

## Área

```text
x: 12 px
y: 1056 px
w: 416 px
h: 180 px          (base 1236)
```

Posição na composição: coluna do viewport, abaixo do cartão do viewport (gap 16 px).

## Conteúdo

Matriz `2 × 2`:

```text
E0   0/0/0/0%
E1   0/1/2/12%
E2   0/2/6/16%
E3   0/4/12/20%
```

## Posições das amostras

Cada amostra:

```text
w: 128 px
h: 44 px
preenchimento: WF-B-SURFACE-ALT (D5); borda 1 px WF-B-BORDER
```

Colunas (centradas no cartão: margem lateral 68 px; gap entre amostras 24 px):

```text
x1: 80 px
x2: 232 px
```

Linhas:

```text
título "7. ELEVAÇÃO": x: 28, y: 1068

linha 1:
y amostra: 1100
y legenda: 1148

linha 2:
y amostra: 1172
y legenda: 1220
```

Referência:

```text
.specs/wireframes/REGRAS-TECNICAS.md
8 — Bordas, radius e elevação
9 — Iconografia
```



---

# Região inferior

A região inferior começa depois do corpo principal:

```text
x: 12 px
y: 1260 px
w: 1256 px
h: 648 px
```

Afastamento:

```text
1236 → fim do corpo principal
1260 → início da região inferior

gap = 24 px
```

Primeira linha da região inferior (blocos 8, 9 e 10):

```text
y: 1260
h: 208

8. RADIUS      x: 12   w: 328
9. ÍCONES      x: 356  w: 328
10. ESTADOS    x: 700  w: 568

gap horizontal: 16 px
328 + 16 + 328 + 16 + 568 = 1256
```

---

# 8. RADIUS

## Área

```text
x: 12 px
y: 1260 px
w: 328 px
h: 208 px
```

Posição na composição: região inferior, primeiro bloco da linha 8 | 9 | 10, à esquerda de ÍCONES (gap 16 px).

## Conteúdo

```text
12 px
Campos e botões

16 px
Cards e modais
```

Posições:

```text
título "8. RADIUS": x: 28, y: 1272

amostra 12 px:
x: 36
y: 1304
w: 128
h: 64
rótulo interno "12 px": centralizado, y: 1326

amostra 16 px:
x: 188
y: 1304
w: 128
h: 64
rótulo interno "16 px": centralizado, y: 1326
```

Legendas:

```text
y: 1380 (centradas sob cada amostra)
```

Referência:

```text
.specs/wireframes/REGRAS-TECNICAS.md
8 — Bordas, radius e elevação
9 — Iconografia
```

---

# 9. ÍCONES (Material Icons Outlined)

## Área

```text
x: 356 px
y: 1260 px
w: 328 px
h: 208 px
```

## Conteúdo

```text
20 px
Ícone auxiliar

24 px
Ação / navegação
```

Amostras:

```text
20 px:
área demonstrativa 128 × 88 px
ícone central 20 × 20 px

24 px:
área demonstrativa 128 × 88 px
ícone central 24 × 24 px
```

Posições:

```text
título "9. ÍCONES (Material Icons Outlined)": x: 372, y: 1272

área 20 px:
x: 380
y: 1304
w: 128
h: 88
rótulo "20 px": centralizado, y: 1316
ícone central: centro em y: 1360

área 24 px:
x: 532
y: 1304
w: 128
h: 88
rótulo "24 px": centralizado, y: 1316
ícone central: centro em y: 1360

legendas: y: 1400 (centradas sob cada área)
texto de referência "Material Icons Outlined: referência conceitual.": x: 380, y: 1432
```

Referência:

```text
.specs/wireframes/REGRAS-TECNICAS.md
9 — Iconografia
```

---

# 10. ESTADOS (Componentes)

## Área

```text
x: 700 px
y: 1260 px
w: 568 px
h: 208 px
```

## Estados

```text
Default
Focus
Pressed / Selected
Disabled
Error
```

`Hover` permanece documentado, mas não precisa ser demonstrado como estado visual obrigatório nesta prancha mobile. A nota registra isso:

```text
nota:
x: 936
y: 1274 (na linha do título do bloco, alinhada à direita; w: 316, termina em x: 1252)
"Hover: documentado; não obrigatório em mobile."
WF-CAPTION, WF-B-TEXT-2
```

Amostras:

```text
x: 716 px
w: 536 px
h: 24 px
```

Posições:

```text
Default             y: 1300
Focus               y: 1332
Pressed / Selected  y: 1364
Disabled            y: 1396
Error               y: 1428
```

Tratamento de cor das amostras:

```text
Default             borda 1 px WF-B-BORDER-CONTROL
Focus               borda 2 px WF-B-FOCUS
Pressed / Selected  fundo Info BG, borda Primary, barra esquerda 4 px Primary; ícone check Primary
Disabled            fundo WF-B-SURFACE-ALT, borda tracejada WF-B-DISABLED; texto e ícone em WF-B-DISABLED
Error               borda 2 px Error; texto e ícone error_outline em Error
```

Referências:

```text
.specs/wireframes/REGRAS-TECNICAS.md
10 — Estados
11 — Acessibilidade estrutural
```

---

# 11. REGRAS GERAIS DE COMPONENTES

## Área

```text
x: 12 px
y: 1484 px
w: 780 px
h: 144 px
```

## Conteúdo exato

```text
Touch target mínimo: 48 × 48 px.

Aplicável a botões, ícones, itens de lista,
navegação e demais áreas interativas.

A área clicável deve respeitar o mínimo mesmo
quando o elemento visual for menor.
```

Amostra de touch target:

```text
x: 28 px
y: 1520 px
w: 48 px
h: 48 px
```

Texto:

```text
x: 96 px
y: 1512 px
w: 680 px
```

Referências:

```text
.specs/wireframes/REGRAS-TECNICAS.md
7 — Componentes técnicos
11 — Acessibilidade estrutural
```

---

# BORDAS E DIVISORES

## Área

```text
x: 808 px
y: 1484 px
w: 460 px
h: 144 px
```

## Borda

```text
amostra:
x: 824
y: 1520
w: 160
h: 64
texto interno: "Borda de controle" (WF-LABEL)

borda:
1 px

token Escuro:
WF-B-BORDER-CONTROL (controle); WF-B-BORDER (decorativa e divisores)
os HEX constam no bloco 6
```

## Divisor

```text
x: 1016
y: 1552
w: 220
h: 1
cor: WF-B-BORDER
```

Referência:

```text
.specs/wireframes/REGRAS-TECNICAS.md
8 — Bordas, radius e elevação
9 — Iconografia
```

---

# 12. OBSERVAÇÕES TÉCNICAS

## Área

```text
x: 12 px
y: 1644 px
w: 1256 px
h: 264 px

limite inferior: 1908 px
margem inferior do canvas: 12 px
```

## Estrutura interna

Este bloco é uma única área documental horizontal.

Não dividir em duas colunas nesta prancha-modelo.

```text
padding horizontal: 16 px
padding vertical: 12 px

x interno: 28 px
w interno: 1224 px

título: x 28, y 1656
primeiro item: y 1688; passo entre itens: 20 px (itens 1 a 10, uma linha cada; último item em y 1868)
```

## Conteúdo exato

```text
1. O viewport representa a tela completa do celular: 360 × 800 px em escala 1:1.

2. A referência dimensional usa largura total 360 px, largura útil 336 px e margens laterais 12 + 12 px.

3. Não existe reserva fixa de faixa superior ou inferior de safe area nesta prancha-modelo.

4. O bitmap WF-VIEWPORT-360x800.png deve permanecer fisicamente 360 × 800 px, inserido em 100%, sem resize.

5. Todos os elementos seguem grid de 4 px e escala de espaçamento 4 / 8 / 12 / 16 / 24 / 32 px.

6. Inter é tipografia técnica do wireframe e não tipografia oficial da marca SaOr.

7. Em páginas seguintes, repetir apenas elementos realmente persistentes.

8. Nomenclatura dos arquivos funcionais: <ID>-<PÁGINA>-<TOTAL>_v<VERSÃO>.png.

9. Interface multipágina só é aprovada quando todas as páginas Claro e Escuro estiverem aprovadas.

10. Cor nunca deve ser o único indicador de estado; cores, ícones e componentes são referências técnicas dos wireframes.
```

Tipografia:

```text
texto:
WF-CAPTION
12 px / 16 px

numeração:
WF-LABEL
```

Referências:

```text
.specs/wireframes/REGRAS-TECNICAS.md
2 — Canvas
3 — Viewport
4 — Grid e spacing
5 — Tipografia técnica
6 — Tokens técnicos
7 — Componentes técnicos
8 — Bordas, radius e elevação
9 — Iconografia
10 — Estados
11 — Acessibilidade estrutural
```

---

# Cotas de componente e detalhes complementares de montagem

```text
Cotas de componente (Primary, estilo A_v02):
coluna da cota: x: 1260 (gutter de 16 px entre a amostra, que termina em 1252, e a borda do cartão, 1268)
colchetes horizontais 1255–1265 nos limites; linha vertical com setas; rótulo vertical "NN px" no centro (12 px, 500)
alturas (y1–y2): 56 (352–408), 56 (436–492), 48 (520–568), 48 (596–644), 48 (672–720),
                 56 (748–804), 64 (832–896), 64 (924–988), 96 (1016–1112), 64 (1140–1204)
modal: cotas horizontais "24" em x: 836–860 e x: 1228–1252, y: 1064 (rótulo 18 px acima da linha)

Modal (4.9): área WF-B-SURFACE-ALT com borda 1 px WF-B-BORDER, radius 12; modal x: 860, y: 1020, w: 368, h: 88, radius 16, borda 1 px WF-B-BORDER, sombra 0 4px 12px rgba(0,0,0,.20);
  alça 32 × 4 no topo (y: 1026); "Título do Modal" (WF-SECTION) x: 876 y: 1034; "Texto de exemplo do modal." (WF-CAPTION) x: 876 y: 1054;
  [Cancelar] 84 × 26 em x: 876 y: 1074, borda 1 px WF-B-BORDER-CONTROL; [Confirmar] 92 × 26, fundo Primary, texto On Primary, em x: 1120 y: 1074; radius 8
Bottom Navigation (4.10): 4 itens a cada 104 px; ícones home, description, people, more_horiz de 24 px em y: 1148; rótulos em y: 1178 (WF-CAPTION); ativo: pílula Info BG 48 × 28 radius 14 em y: 1146, ícone e texto Primary
Itens de lista (4.6 e 4.7): avatar 40 × 40 radius 20, borda 1 px WF-B-BORDER; título em x: 900; chevron_right 24 px à direita
```

---

# Sequência de construção desta prancha-modelo

Esta B_v01 deve obedecer aos gates de `.specs/wireframes/PROCESSO-PRANCHA.md`.

```text
01. Canvas 1280 × 1920 (Gate 1 — técnico)
02. Cabeçalho (Gate 2 — aprovação humana) — APROVADO E CONGELADO
03. Posicionar WF-VIEWPORT-360x800.png em 100% / 1:1 e adicionar cotas 360 / 336 / 12 / 12 / 800 (Gate 3 — aprovação humana) — APROVADO E CONGELADO
04. Calcular a área documental restante (Gate 4 — técnico) — APROVADO E CONGELADO
05. Definir Blocos 1 a 12 e Bordas/Divisores (Gate 5 — técnico) — APROVADO E CONGELADO
06. Conferir integralmente o Wireframe Text (Gate 6 — aprovação humana) — APROVADO E CONGELADO
07. Produção do PNG — APROVADO E CONGELADO (gerado após o Gate 6 APROVADO E CONGELADO)
```

---

# Registro de validação desta versão

```text
[x] Gate 1 registrado como APROVADO E CONGELADO (técnico)
[x] Gates 2 e 3 registrados como APROVADO E CONGELADO (Gate 2 reaprovado após a correção de D4, em 27/10/2026)
[x] Gates 4 e 5 (técnicos) validados e registrados como APROVADO E CONGELADO
[x] Gate 6 registrado como APROVADO E CONGELADO (reaprovado em 27/10/2026)
[x] Produção do PNG registrada como APROVADO E CONGELADO (aprovação explícita do responsável em 27/10/2026)
[x] STATUS do cabeçalho registrado como APROVADO E CONGELADO; PNG regenerado com o STATUS aprovado e revalidado
[x] WF-TEMPLATE-B_v01 (black) é a versão vigente do Modelo B black
[x] origem registrada: WF-TEMPLATE-B_v02 (white), estado Wireframe Text APROVADO E CONGELADO; diferenças classificadas como DIFERENÇA INTENCIONAL (D1 a D5)
[x] viewport especificado: references/black/WF-VIEWPORT-360x800.png, 360 × 800 px em 1:1; nenhum ativo ou bitmap white reutilizado
[x] todas as cores usadas constam em REGRAS-TECNICAS.md, seção 6 (tabela 6.6); HEX somente no bloco 6
[x] pares texto/fundo registrados (sem exceção de nível)
[x] canvas 1280 × 1920; todas as áreas documentadas dentro do canvas
[x] REGRAS-TECNICAS.md seção 3.1 lista references/black/WF-VIEWPORT-360x800.png
[x] REGRAS-TECNICAS.md 6.7 — aprovação das lacunas de cor registrada em 27/10/2026
[x] REGRAS-TECNICAS.md seção 8 — regra de elevação na variação black registrada
[x] origem white WF-TEMPLATE-B_v02: Wireframe Text APROVADO E CONGELADO (7.1); PNG da origem APROVADO E CONGELADO
```

A variação `white` de origem é a `WF-TEMPLATE-B_v02` (pasta `templates/white/`), conforme `WIREFRAME-TEXT.md` 7.1.
