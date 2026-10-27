# Wireframes — Regras técnicas canônicas

## 1. Escopo

Esta spec define as regras técnicas invariantes da representação de wireframes.

Ela não define a composição específica de uma prancha-modelo.

## 2. Canvas

```text
Canvas: 1280 × 1920 px
Orientação: retrato
Margem horizontal estrutural: 12 px
```

## 3. Viewport

```text
Viewport lógico: 360 × 800 px
Orientação: retrato
Escala na prancha: 1:1
```

Regras obrigatórias:

- o viewport deve medir fisicamente `360 × 800 px`;
- não redimensionar, esticar, comprimir ou reproporcionar;
- não criar área funcional fora dos `800 px`;
- não desenhar moldura física de aparelho;
- não criar versão específica para iOS ou Android;
- uma legenda de dimensão não substitui a verificação física.

### 3.1 Referências físicas de demonstração

As referências físicas atualmente disponíveis para a variação `white` são:

```text
docs/wireframes/images/references/white/WF-VIEWPORT-360x800-clean.png
docs/wireframes/images/references/white/WF-VIEWPORT-360x800-clean_icone-esquerda.png
docs/wireframes/images/references/white/WF-VIEWPORT-360x800.png
```

`WF-VIEWPORT-360x800.png` (white) foi gerado com a paleta técnica da seção 6 (tabela 6.5) e é usado por `WF-TEMPLATE-A_v04`, `WF-TEMPLATE-B_v02` e `WF-TEMPLATE-C_v02`.

Ambas medem fisicamente `360 × 800 px` e podem ser inseridas em `100%` quando o Wireframe Text específico determinar seu uso.

A diferença entre elas é parte do próprio ativo:

```text
WF-VIEWPORT-360x800-clean.png
→ Botão Texto com Icon Button à direita

WF-VIEWPORT-360x800-clean_icone-esquerda.png
→ Icon Button à esquerda do Botão Texto
```

Nenhuma das duas substitui universalmente a outra. A escolha do bitmap pertence ao Wireframe Text específico. É proibido trocar, reconstruir ou adaptar silenciosamente um ativo para reproduzir a outra variante.

As `WF-TEMPLATE-A_v03`, `WF-TEMPLATE-B_v01` e `WF-TEMPLATE-C_v01` (históricas) usavam `WF-VIEWPORT-360x800-clean_icone-esquerda.png`. As `WF-TEMPLATE-A_v04`, `WF-TEMPLATE-B_v02` e `WF-TEMPLATE-C_v02` usam `WF-VIEWPORT-360x800.png`. O arquivo `WF-VIEWPORT-360x800-clean.png` permanece preservado como referência válida para artefatos que o especifiquem.

As referências físicas atualmente disponíveis para a variação `black` são:

```text
docs/wireframes/images/references/black/WF-VIEWPORT-360x800.png
```

`WF-VIEWPORT-360x800.png` (black) foi gerado com a paleta técnica da seção 6 (tabela 6.6) e é usado por `WF-TEMPLATE-A_v01` e `WF-TEMPLATE-B_v01` (black). Referências físicas específicas da variação `black` pertencem a `docs/wireframes/images/references/black/`.

Não reutilizar por inferência um bitmap específico de `white` em uma prancha `black`. As dimensões normativas do viewport permanecem as mesmas independentemente da variação.

### 3.2 Cotas

Referência física atualmente disponível para a variação `white`:

```text
docs/wireframes/images/references/white/Especificação Técnica do Viewport Mobile.png
```

As cotas abaixo são normativas e independem da variação visual.

Cotas vigentes:

```text
largura total:             360 px
largura útil:              336 px
margem lateral esquerda:    12 px
margem lateral direita:     12 px
altura total:              800 px

12 + 336 + 12 = 360
```

### 3.3 Safe area

Não existe reserva fixa de faixa superior ou inferior de safe area nesta etapa.

Não reservar automaticamente `24 px` no topo ou `32 px` na base.

## 4. Grid e spacing

```text
Base: 4 px
Escala: 4 / 8 / 12 / 16 / 24 / 32 px
Padding-base horizontal: 16 px
Padding-base vertical: 12 px
```

