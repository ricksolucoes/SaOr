# WF-TEMPLATE-A_v01 — Reprodução textual fiel da prancha final

> **Natureza deste documento:** reconstrução retroativa. O PNG `WF-TEMPLATE-A_v01.png` já existia; este Wireframe Text foi escrito a partir dele. Coordenadas lidas na imagem (1024 × 1536 px), com tolerância de ±3 px. Divergências em relação à spec vigente estão na seção 3 e **não foram corrigidas**.

```text
CANVAS FINAL — 1024 × 1536 px

┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ SaOr / Sales Order │ WIREFRAME · PRANCHA TÉCNICA - MODELO A (Viewport central dominante) │ WF-TEMPLATE-A │ XX / YY │ v01 │ DD/MM/AAAA        │
│ (cabeçalho de linha única: sem STATUS, BASELINE, VARIAÇÃO e ETAPA)                                                                           │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

1. CANVAS E VIEWPORT                            VIEWPORT CENTRAL DOMINANTE                6. COMPONENTES (MEDIDAS)
┌────────────────────────────────────────────┐  ┌──────────────────────────────────┐      ┌────────────────────────────────────────────────────┐
│ Canvas da prancha   1024 × 1536 px         │  │         360 px (viewport total)  │      │ App Bar (56 px)                                    │
│ Viewport (interface) 360 × 800 px (1:1)    │  │   12 px | 336 px (área útil) | 12 px │  │ Campo Outlined (56 px)                             │
│ Orientação          Retrato (vertical)     │  │ ┌────────────────────────────────┐ │    │ Botão Primário (48 px)                             │
│ Margem horizontal   12 px (estrutura)      │  │ │ 9:41                 [sinal bat]│ │   │ Botão Secundário (48 px)                           │
└────────────────────────────────────────────┘  │ ├────────────────────────────────┤ │    │ Botão Texto (48 px)                                │
                                                │ │ (o) Título da Página   [S] [:] │ │    │ Icon Button (48 px)                                │
2. SAFE AREAS                                   │ │     Subtítulo da página        │ │    │ Item de Lista (56 px / 64 px)                      │
┌────────────────────────────────────────────┐  │ │ Seção de Conteúdo              │ │    │ Card (radius 16 px)                                │
│ Safe area superior  24 px                  │  │ │ Rótulo do campo                │ │    │ Modal (margem lateral 24 px)                       │
│ Safe area inferior  32 px                  │  │ │ [ Texto de exemplo          v ]│ │    │ + cota azul vertical à direita                     │
└────────────────────────────────────────────┘  │ │ [       Botão Primário        ]│ │    └────────────────────────────────────────────────────┘
                                                │ │ [      Botão Secundário       ]│ │
3. GRID E SPACING                               │ │   Botão Texto           [G]    │ │
┌────────────────────────────────────────────┐  │ │ (o) Item de Lista            > │ │
│ Grid base               4 px               │  │ │ [ Título do Card              ]│ │
│ Escala de espaçamento   4/8/12/16/24/32 px │  │ │ [i] Mensagem informativa       │ │
└────────────────────────────────────────────┘  │ │ [ ^ Área de conteúdo scroll v ]│ │
                                                │ │ Início Pedidos Clientes Mais   │ │
4. TIPOGRAFIA (Inter)                           │ │ (faixa safe area inferior)     │ │
┌────────────────────────────────────────────┐  │ └────────────────────────────────┘ │
│ H1 H2 H3 H4 | Subtitle 1-2 | Body 1-2      │  │        800 px (viewport total)   │
│ Caption | Overline | Letter-spacing normal │  └──────────────────────────────────┘
└────────────────────────────────────────────┘

5. CORES (Tokens Base)
┌────────────────────────────────────────────┐
│ [chip] Primary #1976D2 ... Info #0288D1    │
│ (11 tokens, sem nota)                      │
└────────────────────────────────────────────┘


7–10 (linha de 4 cards)                                                                                                                         
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 7. ELEVAÇÃO: E1 Discreta / E2 Média / E3 Alta   8. RADIUS: 12 px / 16 px                                                                     │
│ 9. ÍCONES: 20 px / 24 px (home)   10. ESTADOS: Default Focus Pressed/Selected Disabled Error                                                 │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
11. OBSERVAÇÕES TÉCNICAS (2 colunas: 1–5 e 6–9)                                                                                                 
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 1–5 (esquerda)                                  6–9 (direita)                                                                                │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

# Especificação de implementação da prancha

## 1. Regra de leitura deste documento

A reprodução textual acima é a **referência conceitual de composição** da `WF-TEMPLATE-A_v01`: ordem das regiões, quais blocos existem e quais ficam lado a lado. Não é escala de caracteres para pixels; as medidas valem somente nas seções abaixo.

```text
canvas (como está no PNG):   1024 × 1536 px
orientação:                  retrato
margem externa:              ~11 px (esquerda/direita); ~8 px (topo); ~9 px (base)
modelo:                      A — viewport central dominante
```

## 2. Hierarquia de autoridade e estado

```text
1. docs/Documento_Mestre.md — somente conteúdo e comportamento funcional
2. .specs/wireframes/REGRAS-TECNICAS.md — invariantes técnicos
3. .specs/wireframes/PROCESSO-PRANCHA.md — sequência e gates
4. .specs/wireframes/WIREFRAME-TEXT.md — contrato documental
5. este WF-TEMPLATE-A_v01.md — composição específica desta alternativa
6. PNG correspondente — nesta reconstrução, o PNG é a origem do texto
```

```text
Gates 1 a 6: não registrados — nenhuma aprovação humana encontrada para esta versão
```

## 3. Divergências entre o PNG e a spec vigente

```text
D1  Canvas 1024 × 1536 px; a spec vigente define 1280 × 1920 px (mesma proporção 2:3).
D2  Safe areas: faixas de 24 px (superior, com barra de status 9:41 + ícones de sinal/wifi/bateria)
    e 32 px (inferior) e bloco 2 SAFE AREAS. O modelo B diz que não existe reserva fixa de safe area.
