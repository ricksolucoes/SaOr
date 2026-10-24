# SaOr - Sales Order
## Controle da etapa — Wireframes Conceituais em Imagem

**Baseline funcional:** v1.0 — APROVADO / BASELINE FUNCIONAL  
**Etapa atual:** Wireframe Conceitual em Imagem  
**Status deste documento:** EM VALIDAÇÃO — especificação técnica em fechamento  
**Interfaces documentadas:** 71  
**Variações obrigatórias:** Claro (`white`) e Escuro (`black`)  
**Quantidade mínima de imagens:** 142  
**Quantidade final de imagens:** variável conforme paginação necessária por interface  
**Fonte funcional:** `docs/Documento_Mestre.md`  
**Registro de não regressão:** `docs/Registro_Fechamento_Documento_Mestre.md`

---

# 1. Finalidade

Este documento controla exclusivamente a produção, validação, aprovação e preservação dos wireframes conceituais em imagem do **SaOr - Sales Order**.

Cada interface `T`, `M` ou `E` da baseline funcional deve possuir, no mínimo:

- uma representação **Claro**, em `docs/wireframes/images/white`;
- uma representação **Escuro**, em `docs/wireframes/images/black`.

Quando todo o conteúdo funcional de uma interface não puder ser representado em um único viewport de `360 × 800 px`, a mesma interface será documentada em páginas sequenciais. Por esse motivo, **142 é o mínimo de imagens**, e não um total rígido.

As variantes Claro e Escuro representam a mesma interface e devem ser estruturalmente equivalentes. As definições deste documento existem para tornar o wireframe reproduzível e transferível ao Figma, sem antecipar o Design Visual definitivo nem a arquitetura de implementação.

---

# 2. Estrutura oficial

```text
docs/
└── wireframes/
    └── images/
        ├── README.md
        ├── white/
        │   ├── .gitkeep
        │   ├── T00-01-01_v01.png
        │   └── ...
        └── black/
            ├── .gitkeep
            ├── T00-01-01_v01.png
            └── ...
```

Os arquivos `.gitkeep` existem somente porque o Git não versiona diretórios vazios.

---

# 3. Referência dimensional aprovada

## 3.1 Viewport mobile oficial

**Viewport lógico oficial: `360 × 800 px`**

Regras aprovadas:

- orientação: **retrato**;
- largura lógica total: `360 px`;
- altura lógica total: `800 px`;
- o retângulo de `360 × 800 px` representa a **tela lógica completa do celular** para esta etapa;
- barras, navegação, indicadores de rolagem e demais elementos que ocupem ou sobreponham a tela devem ser considerados **dentro desses 360 × 800 px**, nunca acrescentados por fora;
- não deve ser desenhada moldura física de aparelho;
- não deve ser criada uma versão específica para iOS ou Android;
- paisagem não faz parte da produção inicial e será estudada posteriormente;
- tablet e desktop não serão produzidos automaticamente nesta etapa.

## 3.2 Safe areas técnicas

Dentro dos `360 × 800 px`, reservar:

```text
Safe area superior: 24 px
Safe area inferior: 32 px
```

Essas reservas são técnicas e neutras em relação ao sistema operacional.

Regras:

- não desenhar notch, Dynamic Island, barra Android ou outro chrome específico;
- App Bar, conteúdo e navegação da aplicação devem respeitar as safe areas;
- elementos persistentes da aplicação continuam consumindo espaço dentro do viewport;
- a representação gráfica final das safe areas será validada na prancha técnica-modelo.

## 3.3 Prancha técnica

**Canvas aprovado: `1024 × 1536 px`, orientação retrato.**

**Escala do viewport dentro da prancha: `1:1`.**

```text
1 px lógico do wireframe = 1 px na representação do viewport na prancha
```

A prancha deve conter:

- metadados técnicos;
- viewport `360 × 800 px`;
- wireframe;
- legenda cromática usada;
- legenda tipográfica usada;
- observações técnicas quando aplicáveis.

A composição conceitual da prancha está aprovada, porém **as coordenadas exatas das áreas documentais ainda dependem da aprovação da prancha técnica-modelo**.

---

# 4. Margens, grid e espaçamento