Espaçamento fora dessa escala exige necessidade objetiva registrada no Wireframe Text específico.

## 5. Tipografia técnica

```text
Família: Inter
```

| Token | Peso | Tamanho | Line-height |
|---|---:|---:|---:|
| `WF-TITLE` | 600 | 20 px | 28 px |
| `WF-SECTION` | 600 | 14 px | 20 px |
| `WF-BODY` | 400 | 16 px | 24 px |
| `WF-LABEL` | 500 | 14 px | 20 px |
| `WF-ACTION-TEXT` | 500 | 16 px | 24 px |
| `WF-CAPTION` | 400 | 12 px | 16 px |

Inter é tipografia técnica e não substitui a tipografia oficial da marca.

## 6. Tokens técnicos

Esta seção é a **fonte única das cores da representação técnica** dos wireframes. Nenhum Wireframe Text, prancha ou montagem pode usar cor que não conste nas tabelas 6.5 e 6.6.

As cores técnicas pertencem à representação dos wireframes. Elas **não redefinem nem substituem** a paleta funcional/visual do produto documentada no Documento Mestre ou em etapas posteriores de Design Visual.

### 6.1 Fonte e precedência

```text
1. Token do Documento Mestre §20.1 (Tema Claro → white; Tema Escuro → black)
   → usado como está, sem recalcular.
2. Neutros técnicos WF-W-* e WF-B-*
   → definidos nesta seção.
3. Lacuna: cor sem token no Documento Mestre
   → definida por teste (6.2) e derivação reproduzível (6.3);
   → marcada com * nas tabelas;
   → só vale depois da aprovação humana registrada nesta seção.
```

É proibido:

- usar cor fora das tabelas 6.5 e 6.6;
- inferir equivalente de uma variação na outra sem teste;
- alterar token durante a montagem ou a criação de um Wireframe Text; a inconsistência volta para esta seção (`MONTAGEM-IMAGEM.md`, seção 14);
- misturar tokens `WF-W-*` e `WF-B-*` sem regra explícita.

### 6.2 Critérios de teste

Fórmula: luminância relativa e razão de contraste da WCAG 2.2. A razão é calculada contra as três superfícies do tema (`SURFACE`, `BG`, `SURFACE-ALT`) e a tabela registra a **razão e o nível do pior caso**.

| Papel da cor | Critério |
|---|---|
| Texto e ícone informativo | AAA (7:1) sobre `SURFACE`; mínimo AA (4,5:1) sobre `BG` e `SURFACE-ALT`; texto grande mínimo 3:1 |
| Par texto sobre preenchimento | testado como texto: o texto sobre o preenchimento |
| Borda de controle, foco e indicador não textual | mínimo 3:1 |
| Divisor e borda decorativa | sem exigência; proibida como borda de controle |
| Componente inativo | isento; razão registrada só como informação |

Regras do teste:

- abaixo do mínimo, a cor é inválida e não pode ser registrada;
- nível abaixo de AAA sobre `SURFACE` é aceito somente com a exceção registrada na coluna Observação;
- a cor nunca é o único indicador de estado (seção 11).

### 6.3 Derivação das lacunas

Cada lacuna registra a regra que a gerou, para que qualquer execução chegue ao mesmo HEX:

```text
Info BG                 mistura de 10% da cor Info sobre WF-*-SURFACE
Secondary               matiz e saturação do valor anterior (#9E9EDE); só a luminosidade muda,
                        com o menor ajuste que dá AAA nas três superfícies
WF-*-BORDER-CONTROL     cinza neutro (R = G = B) mais próximo de WF-*-BORDER que dá 3:1
                        nas três superfícies
Warning (texto/ícone)   white: matiz de #ED6C02 com o menor escurecimento que dá AA nas três superfícies
On Warning              reuso do texto principal (white) ou de text.inverse (black)
Zebra black             mesmo deslocamento de nível da zebra white em relação a SURFACE (9 níveis)
BRAND / On Brand black  WF-B-TEXT como fundo e WF-B-BG como texto
```

