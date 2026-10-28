# WF-TEMPLATE-C_v01 — Reprodução textual fiel da prancha final

```text
CANVAS FINAL — 1280 × 1920 px

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ SaOr / Sales Order │ WIREFRAME · MODELO C │ WF-TEMPLATE-C │ XX / YY │ v01 │ DD/MM/AAAA │ [✓] APROVADO E CONGELADO                                  │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

VIEWPORT                                      ESTRUTURA                                 COMPONENTES
(1) VIEWPORT TÉCNICO 360 x 800 px             (5) CANVAS E VIEWPORT                     (10) COMPONENTES (MEDIDAS)
┌──────────────────────────────────────────┐  ┌──────────────────────────────────────┐  ┌──────────────────────────────────────────────────────────┐
│ 360 px (viewport total)                  │  │ Canvas da prancha 1280 x 1920 px     │  │ APP BAR (56) | CAMPO OUTLINED (56)                       │
│ 12 | 336 | 12 px                         │  │ Viewport 360 x 800 px                │  │ BOTÃO PRIMÁRIO (48) | SECUNDÁRIO (48)                    │
│ ┌──────────────────────────┐             │  │ Escala 1:1 | Retrato | Margem 12 px  │  │ [G] Botão Texto + ICON BUTTON (48 x 48)                  │
│ │ O Título da Página [S][M]│             │  └──────────────────────────────────────┘  │ ITEM DE LISTA simples (56) / secund. (64)                │
│ │   Subtítulo da página    │             │                                            │ CARD (64) | MODAL / DIALOG (96)                          │
│ ├──────────────────────────┤             │  (6) COTAS DO VIEWPORT                     │ BOTTOM NAVIGATION (64)                                   │
│ │ Seção de Conteúdo        │             │  ┌──────────────────────────────────────┐  │ + cota vertical Primary à direita de cada amostra        │
│ │ Rótulo do campo          │             │  │ Largura total 360 | útil 336 px      │  └──────────────────────────────────────────────────────────┘
│ │ [ Texto de exemplo    v ]│             │  │ Margens 12 + 12 | Altura 800 px      │
│ │ [    Botão Primário     ]│             │  │ Escala 1:1                           │  (11) ESTADOS (Componentes)
│ │ [   Botão Secundário    ]│             │  └──────────────────────────────────────┘  ┌──────────────────────────────────────────────────────────┐
│ │ [G] Botão Texto          │             │                                            │ [o] Default                                              │
│ ├──────────────────────────┤             │  (7) GRID E SPACING                        │ [+] Focus                                                │
│ │ O Título do item       > │             │  ┌──────────────────────────────────────┐  │ [v] Pressed / Selected                                   │
│ │   Texto secundário       │             │  │ Grid base 4 px                       │  │ [x] Disabled                                             │
│ │ [ Título do Card        ]│             │  │ Escala 4/8/12/16/24/32 px            │  │ [!] Error                                                │
│ │ [i] Mensagem informativa │             │  │ Padding-base 16 / 12 px              │  └──────────────────────────────────────────────────────────┘
│ │ [ ^ Área de scroll v    ]│             │  └──────────────────────────────────────┘
│ ├──────────────────────────┤             │                                            (12) BORDAS E DIVISORES
│ │ Início Pedidos Clientes M│             │  FUNDAMENTOS                               ┌──────────────────────────────────────────────────────────┐
│ └──────────────────────────┘             │  (8) TIPOGRAFIA (Inter - Wireframe)        │ [ Borda de controle ] 1 px  [ ─── ] Divisor 1 px         │
│ 800 px (viewport total)                  │  ┌──────────────────────────────────────┐  └──────────────────────────────────────────────────────────┘
└──────────────────────────────────────────┘  │ WF-TITLE ... WF-CAPTION (6 linhas)   │
                                              └──────────────────────────────────────┘  (13) ELEVAÇÃO
(2) ÍCONES (Material Icons Outlined)                                                    ┌──────────────────────────────────────────────────────────┐
┌──────────────────────────────────────────┐  (9) PALETA TÉCNICA - ESCURO               │ [E0]  [E1]  [E2]  [E3]    (0/0/0/0% ... 0/4/12/20%)      │
│ [20 px] auxiliares  [24 px] ação/nav.    │  ┌──────────────────────────────────────┐  └──────────────────────────────────────────────────────────┘
│ Referência conceitual.                   │  │ ... (11 tokens neutros)              │
└──────────────────────────────────────────┘  │ ... (10 semânticas + 3 adicionais)   │
                                              │ 24 linhas, chips com HEX             │
(3) REGRAS GERAIS DE COMPONENTES              │                                      │
┌──────────────────────────────────────────┐  │                                      │
│ [ ] Touch target mínimo: 48 x 48 px.     │  │                                      │
│  Botões, ícones, listas, navegação.      │  │                                      │
└──────────────────────────────────────────┘  │                                      │
                                              │                                      │
(4) RADIUS                                    │                                      │
┌──────────────────────────────────────────┐  │                                      │
│ [12 px] [16 px]                          │  │                                      │
└──────────────────────────────────────────┘  │                                      │
                                              │                                      │
                                              │                                      │
                                              │                                      │
                                              │                                      │
                                              │                                      │
                                              │                                      │
                                              │                                      │
                                              │                                      │
                                              │                                      │
                                              │                                      │
                                              └──────────────────────────────────────┘


(14) OBSERVAÇÕES TÉCNICAS
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 1–5 (coluna esquerda)                          6–10 (coluna direita)                                                                           │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

# Especificação de implementação da prancha

## 1. Regra de leitura deste documento

A reprodução textual acima é a **referência conceitual de composição** da `WF-TEMPLATE-C_v01`: ordem das regiões, quais blocos existem, quais ficam lado a lado e a hierarquia geral. Ela **não é escala de caracteres para pixels**; as medidas valem somente nas seções abaixo.

```text
canvas:              1280 × 1920 px
margem estrutural:     12 px
grid base:              4 px
escala de spacing:      4 / 8 / 12 / 16 / 24 / 32 px
viewport físico:      360 × 800 px, escala 1:1
```

As coordenadas são **específicas desta prancha-modelo C_v01** e não são medidas universais de futuros wireframes funcionais T/M/E.

## 2. O que diferencia o Modelo C do Modelo B

```text
1. Título do bloco FORA do card: badge numerado + título (WF-SECTION) acima do card.
2. Card sem borda: fundo SURFACE, radius 16, sem sombra no black (ver 4.2 e D5). Antes: borda 1 px.
3. Quatro cabeçalhos de zona: VIEWPORT, ESTRUTURA, FUNDAMENTOS, COMPONENTES.
4. Viewport como elemento principal da coluna esquerda, com as cotas dentro do próprio card.
5. Sem bloco de legenda de cotas; RADIUS na coluna esquerda e ELEVAÇÃO na coluna direita.
6. Tabelas de medidas com linhas alternadas (zebra) e valores em peso 500.
7. Blocos reorganizados em 3 colunas (416 / 360 / 448) e renumerados de 1 a 14.
8. Observações em duas colunas (5 + 5), no rodapé.
9. Cromia: cotas e destaques em Primary; status em Success; marca com SVG mestre.
10. Estados com ícone à esquerda; Botão Texto com ícone à esquerda e texto colado ao ícone.
```

## 2.1 Origem e diferenças em relação ao white (WIREFRAME-TEXT.md 7.1)

Origem (WIREFRAME-TEXT.md, 7.1):

```text
Wireframe Text white de origem: WF-TEMPLATE-C_v02 (docs/wireframes/images/references/templates/white/wiframetext/)
Estado do white de origem:      Wireframe Text APROVADO E CONGELADO (Gates 1 a 6, Gates 2, 3 e 6 aprovados pelo responsável em 27/10/2026); PNG da origem e STATUS do cabeçalho APROVADO E CONGELADO em 27/10/2026
Regra: geometria e composição herdadas; mudam apenas paleta, ativos físicos e as decisões que dependem da paleta.
Geometria herdada continua GEOMETRIA DESTA PRANCHA (não passa a regra normativa).
Gates não herdados: o black registra os próprios estados (seção 3); Gates 2, 3 e 6 foram aprovados pelo responsável em 27/10/2026.
Numeração própria: esta é a v01 da variação black.
```

O WIREFRAME-TEXT.md 7.1 prevê a origem `APROVADO E CONGELADO`: o Wireframe Text white de origem está `APROVADO E CONGELADO`; o PNG da origem também está `APROVADO E CONGELADO`. Os estados do black são próprios e a aprovação do white não aprova este documento.

Diferenças em relação ao white de origem (todas DIFERENÇA INTENCIONAL; aprovadas nos Gates 2, 3 e 6 em 27/10/2026):

```text
D1 — Paleta: tokens WF-B-* e semânticas da tabela 6.6 de REGRAS-TECNICAS.md no lugar de WF-W-* e da tabela 6.5; HEX somente no bloco 9.
D2 — Viewport: references/black/WF-VIEWPORT-360x800.png (360 × 800 px, 1:1) no lugar do bitmap white.
D3 — Pares texto/fundo: razões recalculadas para a paleta escura (tabela 6.6); não há exceção de nível (todos os pares de texto em AAA).
D4 — Ícone do cabeçalho: assets/logo/saor-icon-para_fundos_escuros.png (variante preparada para fundos escuros; sem inversão manual nem filtro) no lugar de saor-icon-master.svg; ícone 44 × 44 em (24, 38), com o mesmo centro vertical do white; SaOr e SALES ORDER em BRAND (paleta escura).
D5 — Sombra dos cards e do cabeçalho: o tratamento documental de sombra do white não é perceptível sobre WF-B-BG e não é herdado (MONTAGEM-IMAGEM.md: não herdar sombra por semelhança visual); cards e cabeçalho ficam sem sombra e sem borda, separados pelo contraste tonal WF-B-SURFACE × WF-B-BG.
D6 — Elevação (amostras E0 a E3): parâmetros de sombra inalterados (REGRAS-TECNICAS.md); sobre superfície escura a sombra rgba(0,0,0,·) é pouco perceptível. As quatro amostras usam WF-B-SURFACE-ALT (token existente, mais claro que o card WF-B-SURFACE) como preenchimento, conforme a regra de REGRAS-TECNICAS.md, seção 8 (variação black); o nível é identificado pela legenda e pela sombra.
```

Todo o resto (composição, geometria, conteúdo textual, tipografia, componentes, ícones e regras específicas) é o da origem.

## 3. Hierarquia de autoridade e estado

```text
1. docs/Documento_Mestre.md — somente conteúdo e comportamento funcional
2. .specs/wireframes/REGRAS-TECNICAS.md — invariantes técnicos
3. .specs/wireframes/PROCESSO-PRANCHA.md — sequência e gates
4. .specs/wireframes/WIREFRAME-TEXT.md — contrato documental
5. docs/wireframes/images/README.md — estrutura operacional white / black
6. este WF-TEMPLATE-C_v01.md — composição específica desta alternativa
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

