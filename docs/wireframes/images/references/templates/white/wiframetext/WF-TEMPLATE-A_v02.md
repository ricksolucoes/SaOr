# WF-TEMPLATE-A_v02 — Reprodução textual fiel da prancha final

> **Natureza deste documento:** reconstrução retroativa. O PNG `WF-TEMPLATE-A_v02.png` já existia; este Wireframe Text foi escrito a partir dele. Coordenadas lidas na imagem (1024 × 1536 px), com tolerância de ±3 px. Onde o PNG diverge da spec vigente, a divergência está registrada na seção 3 e **não foi corrigida**.

```text
CANVAS FINAL — 1024 × 1536 px

┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ SaOr / Sales Order │ WIREFRAME · PRANCHA TÉCNICA - MODELO A │ WF-TEMPLATE-A │ XX / YY │ v02 │ DD/MM/AAAA │ EM VALIDAÇÃO                      │
│ (Viewport central dominante) │ BASELINE v1.0 │ VARIAÇÃO Claro | Escuro │ ETAPA Wireframe Conceitual em Imagem                                │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

1. CANVAS E VIEWPORT                            VIEWPORT CENTRAL DOMINANTE                6. COMPONENTES (MEDIDAS)
┌────────────────────────────────────────────┐  ┌──────────────────────────────────┐      ┌────────────────────────────────────────────────────┐
│ Canvas da prancha   1024 × 1536 px         │  │         360 px (viewport total)  │      │ App Bar (56 px)                                    │
│ Viewport (interface) 360 × 800 px (1:1)    │  │   12 px | 336 px (área útil) | 12 px │  │ Campo Outlined (56 px)                             │
│ Escala do viewport  1:1 (tamanho real)     │  │ ┌────────────────────────────────┐ │    │ Botão Primário (48 px)                             │
│ Orientação          Retrato (vertical)     │  │ │ 9:41  Safe area (24 px)        │ │    │ Botão Secundário (48 px)                           │
│ Margem horizontal   12 px (estrutura)      │  │ ├────────────────────────────────┤ │    │ Botão Texto (48 px - altura mínima)                │
└────────────────────────────────────────────┘  │ │ (o) Título da Página   [S] [:] │ │    │ Icon Button (touch target 48 × 48 px)              │
                                                │ │     Subtítulo da página        │ │    │ Item de Lista: simples (56) / secundário (64)      │
2. SAFE AREAS (Referência do wireframe)         │ │ Seção de Conteúdo              │ │    │ Card (radius 16 px)                                │
┌────────────────────────────────────────────┐  │ │ Rótulo do campo                │ │    │ Modal / Dialog (margem lateral 24 px)              │
│ Safe area superior  24 px                  │  │ │ [ Texto de exemplo          v ]│ │    │ Bottom Navigation (64 px)                          │
│ Safe area inferior  32 px                  │  │ │ [       Botão Primário        ]│ │    │ + cota azul vertical à direita de cada item        │
│ [i] Referências exclusivas do              │  │ │ [      Botão Secundário       ]│ │    └────────────────────────────────────────────────────┘
│     wireframe; não são paddings            │  │ │   Botão Texto           [G]    │ │
│     ou constantes da implementação.        │  │ │ (o) Título do item           > │ │
└────────────────────────────────────────────┘  │ │ [ Título do Card              ]│ │
                                                │ │ [i] Mensagem informativa       │ │
3. GRID E SPACING                               │ │ [ ^ Área de conteúdo scroll v ]│ │
┌────────────────────────────────────────────┐  │ │ Início Pedidos Clientes Mais   │ │
│ Grid base           4 px                   │  │ │ Safe area (32 px)              │ │
│ Escala de spacing   4/8/12/16/24/32 px     │  │ └────────────────────────────────┘ │
│ Padding-base        16 px (h) / 12 px (v)  │  │        800 px (viewport total)   │
└────────────────────────────────────────────┘  └──────────────────────────────────┘

4. TIPOGRAFIA (Inter - Wireframe)
┌────────────────────────────────────────────┐
│ WF-TITLE / WF-SECTION / WF-BODY            │
│ WF-LABEL / WF-ACTION-TEXT / WF-CAPTION     │
│ (valores + Letter-spacing: normal)         │
└────────────────────────────────────────────┘

5. PALETA DE CORES (Tokens - Claro)
┌────────────────────────────────────────────┐
│ [chip] Primary #1976D2 ... Info #0288D1    │
│ (11 tokens) + nota semântica tracejada     │
└────────────────────────────────────────────┘


7–10 (linha de 4 cards)                                                                                                                         
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 7. ELEVAÇÃO: 4 amostras WF-ELEVATION-0..3   8. RADIUS: 12 px / 16 px                                                                         │
│ 9. ÍCONES: 20 px (home) / 24 px (pessoa)  10. ESTADOS: Default Focus Pressed/Selected Disabled Error                                         │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
11. REGRAS GERAIS DE COMPONENTES │ BORDAS E DIVISORES                                                                                           
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ [mão] Touch Target mínimo 48 × 48 px  │  Borda 1 px (onde aplicável) · Divisor 1 px (entre seções/listas)                                    │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
12. OBSERVAÇÕES TÉCNICAS (2 colunas: 1–5 e 6–10)                                                                                                
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 1–5 (esquerda)                                  6–10 (direita)                                                                               │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

# Especificação de implementação da prancha

## 1. Regra de leitura deste documento

A reprodução textual acima é a **referência conceitual de composição** da `WF-TEMPLATE-A_v02`: ordem das regiões, quais blocos existem, quais ficam lado a lado. Não é escala de caracteres para pixels; as medidas valem somente nas seções abaixo.

```text
canvas (como está no PNG):   1024 × 1536 px
orientação:                  retrato
margem externa:              12 px (esquerda e direita); ~8 px (topo); ~9 px (base)
modelo:                      A — viewport central dominante
variação:                    Claro | Escuro (a imagem é a versão Claro)
```

## 2. Hierarquia de autoridade e estado

```text
1. docs/Documento_Mestre.md — somente conteúdo e comportamento funcional
2. .specs/wireframes/REGRAS-TECNICAS.md — invariantes técnicos
3. .specs/wireframes/PROCESSO-PRANCHA.md — sequência e gates
4. .specs/wireframes/WIREFRAME-TEXT.md — contrato documental
5. este WF-TEMPLATE-A_v02.md — composição específica desta alternativa
6. PNG correspondente — nesta reconstrução, o PNG é a origem do texto
```

```text
STATUS no cabeçalho do PNG: EM VALIDAÇÃO
Gates 1 a 6: não registrados — nenhuma aprovação humana encontrada para esta versão
```

## 3. Divergências entre o PNG e a spec vigente

```text
D1  Canvas 1024 × 1536 px; a spec vigente define 1280 × 1920 px (mesma proporção 2:3).
D2  Safe areas: o PNG mostra faixas de 24 px (superior, com "9:41") e 32 px (inferior),
    e o bloco 2 SAFE AREAS. As notas do modelo B dizem que não existe reserva fixa de safe area.