## 4.1 Margem estrutural

**Margem horizontal estrutural do conteúdo: `12 px`.**

A margem é aplicada dentro do viewport e deve ser respeitada como referência geral, salvo componente cuja geometria aprovada exija comportamento diferente.

## 4.2 Unidade de espaçamento

**Base técnica: `4 px`.**

Escala aprovada:

```text
4 px
8 px
12 px
16 px
24 px
32 px
```

Não devem ser utilizados espaçamentos arbitrários sem justificativa registrada.

## 4.3 Padding-base

```text
Horizontal: 16 px
Vertical:   12 px
```

O padding-base não substitui dimensões mínimas específicas de cada componente.

---

# 5. Convenção de arquivos e paginação

## 5.1 Formato oficial

```text
<ID>-<PÁGINA>-<TOTAL>_v<VERSÃO>.png
```

Os números de página e total devem utilizar dois dígitos quando aplicável.

Exemplos:

```text
white/T00-01-01_v01.png
black/T00-01-01_v01.png
white/T00-01-02_v01.png
white/T00-02-02_v01.png
```

Significado:

- `<ID>`: identificador funcional da interface;
- `<PÁGINA>`: página atual da sequência;
- `<TOTAL>`: quantidade total de páginas daquela representação;
- `<VERSÃO>`: versão do arquivo daquela página.

## 5.2 Regra multipágina

Quando a interface exceder o viewport:

- o viewport permanece `360 × 800 px`;
- o conteúdo não deve ser comprimido para caber artificialmente;
- devem ser criadas páginas sequenciais;
- elementos realmente persistentes da interface devem ser repetidos nas páginas em que permaneceriam visíveis durante a rolagem;
- conteúdo não persistente deve continuar a partir do ponto correspondente;
- não criar controle de paginação dentro da interface se a baseline não possuir tal controle;
- a paginação documental é externa à funcionalidade do produto.

## 5.3 Versionamento multipágina

Uma correção pode incrementar somente a página afetada, preservando as demais quando não mudarem.

Exemplo:

```text
T00-01-02_v01.png
T00-02-02_v02.png
```

Se uma alteração mudar o número total de páginas, a nova sequência deve utilizar o novo total de forma consistente nos arquivos afetados.

## 5.4 Aprovação multipágina

As páginas podem ser avaliadas individualmente, porém a interface somente recebe `APROVADO` quando:

```text
todas as páginas Claro = APROVADO
E
todas as páginas Escuro = APROVADO
```

---

# 6. Estados de controle documental

Estados permitidos:

```text
PENDENTE
EM VALIDAÇÃO
AJUSTES NECESSÁRIOS
APROVADO
```

Silêncio ou ausência de solicitação de ajuste não constitui aprovação.

Quando uma página/variante é aprovada:

```text
APROVADO → CONGELADO NESTA ETAPA
```

Um arquivo aprovado não pode ser sobrescrito, regenerado, alterado silenciosamente ou substituído por melhoria automática. Reabertura exige solicitação explícita e preservação da versão aprovada anterior.

---

# 7. Equivalência entre Claro e Escuro

Para uma mesma interface e página, as variantes devem possuir exatamente:

- informações;
- textos funcionais;
- campos;
- ações;
- destinos;
- hierarquia;
- agrupamentos;
- proporções;
- navegação;
- estados;
- ordem de leitura;
- componentes;
- tipografia técnica;
- paginação funcional equivalente.

A diferença permitida é a aplicação da paleta técnica correspondente.

---

# 8. Paletas técnicas do Wireframe

As cores abaixo pertencem exclusivamente a esta etapa e não constituem automaticamente a paleta definitiva do produto.

## 8.1 Claro — `white`

| Token | Aplicação | HEX |
|---|---|---|
| `WF-W-BG` | fundo geral | `#F4F4F4` |
| `WF-W-SURFACE` | superfícies principais / cards | `#FFFFFF` |
| `WF-W-SURFACE-ALT` | superfícies secundárias | `#EAEAEA` |
| `WF-W-BORDER` | bordas e divisores | `#B5B5B5` |
| `WF-W-TEXT` | texto principal | `#1A1A1A` |
| `WF-W-TEXT-2` | texto secundário | `#565656` |
| `WF-W-ACTION` | ações e elementos interativos | `#333333` |
| `WF-W-DISABLED` | estado desabilitado | `#9A9A9A` |
| `WF-W-FOCUS` | foco/seleção estrutural | `#4A4A4A` |
| `WF-W-STATUS` | indicador de status acompanhado de outro indicador | `#626262` |

