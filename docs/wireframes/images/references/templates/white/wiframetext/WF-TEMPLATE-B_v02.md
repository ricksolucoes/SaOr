# WF-TEMPLATE-B_v02 — Reprodução textual fiel da prancha final

```text
CANVAS FINAL — 1280 × 1920 px

┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│SaOr                │WIREFRAME                                       │ID                │PÁGINA       │VERSÃO      │DATA            │STATUS                       │
│Sales Order         │PRANCHA TÉCNICA - MODELO B                      │WF-TEMPLATE-B     │XX / YY   │v02       │DD/MM/AAAA    │[✓] APROVADO E CONGELADO            │
│                    │(Viewport à esquerda + painel técnico à direita)│BASELINE v1.0     │VARIAÇÃO white              │ETAPA Wireframe Conceitual em Imagem        │
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
││       │ │ card com informações.  │     │     │  ┌ 6. PALETA TÉCNICA - CLARO                      ┐  │    └──────────────────────────────────────────────┘      ││
││       │ └────────────────────────┘     │     │  │ WF-W-BG                                        │  │                                                          ││
││       │ [i] Mensagem informativa       │     │  │ WF-W-SURFACE                                   │  │  BOTÃO TEXTO (mínimo 48 px) + ICON BUTTON (48 x 48 px)   ││
││       │     de exemplo.                │     │  │ WF-W-SURFACE-ALT                               │  │    ┌──────┐                                              ││
││       │ ┌────────────────────────┐     │     │  │ WF-W-BORDER                                    │  │    │ [G]  │  Botão Texto                                 ││
││       │ │           ^            │     │     │  │ WF-W-BORDER-CONTROL                            │  │    └──────┘                                              ││
││       │ │ Área de conteúdo       │     │     │  │ WF-W-TEXT                                      │  │                                                          ││
││       │ │ indicando scroll       │     │     │  │ WF-W-TEXT-2                                    │  │                                                          ││
││       │ │ vertical               │     │     │  │ WF-W-ACTION                                    │  │                                                          ││
││       │ │           v            │     │     │  │ WF-W-DISABLED                                  │  │                                                          ││
││       │ └────────────────────────┘     │     │  │ WF-W-FOCUS                                     │  │  ITEM DE LISTA - simples (56 px)                         ││
││       ├────────────────────────────────┤     │  │ WF-W-STATUS                                    │  │    ┌──────────────────────────────────────────────┐      ││
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
││  A área clicável deve respeitar o mínimo mesmo quando                                            │  │  Tokens: WF-W-BORDER-CONTROL | WF-W-BORDER               ││
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

A reprodução textual apresentada no início deste arquivo é a **referência conceitual de composição** da `WF-TEMPLATE-B_v02`.

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

As coordenadas, larguras e alturas abaixo são **específicas desta prancha-modelo B_v02**.

Elas não são medidas universais dos futuros wireframes funcionais T/M/E.

Ao reutilizar o conceito desta composição em outra prancha, deve-se recalcular as áreas documentais conforme o conteúdo real daquela prancha, preservando as regras técnicas normativas.

### 1.1 O que a v02 muda em relação à v01

```text
1. Cores: a paleta técnica passa a seguir REGRAS-TECNICAS.md, seção 6 (tabela 6.5): semânticas do Documento Mestre §20.1
   (Tema Claro) e lacunas definidas por teste. O conjunto da v01 está preservado em REGRAS-TECNICAS.md 6.4 como histórico.
2. As cores são citadas pelo nome do token; o HEX aparece somente no bloco 6 (WIREFRAME-TEXT.md, seção 4.2).
3. Bordas: campo, botão secundário, icon button, Cancelar e a amostra de borda usam WF-W-BORDER-CONTROL (3:1);
   divisores e bordas decorativas continuam em WF-W-BORDER.
