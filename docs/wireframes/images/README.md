# SaOr - Sales Order
## Controle da etapa — Wireframes Conceituais em Imagem

**Baseline funcional:** v1.0 — APROVADO / BASELINE FUNCIONAL  
**Etapa atual:** Wireframe Conceitual em Imagem  
**Status deste documento:** EM VALIDAÇÃO  
**Interfaces documentadas:** 71  
**Variações obrigatórias:** Claro (`white`) e Escuro (`black`)  
**Total de imagens previstas:** 142  
**Fonte funcional:** `docs/Documento_Mestre.md`  
**Registro de não regressão:** `docs/Registro_Fechamento_Documento_Mestre.md`

---

# 1. Finalidade

Este documento controla exclusivamente a produção, validação, aprovação e preservação dos wireframes conceituais em imagem do **SaOr - Sales Order**.

Cada interface `T`, `M` ou `E` da baseline funcional deve possuir duas imagens independentes:

- uma variação **Claro**, em `docs/wireframes/images/white`;
- uma variação **Escuro**, em `docs/wireframes/images/black`.

As duas imagens representam a mesma interface e devem ser estruturalmente idênticas. A existência das duas variantes nesta etapa tem a finalidade de permitir avaliar o comportamento estrutural da interface em ambiente claro e escuro, sem transformar o wireframe em Design Visual final.

---

# 2. Estrutura oficial

```text
docs/
└── wireframes/
    └── images/
        ├── README.md
        ├── white/
        │   ├── .gitkeep
        │   ├── T00_v01.png
        │   └── ...
        └── black/
            ├── .gitkeep
            ├── T00_v01.png
            └── ...
```

Os arquivos `.gitkeep` existem somente porque o Git não versiona diretórios vazios. Eles podem permanecer sem efeito funcional após a inclusão das imagens.

---

# 3. Referência dimensional

## 3.1 Viewport mobile oficial desta etapa

**Viewport lógico de referência: `390 × 844 px`**

O viewport foi definido como referência única para a produção inicial dos wireframes mobile.

Regras:

- orientação: retrato;
- largura lógica: 390 px;
- altura lógica: 844 px;
- a estrutura funcional da interface deve ser concebida dentro desse viewport;
- todas as interfaces partem da mesma referência dimensional;
- tablet e desktop não serão produzidos automaticamente nesta etapa;
- diferenças estruturais relevantes para tablet ou desktop devem ser registradas quando identificadas, sem criar versões adicionais sem autorização.

O viewport representa a área lógica da interface. Ele não é o tamanho total do arquivo de documentação.

## 3.2 Prancha técnica

**Canvas da prancha: `1024 × 1536 px`, orientação retrato.**

A prancha deve permitir exibir a interface na proporção correta e, fora do viewport, os metadados técnicos necessários à rastreabilidade.

A prancha deve conter obrigatoriamente:

- projeto;
- ID e nome da interface;
- baseline;
- etapa;
- variação Claro/Escuro;
- status;
- versão do arquivo;
- viewport lógico `390 × 844 px`;
- canvas da prancha `1024 × 1536 px`;
- wireframe da interface;
- legenda dos tokens cromáticos efetivamente utilizados;
- referência tipográfica efetivamente utilizada.

---

# 4. Convenção dos arquivos

Formato:

```text
<ID>_vNN.png
```

Exemplos:

```text
white/T00_v01.png
black/T00_v01.png
white/T00_v02.png
black/T00_v02.png
```

Regras:

- `v01` representa a primeira versão colocada em validação;
- qualquer ajuste gera uma nova versão somente para a variante afetada;
- versões anteriores não são apagadas durante a validação;
- o checklist deve indicar a versão atualmente aprovada;
- uma imagem já aprovada não poderá receber nova versão nesta etapa sem solicitação explícita do responsável pelo projeto.

---

# 5. Estados de controle

Estados permitidos para cada variante:

