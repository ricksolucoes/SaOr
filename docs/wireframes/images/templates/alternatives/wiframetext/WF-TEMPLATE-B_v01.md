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

A reprodução textual acima é a referência visual da composição final da `WF-TEMPLATE-B_v01`.

A implementação da prancha deve seguir os tópicos abaixo na mesma ordem em que os elementos são congelados na imagem.

---

## Cabeçalho

### Área ocupada

```text
Canvas de referência: 1280 × 1920 px

x:       12 px
y:       12 px
largura: 1256 px
altura:    96 px

limite direito:  1268 px
limite inferior:  108 px
```

O cabeçalho ocupa toda a largura útil superior da prancha, preservando `12 px` de margem estrutural em cada lado.

A composição visual parte do cabeçalho validado da `WF-TEMPLATE-A_v02.png`, mas a geometria é reconstruída para o canvas vigente `1280 × 1920 px` e ajustada ao grid de `4 px`.

Não utilizar resize do raster da Alternativa A como forma de construção.

### Estrutura horizontal

```text
┌────────────────┬────────────────────────────────┬────────────────────────────────────────────────────────────┐
│ MARCA          │ IDENTIFICAÇÃO DA PRANCHA       │ METADADOS                                                  │
│ 156 px         │ 384 px                         │ 716 px                                                     │
└────────────────┴────────────────────────────────┴────────────────────────────────────────────────────────────┘
```

Coordenadas:

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

### Marca — conteúdo e posição

Área:

```text
x: 12
y: 12
w: 156
h: 96
```

Conteúdo:

```text
SaOr
Sales Order
```

Disposição:

```text
alinhamento horizontal: esquerda
alinhamento vertical do conjunto: centro
padding esquerdo: 16 px
```

Hierarquia:

```text
SaOr
→ identificação principal da marca

Sales Order
→ assinatura secundária da marca
```

Referências obrigatórias:

```text
assets/fonts/logo/README.md
assets/logo/README.md
docs/wireframes/images/templates/alternatives/WF-TEMPLATE-B_v[XX].png
```

> XX -> E a versão da imagem que foi tentada ser gerada apartir deste template.

A tipografia da marca não deve ser substituída pela tipografia técnica Inter.

### Identificação da prancha — conteúdo e posição

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
alinhamento: esquerda
padding horizontal: 24 px
ordem vertical:
1. WIREFRAME
2. PRANCHA TÉCNICA - MODELO B
3. (Viewport à esquerda + painel técnico à direita)
```

A hierarquia visual deve seguir o padrão do cabeçalho da `WF-TEMPLATE-A_v02.png`.

### Metadados — estrutura interna

Área total:

```text
x: 552
y: 12
w: 716
h: 96
```

A área é dividida em duas linhas.

#### Linha superior

```text
x: 552
y: 12
w: 716
h: 64
```

Distribuição:

```text
ID
x: 552
y: 12
w: 164
h: 64

PÁGINA
x: 716
y: 12
w: 128
h: 64

VERSÃO
x: 844
y: 12
w: 124
h: 64

DATA
x: 968
y: 12
w: 140
h: 64

STATUS
x: 1108
y: 12
w: 160
h: 64
```

Conteúdo exato:

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

#### Linha inferior

```text
x: 552
y: 76
w: 716
h: 32
```

Distribuição:

```text
BASELINE
x: 552
y: 76
w: 164
h: 32

VARIAÇÃO
x: 716
y: 76
w: 220
h: 32

ETAPA
x: 936
y: 76
w: 332
h: 32
```

Conteúdo exato:

```text
BASELINE
v1.0

VARIAÇÃO
Claro | Escuro

ETAPA
Wireframe Conceitual em Imagem
```

### Referência obrigatória do cabeçalho

```text
docs/wireframes/images/templates/alternatives/WF-TEMPLATE-A_v02.png
```

A referência define:

```text
- linguagem visual;
- hierarquia entre marca, título e metadados;
- organização em linha superior e inferior;
- uso de divisores;
- densidade visual;
- alinhamento dos conteúdos.
```

A geometria registrada neste Wireframe Text é a geometria da Alternativa B no canvas atual e prevalece sobre as dimensões físicas da antiga prancha A.

---

## Viewport

### Área reservada do conjunto técnico

O conjunto do viewport ocupa a coluna esquerda imediatamente abaixo do cabeçalho.

Área reservada:

```text
x:        12 px
y:       132 px
largura: 428 px
altura: 1012 px

