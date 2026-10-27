# WF-TEMPLATE-A_v01 — Reprodução textual fiel da prancha final

```text
CANVAS FINAL — 1280 × 1920 px

┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ SaOr / Sales Order │ WIREFRAME · PRANCHA TÉCNICA - MODELO A (Viewport central dominante) │ WF-TEMPLATE-A │ XX / YY │ v01 │ DD/MM/AAAA │ [ ] AGUARDANDO APROVAÇÃO │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

▌1. CANVAS E VIEWPORT                       ▌MODELO VIEWPORT                        ▌6. COMPONENTES (MEDIDAS)
┌────────────────────────────────────────┐                                          ┌──────────────────────────────────────────────────────────────────────────────┐
│ Canvas 1280 × 1920 | Viewport 360 × 800│     360 px (viewport total)              │ App Bar (56) | Campo Outlined (56)                                           │
│ Escala 1:1 | Retrato | Margem 12 px    │    12 | 336 px (largura útil) | 12       │ Botão Primário (48) | Secundário (48)                                        │
└────────────────────────────────────────┘     ┌───────────────────────────┐        │ [⚙] Icon Button + Botão Texto (48 × 48)                                      │
                                               │ (o) Título da Página [S][:]│       │ Item de lista simples (56) / secundário (64)                                 │
▌2. COTAS DO VIEWPORT                          │     Subtítulo da página   │        │ Card (64) | Modal (96)                                                       │
┌────────────────────────────────────────┐     │ Seção de Conteúdo         │        │ Bottom Navigation (64)                                                       │
│ 360 | 336 | 12 + 12 | 800 px | 1:1     │     │ Rótulo do campo           │        │ + cota Primary vertical à direita                                            │
└────────────────────────────────────────┘     │ [ Texto de exemplo     v ]│        │                                                                              │
                                               │ [    Botão Primário     ]│         │                                                                              │
▌3. GRID E SPACING                             │ [   Botão Secundário    ]│         │                                                                              │
┌────────────────────────────────────────┐     │ [G] Botão Texto           │        │                                                                              │
│ Grid 4 px | 4/8/12/16/24/32            │     │ (o) Título do item      > │        │                                                                              │
│ Padding-base 16 / 12 px                │     │ [ Título do Card        ]│         │                                                                              │
└────────────────────────────────────────┘     │ [i] Mensagem informativa  │        │                                                                              │
                                               │ [ ^ Área de scroll v    ]│         │                                                                              │
▌4. TIPOGRAFIA (Inter - Wireframe)             │ Início Pedidos Clientes Mais│      │                                                                              │
┌────────────────────────────────────────┐     └───────────────────────────┘        │                                                                              │
│ WF-TITLE ... WF-CAPTION (6 linhas)     │        800 px (viewport total)           │                                                                              │
└────────────────────────────────────────┘                                          └──────────────────────────────────────────────────────────────────────────────┘
                                            ▌7. ELEVAÇÃO
▌5. PALETA TÉCNICA — ESCURO                 ┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
┌────────────────────────────────────────┐  │ E0        E1        E2        E3        (4 amostras em uma fileira, legenda sob cada uma)                            │
│ [#HEX]  WF-B-BG                        │  └──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
│ [#HEX]  WF-B-SURFACE                   │
│ ... (11 tokens neutros)                │  ▌8. RADIUS                      ▌9. ÍCONES (Material Icons Outlined)      ▌10. ESTADOS (Componentes)
│ ──────────────────────────────         │  ┌────────────────────────────┐  ┌──────────────────────────────────────┐  ┌────────────────────────────────────────────┐
│ [#HEX]  Primary                        │  │ 12 px  Campos e botões     │  │ 20 px  info                          │  │ Default                                    │
│ [#HEX]  On Primary                     │  │ 16 px  Cards e modais      │  │ 24 px  home                          │  │ Focus                                      │
│ ... (10 semânticas + 3 adicionais)     │  │                            │  │ Referência conceitual                │  │ Pressed / Selected                         │
│                                        │  │                            │  │                                      │  │ Disabled                                   │
│                                        │  │                            │  │                                      │  │ Error                                      │
│                                        │  │                            │  │                                      │  │                                            │
│                                        │  │                            │  │                                      │  │                                            │
│                                        │  │                            │  │                                      │  │                                            │
└────────────────────────────────────────┘  └────────────────────────────┘  └──────────────────────────────────────┘  └────────────────────────────────────────────┘

▌11. REGRAS GERAIS DE COMPONENTES                                                  ▌12. BORDAS E DIVISORES
┌───────────────────────────────────────────────────────────────────────────────┐  ┌───────────────────────────────────────────────────────────────────────────────┐
│ [ ] Touch target mínimo 48 × 48 px                                            │  │ [ ] Borda de controle 1 px | [──] Divisor 1 px (entre seções e listas)        │
└───────────────────────────────────────────────────────────────────────────────┘  └───────────────────────────────────────────────────────────────────────────────┘

▌13. OBSERVAÇÕES TÉCNICAS
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ (1)–(5) esquerda                                                   (6)–(10) direita                                                                              │
│                                                                                                                                                                  │
│                                                                                                                                                                  │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

# Especificação de implementação da prancha

## 1. Regra de leitura deste documento

A reprodução textual acima é a **referência conceitual de composição** da `WF-TEMPLATE-A_v01`. Não é escala de caracteres para pixels; as medidas valem somente nas seções abaixo, que são **específicas desta prancha-modelo** e não medidas universais de futuros wireframes T/M/E.

```text
canvas:              1280 × 1920 px
margem estrutural:     12 px
grid base:              4 px
escala de spacing:      4 / 8 / 12 / 16 / 24 / 32 px
viewport físico:      360 × 800 px, escala 1:1
```


## 2. Origem e diferenças em relação ao white (WIREFRAME-TEXT.md 7.1)

Origem (WIREFRAME-TEXT.md, 7.1):

```text
Wireframe Text white de origem: WF-TEMPLATE-A_v04 (docs/wireframes/images/references/templates/white/wiframetext/)
Estado do white de origem:      Wireframe Text APROVADO E CONGELADO (Gates 1 a 6, Gates 2, 3 e 6 aprovados pelo responsável em 27/10/2026); PNG da origem e STATUS do cabeçalho APROVADO E CONGELADO em 27/10/2026
Regra: geometria e composição herdadas; mudam apenas paleta, ativos físicos e as decisões que dependem da paleta.
Geometria herdada continua GEOMETRIA DESTA PRANCHA (não passa a regra normativa).
Gates não herdados: o black registra os próprios estados (seção 3); Gates 2, 3 e 6 exigem nova aprovação humana.
Numeração própria: esta é a v01 da variação black.
```

O WIREFRAME-TEXT.md 7.1 prevê a origem `APROVADO E CONGELADO`: o Wireframe Text white de origem está `APROVADO E CONGELADO`; o PNG da origem também está `APROVADO E CONGELADO`. Os estados do black são próprios e a aprovação do white não aprova este documento.

Diferenças em relação ao white de origem (todas DIFERENÇA INTENCIONAL; aguardam aprovação nos Gates 2, 3 e 6):

```text
D1 — Paleta: tokens WF-B-* e semânticas da tabela 6.6 de REGRAS-TECNICAS.md no lugar de WF-W-* e da tabela 6.5; HEX somente no bloco 5.
D2 — Viewport: references/black/WF-VIEWPORT-360x800.png (360 × 800 px, 1:1) no lugar do bitmap white.
D3 — Pares texto/fundo: razões recalculadas para a paleta escura (tabela 6.6); não há exceção de nível (todos os pares de texto em AAA).
D4 — Ícone do cabeçalho: assets/logo/saor-icon-para_fundos_escuros.png (variante preparada para fundos escuros; sem inversão manual nem filtro) no lugar de saor-icon-master.svg; ícone 44 × 44 em (24, 38), com o mesmo centro vertical do white; SaOr e SALES ORDER em BRAND (paleta escura).
D5 — Sombra dos cards e do cabeçalho: o tratamento documental de sombra do white não é perceptível sobre WF-B-BG e não é herdado (MONTAGEM-IMAGEM.md: não herdar sombra por semelhança visual); cards e cabeçalho ficam sem sombra e sem borda, separados pelo contraste tonal WF-B-SURFACE × WF-B-BG.
D6 — Elevação (amostras E0 a E3): parâmetros inalterados (REGRAS-TECNICAS.md); sobre superfície escura a sombra rgba(0,0,0,·) é pouco perceptível, e o nível é identificado pela legenda numérica.
```

Todo o resto (composição, geometria, conteúdo textual, tipografia, componentes, ícones e regras específicas) é o da origem.

## 3. Hierarquia de autoridade e estado

```text
1. docs/Documento_Mestre.md — somente conteúdo e comportamento funcional
2. .specs/wireframes/REGRAS-TECNICAS.md — invariantes técnicos
3. .specs/wireframes/PROCESSO-PRANCHA.md — sequência e gates
4. .specs/wireframes/WIREFRAME-TEXT.md — contrato documental
5. docs/wireframes/images/README.md — estrutura operacional white / black
6. este WF-TEMPLATE-A_v01.md — composição específica desta alternativa
7. PNG correspondente — resultado visual, nunca fonte normativa superior
```


```text
Gate 1 — Canvas:                       APROVADO E CONGELADO
Gate 2 — Título / Cabeçalho:           AGUARDANDO APROVAÇÃO
Gate 3 — Viewport Técnico:             AGUARDANDO APROVAÇÃO
Gate 4 — Área restante calculada:      BLOQUEADO POR GATE ANTERIOR
Gate 5 — Demais elementos definidos:   BLOQUEADO POR GATE ANTERIOR
Gate 6 — Wireframe Text completo:      BLOQUEADO POR GATE ANTERIOR
Produção do PNG:                       BLOQUEADO POR GATE ANTERIOR
STATUS no cabeçalho:                   AGUARDANDO APROVAÇÃO
```

Esta v01 é a primeira versão da variação black e os estados acima são próprios (não herdados da origem white).

Registros:

```text
Gate 1 (técnico): canvas 1280 × 1920 px conforme REGRAS-TECNICAS.md — APROVADO E CONGELADO.
Gate 2: cabeçalho da v01 black, tokens da seção 6 (tabela 6.6) e STATUS AGUARDANDO APROVAÇÃO — aguarda aprovação humana (inclui D4).
Gate 3: o bitmap references/black/WF-VIEWPORT-360x800.png foi aprovado pelo responsável em 27/10/2026 (comunicado na conversa);
        a posição, as cotas e o registro formal do Gate 3 neste documento aguardam aprovação humana.