## 8.2 Escuro — `black`

| Token | Aplicação | HEX |
|---|---|---|
| `WF-B-BG` | fundo geral | `#121212` |
| `WF-B-SURFACE` | superfícies principais / cards | `#1E1E1E` |
| `WF-B-SURFACE-ALT` | superfícies secundárias | `#2A2A2A` |
| `WF-B-BORDER` | bordas e divisores | `#5E5E5E` |
| `WF-B-TEXT` | texto principal | `#F2F2F2` |
| `WF-B-TEXT-2` | texto secundário | `#C2C2C2` |
| `WF-B-ACTION` | ações e elementos interativos | `#E0E0E0` |
| `WF-B-DISABLED` | estado desabilitado | `#777777` |
| `WF-B-FOCUS` | foco/seleção estrutural | `#D0D0D0` |
| `WF-B-STATUS` | indicador de status acompanhado de outro indicador | `#A8A8A8` |

## 8.3 Catalogação cromática

Cada prancha deve listar somente os tokens realmente utilizados. Cor nunca pode ser o único indicador de estado, erro, foco, seleção, sucesso ou indisponibilidade.

---

# 9. Tipografia técnica aprovada

A tipografia técnica desta etapa é deliberadamente separada da tipografia oficial da marca.

```text
WF-FONT-FAMILY: Inter
```

A família Inter é referência técnica de wireframe e **não se torna automaticamente a tipografia oficial do produto ou do futuro Design System**.

## 9.1 Escala tipográfica

| Token | Família | Peso | Tamanho | Line-height | Letter-spacing |
|---|---|---:|---:|---:|---|
| `WF-TITLE` | Inter | 600 / SemiBold | 20 px | 28 px | `normal` |
| `WF-SECTION` | Inter | 600 / SemiBold | 14 px | 20 px | `normal` |
| `WF-BODY` | Inter | 400 / Regular | 16 px | 24 px | `normal` |
| `WF-LABEL` | Inter | 500 / Medium | 14 px | 20 px | `normal` |
| `WF-ACTION-TEXT` | Inter | 500 / Medium | 16 px | 24 px | `normal` |
| `WF-CAPTION` | Inter | 400 / Regular | 12 px | 16 px | `normal` |

Claro e Escuro devem usar exatamente a mesma escala.

A especificação registrada na prancha é a fonte da verdade. Se a ferramenta raster não reproduzir a família com fidelidade perfeita, isso é limitação de renderização, não autorização para modificar o padrão.

---

# 10. Referência de componentes

Os componentes visíveis nos wireframes devem possuir geometria consistente porque servirão como referência para reconstrução posterior no Figma.

MUI / Material UI pode ser usado como **referência conceitual de componentes, estados e iconografia**, mas:

- não constitui escolha definitiva de framework;
- não constitui decisão de TypeScript;
- não cria dependência tecnológica;
- não antecipa a arquitetura definitiva.

## 10.1 App Bar

```text
Altura: 56 px
```

A App Bar deve respeitar a safe area superior e somente existir nas interfaces cuja estrutura funcional exigir cabeçalho.

## 10.2 Alvos interativos

```text
Touch target mínimo: 48 × 48 px
```

O ícone visível pode ser menor que o alvo interativo.

## 10.3 Campos

```text
Variante: Outlined
Altura: 56 px
Radius: 12 px
Borda: 1 px quando aplicável
Padding-base horizontal: 16 px
Padding-base vertical: 12 px
```

Campos devem possuir rótulo identificável e estados estruturais coerentes.

## 10.4 Botões

Categorias aprovadas:

```text
Primary
Secondary
Text
Icon Button
```

```text
Altura mínima de botão textual: 48 px
Touch target mínimo: 48 × 48 px
Radius: 12 px
```