limite direito:  440 px
limite inferior: 1144 px
```

Existe um afastamento vertical de `24 px` entre o fim do cabeçalho e o início da área do viewport:

```text
fim do cabeçalho: y = 108 px
início do viewport técnico: y = 132 px

108 + 24 = 132
```

Esta área contém:

```text
- identificação VIEWPORT TÉCNICO 360 × 800 px;
- cotas superiores;
- referência da safe area superior;
- bitmap mestre 360 × 800 px;
- referência da safe area inferior;
- identificação da altura total 800 px.
```

### Arquivo obrigatório do viewport

```text
docs/wireframes/images/templates/references/WF-VIEWPORT-360x800-clean.png
```

Dimensão física do arquivo:

```text
360 × 800 px
```

Uso obrigatório:

```text
escala de inserção: 100%
escala física na prancha: 1:1
largura final: 360 px
altura final: 800 px
```

O bitmap é inserido diretamente.

Seu conteúdo interno não deve ser reconstruído pelo Wireframe Text.

### Posição física do bitmap

```text
x:  46 px
y: 252 px
w: 360 px
h: 800 px

limite direito: 406 px
limite inferior: 1052 px
```

O bitmap fica centralizado horizontalmente dentro da área reservada:

```text
área reservada:
x = 12
w = 428

bitmap:
x = 46
w = 360

espaço lateral:
34 px à esquerda
34 px à direita
```

### Proibição de redimensionamento

É proibido, em qualquer hipótese:

```text
- reduzir;
- ampliar;
- esticar;
- comprimir;
- reproporcionar;
- aplicar fit;
- recortar;
- reconstruir;
- redesenhar;
- substituir por aproximação;
- alterar a dimensão para abrir espaço para documentação.
```

Adicionar cotas, legendas, safe areas ou qualquer outra anotação técnica não autoriza alteração do bitmap.

Depois de toda a documentação ser adicionada, o arquivo deve continuar medindo fisicamente:

```text
360 × 800 px
```

### Referência obrigatória das cotas

```text
docs/wireframes/images/templates/references/Especificação Técnica do Viewport Mobile.png
```

Essa imagem define a linguagem das marcações dimensionais.

Devem ser reproduzidas as seguintes referências:

```text
largura total:                360 px
margem esquerda:               12 px
largura útil:                 336 px
margem direita:                12 px
safe area superior:            24 px
safe area inferior:            32 px
altura total:                 800 px
```

Relação obrigatória:

```text
12 + 336 + 12 = 360
```

### Âncoras horizontais das cotas

As cotas horizontais devem usar como referência os limites reais do bitmap.

```text
x0 = 46 px
→ início físico do viewport

x1 = 58 px
→ início da largura útil
→ 46 + 12

x2 = 394 px
→ fim da largura útil
→ 58 + 336

x3 = 406 px
→ fim físico do viewport
→ 394 + 12
```

Portanto:

```text
46 ─────────────── 406
        360 px

46 ─ 58 ───────────────────── 394 ─ 406
     12          336           12
```

### Distribuição vertical das referências

```text
TÍTULO DO BLOCO
y: 144–164 px

COTA 360 px
y: 172–196 px

COTA 12 / 336 / 12
y: 196–220 px

REFERÊNCIA SAFE AREA SUPERIOR
y: 224–244 px

BITMAP
y: 252–1052 px

REFERÊNCIA SAFE AREA INFERIOR
y: 1060–1080 px

IDENTIFICAÇÃO 800 px
y: 1088–1108 px

TEXTO "(viewport total)"
y: 1112–1132 px
```

A disposição interna das setas, linhas e textos das cotas deve copiar a linguagem visual de:

```text
Especificação Técnica do Viewport Mobile.png
```

Não criar um novo padrão gráfico para as cotas.

### Safe area superior

Referência:

```text
24 px
```

Limites físicos dentro do viewport:

```text
x: 46 px
y: 252 px
w: 360 px
h: 24 px
```

Se houver faixa visual de anotação sobre o viewport, ela deve existir como camada documental separada.

O arquivo `WF-VIEWPORT-360x800-clean.png` permanece intacto.

### Safe area inferior

Referência:

```text
32 px
```

Limites físicos dentro do viewport:

```text
x: 46 px
y: 1020 px
w: 360 px
h: 32 px
```

Cálculo:

```text
252 + 800 = 1052
1052 - 32 = 1020
```

A anotação deve ser uma camada documental separada e não uma alteração do bitmap mestre.

### Referência normativa do viewport

```text
docs/wireframes/images/README.md
```

Aplicar especialmente:

```text
3.1 — Viewport mobile oficial
3.2 — Safe areas técnicas
3.3 — Prancha técnica
3.4 — Ordem obrigatória de construção da prancha
```

Essas regras são superiores a qualquer decisão visual da Alternativa B.

### Geometria 

Depois da montagem e validação do Cabeçalho e do Viewport:

```text
CABEÇALHO
x: 12
y: 12
w: 1256
h: 96

