# WF-TEMPLATE-A_v03 — Reprodução textual fiel da prancha final

```text
CANVAS FINAL — 1280 × 1920 px

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ SaOr / Sales Order │ WIREFRAME · PRANCHA TÉCNICA - MODELO A (Viewport central dominante) │ WF-TEMPLATE-A │ XX / YY │ v03 │ DD/MM/AAAA │ [✓] APROVADO E CONGELADO │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

▌1. CANVAS E VIEWPORT                       VIEWPORT CENTRAL DOMINANTE (sem card)   ▌6. COMPONENTES (MEDIDAS)
┌────────────────────────────────────────┐  ┌────────────────────────────────────┐  ┌────────────────────────────────────────────────┐
│ Canvas 1280 × 1920 | Viewport 360 × 800 │  │ 360 px (viewport total)            │  │ App Bar (56) | Campo Outlined (56)             │
│ Escala 1:1 | Retrato | Margem 12 px    │  │ 12 | 336 px (largura útil) | 12    │  │ Botão Primário (48) | Secundário (48)          │
└────────────────────────────────────────┘  │ ┌──────────────────────────┐       │  │ [G] Botão Texto + Icon Button (48 × 48)        │
                                            │ │ (o) Título da Página [S][:]│     │  │ Item de lista simples (56) / secundário (64)   │
▌2. COTAS DO VIEWPORT                       │ │     Subtítulo da página  │       │  │ Card (64) | Modal (96)                         │
┌────────────────────────────────────────┐  │ │ Seção de Conteúdo        │       │  │ Bottom Navigation (64)                         │
│ 360 | 336 | 12 + 12 | 800 px | 1:1     │  │ │ Rótulo do campo          │       │  │ + cota azul vertical à direita                 │
└────────────────────────────────────────┘  │ │ [ Texto de exemplo    v ]│       │  └────────────────────────────────────────────────┘
                                            │ │ [    Botão Primário     ]│       │
▌3. GRID E SPACING                          │ │ [   Botão Secundário    ]│       │
┌────────────────────────────────────────┐  │ │ [G] Botão Texto          │       │
│ Grid 4 px | 4/8/12/16/24/32            │  │ │ (o) Título do item     > │       │
│ Padding-base 16 / 12 px                │  │ │ [ Título do Card        ]│       │
└────────────────────────────────────────┘  │ │ [i] Mensagem informativa │       │
                                            │ │ [ ^ Área de scroll v    ]│       │
▌4. TIPOGRAFIA (Inter - Wireframe)          │ │ Início Pedidos Clientes M│       │
┌────────────────────────────────────────┐  │ └──────────────────────────┘       │
│ WF-TITLE ... WF-CAPTION (6 linhas)     │  │ 800 px (viewport total)            │
└────────────────────────────────────────┘  └────────────────────────────────────┘

▌5. PALETA TÉCNICA — CLARO
┌────────────────────────────────────────┐
│ 10 tokens neutros [chip + HEX]         │
│ 8 cores semânticas [chip + HEX]        │
└────────────────────────────────────────┘


▌7 ELEVAÇÃO │ ▌8 RADIUS │ ▌9 ÍCONES (Material Icons Outlined) │ ▌10 ESTADOS (Componentes)   [4 cards em linha]                        
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ E0–E3 (2×2)  │  12 px / 16 px  │  20 px / 24 px  │  Default Focus Pressed Disabled Error                                           │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
▌11 REGRAS GERAIS DE COMPONENTES │ ▌12 BORDAS E DIVISORES   [2 cards em linha]                                                        
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ [ ] Touch target mínimo 48 × 48 px  │  Borda 1 px · Divisor 1 px                                                                   │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
▌13 OBSERVAÇÕES TÉCNICAS   [2 colunas: 1–5 e 6–10]                                                                                    
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 1–5 (esquerda)                                         6–10 (direita)                                                              │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

# Especificação de implementação da prancha

## 1. Regra de leitura deste documento

A reprodução textual acima é a **referência conceitual de composição** da `WF-TEMPLATE-A_v03`. Não é escala de caracteres para pixels; as medidas valem somente nas seções abaixo, que são **específicas desta prancha-modelo** e não medidas universais de futuros wireframes T/M/E.

```text
canvas:              1280 × 1920 px
margem estrutural:     12 px
grid base:              4 px
escala de spacing:      4 / 8 / 12 / 16 / 24 / 32 px
viewport físico:      360 × 800 px, escala 1:1
```

## 2. O que a v03 muda em relação à v02

```text
1. Canvas 1024 × 1536 → 1280 × 1920 px (REGRAS-TECNICAS vigente).
2. Viewport 360 × 800 px em 1:1, bitmap sem resize (a v02 desenhava o viewport distorcido).
3. Safe areas removidas: bloco 2 SAFE AREAS, faixas de 24/32 px e cotas correspondentes.
   REGRAS-TECNICAS 3.3: não existe reserva fixa de safe area nesta etapa.