A categoria deve refletir hierarquia funcional, não preferência estética.

## 10.5 Itens de lista e configuração

```text
Item simples: mínimo 56 px
Item com informação secundária/status: mínimo 64 px
```

A altura pode crescer quando o conteúdo funcional exigir.

## 10.6 Cards e superfícies agrupadas

```text
Radius: 16 px
Borda: 1 px quando necessária
```

Cards não devem ser introduzidos apenas por estética.

## 10.7 Modal / Dialog

```text
Margem lateral no viewport: 24 px
Radius: 16 px
```

## 10.8 Bottom Navigation

Quando prevista pela baseline:

```text
Altura: 64 px
```

A Bottom Navigation deve permanecer acima da safe area inferior e não pode ser adicionada a uma interface sem necessidade funcional documentada.

---

# 11. Bordas, divisores, radius e elevação

## 11.1 Bordas

```text
1 px quando necessária para delimitação estrutural
```

## 11.2 Divisores

```text
Espessura: 1 px
```

Devem respeitar o alinhamento do conteúdo e existir apenas quando houver separação semântica real.

## 11.3 Radius

```text
Campos: 12 px
Botões: 12 px
Cards: 16 px
Modais/Dialogs: 16 px
```

## 11.4 Elevação técnica

```text
WF-ELEVATION-0
offset-x: 0 px
offset-y: 0 px
blur: 0 px
opacidade: 0%

WF-ELEVATION-1
offset-x: 0 px
offset-y: 1 px
blur: 2 px
cor-base: preto neutro
opacidade: 12%

WF-ELEVATION-2
offset-x: 0 px
offset-y: 2 px
blur: 6 px
cor-base: preto neutro
opacidade: 16%

WF-ELEVATION-3
offset-x: 0 px
offset-y: 4 px
blur: 12 px
cor-base: preto neutro
opacidade: 20%
```

Uso de referência:

- E0: conteúdo integrado;
- E1: card destacado quando houver necessidade estrutural;
- E2: menu, dropdown ou elemento temporariamente sobreposto;
- E3: modal/dialog.

---

# 12. Iconografia técnica

Referência visual aprovada:

```text
Material Icons Outlined
```

Essa referência não obriga a implementação futura a utilizar MUI ou Material Icons.

```text
Ícone auxiliar: 20 px
Ícone de ação/navegação: 24 px
Touch target mínimo: 48 × 48 px
```

Ícones isolados somente devem ser utilizados para ações reconhecíveis e inequívocas. Quando houver ambiguidade, utilizar texto ou associação textual.

---

# 13. Estados de componentes

Estados previstos:

```text
default
focus
pressed / selected
disabled
error
hover
```

Regras:

- `hover` integra a especificação, mas não precisa ser apresentado nas pranchas mobile salvo necessidade específica;
- `focus`, `selected`, `disabled` e `error` não podem depender somente de cor;
- `error` deve possuir mensagem, rótulo, ícone ou outro marcador estrutural quando aplicável;
- estados inexistentes na baseline de uma interface não devem ser inventados para preencher a prancha.

---

# 14. Scroll e continuidade vertical

O viewport permanece sempre `360 × 800 px`.

Quando o conteúdo ultrapassar a altura disponível:

- utilizar rolagem vertical conceitual;
- não aumentar a altura do telefone;
- não reduzir tipografia, touch targets ou espaçamento para forçar o conteúdo a caber;
- representar a continuação por páginas documentais sequenciais;
- utilizar indicador vertical de rolagem somente quando necessário;
- o indicador deve existir dentro dos `360 × 800 px`;
- a geometria visual exata do indicador será validada na prancha técnica-modelo.

Apenas elementos realmente persistentes reaparecem em páginas subsequentes.

---

# 15. Regra para componentes ainda não catalogados

O catálogo acima não antecipa todos os componentes possíveis das 71 interfaces.

Se uma interface exigir componente ainda não especificado — por exemplo switch, radio, checkbox, chip, tabs, seletor de data ou outro controle — aplicar:

```text
componente necessário
        ↓
verificar requisito no Documento Mestre
        ↓
definir geometria e estados antes da primeira imagem que o utilize
        ↓
registrar neste README
        ↓
usar de forma consistente nas interfaces seguintes
```