D3  Viewport NÃO está em 1:1. O frame mede ~274 px de largura e ~895 px de altura
    (y 210 a 1105), proporção ≈ 0,31, distorcida em relação a 360 × 800 (0,45).
    Os rótulos "360 × 800 px (1:1)" não correspondem à geometria desenhada.
D4  Paleta: rótulos HEX não batem com os swatches desenhados. Medido: Primary desenhado
    ≈ #0266E4 (rótulo #1976D2); Secondary desenhado ≈ #A8AFB6 (cinza; o rótulo parece
    "#9E9EDE" ou "#9E9E0E", ilegível).
D5  Tipografia: tokens H1–H4, Subtitle 1–2, Body 1–2, Caption, Overline — nomenclatura diferente
    dos tokens WF-TITLE / WF-SECTION / WF-BODY / WF-LABEL / WF-ACTION-TEXT / WF-CAPTION
    da REGRAS-TECNICAS. Inclui Overline 10 px, abaixo do mínimo 12 px dos demais.
D6  Elevação lista só E1, E2, E3 (sem E0) e usa nomes "Discreta / Média / Alta".
D7  Ícones: as duas amostras (20 px e 24 px) usam o mesmo ícone (home).
D8  Estados desenhados como barras coloridas cheias; o texto do estado Focus está ilegível no PNG.
D9  Cabeçalho de linha única: sem STATUS, BASELINE, VARIAÇÃO e ETAPA.
D10 Não existem os blocos REGRAS GERAIS DE COMPONENTES e BORDAS E DIVISORES (presentes em v02 e B/C).
D11 Icon Button à DIREITA do Botão Texto no viewport.
D12 Item de Lista no viewport rotulado "Item de Lista" (no bloco 6: "Título do item").
D13 Observação 5 ("Interfaces com conteúdo maior serão divididas em múltiplas páginas") e 9
    ("Esta prancha é um modelo técnico de referência…") não existem em B/C.
```

Estas divergências são registradas, não resolvidas.

---

# Cabeçalho

```text
área: x 11, y 8, w 1002, h 79 (limite direito 1013, inferior 87)

