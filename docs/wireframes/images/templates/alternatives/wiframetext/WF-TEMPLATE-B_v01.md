# WF-TEMPLATE-B_v01 — Reprodução textual fiel da prancha final

```text
CANVAS FINAL — 1280 × 1920 px

┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│SaOr                │WIREFRAME                                       │ID                │PÁGINA       │VERSÃO      │DATA            │STATUS                       │
│Sales Order         │PRANCHA TÉCNICA - MODELO B                      │WF-TEMPLATE-B     │XX / YY   │v01       │DD/MM/AAAA    │PENDENTE DE PRODUÇÃO                │
│                    │(Viewport à esquerda + painel técnico à direita)│BASELINE v1.0     │VARIAÇÃO Claro | Escuro     │ETAPA Wireframe Conceitual em Imagem        │
├──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│┌ VIEWPORT TÉCNICO 360 x 800 px                ┐  ┌ 1. CANVAS E VIEWPORT                           ┐  ┌ 2. SAFE AREAS                                            ┐│
││                  360 px                      │  │  Canvas da prancha      1280 x 1920 px         │  │  Safe area superior      24 px                           ││
││        12 px | 336 px | 12 px                │  │  Viewport (interface)    360 x 800 px          │  │  Safe area inferior      32 px                           ││
││                                              │  │  Escala do viewport      1:1                   │  │                                                          ││
││          24 px safe area superior            │  │  Orientação              Retrato               │  │  Referências do wireframe; não são paddings              ││
││       ┌────────────────────────────────┐     │  │  Margem horizontal       12 px                 │  │  fixos da implementação.                                 ││
││       │  O  Título da Página  [S][M]   │     │  │                                                │  │                                                          ││
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
││       │ └────────────────────────┘     │     │  │  WF-W-BG          #F4F4F4                      │  │                                                          ││
││       │ [i] Mensagem informativa       │     │  │  WF-W-SURFACE     #FFFFFF                      │  │  BOTÃO TEXTO (mínimo 48 px)                              ││
││       │     de exemplo.                │     │  │  WF-W-SURFACE-ALT #EAEAEA                      │  │                      Botão Texto                         ││
││       │ ┌────────────────────────┐     │     │  │  WF-W-BORDER      #B5B5B5                      │  │                                                          ││
││       │ │           ^            │     │     │  │  WF-W-TEXT        #1A1A1A                      │  │  ICON BUTTON (touch target 48 x 48 px)                   ││
││       │ │ Área de conteúdo       │     │     │  │  WF-W-TEXT-2      #565656                      │  │    ┌──────────┐                                          ││
││       │ │ indicando scroll       │     │     │  │  WF-W-ACTION      #333333                      │  │    │   [G]    │                                          ││
││       │ │ vertical               │     │     │  │  WF-W-DISABLED    #9A9A9A                      │  │    └──────────┘                                          ││
││       │ │           v            │     │     │  │  WF-W-FOCUS       #4A4A4A                      │  │                                                          ││
││       │ └────────────────────────┘     │     │  │  WF-W-STATUS      #626262                      │  │  ITEM DE LISTA - simples (56 px)                         ││
││       ├────────────────────────────────┤     │  │                                                │  │    ┌──────────────────────────────────────────────┐      ││
││       │ Início Pedidos Clientes Mais   │     │  │                                                │  │    │ O  Título do item                       >    │      ││
││       ├────────────────────────────────┤     │  │                                                │  │    └──────────────────────────────────────────────┘      ││
││       │ 32 px safe area inferior       │     │  └────────────────────────────────────────────────┘  │                                                          ││
││       └────────────────────────────────┘     │                                                      │  ITEM DE LISTA - secundário (64 px)                      ││
││                                              │  ┌ 7. ELEVAÇÃO                                    ┐  │    ┌──────────────────────────────────────────────┐      ││
││                800 px                        │  │                                                │  │    │ O  Título do item                       >    │      ││
││           (viewport total)                   │  │          ┌────────┐        ┌────────┐          │  │    │    Texto secundário adicional                │      ││
││                                              │  │          │   E0   │        │   E1   │          │  │    └──────────────────────────────────────────────┘      ││
││                                              │  │          └────────┘        └────────┘          │  │                                                          ││
││                                              │  │           0/0/0/0%          0/1/2/12%          │  │  CARD (radius 16 px)                                     ││
││                                              │  │                                                │  │    ┌──────────────────────────────────────────────┐      ││
││                                              │  │          ┌────────┐        ┌────────┐          │  │    │ Título do Card                               │      ││
││                                              │  │          │   E2   │        │   E3   │          │  │    │ Texto de exemplo do card.                    │      ││
││                                              │  │          └────────┘        └────────┘          │  │    └──────────────────────────────────────────────┘      ││
││                                              │  │           0/2/6/16%        0/4/12/20%          │  │                                                          ││
││                                              │  │                                                │  │  MODAL / DIALOG (margem lateral 24 px)                   ││
││                                              │  │                                                │  │    ┌──────────────────────────────────────────────┐      ││
││                                              │  │                                                │  │    │                  -----                       │      ││
││                                              │  └────────────────────────────────────────────────┘  │    │ Título do Modal                              │      ││
││                                              │                                                      │    │ Texto de exemplo do modal.                   │      ││
││                                              │  ┌ 8. RADIUS                                      ┐  │    │ [ Cancelar ]              [ Confirmar ]      │      ││
││                                              │  │                                                │  │    └──────────────────────────────────────────────┘      ││
││                                              │  │         ┌──────────┐      ┌──────────┐         │  │                                                          ││
││                                              │  │         │  12 px   │      │  16 px   │         │  │  BOTTOM NAVIGATION (64 px)                               ││
││                                              │  │         └──────────┘      └──────────┘         │  │    ┌──────────────────────────────────────────────┐      ││
││                                              │  │       Campos e botões    Cards e modais        │  │    │ Início | Pedidos | Clientes | Mais           │      ││
││                                              │  │                                                │  │    └──────────────────────────────────────────────┘      ││
││                                              │  │                                                │  │  Somente quando previsto na baseline.                    ││
│└──────────────────────────────────────────────┘  └────────────────────────────────────────────────┘  └──────────────────────────────────────────────────────────┘│
├──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│┌ 9. ÍCONES (Material Icons Outlined)                                          ┐  ┌ 10. ESTADOS (Componentes)                                                    ┐│
││                                                                              │  │  ┌──────────────────────────────────────────────┐                            ││
││  ┌──────────────┐           ┌──────────────┐                                 │  │  │ Default                                      │                            ││
││  │    20 px     │           │    24 px     │                                 │  │  ├──────────────────────────────────────────────┤                            ││
││  │  [AUXILIAR]  │           │ [AÇÃO / NAV] │                                 │  │  │ Focus                                        │                            ││
││  └──────────────┘           └──────────────┘                                 │  │  ├──────────────────────────────────────────────┤                            ││
││  Ícones auxiliares          Ação / navegação                                 │  │  │ Pressed / Selected                           │                            ││
││                                                                              │  │  ├──────────────────────────────────────────────┤                            ││
││  Material Icons Outlined: referência conceitual.                             │  │  │ Disabled                                     │                            ││
││                                                                              │  │  ├──────────────────────────────────────────────┤                            ││
││                                                                              │  │  │ Error                                        │                            ││
││                                                                              │  │  └──────────────────────────────────────────────┘                            ││
││                                                                              │  │  Hover: documentado; não obrigatório em mobile.                              ││
││                                                                              │  │                                                                              ││
│└──────────────────────────────────────────────────────────────────────────────┘  └──────────────────────────────────────────────────────────────────────────────┘│
├──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│┌ 11. REGRAS GERAIS DE COMPONENTES                                                                 ┐  ┌ BORDAS E DIVISORES                                       ┐│
││  Touch target mínimo: 48 x 48 px.                                                                │  │  ┌────────────────┐    ─────────────────────             ││
││  Aplicável a botões, ícones, itens de lista, navegação                                           │  │  │ Borda 1 px     │    Divisor 1 px                      ││
││  e demais áreas interativas.                                                                     │  │  └────────────────┘                                      ││
││  A área clicável deve respeitar o mínimo mesmo quando                                            │  │  Token claro: WF-W-BORDER #B5B5B5                        ││
││  o elemento visual for menor.                                                                    │  │  Uso entre seções e listas quando necessário.            ││
││                                                                                                  │  │                                                          ││
││                                                                                                  │  │                                                          ││
│└──────────────────────────────────────────────────────────────────────────────────────────────────┘  └──────────────────────────────────────────────────────────┘│
├──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│┌ 12. OBSERVAÇÕES TÉCNICAS                                                                                                                                       ┐│
││  1. O viewport representa a tela completa do celular: 360 x 800 px em escala 1:1.                                                                              ││
││  2. Safe areas de 24 px superior e 32 px inferior são referências do wireframe.                                                                                ││
││  3. Na implementação, superfícies podem ocupar 100% da tela; conteúdos sensíveis respeitam os insets reais da plataforma/dispositivo.                          ││
││  4. Todos os elementos seguem grid de 4 px e escala de espaçamento 4 / 8 / 12 / 16 / 24 / 32 px.                                                               ││
││  5. Inter é tipografia técnica do wireframe e não tipografia oficial da marca SaOr.                                                                            ││
││  6. Em páginas seguintes, repetir apenas elementos realmente persistentes.                                                                                     ││
││  7. Nomenclatura dos arquivos funcionais: <ID>-<PÁGINA>-<TOTAL>_v<VERSÃO>.png.                                                                                 ││
││  8. Interface multipágina só é aprovada quando todas as páginas Claro e Escuro estiverem aprovadas.                                                            ││
││  9. Cores, ícones e componentes são tokens e referências técnicas dos wireframes.                                                                              ││
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

---

## 2. Hierarquia de autoridade

Para esta prancha, a ordem de autoridade é:

```text
1. docs/wireframes/images/README.md
2. docs/wireframes/images/templates/README.md
3. reprodução textual no início deste WF-TEMPLATE-B_v01.md
4. especificação geométrica detalhada abaixo
5. PNG que será produzido a partir deste Wireframe Text
```

Nenhuma prancha histórica ou alternativa anterior é referência de geometria, proporção, posicionamento ou distribuição desta alternativa B.

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

A proporção vem do frame inicial desta própria B_v01.

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
PENDENTE DE PRODUÇÃO
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
Claro | Escuro

ETAPA
Wireframe Conceitual em Imagem
```