VIEWPORT TÉCNICO
x: 12
y: 132
w: 428
h: 1012

BITMAP DO VIEWPORT
x: 46
y: 252
w: 360
h: 800
```

> Essas áreas não podem ser alteradas para acomodar os demais blocos.

### Espaço restante para os próximos blocos

Após congelar Cabeçalho + Viewport, a região principal disponível à direita é:

```text
x: 456 px
y: 132 px
w: 812 px
h: 1012 px

limite direito: 1268 px
limite inferior: 1144 px
```

Separação horizontal entre o viewport técnico e a região documental direita:

```text
440 → fim da região do viewport
456 → início da documentação

gap = 16 px
```

A região inferior restante começa somente depois do corpo principal:

```text
x: 12 px
y: 1168 px
w: 1256 px
h: 740 px

gap vertical:
1144 → fim do corpo principal
1168 → início da região inferior
24 px
```

O detalhamento dos blocos `1` a `12` deverá utilizar somente essas áreas restantes.

É proibido reduzir ou deslocar o viewport para fazer qualquer bloco posterior caber.

## Mapa geométrico consolidado das áreas restantes

### Corpo principal à direita do viewport

```text
REGIÃO DISPONÍVEL
x: 456 px
y: 132 px
w: 812 px
h: 1012 px
```

A região é dividida em duas colunas com `16 px` de separação:

```text
COLUNA CENTRAL
x: 456 px
w: 360 px

GAP
x: 816 px
w: 16 px

COLUNA DIREITA
x: 832 px
w: 436 px
```

Composição vertical:

```text
y = 132
┌──────────────────────── 144 px ────────────────────────┐
│ 1. CANVAS E VIEWPORT       │ 2. SAFE AREAS             │
└────────────────────────────────────────────────────────┘

gap vertical = 16 px

y = 292
┌────────────────────────────┬────────────────────────────┐
│ 3. GRID E SPACING          │                            │
├────────────────────────────┤                            │
│ 5. TIPOGRAFIA              │                            │
├────────────────────────────┤ 4. COMPONENTES             │
│ 6. PALETA                  │                            │
├────────────────────────────┤                            │
│ 7. ELEVAÇÃO                │                            │
├────────────────────────────┤                            │
│ 8. RADIUS                  │                            │
└────────────────────────────┴────────────────────────────┘
base comum = y 1144
```

### Região inferior

```text
x: 12 px
y: 1168 px
w: 1256 px
h: 740 px
```

Distribuição:

```text
9. ÍCONES                    10. ESTADOS
y: 1168
h: 220
gap horizontal: 16 px

gap vertical: 16 px

11. REGRAS GERAIS            BORDAS E DIVISORES
y: 1404
h: 148
gap horizontal: 16 px

gap vertical: 16 px

12. OBSERVAÇÕES TÉCNICAS
y: 1568
h: 340

margem inferior do canvas:
1908 → 1920 = 12 px
```

## Regra comum dos cartões técnicos

Os cartões documentais da Alternativa B seguem a mesma linguagem visual observada na `WF-TEMPLATE-A_v02.png`, reconstruída no canvas vigente.

Aplicação comum:

```text
borda: 1 px
token da borda no Claro: WF-W-BORDER
superfície: WF-W-SURFACE
texto principal: WF-W-TEXT
texto secundário: WF-W-TEXT-2

padding interno horizontal: 16 px
padding interno vertical: 12 px

título do cartão:
WF-SECTION
alinhado à esquerda

conteúdo documental:
WF-CAPTION ou WF-LABEL conforme hierarquia
```

Referências:

```text
docs/wireframes/images/README.md
Seção 5 — Grid e espaçamento
Seção 6 — Tokens técnicos do wireframe

docs/wireframes/images/templates/alternatives/WF-TEMPLATE-A_v02.png
→ linguagem visual dos cartões
→ hierarquia de títulos
→ divisores
→ densidade documental
```

A geometria abaixo é específica da Alternativa B e prevalece para este Wireframe Text.

---

## 1. CANVAS E VIEWPORT

### Área

```text
x: 456 px
y: 132 px
w: 360 px
h: 144 px