MARCA          x 11   w 126
IDENTIFICAÇÃO  x 137  w 424
METADADOS      x 561  w 452   (linha única)
```

Marca: "SaOr" (negrito, azul-marinho) acima de "Sales Order" (leve, cinza). Sem ícone.

Identificação:

```text
WIREFRAME
PRANCHA TÉCNICA - MODELO A
(Viewport central dominante)
```

Metadados (rótulo acima, valor abaixo, em negrito):

```text
ID       x 561  w 138   WF-TEMPLATE-A
PÁGINA   x 699  w 86    XX / YY
VERSÃO   x 785  w 96    v01
DATA     x 881  w 132   DD/MM/AAAA
```

---

# Mapa geométrico principal

```text
COLUNA ESQUERDA  x 11   a 290   (w 279)
COLUNA CENTRAL   x 290  a 730   (w 440) — viewport
COLUNA DIREITA   x 730  a 1013  (w 283)
```

Corpo principal: y 102 a 1183. Linha de cartões inferiores: y 1193 a 1375. Observações: y 1383 a 1527.

Blocos (x, y, w, h):

```text
1  CANVAS E VIEWPORT                11  102  279  148
2  SAFE AREAS                       11  260  279  101
3  GRID E SPACING                   11  371  279  109
4  TIPOGRAFIA (Inter)               11  491  279  324
5  CORES (Tokens Base)              11  825  279  358
6  COMPONENTES (MEDIDAS)           730  102  283 1081
7  ELEVAÇÃO (Sombras)               11 1193  323  182
8  RADIUS                          343 1193  237  182
9  ÍCONES (Material Icons Outlined) 590 1193  235  182
10 ESTADOS                         835 1193  178  182
11 OBSERVAÇÕES TÉCNICAS             11 1383 1002  144
```

Estilo dos cards: fundo claro azulado muito leve, borda fina cinza, radius ~4 px; título "N. TÍTULO" em negrito caixa alta; complemento entre parênteses em peso normal.

---

# Viewport central

Sem card próprio.

```text
frame interno: x 375 a 649, y 210 a 1105
contorno externo (arredondado): x 365 a 659, y 202 a 1113
```

Cotas (azul):

```text
360 px                      linha horizontal em y ≈ 131, x 369–655; rótulo "360 px" acima (sem "(viewport total)")
12 px | 336 px (área útil) | 12 px
                            linha em y ≈ 172; extensões verticais até o frame
24 px — Safe area superior  à esquerda, bracket x ≈ 351, y 210–247; rótulo x ≈ 323
32 px — Safe area inferior  à esquerda, bracket y ≈ 1075–1113
800 px                      linha vertical azul em x ≈ 679, y 210–1105; rótulo vertical "800 px" em x ≈ 695
```

Conteúdo do viewport (de cima para baixo):

```text
Faixa superior (azul claro, y 210–247): "9:41" à esquerda; ícones sinal, wifi e bateria à direita
App bar (fundo cinza claro): avatar circular cinza; "Título da Página" / "Subtítulo da página"; ícones search e more_vert
"Seção de Conteúdo"
Campo outlined com rótulo flutuante: "Rótulo do campo" / "Texto de exemplo" / expand_more
Botão Primário (azul)
Botão Secundário (contorno cinza)
Botão Texto "Botão Texto" (azul) + Icon Button settings à direita
Item de lista: avatar cinza / "Item de Lista" / "Texto secundário de apoio" / chevron_right
Card: "Título do Card" / "Texto de exemplo do card com algumas informações."
Mensagem informativa: ícone info azul + "Mensagem informativa de exemplo." (fundo azul claro)
Área tracejada: seta cima / "Área de conteúdo indicando scroll vertical" / seta baixo (cinza)
Bottom navigation: Início (ativo, azul), Pedidos, Clientes, Mais
Faixa inferior safe area (azul claro, sem texto), y ≈ 1069–1105
```

---

# 1. CANVAS E VIEWPORT

```text
Canvas da prancha      1024 × 1536 px
Viewport (interface)   360 × 800 px (1:1)
Orientação             Retrato (vertical)
Margem horizontal      12 px (estrutura)
```

Rótulos e valores em duas colunas separadas por divisor vertical fino.

# 2. SAFE AREAS

```text
Safe area superior   24 px
Safe area inferior   32 px
```

# 3. GRID E SPACING

```text
Grid base               4 px
Escala de espaçamento   4 / 8 / 12 / 16 / 24 / 32 px
```

# 4. TIPOGRAFIA (Inter)

Tabela com divisores horizontais finos; tokens H1–H4 em negrito.

```text
H1              28 px | SemiBold
H2              24 px | SemiBold
H3              20 px | SemiBold
H4              18 px | SemiBold
Subtitle 1      16 px | Medium
Subtitle 2      14 px | Medium
Body 1          16 px | Regular
Body 2          14 px | Regular
Caption         12 px | Regular
Overline        10 px | Medium
Letter-spacing  normal (Inter)
```

# 5. CORES (Tokens Base)

Cada linha: swatch retangular + nome + HEX (rótulo conforme impresso no PNG).

```text
Primary      #1976D2   swatch azul
On Primary   #FFFFFF   swatch branco com contorno azul
Secondary    #9E9EDE   swatch cinza (rótulo ilegível; ver D4)
Background   #FAFAFA
Surface      #FFFFFF
On Surface   #212121   swatch quase preto
Outline      #E0E0E0
Error        #D32F2F
Success      #2E7D32
Warning      #ED6C02
Info         #0288D1
```

---

# 6. COMPONENTES (MEDIDAS)

Cada componente: rótulo em negrito + medida entre parênteses; amostra; cota azul vertical à direita com "NN px".

```text
App Bar (56 px)             [menu] Título [search]                                       cota 56 px
Campo Outlined (56 px)      Rótulo / Texto de exemplo / expand_more                       cota 56 px
Botão Primário (48 px)      fundo azul, texto branco                                      cota 48 px
Botão Secundário (48 px)    fundo cinza claro, contorno                                   cota 48 px
Botão Texto (48 px)         "Botão Texto" azul, sem contorno                              cota 48 px
Icon Button (48 px)         quadrado com ícone settings                                   cota 48 px
Item de Lista (56 px / 64 px)
  item 1                    avatar / Título do item / Texto secundário / chevron_right    cota 56 px
  item 2                    avatar / Título do item /
                            Texto secundário adicional em duas linhas                     cota 64 px