4. Viewport: references/white/WF-VIEWPORT-360x800.png (gerado com a paleta da seção 6). Posição (x 40, y 224) e escala 1:1 inalteradas.
5. Bloco 6 PALETA: 24 linhas (11 neutros, 10 semânticas, 3 de cromia adicional) em lista única, passo de linha de 24 px;
   o card cresce de h 216 para h 648 (y 588 → 1236). Para acomodar o crescimento:
   - ELEVAÇÃO (bloco 7) passa da coluna central para a coluna do viewport (x 12, y 1056, w 416, h 180);
   - o cartão do viewport passa de h 1024 para h 908 (base 1040); o bitmap e as cotas não mudam;
   - RADIUS (bloco 8) sai da coluna central e passa para a região inferior, à esquerda de ÍCONES (x 12, y 1260, w 328, h 208);
   - ÍCONES (bloco 9) passa para x 356, w 328; ESTADOS (bloco 10) passa para x 700, w 568 (328 + 16 + 328 + 16 + 568 = 1256);
   - a base do corpo principal passa de y 1156 para y 1236 (+80); COMPONENTES (bloco 4) passa de h 864 para h 944,
     com +8 px de intervalo entre componentes consecutivos;
   - a região inferior (blocos 8 a 12) desce 80 px; OBSERVAÇÕES passa de h 344 para h 264 (itens em passo de 20 px), base 1908 inalterada.
6. STATUS do cabeçalho: APROVADO E CONGELADO (nova versão; gates reiniciados na seção 2 e todos aprovados em 27/10/2026).
7. Conteúdo, composição e geometria dos blocos 1, 2, 3 e 5 e do cabeçalho permanecem como na v01.
8. A disposição dos blocos 6, 8, 9 e 10 (RADIUS na região inferior, à esquerda de ÍCONES; PALETA ampliada) foi definida pelo responsável
   em 27/10/2026 (decisão registrada neste Wireframe Text) por critério visual; ela substitui a disposição da v01 e reabre o Gate 6.
```

---

## 2. Hierarquia de autoridade

Para esta prancha, a ordem de autoridade é:

```text
1. docs/Documento_Mestre.md — somente conteúdo e comportamento funcional quando aplicável
2. .specs/wireframes/REGRAS-TECNICAS.md — invariantes técnicos
3. .specs/wireframes/PROCESSO-PRANCHA.md — sequência e gates
4. .specs/wireframes/WIREFRAME-TEXT.md — contrato documental
5. docs/wireframes/images/README.md — estrutura operacional e separação `white` / `black`
6. este WF-TEMPLATE-B_v02.md — composição específica desta alternativa
7. PNG correspondente — resultado visual, nunca fonte normativa superior
```

Nenhuma prancha histórica ou alternativa anterior é referência de geometria, proporção, posicionamento ou distribuição desta alternativa B.

### Estado dos gates desta B_v02

O Gate 1 é técnico e está concluído porque o canvas registrado nesta B_v02 atende às invariantes canônicas.

Os Gates 2, 3 e 6 exigem aprovação humana explícita. Os Gates 4 e 5 são técnicos e somente podem ser concluídos depois das dependências anteriores estarem congeladas.

Estado registrado:

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

Esta v02 deriva da `WF-TEMPLATE-B_v01` (Gates 1 a 6 e PNG APROVADO E CONGELADO), que permanece como histórico imutável. A v02 é uma nova versão: os gates humanos foram reabertos porque cores, viewport, bloco 6 e a distribuição vertical do corpo principal mudaram.

Registros:

```text
Gate 1 (técnico): canvas 1280 × 1920 px conforme REGRAS-TECNICAS.md — APROVADO E CONGELADO.
Gate 2: aprovado explicitamente pelo responsável em 27/10/2026 (aprovação registrada neste Wireframe Text) — APROVADO E CONGELADO. O cabeçalho não mudou com a nova disposição.
Gate 3: bitmap aprovado em 27/10/2026; posição, cotas e registro do gate aprovados explicitamente pelo responsável em 27/10/2026 (aprovação registrada neste Wireframe Text) — APROVADO E CONGELADO. Viewport e cotas não mudaram com a nova disposição.
Gates 4 e 5 (técnicos): revalidados em 27/10/2026 para a nova disposição dos blocos 6, 8, 9 e 10 (decidida pelo responsável em 27/10/2026), com os Gates 2 e 3 congelados — APROVADO E CONGELADO.
Gate 6: reaberto pela nova disposição dos blocos 6, 8, 9 e 10 e aprovado explicitamente pelo responsável em 27/10/2026 (aprovação registrada neste Wireframe Text) — APROVADO E CONGELADO.
Produção do PNG: gerado em 27/10/2026 a partir deste Wireframe Text e validado contra ele; aprovado explicitamente pelo responsável em 27/10/2026 (aprovação registrada neste Wireframe Text) — APROVADO E CONGELADO.
STATUS no cabeçalho: registrado como APROVADO E CONGELADO; o PNG foi regenerado com o STATUS aprovado e revalidado.
Validação técnica dos Gates 4 e 5:
  - fechamento horizontal do cabeçalho: 156 + 384 + 716 = 1256 px;
  - fechamento horizontal do corpo principal: 416 + 16 + 360 + 16 + 448 = 1256 px;
  - viewport: 12 + 336 + 12 = 360 px;
  - fechamento vertical do corpo principal: coluna do viewport 132 + 908 + 16 + 180 = 1236; coluna central 132 + 144 + 16 + 112 + 16 + 152 + 16 + 648 = 1236;
    coluna direita 132 + 144 + 16 + 944 = 1236;
  - fechamento horizontal da linha inferior 8 | 9 | 10: 328 + 16 + 328 + 16 + 568 = 1256 px;
  - região inferior: 1260 + 208 + 16 + 144 + 16 + 264 = 1908 (limite inferior do canvas);
  - todas as áreas x/y/w/h permanecem dentro do canvas 1280 × 1920 px.