4. Novo bloco 2 COTAS DO VIEWPORT no lugar do antigo bloco de safe areas.
5. Cabeçalho completo (STATUS, BASELINE, VARIAÇÃO, ETAPA), como nos modelos B e C.
6. Título do bloco FORA do card: barra azul vertical à esquerda + "N. TÍTULO" em caixa alta.
7. Cards sem borda: fundo branco, radius 16, sombra leve.
8. Botão Texto e Icon Button reunidos numa só faixa (ícone à esquerda, texto colado ao ícone).
9. Estados com contorno de componente e ícone à esquerda (a v02 usava barras coloridas).
10. Blocos REGRAS GERAIS e BORDAS E DIVISORES numerados 11 e 12; observações viram o bloco 13.
11. Mantida a disposição do A: viewport central dominante entre a coluna de referências (esquerda)
    e a coluna de componentes (direita); linha inferior com 4 cards; regras e observações no rodapé.
```

## 3. Hierarquia de autoridade e estado

```text
1. docs/Documento_Mestre.md — somente conteúdo e comportamento funcional
2. .specs/wireframes/REGRAS-TECNICAS.md — invariantes técnicos
3. .specs/wireframes/PROCESSO-PRANCHA.md — sequência e gates
4. .specs/wireframes/WIREFRAME-TEXT.md — contrato documental
5. docs/wireframes/images/README.md — estrutura operacional white / black
6. este WF-TEMPLATE-A_v03.md — composição específica desta alternativa
7. PNG correspondente — resultado visual, nunca fonte normativa superior
```

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

A aprovação humana dos Gates 2, 3 e 6 e do PNG foi dada pelo responsável em `26/10/2026`, após a visualização da prévia. Os Gates 4 e 5 foram validados tecnicamente contra este texto: 336 + 16 + 440 + 16 + 448 = 1256 px; viewport 12 + 336 + 12 = 360 px; todas as áreas x/y/w/h dentro do canvas 1280 × 1920 px; limite inferior documental y 1904 ≤ 1908.

Pendências na spec, herdadas do modelo C, que **não foram resolvidas** por esta aprovação: cromia adicional (azul, verde, semânticas), viewport derivado `WF-VIEWPORT-360x800-clean_icone-esquerda.png`, card sem borda e título fora do card.

## 4. Padrões visuais

### 4.1 Título de bloco (fora do card)

```text
faixa de título: 32 px (o card começa em y_título + 32)
barra: 4 × 20 px, radius 2, #0061FE, em (x_bloco, y_título + 2)
texto: "N. TÍTULO" em caixa alta, WF-SECTION 14/20 600, WF-W-TEXT, x_bloco + 14, y_título + 2
gap entre blocos: 16 px (24 a 32 px entre seções)
```

### 4.2 Card

```text
fundo WF-W-SURFACE #FFFFFF · sem borda · radius 16
sombra: 0 1px 2px rgba(0,0,0,.12), 0 2px 8px rgba(0,0,0,.06)
```

### 4.3 Tabela zebra (blocos 1 a 4)

```text
passo da linha: 20 px; linhas ímpares com faixa #F6F6F6 (radius 4, x_card + 8, largura = card − 16)
rótulo: x_card + 16, y_linha + 2, WF-CAPTION, WF-W-TEXT-2 (bloco 4: WF-W-TEXT)
valor: WF-CAPTION 500, WF-W-TEXT
```

### 4.4 Cromia adicional

```text
BLUE #0061FE · INFO_BG #DDEEFC · ERROR #D32F2F · SUCCESS #2E7D32 · BRAND #0F172A · zebra #F6F6F6
```

---

# Canvas e cabeçalho

```text
área útil: x 12, y 12, w 1256, h 1896 · limites: esq 12 | dir 1268 | topo 12 | base 1908
cabeçalho: x 12, y 12, w 1256, h 96 (card sem borda, sombra 4.2, divisores 1 px WF-W-BORDER)
MARCA x 12 w 156 | IDENTIFICAÇÃO x 168 w 384 | METADADOS x 552 w 716  (156 + 384 + 716 = 1256)
```

Marca: ícone `assets/logo/saor-icon-master.svg` (x 24, y 40, w 44); "SaOr" Google Sans Bold 700 30/34 #0F172A (x 76, y 34); "SALES ORDER" Quicksand 400 10/14 uppercase, tracking 0.14em (x 77, y 70).

Identificação (x 192):

```text
WIREFRAME                           y 20, WF-LABEL, tracking 0.08em
PRANCHA TÉCNICA - MODELO A          y 40, WF-TITLE
(Viewport central dominante)        y 72, WF-CAPTION, WF-W-TEXT-2
```

Metadados — linha superior (y 12, h 64; rótulo y 20, valor y 40):

```text
ID      x 552  w 164   WF-TEMPLATE-A
PÁGINA  x 716  w 128   XX / YY
VERSÃO  x 844  w 124   v03
DATA    x 968  w 140   DD/MM/AAAA
STATUS  x 1108 w 160   APROVADO E CONGELADO
```

STATUS: fundo branco; só o valor e o ícone em verde #2E7D32 (check_circle 20 px em (1120, 46); valor em (1146, 38), w 114, 2 linhas "APROVADO E / CONGELADO", WF-CAPTION 600).

Linha inferior (y 76, h 32; rótulo WF-CAPTION + valor WF-LABEL na mesma linha, y 84):

```text
BASELINE  x 552  w 164   v1.0
VARIAÇÃO  x 716  w 220   white
ETAPA     x 936  w 332   Wireframe Conceitual em Imagem
```

---

# Mapa geométrico principal

```text
COLUNA ESQUERDA  x 12   w 336
gap              16
COLUNA CENTRAL   x 364  w 440   (viewport, sem card)
gap              16
COLUNA DIREITA   x 820  w 448
336 + 16 + 440 + 16 + 448 = 1256
```

Blocos (y_título → y_card, h → base):

```text
COLUNA ESQUERDA (x 12, w 336)
1  CANVAS E VIEWPORT                132 → 164,   h 132 → 296
2  COTAS DO VIEWPORT                312 → 344,   h 152 → 496
3  GRID E SPACING                   512 → 544,   h 112 → 656
4  TIPOGRAFIA (Inter - Wireframe)   672 → 704,   h 152 → 856
5  PALETA TÉCNICA — CLARO           872 → 904,   h 192 → 1096