Esta v01 é a primeira versão da variação black e os estados acima são próprios (não herdados da origem white).

Registros:

```text
Gate 1 (técnico): canvas 1280 × 1920 px conforme REGRAS-TECNICAS.md — APROVADO E CONGELADO.
Gate 2: cabeçalho da v01 black, tokens da seção 6 (tabela 6.6) e STATUS (inclui D4) — aprovado explicitamente pelo responsável em 27/10/2026 (aprovação registrada neste Wireframe Text) — APROVADO E CONGELADO.
Gate 3: bitmap references/black/WF-VIEWPORT-360x800.png aprovado em 27/10/2026; posição, cotas e registro do gate aprovados explicitamente pelo responsável em 27/10/2026 (aprovação registrada neste Wireframe Text) — APROVADO E CONGELADO.
Gates 4 e 5 (técnicos): validados em 27/10/2026 depois dos Gates 2 e 3 estarem congelados — APROVADO E CONGELADO.
Gate 6: aprovado explicitamente pelo responsável em 27/10/2026 (aprovação registrada neste Wireframe Text) — APROVADO E CONGELADO.
Produção do PNG: gerado em 27/10/2026 a partir deste Wireframe Text e validado contra ele; aprovado explicitamente pelo responsável em 27/10/2026 (aprovação registrada neste Wireframe Text) — APROVADO E CONGELADO.
STATUS no cabeçalho: registrado como APROVADO E CONGELADO; o PNG foi regenerado com o STATUS aprovado (ícone check_circle e texto em Success) e revalidado.
Validação técnica dos Gates 4 e 5: 416 + 16 + 360 + 16 + 448 = 1256 px; viewport 12 + 336 + 12 = 360 px;
  todas as áreas x/y/w/h dentro do canvas 1280 × 1920 px; limite inferior documental y 1904 ≤ 1908; bloco 9 dentro do card (última linha termina em y 1584 ≤ 1608).
Cores: as lacunas da seção 6 (marcadas com *) foram aprovadas pelo responsável em 27/10/2026 (decisão registrada neste Wireframe Text);
  o registro formal em REGRAS-TECNICAS.md 6.7 é feito pelo responsável.
```