limite direito: 816 px
limite inferior: 276 px
```

### Conteúdo exato

```text
1. CANVAS E VIEWPORT

Canvas da prancha      1280 × 1920 px
Viewport (interface)    360 × 800 px
Escala do viewport      1:1
Orientação              Retrato
Margem horizontal       12 px
```

### Disposição interna

```text
padding:
16 px horizontal
12 px vertical

título:
x = 472
y = 144
w = 328
h = 20

linhas de conteúdo:
início y = 176
line-height = 20 px

coluna dos rótulos:
x = 472
w = 180

coluna dos valores:
x = 652
w = 148
```

Ordem vertical:

```text
y 176  Canvas da prancha
y 196  Viewport (interface)
y 216  Escala do viewport
y 236  Orientação
y 256  Margem horizontal
```

### Referência normativa

```text
docs/wireframes/images/README.md

4.3 — Canvas técnico
4.4 — Ordem obrigatória de montagem
5 — Grid e espaçamento
```

Este cartão é documental.

Ele não redefine o viewport físico já congelado.

---

## 2. SAFE AREAS

### Área

```text
x: 832 px
y: 132 px
w: 436 px
h: 144 px

limite direito: 1268 px
limite inferior: 276 px
```

### Conteúdo exato

```text
2. SAFE AREAS

Safe area superior      24 px
Safe area inferior      32 px

Referências do wireframe; não são paddings
fixos da implementação.
```

### Disposição interna

```text
padding:
16 px horizontal
12 px vertical

título:
x = 848
y = 144
w = 404
h = 20

linha superior:
y = 176

linha inferior:
y = 196

observação:
x = 848
y = 228
w = 404
duas linhas
line-height = 20 px
```

### Referência normativa

```text
docs/wireframes/images/README.md
4.2 — Safe areas de referência
```

Este cartão explica a reserva técnica.

Ele não autoriza desenhar chrome específico de iOS ou Android.

---

## 3. GRID E SPACING

### Área

```text
x: 456 px
y: 292 px
w: 360 px
h: 120 px

limite direito: 816 px
limite inferior: 412 px
```

### Conteúdo exato

```text
3. GRID E SPACING

Grid base               4 px
Escala                  4 / 8 / 12 / 16 / 24 / 32 px
Padding-base horizontal 16 px
Padding-base vertical   12 px
```

### Disposição interna

```text
padding:
16 px horizontal
12 px vertical

título:
x = 472
y = 304
h = 20

conteúdo:
x = 472
y = 336
w = 328
```

As quatro informações são apresentadas em linhas independentes.

A linha da escala pode usar a largura completa interna do cartão.

### Referência normativa

```text
docs/wireframes/images/README.md
5 — Grid e espaçamento
```

Não representar espaçamento fora da escala neste cartão.

---

## 4. COMPONENTES (MEDIDAS)

### Área

```text
x: 832 px
y: 292 px
w: 436 px
h: 852 px

limite direito: 1268 px
limite inferior: 1144 px
```

O cartão ocupa toda a coluna direita abaixo de `2. SAFE AREAS`.

Sua base deve coincidir exatamente com a base de `8. RADIUS`.

### Área interna útil

```text
padding horizontal: 16 px

x interno: 848 px
largura interna: 404 px

início do conteúdo:
y: 316 px

fim máximo do conteúdo:
y: 1128 px

reserva inferior:
16 px
```

### Referência normativa

```text
docs/wireframes/images/README.md
7 — Componentes técnicos de representação

docs/wireframes/images/templates/alternatives/WF-TEMPLATE-A_v02.png
→ forma de demonstrar fisicamente as medidas
```

### 4.1 App Bar

Rótulo:

```text
APP BAR (56 px)
x: 848
y: 316
h: 16
```

Amostra:

```text
x: 848
y: 332
w: 404
h: 56
```

Conteúdo:

```text
[MENU]  Título                         [SEARCH]
```

Regras:

```text
altura física da amostra: 56 px
ícones de ação/navegação: 24 px
touch target dos ícones: mínimo 48 × 48 px
```

### 4.2 Campo Outlined

Rótulo:

```text
CAMPO OUTLINED (56 px) · Rótulo
x: 848
y: 392
h: 16
```

Amostra:

```text
x: 848
y: 408
w: 404
h: 56
```

Conteúdo:

```text
Texto de exemplo                              v
```

Regras:

```text
altura: 56 px
radius: 12 px
borda: 1 px
padding-base: 16 px horizontal / 12 px vertical
```

### 4.3 Botão Primário

Rótulo:

```text
BOTÃO PRIMÁRIO (48 px)
x: 848
y: 468
h: 16
```

Amostra:

```text
x: 848
y: 484
w: 404
h: 48
```

Texto central:

```text
Botão Primário
```

Regras:

```text
altura: 48 px
radius: 12 px
texto: WF-ACTION-TEXT
```

### 4.4 Botão Secundário

Rótulo:

```text
BOTÃO SECUNDÁRIO (48 px)
x: 848
y: 536
h: 16
```

Amostra:

```text
x: 848
y: 552
w: 404
h: 48
```

Texto central:

```text
Botão Secundário
```

### 4.5 Botão Texto + Icon Button

Os dois exemplos compartilham a mesma faixa horizontal, como na referência A_v02.

Rótulo:

```text
BOTÃO TEXTO / ICON BUTTON
x: 848
y: 604
h: 16
```

Botão Texto:

```text
x: 848
y: 620
w: 340
h: 48