Nova lacuna: aplicar 6.2, registrar a regra de derivação nesta lista, acrescentar a linha à tabela e submeter à aprovação humana antes do uso.

### 6.4 Controle de mudança

- Qualquer alteração de token cria nova revisão desta seção, com revalidação completa das tabelas e aprovação humana.
- Mudança de token no Documento Mestre §20.1 exige revalidar as tabelas antes de qualquer novo Wireframe Text.
- Wireframe Texts `APROVADO E CONGELADO` não são editados; a mudança de cor gera nova versão do Wireframe Text.
- O Wireframe Text cita tokens pelo nome. O HEX aparece apenas no bloco de paleta, que deve ser cópia da tabela vigente (`WIREFRAME-TEXT.md`, seção 4.2).

Conjunto semântico white anterior, usado por `WF-TEMPLATE-A_v03`, `WF-TEMPLATE-B_v01` e `WF-TEMPLATE-C_v01` e preservado como histórico dessas versões:

```text
Primary #0061FE · On Primary #FFFFFF · Secondary #9E9EDE · Info #0288D1
Error #D32F2F · Success #2E7D32 · Warning #ED6C02 · Info BG #DDEEFC
```

Esse conjunto **não vale** para novos Wireframe Texts.

### 6.5 Claro (white)

Superfícies de teste: `SURFACE` `#FFFFFF`, `BG` `#F4F4F4`, `SURFACE-ALT` `#EAEAEA`. `*` = lacuna do Documento Mestre.