Gates 4 e 5 (técnicos): permanecem BLOQUEADO POR GATE ANTERIOR até os Gates 2 e 3 estarem APROVADO E CONGELADO.
Pré-validação técnica (informativa, não conclui gate): 336 + 16 + 440 + 16 + 448 = 1256 px; viewport 12 + 336 + 12 = 360 px;
  todas as áreas x/y/w/h dentro do canvas 1280 × 1920 px; limite inferior documental y 1904 ≤ 1908; bloco 5 dentro do card (última linha termina em y 1416 ≤ 1428).
Cores: as lacunas da seção 6 (marcadas com *) foram aprovadas pelo responsável em 27/10/2026 (comunicado na conversa);
  o registro formal em REGRAS-TECNICAS.md 6.7 é feito pelo responsável.
```

As decisões visuais desta prancha permanecem específicas de `WF-TEMPLATE-A_v01` quando não forem invariantes canônicas. A paleta técnica black está em `REGRAS-TECNICAS.md`, seção 6 (tabela 6.6). Card sem borda, título fora do card e chips cromáticos documentais não constituem, por si só, desvios das regras canônicas.

## 4. Padrões visuais

### 4.1 Título de bloco (fora do card)

```text
faixa de título: 32 px (o card começa em y_título + 32)
barra: 4 × 20 px, radius 2, Primary, em (x_bloco, y_título + 2)
texto: "N. TÍTULO" em caixa alta, WF-SECTION 14/20 600, WF-B-TEXT, x_bloco + 14, y_título + 2
       (texto entre parênteses mantém a caixa original)