D3  Viewport NÃO está em 1:1. Na imagem, o frame mede ~262 px de largura e ~851 px de altura
    (cota vertical azul em x ≈ 676, de y 217 a y 1068), ou seja, proporção distorcida
    (360 × 800 = 0,45; na imagem ≈ 0,31). Os rótulos "360 × 800 px (1:1)" não correspondem à geometria desenhada.
D4  Paleta: Primary #1976D2 e semânticas diferentes dos tokens neutros da REGRAS-TECNICAS
    (WF-W-BG #F4F4F4 etc.). O PNG usa Background #FAFAFA, On Surface #212121, Outline #E0E0E0.
D5  Botão Texto e Icon Button lado a lado, com o Icon Button à DIREITA (no modelo C está à esquerda).
D6  Texto da imagem com erros de renderização: "entres seções/listas"; "WF-ELEVATION" com
    espaçamento irregular; "Uma interface multipágina" com glifos trocados na observação 8.
D7  Estados desenhados como barras coloridas cheias (azul/azul-claro/azul/cinza/vermelho),
    sem o contorno de componente usado em B e C.
D8  Nomenclatura de arquivo nas observações: <ID>_<PÁGINA>_<TOTAL>_<VERSÃO>.png, com exemplo
    T00-01-02_v01.png; em B/C: <ID>-<PÁGINA>-<TOTAL>_v<VERSÃO>.png.
```

Estas divergências são registradas, não resolvidas. A decisão de manter ou corrigir cada uma pertence à spec.

---

# Cabeçalho

```text
área: x 12, y 8, w 1001, h 74 (limite direito 1013, inferior 82)
card com borda fina cinza-azulada, cantos arredondados

MARCA          x 12   w 125
IDENTIFICAÇÃO  x 137  w 306
METADADOS      x 443  w 570
```

Marca: "SaOr" (negrito, azul-marinho) acima de "Sales Order" (leve, cinza). Sem ícone.

Identificação:

```text
WIREFRAME
PRANCHA TÉCNICA - MODELO A
(Viewport central dominante)
```

Metadados — linha superior (y 8 a 57):

```text
ID       x 443  w 130   WF-TEMPLATE-A
PÁGINA   x 573  w 103   XX / YY
VERSÃO   x 676  w 97    v02
DATA     x 773  w 112   DD/MM/AAAA
STATUS   x 885  w 128   EM VALIDAÇÃO
```

Linha inferior (y 57 a 82):

```text
BASELINE  x 443  w 130   v1.0
VARIAÇÃO  x 573  w 175   Claro | Escuro
ETAPA     x 748  w 265   Wireframe Conceitual em Imagem
```

---

# Mapa geométrico principal

```text
COLUNA ESQUERDA  x 12   a 319   (w 307)
COLUNA CENTRAL   x 319  a 710   (w 391)  — viewport
COLUNA DIREITA   x 710  a 1013  (w 303)
```

Corpo principal: y 95 a 1181. Linha de cartões inferiores: y 1190 a 1330. Linha de regras: y 1337 a 1425. Observações: y 1430 a 1527.

Blocos (x, y, w, h):

```text
1  CANVAS E VIEWPORT                12   95  307  156
2  SAFE AREAS                       12  261  307  233
3  GRID E SPACING                   12  503  307  124
4  TIPOGRAFIA                       12  637  307  294
5  PALETA DE CORES                  12  939  307  242
6  COMPONENTES (MEDIDAS)           710   95  303 1086
7  ELEVAÇÃO (Sombras)               12 1190  359  140
8  RADIUS                          377 1190  207  140
9  ÍCONES                          591 1190  212  140
10 ESTADOS (Componentes)           809 1190  204  140
11 REGRAS GERAIS DE COMPONENTES     12 1337  513   88
-  BORDAS E DIVISORES              531 1337  482   88
12 OBSERVAÇÕES TÉCNICAS             12 1430 1001   97
```

Estilo dos cards: fundo branco-azulado muito claro, borda fina, radius ~6 px; título numerado "N. TÍTULO" em negrito, subtítulo em peso normal entre parênteses.

---

# Viewport central

Sem card próprio: o viewport fica no espaço entre as colunas, sobre fundo claro.

Frame do viewport (aproximado): x 389 a 651, y 217 a 1068. Contorno cinza com cantos arredondados.

Cotas (azul):

```text
360 px (viewport total)      linha horizontal em y ≈ 133, x 383–655; rótulo "(viewport total)" abaixo
12 px (margem) | 336 px (área útil) | 12 px (margem)
                             linha em y ≈ 160; rótulos azuis; extensões verticais tracejadas até o frame
24 px — Safe area superior (referência)
                             à esquerda do frame, x ≈ 327–375, y 217–253
32 px — Safe area inferior (referência)
                             à esquerda do frame, y ≈ 1032–1068
800 px (viewport total)      linha vertical azul em x ≈ 676, y 217–1068; rótulo vertical em x ≈ 687
```

Conteúdo do viewport (de cima para baixo):

```text
Faixa safe area superior (fundo azul claro): "9:41" à esquerda; "Safe area (24 px) / Referência do wireframe" centralizado
App bar: avatar circular cinza; "Título da Página" / "Subtítulo da página"; ícone search; ícone more_vert
"Seção de Conteúdo" (WF-SECTION)
Campo outlined com rótulo flutuante: "Rótulo do campo" / "Texto de exemplo" / expand_more
Botão Primário (azul)
Botão Secundário (contorno)
Botão Texto "Botão Texto" (azul) + Icon Button settings à direita
Item de lista: avatar cinza / "Título do item" / "Texto secundário de apoio" / chevron_right
Card: "Título do Card" / "Texto de exemplo do card com algumas informações."
Mensagem informativa: ícone info azul + "Mensagem informativa de exemplo." (fundo azul claro)
Área tracejada: seta para cima / "Área de conteúdo indicando scroll vertical" / seta para baixo
Bottom navigation: Início (ativo, azul), Pedidos, Clientes, Mais
Faixa safe area inferior (azul claro): "Safe area (32 px) / Referência do wireframe"
```

---

# 1. CANVAS E VIEWPORT

```text
1. CANVAS E VIEWPORT

Canvas da prancha      1024 × 1536 px
Viewport (interface)   360 × 800 px (1:1)
Escala do viewport     1:1 (tamanho real)
Orientação             Retrato (vertical)
Margem horizontal      12 px (estrutura)
```

Rótulos em WF-BODY; valores em coluna alinhada à direita dos rótulos (x ≈ 158).

# 2. SAFE AREAS (Referência do wireframe)

```text
Safe area superior   24 px
Safe area inferior   32 px
```

Caixa informativa (fundo azul claro, ícone info azul):

```text
As safe areas de 24 px superior e 32 px inferior são referências exclusivas do wireframe.
Não constituem paddings ou constantes obrigatórias da implementação.
Na implementação, as superfícies podem ocupar 100% da tela, enquanto conteúdos
sensíveis devem respeitar os insets reais da plataforma/dispositivo.
```

# 3. GRID E SPACING

```text
Grid base            4 px
Escala de spacing    4 / 8 / 12 / 16 / 24 / 32 px
Padding-base         16 px (horizontal)
                     12 px (vertical)
```

# 4. TIPOGRAFIA (Inter - Wireframe)

Cada token em duas linhas, separadas por divisor fino:

```text
WF-TITLE         20 px | 28 px | SemiBold (600)    Letter-spacing: normal
WF-SECTION       14 px | 20 px | SemiBold (600)    Letter-spacing: normal
WF-BODY          16 px | 24 px | Regular (400)     Letter-spacing: normal
WF-LABEL         14 px | 20 px | Medium (500)      Letter-spacing: normal
WF-ACTION-TEXT   16 px | 24 px | Medium (500)      Letter-spacing: normal
WF-CAPTION       12 px | 16 px | Regular (400)     Letter-spacing: normal
```

# 5. PALETA DE CORES (Tokens - Claro)

Cada linha: swatch retangular colorido + nome + HEX.

```text
Primary      #1976D2   azul
On Primary   #FFFFFF   branco com contorno
Secondary    #9E9EDE   lilás (o swatch é azul-claro; ver D4)
Background   #FAFAFA
Surface      #FFFFFF
On Surface   #212121   quase preto
Outline      #E0E0E0
Error        #D32F2F
Success      #2E7D32
Warning      #ED6C02
Info         #0288D1
```

Nota (caixa tracejada azul, à direita da lista):

```text
Estas cores são tokens semânticos utilizados na representação visual do wireframe.
Não representam, obrigatoriamente, a paleta definitiva do produto.
```

---

# 6. COMPONENTES (MEDIDAS)

Cada componente: rótulo em negrito + medida entre parênteses; amostra à esquerda; cota azul vertical à direita com "NN px".

```text
App Bar (56 px)                         [menu] Título [search]                    cota 56 px
Campo Outlined (56 px)                  Rótulo / Texto de exemplo / expand_more   cota 56 px
Botão Primário (48 px)                  fundo azul, texto branco                  cota 48 px
Botão Secundário (48 px)                fundo cinza claro, contorno               cota 48 px
Botão Texto (48 px - altura mínima)     "Botão Texto" azul, sem contorno          cota 48 px
Icon Button (touch target 48 × 48 px)   ícone settings                            cota 48 px
Item de Lista
  Item simples (56 px)                  avatar / Título do item / chevron_right   cota 56 px
  Item com secundário (64 px)           avatar / Título do item /
                                        Texto secundário adicional em duas linhas /
                                        chevron_right                             cota 64 px
Card (radius 16 px)                     Título do Card / Texto de exemplo do card.
                                        legenda "Radius: 16 px"
Modal / Dialog (margem lateral 24 px)   fundo cinza; modal com alça;
                                        Título do Modal / Texto de exemplo do modal.;
                                        [Cancelar] [Confirmar]
                                        legenda "Margem lateral: 24 px | Radius: 16 px"
Bottom Navigation (64 px)               Início (ativo), Pedidos, Clientes, Mais   cota 64 px
                                        legenda "Uso somente quando previsto pela interface/baseline."
```

Observação de fidelidade: neste modelo o Botão Texto e o Icon Button aparecem em linhas separadas no bloco 6 (Botão Texto isolado; Icon Button logo abaixo) e lado a lado dentro do viewport.

---

# 7. ELEVAÇÃO (Sombras)

Quatro amostras quadradas brancas com sombra crescente, em linha:

```text
WF-ELEVATION-0   0 0 0 / 0%
WF-ELEVATION-1   0 1 2 / 12%
WF-ELEVATION-2   0 2 6 / 16%
WF-ELEVATION-3   0 4 12 / 20%
```

# 8. RADIUS

```text
12 px   Campos e Botões   (amostra retangular)
16 px   Cards e Modais    (amostra retangular)
```

# 9. ÍCONES (Material Icons Outlined)

```text
20 px   ícones auxiliares     (amostra: home)
24 px   Ação / Navegação      (amostra: person)

Material Icons Outlined é apenas referência visual.
```

# 10. ESTADOS (Componentes)

Cinco barras horizontais de largura total, empilhadas:

```text
Default              barra azul
Focus                barra azul claro
Pressed / Selected   barra azul
Disabled             barra cinza
Error                barra vermelha

Hover: documentado;
não obrigatório nas pranchas mobile.
```

---

# 11. REGRAS GERAIS DE COMPONENTES

```text
[ícone de mão]  Touch Target mínimo
                48 × 48 px

Aplicável a todos os elementos interativos
(botões, ícones, itens de lista, navegação, etc).
A área clicável deve respeitar no mínimo 48 × 48 px,
mesmo quando o elemento visual for menor.
```

# BORDAS E DIVISORES

```text
[amostra retangular]   Borda
                       1 px
                       (onde aplicável)

[amostra com linha]    Divisor
                       1 px
                       (entres seções/listas)      ← texto como aparece no PNG (D6)
```

---

# 12. OBSERVAÇÕES TÉCNICAS

Duas colunas, 5 itens cada (coluna esquerda x ≈ 27, direita x ≈ 540), WF-CAPTION, itens numerados.

```text
1. O viewport representa a tela completa do celular (360 × 800 px) em escala 1:1.
2. As safe areas de 24 px (superior) e 32 px (inferior) são referências do wireframe.
3. Na implementação, as superfícies podem ocupar 100% da tela, enquanto conteúdos sensíveis devem
   respeitar os insets reais da plataforma/dispositivo.
4. Todos os elementos seguem o grid de 4 px e a escala de espaçamento definida.
5. A tipografia Inter é exclusiva para os wireframes e não representa a tipografia oficial da marca SaOr.
6. Em páginas seguintes, repetir apenas os elementos realmente persistentes.
7. Nomenclatura dos arquivos: <ID>_<PÁGINA>_<TOTAL>_<VERSÃO>.png
   Exemplo: T00-01-02_v01.png | T00-02-02_v01.png
8. Uma interface multipágina só é aprovada quando todas as páginas, Claro e Escuro, estiverem aprovadas.
9. Cores, ícones e componentes são tokens e referências técnicas dos wireframes.
10. Cor nunca deve ser o único indicador de estado.
```

---

# Checklist de conferência PNG × texto

```text
[x] 12 blocos numerados + região BORDAS E DIVISORES presentes
[x] textos transcritos do PNG, incluindo os que contêm erros de renderização (D6)
[ ] coordenadas conferidas por medição pixel a pixel (hoje: leitura visual, ±3 px)
[ ] divergências D1–D8 decididas na spec (manter, corrigir ou descartar)
[ ] versão Escuro desta prancha (a spec exige Claro e Escuro)
```