```text
PENDENTE
EM VALIDAÇÃO
AJUSTES NECESSÁRIOS
APROVADO
```

O estado geral da interface somente será `APROVADO` quando:

```text
Claro = APROVADO
E
Escuro = APROVADO
```

Silêncio ou ausência de solicitação de ajuste não constitui aprovação.

---

# 6. Congelamento após aprovação

Quando uma variante receber aprovação explícita:

```text
APROVADO → CONGELADO NESTA ETAPA
```

A partir desse momento, o arquivo aprovado:

- não poderá ser alterado;
- não poderá ser substituído;
- não poderá ser regenerado;
- não poderá receber melhorias automáticas;
- não poderá ser adaptado em consequência de mudanças feitas em outras interfaces.

A única exceção é uma solicitação explícita do responsável pelo projeto.

Caso uma interface aprovada seja reaberta, a versão aprovada anterior deve ser preservada e o motivo da reabertura registrado.

---

# 7. Equivalência obrigatória entre Claro e Escuro

As variantes `white` e `black` da mesma interface devem possuir exatamente:

- mesmas informações;
- mesmos textos funcionais;
- mesmos campos;
- mesmas ações;
- mesmos destinos;
- mesma hierarquia;
- mesmos agrupamentos;
- mesmas proporções;
- mesma navegação;
- mesmos estados;
- mesma ordem de leitura;
- mesmos componentes funcionais;
- mesma escala tipográfica técnica.

A única diferença permitida é a aplicação da paleta técnica correspondente à variante.

Uma variante não poderá possuir funcionalidade, ação, campo, estado ou hierarquia tipográfica diferente da outra.

---

# 8. Paletas técnicas do Wireframe

As cores abaixo pertencem exclusivamente à etapa de **Wireframe Conceitual em Imagem**. Elas não são automaticamente os tokens definitivos do Design Visual.

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
| `WF-W-STATUS` | indicador de status, sempre acompanhado de outro indicador | `#626262` |

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
| `WF-B-STATUS` | indicador de status, sempre acompanhado de outro indicador | `#A8A8A8` |

## 8.3 Catalogação cromática dentro de cada imagem

Cada prancha deve apresentar a legenda dos tokens realmente usados naquela interface.

A legenda deve permitir identificar, no mínimo quando existirem na tela:

- fundo;
- superfície principal;
- superfície secundária;
- borda/divisor;
- texto principal;
- texto secundário;
- ação/interação;
- desabilitado;
- foco/seleção;
- status.

Nenhum elemento visível deve receber uma cor arbitrária fora da paleta técnica sem que essa exceção seja registrada na própria prancha.

---

# 9. Tipografia técnica do Wireframe

A tipografia utilizada nos wireframes deve ser **catalogada com o mesmo rigor das cores**, porque fará parte da referência para reconstrução posterior no Figma.

A tipografia desta etapa é técnica e temporária. Ela **não constitui automaticamente a tipografia oficial do SaOr nem do futuro Design System**.

## 9.1 Família tipográfica técnica

```text
WF-FONT-FAMILY: A DEFINIR ANTES DA GERAÇÃO DO PRIMEIRO WIREFRAME
```

A família não deve ser escolhida ou inferida automaticamente.

Antes de gerar `T00_v01`, deve existir decisão explícita sobre a família tipográfica técnica utilizada nesta etapa. Depois de definida, a mesma família deve ser aplicada às 71 interfaces, salvo exceção explicitamente documentada.

## 9.2 Catálogo tipográfico obrigatório

A escala técnica deverá utilizar identificadores consistentes. A referência inicial é:

| Token | Finalidade estrutural |
|---|---|
| `WF-TITLE` | título principal da interface |
| `WF-SECTION` | título ou rótulo de agrupamento/seção |
| `WF-BODY` | conteúdo textual principal |
| `WF-LABEL` | rótulos de campos e controles |
| `WF-ACTION-TEXT` | texto de ações, botões ou itens navegáveis |
| `WF-CAPTION` | texto auxiliar, metadado ou informação secundária |