## 4. Decisões específicas da composição

As decisões abaixo pertencem a `WF-TEMPLATE-C_v01` quando não forem invariantes canônicas:

```text
- A paleta técnica black está em REGRAS-TECNICAS.md, seção 6 (tabela 6.6); as cores são citadas por token e o HEX consta somente no bloco 9.
- O viewport usa references/black/WF-VIEWPORT-360x800.png.
- Cards documentais podem aparecer sem borda porque REGRAS-TECNICAS.md exige borda somente quando necessária.
- Sem sombra nos cards e no cabeçalho (D5): a separação é tonal (WF-B-SURFACE sobre WF-B-BG).
```

### 4.1 Cores usadas e pares texto/fundo

As cores desta prancha são citadas pelo nome do token. O HEX consta somente no bloco 9. Cromia adicional: BRAND, On Brand e Zebra de tabela. Semânticas usadas: Primary, On Primary, Info BG, Error, Success.

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

### 4.2 Card e sombra

```text
fundo:   WF-B-SURFACE
borda:   nenhuma
radius:  16 px
sombra:  nenhuma (D5); separação tonal WF-B-SURFACE × WF-B-BG
```

### 4.3 Título de bloco (fora do card)

```text
altura da faixa de título: 32 px (card começa em y_título + 32)
badge: 22 × 22 px, radius 11, fundo BRAND, número WF-CAPTION 600 On Brand, centralizado
título: x_bloco + 30, y_título + 2, WF-SECTION, WF-B-TEXT
gap entre cards: 16 px
```

