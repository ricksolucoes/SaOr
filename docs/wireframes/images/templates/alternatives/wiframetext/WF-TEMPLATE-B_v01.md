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

Nesta etapa estão definidos somente:

```text
1. Cabeçalho
2. Viewport
```

Os blocos técnicos `1` a `12` da prancha somente serão dimensionados e detalhados depois que Cabeçalho + Viewport estiverem fechados.

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
docs/wireframes/images/templates/alternatives/WF-TEMPLATE-A_v02.png
```

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

### Geometria congelada após esta etapa

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

Essas áreas não podem ser alteradas para acomodar os demais blocos.

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