gap entre blocos: 16 px (24 a 32 px entre seções)
coluna central: título "MODELO VIEWPORT", sem numeração, mesmo estilo (barra em x 364, texto em x 378)
```

### 4.2 Card

```text
fundo WF-B-SURFACE · sem borda · radius 16
sombra: nenhuma (D5); separação tonal WF-B-SURFACE × WF-B-BG
```

### 4.3 Tabela zebra (blocos 1 a 4)

```text
passo da linha: 20 px; linhas ímpares com faixa Zebra de tabela (radius 4, x_card + 8, largura = card − 16)
rótulo: x_card + 16, y_linha + 2, WF-CAPTION, WF-B-TEXT-2 (bloco 4: WF-B-TEXT)
valor: WF-CAPTION 500, WF-B-TEXT
```

### 4.4 Cores usadas e pares texto/fundo

As cores desta prancha são citadas pelo nome do token. O HEX consta somente no bloco 5. Cromia adicional: BRAND, On Brand e Zebra de tabela. Semânticas usadas: Primary, On Primary, Info BG, Error, Success.

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

Sem exceção de nível nos pares acima (todos AAA); a seção 6.6 registra os demais pares.

---

# Canvas e cabeçalho

```text
área útil: x 12, y 12, w 1256, h 1896 · limites: esq 12 | dir 1268 | topo 12 | base 1908
cabeçalho: x 12, y 12, w 1256, h 96 (card sem borda, sem sombra (4.2, D5), divisores 1 px WF-B-BORDER)
MARCA x 12 w 156 | IDENTIFICAÇÃO x 168 w 384 | METADADOS x 552 w 716  (156 + 384 + 716 = 1256)
```

Marca: ícone `assets/logo/saor-icon-para_fundos_escuros.png` (x 24, y 38, 44 × 44, proporção original do arquivo; D4); "SaOr" Google Sans Bold 700 30/34 BRAND (x 76, y 34); "SALES ORDER" Quicksand 400 10/14 uppercase, tracking 0.14em, BRAND (x 77, y 70).

Identificação (x 192):

```text
WIREFRAME                           y 20, WF-LABEL, tracking 0.08em
PRANCHA TÉCNICA - MODELO A          y 40, WF-TITLE
(Viewport central dominante)        y 72, WF-CAPTION, WF-B-TEXT-2
```

Metadados — linha superior (y 12, h 64; rótulo y 20, valor y 40):

```text
ID      x 552  w 164   WF-TEMPLATE-A
PÁGINA  x 716  w 128   XX / YY
VERSÃO  x 844  w 124   v01
DATA    x 968  w 140   DD/MM/AAAA
STATUS  x 1108 w 160   AGUARDANDO APROVAÇÃO
```

STATUS: fundo WF-B-SURFACE. Enquanto AGUARDANDO APROVAÇÃO (estado atual desta v01 black): sem ícone; valor em (1120, 38), w 140, 2 linhas "AGUARDANDO / APROVAÇÃO", WF-CAPTION 600, WF-B-TEXT-2. Ao ser registrado APROVADO E CONGELADO: ícone check_circle 20 px em (1120, 46) e valor em (1146, 38), w 114, 2 linhas "APROVADO E / CONGELADO", WF-CAPTION 600, ambos em Success.

Linha inferior (y 76, h 32; rótulo WF-CAPTION + valor WF-LABEL na mesma linha, y 84):

```text
BASELINE  x 552  w 164   v1.0
VARIAÇÃO  x 716  w 220   black
ETAPA     x 936  w 332   Wireframe Conceitual em Imagem
```

---

# Mapa geométrico principal

```text
COLUNA ESQUERDA  x 12   w 336
gap              16
COLUNA CENTRAL   x 364  w 440   (título + viewport, sem card)
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
5  PALETA TÉCNICA — ESCURO          872 → 904,   h 524 → 1428