---

# Viewport

## Papel na composição

O viewport é o primeiro elemento estrutural montado após o cabeçalho.

Ele deve ser inserido fisicamente antes do cálculo final das áreas documentais.

Arquivo obrigatório:

```text
docs/wireframes/images/templates/references/WF-VIEWPORT-360x800-clean.png
```

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
h: 1024 px

limite direito: 428 px
limite inferior: 1156 px
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
docs/wireframes/images/templates/references/
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

```text
TÍTULO DO BLOCO
y: 144–164 px

COTA 360 px
y: 172–188 px

COTA 12 / 336 / 12
y: 196–212 px

BITMAP
y: 224–1024 px

IDENTIFICAÇÃO 800 px
y: 1032–1048 px

TEXTO "(viewport total)"
y: 1052–1068 px
```

O espaço restante até `y = 1156` é respiro documental desta prancha-modelo.

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
h: 1024
base: 1156
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
h: 216

7. ELEVAÇÃO
x: 444
y: 820
w: 360
h: 180

8. RADIUS
x: 444
y: 1016
w: 360
h: 140
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
h: 864
```

Base comum:

```text
bloco 4 termina em y = 1156
bloco 8 termina em y = 1156
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
docs/wireframes/images/README.md
4.1 — Viewport
4.3 — Canvas técnico
5 — Grid e espaçamento
```

---

# 2. COTAS DO VIEWPORT

> O frame inicial ainda preserva o rótulo histórico `2. SAFE AREAS`.
> Para a execução técnica vigente desta B_v01, essa mesma região passa a documentar as cotas atuais do viewport.

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
docs/wireframes/images/README.md
3 — Referências técnicas compartilhadas
4.1 — Viewport
4.2 — Sem reserva fixa de safe area

docs/wireframes/images/templates/references/
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
docs/wireframes/images/README.md
5 — Grid e espaçamento
```