Para cada token efetivamente utilizado na imagem, a prancha deve registrar:

```text
Família
Peso
Tamanho em px
Line-height em px
Letter-spacing, quando diferente do padrão da família
```

Exemplo estrutural, sem definir valores nesta etapa:

```text
WF-BODY
Família: <família técnica aprovada>
Peso: <valor utilizado>
Tamanho: <valor utilizado> px
Line-height: <valor utilizado> px
Letter-spacing: <valor, se aplicável>
```

## 9.3 Regra de equivalência tipográfica

As variantes Claro e Escuro da mesma interface devem utilizar exatamente:

- mesma família;
- mesmos pesos;
- mesmos tamanhos;
- mesmos line-heights;
- mesmos letter-spacings;
- mesma hierarquia tipográfica.

A troca de tema não pode alterar a estrutura tipográfica.

## 9.4 Fonte da verdade tipográfica

Em uma imagem gerada, não se deve tentar identificar visualmente a fonte depois da geração.

A fonte da verdade é a **especificação registrada na prancha técnica**.

Se a ferramenta de geração não reproduzir visualmente a família com fidelidade suficiente, a prancha ainda deverá registrar a especificação correta; essa diferença deve ser considerada limitação do artefato raster e não autorização para alterar o padrão.

## 9.5 Relação futura com o Design System

Os tokens `WF-*` de tipografia servem como referência de transição.

Na etapa de Design Visual/Figma, eles poderão ser mapeados para tokens definitivos do Design System, mas não deverão ser promovidos automaticamente.

---

# 10. Acessibilidade estrutural

Mesmo nesta etapa:

- cor nunca pode ser o único indicador de estado;
- status deve possuir texto, ícone, forma ou rótulo adicional;
- ordem de leitura deve ser clara;
- campos devem possuir rótulos identificáveis;
- erros devem permanecer próximos ao contexto;
- controles interativos devem ser distinguíveis;
- a estrutura deve permitir alvos adequados;
- foco e seleção devem poder ser representados sem depender somente da cor;
- escala tipográfica deve preservar hierarquia, legibilidade e associação entre rótulos e controles.

A validação cromática e tipográfica definitiva de WCAG pertence à etapa de Design Visual. O wireframe, entretanto, não deve criar uma estrutura incompatível com WCAG 2.2 AA.

---

# 11. Conteúdo obrigatório de cada prancha

Cada arquivo deve apresentar:

```text
Projeto: SaOr - Sales Order
Interface: <ID> — <Nome>
Baseline: v1.0
Etapa: Wireframe Conceitual em Imagem
Variação: Claro | Escuro
Status: EM VALIDAÇÃO | AJUSTES NECESSÁRIOS | APROVADO
Versão: vNN
Viewport lógico: 390 × 844 px
Canvas da prancha: 1024 × 1536 px
Fonte técnica: <família aprovada>
```

Além desses dados, devem existir:

- legenda dos tokens cromáticos realmente utilizados;
- legenda dos tokens tipográficos realmente utilizados, com família, peso, tamanho e line-height.

---

# 12. Regra de produção

Antes de produzir qualquer interface, devem ser lidos no `docs/Documento_Mestre.md`:

- Ficha funcional de aceite;
- objetivo;
- informações exibidas;
- campos;
- campos obrigatórios;
- ações;
- destinos;
- Textframe;
- estados;
- comportamento de retorno;
- relações com outras interfaces;
- regras transversais aplicáveis.

A imagem deve ser uma tradução visual do conteúdo aprovado.

É proibido nesta etapa:

- criar funcionalidade para preencher espaço;
- remover ação documentada;
- criar botão sem destino;
- criar menu, aba ou expansão sem comportamento documentado;
- fundir interfaces com IDs diferentes;
- transformar informação estática em interação;
- alterar o Textframe por conveniência visual;
- introduzir arquitetura ou componentes de framework;
- transformar o wireframe em Design Visual final;
- escolher tipografia diferente por tela sem justificativa e autorização;
- promover a tipografia técnica do wireframe a tipografia oficial do produto sem a etapa correspondente.