COLUNA CENTRAL (x 364, w 440)
   MODELO VIEWPORT (título)         132           barra x 364 y 134 · texto x 378 y 134
   viewport + cotas                 y 138 → 1008  (bitmap y 208 → 1008)

COLUNA DIREITA (x 820, w 448)
6  COMPONENTES (MEDIDAS)            132 → 164,   h 848 → 1012

FAIXA DE ELEVAÇÃO (x 372, w 896)
7  ELEVAÇÃO                         1036 → 1068, h 100 → 1168

LINHA DOS BLOCOS 8, 9 e 10 (y_título 1192 → y_card 1224, h 204 → 1428)
8  RADIUS                           x 372  w 256
9  ÍCONES (Material Icons Outlined) x 644  w 304
10 ESTADOS (Componentes)            x 964  w 304

REGRAS E BORDAS (y_título 1452 → y_card 1484, h 88 → 1572)
11 REGRAS GERAIS DE COMPONENTES     x 12   w 620
12 BORDAS E DIVISORES               x 648  w 620

RODAPÉ
13 OBSERVAÇÕES TÉCNICAS             x 12   w 1256  y_título 1596 → y_card 1628, h 276 → 1904
```

Limite inferior documental: y 1904 (≤ 1908). A base do bloco 5 coincide com a base dos blocos 8, 9 e 10 (y 1428).

---

# Viewport central

Título "MODELO VIEWPORT" (ver 4.1). Sem card. O bitmap fica entre as colunas, sobre o fundo da prancha.

```text
arquivo: docs/wireframes/images/references/black/WF-VIEWPORT-360x800.png (variante física black; gerado em 27/10/2026 com a paleta da seção 6)
posição: x 404, y 208, w 360, h 800 (limite direito 764, inferior 1008)
escala: 100% / 1:1
cálculo horizontal: coluna 440 − bitmap 360 = 80; 80 / 2 = 40; 364 + 40 = x 404
cálculo vertical: o grupo cotas + viewport está em y 208 (herdado da origem white) para liberar o título em y 132
```

Proibido: redimensionar, ampliar, reduzir, esticar, recortar, reconstruir ou adaptar o bitmap. Sem safe area.

Cotas (Primary, linha 1 px, setas 5 px de comprimento × 6 px de largura, rótulos WF-CAPTION 600 sobre fundo da prancha com padding horizontal 6 px):

```text
Linhas de extensão tracejadas (2/2):
  x 404 e x 763, de y 164 a y 208
  x 416 e x 751, de y 190 a y 208