É proibido introduzir componente visual novo silenciosamente.

---

# 16. Acessibilidade estrutural

Mesmo na etapa de wireframe:

- cor nunca pode ser o único indicador;
- touch target mínimo deve ser respeitado;
- ordem de leitura deve ser clara;
- campos devem possuir rótulos;
- erros devem permanecer próximos ao contexto;
- ações devem ser distinguíveis;
- foco e seleção devem possuir representação estrutural;
- hierarquia tipográfica deve ser consistente;
- componentes não devem ser compactados a ponto de prejudicar legibilidade ou operação.

A validação cromática definitiva de WCAG pertence à etapa de Design Visual, mas a estrutura desta etapa não pode impedir conformidade futura com WCAG 2.2 AA.

---

# 17. Conteúdo obrigatório de cada prancha

```text
Projeto: SaOr - Sales Order
Interface: <ID> — <Nome>
Baseline: v1.0
Etapa: Wireframe Conceitual em Imagem
Variação: Claro | Escuro
Status: EM VALIDAÇÃO | AJUSTES NECESSÁRIOS | APROVADO
Página: <XX>/<YY>
Versão do arquivo: vNN
Viewport lógico: 360 × 800 px
Orientação: Retrato
Canvas da prancha: 1024 × 1536 px
Escala do viewport: 1:1
Fonte técnica: Inter
```

Além dos metadados:

- legenda dos tokens cromáticos realmente usados;
- legenda dos tokens tipográficos realmente usados;
- observações técnicas necessárias;
- indicação de continuidade quando a interface possuir outras páginas.

---

# 18. Regra de produção por interface

Antes de produzir qualquer interface, consultar no `docs/Documento_Mestre.md`:

- ficha funcional de aceite;
- objetivo;
- informações exibidas;
- campos;
- campos obrigatórios;
- ações;
- destinos;
- Textframe;
- estados;
- comportamento de retorno;
- interfaces relacionadas;
- regras transversais aplicáveis.

É proibido:

- criar funcionalidade para preencher espaço;
- remover ação documentada;
- criar botão sem destino;
- criar menu, aba ou expansão sem comportamento documentado;
- fundir interfaces com IDs diferentes;
- transformar informação estática em interação;
- alterar o Textframe por conveniência visual;
- introduzir tecnologia definitiva;
- transformar wireframe em Design Visual final;
- introduzir componente não catalogado sem documentá-lo antes;
- alterar padrões aprovados por preferência de uma tela isolada.

---

# 19. Gate antes do primeiro wireframe funcional

## 19.1 Itens aprovados

```text
[x] viewport lógico: 360 × 800 px
[x] orientação: retrato
[x] safe area superior: 24 px
[x] safe area inferior: 32 px
[x] canvas da prancha: 1024 × 1536 px
[x] escala do viewport na prancha: 1:1
[x] margem estrutural horizontal: 12 px
[x] grid/espaçamento base: 4 px
[x] escala de espaçamento: 4 / 8 / 12 / 16 / 24 / 32 px
[x] padding-base: 16 px horizontal / 12 px vertical
[x] paleta técnica Claro
[x] paleta técnica Escuro
[x] família tipográfica: Inter
[x] pesos tipográficos
[x] tamanhos tipográficos
[x] line-heights
[x] letter-spacing: normal
[x] App Bar: 56 px
[x] touch target mínimo: 48 × 48 px
[x] campos Outlined: 56 px
[x] botões: Primary / Secondary / Text / Icon Button
[x] itens de lista: 56 / 64 px
[x] radius: 12 / 16 px
[x] bordas e divisores: 1 px
[x] elevação E0 / E1 / E2 / E3
[x] Material Icons Outlined como referência
[x] ícones: 20 / 24 px
[x] Bottom Navigation: 64 px quando aplicável
[x] modal: margem lateral 24 px
[x] estados de componente
[x] regra de scroll e paginação
[x] convenção multipágina e versionamento
[x] aprovação de interface multipágina
```

## 19.2 Pendente antes de T00