texto:
Botão Texto
```

Icon Button:

```text
x: 1204
y: 620
w: 48
h: 48
```

Regras:

```text
gap entre exemplos: 16 px
touch target do Icon Button: 48 × 48 px
ícone: 24 px
```

### 4.6 Item de Lista — simples

Rótulo:

```text
ITEM DE LISTA — simples (56 px)
x: 848
y: 672
h: 16
```

Amostra:

```text
x: 848
y: 688
w: 404
h: 56
```

Conteúdo:

```text
O  Título do item                              >
```

### 4.7 Item de Lista — com secundário

Rótulo:

```text
ITEM DE LISTA — secundário (64 px)
x: 848
y: 748
h: 16
```

Amostra:

```text
x: 848
y: 764
w: 404
h: 64
```

Conteúdo:

```text
O  Título do item                              >
   Texto secundário adicional
```

### 4.8 Card

Rótulo:

```text
CARD (radius 16 px)
x: 848
y: 832
h: 16
```

Amostra:

```text
x: 848
y: 848
w: 404
h: 64
```

Conteúdo:

```text
Título do Card
Texto de exemplo do card.
```

Regras:

```text
radius: 16 px
borda: 1 px quando necessária
```

### 4.9 Modal / Dialog

Rótulo:

```text
MODAL / DIALOG (margem lateral 24 px)
x: 848
y: 916
h: 16
```

A área documental total da amostra ocupa:

```text
x: 848
y: 932
w: 404
h: 88
```

O modal propriamente dito respeita `24 px` de margem lateral dentro da amostra:

```text
x: 872
y: 932
w: 356
h: 88
```

Conteúdo:

```text
Título do Modal
Texto de exemplo do modal.

[ Cancelar ]              [ Confirmar ]
```

Regras:

```text
radius: 16 px
margem lateral demonstrada: 24 px
```

### 4.10 Bottom Navigation

Rótulo:

```text
BOTTOM NAVIGATION (64 px)
x: 848
y: 1024
h: 16
```

Amostra:

```text
x: 848
y: 1040
w: 404
h: 64
```

Conteúdo:

```text
Início | Pedidos | Clientes | Mais
```

Observação abaixo da amostra:

```text
Somente quando previsto na baseline.
```

Essa observação ocupa:

```text
x: 848
y: 1112
w: 404
h: 16
```

---

## 5. TIPOGRAFIA (Inter - Wireframe)

### Área

```text
x: 456 px
y: 428 px
w: 360 px
h: 160 px

limite direito: 816 px
limite inferior: 588 px
```

### Conteúdo exato

```text
5. TIPOGRAFIA (Inter - Wireframe)

WF-TITLE        20 px | 28 px | SemiBold 600
WF-SECTION      14 px | 20 px | SemiBold 600
WF-BODY         16 px | 24 px | Regular 400
WF-LABEL        14 px | 20 px | Medium 500
WF-ACTION-TEXT  16 px | 24 px | Medium 500
WF-CAPTION      12 px | 16 px | Regular 400
```

### Disposição interna

```text
padding:
16 px horizontal
12 px vertical

título:
x = 472
y = 440
h = 20

lista:
x = 472
y = 472
w = 328
```

Cada token ocupa uma linha com `20 px` de altura visual.

Estrutura de cada linha:

```text
TOKEN | tamanho | line-height | peso
```

Letter-spacing:

```text
normal
```

### Referência normativa

```text
docs/wireframes/images/README.md
6.3 — Tipografia técnica
```

Inter é exclusiva da representação técnica.

Não aplicar Inter automaticamente à marca `SaOr / Sales Order`.

---

## 6. PALETA TÉCNICA — CLARO

### Área

```text
x: 456 px
y: 604 px
w: 360 px
h: 220 px