360 px (viewport total):    linha y 170, x 404–764, setas nas pontas; rótulo centrado em x 584, y 162
12 | 336 | 12:              linha y 194, x 404–764; divisões em x 416 e x 751; setas nas pontas de cada trecho
  rótulo "336 px (largura útil)" centrado em x 584, y 186
  rótulos "12 px": alinhado à direita, terminando em x 403 (y 186), e começando em x 765 (y 186)
800 px (viewport total):
  extensões horizontais tracejadas x 764–788 em y 208 e y 1007
  linha vertical x 778, de y 209 a y 1007, setas nas pontas
  rótulo vertical (lê-se de baixo para cima) sobre a linha, centrado em y 608
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

## 5. PALETA TÉCNICA — ESCURO

Card x 12, y 904, w 336, h 524 (base 1428). Cópia da tabela 6.6 de `REGRAS-TECNICAS.md`: lista única de 24 linhas em três grupos (11 neutros, 10 semânticas, 3 de cromia adicional), sem títulos de grupo e sem nota. Linhas de 20 px a partir de y 920; entre grupos, divisor de 1 px WF-B-BORDER em x 28, w 304, nas posições y 1143 e y 1351 (8 px de avanço por divisor). Faixa zebra (Zebra de tabela, radius 4, x 20, w 320, h 20) nas linhas ímpares de cada grupo (1ª, 3ª, ...). Chip preenchido com a cor em x 28, w 64, h 16, y_linha + 2; HEX centrado (12 px, WF-CAPTION; WF-B-TEXT quando luminância < 0,3; senão WF-B-BG). Chips com luminância > 0,7 recebem borda de 1 px WF-B-BORDER. Nome do token em x 104, y_linha + 2, WF-CAPTION, WF-B-TEXT. Última linha termina em y 1416; margem inferior 12 px.

```text
Neutros (linhas 1 a 11)
 1. WF-B-BG                   #121212   y 920
 2. WF-B-SURFACE              #1E1E1E   y 940
 3. WF-B-SURFACE-ALT          #2A2A2A   y 960
 4. WF-B-BORDER               #5E5E5E   y 980
 5. WF-B-BORDER-CONTROL       #737373   y 1000
 6. WF-B-TEXT                 #F2F2F2   y 1020
 7. WF-B-TEXT-2               #C2C2C2   y 1040
 8. WF-B-ACTION               #E0E0E0   y 1060
 9. WF-B-DISABLED             #777777   y 1080
10. WF-B-FOCUS                #D0D0D0   y 1100
11. WF-B-STATUS               #A8A8A8   y 1120

Semânticas (linhas 12 a 21)
12. Primary                   #8ABEFF   y 1148
13. On Primary                #0F1115   y 1168
14. Secondary                 #B3B3E5   y 1188
15. Info                      #8ABEFF   y 1208
16. Error                     #FCA5A5   y 1228
17. Success                   #A7F3D0   y 1248
18. Warning (texto/ícone)     #FDE68A   y 1268
19. Warning (preenchimento)   #FDE68A   y 1288
20. On Warning                #0F1115   y 1308
21. Info BG                   #292E34   y 1328

Cromia adicional (linhas 22 a 24)
22. BRAND                     #F2F2F2   y 1356
23. On Brand                  #121212   y 1376
24. Zebra de tabela           #272727   y 1396
```