```text
[ ] prancha técnica-modelo produzida
[ ] coordenadas exatas do viewport dentro do canvas aprovadas
[ ] dimensões/posição do cabeçalho técnico aprovadas
[ ] posição da legenda cromática aprovada
[ ] posição da legenda tipográfica aprovada
[ ] posição da área de observações aprovada
[ ] representação gráfica das safe areas aprovada
[ ] representação gráfica do scroll/continuidade aprovada
[ ] composição final da prancha técnica aprovada
```

Enquanto esses itens permanecerem pendentes, `T00` não deve ser tratado como liberado para produção definitiva.

---

# 20. Fluxo operacional

```text
ESPECIFICAÇÃO TÉCNICA DOCUMENTADA
        ↓
PRANCHA TÉCNICA-MODELO
        ↓
EM VALIDAÇÃO
        ↓
aprovação explícita do modelo
        ↓
PADRÃO DA PRANCHA CONGELADO
        ↓
T00 Claro
        ↓
T00 Escuro
        ↓
EM VALIDAÇÃO
        ↓
ajustes, se necessários
        ↓
aprovação de todas as páginas Claro + Escuro
        ↓
T00 APROVADA / CONGELADA
        ↓
próxima interface
```

Por padrão, não avançar para a próxima interface antes da decisão sobre a interface atual, salvo orientação explícita.

---

# 21. Classificação de ocorrências

```text
A — baseline representável exatamente
B — ambiguidade de representação sem mudança funcional
C — contradição documental objetiva
D — requisito novo posterior à baseline
```

Tratamento:

- `A`: produzir normalmente;
- `B`: adotar representação conservadora e registrar;
- `C`: não alterar silenciosamente; apresentar a contradição;
- `D`: não modificar a baseline; registrar como evolução posterior possível.

---

# 22. Checklist mestre

**Estados:** `PENDENTE`, `EM VALIDAÇÃO`, `AJUSTES NECESSÁRIOS`, `APROVADO`.

A coluna de versão pode registrar uma única versão quando a interface tiver uma página ou uma síntese das versões quando houver múltiplas páginas.