---

# 4. COMPONENTES (MEDIDAS)

## Área

```text
x: 820 px
y: 292 px
w: 448 px
h: 864 px
```

Área interna:

```text
x: 836 px
w: 416 px
```

O conteúdo é demonstrativo.
As medidas dos componentes vêm do README técnico; a área deste cartão é específica desta prancha-modelo.

## Distribuição vertical

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
y: 412
h: 16

amostra:
x: 836
y: 428
w: 416
h: 56
```

Conteúdo:

```text
Rótulo
Texto de exemplo                              v
```

### 4.3 Botão Primário

```text
rótulo:
y: 488
h: 16

amostra:
x: 836
y: 504
w: 416
h: 48
```

Texto:

```text
Botão Primário
```

### 4.4 Botão Secundário

```text
rótulo:
y: 556
h: 16

amostra:
x: 836
y: 572
w: 416
h: 48
```

Texto:

```text
Botão Secundário
```

### 4.5 Botão Texto + Icon Button

```text
rótulo:
y: 624
h: 16

faixa de demonstração:
x: 836
y: 640
w: 416
h: 48
```

Distribuição:

```text
Botão Texto:
x: 836
w: 352
h: 48

Icon Button:
x: 1204
w: 48
h: 48

gap: 16 px
```

### 4.6 Item de Lista — simples

```text
rótulo:
y: 692