Card (radius 16 px)         Título do Card / Texto de exemplo do card.; legenda "Radius: 16 px"
Modal (margem lateral 24 px)
                            fundo cinza; modal com alça; Título do Modal /
                            Texto de exemplo do modal.; [Cancelar] [Confirmar];
                            legenda "Margem lateral: 24 px"
```

Não há Bottom Navigation neste bloco (aparece somente dentro do viewport).

---

# 7. ELEVAÇÃO (Sombras)

Três amostras quadradas brancas com sombra crescente:

```text
E1 - Discreta   0 1 2 / 12%
E2 - Média      0 2 6 / 16%
E3 - Alta       0 4 12 / 20%
```

# 8. RADIUS

```text
12 px   Campos e Botões
16 px   Cards e Modais
```

# 9. ÍCONES (Material Icons Outlined)

```text
20 px   ícones auxiliares   (amostra: home)
24 px   Ação / Navegação    (amostra: home)
```

# 10. ESTADOS

Cinco barras horizontais de largura total, empilhadas:

```text
Default              barra azul
Focus                barra azul claro com contorno azul (texto ilegível no PNG)
Pressed / Selected   barra azul
Disabled             barra cinza
Error                barra vermelha
```

Sem nota sobre Hover neste bloco.

---

# 11. OBSERVAÇÕES TÉCNICAS

Duas colunas (esquerda 1–5, direita 6–9), WF-CAPTION, numeradas.

```text
1. O viewport representa a tela completa do celular (360 × 800 px) em escala 1:1.
2. A safe area superior é de 24 px e a inferior de 32 px.
3. Todos os elementos seguem o grid de 4 px e a escala de espaçamento definida.
4. Hover está documentado, mas não é obrigatório nas pranchas mobile.
5. Interfaces com conteúdo maior serão divididas em múltiplas páginas.
6. Em páginas seguintes, repetir apenas os elementos realmente persistentes.
7. Nomenclatura dos arquivos: <ID>-<PÁGINA>-<TOTAL>_v<VERSÃO>.png
   Exemplo: T00-01-02_v01.png
8. Uma interface multipágina só é aprovada quando todas as páginas, Claro e Escuro, estiverem aprovadas.
9. Esta prancha é um modelo técnico de referência e não representa uma interface real.
```

---

# Checklist de conferência PNG × texto

```text
[x] blocos 1 a 11 presentes
[x] textos transcritos do PNG
[ ] coordenadas conferidas por medição pixel a pixel (hoje: leitura visual, ±3 px)
[ ] divergências D1–D13 decididas na spec (manter, corrigir ou descartar)
[ ] versão Escuro desta prancha
```