limite direito: 816 px
limite inferior: 824 px
```

### Conteúdo

A prancha demonstra os dez tokens técnicos Claro:

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

### Disposição interna

```text
padding:
16 px horizontal
12 px vertical

título:
x = 472
y = 616
h = 20

primeira linha:
y = 648

line-height entre tokens:
16 px
```

Cada linha contém:

```text
[amostra cromática]  TOKEN  HEX
```

Amostra cromática:

```text
w: 16 px
h: 16 px
```

Colunas:

```text
swatch:
x = 472

token:
x = 496

HEX:
alinhado à direita da área interna
```

### Referência normativa

```text
docs/wireframes/images/README.md
6.1 — Claro
```

A paleta é técnica.

Não representar estes tokens como paleta oficial do produto.

---

## 7. ELEVAÇÃO

### Área

```text
x: 456 px
y: 840 px
w: 360 px
h: 180 px

limite direito: 816 px
limite inferior: 1020 px
```

### Conteúdo visual obrigatório

O cartão deve mostrar quatro amostras físicas, organizadas em matriz `2 × 2`.

```text
┌────────┐        ┌────────┐
│   E0   │        │   E1   │
└────────┘        └────────┘
0/0/0/0%          0/1/2/12%

┌────────┐        ┌────────┐
│   E2   │        │   E3   │
└────────┘        └────────┘
0/2/6/16%         0/4/12/20%
```

### Posições das amostras

Dimensão de cada amostra:

```text
w: 128 px
h: 44 px
```

Primeira coluna:

```text
x: 496 px
```

Segunda coluna:

```text
x: 648 px
```

Primeira linha:

```text
y da amostra: 872 px
y da legenda: 920 px
```

Segunda linha:

```text
y da amostra: 948 px
y da legenda: 996 px
```

### Efeitos

```text
E0:
0 / 0 / 0 / 0%

E1:
0 / 1 / 2 / 12%

E2:
0 / 2 / 6 / 16%

E3:
0 / 4 / 12 / 20%
```

Ordem da notação:

```text
offset-x / offset-y / blur / opacidade
```

Cor-base:

```text
preto neutro
```

### Referência normativa

```text
docs/wireframes/images/README.md
8 — Bordas, radius, elevação e iconografia
```

A amostra deve demonstrar o efeito visual, não apenas escrever o token.

---

## 8. RADIUS

### Área

```text
x: 456 px
y: 1036 px
w: 360 px
h: 108 px

limite direito: 816 px
limite inferior: 1144 px
```

### Conteúdo visual obrigatório

Duas amostras lado a lado:

```text
┌──────────┐      ┌──────────┐
│  12 px   │      │  16 px   │
└──────────┘      └──────────┘
Campos e botões   Cards e modais
```

### Posições

Amostras:

```text
12 px:
x = 496
y = 1060
w = 128
h = 44

16 px:
x = 648
y = 1060
w = 128
h = 44
```

Legendas:

```text
y = 1108
h = 16
```

### Referência normativa

```text
docs/wireframes/images/README.md
8 — Bordas, radius, elevação e iconografia
```

As amostras devem exibir os cantos fisicamente arredondados.

---

## 9. ÍCONES (Material Icons Outlined)

### Área

```text
x: 12 px
y: 1168 px
w: 620 px
h: 220 px

limite direito: 632 px
limite inferior: 1388 px
```

### Estrutura

O cartão demonstra dois tamanhos técnicos.

```text
20 px
ícone auxiliar

24 px
ação / navegação
```

### Amostras visuais

Cada amostra fica dentro de uma área demonstrativa própria.

Primeira amostra:

```text
x: 140 px
y: 1212 px
área demonstrativa: 128 × 96 px

ícone:
20 × 20 px
centralizado
```

Segunda amostra:

```text
x: 356 px
y: 1212 px
área demonstrativa: 128 × 96 px

ícone:
24 × 24 px
centralizado
```

Legendas:

```text
Ícones auxiliares
Ação / navegação
```

### Ícones demonstrativos

Usar a mesma linguagem da A_v02:

```text
Material Icons Outlined
```

A seleção do glifo é apenas demonstrativa.

Não cria função no produto.

### Referência normativa

```text
docs/wireframes/images/README.md
8 — Iconografia
```

Touch target de ações interativas permanece mínimo `48 × 48 px`.

---

## 10. ESTADOS (Componentes)

### Área

```text
x: 648 px
y: 1168 px
w: 620 px
h: 220 px