### 4.4 Cabeçalho de zona

```text
texto:   WF-CAPTION 600, letter-spacing 0.14em, WF-B-TEXT-2, uppercase
linha:   1 px WF-B-BORDER em y_texto + 20, largura = largura da coluna
acento:  40 × 3 px Primary em y_texto + 19, alinhado à esquerda
```

### 4.5 Tabela zebra (blocos 5, 6, 7, 8)

```text
passo da linha: 20 px
linhas pares (1ª, 3ª, 5ª...): faixa Zebra de tabela, radius 4, x_card + 8, largura = card − 16
rótulo: x_card + 16, y_linha + 2, WF-CAPTION, WF-B-TEXT-2 (bloco 8: WF-B-TEXT)
valor:  WF-CAPTION 500, WF-B-TEXT
```

---

# Canvas

```text
canvas: 1280 × 1920 px, retrato, margem 12 px
área útil: x 12, y 12, w 1256, h 1896
limites: esquerda 12 | direita 1268 | topo 12 | base 1908
```

# Cabeçalho

```text
área: x 12, y 12, w 1256, h 96 (limite inferior 108)
card: sem borda, radius 16, sem sombra (4.2, D5); divisores internos 1 px WF-B-BORDER

MARCA          x 12   w 156
IDENTIFICAÇÃO  x 168  w 384
METADADOS      x 552  w 716
156 + 384 + 716 = 1256
```

Marca:

```text
ícone: assets/logo/saor-icon-para_fundos_escuros.png, x 24, y 38, 44 × 44 (proporção original do arquivo; D4)
SaOr:         Google Sans Bold 700, 30/34, cor BRAND, x 76, y 34
SALES ORDER:  Quicksand Regular 400, 10/14, uppercase, tracking 0.14em, BRAND, x 77, y 70
```

Identificação (padding horizontal 24 px, x 192):

```text
WIREFRAME                                              y 20, WF-LABEL, tracking 0.08em
PRANCHA TÉCNICA - MODELO C                             y 40, WF-TITLE
(Viewport à esquerda + painel técnico à direita)       y 72, WF-CAPTION, WF-B-TEXT-2
```

Metadados — linha superior (y 12, h 64): rótulo em y 20 (WF-CAPTION, tracking 0.06em), valor em y 40 (WF-LABEL).

```text
ID      x 552  w 164   WF-TEMPLATE-C
PÁGINA  x 716  w 128   XX / YY
VERSÃO  x 844  w 124   v01
DATA    x 968  w 140   DD/MM/AAAA
STATUS  x 1108 w 160
```

STATUS: fundo WF-B-SURFACE, rótulo "STATUS" como os demais. Estado atual APROVADO E CONGELADO: ícone check_circle 20 px em (1120, 46) e valor em (1146, 38), w 114, 2 linhas "APROVADO E / CONGELADO", WF-CAPTION 600, ambos em Success. Enquanto AGUARDANDO APROVAÇÃO (regra de estado, não aplicável a esta versão congelada): sem ícone; valor em (1120, 38), w 140, 2 linhas "AGUARDANDO / APROVAÇÃO", WF-CAPTION 600, WF-B-TEXT-2.

```text
ícone check_circle: x 1120, y 46, 20 × 20
valor "APROVADO E CONGELADO": x 1146, y 38, w 114, 2 linhas, WF-CAPTION 600
```

Linha inferior (y 76, h 32): rótulo WF-CAPTION + valor WF-LABEL na mesma linha, y 84.

```text
BASELINE  x 552  w 164   v1.0
VARIAÇÃO  x 716  w 220   black
ETAPA     x 936  w 332   Wireframe Conceitual em Imagem
```

---

# Mapa geométrico principal

```text
COLUNA ESQUERDA  x 12   w 416
gap              16
COLUNA CENTRAL   x 444  w 360
gap              16
COLUNA DIREITA   x 820  w 448
416 + 16 + 360 + 16 + 448 = 1256
```

Cabeçalhos de zona (y 132, linha em y 152):

```text
VIEWPORT      x 12   w 416
ESTRUTURA     x 444  w 360
COMPONENTES   x 820  w 448
FUNDAMENTOS   x 444  w 360   y 712 (linha em y 732)
```

Blocos (y_título → card y, h → base):