amostra:
x: 836
y: 708
w: 416
h: 56
```

### 4.7 Item de Lista — secundário

```text
rótulo:
y: 768

amostra:
x: 836
y: 784
w: 416
h: 64
```

### 4.8 Card

```text
rótulo:
y: 852

amostra:
x: 836
y: 868
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
y: 936

área demonstrativa:
x: 836
y: 952
w: 416
h: 96
```

O modal dentro da área respeita a margem lateral normativa de `24 px`.

### 4.10 Bottom Navigation

```text
rótulo:
y: 1052

amostra:
x: 836
y: 1068
w: 416
h: 64

observação:
y: 1136
h: 16
```

Texto da observação:

```text
Somente quando previsto na baseline.
```

Referências:

```text
docs/wireframes/images/README.md
7 — Componentes técnicos de representação
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
docs/wireframes/images/README.md
6.3 — Tipografia técnica
```

---

# 6. PALETA TÉCNICA — CLARO

## Área

```text
x: 444 px
y: 588 px
w: 360 px
h: 216 px
```

## Conteúdo exato

```text
WF-W-BG          #F4F4F4
WF-W-SURFACE     #FFFFFF
WF-W-SURFACE-ALT #EAEAEA
WF-W-BORDER      #B5B5B5
WF-W-TEXT        #1A1A1A
WF-W-TEXT-2      #565656
WF-W-ACTION      #333333
WF-W-DISABLED    #9A9A9A
WF-W-FOCUS       #4A4A4A
WF-W-STATUS      #626262
```

## Disposição

Cada linha contém:

```text
[swatch 16 × 16]  TOKEN  HEX
```

Posições:

```text
título:
x: 460
y: 600

primeira linha:
y: 632

line-height:
16 px
```

Referência:

```text
docs/wireframes/images/README.md
6.1 — Claro
```

---

# 7. ELEVAÇÃO

## Área

```text
x: 444 px
y: 820 px
w: 360 px
h: 180 px
```

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

Colunas:

```text
x1: 484 px
x2: 636 px
```

Linhas:

```text
linha 1:
y amostra: 864
y legenda: 912

linha 2:
y amostra: 936
y legenda: 984
```

Referência:

```text
docs/wireframes/images/README.md
8 — Bordas, radius, elevação e iconografia
```

---

# 8. RADIUS

## Área

```text
x: 444 px
y: 1016 px
w: 360 px
h: 140 px
```

## Conteúdo

```text
12 px
Campos e botões

16 px
Cards e modais
```

Amostras:

```text
12 px:
x: 484
y: 1060
w: 128
h: 44

16 px:
x: 636
y: 1060
w: 128
h: 44
```

Legendas:

```text
y: 1112
```

Referência:

```text
docs/wireframes/images/README.md
8 — Bordas, radius, elevação e iconografia
```

---

# Região inferior

A região inferior começa depois do corpo principal:

```text
x: 12 px
y: 1180 px
w: 1256 px
h: 728 px
```

Afastamento:

```text
1156 → fim do corpo principal
1180 → início da região inferior