| # | ID | Interface | Claro | Versão/Páginas | Escuro | Versão/Páginas | Interface |
|---:|---|---|---|---|---|---|---|
| 01 | `T00` | Configuração da aplicação | PENDENTE | — | PENDENTE | — | PENDENTE |
| 02 | `T00.1` | Configuração da API | PENDENTE | — | PENDENTE | — | PENDENTE |
| 03 | `T00.2` | Aparência / Tema | PENDENTE | — | PENDENTE | — | PENDENTE |
| 04 | `T00.3` | Diagnóstico de conexão | PENDENTE | — | PENDENTE | — | PENDENTE |
| 05 | `M00.4` | Confirmar alteração da API | PENDENTE | — | PENDENTE | — | PENDENTE |
| 06 | `M00.5` | Restaurar configuração | PENDENTE | — | PENDENTE | — | PENDENTE |
| 07 | `E00.6` | Testando conexão | PENDENTE | — | PENDENTE | — | PENDENTE |
| 08 | `E00.7` | Conexão realizada | PENDENTE | — | PENDENTE | — | PENDENTE |
| 09 | `E00.8` | Falha de conexão | PENDENTE | — | PENDENTE | — | PENDENTE |
| 10 | `E00.9` | API não configurada | PENDENTE | — | PENDENTE | — | PENDENTE |
| 11 | `E00.10` | API indisponível no login | PENDENTE | — | PENDENTE | — | PENDENTE |
| 12 | `T01` | Login | PENDENTE | — | PENDENTE | — | PENDENTE |
| 13 | `T01.1` | Recuperar senha | PENDENTE | — | PENDENTE | — | PENDENTE |
| 14 | `E01.2` | Login inválido | PENDENTE | — | PENDENTE | — | PENDENTE |
| 15 | `E01.3` | Sem conexão | PENDENTE | — | PENDENTE | — | PENDENTE |
| 16 | `E01.4` | Recuperação solicitada | PENDENTE | — | PENDENTE | — | PENDENTE |
| 17 | `E01.5` | Falha ao solicitar recuperação | PENDENTE | — | PENDENTE | — | PENDENTE |
| 18 | `T02` | Início / Dashboard | PENDENTE | — | PENDENTE | — | PENDENTE |
| 19 | `T02.1` | Notificações | PENDENTE | — | PENDENTE | — | PENDENTE |
| 20 | `T03` | Clientes e Prospects | PENDENTE | — | PENDENTE | — | PENDENTE |
| 21 | `M03.1` | Filtros de clientes | PENDENTE | — | PENDENTE | — | PENDENTE |
| 22 | `E03.2` | Busca sem resultado | PENDENTE | — | PENDENTE | — | PENDENTE |
| 23 | `T04` | Cliente — Resumo | PENDENTE | — | PENDENTE | — | PENDENTE |
| 24 | `T04.1` | Cliente — Pedidos | PENDENTE | — | PENDENTE | — | PENDENTE |
| 25 | `T04.2` | Cliente — Visitas | PENDENTE | — | PENDENTE | — | PENDENTE |
| 26 | `T04.3` | Cliente — Financeiro | PENDENTE | — | PENDENTE | — | PENDENTE |
| 27 | `T04.4` | Cliente — Endereço | PENDENTE | — | PENDENTE | — | PENDENTE |
| 28 | `T04.5` | Cliente — Dados cadastrais | PENDENTE | — | PENDENTE | — | PENDENTE |
| 29 | `T05` | Novo Prospect — Dados básicos | PENDENTE | — | PENDENTE | — | PENDENTE |
| 30 | `T05.1` | Novo Prospect — Endereço | PENDENTE | — | PENDENTE | — | PENDENTE |
| 31 | `T05.2` | Novo Prospect — Informações comerciais | PENDENTE | — | PENDENTE | — | PENDENTE |
| 32 | `T05.3` | Prospect — Resumo | PENDENTE | — | PENDENTE | — | PENDENTE |
| 33 | `T05.4` | Prospect — Histórico de visitas | PENDENTE | — | PENDENTE | — | PENDENTE |
| 34 | `T06` | Registrar visita | PENDENTE | — | PENDENTE | — | PENDENTE |
| 35 | `M06.1` | Finalizar visita | PENDENTE | — | PENDENTE | — | PENDENTE |
| 36 | `T06.2` | Detalhes da visita | PENDENTE | — | PENDENTE | — | PENDENTE |
| 37 | `E06.3` | Falha ao finalizar visita | PENDENTE | — | PENDENTE | — | PENDENTE |
| 38 | `T07` | Catálogo de produtos | PENDENTE | — | PENDENTE | — | PENDENTE |
| 39 | `M07.1` | Filtros de produtos | PENDENTE | — | PENDENTE | — | PENDENTE |
| 40 | `E07.2` | Produto não encontrado | PENDENTE | — | PENDENTE | — | PENDENTE |
| 41 | `T08` | Detalhes do produto | PENDENTE | — | PENDENTE | — | PENDENTE |
| 42 | `T09` | Pedido — Cliente | PENDENTE | — | PENDENTE | — | PENDENTE |
| 43 | `M09.1` | Selecionar cliente | PENDENTE | — | PENDENTE | — | PENDENTE |
| 44 | `T09.2` | Selecionar endereço | PENDENTE | — | PENDENTE | — | PENDENTE |
| 45 | `M09.3` | Selecionar tabela de preço | PENDENTE | — | PENDENTE | — | PENDENTE |
| 46 | `T10` | Pedido — Itens | PENDENTE | — | PENDENTE | — | PENDENTE |
| 47 | `M10.1` | Editar item | PENDENTE | — | PENDENTE | — | PENDENTE |
| 48 | `T11` | Pedido — Condições comerciais | PENDENTE | — | PENDENTE | — | PENDENTE |
| 49 | `T12` | Pedido — Revisão | PENDENTE | — | PENDENTE | — | PENDENTE |
| 50 | `M12.1` | Confirmar pedido | PENDENTE | — | PENDENTE | — | PENDENTE |
| 51 | `T13` | Pedido confirmado | PENDENTE | — | PENDENTE | — | PENDENTE |
| 52 | `T14` | Pedidos | PENDENTE | — | PENDENTE | — | PENDENTE |
| 53 | `M14.1` | Filtros de pedidos | PENDENTE | — | PENDENTE | — | PENDENTE |
| 54 | `T15` | Detalhes do pedido | PENDENTE | — | PENDENTE | — | PENDENTE |
| 55 | `T15.1` | Condições do pedido | PENDENTE | — | PENDENTE | — | PENDENTE |
| 56 | `T15.2` | Endereço de entrega | PENDENTE | — | PENDENTE | — | PENDENTE |
| 57 | `T16` | Agenda | PENDENTE | — | PENDENTE | — | PENDENTE |
| 58 | `T16.1` | Agendar visita | PENDENTE | — | PENDENTE | — | PENDENTE |
| 59 | `T16.2` | Compromisso / Visita | PENDENTE | — | PENDENTE | — | PENDENTE |
| 60 | `M16.3` | Confirmar cancelamento da visita | PENDENTE | — | PENDENTE | — | PENDENTE |
| 61 | `E16.4` | Falha ao cancelar visita | PENDENTE | — | PENDENTE | — | PENDENTE |
| 62 | `T17` | Mais | PENDENTE | — | PENDENTE | — | PENDENTE |
| 63 | `T17.1` | Meu perfil | PENDENTE | — | PENDENTE | — | PENDENTE |
| 64 | `T17.2` | Sincronização | PENDENTE | — | PENDENTE | — | PENDENTE |
| 65 | `T17.3` | Configurações | PENDENTE | — | PENDENTE | — | PENDENTE |
| 66 | `T17.4` | Ajuda | PENDENTE | — | PENDENTE | — | PENDENTE |
| 67 | `T17.5` | Sobre | PENDENTE | — | PENDENTE | — | PENDENTE |
| 68 | `M17.6` | Confirmar saída | PENDENTE | — | PENDENTE | — | PENDENTE |
| 69 | `E17.7` | Sincronização em andamento | PENDENTE | — | PENDENTE | — | PENDENTE |
| 70 | `E17.8` | Sincronização concluída | PENDENTE | — | PENDENTE | — | PENDENTE |
| 71 | `E17.9` | Falha na sincronização | PENDENTE | — | PENDENTE | — | PENDENTE |