```text
COLUNA ESQUERDA
1  VIEWPORT TÉCNICO 360 × 800 px      164 → 196,  h 892 → 1088
2  ÍCONES (Material Icons Outlined)   1104 → 1136, h 168 → 1304
3  REGRAS GERAIS DE COMPONENTES       1320 → 1352, h 104 → 1456
4  RADIUS                             1472 → 1504, h 104 → 1608

COLUNA CENTRAL
5  CANVAS E VIEWPORT                  164 → 196,   h 132 → 328
6  COTAS DO VIEWPORT                  344 → 376,   h 152 → 528
7  GRID E SPACING                     544 → 576,   h 112 → 688
8  TIPOGRAFIA (Inter - Wireframe)     744 → 776,   h 152 → 928
9  PALETA TÉCNICA — ESCURO            944 → 976,   h 632 → 1608

COLUNA DIREITA
10 COMPONENTES (MEDIDAS)              164 → 196,   h 848 → 1044
11 ESTADOS (Componentes)              1060 → 1092, h 204 → 1296
12 BORDAS E DIVISORES                 1312 → 1344, h 88 → 1432
13 ELEVAÇÃO                           1448 → 1480, h 128 → 1608

RODAPÉ
14 OBSERVAÇÕES TÉCNICAS (x 12, w 1256) 1664 → 1696, h 208 → 1904
```

Bases alinhadas: colunas esquerda, central e direita terminam em y 1608.

Limite inferior documental: y 1904 (≤ 1908).

---

# 1. VIEWPORT TÉCNICO 360 × 800 px

Card: x 12, y 196, w 416, h 892.

Bitmap obrigatório:

```text
docs/wireframes/images/references/black/WF-VIEWPORT-360x800.png  (variante física black; gerado em 27/10/2026 com a paleta da seção 6)
```

```text
posição: x 40, y 272, w 360, h 800 (limite direito 400, inferior 1072)
escala: 100% / 1:1
```

Proibido: redimensionar, ampliar, reduzir, esticar, recortar, reconstruir ou adaptar o bitmap.

Cotas (Primary, linha 1 px, setas de 5 px):

```text
Linhas de extensão (tracejado 2/2):
  x 40 e x 399, de y 228 a y 272
  x 52 e x 387, de y 254 a y 272

360 px (viewport total):
  linha y 234, de x 40 a x 400; rótulo centrado, y 226, fundo WF-B-SURFACE, WF-CAPTION 600

12 / 336 / 12:
  linha y 258, de x 40 a x 400; divisões em x 52 e x 387
  rótulo "336 px (largura útil)" centrado, y 250
  rótulos "12 px" à esquerda (x 13, alinhado à direita, w 26) e à direita (x 401, alinhado à esquerda)

800 px (viewport total):
  extensões horizontais x 400–424 em y 272 e y 1071
  linha vertical x 414, de y 273 a y 1071, setas nas pontas
  rótulo vertical "800 px (viewport total)" sobre a linha, centrado em y 672
```

Não existe reserva fixa de safe area superior ou inferior.

---

# 2. ÍCONES (Material Icons Outlined)

Card: x 12, y 1136, w 416, h 168.

```text
amostra 20 px: x 52, y 1152, w 160, h 88, borda 1 px, radius 12
amostra 24 px: x 228, y 1152, w 160, h 88, borda 1 px, radius 12
rótulo "20 px" / "24 px": y 1164, centrado, WF-CAPTION, WF-B-TEXT-2
ícone: centro da amostra (x + 80, y 1208), com guia tracejado 1 px
legenda: y 1248, centrada ("Ícones auxiliares" / "Ação / navegação")
nota: x 28, y 1270 — "Referência conceitual dos wireframes."
```

Ícones: info (20 px), home (24 px).

---

# 3. REGRAS GERAIS DE COMPONENTES

Card: x 12, y 1352, w 416, h 104.

```text
amostra touch target: x 28, y 1368, w 48, h 48, borda tracejada WF-B-FOCUS; ícone settings 24 px em (40, 1380)
título:   x 92, y 1366, WF-LABEL — "Touch target mínimo: 48 × 48 px."
parágrafo: x 92, y 1388, w 320, até 3 linhas, WF-CAPTION, WF-B-TEXT-2
           "Aplicável a botões, ícones, itens de lista, navegação e demais áreas interativas, mesmo quando o elemento visual for menor."
```

---

# 4. RADIUS

Card: x 12, y 1504, w 416, h 104. Amostras 128 × 44 px, borda 1 px.

```text
12 px — Campos e botões:  x 80,  y 1520, w 128, h 44, radius 12   legenda y 1572
16 px — Cards e modais:   x 232, y 1520, w 128, h 44, radius 16   legenda y 1572
```

Valor ("12 px" / "16 px") centrado na amostra, WF-LABEL; legenda centrada, WF-CAPTION, WF-B-TEXT-2.

---

# 5. CANVAS E VIEWPORT

Card: x 444, y 196, w 360, h 132. Tabela zebra (4.5) a partir de y 212; valor em x 620.

```text
Canvas da prancha       1280 × 1920 px
Viewport (interface)     360 × 800 px
Escala do viewport       1:1
Orientação               Retrato
Margem horizontal        12 px
```

# 6. COTAS DO VIEWPORT

Card: x 444, y 376, w 360, h 152. Tabela zebra a partir de y 392; valor em x 620.