COLUNA DIREITA (x 820, w 448)
6  COMPONENTES (MEDIDAS)            132 → 164,   h 848 → 1012

LINHA INFERIOR (y_título 1128 → y_card 1160)
7  ELEVAÇÃO                         x 12   w 344  h 168 → 1328
8  RADIUS                           x 372  w 256  h 100 → 1260
9  ÍCONES (Material Icons Outlined) x 644  w 304  h 160 → 1320
10 ESTADOS (Componentes)            x 964  w 304  h 228 → 1388

REGRAS E BORDAS (y_título 1420 → y_card 1452, h 120 → 1572)
11 REGRAS GERAIS DE COMPONENTES     x 12   w 620
12 BORDAS E DIVISORES               x 648  w 620

RODAPÉ
13 OBSERVAÇÕES TÉCNICAS             x 12   w 1256  y_título 1604 → y_card 1636, h 268 → 1904
```

Limite inferior documental: y 1904 (≤ 1908).

---

# Viewport central

Sem título e sem card. O bitmap fica entre as colunas, sobre o fundo da prancha.

```text
arquivo: docs/wireframes/images/references/white/WF-VIEWPORT-360x800-clean_icone-esquerda.png (derivado; ver seção 3)
posição: x 404, y 184, w 360, h 800 (limite direito 764, inferior 984)
escala: 100% / 1:1
cálculo horizontal: coluna 440 − bitmap 360 = 80; 80 / 2 = 40; 364 + 40 = x 404
```

Proibido: redimensionar, ampliar, reduzir, esticar, recortar, reconstruir ou adaptar o bitmap. Sem safe area.

Cotas (azul #0061FE, linha 1 px, setas 5 px, rótulos WF-CAPTION 600 sobre fundo da prancha):

```text
Linhas de extensão tracejadas (2/2):
  x 404 e x 763, de y 140 a y 184
  x 416 e x 751, de y 166 a y 184