---


# 6. COMPONENTES (MEDIDAS)

Card x 820, y 164, w 448, h 848. Amostras x 836, w 416. Rótulo WF-CAPTION, h 16, 16 px acima da amostra. Geometria idêntica à do modelo C (bloco 12), com o card em y 164.

```text
4.1  APP BAR (56 px)                         rótulo y 180 | amostra y 196, h 56
4.2  CAMPO OUTLINED (56 px)                  rótulo y 256 | amostra y 272, h 56, radius 12
4.3  BOTÃO PRIMÁRIO (48 px)                  rótulo y 332 | amostra y 348, h 48, fundo Primary, texto On Primary
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
4.1  avatar 40 × 40 (radius 20, SURFACE-ALT) em x +12 / y +8; "Título da Página" (WF-SECTION) x +64 / y +10;
     "Subtítulo da página" (WF-CAPTION, WF-B-TEXT-2) x +64 / y +30; [search] 24 px em x 1184, y 212;
     [more_vert] 24 px em x 1216, y 212 (extremo direito, 12 px de margem); sem logo
4.2  Rótulo (WF-CAPTION, y +7) / Texto de exemplo (WF-BODY, y +24) / expand_more
4.5  Icon Button à ESQUERDA: x 836, y 484, 48 × 48, radius 12, borda 1 px WF-B-BORDER-CONTROL, ícone settings 24 px em (848, 496)
     Botão Texto colado ao ícone: x 900, Primary, WF-ACTION-TEXT, y 496
4.6  avatar 40 × 40 (radius 20, SURFACE-ALT) x +12 / y +8; título x +64; chevron_right 24 px
4.7  avatar 40 × 40 x +12 / y +12; título x +64 / y +10; secundário x +64 / y +34; chevron_right
4.8  Título do Card (WF-SECTION) / Texto de exemplo do card. (WF-CAPTION), padding 16
4.9  fundo SURFACE-ALT; modal x 860, y 800, w 368, h 88, radius 16, sombra E3, alça 32 × 4;
     Título do Modal; Texto de exemplo do modal.; [Cancelar] 84 × 26; [Confirmar] 92 × 26 Primary
4.10 itens a cada 104 px: Início (ativo, pílula Info BG 48 × 28, Primary), Pedidos, Clientes, Mais
```

Cotas de componente (Primary, estilo A_v02): coluna em x 1260 (gutter de 16 px entre a amostra, que termina em 1252, e o card, 1268); colchetes 1255–1265; rótulo vertical "NN px" no centro. Alturas: 56, 56, 48, 48, 48, 56, 64, 64, 96, 64. Modal: cotas horizontais "24" em x 836–860 e x 1228–1252, y 844.

---

# Faixa de elevação e linha dos blocos 8, 9 e 10