limite direito: 1268 px
limite inferior: 1388 px
```

### Estados exibidos

```text
Default
Focus
Pressed / Selected
Disabled
Error
```

`Hover` aparece apenas como observação documental:

```text
Hover: documentado; não obrigatório em mobile.
```

### Disposição

Área interna:

```text
x: 664
w: 588
```

Amostras de estado:

```text
w: 540 px
h: 24 px

x: 688 px
```

Posições verticais:

```text
Default             y = 1212
Focus               y = 1244
Pressed / Selected  y = 1276
Disabled            y = 1308
Error               y = 1340
```

Gap vertical entre amostras:

```text
8 px
```

Observação Hover:

```text
x = 664
y = 1372
```

### Regra visual

Cada estado deve possuir diferenciação perceptível.

Cor não pode ser o único indicador de estado.

### Referência normativa

```text
docs/wireframes/images/README.md
9 — Estados técnicos
10 — Acessibilidade estrutural
```

---

## 11. REGRAS GERAIS DE COMPONENTES

### Área

```text
x: 12 px
y: 1404 px
w: 780 px
h: 148 px

limite direito: 792 px
limite inferior: 1552 px
```

### Conteúdo exato

```text
11. REGRAS GERAIS DE COMPONENTES

Touch target mínimo: 48 × 48 px.

Aplicável a botões, ícones, itens de lista,
navegação e demais áreas interativas.

A área clicável deve respeitar o mínimo mesmo
quando o elemento visual for menor.
```

### Demonstração do touch target

À esquerda do texto deve existir uma amostra quadrada:

```text
x: 28 px
y: 1440 px
w: 48 px
h: 48 px
```

O glifo dentro da amostra pode utilizar um ícone Material Outlined de interação.

A amostra demonstra o alvo mínimo, não uma função específica.

### Texto

```text
x: 96 px
y: 1432 px
w: 680 px
```

### Referência normativa

```text
docs/wireframes/images/README.md
7 — Componentes técnicos de representação
10 — Acessibilidade estrutural
```

---

## BORDAS E DIVISORES

### Área

```text
x: 808 px
y: 1404 px
w: 460 px
h: 148 px

limite direito: 1268 px
limite inferior: 1552 px
```

### Conteúdo visual

Duas demonstrações lado a lado.

#### Borda

Amostra:

```text
x: 824
y: 1440
w: 160
h: 64
```

Aplicação:

```text
borda: 1 px
token Claro: WF-W-BORDER
HEX: #B5B5B5
```

Legenda:

```text
Borda
1 px
```

#### Divisor

Amostra:

```text
x: 1016
y: 1472
w: 220
h: 1
```

Legenda:

```text
Divisor
1 px
```

Uso:

```text
entre seções/listas quando necessário
```

### Referência normativa

```text
docs/wireframes/images/README.md
8 — Bordas, radius, elevação e iconografia
```

---

## 12. OBSERVAÇÕES TÉCNICAS

### Área

```text
x: 12 px
y: 1568 px
w: 1256 px
h: 340 px

limite direito: 1268 px
limite inferior: 1908 px
```

Margem inferior preservada:

```text
12 px
```

### Estrutura interna

O conteúdo é dividido em duas colunas, seguindo a linguagem da A_v02.

Padding:

```text
16 px
```

Área interna total:

```text
x: 28 px
y: 1604 px
w: 1224 px
```

Duas colunas:

```text
COLUNA A
x: 28 px
w: 596 px

GAP
x: 624 px
w: 32 px

COLUNA B
x: 656 px
w: 596 px
```

### Coluna A — itens 1 a 5

```text
1. O viewport representa a tela completa do celular:
   360 × 800 px em escala 1:1.

2. Safe areas de 24 px superior e 32 px inferior
   são referências do wireframe.

3. Na implementação, superfícies podem ocupar 100%
   da tela; conteúdos sensíveis respeitam os insets
   reais da plataforma/dispositivo.

4. Todos os elementos seguem grid de 4 px e escala
   de espaçamento 4 / 8 / 12 / 16 / 24 / 32 px.

5. Inter é tipografia técnica do wireframe e não
   tipografia oficial da marca SaOr.
```

### Coluna B — itens 6 a 10

```text
6. Em páginas seguintes, repetir apenas elementos
   realmente persistentes.

7. Nomenclatura dos arquivos funcionais:
   <ID>-<PÁGINA>-<TOTAL>_v<VERSÃO>.png.

8. Interface multipágina só é aprovada quando todas
   as páginas Claro e Escuro estiverem aprovadas.