360 px (viewport total):    linha y 146, x 404–764; rótulo centrado, y 138
12 | 336 | 12:              linha y 170, x 404–764; divisões em x 416 e x 751
  rótulo "336 px (largura útil)" centrado, y 162
  rótulos "12 px": x 377 (alinhado à direita, w 26) e x 765 (alinhado à esquerda)
800 px (viewport total):
  extensões horizontais x 764–788 em y 184 e y 983
  linha vertical x 778, de y 185 a y 983, setas nas pontas
  rótulo vertical sobre a linha, centrado em y 584
```

---

# Blocos da coluna esquerda

Tabelas zebra (4.3) começam em y_card + 16; valor em x_card + 176 (blocos 1 a 3) e x_card + 128 (bloco 4).

```text
1. CANVAS E VIEWPORT (card y 164)
   Canvas da prancha       1280 × 1920 px
   Viewport (interface)     360 × 800 px
   Escala do viewport       1:1
   Orientação               Retrato
   Margem horizontal        12 px

2. COTAS DO VIEWPORT (card y 344)
   Largura total   360 px | Largura útil 336 px | Margem esquerda 12 px
   Margem direita   12 px | Altura total  800 px | Escala 1:1
   (uma linha por item)

3. GRID E SPACING (card y 544)
   Grid base                 4 px
   Escala                    4 / 8 / 12 / 16 / 24 / 32 px
   Padding-base horizontal   16 px
   Padding-base vertical     12 px

4. TIPOGRAFIA (Inter - Wireframe) (card y 704)
   WF-TITLE        20 px | 28 px | SemiBold 600
   WF-SECTION      14 px | 20 px | SemiBold 600
   WF-BODY         16 px | 24 px | Regular 400
   WF-LABEL        14 px | 20 px | Medium 500
   WF-ACTION-TEXT  16 px | 24 px | Medium 500
   WF-CAPTION      12 px | 16 px | Regular 400
```

## 5. PALETA TÉCNICA — CLARO

Card x 12, y 904, w 336, h 192. Linhas de 16 px a partir de y 920. Chip preenchido com a cor, HEX centrado (11 px; branco ou #1A1A1A conforme contraste).

```text
Neutros (token x 28, chip x 152, w 56, h 16)
WF-W-BG #F4F4F4 · WF-W-SURFACE #FFFFFF · WF-W-SURFACE-ALT #EAEAEA · WF-W-BORDER #B5B5B5
WF-W-TEXT #1A1A1A · WF-W-TEXT-2 #565656 · WF-W-ACTION #333333 · WF-W-DISABLED #9A9A9A
WF-W-FOCUS #4A4A4A · WF-W-STATUS #626262

Semânticas (rótulo x 216, chip x 288, w 52, h 16)
Primary #0061FE · On Primary #FFFFFF · Secondary #9E9EDE · Info #0288D1
Error #D32F2F · Success #2E7D32 · Warning #ED6C02 · Info BG #DDEEFC