---

# 13. Gate obrigatório antes do primeiro wireframe

Antes da geração de `T00_v01`, devem estar fechados e registrados neste documento:

```text
[x] viewport lógico: 390 × 844 px
[x] canvas da prancha: 1024 × 1536 px
[x] paleta técnica Claro
[x] paleta técnica Escuro
[ ] família tipográfica técnica do Wireframe
[ ] escala tipográfica técnica inicial
```

Enquanto os dois itens tipográficos permanecerem pendentes, nenhum wireframe deverá ser tratado como artefato definitivo de validação.

---

# 14. Fluxo por interface

```text
PENDENTE
   ↓
WHITE v01
   ↓
BLACK v01
   ↓
EM VALIDAÇÃO
   ↓
ajuste solicitado?
   ├── SIM → AJUSTES NECESSÁRIOS → nova versão afetada → EM VALIDAÇÃO
   └── NÃO
          ↓
aprovação explícita das duas variantes
          ↓
APROVADO
          ↓
CONGELADO NESTA ETAPA
```

Por padrão, a próxima interface somente deve ser iniciada depois da decisão de validação da interface atual, salvo orientação explícita em contrário.

---

# 15. Classificação de ocorrências

Durante a elaboração de uma interface:

```text
A — a baseline pode ser representada exatamente;
B — existe ambiguidade de representação sem mudança funcional;
C — existe contradição documental objetiva;
D — seria necessário requisito novo posterior à baseline.
```

Tratamento:

- `A`: produzir normalmente;
- `B`: adotar a representação mais conservadora e registrar;
- `C`: não alterar silenciosamente; apresentar a contradição;
- `D`: não modificar a baseline; registrar como evolução posterior possível.

---

# 16. Checklist mestre

**Estados possíveis:** `PENDENTE`, `EM VALIDAÇÃO`, `AJUSTES NECESSÁRIOS`, `APROVADO`.

| # | ID | Interface | Claro | Versão | Escuro | Versão | Interface |
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

# 17. Contadores

Estado inicial deste documento:

```text
Interfaces previstas:               71
Imagens Claro previstas:            71
Imagens Escuro previstas:           71
Total de imagens previstas:        142

Claro aprovado:                     0 / 71
Escuro aprovado:                    0 / 71
Interfaces totalmente aprovadas:   0 / 71
```

Os contadores somente podem ser alterados após aprovação explícita.

---

# 18. Registro de aprovação e reabertura

Modelo de aprovação:

```text
Data:
Interface:
Variação:
Arquivo:
Versão:
Status anterior:
Status novo: APROVADO
Observação:
```

Quando ambas as variantes forem aprovadas:

```text
Interface <ID> = APROVADA / CONGELADA NA ETAPA DE WIREFRAME
```

Modelo de reabertura:

```text
Data:
Interface:
Variação:
Versão aprovada anterior:
Motivo da reabertura:
Solicitação explícita do responsável:
Nova versão iniciada:
```

---

# 19. Preservação documental

A autoridade documental permanece:

1. `docs/Documento_Mestre.md`;
2. `docs/Registro_Fechamento_Documento_Mestre.md`;
3. `README.md`;
4. este documento de controle da etapa.

Este documento:

- não altera a baseline funcional;
- não cria novos requisitos funcionais;
- não substitui o Documento Mestre;
- não autoriza avanço para Design Visual;
- não autoriza Figma, protótipo ou implementação;
- não pode marcar uma interface como aprovada sem declaração explícita do responsável.

A conclusão das 142 imagens não libera automaticamente a etapa seguinte. A etapa completa de Wireframes somente será encerrada após aprovação formal do responsável pelo projeto.