Cores: as lacunas da seção 6 (marcadas com *) foram aprovadas pelo responsável em 27/10/2026 (decisão registrada neste Wireframe Text);
  o registro formal em REGRAS-TECNICAS.md 6.7 é feito pelo responsável.
```

As geometrias documentadas abaixo são desta `B_v02` e dependem da aprovação humana dos Gates 2, 3 e 6. Qualquer alteração posterior deve seguir o processo vigente e reabrir somente os gates realmente afetados.

### Cores usadas e pares texto/fundo

As cores desta prancha são citadas pelo nome do token. O HEX consta somente no bloco 6. Cromia adicional: BRAND, On Brand e Zebra de tabela (esta última registrada na paleta; esta prancha não usa linhas zebradas). Semânticas usadas: Primary, On Primary, Info BG, Error, Success.

Pares texto/fundo usados (razões da tabela 6.5 de `REGRAS-TECNICAS.md`):

| Par | Razão | Nível |
|---|---:|---|
| WF-W-TEXT sobre WF-W-SURFACE | 17,40:1 | AAA |
| WF-W-TEXT-2 sobre WF-W-SURFACE | 7,34:1 | AAA |
| Primary sobre WF-W-SURFACE | 8,61:1 | AAA |
| On Primary sobre Primary | 8,61:1 | AAA |
| Info sobre Info BG | 7,30:1 | AAA |
| Error sobre WF-W-SURFACE | 8,31:1 | AAA |
| Success sobre WF-W-SURFACE | 7,13:1 | AAA |
| Warning (texto/ícone) sobre WF-W-SURFACE | 5,42:1 | AA |
| On Warning sobre Warning (preenchimento) | 5,59:1 | AA |
| On Brand sobre BRAND | 17,85:1 | AAA |
| WF-W-TEXT sobre Zebra de tabela | 16,10:1 | AAA |
| WF-W-BORDER-CONTROL sobre WF-W-SURFACE (borda de campo, botão secundário, icon button) | 3,64:1 | OK (≥ 3:1) |
| WF-W-FOCUS sobre WF-W-SURFACE (foco) | 8,86:1 | OK (≥ 3:1) |

Exceções registradas na seção 6.5: Warning (texto/ícone) e On Warning sobre Warning (preenchimento) em AA (não AAA); WF-W-STATUS em AA sobre SURFACE (neutro vigente, não usado em par de texto desta prancha).

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

A proporção vem do frame inicial da B_v01, preservado nesta B_v02.

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
v02

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
white

ETAPA
Wireframe Conceitual em Imagem
```