gap = 24 px
```

---

# 9. ÍCONES (Material Icons Outlined)

## Área

```text
x: 12 px
y: 1180 px
w: 620 px
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

Referência:

```text
docs/wireframes/images/README.md
8 — Iconografia
```

---

# 10. ESTADOS (Componentes)

## Área

```text
x: 648 px
y: 1180 px
w: 620 px
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

`Hover` permanece documentado, mas não precisa ser demonstrado como estado visual obrigatório nesta prancha mobile.

Amostras:

```text
x: 688 px
w: 540 px
h: 24 px
```

Posições:

```text
Default             y: 1220
Focus               y: 1252
Pressed / Selected  y: 1284
Disabled            y: 1316
Error               y: 1348
```

Referências:

```text
docs/wireframes/images/README.md
9 — Estados técnicos
10 — Acessibilidade estrutural
```

---

# 11. REGRAS GERAIS DE COMPONENTES

## Área

```text
x: 12 px
y: 1404 px
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
y: 1440 px
w: 48 px
h: 48 px
```

Texto:

```text
x: 96 px
y: 1432 px
w: 680 px
```

Referências:

```text
docs/wireframes/images/README.md
7 — Componentes técnicos de representação
10 — Acessibilidade estrutural
```

---

# BORDAS E DIVISORES

## Área

```text
x: 808 px
y: 1404 px
w: 460 px
h: 144 px
```

## Borda

```text
amostra:
x: 824
y: 1440
w: 160
h: 64

borda:
1 px

token Claro:
WF-W-BORDER
#B5B5B5
```

## Divisor

```text
x: 1016
y: 1472
w: 220
h: 1
```

Referência:

```text
docs/wireframes/images/README.md
8 — Bordas, radius, elevação e iconografia
```

---

# 12. OBSERVAÇÕES TÉCNICAS

## Área

```text
x: 12 px
y: 1564 px
w: 1256 px
h: 344 px

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
```

## Conteúdo exato

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
docs/wireframes/images/README.md
3 — Referências técnicas compartilhadas
4 — Viewport e geometria
5 — Grid e espaçamento
6 — Tokens técnicos
7 — Componentes
8 — Bordas, radius, elevação e iconografia
9 — Estados
10 — Acessibilidade
```

---

# Sequência de construção desta prancha-modelo

```text
01. Canvas 1280 × 1920
02. Cabeçalho
03. Bitmap WF-VIEWPORT-360x800-clean.png em 100% / 1:1
04. Cotas 360 / 336 / 12 / 12 / 800
05. Validar fisicamente o viewport
06. Calcular as áreas documentais restantes desta B_v01
07. Bloco 1
08. Bloco 2
09. Bloco 3
10. Bloco 4
11. Bloco 5
12. Bloco 6
13. Bloco 7
14. Bloco 8
15. Bloco 9
16. Bloco 10
17. Bloco 11
18. Bordas e Divisores
19. Bloco 12
20. Conferência integral
21. Somente após PASS: produzir o PNG correspondente
```

---

# Gate antes da produção do PNG

```text
[ ] frame inicial preservado como referência conceitual de composição
[ ] canvas = 1280 × 1920 px
[ ] cabeçalho montado conforme esta B_v01
[ ] viewport físico = 360 × 800 px
[ ] viewport inserido em 100% / 1:1
[ ] nenhuma reserva fixa de safe area adicionada
[ ] cotas 360 / 336 / 12 / 12 / 800 representadas
[ ] nenhuma cota alterou o bitmap
[ ] todas as áreas desta prancha-modelo permanecem dentro do canvas
[ ] blocos 1 a 12 dimensionados para o conteúdo real deste template
[ ] bloco 12 permanece como uma única área documental
[ ] nenhuma medida desta B_v01 foi tratada como dimensão universal de futuros T/M/E
[ ] nenhuma referência de layout foi herdada de prancha histórica ou alternativa anterior
[ ] marca usa as fontes oficiais catalogadas
[ ] componentes usam as medidas normativas do README técnico
[ ] não existe requisito funcional inventado
```

Somente depois desse gate o PNG da `WF-TEMPLATE-B_v01` deve ser produzido e comparado com esta especificação.