```text
7. ELEVAÇÃO (card x 372, y 1068, w 896, h 100) — amostras 128 × 44, radius 12, borda 1 px WF-B-BORDER, em uma fileira
   quatro colunas de 224 px a partir de x 372; amostra centrada na coluna (x = 372 + 224·k + 48), y 1084
   rótulo (E0…E3, WF-LABEL) centrado na amostra, y +12; legenda (WF-CAPTION, WF-B-TEXT-2) centrada, y 1132
   E0 0/0/0/0%    x 420   sem sombra
   E1 0/1/2/12%   x 644   sombra 0 1px 2px rgba(0,0,0,.12)
   E2 0/2/6/16%   x 868   sombra 0 2px 6px rgba(0,0,0,.16)
   E3 0/4/12/20%  x 1092  sombra 0 4px 12px rgba(0,0,0,.20)

8. RADIUS (card x 372, y 1224, w 256, h 204) — amostras 112 × 44
   12 px — Campos e botões   x 384, y 1240, radius 12   rótulo y 1254, legenda y 1292
   16 px — Cards e modais    x 504, y 1240, radius 16   rótulo y 1254, legenda y 1292

9. ÍCONES (Material Icons Outlined) (card x 644, y 1224, w 304, h 204)
   amostra 20 px: x 660, y 1240, 128 × 88, radius 12, borda 1 px (ícone info 20 px, guia tracejado do tamanho do ícone)
   amostra 24 px: x 804, y 1240, 128 × 88, radius 12, borda 1 px (ícone home 24 px, guia tracejado do tamanho do ícone)
   rótulo "20 px"/"24 px" y 1252; ícone centrado em y 1296; legenda y 1336 ("Ícones auxiliares" / "Ação / navegação")
   nota x 660, y 1358: "Referência conceitual dos wireframes."

10. ESTADOS (Componentes) (card x 964, y 1224, w 304, h 204)
   amostras x 980, w 272, h 28, radius 6; texto x 1016, y +6; ícone 16 px x 992, y +6
   Default             y 1240   borda 1 px WF-B-BORDER-CONTROL      radio_button_unchecked
   Focus               y 1276   borda 2 px WF-B-FOCUS               center_focus_strong
   Pressed / Selected  y 1312   fundo Info BG, borda Primary, barra esquerda 4 px Primary; check Primary
   Disabled            y 1348   fundo SURFACE-ALT, borda tracejada WF-B-DISABLED; block
   Error               y 1384   borda 2 px Error; error_outline Error
   (sem nota de hover)
```

# 11. REGRAS GERAIS DE COMPONENTES

Card x 12, y 1484, w 620, h 88.

```text
amostra touch target: x 28, y 1500, 48 × 48, borda tracejada WF-B-FOCUS; ícone settings 24 px em (40, 1512)
título: x 92, y 1498, WF-LABEL — "Touch target mínimo: 48 × 48 px."
parágrafo: x 92, y 1520, w 520, até 3 linhas, WF-CAPTION, WF-B-TEXT-2
  "Aplicável a botões, ícones, itens de lista, navegação e demais áreas interativas. A área clicável deve respeitar o mínimo mesmo quando o elemento visual for menor."
```

# 12. BORDAS E DIVISORES

Card x 648, y 1484, w 620, h 88. Amostra à esquerda e texto à direita, para borda e divisor.

```text
amostra de borda:   x 664, y 1500, 80 × 56, radius 12, borda 1 px WF-B-BORDER-CONTROL, fundo SURFACE, vazia
  texto (x 760):    "Borda de controle" y 1502 WF-LABEL · "1 px" y 1522 WF-CAPTION WF-B-TEXT · "(onde aplicável)" y 1538 WF-CAPTION WF-B-TEXT-2
amostra de divisor: x 972, y 1500, 80 × 56, radius 12, borda 1 px WF-B-BORDER, fundo SURFACE
  linha interna:    x 984, y 1528, w 56, h 1, WF-B-BORDER
  texto (x 1068):   "Divisor" y 1502 WF-LABEL · "1 px" y 1522 WF-CAPTION WF-B-TEXT · "(entre seções e listas)" y 1538 WF-CAPTION WF-B-TEXT-2
(sem linha de token: os HEX de WF-B-BORDER e WF-B-BORDER-CONTROL constam no bloco 5)
```

---


# 13. OBSERVAÇÕES TÉCNICAS

Card x 12, y 1628, w 1256, h 276 (base 1904). Duas colunas de 5 itens: marcador em x 28 e x 648; texto em x 56 e x 676, y_linha + 2 (w 572, até 2 linhas, WF-CAPTION, WF-B-TEXT); linhas em y 1648 + 52 × n (n = 0…4). Marcador: círculo 22 × 22, radius 11, Primary, em (x, y_linha − 1), número On Primary centralizado, WF-CAPTION 600.

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


---

# Detalhes complementares de montagem (não numerados nas seções acima)