```text
Largura total      360 px
Largura útil       336 px
Margem esquerda     12 px
Margem direita      12 px
Altura total       800 px
Escala              1:1
```

# 7. GRID E SPACING

Card: x 444, y 576, w 360, h 112. Tabela zebra a partir de y 592; valor em x 620.

```text
Grid base                 4 px
Escala                    4 / 8 / 12 / 16 / 24 / 32 px
Padding-base horizontal   16 px
Padding-base vertical     12 px
```

# 8. TIPOGRAFIA (Inter - Wireframe)

Card: x 444, y 776, w 360, h 152. Tabela zebra a partir de y 792; valor em x 572.

```text
WF-TITLE        20 px | 28 px | SemiBold 600
WF-SECTION      14 px | 20 px | SemiBold 600
WF-BODY         16 px | 24 px | Regular 400
WF-LABEL        14 px | 20 px | Medium 500
WF-ACTION-TEXT  16 px | 24 px | Medium 500
WF-CAPTION      12 px | 16 px | Regular 400
```

# 9. PALETA TÉCNICA — ESCURO

Card: x 444, y 976, w 360, h 632 (base 1608). Cópia da tabela 6.6 de `REGRAS-TECNICAS.md`: lista única de 24 linhas em três grupos (11 neutros, 10 semânticas, 3 de cromia adicional), sem títulos de grupo e sem nota.

```text
linha:   h 24, passo 24, a partir de y 992; faixa zebra (Zebra de tabela, radius 4, x 452, w 344, h 24) nas linhas ímpares de cada grupo (1ª, 3ª...)
token:   x 460, y_linha + 4, WF-CAPTION, WF-B-TEXT
chip:    x 692, y_linha + 2, w 96, h 20, preenchido com a cor; HEX centrado, 12 px
         WF-B-TEXT quando luminância < 0,3; senão WF-B-BG; chips com luminância > 0,7 recebem borda 1 px WF-B-BORDER
divisor: 1 px WF-B-BORDER, x 460, w 328, em y 1259 e y 1507 (8 px de avanço por divisor)
fim da lista: y 1584; margem inferior: 24 px (base 1608)
```

Linhas (y da linha):

```text
Neutros (linhas 1 a 11)
 1. WF-B-BG                   #121212   y 992
 2. WF-B-SURFACE              #1E1E1E   y 1016
 3. WF-B-SURFACE-ALT          #2A2A2A   y 1040
 4. WF-B-BORDER               #5E5E5E   y 1064
 5. WF-B-BORDER-CONTROL       #737373   y 1088
 6. WF-B-TEXT                 #F2F2F2   y 1112
 7. WF-B-TEXT-2               #C2C2C2   y 1136
 8. WF-B-ACTION               #E0E0E0   y 1160
 9. WF-B-DISABLED             #777777   y 1184
10. WF-B-FOCUS                #D0D0D0   y 1208
11. WF-B-STATUS               #A8A8A8   y 1232

Semânticas (linhas 12 a 21)
12. Primary                   #8ABEFF   y 1264
13. On Primary                #0F1115   y 1288
14. Secondary                 #B3B3E5   y 1312
15. Info                      #8ABEFF   y 1336
16. Error                     #FCA5A5   y 1360
17. Success                   #A7F3D0   y 1384
18. Warning (texto/ícone)     #FDE68A   y 1408
19. Warning (preenchimento)   #FDE68A   y 1432
20. On Warning                #0F1115   y 1456
21. Info BG                   #292E34   y 1480

Cromia adicional (linhas 22 a 24)
22. BRAND                     #F2F2F2   y 1512
23. On Brand                  #121212   y 1536
24. Zebra de tabela           #272727   y 1560
```

Os tokens WF-B-BORDER e WF-B-BORDER-CONTROL são as cores de bordas e divisores; não há token repetido no bloco 12.

---

# 10. COMPONENTES (MEDIDAS)

Card: x 820, y 196, w 448, h 848. Amostras: x 836, w 416. Rótulo de cada componente: WF-CAPTION, h 16, 16 px acima da amostra.

```text
4.1  APP BAR (56 px)                         rótulo y 212 | amostra y 228, h 56
4.2  CAMPO OUTLINED (56 px)                  rótulo y 288 | amostra y 304, h 56, radius 12
4.3  BOTÃO PRIMÁRIO (48 px)                  rótulo y 364 | amostra y 380, h 48, fundo Primary, texto On Primary
4.4  BOTÃO SECUNDÁRIO (48 px)                rótulo y 432 | amostra y 448, h 48
4.5  BOTÃO TEXTO (mínimo 48 px) + ICON BUTTON (48 × 48 px)
                                             rótulo y 500 | faixa y 516, h 48
4.6  ITEM DE LISTA - simples (56 px)         rótulo y 568 | amostra y 584, h 56
4.7  ITEM DE LISTA - secundário (64 px)      rótulo y 644 | amostra y 660, h 64
4.8  CARD (radius 16 px)                     rótulo y 728 | amostra y 744, h 64
4.9  MODAL / DIALOG (margem lateral 24 px)   rótulo y 812 | área y 828, h 96
4.10 BOTTOM NAVIGATION (64 px)               rótulo y 928 | amostra y 944, h 64
     observação y 1012: "Somente quando previsto na baseline."
```