9. Cores, ícones e componentes são tokens e
   referências técnicas dos wireframes.

10. Cor nunca deve ser o único indicador de estado.
```

### Tipografia

Usar:

```text
WF-CAPTION
12 px / 16 px
Regular 400
```

Número de cada observação:

```text
WF-LABEL
```

### Referências normativas

As observações são síntese de regras já vigentes em:

```text
docs/wireframes/images/README.md

4 — Referências geométricas
5 — Grid e espaçamento
6 — Tokens e tipografia
7 — Componentes
8 — Bordas/radius/elevação/iconografia
9 — Estados
10 — Acessibilidade
11 — Imagens funcionais
```

Não acrescentar observação de processo, conversa ou validação temporária.

---

# Sequência final de construção da WF-TEMPLATE-B_v01

A prancha deve ser montada nesta sequência física:

```text
01. Canvas 1280 × 1920
02. Cabeçalho
03. Viewport mestre 360 × 800 em 100% / 1:1
04. Cotas do viewport
05. Congelar Cabeçalho + Viewport + Cotas
06. Bloco 1 — Canvas e Viewport
07. Bloco 2 — Safe Areas
08. Bloco 3 — Grid e Spacing
09. Bloco 4 — Componentes
10. Bloco 5 — Tipografia
11. Bloco 6 — Paleta
12. Bloco 7 — Elevação
13. Bloco 8 — Radius
14. Bloco 9 — Ícones
15. Bloco 10 — Estados
16. Bloco 11 — Regras Gerais
17. Bordas e Divisores
18. Bloco 12 — Observações Técnicas
19. Conferência física completa
20. Somente após PASS: geração do PNG correspondente
```

Nenhum passo posterior pode alterar silenciosamente a geometria congelada de passo anterior.

---

# Referências específicas utilizadas pela composição B

```text
docs/wireframes/images/README.md

docs/wireframes/images/templates/README.md

docs/wireframes/images/templates/references/
Especificação Técnica - Prancha de Trabalho.png

docs/wireframes/images/templates/references/
Especificação Técnica do Viewport Mobile.png

docs/wireframes/images/templates/references/
WF-VIEWPORT-360x800-clean.png

docs/wireframes/images/templates/alternatives/
WF-TEMPLATE-A_v02.png

assets/logo/README.md

assets/fonts/logo/README.md
```

Uso das referências:

```text
README técnico
→ medidas, tokens, tipografia, componentes e regras superiores

templates/README.md
→ conceito e governança da Alternativa B

Prancha de Trabalho
→ canvas físico vigente

Especificação Técnica do Viewport Mobile
→ cotas e linguagem das referências dimensionais

WF-VIEWPORT-360x800-clean.png
→ bitmap obrigatório do viewport

WF-TEMPLATE-A_v02.png
→ linguagem visual documental já validada
→ não usar como fonte raster de geometria

assets/logo + assets/fonts/logo
→ marca e tipografia da marca no cabeçalho
```

---

# Gate de conclusão do Wireframe Text da Alternativa B

Antes de produzir a imagem `WF-TEMPLATE-B_v01.png`, o Wireframe Text deve fechar todos os itens:

```text
[ ] frame inicial corresponde à composição especificada abaixo

[ ] canvas = 1280 × 1920 px

[ ] cabeçalho especificado

[ ] viewport mestre definido por arquivo

[ ] viewport físico = 360 × 800 px

[ ] viewport inserido em 100% / 1:1

[ ] cotas do viewport especificadas

[ ] áreas Cabeçalho + Viewport congeladas

[ ] bloco 1 especificado

[ ] bloco 2 especificado

[ ] bloco 3 especificado

[ ] bloco 4 especificado

[ ] bloco 5 especificado

[ ] bloco 6 especificado

[ ] bloco 7 especificado com amostras visuais

[ ] bloco 8 especificado com amostras visuais

[ ] bloco 9 especificado

[ ] bloco 10 especificado

[ ] bloco 11 especificado

[ ] Bordas e Divisores especificado

[ ] bloco 12 especificado

[ ] todas as coordenadas permanecem dentro do canvas

[ ] nenhum cartão invade o viewport

[ ] nenhuma documentação exige resize do viewport

[ ] margem estrutural externa preservada

[ ] referências técnicas identificadas

[ ] não existe requisito funcional inventado

[ ] não existe informação de conversa/processo na prancha
```

Somente depois de este Wireframe Text ser aceito como completo deve ser produzida a imagem correspondente da Alternativa B.