```text
Cabeçalho: rótulos ID/PÁGINA/VERSÃO/DATA em x_célula + 12, y 20, WF-CAPTION, WF-B-TEXT-2, tracking 0.06em; valores em x_célula + 12, y 40, WF-LABEL.
           Linha inferior: rótulo (WF-CAPTION, WF-B-TEXT-2, tracking 0.06em) em x_célula + 12, y 84 + gap 8 + valor (WF-LABEL) na mesma linha.
           Divisores: verticais x 168 e 552 (y 13–107); x 716, 844, 968, 1108 (y 13–76); x 716 e 936 (y 77–107); horizontal y 76 de x 553 a 1267.
Rótulos dos componentes do bloco 6: texto "NOME (medida)" sem o prefixo 4.x, WF-CAPTION, WF-B-TEXT, x 836.
Amostras do bloco 6: fundo SURFACE, borda 1 px WF-B-BORDER; radius: App Bar 0, Campo 12, botões 12, itens de lista 12, card 16. Controles demonstrados (Campo Outlined, Botão Secundário e Icon Button): borda 1 px WF-B-BORDER-CONTROL; Botão Secundário fundo SURFACE com borda.
  4.2 rótulo x 852 (WF-B-TEXT-2); texto x 852; expand_more 24 px a 16 px da borda direita, y +16
  4.6/4.7 chevron_right 24 px a 12 px da borda direita; 4.7 secundário: "Texto secundário adicional" (WF-CAPTION, WF-B-TEXT-2)
  4.8 título y +10, texto y +34
  4.9 alça 32 × 4 radius 2 WF-B-BORDER em (1028, 806); título x 876 y 814 (WF-SECTION); texto x 876 y 834; botões y 854, radius 6, texto WF-LABEL;
      Cancelar x 876 (borda 1 px WF-B-BORDER-CONTROL); Confirmar x 1120 (fundo Primary, texto On Primary)
  4.10 ícones home, description, people, more_horiz 24 px centrados em cada coluna de 104 px, y +10; rótulo y +42 centrado (WF-CAPTION); ativo: pílula Info BG 48 × 28 radius 14 em y +8, ícone e texto Primary (600)
Cotas de componente: colchetes 11 px em 1255–1265, linha vertical x 1260 com setas; rótulo vertical sobre a linha, fundo SURFACE.
Estados: barra esquerda do Pressed/Selected 4 px, radius esquerdo 6.
Elevação: E3 do modal 0 4px 12px rgba(0,0,0,.20).
```

---

# Registro de validação desta versão

```text
[x] Gate 1 registrado como APROVADO E CONGELADO (técnico)
[ ] Gate 2 — AGUARDANDO APROVAÇÃO humana
[ ] Gate 3 — AGUARDANDO APROVAÇÃO humana (bitmap aprovado em 27/10/2026; posição e cotas pendentes)
[ ] Gates 4 e 5 — BLOQUEADO POR GATE ANTERIOR
[ ] Gate 6 — BLOQUEADO POR GATE ANTERIOR
[ ] Produção do PNG — BLOQUEADO POR GATE ANTERIOR
[x] origem registrada: WF-TEMPLATE-A_v04 (white), estado Wireframe Text APROVADO E CONGELADO; diferenças classificadas como DIFERENÇA INTENCIONAL (D1 a D6)
[x] viewport especificado: references/black/WF-VIEWPORT-360x800.png, 360 × 800 px em 1:1; nenhum ativo ou bitmap white reutilizado
[x] todas as cores usadas constam em REGRAS-TECNICAS.md, seção 6 (tabela 6.6); HEX somente no bloco 5
[x] pares texto/fundo registrados (sem exceção de nível)
[x] canvas 1280 × 1920; todas as áreas documentadas dentro do canvas
[ ] REGRAS-TECNICAS.md seção 3.1 ainda não lista references/black/WF-VIEWPORT-360x800.png (registro pendente do responsável)
[ ] REGRAS-TECNICAS.md 6.7 — registro formal da aprovação das lacunas de cor (pendente do responsável)
[x] origem white WF-TEMPLATE-A_v04: Wireframe Text APROVADO E CONGELADO (7.1); PNG da origem APROVADO E CONGELADO
```

A variação `white` de origem é a `WF-TEMPLATE-A_v04` (pasta `templates/white/`), conforme `WIREFRAME-TEXT.md` 7.1.