Cor do valor de STATUS: estado atual APROVADO E CONGELADO — Success, com o ícone check_circle 20 px em (1120, 46) e valor em (1146, 38), 2 linhas "APROVADO E / CONGELADO"; enquanto AGUARDANDO APROVAÇÃO (regra de estado, não aplicável a esta versão congelada) — WF-W-TEXT-2, sem ícone, 2 linhas "AGUARDANDO / APROVAÇÃO" em (1120, 38/54). Fundo do campo: WF-W-SURFACE.

---

# Viewport

## Papel na composição

O viewport é o primeiro elemento estrutural montado após o cabeçalho.

Ele deve ser inserido fisicamente antes do cálculo final das áreas documentais.

Arquivo obrigatório:

```text
docs/wireframes/images/references/white/WF-VIEWPORT-360x800.png
```

Este é o bitmap white gerado em 27/10/2026 com a paleta da seção 6 de `REGRAS-TECNICAS.md` (Icon Button à esquerda do Botão Texto). Os bitmaps anteriores permanecem preservados como referências históricas e não são usados nesta prancha. O arquivo está registrado em `REGRAS-TECNICAS.md`, seção 3.1.

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

Cotas em Primary, linha de 1 px, setas de 5 px, rótulos WF-CAPTION 600 com fundo WF-W-SURFACE (padding horizontal 6 px).

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

# Mapa geométrico principal da B_v02

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
borda: 1 px WF-W-BORDER-CONTROL
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
fundo: WF-W-SURFACE; borda: 1 px WF-W-BORDER-CONTROL
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
radius: 12, borda 1 px WF-W-BORDER-CONTROL
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

# 6. PALETA TÉCNICA — CLARO

## Área

```text
x: 444 px
y: 588 px
w: 360 px
h: 648 px          (base 1236)
```

## Conteúdo exato

Cópia da tabela 6.5 de `REGRAS-TECNICAS.md`: lista única de 24 linhas em três grupos (11 neutros, 10 semânticas, 3 de cromia adicional), sem títulos de grupo e sem nota. Cada linha: nome do token e chip preenchido com a cor, com o HEX centrado dentro do chip.

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
x: 460, y_linha, WF-CAPTION, WF-W-TEXT

chip:
x: 692, y_linha, w: 96, h: 16, borda 1 px WF-W-BORDER
HEX centrado (WF-CAPTION; On Primary quando luminância < 0,3; senão WF-W-TEXT)

divisor:
1 px WF-W-BORDER, x: 460, w: 328, em y: 896 e y: 1144 (= y da primeira linha do grupo − 8)

fim da lista:
y: 1216; margem inferior: 20 px (base 1236)
```

Linhas (y da linha):

```text
Neutros (linhas 1 a 11)
 1. WF-W-BG                   #F4F4F4   y 632
 2. WF-W-SURFACE              #FFFFFF   y 656
 3. WF-W-SURFACE-ALT          #EAEAEA   y 680
 4. WF-W-BORDER               #B5B5B5   y 704
 5. WF-W-BORDER-CONTROL       #868686   y 728
 6. WF-W-TEXT                 #1A1A1A   y 752
 7. WF-W-TEXT-2               #565656   y 776
 8. WF-W-ACTION               #333333   y 800
 9. WF-W-DISABLED             #9A9A9A   y 824
10. WF-W-FOCUS                #4A4A4A   y 848
11. WF-W-STATUS               #626262   y 872

Semânticas (linhas 12 a 21)
12. Primary                   #004A99   y 904
13. On Primary                #FFFFFF   y 928
14. Secondary                 #3C3CB0   y 952
15. Info                      #004A99   y 976
16. Error                     #991B1B   y 1000
17. Success                   #166534   y 1024
18. Warning (texto/ícone)     #AC4F01   y 1048
19. Warning (preenchimento)   #ED6C02   y 1072
20. On Warning                #1A1A1A   y 1096
21. Info BG                   #E6EDF5   y 1120