Conteúdo das amostras:

```text
4.1  [menu] Título (WF-TITLE)                       [search]   ícones 24 px
4.2  borda 1 px WF-B-BORDER-CONTROL; Rótulo (WF-CAPTION, dentro do campo, y +7) / Texto de exemplo (WF-BODY, y +24) / [expand_more]
4.4  Botão Secundário: fundo WF-B-SURFACE, borda 1 px WF-B-BORDER-CONTROL
4.5  ICON BUTTON à ESQUERDA: x 836, y 516, 48 × 48, radius 12, borda 1 px WF-B-BORDER-CONTROL, ícone settings 24 px em (848, 528)
     Botão Texto colado ao ícone: x 900 (48 + 16 de gap), alinhado à esquerda, Primary, WF-ACTION-TEXT, y 528
4.6  avatar 40 × 40 (radius 20, SURFACE-ALT) em x +12 / y +8; título em x +64; chevron_right 24 px à direita
4.7  avatar 40 × 40 em x +12 / y +12; título em x +64 / y +10; secundário em x +64 / y +34; chevron_right
4.8  Título do Card (WF-SECTION) / Texto de exemplo do card. (WF-CAPTION), padding 16
4.9  fundo SURFACE-ALT; modal x 860, y 832, w 368, h 88, radius 16, sombra E3;
     alça 32 × 4 no topo; Título do Modal; Texto de exemplo do modal.;
     [Cancelar] 84 × 26 à esquerda, borda 1 px WF-B-BORDER-CONTROL; [Confirmar] 92 × 26 Primary (texto On Primary) à direita; margens laterais 24 px
4.10 4 itens com espaçamento de 104 px: Início (ativo, pílula Info BG 48 × 28, Primary), Pedidos, Clientes, Mais
```

Cotas de componente (Primary, estilo A_v02):

```text
coluna da cota: x 1260 (gutter de 16 px entre a amostra, que termina em 1252, e a borda do card, 1268)
colchetes horizontais 1255–1265 nos limites; linha vertical com setas; rótulo vertical "NN px" no centro
alturas: 56, 56, 48, 48, 48, 56, 64, 64, 96, 64 px (na ordem 4.1 a 4.10)
modal: cotas horizontais "24" em x 836–860 e x 1228–1252, y 876
```

---

# 11. ESTADOS (Componentes)

Card: x 820, y 1092, w 448, h 204. Amostras: x 836, w 416, h 28, radius 6, passo 36 px. Texto WF-CAPTION em x 872, y +6; ícone 16 px em x 848, y +6.

```text
Default             y 1108   borda 1 px WF-B-BORDER-CONTROL      ícone radio_button_unchecked  WF-B-TEXT
Focus               y 1144   borda 2 px WF-B-FOCUS      ícone center_focus_strong
Pressed / Selected  y 1180   fundo Info BG, borda Primary, barra esquerda 4 px Primary; ícone check Primary
Disabled            y 1216   fundo SURFACE-ALT, borda tracejada WF-B-DISABLED; texto e ícone block em WF-B-DISABLED
Error               y 1252   borda 2 px Error; texto e ícone error_outline em Error
```

Sem nota de hover (removida). Última amostra termina em y 1280; margem inferior 16 px.

---

# 12. BORDAS E DIVISORES

Card: x 820, y 1344, w 448, h 88. Duas amostras lado a lado, sem linha de token (os HEX de WF-B-BORDER e WF-B-BORDER-CONTROL constam no bloco 9).

```text
amostra de borda:   x 836,  y 1360, w 56, h 56, radius 12, borda 1 px WF-B-BORDER-CONTROL, vazia
  texto (x 904):    "Borda de controle" y 1362 WF-LABEL | "1 px" y 1384 WF-CAPTION WF-B-TEXT-2 | "(onde aplicável)" y 1400 WF-CAPTION WF-B-TEXT-2
amostra de divisor: x 1036, y 1360, w 72, h 56, radius 12, borda 1 px WF-B-BORDER
  linha interna:    x 1044, y 1388, w 56, h 1, WF-B-BORDER
  texto (x 1120):   "Divisor" y 1362 WF-LABEL | "1 px" y 1384 WF-CAPTION WF-B-TEXT-2 | "(entre seções e listas)" y 1400 WF-CAPTION WF-B-TEXT-2
```

---

# 13. ELEVAÇÃO

Card: x 820, y 1480, w 448, h 128. Quatro amostras em uma linha: w 88, h 52, radius 12, y 1500, passo 104.