---

# 23. Contadores

Estado inicial:

```text
Interfaces previstas:                    71
Mínimo de imagens Claro:                 71
Mínimo de imagens Escuro:                71
Mínimo total de imagens:                142

Total final de imagens:          VARIÁVEL POR PAGINAÇÃO

Páginas Claro aprovadas:                  0
Páginas Escuro aprovadas:                 0
Interfaces totalmente aprovadas:        0 / 71
```

O número final de imagens somente será conhecido conforme cada interface for paginada.

Nenhum contador de aprovação pode ser alterado sem aprovação explícita.

---

# 24. Registro de aprovação e reabertura

Modelo de aprovação de página:

```text
Data:
Interface:
Variação:
Página:
Arquivo:
Versão:
Status anterior:
Status novo: APROVADO
Observação:
```

Quando todas as páginas das duas variantes estiverem aprovadas:

```text
Interface <ID> = APROVADA / CONGELADA NA ETAPA DE WIREFRAME
```

Modelo de reabertura:

```text
Data:
Interface:
Variação:
Página:
Versão aprovada anterior:
Motivo da reabertura:
Solicitação explícita do responsável:
Nova versão iniciada:
```

---

# 25. Preservação documental

A autoridade documental permanece:

1. `docs/Documento_Mestre.md`;
2. `docs/Registro_Fechamento_Documento_Mestre.md`;
3. `README.md`;
4. este documento de controle da etapa.

Este documento:

- não altera a baseline funcional;
- não cria novos requisitos de negócio;
- não substitui o Documento Mestre;
- não define arquitetura definitiva;
- não transforma MUI em tecnologia oficial;
- não autoriza avanço para Design Visual;
- não autoriza Figma antes da etapa correspondente;
- não autoriza protótipo ou implementação;
- não pode marcar interface como aprovada sem declaração explícita do responsável.

A conclusão das imagens não libera automaticamente a etapa seguinte. A etapa de Wireframes somente será encerrada após aprovação formal.