Cromia adicional (linhas 22 a 24)
22. BRAND                     #0F172A   y 1152
23. On Brand                  #FFFFFF   y 1176
24. Zebra de tabela           #F6F6F6   y 1200
```

Referência:

```text
.specs/wireframes/REGRAS-TECNICAS.md
6 — Tokens técnicos / Claro
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
WF-CAPTION, WF-W-TEXT-2
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
Default             borda 1 px WF-W-BORDER-CONTROL
Focus               borda 2 px WF-W-FOCUS
Pressed / Selected  fundo Info BG, borda Primary, barra esquerda 4 px Primary; ícone check Primary
Disabled            fundo WF-W-SURFACE-ALT, borda tracejada WF-W-DISABLED; texto e ícone em WF-W-DISABLED
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

token Claro:
WF-W-BORDER-CONTROL (controle); WF-W-BORDER (decorativa e divisores)
os HEX constam no bloco 6
```

## Divisor

```text
x: 1016
y: 1552
w: 220
h: 1
cor: WF-W-BORDER
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

Modal (4.9): área WF-W-SURFACE-ALT com borda 1 px WF-W-BORDER, radius 12; modal x: 860, y: 1020, w: 368, h: 88, radius 16, borda 1 px WF-W-BORDER, sombra 0 4px 12px rgba(0,0,0,.20);
  alça 32 × 4 no topo (y: 1026); "Título do Modal" (WF-SECTION) x: 876 y: 1034; "Texto de exemplo do modal." (WF-CAPTION) x: 876 y: 1054;
  [Cancelar] 84 × 26 em x: 876 y: 1074, borda 1 px WF-W-BORDER-CONTROL; [Confirmar] 92 × 26, fundo Primary, texto On Primary, em x: 1120 y: 1074; radius 8
Bottom Navigation (4.10): 4 itens a cada 104 px; ícones home, description, people, more_horiz de 24 px em y: 1148; rótulos em y: 1178 (WF-CAPTION); ativo: pílula Info BG 48 × 28 radius 14 em y: 1146, ícone e texto Primary
Itens de lista (4.6 e 4.7): avatar 40 × 40 radius 20, borda 1 px WF-W-BORDER; título em x: 900; chevron_right 24 px à direita
```

---

# Sequência de construção desta prancha-modelo

Esta B_v02 deve obedecer aos gates de `.specs/wireframes/PROCESSO-PRANCHA.md`.

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
[x] Gates 2 e 3 registrados como APROVADO E CONGELADO (aprovação do responsável em 27/10/2026)
[x] Gates 4 e 5 (técnicos) revalidados para a nova disposição e registrados como APROVADO E CONGELADO
[x] Gate 6 registrado como APROVADO E CONGELADO (reaberto pela nova disposição e aprovado pelo responsável em 27/10/2026)
[x] Produção do PNG registrada como APROVADO E CONGELADO (aprovação explícita do responsável em 27/10/2026)
[x] STATUS do cabeçalho registrado como APROVADO E CONGELADO; PNG regenerado com o STATUS aprovado e revalidado
[x] WF-TEMPLATE-B_v02 é a versão vigente do Modelo B white; WF-TEMPLATE-B_v01 permanece como histórico imutável
[x] viewport especificado: WF-VIEWPORT-360x800.png (white), 360 × 800 px em 1:1
[x] todas as cores usadas constam em REGRAS-TECNICAS.md, seção 6 (tabela 6.5); HEX somente no bloco 6
[x] pares texto/fundo registrados na seção 2 (Cores usadas e pares texto/fundo)
[x] canvas 1280 × 1920; todas as áreas documentadas dentro do canvas (base 1908)
[x] REGRAS-TECNICAS.md seção 3.1 lista WF-VIEWPORT-360x800.png
[x] REGRAS-TECNICAS.md 6.7 — aprovação das lacunas de cor registrada em 27/10/2026
```

A variação `black` correspondente é a `WF-TEMPLATE-B_v01` (pasta `templates/black/`), derivada desta v02 conforme `WIREFRAME-TEXT.md` 7.1.