Nota (x 220, y 1052 e 1068): "Cores semânticas / da representação."
```

---

# 6. COMPONENTES (MEDIDAS)

Card x 820, y 164, w 448, h 848. Amostras x 836, w 416. Rótulo WF-CAPTION, h 16, 16 px acima da amostra. Geometria idêntica à do modelo C (bloco 12), com o card em y 164.

```text
4.1  APP BAR (56 px)                         rótulo y 180 | amostra y 196, h 56
4.2  CAMPO OUTLINED (56 px)                  rótulo y 256 | amostra y 272, h 56, radius 12
4.3  BOTÃO PRIMÁRIO (48 px)                  rótulo y 332 | amostra y 348, h 48, #0061FE, texto branco
4.4  BOTÃO SECUNDÁRIO (48 px)                rótulo y 400 | amostra y 416, h 48
4.5  BOTÃO TEXTO (mínimo 48 px) + ICON BUTTON (48 × 48 px)
                                             rótulo y 468 | faixa y 484, h 48
4.6  ITEM DE LISTA - simples (56 px)         rótulo y 536 | amostra y 552, h 56
4.7  ITEM DE LISTA - secundário (64 px)      rótulo y 612 | amostra y 628, h 64
4.8  CARD (radius 16 px)                     rótulo y 696 | amostra y 712, h 64
4.9  MODAL / DIALOG (margem lateral 24 px)   rótulo y 780 | área y 796, h 96
4.10 BOTTOM NAVIGATION (64 px)               rótulo y 896 | amostra y 912, h 64
     observação y 980: "Somente quando previsto na baseline."
```

Conteúdo:

```text
4.1  [menu] Título (WF-TITLE) [search]; ícones 24 px
4.2  Rótulo (WF-CAPTION, y +7) / Texto de exemplo (WF-BODY, y +24) / expand_more
4.5  Icon Button à ESQUERDA: x 836, y 484, 48 × 48, radius 12, ícone settings 24 px em (848, 496)
     Botão Texto colado ao ícone: x 900, azul #0061FE, WF-ACTION-TEXT, y 496
4.6  avatar 40 × 40 (radius 20, SURFACE-ALT) x +12 / y +8; título x +64; chevron_right 24 px
4.7  avatar 40 × 40 x +12 / y +12; título x +64 / y +10; secundário x +64 / y +34; chevron_right
4.8  Título do Card (WF-SECTION) / Texto de exemplo do card. (WF-CAPTION), padding 16
4.9  fundo SURFACE-ALT; modal x 860, y 800, w 368, h 88, radius 16, sombra E3, alça 32 × 4;
     Título do Modal; Texto de exemplo do modal.; [Cancelar] 84 × 26; [Confirmar] 92 × 26 azul