| Token | HEX | Origem | Papel | Contraste | Nível | Observação |
|---|---|---|---|---|---|---|
| `WF-W-BG` | `#F4F4F4` | Vigente (esta seção) | Fundo da prancha / app bar | 15,82 (TEXT sobre ele) | AAA |  |
| `WF-W-SURFACE` | `#FFFFFF` | Vigente (esta seção) | Superfície de cards, campos, viewport | 17,40 (TEXT sobre ele) | AAA |  |
| `WF-W-SURFACE-ALT` | `#EAEAEA` | Vigente (esta seção) | Superfície alternativa, avatares, placeholders | 14,47 (TEXT sobre ele) | AAA |  |
| `WF-W-BORDER` | `#B5B5B5` | Vigente (esta seção) | Divisor e borda decorativa | SURFACE 2,05 · BG 1,86 · ALT 1,70 | decorativo (isento) | Uso restrito a divisores decorativos; nunca em borda de controle |
| `WF-W-BORDER-CONTROL` \* | `#868686` | Lacuna → teste e derivação (6.3) | Borda de campos, botões secundários e icon buttons | SURFACE 3,64 · BG 3,31 · ALT 3,03 | OK (≥3:1) | Cinza neutro. O border.default do Doc. Mestre (#64748B) é azulado |
| `WF-W-TEXT` | `#1A1A1A` | Vigente (esta seção) | Texto principal | SURFACE 17,40 · BG 15,82 · ALT 14,47 | AAA |  |
| `WF-W-TEXT-2` | `#565656` | Vigente (esta seção) | Texto secundário | SURFACE 7,34 · BG 6,67 · ALT 6,10 | SURFACE AAA · pior caso AA |  |
| `WF-W-ACTION` | `#333333` | Vigente (esta seção) | Ícones e ações neutras | SURFACE 12,63 · BG 11,49 · ALT 10,50 | AAA |  |
| `WF-W-DISABLED` | `#9A9A9A` | Vigente (esta seção) | Componente inativo | SURFACE 2,81 · BG 2,56 · ALT 2,34 | isento | Inativo é isento no WCAG 1.4.3 e 1.4.11; razão só informativa |
| `WF-W-FOCUS` | `#4A4A4A` | Vigente (esta seção) | Anel de foco | SURFACE 8,86 · BG 8,06 · ALT 7,37 | OK (≥3:1) |  |
| `WF-W-STATUS` | `#626262` | Vigente (esta seção) | Rótulo de status neutro | SURFACE 6,10 · BG 5,55 · ALT 5,07 | AA | AA sobre SURFACE: exceção registrada (neutro vigente) |
| Primary | `#004A99` | Doc. Mestre §20.1 action.primary | Ação principal, link, cotas, destaque | SURFACE 8,61 · BG 7,83 · ALT 7,16 | AAA | Substitui #0061FE do conjunto anterior |
| On Primary | `#FFFFFF` | Doc. Mestre §20.1 text.inverse | Texto sobre Primary | 8,61 (sobre Primary) | AAA |  |
| Secondary \* | `#3C3CB0` | Lacuna → teste e derivação (6.3) | Apoio / acento secundário | SURFACE 8,52 · BG 7,74 · ALT 7,08 | AAA | Substitui #9E9EDE (2,50:1 sobre SURFACE, reprovava) |
| Info | `#004A99` | Doc. Mestre §20.1 status.info | Informação (ícone e texto) | SURFACE 8,61 · BG 7,83 · ALT 7,16 | AAA | Igual ao Primary, como no Doc. Mestre |
| Error | `#991B1B` | Doc. Mestre §20.1 status.error | Erro (ícone e texto) | SURFACE 8,31 · BG 7,56 · ALT 6,91 | SURFACE AAA · pior caso AA | Substitui #D32F2F do conjunto anterior |
| Success | `#166534` | Doc. Mestre §20.1 status.success | Sucesso (ícone e texto) | SURFACE 7,13 · BG 6,48 · ALT 5,93 | SURFACE AAA · pior caso AA | Substitui #2E7D32 do conjunto anterior |
| Warning (texto/ícone) \* | `#AC4F01` | Lacuna → derivação (6.3) | Aviso em texto solto e ícone sobre superfície | SURFACE 5,42 · BG 4,93 · ALT 4,51 | AA | AA, não AAA: matiz de #ED6C02 com o menor escurecimento que dá AA nas 3 superfícies. Para AAA seria #7E3A01 (mais escuro) |
| Warning (preenchimento) \* | `#ED6C02` | Existente nos WT white, validado por teste | Fundo de banner, badge e chip de aviso | 5,59 (On Warning sobre ele) | AA | Não usar como cor de texto (3,11:1 sobre SURFACE) |
| On Warning \* | `#1A1A1A` | Reuso de WF-W-TEXT | Texto e ícone sobre Warning (preenchimento) | 5,59 (sobre Warning (preenchimento)) | AA |  |
| Info BG \* | `#E6EDF5` | Lacuna → derivação (6.3) | Fundo do banner informativo, pílula ativa | Info 7,30 · TEXT 14,75 (sobre ele) | AAA | Substitui #DDEEFC do conjunto anterior |
| BRAND | `#0F172A` | Existente nos WT white | Marca, badge numerado | 17,85 (On Brand sobre ele) | AAA | Sem token no Doc. Mestre; mantida |
| On Brand | `#FFFFFF` | Existente nos WT white | Texto sobre BRAND | 17,85 (sobre BRAND) | AAA |  |
| Zebra de tabela | `#F6F6F6` | Existente nos WT white | Faixa zebra (decorativa) | 16,10 (WF-W-TEXT sobre ela) | AAA |  |

### 6.6 Escuro (black)

Superfícies de teste: `SURFACE` `#1E1E1E`, `BG` `#121212`, `SURFACE-ALT` `#2A2A2A`. `*` = lacuna do Documento Mestre.

| Token | HEX | Origem | Papel | Contraste | Nível | Observação |
|---|---|---|---|---|---|---|
| `WF-B-BG` | `#121212` | Vigente (esta seção) | Fundo da prancha / app bar | 16,73 (TEXT sobre ele) | AAA |  |
| `WF-B-SURFACE` | `#1E1E1E` | Vigente (esta seção) | Superfície de cards, campos, viewport | 14,89 (TEXT sobre ele) | AAA |  |
| `WF-B-SURFACE-ALT` | `#2A2A2A` | Vigente (esta seção) | Superfície alternativa, avatares, placeholders | 12,82 (TEXT sobre ele) | AAA |  |
| `WF-B-BORDER` | `#5E5E5E` | Vigente (esta seção) | Divisor e borda decorativa | SURFACE 2,57 · BG 2,89 · ALT 2,21 | decorativo (isento) | Uso restrito a divisores decorativos; nunca em borda de controle |
| `WF-B-BORDER-CONTROL` \* | `#737373` | Lacuna → teste e derivação (6.3) | Borda de campos, botões secundários e icon buttons | SURFACE 3,52 · BG 3,95 · ALT 3,03 | OK (≥3:1) | Cinza neutro. O border.default do Doc. Mestre (#64748B) é azulado |
| `WF-B-TEXT` | `#F2F2F2` | Vigente (esta seção) | Texto principal | SURFACE 14,89 · BG 16,73 · ALT 12,82 | AAA |  |
| `WF-B-TEXT-2` | `#C2C2C2` | Vigente (esta seção) | Texto secundário | SURFACE 9,36 · BG 10,52 · ALT 8,06 | AAA |  |
| `WF-B-ACTION` | `#E0E0E0` | Vigente (esta seção) | Ícones e ações neutras | SURFACE 12,63 · BG 14,19 · ALT 10,87 | AAA |  |
| `WF-B-DISABLED` | `#777777` | Vigente (esta seção) | Componente inativo | SURFACE 3,72 · BG 4,18 · ALT 3,21 | isento | Inativo é isento; razão só informativa |
| `WF-B-FOCUS` | `#D0D0D0` | Vigente (esta seção) | Anel de foco | SURFACE 10,81 · BG 12,15 · ALT 9,31 | OK (≥3:1) |  |
| `WF-B-STATUS` | `#A8A8A8` | Vigente (esta seção) | Rótulo de status neutro | SURFACE 7,01 · BG 7,88 · ALT 6,04 | SURFACE AAA · pior caso AA |  |
| Primary | `#8ABEFF` | Doc. Mestre §20.1 action.primary | Ação principal, link, cotas, destaque | SURFACE 8,65 · BG 9,71 · ALT 7,44 | AAA |  |
| On Primary | `#0F1115` | Doc. Mestre §20.1 text.inverse | Texto sobre Primary | 9,80 (sobre Primary) | AAA |  |
| Secondary \* | `#B3B3E5` | Lacuna → teste e derivação (6.3) | Apoio / acento secundário | SURFACE 8,33 · BG 9,36 · ALT 7,17 | AAA | Substitui #9E9EDE (5,74:1 sobre ALT, só AA) |
| Info | `#8ABEFF` | Doc. Mestre §20.1 status.info | Informação (ícone e texto) | SURFACE 8,65 · BG 9,71 · ALT 7,44 | AAA | Igual ao Primary, como no Doc. Mestre |
| Error | `#FCA5A5` | Doc. Mestre §20.1 status.error | Erro (ícone e texto) | SURFACE 8,78 · BG 9,87 · ALT 7,56 | AAA |  |
| Success | `#A7F3D0` | Doc. Mestre §20.1 status.success | Sucesso (ícone e texto) | SURFACE 13,00 · BG 14,61 · ALT 11,19 | AAA |  |
| Warning (texto/ícone) | `#FDE68A` | Doc. Mestre §20.1 status.warning | Aviso em texto solto e ícone sobre superfície | SURFACE 13,39 · BG 15,04 · ALT 11,53 | AAA |  |
| Warning (preenchimento) | `#FDE68A` | Doc. Mestre §20.1 status.warning | Fundo de banner, badge e chip de aviso | 15,17 (On Warning sobre ele) | AAA | Mesmo valor do texto/ícone |
| On Warning \* | `#0F1115` | Reuso de Doc. Mestre §20.1 text.inverse | Texto e ícone sobre Warning (preenchimento) | 15,17 (sobre Warning (preenchimento)) | AAA |  |
| Info BG \* | `#292E34` | Lacuna → derivação (6.3) | Fundo do banner informativo, pílula ativa | Info 7,10 · TEXT 12,22 (sobre ele) | AAA |  |
| BRAND \* | `#F2F2F2` | Lacuna → derivação (6.3) | Badge numerado (fundo claro) | 16,73 (On Brand sobre ele) | AAA | Sem equivalente no Doc. Mestre. Cabeçalho black usa o logo para fundos escuros, sem preenchimento BRAND |
| On Brand \* | `#121212` | Reuso de WF-B-BG | Texto sobre BRAND | 16,73 (sobre BRAND) | AAA |  |
| Zebra de tabela \* | `#272727` | Lacuna → derivação (6.3) | Faixa zebra (decorativa) | 13,34 (WF-B-TEXT sobre ela) | AAA |  |

Cor nunca pode ser o único indicador de estado.

### 6.7 Estado das lacunas desta revisão

```text
Cores marcadas com * (white e black): APROVADO E CONGELADO
Aprovação humana explícita: REGISTRADA em 27/10/2026
```

As cores marcadas com `*` foram aprovadas pelo responsável em 27/10/2026 e podem ser usadas em Wireframe Text e em imagem final. Qualquer alteração dessas cores reabre este estado (6.4).

## 7. Componentes técnicos

| Elemento | Especificação |
|---|---|
| App Bar | `56 px` |
| Touch target | mínimo `48 × 48 px` |
| Campo Outlined | `56 px`, radius `12 px`, borda `1 px` quando aplicável |
| Botão textual | altura mínima `48 px`, radius `12 px` |
| Icon Button | touch target mínimo `48 × 48 px` |
| Item simples | mínimo `56 px` |
| Item com secundário/status | mínimo `64 px` |
| Card | radius `16 px`, borda `1 px` quando necessária |
| Modal/Dialog | margem lateral `24 px`, radius `16 px` |
| Bottom Navigation | `64 px` quando prevista na baseline |

## 8. Bordas, radius e elevação

```text
Bordas: 1 px quando necessárias
Divisores: 1 px
Campos/botões: radius 12 px
Cards/modais: radius 16 px
```

Elevação:

```text
WF-ELEVATION-0: 0 / 0 / 0 / 0%
WF-ELEVATION-1: 0 / 1 / 2 / 12%
WF-ELEVATION-2: 0 / 2 / 6 / 16%
WF-ELEVATION-3: 0 / 4 / 12 / 20%
```

Ordem:

```text
offset-x / offset-y / blur / opacidade
```

Elevação na variação `black`: a sombra `rgba(0,0,0,·)` dos tokens `WF-ELEVATION-*` é pouco perceptível sobre superfícies escuras (sobre `WF-B-SURFACE` #1E1E1E, a sombra E3 escurece apenas cerca de 6 níveis de cinza), e o que funciona no white não é aplicado por semelhança. Nas amostras de elevação da variação `black`, o preenchimento usa **um único token existente mais claro que o card**, `WF-B-SURFACE-ALT`, do mesmo modo que o white usa uma única cor nas amostras; os parâmetros de sombra permanecem os da lista acima, e o nível é identificado pela legenda. Não se criam tokens novos de superfície por nível de elevação. Definição aprovada em 27/10/2026 e aplicada em `WF-TEMPLATE-A_v01` e `WF-TEMPLATE-B_v01` (black).

Os tokens `WF-ELEVATION-*` governam elevação técnica de componentes e amostras de interface. Uma sombra usada exclusivamente como tratamento documental da própria prancha pode ser definida pelo Wireframe Text específico quando fizer parte de uma composição aprovada. Nesse caso, ela não cria automaticamente novo token de componente nem regra universal para futuras interfaces.

## 9. Iconografia

```text
Referência: Material Icons Outlined
Auxiliar: 20 px
Ação/navegação: 24 px
Touch target: mínimo 48 × 48 px
```

## 10. Estados

```text
default
focus
pressed / selected
disabled
error
hover
```

`hover` é documentado, mas não é obrigatório em prancha mobile sem necessidade específica.

## 11. Acessibilidade estrutural

A composição deve preservar:

- cor nunca como único indicador;
- touch target mínimo;
- ordem de leitura clara;
- campos com rótulos;
- erro próximo ao contexto;
- foco e seleção distinguíveis;
- hierarquia tipográfica consistente;
- contraste de texto, controles e indicadores conforme os critérios da seção 6.2;
- ausência de compactação prejudicial.