```text
E0  0/0/0/0%      x 844    sem sombra
E1  0/1/2/12%     x 948    0 1px 2px rgba(0,0,0,.12)
E2  0/2/6/16%     x 1052   0 2px 6px rgba(0,0,0,.16)
E3  0/4/12/20%    x 1156   0 4px 12px rgba(0,0,0,.20)
```

Preenchimento das quatro amostras: WF-B-SURFACE-ALT (D6); borda 1 px WF-B-BORDER.

Nome (E0…E3) centrado na amostra, y 1516, WF-LABEL; legenda centrada, y 1564, WF-CAPTION, WF-B-TEXT-2.

---

# 14. OBSERVAÇÕES TÉCNICAS

Card: x 12, y 1696, w 1256, h 208 (base 1904; margem inferior do canvas 12 px a partir de 1908).

Duas colunas de 5 itens. Coluna esquerda: número em x 28, texto em x 56. Coluna direita: número em x 648, texto em x 676. Texto: w 572, até 2 linhas, WF-CAPTION; número WF-LABEL. Linhas em y 1712 + 38 × n (n = 0…4).

```text
Coluna esquerda
1. O viewport representa a tela completa do celular: 360 × 800 px em escala 1:1.
2. A referência dimensional usa largura total 360 px, largura útil 336 px e margens laterais 12 + 12 px.
3. Não existe reserva fixa de faixa superior ou inferior de safe area nesta prancha-modelo.
4. O bitmap do viewport deve permanecer fisicamente 360 × 800 px, inserido em 100%, sem resize.
5. Todos os elementos seguem grid de 4 px e escala de espaçamento 4 / 8 / 12 / 16 / 24 / 32 px.

Coluna direita
6. Inter é tipografia técnica do wireframe e não tipografia oficial da marca SaOr.
7. Em páginas seguintes, repetir apenas elementos realmente persistentes.
8. Nomenclatura dos arquivos funcionais: <ID>-<PÁGINA>-<TOTAL>_v<VERSÃO>.png.
9. Interface multipágina só é aprovada quando todas as páginas Claro e Escuro estiverem aprovadas.
10. Cor nunca deve ser o único indicador de estado; cores, ícones e componentes são referências técnicas dos wireframes.
```

---

# Sequência de construção

```text
01. Canvas 1280 × 1920 (Gate 1 — técnico)
02. Cabeçalho (Gate 2 — aprovação humana) — APROVADO E CONGELADO
03. Viewport em 100% / 1:1 em (40, 272) + cotas (Gate 3 — aprovação humana) — APROVADO E CONGELADO
04. Zonas e blocos 2 a 14 (Gates 4 e 5) — APROVADO E CONGELADO
05. Conferência integral do Wireframe Text (Gate 6 — aprovação humana) — APROVADO E CONGELADO
06. Produção do PNG — APROVADO E CONGELADO (gerado após o Gate 6 APROVADO E CONGELADO)
```

# Registro de validação desta versão

```text
[x] Gate 1 registrado como APROVADO E CONGELADO (técnico)
[x] Gates 2 e 3 registrados como APROVADO E CONGELADO (aprovação do responsável em 27/10/2026)
[x] Gates 4 e 5 (técnicos) validados e registrados como APROVADO E CONGELADO
[x] Gate 6 registrado como APROVADO E CONGELADO (aprovação do responsável em 27/10/2026)
[x] Produção do PNG registrada como APROVADO E CONGELADO (aprovação explícita do responsável em 27/10/2026)
[x] STATUS do cabeçalho registrado como APROVADO E CONGELADO; PNG regenerado com o STATUS aprovado e revalidado
[x] WF-TEMPLATE-C_v01 (black) é a versão vigente do Modelo C black
[x] origem registrada: WF-TEMPLATE-C_v02 (white), estado Wireframe Text APROVADO E CONGELADO; diferenças classificadas como DIFERENÇA INTENCIONAL (D1 a D6)
[x] viewport especificado: references/black/WF-VIEWPORT-360x800.png, 360 × 800 px em 1:1; nenhum ativo ou bitmap white reutilizado
[x] todas as cores usadas constam em REGRAS-TECNICAS.md, seção 6 (tabela 6.6); HEX somente no bloco 9
[x] pares texto/fundo registrados (sem exceção de nível)
[x] canvas 1280 × 1920; todas as áreas documentadas dentro do canvas
[x] REGRAS-TECNICAS.md seção 3.1 lista references/black/WF-VIEWPORT-360x800.png
[x] REGRAS-TECNICAS.md 6.7 — aprovação das lacunas de cor registrada em 27/10/2026
[x] REGRAS-TECNICAS.md seção 8 — regra de elevação na variação black registrada
[x] origem white WF-TEMPLATE-C_v02: Wireframe Text APROVADO E CONGELADO (7.1); PNG da origem APROVADO E CONGELADO
```

A variação `white` de origem é a `WF-TEMPLATE-C_v02` (pasta `templates/white/`), conforme `WIREFRAME-TEXT.md` 7.1.