4.10 itens a cada 104 px: Início (ativo, pílula #DDEEFC 48 × 28, azul), Pedidos, Clientes, Mais
```

Cotas de componente (azul, estilo A_v02): coluna em x 1260 (gutter de 16 px entre a amostra, que termina em 1252, e o card, 1268); colchetes 1255–1265; rótulo vertical "NN px" no centro. Alturas: 56, 56, 48, 48, 48, 56, 64, 64, 96, 64. Modal: cotas horizontais "24" em x 836–860 e x 1228–1252, y 844.

---

# Linha inferior

```text
7. ELEVAÇÃO (card x 12, y 1160, w 344, h 168) — amostras 128 × 44, radius 12, borda 1 px
   E0 0/0/0/0%   x 44,  y 1176   legenda y 1224
   E1 0/1/2/12%  x 196, y 1176   legenda y 1224
   E2 0/2/6/16%  x 44,  y 1248   legenda y 1296
   E3 0/4/12/20% x 196, y 1248   legenda y 1296

8. RADIUS (card x 372, y 1160, w 256, h 100) — amostras 112 × 44
   12 px — Campos e botões   x 384, y 1176, radius 12   rótulo y 1190, legenda y 1228
   16 px — Cards e modais    x 504, y 1176, radius 16   rótulo y 1190, legenda y 1228

9. ÍCONES (Material Icons Outlined) (card x 644, y 1160, w 304, h 160)
   amostra 20 px: x 660, y 1176, 128 × 88 (ícone info 20 px, guia tracejado)
   amostra 24 px: x 804, y 1176, 128 × 88 (ícone home 24 px, guia tracejado)
   rótulo "20 px"/"24 px" y 1188; ícone centrado em y 1232; legenda y 1272 ("Ícones auxiliares" / "Ação / navegação")
   nota x 660, y 1294: "Referência conceitual dos wireframes."

10. ESTADOS (Componentes) (card x 964, y 1160, w 304, h 228)
   amostras x 980, w 272, h 28, radius 6; texto x 1016, y +6; ícone 16 px x 992, y +6
   Default             y 1176   borda 1 px                          radio_button_unchecked
   Focus               y 1212   borda 2 px WF-W-FOCUS               center_focus_strong
   Pressed / Selected  y 1248   fundo #DDEEFC, borda #0061FE, barra esquerda 4 px azul; check azul
   Disabled            y 1284   fundo SURFACE-ALT, borda tracejada WF-W-DISABLED; block
   Error               y 1320   borda 2 px #D32F2F; error_outline #D32F2F
   nota x 980, y 1356: "Hover: documentado; não obrigatório em mobile."
```

# 11. REGRAS GERAIS DE COMPONENTES

Card x 12, y 1452, w 620, h 120.

```text
amostra touch target: x 28, y 1468, 48 × 48, borda tracejada WF-W-FOCUS; ícone settings 24 px em (40, 1480)
título: x 92, y 1466, WF-LABEL — "Touch target mínimo: 48 × 48 px."
parágrafo: x 92, y 1488, w 520, até 3 linhas, WF-CAPTION, WF-W-TEXT-2
  "Aplicável a botões, ícones, itens de lista, navegação e demais áreas interativas. A área clicável deve respeitar o mínimo mesmo quando o elemento visual for menor."
```

# 12. BORDAS E DIVISORES

Card x 648, y 1452, w 620, h 120.

```text
amostra de borda: x 664, y 1468, 160 × 56, radius 12, borda 1 px; "Borda 1 px" centrado
título do divisor: x 848, y 1468, WF-LABEL — "Divisor 1 px"
divisor: x 848, y 1496, w 400, h 1, WF-W-BORDER
legenda: x 848, y 1504, w 400 — "Uso entre seções e listas quando necessário."
token: x 664, y 1540 — "Token claro: WF-W-BORDER #B5B5B5"
```

---

# 13. OBSERVAÇÕES TÉCNICAS

Card x 12, y 1636, w 1256, h 268 (base 1904). Duas colunas de 5 itens: número em x 28 e x 648; texto em x 56 e x 676 (w 572, até 2 linhas, WF-CAPTION); número em WF-LABEL; linhas em y 1656 + 50 × n (n = 0…4).

```text
1. O viewport representa a tela completa do celular: 360 × 800 px em escala 1:1.
2. A referência dimensional usa largura total 360 px, largura útil 336 px e margens laterais 12 + 12 px.
3. Não existe reserva fixa de faixa superior ou inferior de safe area nesta prancha-modelo.
4. O bitmap WF-VIEWPORT-360x800-clean.png deve permanecer fisicamente 360 × 800 px, inserido em 100%, sem resize.
5. Todos os elementos seguem grid de 4 px e escala de espaçamento 4 / 8 / 12 / 16 / 24 / 32 px.
6. Inter é tipografia técnica do wireframe e não tipografia oficial da marca SaOr.
7. Em páginas seguintes, repetir apenas elementos realmente persistentes.
8. Nomenclatura dos arquivos funcionais: <ID>-<PÁGINA>-<TOTAL>_v<VERSÃO>.png.
9. Interface multipágina só é aprovada quando todas as páginas Claro e Escuro estiverem aprovadas.
10. Cor nunca deve ser o único indicador de estado; cores, ícones e componentes são referências técnicas dos wireframes.
```

---

# Checklist (itens de spec ainda abertos)

```text
[ ] cromia adicional registrada em REGRAS-TECNICAS.md
[ ] bitmap derivado do viewport aceito (ou original restaurado)
[ ] título fora do card com barra azul e card sem borda aceitos na spec
[ ] canvas 1280 × 1920; viewport 360 × 800 em 1:1; nenhuma cota altera o bitmap
[ ] todas as áreas dentro do canvas (base documental 1904 ≤ 1908)
[ ] marca com SVG mestre e fontes oficiais
[ ] componentes com as medidas normativas
[ ] versão Escuro desta prancha
```
