# SaOr - Sales Order
## Documento Mestre de UX, Telas e Navegação

**Versão:** 1.0  
**Status:** APROVADO / BASELINE FUNCIONAL  
**Etapa:** Documentação Mestre concluída / Baseline funcional aprovada  
**Projeto:** SaOr - Sales Order — Sistema de Pedido de Venda / Força de Vendas Externa

---

# 1. Finalidade deste documento

Este é o documento principal de definição funcional e visual do SaOr - Sales Order.

Ele será utilizado como referência para:

- definição das funcionalidades;
- definição das telas, subtelas, modais e estados;
- construção dos textframes;
- criação dos wireframes conceituais em imagem;
- criação do design visual de cada tela em imagem;
- construção estruturada das telas e componentes no Figma;
- criação do protótipo navegável no Figma;
- definição do fluxo de navegação;
- criação posterior dos slides de navegação e apresentação;
- construção de um MVP navegável em HTML, CSS e JavaScript para validação do layout e da navegação;
- elaboração posterior do Documento Técnico de Arquitetura;
- referência funcional para a implementação definitiva do frontend e backend;
- validação entre negócio, UX e desenvolvimento.

Este documento continuará sendo a fonte oficial das definições funcionais e visuais do projeto. As etapas posteriores deverão evoluir a partir dele, sem criar uma especificação funcional paralela.

Uma tela ou fluxo não deverá avançar para wireframe, design visual, Figma ou HTML sem antes estar documentado aqui.

## 1.1 Processo oficial de evolução

Cada interface deverá evoluir por etapas sequenciais, e **a validação será obrigatória em todas as etapas**.

```text
DOCUMENTO MESTRE / TEXTFRAME
          │
          ▼
VALIDAÇÃO FUNCIONAL OBRIGATÓRIA
          │
          ▼
WIREFRAME CONCEITUAL EM IMAGEM
          │
          ▼
VALIDAÇÃO DO WIREFRAME OBRIGATÓRIA
          │
          ▼
DESIGN VISUAL DA TELA EM IMAGEM
          │
          ▼
VALIDAÇÃO VISUAL + WCAG OBRIGATÓRIA
          │
          ▼
CONSTRUÇÃO NO FIGMA
          │
          ▼
VALIDAÇÃO DO FIGMA OBRIGATÓRIA
          │
          ▼
PROTÓTIPO NAVEGÁVEL NO FIGMA
          │
          ▼
VALIDAÇÃO DE FLUXOS E JORNADAS OBRIGATÓRIA
          │
          ▼
SLIDES DE NAVEGAÇÃO / APRESENTAÇÃO
          │
          ▼
VALIDAÇÃO DA APRESENTAÇÃO OBRIGATÓRIA
          │
          ▼
MVP HTML / CSS / JAVASCRIPT
          │
          ▼
VALIDAÇÃO FUNCIONAL + RESPONSIVA + ACESSIBILIDADE OBRIGATÓRIA
          │
          ▼
DOCUMENTO TÉCNICO DE ARQUITETURA
          │
          ▼
VALIDAÇÃO TÉCNICA OBRIGATÓRIA
          │
          ▼
DEFINIÇÃO DAS TECNOLOGIAS OFICIAIS
          │
          ▼
IMPLEMENTAÇÃO DEFINITIVA
```

O HTML não será utilizado para descobrir o layout. Quando o MVP HTML for iniciado, o layout, os estados principais, a identidade visual e a navegação já deverão ter sido definidos e validados nas etapas anteriores.

A linguagem oficial do backend, framework, banco de dados, contrato definitivo da API, segurança, infraestrutura e demais decisões de arquitetura serão especificados somente no Documento Técnico, depois da validação do MVP HTML.

## 1.2 Regra de validação e aprovação

Nenhuma etapa poderá ser considerada concluída e nenhuma etapa seguinte poderá ser iniciada sem a validação da entrega atual.

Cada entrega utilizará um dos seguintes estados de controle:

```text
PENDENTE
   ↓
EM VALIDAÇÃO
   ↓
┌───────────────────────┐
│                       │
▼                       ▼
AJUSTES NECESSÁRIOS   APROVADO
│
└── volta para a etapa correspondente
```

Somente o estado **APROVADO** libera a etapa seguinte.

A validação deverá verificar o objeto específico de cada fase:

| Etapa | Validação obrigatória |
|---|---|
| Documento / Textframe | conteúdo, campos, ações, destinos, regras e completude funcional |
| Wireframe | hierarquia, disposição, agrupamento, proporções e navegação estrutural |
| Design visual | identidade, legibilidade, consistência, temas e acessibilidade WCAG |
| Figma | fidelidade ao design aprovado, componentes, variantes, tokens e estados |
| Protótipo | navegação, jornadas, retornos, modais e continuidade dos fluxos |
| Slides | coerência da apresentação e representação correta dos fluxos aprovados |
| MVP HTML | comportamento, responsividade, navegação, acessibilidade e aderência ao Figma |
| Documento Técnico | arquitetura, segurança, integrações, contratos e viabilidade técnica |

## 1.3 Consolidações desta revisão — versão 1.0

Esta revisão formaliza:

- a definição de **Prospect** e **Cliente** como classificações do mesmo Cadastro Comercial;
- a regra de conversão de Prospect em Cliente após aprovação cadastral;
- a separação entre classificação comercial e situação operacional;
- a regra de emissão de pedido somente para **Cliente + Ativo**;
- a paleta cromática inicial oficial dos temas Claro e Escuro com valores HEX;
- WCAG 2.2 nível AA como mínimo obrigatório e AAA como objetivo padrão;
- a proibição de utilizar cor como único meio de transmitir informação;
- validação obrigatória em todas as etapas do processo de construção;
- fechamento dos destinos e comportamentos de ações anteriormente implícitas;
- suporte ao usuário por WhatsApp;
- estados explícitos de recuperação de senha, finalização de visita, cancelamento de visita e sincronização;
- critérios funcionais de acesso à configuração da API;
- consolidação do documento como baseline funcional aprovada;
- normalização das 71 interfaces com Ficha funcional de aceite;
- fechamento explícito dos comportamentos de tentativa de login, filtros de clientes e consulta de CEP;
- definição dos comportamentos dos componentes de seleção sem criação de rotas artificiais;
- remoção de conceito técnico de implementação que não pertence à Documentação Mestre.
- correção semântica da classificação entre estados de processamento, sucesso, erro e resultado vazio nas Fichas funcionais;
- alinhamento dos filtros de clientes entre lista de campos e textframe;
- explicitação determinística da obrigatoriedade de campos nas Fichas restantes;
- consolidação do ciclo completo de sincronização T17.2 → E17.7 → E17.8/E17.9.
- aplicação explícita da elegibilidade `CLIENTE + ATIVO` em todos os pontos de entrada de pedido;
- fechamento do modo de edição das informações comerciais do Prospect em T05.2;
- definição do contexto do catálogo/produto exclusivamente dentro do pedido em edição nesta baseline;
- definição funcional dos estados globais de sessão expirada e acesso não autorizado;
- preservação de dados pendentes diante de falha, rejeição ou conflito de sincronização.

---

# 2. Regra de completude do documento

A partir desta versão, será utilizada a seguinte regra:

> Nenhum botão, link, aba, item com seta `>`, ação de menu, filtro, etapa de wizard ou campo que abra outra interface poderá existir sem que seu destino esteja documentado.

Os destinos serão classificados como:

| Prefixo | Tipo |
|---|---|
| T | Tela completa |
| M | Modal, Dialog ou Bottom Sheet |
| E | Estado alternativo de uma tela |
| C | Componente reutilizável |

Exemplo:

```text
Endereço de entrega              >
                                  │
                                  └──── T09.2 Selecionar endereço
```

Portanto, não haverá mais indicação de uma funcionalidade sem seu respectivo textframe.

---

# 3. Referência do Figma

O projeto de referência apresentado utiliza conceitos que deverão ser preservados como inspiração arquitetural:

- barra superior de aplicação;
- áreas bem definidas de dados;
- componentes reutilizáveis de formulário;
- diálogos para edição ou seleção de informações;
- tabelas/listas estruturadas;
- ações principais bem posicionadas;
- rodapé de ações;
- separação entre contexto principal e edição complementar.

No SaOr esses princípios serão adaptados para uma experiência prioritariamente voltada ao vendedor em campo.

---

# 4. Contexto do produto

O SaOr - Sales Order será utilizado principalmente por vendedores externos.

O **Pedido de Venda é o núcleo transacional do projeto**, e o SaOr - Sales Order contemplará os módulos de apoio necessários ao trabalho do vendedor em campo, incluindo clientes, prospects, visitas, agenda, produtos, informações comerciais, sincronização e demais funções definidas neste Documento Mestre.

Esses módulos fazem parte do escopo do produto e não deverão ser removidos sem decisão explícita registrada neste documento.

O vendedor poderá visitar um cliente existente ou prospectar um novo estabelecimento.

Durante sua rotina deverá conseguir:

- consultar sua carteira;
- localizar clientes;
- cadastrar prospects;
- consultar informações comerciais;
- consultar informações financeiras permitidas;
- registrar visitas;
- agendar retornos;
- consultar produtos;
- verificar preços;
- montar pedidos;
- escolher condições comerciais;
- revisar pedidos;
- transmitir pedidos;
- acompanhar pedidos anteriores;
- consultar sua agenda.

## 4.1 Cadastro Comercial, Prospect e Cliente

Para evitar duplicidade de registros e perda de histórico, **Prospect e Cliente serão classificações comerciais do mesmo Cadastro Comercial**.

### Cadastro Comercial

Representa a pessoa ou empresa acompanhada pelo SaOr. O mesmo cadastro preservará seus dados, contatos, endereços, informações comerciais, visitas e histórico ao longo de sua evolução comercial.

### Prospect

> **Prospect** é um novo Cadastro Comercial identificado, prospectado ou contatado pelo vendedor e que ainda não teve seu cadastro aprovado.

No fluxo atual, um novo cadastro criado pelo vendedor como resultado de prospecção terá:

```text
Classificação comercial = PROSPECT
Situação operacional    = BLOQUEADO
```

Enquanto permanecer como Prospect, **não poderá emitir Pedido de Venda**.

### Cliente

> **Cliente** é o Cadastro Comercial cujo cadastro foi aprovado.

Quando o cadastro do Prospect for aprovado, o mesmo registro será convertido para:

```text
Classificação comercial = CLIENTE
Situação operacional    = ATIVO
```

A aprovação não cria um novo registro. Dados, endereços, informações comerciais, visitas e histórico deverão ser preservados.

### Cliente bloqueado ou inativo

Depois de convertido em Cliente, o cadastro poderá posteriormente ser bloqueado ou inativado por motivo interno sem retornar à classificação Prospect.

Exemplos válidos:

```text
CLIENTE + ATIVO      → pode emitir pedido
CLIENTE + BLOQUEADO  → não pode emitir pedido
CLIENTE + INATIVO    → não pode emitir pedido
PROSPECT + BLOQUEADO → não pode emitir pedido
```

A combinação **PROSPECT + ATIVO** não faz parte da regra de negócio atual.

### Regra para emissão de pedido

Um Pedido de Venda somente poderá ser iniciado ou confirmado quando as duas condições abaixo forem verdadeiras:

```text
Classificação comercial = CLIENTE
            E
Situação operacional    = ATIVO
```

Caso uma dessas condições não seja atendida, a interface deverá impedir a emissão do pedido e apresentar uma mensagem textual explicando a restrição. A cor nunca será o único indicador do bloqueio.

Esta regra é transversal e vale para **todos os pontos de entrada do Pedido de Venda**. Quando o fluxo iniciar sem Cliente pré-selecionado, T09 poderá ser aberta para seleção, mas somente permitirá avanço com `CLIENTE + ATIVO`. Quando uma ação partir de um Cadastro Comercial já conhecido, como T04/T04.1 ou T06, a ação de iniciar pedido deverá permanecer indisponível se o cadastro não for `CLIENTE + ATIVO`, com explicação textual do motivo.

### Aprovação cadastral

A aprovação cadastral é **externa ao escopo funcional do vendedor no SaOr nesta baseline**. O SaOr deverá receber o resultado da aprovação por processo autorizado externo ao fluxo aqui documentado e, a partir desse resultado, aplicar a transição funcional definida abaixo.

Este Documento Mestre não define quem aprova, por qual ferramenta administrativa a aprovação é realizada nem o mecanismo técnico de integração. Esses pontos pertencem a escopos posteriores e **não constituem pendência da Documentação Mestre**, porque o comportamento do SaOr antes e depois do resultado da aprovação já está definido.

O Documento Mestre registra a seguinte regra de negócio:

```text
PROSPECT + BLOQUEADO
        │
        │ cadastro aprovado
        ▼
CLIENTE + ATIVO
        │
        ├── pode permanecer ATIVO
        ├── pode ser BLOQUEADO posteriormente
        └── pode ser INATIVO posteriormente
```

---

# 5. Plataforma de referência

O projeto deverá ser concebido como aplicação responsiva.

## Prioridade operacional

```text
1. Smartphone
2. Tablet
3. Desktop
```

O vendedor normalmente estará:

- em pé;
- dentro de um estabelecimento;
- conversando com o cliente;
- usando uma mão;
- alternando rapidamente entre cliente, produto e pedido.

Por isso, a versão mobile será usada como referência para os primeiros textframes, wireframes e designs.

Antes da implementação definitiva, será construído um MVP em HTML, CSS e JavaScript para validar layout, responsividade e navegação.

A arquitetura definitiva do frontend, a linguagem oficial do backend e os respectivos frameworks serão formalizados somente no Documento Técnico, após a validação do MVP HTML.

---

# 6. Usuário principal

## Vendedor

Responsabilidades:

- administrar sua carteira;
- realizar visitas;
- prospectar;
- negociar;
- vender;
- registrar informações;
- acompanhar seus pedidos.

Perfis administrativos, supervisores e gerentes serão tratados posteriormente.

---

# 7. Navegação principal

A navegação inferior será composta inicialmente por:

```text
┌────────────────────────────────────┐
│                                    │
│            CONTEÚDO                │
│                                    │
│────────────────────────────────────│
│ Início │ Clientes │ + │ Pedidos │⋯ │
└────────────────────────────────────┘
```

Onde:

| Item | Destino |
|---|---|
| Início | T02 |
| Clientes | T03 |
| + | T09 |
| Pedidos | T14 |
| Mais | T17 |

O botão central `+` representa a ação principal de iniciar uma venda.

---

# 8. Inventário mestre

## Configuração inicial e aplicação

| ID | Interface |
|---|---|
| T00 | Configuração da aplicação |
| T00.1 | Configuração da API |
| T00.2 | Aparência / Tema |
| T00.3 | Diagnóstico de conexão |
| M00.4 | Confirmar alteração da API |
| M00.5 | Restaurar configuração |
| E00.6 | Testando conexão |
| E00.7 | Conexão realizada |
| E00.8 | Falha de conexão |
| E00.9 | API não configurada |
| E00.10 | API indisponível no login |

## Autenticação

| ID | Interface |
|---|---|
| T01 | Login |
| T01.1 | Recuperar senha |
| E01.2 | Login inválido |
| E01.3 | Sem conexão |
| E01.4 | Recuperação solicitada |
| E01.5 | Falha ao solicitar recuperação |

## Operação

| ID | Interface |
|---|---|
| T02 | Início / Dashboard |
| T02.1 | Notificações |

## Clientes

| ID | Interface |
|---|---|
| T03 | Clientes e Prospects |
| M03.1 | Filtros de clientes |
| E03.2 | Busca sem resultado |
| T04 | Cliente — Resumo |
| T04.1 | Cliente — Pedidos |
| T04.2 | Cliente — Visitas |
| T04.3 | Cliente — Financeiro |
| T04.4 | Cliente — Endereço |
| T04.5 | Cliente — Dados cadastrais |

## Prospects

| ID | Interface |
|---|---|
| T05 | Novo Prospect — Dados básicos |
| T05.1 | Novo Prospect — Endereço |
| T05.2 | Novo Prospect — Informações comerciais |
| T05.3 | Prospect — Resumo |
| T05.4 | Prospect — Histórico de visitas |

## Visitas

| ID | Interface |
|---|---|
| T06 | Registrar visita |
| M06.1 | Finalizar visita |
| T06.2 | Detalhes da visita |
| E06.3 | Falha ao finalizar visita |

## Produtos

| ID | Interface |
|---|---|
| T07 | Catálogo de produtos |
| M07.1 | Filtros de produtos |
| E07.2 | Produto não encontrado |
| T08 | Detalhes do produto |

## Pedido de Venda

| ID | Interface |
|---|---|
| T09 | Pedido — Cliente |
| M09.1 | Selecionar cliente |
| T09.2 | Selecionar endereço |
| M09.3 | Selecionar tabela de preço |
| T10 | Pedido — Itens |
| M10.1 | Editar item |
| T11 | Pedido — Condições comerciais |
| T12 | Pedido — Revisão |
| M12.1 | Confirmar pedido |
| T13 | Pedido confirmado |

## Consulta de pedidos

| ID | Interface |
|---|---|
| T14 | Pedidos |
| M14.1 | Filtros de pedidos |
| T15 | Detalhes do pedido |
| T15.1 | Condições do pedido |
| T15.2 | Endereço de entrega |

## Agenda

| ID | Interface |
|---|---|
| T16 | Agenda |
| T16.1 | Agendar visita |
| T16.2 | Compromisso / Visita |
| M16.3 | Confirmar cancelamento da visita |
| E16.4 | Falha ao cancelar visita |

## Configurações

| ID | Interface |
|---|---|
| T17 | Mais |
| T17.1 | Meu perfil |
| T17.2 | Sincronização |
| T17.3 | Configurações |
| T17.4 | Ajuda |
| T17.5 | Sobre |
| M17.6 | Confirmar saída |
| E17.7 | Sincronização em andamento |
| E17.8 | Sincronização concluída |
| E17.9 | Falha na sincronização |

---

# 9. Fluxo macro

```text
INICIALIZAÇÃO
 │
 ▼
Carregar configurações locais
 │
 ├── API não configurada
 │      │
 │      ▼
 │    E00.9
 │      │
 │      ▼
 │    T00.1 Configuração da API
 │
 └── API configurada
        │
        ▼
      T01 LOGIN
        │
        ├── ⚙ Configurações → T00
        │
        ▼
      T02 INÍCIO
        │
        ├──────────────────────────────────────┐
        │                                      │
        ▼                                      ▼
      T03 CLIENTES                         T14 PEDIDOS
        │                                      │
        ├── T04 CLIENTE                        └── T15 PEDIDO
        │     │
        │     ├── T04.1 Pedidos
        │     ├── T04.2 Visitas
        │     ├── T04.3 Financeiro
        │     ├── T04.4 Endereço
        │     ├── T04.5 Cadastro
        │     ├── T06 Registrar visita
        │     └── T09 Novo pedido
        │
        └── T05 NOVO PROSPECT
              │
              ├── T05 Dados básicos
              ├── T05.1 Endereço
              ├── T05.2 Comercial
              └── T05.3 Resumo

NOVO PEDIDO

T09 Cliente
 │
 ▼
T10 Itens
 │
 ▼
T11 Condições
 │
 ▼
T12 Revisão
 │
 ▼
M12.1 Confirmação
 │
 ▼
T13 Pedido confirmado
```

---

# 9.1 CONFIGURAÇÃO INICIAL E APLICAÇÃO

A configuração da aplicação é transversal e deverá estar acessível antes e depois da autenticação, respeitando as regras de autorização abaixo.

Antes do login, sua finalidade principal será permitir a configuração inicial da API quando ainda não existir servidor configurado. Depois do login, as configurações poderão ser acessadas pela área **Mais / Configurações**.

### Regra de acesso à configuração da API

- quando nenhuma API estiver configurada, a configuração inicial poderá ser realizada antes do login;
- quando a API já estiver configurada, qualquer alteração de URL ou credencial deverá exigir autorização específica para **Alterar configuração da API**;
- sem essa autorização, T00.1 permanecerá disponível apenas para consulta do endereço configurado, status e teste de conexão;
- após uma alteração autorizada da API, a aplicação deverá invalidar a sessão atual e retornar para **T01 — Login** após salvar a nova configuração;
- o mecanismo técnico utilizado para conceder e validar essa autorização será definido no Documento Técnico, sem alterar este comportamento funcional.

## T00 — Configuração da aplicação

### Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T00` |
| Nome | Configuração da aplicação |
| Objetivo | Centralizar as configurações técnicas e visuais disponíveis na aplicação. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — tela de navegação entre configurações. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T00.1, T00.2, T00.3, M00.5. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Retorna à interface de origem; antes do login, normalmente T01/E00.9; após login, T17.3. |
| Relação com outras interfaces | T01, E00.9, T17.3, T00.1, T00.2, T00.3, M00.5 |

### Objetivo

Centralizar configurações técnicas e visuais da aplicação.

### Destinos

| Item | Destino |
|---|---|
| API de acesso | T00.1 |
| Tema | T00.2 |
| Diagnóstico | T00.3 |
| Restaurar configuração | M00.5 |

### Textframe

```text
┌────────────────────────────────────┐
│ ‹        Configurações             │
│                                    │
│ CONEXÃO                            │
│                                    │
│ API de acesso                  >   │
│ ● Conectada                        │
│────────────────────────────────────│
│                                    │
│ APARÊNCIA                          │
│                                    │
│ Tema                           >   │
│ Claro / Escuro                     │
│────────────────────────────────────│
│                                    │
│ SISTEMA                            │
│                                    │
│ Diagnóstico                    >   │
│                                    │
│ Versão                             │
│ 1.0.0                              │
│                                    │
│ Restaurar configuração         >   │
└────────────────────────────────────┘
```

---

## T00.1 — Configuração da API

### Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T00.1` |
| Nome | Configuração da API |
| Objetivo | Configurar, testar e salvar a API utilizada pelo SaOr, respeitando as regras de autorização. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | URL da API; credencial de acesso quando exigida pelo contrato. |
| Campos obrigatórios | URL da API é obrigatória; credencial depende do contrato da API. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: E00.6, E00.7, E00.8, T01, M00.4. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | E00.8 — Falha de conexão. E00.6 representa processamento e E00.7 representa sucesso; estados globais aplicam-se quando pertinentes. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Volta à interface de origem sem salvar alterações não confirmadas; alteração autorizada salva e retorna a T01 conforme regra. |
| Relação com outras interfaces | E00.6, E00.7, E00.8, T01, M00.4 |

### Objetivo

Permitir definir a API utilizada pela aplicação e testar a conectividade antes de salvar a configuração.

### Campos previstos nesta etapa

| Campo | Obrigatório | Observação |
|---|---:|---|
| URL da API | Sim | Endereço base do serviço |
| Credencial de acesso | Conforme contrato | Campo protegido quando aplicável |

Os demais parâmetros dependerão do contrato definitivo da API e serão formalizados no Documento Técnico.

### Textframe

```text
┌────────────────────────────────────┐
│ ‹       Configuração da API        │
│                                    │
│ URL da API *                       │
│ ┌────────────────────────────────┐ │
│ │ https://api.exemplo.com.br     │ │
│ └────────────────────────────────┘ │
│                                    │
│ Credencial de acesso               │
│ ┌────────────────────────────────┐ │
│ │ •••••••••••••••••••       👁 │ │
│ └────────────────────────────────┘ │
│                                    │
│ [        TESTAR CONEXÃO        ]   │
│                                    │
│ Status                             │
│ ● Conectado                        │
│                                    │
│ [             SALVAR           ]   │
└────────────────────────────────────┘
```

### Ações

| Ação | Destino / comportamento |
|---|---|
| Testar conexão | E00.6; sucesso → E00.7; falha → E00.8 |
| Salvar configuração inicial | Persiste a configuração validada e segue para T01 |
| Salvar alteração de configuração existente | M00.4 |
| Voltar | Retorna à interface de origem sem salvar alterações não confirmadas |

### Regras

- credenciais não deverão ser exibidas abertas por padrão;
- valores sensíveis não deverão aparecer em mensagens de erro, logs ou telas de diagnóstico;
- uma alteração de servidor deverá solicitar confirmação em **M00.4**;
- após confirmar e salvar uma alteração de servidor, a sessão atual deverá ser encerrada e o fluxo retornará para **T01**;
- usuários sem autorização para alterar a API poderão apenas consultar a configuração e executar o teste de conexão;
- o formato definitivo de autenticação será definido posteriormente no Documento Técnico.

---

## T00.2 — Aparência / Tema

### Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T00.2` |
| Nome | Aparência / Tema |
| Objetivo | Selecionar, pré-visualizar e aplicar o tema Claro ou Escuro. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Seleção de tema: Claro ou Escuro. |
| Campos obrigatórios | Uma opção de tema deve permanecer selecionada: Claro ou Escuro. |
| Ações e destinos | Selecionar Claro/Escuro atualiza apenas a prévia; `APLICAR TEMA` persiste a escolha e retorna à origem. O `NOVO PEDIDO` exibido na prévia é somente ilustrativo. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Após aplicar, retorna à interface de origem com o tema aplicado. |
| Relação com outras interfaces | T00 |

### Objetivo

Permitir escolher entre os temas **Claro** e **Escuro**.

### Ações

- `APLICAR TEMA` persiste a preferência e retorna para a interface de origem com o novo tema já aplicado;
- alternar entre Claro e Escuro atualiza a pré-visualização sem alterar a preferência salva até a confirmação.

### Regras

- o tema selecionado deverá ser persistido localmente;
- o tema deverá ser aplicado antes da renderização da tela de login para evitar troca visual após o carregamento;
- a estrutura e as funcionalidades deverão permanecer idênticas nos dois temas;
- somente os tokens visuais serão alterados;
- o conteúdo dentro da área **Pré-visualização** é exclusivamente demonstrativo; controles representados nessa miniatura, inclusive `NOVO PEDIDO`, **não são interativos e não iniciam navegação**.

### Textframe

```text
┌────────────────────────────────────┐
│ ‹           Aparência              │
│                                    │
│ Tema                               │
│                                    │
│ ┌──────────────┐ ┌──────────────┐ │
│ │              │ │              │ │
│ │    CLARO     │ │    ESCURO    │ │
│ │              │ │              │ │
│ │      ●       │ │      ○       │ │
│ └──────────────┘ └──────────────┘ │
│                                    │
│ Pré-visualização                   │
│                                    │
│ ┌────────────────────────────────┐ │
│ │ SaOr                           │ │
│ │                                │ │
│ │ Olá, Carlos                    │ │
│ │                                │ │
│ │ ┌────────────┐ ┌────────────┐ │ │
│ │ │ R$ 8.450   │ │ 6 pedidos  │ │ │
│ │ └────────────┘ └────────────┘ │ │
│ │                                │ │
│ │ [      NOVO PEDIDO       ]     │ │
│ └────────────────────────────────┘ │
│                                    │
│ [          APLICAR TEMA        ]   │
└────────────────────────────────────┘
```

---

## T00.3 — Diagnóstico de conexão

### Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T00.3` |
| Nome | Diagnóstico de conexão |
| Objetivo | Diagnosticar conectividade de internet, API, autenticação e sincronização. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — diagnóstico e ação de repetição de teste. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | `TESTAR NOVAMENTE` repete o diagnóstico na própria T00.3; não cria nova rota. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Retorna à interface de origem; repetir teste permanece na própria tela. |
| Relação com outras interfaces | T00 |

### Objetivo

Permitir diferenciar problemas de internet, API, autenticação e sincronização.

### Ações

- `TESTAR NOVAMENTE` repete os testes e atualiza os resultados na própria T00.3;
- a tela deverá identificar textualmente qual verificação falhou, sem depender apenas de cor.

### Textframe

```text
┌────────────────────────────────────┐
│ ‹          Diagnóstico             │
│                                    │
│ Internet                           │
│ ● Disponível                       │
│                                    │
│ API                                │
│ ● Disponível                       │
│                                    │
│ Autenticação                       │
│ ● Serviço disponível               │
│                                    │
│ Última sincronização               │
│ Hoje • 14:25                       │
│                                    │
│ Pedidos pendentes                  │
│ 0                                  │
│                                    │
│ Aplicativo                         │
│ Versão 1.0.0                       │
│                                    │
│ [       TESTAR NOVAMENTE       ]   │
└────────────────────────────────────┘
```

---

## M00.4 — Confirmar alteração da API

### Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `M00.4` |
| Nome | Confirmar alteração da API |
| Objetivo | Confirmar uma alteração da configuração da API antes de aplicá-la. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — confirmação binária da alteração. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T00.1, T01. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Cancelar/fechar retorna à interface que abriu o modal, preservando o contexto anterior. |
| Relação com outras interfaces | T00.1, T01 |

```text
┌────────────────────────────────────┐
│      Alterar servidor da API?      │
│                                    │
│ Você está alterando o servidor     │
│ utilizado pelo aplicativo.         │
│                                    │
│ A sessão atual poderá precisar     │
│ ser encerrada e os dados locais    │
│ poderão precisar ser sincronizados │
│ novamente.                         │
│                                    │
│ [ CANCELAR ]       [ ALTERAR ]     │
└────────────────────────────────────┘
```

Cancelar → **T00.1**, preservando a configuração atual.  
Alterar → salva a nova configuração, encerra a sessão quando houver usuário autenticado e segue para **T01**.

---

## M00.5 — Restaurar configuração

### Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `M00.5` |
| Nome | Restaurar configuração |
| Objetivo | Confirmar a restauração das configurações locais da aplicação. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — confirmação binária da restauração. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T00, E00.9. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Não há estado de erro específico deste modal nesta baseline. E00.9 representa o estado funcional resultante quando a API deixa de estar configurada após a restauração. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Cancelar/fechar retorna à interface que abriu o modal, preservando o contexto anterior. |
| Relação com outras interfaces | T00, E00.9 |

```text
┌────────────────────────────────────┐
│    Restaurar configurações?        │
│                                    │
│ Serão restauradas as configurações │
│ locais do aplicativo.              │
│                                    │
│ Isso poderá remover:               │
│                                    │
│ • configuração da API              │
│ • preferência de tema              │
│ • preferências locais              │
│                                    │
│ Dados operacionais não deverão ser │
│ apagados sem confirmação própria.  │
│                                    │
│ [ CANCELAR ]       [ RESTAURAR ]   │
└────────────────────────────────────┘
```

Cancelar → retorna para **T00** sem alterações.  
Restaurar → remove preferências locais restauráveis; se a API for removida, segue para **E00.9**. Dados operacionais somente poderão ser removidos por fluxo próprio e confirmação específica.

---

## E00.6 — Testando conexão

### Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `E00.6` |
| Nome | Testando conexão |
| Objetivo | Representar o estado de teste de conectividade em andamento. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — estado transitório. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: E00.7, E00.8. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Este registro é um estado específico; aplica também as regras globais de acessibilidade, retorno e mensagens. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Segue as ações de recuperação documentadas neste estado ou retorna automaticamente à interface-base quando a condição for resolvida. |
| Relação com outras interfaces | E00.7, E00.8 |

```text
┌────────────────────────────────────┐
│                                    │
│               ◌                    │
│                                    │
│        Testando conexão...         │
│                                    │
│ Aguarde enquanto verificamos       │
│ o acesso ao servidor.              │
│                                    │
└────────────────────────────────────┘
```

Conexão válida → **E00.7**.  
Falha de conexão → **E00.8**.

---

## E00.7 — Conexão realizada

### Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `E00.7` |
| Nome | Conexão realizada |
| Objetivo | Informar que o teste de conexão foi concluído com sucesso. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — estado informativo. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T00.1. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Este registro é um estado específico; aplica também as regras globais de acessibilidade, retorno e mensagens. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Segue as ações de recuperação documentadas neste estado ou retorna automaticamente à interface-base quando a condição for resolvida. |
| Relação com outras interfaces | T00.1 |

```text
┌────────────────────────────────────┐
│               ✓                    │
│                                    │
│        Conexão realizada           │
│                                    │
│ O servidor respondeu corretamente. │
│                                    │
│ Status                             │
│ ● Online                           │
│                                    │
│ [             OK              ]    │
└────────────────────────────────────┘
```

OK → retorna para **T00.1** mantendo a configuração em edição.

---

## E00.8 — Falha de conexão

### Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `E00.8` |
| Nome | Falha de conexão |
| Objetivo | Informar falha no teste de conexão e oferecer ações de recuperação. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — estado de erro com ações de recuperação. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: E00.6, T00.1. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Este registro é um estado específico; aplica também as regras globais de acessibilidade, retorno e mensagens. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Segue as ações de recuperação documentadas neste estado ou retorna automaticamente à interface-base quando a condição for resolvida. |
| Relação com outras interfaces | E00.6, T00.1 |

```text
┌────────────────────────────────────┐
│               ⚠                    │
│                                    │
│      Não foi possível conectar     │
│                                    │
│ Verifique o endereço configurado,  │
│ a conexão de rede e a              │
│ disponibilidade do servidor.       │
│                                    │
│ [        TESTAR NOVAMENTE      ]   │
│ [        EDITAR API           ]    │
└────────────────────────────────────┘
```

Testar novamente → **E00.6**.  
Editar API → **T00.1**.

---

## E00.9 — API não configurada

### Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `E00.9` |
| Nome | API não configurada |
| Objetivo | Informar que a API ainda não está configurada e direcionar para sua configuração. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — estado informativo com ação de configuração. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T00.1. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Este registro é um estado específico; aplica também as regras globais de acessibilidade, retorno e mensagens. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Segue as ações de recuperação documentadas neste estado ou retorna automaticamente à interface-base quando a condição for resolvida. |
| Relação com outras interfaces | T00.1 |

```text
┌────────────────────────────────────┐
│                                    │
│              ⚙                     │
│                                    │
│        Configure o servidor        │
│                                    │
│ Para utilizar o SaOr é        │
│ necessário configurar a API        │
│ de acesso.                         │
│                                    │
│ [       CONFIGURAR AGORA       ]   │
│                                    │
└────────────────────────────────────┘
```

Configurar agora → **T00.1**

---

## E00.10 — API indisponível no login

### Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `E00.10` |
| Nome | API indisponível no login |
| Objetivo | Informar que a API configurada está indisponível durante o acesso ao login. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — estado de indisponibilidade com ações de recuperação. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T01, T00.1. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Este registro é um estado específico; aplica também as regras globais de acessibilidade, retorno e mensagens. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Segue as ações de recuperação documentadas neste estado ou retorna automaticamente à interface-base quando a condição for resolvida. |
| Relação com outras interfaces | T01, T00.1 |

```text
┌────────────────────────────────────┐
│ ⚠ Não foi possível acessar o       │
│   servidor configurado.            │
│                                    │
│ [      TENTAR NOVAMENTE        ]   │
│                                    │
│ [   VER CONFIGURAÇÃO DA API    ]   │
└────────────────────────────────────┘
```

Tentar novamente → repete a tentativa de conexão permanecendo em **T01**; em sucesso, o login volta ao estado normal.  
Ver configuração da API → **T00.1**.

---

# 10. AUTENTICAÇÃO

# T01 — Login

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T01` |
| Nome | Login |
| Objetivo | Autenticar o vendedor e permitir acesso às configurações e à recuperação de senha. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Usuário/e-mail; senha; opção Lembrar-me. |
| Campos obrigatórios | Usuário/e-mail e senha são obrigatórios; Lembrar-me é opcional. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T00, T02, E01.2, E01.3, E00.10, T01.1, T00.3. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Estados específicos relacionados: E01.2, E01.3, E00.10. Estados globais aplicam-se quando pertinentes. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Não se aplica como retorno principal; após autenticação válida segue para T02. |
| Relação com outras interfaces | T00, T02, E01.2, E01.3, E00.10, T01.1, T00.3 |

## Objetivo

Autenticar o vendedor.

## Campos

| Campo | Obrigatório | Regra |
|---|---:|---|
| Usuário/e-mail | Sim | Identificação do usuário |
| Senha | Sim | Campo protegido |
| Lembrar-me | Não | Quando marcado, permite restaurar a sessão em uma nova abertura do aplicativo até logout, expiração, revogação da sessão ou alteração da API; quando desmarcado, uma nova abertura exige autenticação |

## Ações

| Ação | Destino |
|---|---|
| Configurações | T00 |
| Entrar | T02 em sucesso; E01.2 para credenciais inválidas; E01.3/E00.10 para falha de conectividade conforme origem |
| Esqueci minha senha | T01.1 |
| Exibir senha | Permanece T01 |
| Status da API | T00.3 |

## Textframe

```text
┌────────────────────────────────────┐
│                              ⚙     │
│                                    │
│              [ LOGO ]              │
│                                    │
│               SaOr                 │
│     Força de vendas em campo       │
│                                    │
│ Usuário / E-mail                   │
│ ┌────────────────────────────────┐ │
│ │ vendedor@empresa.com           │ │
│ └────────────────────────────────┘ │
│                                    │
│ Senha                              │
│ ┌────────────────────────────────┐ │
│ │ •••••••••                  👁 │ │
│ └────────────────────────────────┘ │
│                                    │
│ □ Lembrar-me                       │
│                                    │
│ ┌────────────────────────────────┐ │
│ │             ENTRAR             │ │
│ └────────────────────────────────┘ │
│                                    │
│       Esqueci minha senha          │
│                                    │
│────────────────────────────────────│
│ ● API conectada                    │
│ Versão 1.0                         │
└────────────────────────────────────┘
```

---

# T01.1 — Recuperar senha

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T01.1` |
| Nome | Recuperar senha |
| Objetivo | Solicitar a recuperação de acesso do usuário. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Usuário ou e-mail. |
| Campos obrigatórios | Usuário ou e-mail é obrigatório. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: E01.4, E01.5, T01. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | E01.5 — Falha ao solicitar recuperação. E01.4 representa a confirmação de sucesso da solicitação; estados globais aplicam-se quando pertinentes. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Volta para T01. |
| Relação com outras interfaces | E01.4, E01.5, T01 |

## Objetivo

Solicitar recuperação da senha.

## Campo

- e-mail ou usuário.

## Ações

| Ação | Destino / comportamento |
|---|---|
| Enviar recuperação | E01.4 em caso de aceite da solicitação; E01.5 em caso de falha |
| Voltar ao login | T01 |

## Textframe

```text
┌────────────────────────────────────┐
│ ‹       Recuperar senha            │
│                                    │
│ Informe seu usuário ou e-mail.     │
│                                    │
│ Usuário / E-mail                   │
│ ┌────────────────────────────────┐ │
│ │                                │ │
│ └────────────────────────────────┘ │
│                                    │
│ ┌────────────────────────────────┐ │
│ │     ENVIAR RECUPERAÇÃO         │ │
│ └────────────────────────────────┘ │
│                                    │
│          Voltar ao login           │
└────────────────────────────────────┘
```

---

# E01.2 — Login inválido

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `E01.2` |
| Nome | Login inválido |
| Objetivo | Informar falha de autenticação por credenciais inválidas e permitir nova tentativa. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Senha no contexto do formulário de login; demais dados permanecem em T01. |
| Campos obrigatórios | Mantêm-se obrigatórios Usuário/e-mail e Senha, conforme T01. |
| Ações e destinos | `ENTRAR` repete a autenticação; sucesso → T02; credencial inválida → E01.2; falha de rede/API → E01.3/E00.10. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Este registro é um estado específico; aplica também as regras globais de acessibilidade, retorno e mensagens. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Segue as ações de recuperação documentadas neste estado ou retorna automaticamente à interface-base quando a condição for resolvida. |
| Relação com outras interfaces | T01, T02, E01.3, E00.10 |

```text
┌────────────────────────────────────┐
│ Senha                              │
│ ┌────────────────────────────────┐ │
│ │ •••••••••                      │ │
│ └────────────────────────────────┘ │
│ ⚠ Usuário ou senha inválidos.      │
│                                    │
│ [             ENTRAR             ] │
└────────────────────────────────────┘
```

### Comportamento

- `ENTRAR` executa novamente a autenticação usando os valores informados em **T01**;
- autenticação válida → **T02**;
- nova credencial inválida → permanece em **E01.2** com mensagem textual;
- indisponibilidade de rede ou API durante a tentativa → **E01.3** ou **E00.10**, conforme a causa identificada.

---

# E01.3 — Sem conexão

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `E01.3` |
| Nome | Sem conexão |
| Objetivo | Informar indisponibilidade de conexão durante o login e permitir nova verificação. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — estado de conectividade. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | `TENTAR NOVAMENTE` repete a verificação; sucesso → T01; sem rede → E01.3; API indisponível → E00.10. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Este registro é um estado específico; aplica também as regras globais de acessibilidade, retorno e mensagens. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Segue as ações de recuperação documentadas neste estado ou retorna automaticamente à interface-base quando a condição for resolvida. |
| Relação com outras interfaces | T01, E00.10 |

```text
┌────────────────────────────────────┐
│               ⚠                    │
│                                    │
│       Sem conexão com a rede       │
│                                    │
│ Não foi possível acessar o         │
│ servidor neste momento.            │
│                                    │
│ [        TENTAR NOVAMENTE        ] │
└────────────────────────────────────┘
```

### Comportamento

- `TENTAR NOVAMENTE` repete a verificação de conectividade com a API configurada;
- conexão restabelecida → retorna para **T01** em estado normal;
- sem conexão → permanece em **E01.3**;
- API acessível pela rede, porém indisponível → **E00.10**.

---

# E01.4 — Recuperação solicitada

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `E01.4` |
| Nome | Recuperação solicitada |
| Objetivo | Confirmar que a solicitação de recuperação foi recebida sem expor a existência da conta. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — estado informativo. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T01. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Este registro é um estado específico; aplica também as regras globais de acessibilidade, retorno e mensagens. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Segue as ações de recuperação documentadas neste estado ou retorna automaticamente à interface-base quando a condição for resolvida. |
| Relação com outras interfaces | T01 |

```text
┌────────────────────────────────────┐
│               ✓                    │
│                                    │
│ Solicitação recebida               │
│                                    │
│ Se o usuário informado estiver     │
│ habilitado para recuperação, as    │
│ instruções serão enviadas pelo     │
│ canal cadastrado.                  │
│                                    │
│ [        VOLTAR AO LOGIN        ]  │
└────────────────────────────────────┘
```

Voltar ao login → **T01**.

A mensagem não deverá confirmar a existência ou inexistência de uma conta específica.

---

# E01.5 — Falha ao solicitar recuperação

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `E01.5` |
| Nome | Falha ao solicitar recuperação |
| Objetivo | Informar falha ao solicitar recuperação e permitir nova tentativa ou retorno ao login. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — estado de erro. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T01.1, T01. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Este registro é um estado específico; aplica também as regras globais de acessibilidade, retorno e mensagens. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Segue as ações de recuperação documentadas neste estado ou retorna automaticamente à interface-base quando a condição for resolvida. |
| Relação com outras interfaces | T01.1, T01 |

```text
┌────────────────────────────────────┐
│               ⚠                    │
│                                    │
│ Não foi possível enviar a          │
│ solicitação de recuperação.        │
│                                    │
│ [        TENTAR NOVAMENTE       ]  │
│ [         VOLTAR AO LOGIN       ]  │
└────────────────────────────────────┘
```

Tentar novamente → **T01.1**.  
Voltar ao login → **T01**.

---

# 11. DASHBOARD

# T02 — Início

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T02` |
| Nome | Início |
| Objetivo | Apresentar ao vendedor um resumo operacional do dia e atalhos para as principais ações. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — painel de consulta e atalhos. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T02.1, T17.1, T09, T05, T03, T16, T16.2, T15. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | É uma tela raiz da navegação principal. |
| Relação com outras interfaces | T02.1, T17.1, T09, T05, T03, T16, T16.2, T15 |

## Objetivo

Responder rapidamente:

> O que o vendedor precisa fazer agora?

## Conteúdo

- vendedor conectado;
- data;
- sincronização;
- vendas do dia;
- quantidade de pedidos;
- visitas;
- atalhos;
- próximos compromissos;
- pedidos recentes.

## Destinos

| Elemento | Destino |
|---|---|
| Sino | T02.1 |
| Perfil | T17.1 |
| Novo pedido | T09 |
| Prospect | T05 |
| Clientes | T03 |
| Agenda | T16 |
| Visita | T16.2 |
| Pedido recente | T15 |

## Textframe

```text
┌────────────────────────────────────┐
│ SaOr              🔔     👤 │
│                                    │
│ Olá, Carlos                        │
│ Quinta-feira, 15 de outubro        │
│ ✓ Dados sincronizados              │
│                                    │
│ ┌─────────────┐ ┌───────────────┐ │
│ │ R$ 8.450,00 │ │ 6 pedidos     │ │
│ │ Vendas hoje │ │ Hoje          │ │
│ └─────────────┘ └───────────────┘ │
│                                    │
│ Ações rápidas                      │
│                                    │
│ [ + Novo Pedido ] [ + Prospect ]   │
│ [ 👥 Clientes   ] [ 📅 Agenda   ] │
│                                    │
│ Próximas visitas                   │
│                                    │
│ 09:30 Mercado Central          >   │
│       Visita comercial             │
│                                    │
│ 11:00 Loja Primavera          >    │
│       Prospecção                   │
│                                    │
│ Pedidos recentes                   │
│                                    │
│ #10548 Mercado Central         >   │
│ R$ 1.850,00 • Em análise           │
│                                    │
│────────────────────────────────────│
│ Início │ Clientes │ + │ Pedidos │⋯ │
└────────────────────────────────────┘
```

---

# T02.1 — Notificações

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T02.1` |
| Nome | Notificações |
| Objetivo | Listar notificações operacionais e permitir acesso ao item relacionado. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — lista de notificações. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T15, T16.2. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | C27 EmptyState deverá ser utilizado quando não houver registros a exibir. |
| Comportamento de retorno | Volta para T02. |
| Relação com outras interfaces | T02, T15, T16.2 |

## Destinos

| Tipo de notificação | Destino |
|---|---|
| Pedido | T15 — Detalhes do pedido correspondente |
| Visita / compromisso | T16.2 — Compromisso / Visita correspondente |

```text
┌────────────────────────────────────┐
│ ‹         Notificações             │
│                                    │
│ Hoje                               │
│                                    │
│ ● Pedido #10548 aprovado           │
│   Mercado Central                  │
│   Há 15 minutos                >   │
│────────────────────────────────────│
│ ● Visita em 30 minutos             │
│   Loja Primavera                   │
│                              >     │
│────────────────────────────────────│
│ Ontem                              │
│                                    │
│   Pedido #10530 faturado       >   │
└────────────────────────────────────┘
```

---

# 12. CLIENTES

# T03 — Clientes e Prospects

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T03` |
| Nome | Clientes e Prospects |
| Objetivo | Consultar e alternar entre Clientes e Prospects do mesmo Cadastro Comercial. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Busca por nome/CNPJ/código; abas Clientes/Prospects; filtros via M03.1. |
| Campos obrigatórios | Nenhum campo de busca ou filtro é obrigatório nesta interface. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: M03.1, T04, T05.3, T05. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | C27 EmptyState deverá ser utilizado quando não houver registros a exibir. |
| Comportamento de retorno | É acessível pela navegação principal; retorno contextual preserva aba e filtros quando possível. |
| Relação com outras interfaces | M03.1, T04, T05.3, T05 |

## Regra de dados

As abas **Clientes** e **Prospects** são duas visões do mesmo **Cadastro Comercial**. Não existem dois cadastros independentes.

```text
[ CLIENTES ]  → Classificação comercial = CLIENTE
[ PROSPECTS ] → Classificação comercial = PROSPECT
```

A situação operacional deverá ser apresentada de forma independente da classificação comercial.

## Destinos

| Ação | Destino |
|---|---|
| Filtros | M03.1 |
| Cliente | T04 |
| Prospect | T05.3 |
| Novo Prospect | T05 |

## Textframe

```text
┌────────────────────────────────────┐
│ ‹          Clientes                │
│                                    │
│ ┌────────────────────────────────┐ │
│ │ 🔎 Nome, CNPJ ou código        │ │
│ └────────────────────────────────┘ │
│                                    │
│ [ CLIENTES ]       [ PROSPECTS ]   │
│                                    │
│ [ ⚙ Filtros ]                      │
│                                    │
│ Mercado Central                >   │
│ #001245                            │
│ Rio de Janeiro - RJ                │
│ ✓ Ativo                            │
│ Última compra: 10/10/2026          │
│────────────────────────────────────│
│ Supermercado Vitória           >   │
│ #001280                            │
│ Niterói - RJ                       │
│ ✓ Ativo                            │
│ Última compra: 02/10/2026          │
│                                    │
│                   (+) Novo Prospect│
│────────────────────────────────────│
│ Início │ Clientes │ + │ Pedidos │⋯ │
└────────────────────────────────────┘
```

---

# M03.1 — Filtros de clientes

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `M03.1` |
| Nome | Filtros de clientes |
| Objetivo | Refinar a consulta de Clientes e Prospects por critérios comerciais e cadastrais. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Cidade, estado, região, segmento, classificação comercial, situação operacional, última compra, última visita, clientes sem compra e somente clientes ativos. |
| Campos obrigatórios | Nenhum — todos os filtros são opcionais nesta baseline. |
| Ações e destinos | `LIMPAR` redefine os filtros e mantém o modal aberto; `APLICAR FILTRO` → T03; sem resultados → E03.2; `✕` descarta alterações não aplicadas. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Não há estado de erro específico do filtro nesta baseline. E03.2 representa resultado vazio após busca/filtro, não erro técnico; estados globais aplicam-se quando pertinentes. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Cancelar/fechar retorna à interface que abriu o modal, preservando o contexto anterior. |
| Relação com outras interfaces | T03, E03.2 |

## Campos

- cidade;
- estado;
- região;
- segmento;
- classificação comercial;
- situação operacional;
- última compra;
- última visita;
- clientes sem compra;
- somente clientes ativos.

## Textframe

```text
┌────────────────────────────────────┐
│          Filtrar clientes      ✕   │
│────────────────────────────────────│
│ Cidade                             │
│ [ Todas                        ▼ ] │
│                                    │
│ Estado                             │
│ [ Todos                        ▼ ] │
│                                    │
│ Região                             │
│ [ Todas                        ▼ ] │
│                                    │
│ Segmento                           │
│ [ Todos                        ▼ ] │
│                                    │
│ Classificação comercial            │
│ [ Todos                        ▼ ] │
│                                    │
│ Situação operacional               │
│ [ Todas                        ▼ ] │
│                                    │
│ Última compra                      │
│ [ Qualquer período             ▼ ] │
│                                    │
│ Última visita                      │
│ [ Qualquer período             ▼ ] │
│                                    │
│ □ Clientes sem compra              │
│ □ Somente ativos                   │
│                                    │
│ [ LIMPAR ]       [ APLICAR FILTRO ]│
└────────────────────────────────────┘
```

### Comportamento

- `LIMPAR` redefine todos os critérios para seus valores padrão e mantém **M03.1** aberto;
- `APLICAR FILTRO` aplica os critérios selecionados, fecha **M03.1** e atualiza **T03**;
- fechar por `✕` descarta alterações ainda não aplicadas e mantém em **T03** os filtros anteriormente vigentes;
- se a combinação aplicada não retornar registros, **T03** deverá apresentar **E03.2**.

---

# E03.2 — Busca sem resultado

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `E03.2` |
| Nome | Busca sem resultado |
| Objetivo | Informar que a busca ou os filtros não retornaram registros e oferecer recuperação. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — estado vazio de busca. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T05. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Este registro é um estado específico; aplica também as regras globais de acessibilidade, retorno e mensagens. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Segue as ações de recuperação documentadas neste estado ou retorna automaticamente à interface-base quando a condição for resolvida. |
| Relação com outras interfaces | T05, T03 |

```text
┌────────────────────────────────────┐
│ 🔎 Loja inexistente                │
│                                    │
│              ◯                     │
│                                    │
│ Nenhum cliente encontrado          │
│                                    │
│ Verifique a busca ou cadastre      │
│ um novo prospect.                  │
│                                    │
│ [       NOVO PROSPECT        ]     │
└────────────────────────────────────┘
```

Novo Prospect → **T05**.

---

# T04 — Cliente / Resumo

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T04` |
| Nome | Cliente / Resumo |
| Objetivo | Apresentar o resumo do Cliente e as ações comerciais permitidas para sua situação. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — resumo e navegação contextual do Cliente. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T09, T06, T04.1, T04.2, T04.3, T04.4, T04.5. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Volta para T03 preservando o contexto do Cliente. |
| Relação com outras interfaces | T03, T09, T06, T04.1, T04.2, T04.3, T04.4, T04.5 |

## Destinos

| Item | Destino |
|---|---|
| Novo pedido | T09 |
| Registrar visita | T06 |
| Pedidos | T04.1 |
| Visitas | T04.2 |
| Financeiro | T04.3 |
| Endereço | T04.4 |
| Dados cadastrais | T04.5 |

## Regras

- esta tela representa um Cadastro Comercial com classificação **CLIENTE**;
- o exemplo abaixo apresenta situação operacional **ATIVO**;
- **Novo pedido** somente estará habilitado quando `Classificação = CLIENTE` e `Situação = ATIVO`;
- para Cliente **BLOQUEADO** ou **INATIVO**, a ação de Novo Pedido deverá ficar indisponível e a interface deverá informar textualmente o motivo da restrição.

## Textframe

```text
┌────────────────────────────────────┐
│ ‹          Cliente            ⋮    │
│                                    │
│ Mercado Central                    │
│ Cliente #001245                    │
│ Classificação: Cliente             │
│ ✓ Ativo                            │
│                                    │
│ 📍 Rio de Janeiro - RJ             │
│ ☎ (21) 99999-9999                  │
│ 👤 João da Silva                   │
│                                    │
│ [ NOVO PEDIDO ]                    │
│ [ REGISTRAR VISITA ]               │
│                                    │
│ Resumo │ Pedidos │ Visitas │ $     │
│────────────────────────────────────│
│ Limite disponível                  │
│ R$ 18.500,00                       │
│                                    │
│ Última compra                      │
│ 10/10/2026 • R$ 3.250,00           │
│                                    │
│ Endereço                       >   │
│ Rua Exemplo, 150                   │
│                                    │
│ Dados cadastrais               >   │
└────────────────────────────────────┘
```

---

# T04.1 — Cliente / Pedidos

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T04.1` |
| Nome | Cliente / Pedidos |
| Objetivo | Consultar os pedidos vinculados ao Cliente e iniciar um novo pedido quando permitido. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — lista de pedidos do Cliente. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Selecionar pedido → T15; `+ NOVO PEDIDO` → T09 somente quando o Cliente atual estiver `ATIVO`; Cliente Bloqueado/Inativo mantém a ação indisponível. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | C27 EmptyState deverá ser utilizado quando não houver registros a exibir. |
| Comportamento de retorno | Volta para T04 preservando o Cliente. |
| Relação com outras interfaces | T04, T15, T09 |

```text
┌────────────────────────────────────┐
│ ‹       Mercado Central            │
│                                    │
│ Resumo │ PEDIDOS │ Visitas │ $     │
│────────────────────────────────────│
│                                    │
│ #10548                         >   │
│ 15/10/2026                         │
│ R$ 1.850,00                        │
│ ● Em análise                       │
│────────────────────────────────────│
│ #10482                         >   │
│ 10/10/2026                         │
│ R$ 3.250,00                        │
│ ● Faturado                         │
│                                    │
│ [       + NOVO PEDIDO        ]     │
└────────────────────────────────────┘
```

Pedido selecionado → **T15**.  
Novo pedido → **T09**, com o Cliente atual pré-selecionado.

### Regra de elegibilidade

- `+ NOVO PEDIDO` somente ficará habilitado para `CLIENTE + ATIVO`;
- para Cliente `BLOQUEADO` ou `INATIVO`, a consulta aos pedidos existentes continuará disponível, mas a criação de novo pedido ficará indisponível;
- quando indisponível, a interface deverá exibir texto explicando que o Cliente não está apto a emitir novo pedido, sem depender somente de cor.

---

# T04.2 — Cliente / Visitas

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T04.2` |
| Nome | Cliente / Visitas |
| Objetivo | Consultar o histórico de visitas do Cliente e registrar nova visita. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — lista de visitas do Cliente. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T06.2, T06. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | C27 EmptyState deverá ser utilizado quando não houver registros a exibir. |
| Comportamento de retorno | Volta para T04 preservando o Cliente. |
| Relação com outras interfaces | T04, T06.2, T06 |

```text
┌────────────────────────────────────┐
│ ‹       Mercado Central            │
│                                    │
│ Resumo │ Pedidos │ VISITAS │ $     │
│────────────────────────────────────│
│                                    │
│ 15 OUT 2026                    >   │
│ Visita comercial                   │
│ Venda realizada                    │
│────────────────────────────────────│
│ 08 OUT 2026                    >   │
│ Relacionamento                     │
│ Retornar em 7 dias                 │
│                                    │
│ [      + REGISTRAR VISITA      ]   │
└────────────────────────────────────┘
```

Visita selecionada → **T06.2**.  
Registrar visita → **T06**, com o Cliente atual pré-selecionado.

---

# T04.3 — Cliente / Financeiro

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T04.3` |
| Nome | Cliente / Financeiro |
| Objetivo | Consultar as informações financeiras permitidas do Cliente. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — consulta financeira somente leitura. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Somente navegação de retorno; não possui ação funcional própria nesta baseline. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Volta para T04 preservando o Cliente. |
| Relação com outras interfaces | T04 |

## Informações previstas

- limite total;
- limite disponível;
- títulos em aberto;
- títulos vencidos;
- situação cadastral;
- bloqueio comercial.

## Textframe

```text
┌────────────────────────────────────┐
│ ‹       Mercado Central            │
│                                    │
│ Resumo │ Pedidos │ Visitas │ FIN.  │
│────────────────────────────────────│
│ Situação                           │
│ ● Regular                          │
│                                    │
│ Limite de crédito                  │
│ R$ 30.000,00                       │
│                                    │
│ Utilizado                          │
│ R$ 11.500,00                       │
│                                    │
│ Disponível                         │
│ R$ 18.500,00                       │
│────────────────────────────────────│
│ Títulos em aberto                  │
│ R$ 4.850,00                        │
│                                    │
│ Títulos vencidos                   │
│ R$ 0,00                            │
└────────────────────────────────────┘
```

---

# T04.4 — Cliente / Endereço

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T04.4` |
| Nome | Cliente / Endereço |
| Objetivo | Consultar o endereço do Cliente e permitir abertura no serviço de mapas. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — consulta de endereço somente leitura. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | `ABRIR NO MAPA` abre o serviço de mapas padrão; indisponibilidade mantém a tela aberta com mensagem textual. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Volta para a interface que abriu o endereço, preservando o contexto. |
| Relação com outras interfaces | T04, T15.2, T16.2 |

## Informações

- CEP;
- logradouro;
- número;
- complemento;
- bairro;
- cidade;
- UF;
- referência;
- localização.

## Textframe

```text
┌────────────────────────────────────┐
│ ‹          Endereço                │
│                                    │
│ Mercado Central                    │
│                                    │
│ CEP                                │
│ 20000-000                          │
│                                    │
│ Rua Exemplo, 150                   │
│ Sala 2                             │
│ Centro                             │
│ Rio de Janeiro - RJ                │
│                                    │
│ Referência                         │
│ Próximo à Praça Central            │
│                                    │
│ ┌────────────────────────────────┐ │
│ │           MAPA                 │ │
│ │                                │ │
│ │             ●                  │ │
│ └────────────────────────────────┘ │
│                                    │
│ [       ABRIR NO MAPA         ]    │
└────────────────────────────────────┘
```

### Ação externa — Abrir no mapa

`ABRIR NO MAPA` deverá abrir o aplicativo de mapas padrão do dispositivo com o endereço exibido. Se o sistema operacional solicitar escolha de aplicativo, será utilizado o seletor nativo. Caso nenhum aplicativo ou serviço de mapas esteja disponível, a tela permanecerá aberta e exibirá mensagem textual de indisponibilidade.

---

# T04.5 — Cliente / Dados cadastrais

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T04.5` |
| Nome | Cliente / Dados cadastrais |
| Objetivo | Consultar os dados cadastrais do Cliente. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — consulta de dados cadastrais somente leitura. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Somente navegação de retorno; não possui ação de edição nesta baseline. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Volta para T04 preservando o Cliente. |
| Relação com outras interfaces | T04 |

```text
┌────────────────────────────────────┐
│ ‹       Dados cadastrais           │
│                                    │
│ Razão social                       │
│ Mercado Central LTDA               │
│                                    │
│ Nome fantasia                      │
│ Mercado Central                    │
│                                    │
│ CNPJ                               │
│ 00.000.000/0001-00                 │
│                                    │
│ Inscrição Estadual                 │
│ 123456789                          │
│                                    │
│ Segmento                           │
│ Supermercado                       │
│                                    │
│ Contato principal                  │
│ João da Silva                      │
│                                    │
│ Telefone                           │
│ (21) 99999-9999                    │
│                                    │
│ E-mail                             │
│ contato@cliente.com                │
└────────────────────────────────────┘
```

---

# 13. PROSPECT

O Prospect utiliza o mesmo **Cadastro Comercial** que posteriormente poderá ser classificado como Cliente.

Nesta versão, a regra é:

```text
NOVO CADASTRO PROSPECTADO / CONTATADO
              │
              ▼
Classificação comercial = PROSPECT
Situação operacional    = BLOQUEADO
              │
              ▼
       NÃO EMITE PEDIDO
              │
              │ cadastro aprovado
              ▼
Classificação comercial = CLIENTE
Situação operacional    = ATIVO
              │
              ▼
         PODE EMITIR PEDIDO
```

O cadastro do Prospect será dividido em etapas.

```text
Dados básicos
     ↓
Endereço
     ↓
Informações comerciais
     ↓
Prospect criado
```

A conversão para Cliente não deverá duplicar o cadastro nem apagar o histórico existente.

---

# T05 — Novo Prospect / Dados básicos

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T05` |
| Nome | Novo Prospect / Dados básicos |
| Objetivo | Cadastrar os dados básicos de um novo Prospect. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Dados básicos do Prospect conforme tabela da seção. |
| Campos obrigatórios | Nome fantasia, segmento, contato principal e telefone/WhatsApp são obrigatórios; demais campos conforme tabela. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T05.1. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Volta para T03 sem perder contexto já salvo; enquanto em cadastro, dados em edição seguem a regra do fluxo. |
| Relação com outras interfaces | T03, T05.1 |

## Campos

| Campo | Obrigatório |
|---|---:|
| Nome fantasia | Sim |
| Razão social | Não |
| CNPJ/CPF | Não no cadastro preliminar |
| Segmento | Sim |
| Contato principal | Sim |
| Telefone/WhatsApp | Sim |
| E-mail | Não |

## Textframe

```text
┌────────────────────────────────────┐
│ ‹         Novo Prospect            │
│                                    │
│ ●────────○────────○                │
│ Dados    Endereço  Comercial       │
│                                    │
│ Nome fantasia *                    │
│ [______________________________]   │
│                                    │
│ Razão social                       │
│ [______________________________]   │
│                                    │
│ CNPJ / CPF                         │
│ [______________________________]   │
│                                    │
│ Segmento *                         │
│ [ Selecione                    ▼ ] │
│                                    │
│ Contato principal *                │
│ [______________________________]   │
│                                    │
│ Telefone / WhatsApp *              │
│ [______________________________]   │
│                                    │
│ E-mail                             │
│ [______________________________]   │
│                                    │
│ [          CONTINUAR           ]   │
└────────────────────────────────────┘
```

Continuar → **T05.1**.

---

# T05.1 — Novo Prospect / Endereço

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T05.1` |
| Nome | Novo Prospect / Endereço |
| Objetivo | Cadastrar o endereço do novo Prospect, com apoio opcional de consulta por CEP. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | CEP, logradouro, número, complemento, bairro, cidade, UF e referência. |
| Campos obrigatórios | Logradouro, número, bairro, cidade e UF são obrigatórios; CEP, complemento e referência são opcionais. |
| Ações e destinos | `BUSCAR` consulta o CEP na própria tela; `VOLTAR` → T05; `CONTINUAR` → T05.2. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Volta para T05 preservando dados preenchidos. |
| Relação com outras interfaces | T05, T05.2 |

## Campos

| Campo | Obrigatório |
|---|---:|
| CEP | Não |
| Logradouro | Sim |
| Número | Sim |
| Complemento | Não |
| Bairro | Sim |
| Cidade | Sim |
| UF | Sim |
| Referência | Não |

## Textframe

```text
┌────────────────────────────────────┐
│ ‹         Novo Prospect            │
│                                    │
│ ●────────●────────○                │
│ Dados    Endereço  Comercial       │
│                                    │
│ CEP                                │
│ [___________] [ BUSCAR ]           │
│                                    │
│ Logradouro *                       │
│ [______________________________]   │
│                                    │
│ Número *                           │
│ [__________]                       │
│                                    │
│ Complemento                        │
│ [______________________________]   │
│                                    │
│ Bairro *                           │
│ [______________________________]   │
│                                    │
│ Cidade *                           │
│ [______________________________]   │
│                                    │
│ UF *                               │
│ [ Selecione                    ▼ ] │
│                                    │
│ Referência                         │
│ [______________________________]   │
│                                    │
│ [ VOLTAR ]          [ CONTINUAR ]  │
└────────────────────────────────────┘
```

### Comportamento das ações

- `BUSCAR` consulta o endereço a partir do CEP informado;
- quando o serviço retornar dados, os campos disponíveis de Logradouro, Bairro, Cidade e UF deverão ser preenchidos automaticamente, permanecendo editáveis quando permitido pelo cadastro;
- CEP não encontrado ou indisponibilidade do serviço deverá produzir mensagem textual inline e **não bloquear o preenchimento manual do endereço**;
- `VOLTAR` → **T05**, preservando os dados preenchidos;
- `CONTINUAR` → **T05.2**.

---

# T05.2 — Novo Prospect / Informações comerciais

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T05.2` |
| Nome | Novo Prospect / Informações comerciais |
| Objetivo | Cadastrar e revisar as informações comerciais do Prospect. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Origem, potencial, interesse, concorrente atual, frequência de compra, próximo contato e observações. |
| Campos obrigatórios | Origem é obrigatória; Potencial, Interesse principal, Concorrente atual, Frequência de compra, Próximo contato e Observações são opcionais nesta baseline. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T05.1, T05.3. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | No cadastro novo, volta para T05.1 preservando dados preenchidos; ao editar Prospect existente, volta para T05.3 sem aplicar alterações não salvas. |
| Relação com outras interfaces | T05.1, T05.3 |

## Objetivo

Registrar potencial e contexto comercial da oportunidade.

## Campos

| Campo | Obrigatório |
|---|---:|
| Origem | Sim |
| Potencial | Não |
| Interesse principal | Não |
| Concorrente atual | Não |
| Frequência de compra | Não |
| Próximo contato | Não |
| Observações | Não |

## Modos de uso

T05.2 possui dois modos funcionais sob o mesmo ID:

- **Cadastro novo:** aberta a partir de T05.1 durante o wizard de criação do Prospect; `VOLTAR` retorna a T05.1 preservando os dados e `SALVAR` conclui a etapa comercial e abre T05.3.
- **Edição de Prospect existente:** aberta a partir de T05.3 com os dados comerciais atuais carregados; os mesmos campos ficam disponíveis para edição; `VOLTAR` retorna a T05.3 sem aplicar alterações não salvas e `SALVAR` persiste as alterações e retorna a T05.3.

O modo de edição reutiliza a mesma interface e os mesmos componentes; não cria uma nova rota ou novo cadastro.

## Textframe — cadastro novo

```text
┌────────────────────────────────────┐
│ ‹         Novo Prospect            │
│                                    │
│ ●────────●────────●                │
│ Dados    Endereço  Comercial       │
│                                    │
│ Origem do prospect *               │
│ [ Visita espontânea            ▼ ] │
│                                    │
│ Potencial estimado                 │
│ [ Alto                         ▼ ] │
│                                    │
│ Interesse principal               │
│ [______________________________]   │
│                                    │
│ Concorrente atual                  │
│ [______________________________]   │
│                                    │
│ Frequência de compra               │
│ [ Mensal                       ▼ ] │
│                                    │
│ Próximo contato                    │
│ [ 20/10/2026                   📅 ]│
│                                    │
│ Observações                        │
│ ┌────────────────────────────────┐ │
│ │                                │ │
│ │                                │ │
│ └────────────────────────────────┘ │
│                                    │
│ [ VOLTAR ]        [ SALVAR ]       │
└────────────────────────────────────┘
```

Voltar → **T05.1** preservando os dados preenchidos.  
Salvar → **T05.3**.

### Textframe — edição de Prospect existente

```text
┌────────────────────────────────────┐
│ ‹    Informações comerciais        │
│                                    │
│ Loja Nova Esperança                │
│                                    │
│ Origem do prospect *               │
│ [ Visita espontânea            ▼ ] │
│                                    │
│ Potencial estimado                 │
│ [ Alto                         ▼ ] │
│                                    │
│ Interesse principal               │
│ [______________________________]   │
│                                    │
│ Concorrente atual                  │
│ [______________________________]   │
│                                    │
│ Frequência de compra               │
│ [ Mensal                       ▼ ] │
│                                    │
│ Próximo contato                    │
│ [ 20/10/2026                   📅 ]│
│                                    │
│ Observações                        │
│ ┌────────────────────────────────┐ │
│ │                                │ │
│ └────────────────────────────────┘ │
│                                    │
│ [ VOLTAR ]        [ SALVAR ]       │
└────────────────────────────────────┘
```

No modo de edição, `VOLTAR` → **T05.3** sem salvar e `SALVAR` → **T05.3** com os dados atualizados.

---

# T05.3 — Prospect / Resumo

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T05.3` |
| Nome | Prospect / Resumo |
| Objetivo | Apresentar o resumo do Prospect e acesso às informações e ações relacionadas. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — resumo do Prospect e navegação contextual. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T04.4, T05.2, T05.4, T06. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Volta para T03 na aba Prospects, preservando o Prospect. |
| Relação com outras interfaces | T03, T04.4, T05.2, T05.4, T06 |

```text
┌────────────────────────────────────┐
│ ‹          Prospect           ⋮    │
│                                    │
│ Loja Nova Esperança                │
│ Classificação: Prospect            │
│ ⚠ Bloqueado                        │
│ Cadastro ainda não aprovado        │
│ Não pode emitir pedido             │
│                                    │
│ 📍 Rio de Janeiro - RJ             │
│ ☎ (21) 98888-0000                  │
│ 👤 Maria Souza                     │
│                                    │
│ [ REGISTRAR VISITA ]               │
│                                    │
│ Potencial                          │
│ Alto                               │
│                                    │
│ Interesse                          │
│ Linha de produtos ABC              │
│                                    │
│ Próximo contato                    │
│ 20/10/2026                         │
│                                    │
│ Endereço                       >   │
│ Informações comerciais        >   │
│ Histórico de visitas          >   │
└────────────────────────────────────┘
```

Neste contexto:

- Endereço → reutiliza estrutura de **T04.4**;
- Informações comerciais → **T05.2 em modo visualização/edição**;
- Histórico → **T05.4**;
- Registrar visita → **T06**, com o Prospect pré-selecionado.

---

# T05.4 — Prospect / Histórico de visitas

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T05.4` |
| Nome | Prospect / Histórico de visitas |
| Objetivo | Consultar o histórico de visitas do Prospect e iniciar nova visita. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — histórico de visitas. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T06.2, T06. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | C27 EmptyState deverá ser utilizado quando não houver registros a exibir. |
| Comportamento de retorno | Volta para T05.3 preservando o Prospect. |
| Relação com outras interfaces | T05.3, T06.2, T06 |

## Destinos

| Ação | Destino |
|---|---|
| Selecionar visita | T06.2 — Detalhes da visita correspondente |
| Nova visita | T06 — Registrar visita, com o Prospect pré-selecionado |

```text
┌────────────────────────────────────┐
│ ‹      Histórico de visitas        │
│                                    │
│ Loja Nova Esperança                │
│                                    │
│ 15 OUT 2026                    >   │
│ Prospecção                         │
│ Interesse demonstrado             │
│────────────────────────────────────│
│ 08 OUT 2026                    >   │
│ Primeiro contato                   │
│ Retornar em uma semana             │
│                                    │
│ [       + NOVA VISITA        ]     │
└────────────────────────────────────┘
```

---

# 14. VISITAS

# T06 — Registrar visita

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T06` |
| Nome | Registrar visita |
| Objetivo | Registrar uma visita comercial vinculada a Cliente ou Prospect. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Cliente/Prospect, data/hora, tipo, objetivo, observações, resultado, próxima ação e próximo contato. |
| Campos obrigatórios | Cliente/Prospect é obrigatório. Data/hora são registradas no contexto da visita. Os demais campos de T06 são opcionais nesta baseline; para finalizar, M06.1 exige Resultado. |
| Ações e destinos | `INICIAR PEDIDO` → T09 somente para `CLIENTE + ATIVO`; `FINALIZAR VISITA` → M06.1. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Volta para a interface de origem preservando Cliente/Prospect pré-selecionado. |
| Relação com outras interfaces | T04.2, T05.3, T05.4, T16.2, T09, M06.1 |

## Campos

- cliente/prospect;
- data;
- hora;
- tipo;
- objetivo;
- observação;
- resultado;
- próxima ação;
- data do próximo contato.

## Tipos

```text
Venda
Prospecção
Relacionamento
Pós-venda
Cobrança
Outro
```

## Textframe

```text
┌────────────────────────────────────┐
│ ‹       Registrar visita           │
│                                    │
│ Mercado Central                    │
│                                    │
│ Tipo                               │
│ [ Venda ] [ Prospecção ]           │
│ [ Relacionamento ] [ Outro ]       │
│                                    │
│ Data / hora                        │
│ 15/10/2026 • 09:42                 │
│                                    │
│ Objetivo                           │
│ [______________________________]   │
│                                    │
│ Observações                        │
│ ┌────────────────────────────────┐ │
│ │                                │ │
│ └────────────────────────────────┘ │
│                                    │
│ Resultado                          │
│ [ Selecione                    ▼ ] │
│                                    │
│ Próxima ação                       │
│ [______________________________]   │
│                                    │
│ Próximo contato                    │
│ [ __/__/____                   📅 ]│
│                                    │
│ [ INICIAR PEDIDO ]                 │
│ [ FINALIZAR VISITA ]               │
└────────────────────────────────────┘
```

Iniciar Pedido → **T09** somente quando o Cadastro Comercial da visita for `CLIENTE + ATIVO`, mantendo-o pré-selecionado.  
Finalizar → **M06.1**.

### Regra de elegibilidade para iniciar pedido

- visita vinculada a `CLIENTE + ATIVO` → `INICIAR PEDIDO` habilitado;
- visita vinculada a `PROSPECT + BLOQUEADO`, `CLIENTE + BLOQUEADO` ou `CLIENTE + INATIVO` → ação indisponível;
- quando indisponível, a interface deverá apresentar texto explicando a restrição;
- bloquear ou inativar o Cliente durante a visita não altera sua classificação, apenas impede iniciar o pedido.

---

# M06.1 — Confirmar finalização da visita

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `M06.1` |
| Nome | Confirmar finalização da visita |
| Objetivo | Confirmar a finalização da visita e registrar seu resultado e próxima ação. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Resultado e próxima ação para encerramento da visita. |
| Campos obrigatórios | Resultado é obrigatório para concluir a visita; Próxima ação é opcional nesta baseline. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T06, T04.2, T05.4, T16, E06.3. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Estados específicos relacionados: E06.3. Estados globais aplicam-se quando pertinentes. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Cancelar/fechar retorna à interface que abriu o modal, preservando o contexto anterior. |
| Relação com outras interfaces | T06, T04.2, T05.4, T16, E06.3 |

## Comportamento

- `CANCELAR` fecha o modal e retorna para T06 sem salvar a finalização;
- `FINALIZAR` salva a visita como **Concluída**;
- após sucesso, o sistema retorna para a interface de origem mantendo o contexto: T04.2 para Cliente, T05.4 para Prospect ou T16 quando iniciado pela Agenda;
- em caso de falha, permanece no contexto da visita e apresenta **E06.3**.

```text
┌────────────────────────────────────┐
│       Finalizar visita?            │
│                                    │
│ A visita será salva no histórico   │
│ do cliente.                        │
│                                    │
│ Resultado                          │
│ Interesse / Venda / Sem interesse  │
│                                    │
│ Próxima ação                       │
│ Retornar em 7 dias                 │
│                                    │
│ [ CANCELAR ]      [ FINALIZAR ]    │
└────────────────────────────────────┘
```

---

# E06.3 — Falha ao finalizar visita

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `E06.3` |
| Nome | Falha ao finalizar visita |
| Objetivo | Informar falha ao finalizar a visita e permitir recuperação sem perda dos dados. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — estado de erro. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: M06.1, T06. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Este registro é um estado específico; aplica também as regras globais de acessibilidade, retorno e mensagens. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Segue as ações de recuperação documentadas neste estado ou retorna automaticamente à interface-base quando a condição for resolvida. |
| Relação com outras interfaces | M06.1, T06 |

```text
┌────────────────────────────────────┐
│               ⚠                    │
│                                    │
│ Não foi possível finalizar a       │
│ visita. Os dados preenchidos foram │
│ preservados.                       │
│                                    │
│ [        TENTAR NOVAMENTE       ]  │
│ [             VOLTAR           ]  │
└────────────────────────────────────┘
```

Tentar novamente → **M06.1**.  
Voltar → **T06**, preservando os dados preenchidos.

---

# T06.2 — Detalhes da visita

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T06.2` |
| Nome | Detalhes da visita |
| Objetivo | Consultar os detalhes de uma visita registrada e seu pedido relacionado quando existir. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — consulta de visita registrada. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T15. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Volta para a lista/histórico de origem. |
| Relação com outras interfaces | T15 |

```text
┌────────────────────────────────────┐
│ ‹        Detalhes da visita        │
│                                    │
│ Mercado Central                    │
│ 15/10/2026 • 09:42                 │
│                                    │
│ Tipo                               │
│ Venda                              │
│                                    │
│ Resultado                          │
│ Pedido realizado                   │
│                                    │
│ Observações                        │
│ Cliente demonstrou interesse em    │
│ ampliar a linha ABC.               │
│                                    │
│ Próxima ação                       │
│ Retornar após entrega              │
│                                    │
│ Próximo contato                    │
│ 22/10/2026                         │
│                                    │
│ Pedido relacionado                 │
│ #10549                         >   │
└────────────────────────────────────┘
```

Pedido relacionado → **T15**.

---

# 15. PRODUTOS

# T07 — Catálogo

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T07` |
| Nome | Catálogo |
| Objetivo | Consultar o catálogo de produtos, aplicar filtros e adicionar itens ao pedido em edição. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Busca de produto, filtros e ações de quantidade/adição ao pedido. |
| Campos obrigatórios | Nenhum campo de busca ou filtro é obrigatório nesta interface. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: M07.1, T08, T10. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | C27 EmptyState deverá ser utilizado quando não houver registros a exibir. |
| Comportamento de retorno | Volta para T10 preservando o pedido em edição. Nesta baseline, T07 é acessada pelo fluxo de itens do pedido. |
| Relação com outras interfaces | M07.1, T08, T10 |

## Destinos

| Ação | Destino |
|---|---|
| Filtros | M07.1 |
| Produto | T08 |
| Adicionar | Adiciona/atualiza o item no pedido em edição |
| Ver pedido | T10 |

## Regra de contexto

Nesta baseline, **T07 é aberta a partir de T10 e opera no contexto de um pedido em edição**. As ações `Adicionar` e `Ver pedido` utilizam esse pedido corrente; não existe fluxo independente de inclusão de produto fora de um pedido.

## Textframe

```text
┌────────────────────────────────────┐
│ ‹          Produtos                │
│                                    │
│ ┌────────────────────────────────┐ │
│ │ 🔎 Produto, código ou SKU      │ │
│ └────────────────────────────────┘ │
│                                    │
│ [ ⚙ Filtros ]                     │
│                                    │
│ Categorias                         │
│ [Todos] [Bebidas] [Alimentos]      │
│                                    │
│ ┌──────┐ Produto ABC          >    │
│ │ IMG  │ SKU 000123                │
│ │      │ R$ 25,90 / UN             │
│ └──────┘ ✓ Disponível      [ + ]   │
│────────────────────────────────────│
│ ┌──────┐ Produto XYZ          >    │
│ │ IMG  │ SKU 000456                │
│ │      │ R$ 48,50 / CX             │
│ └──────┘ ✓ Disponível      [ + ]   │
│                                    │
│────────────────────────────────────│
│ 3 itens                 R$ 325,80  │
│ [          VER PEDIDO           ]  │
└────────────────────────────────────┘
```

---

# M07.1 — Filtros de produtos

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `M07.1` |
| Nome | Filtros de produtos |
| Objetivo | Refinar o catálogo de produtos por critérios de consulta. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Categoria, disponibilidade, promoção e demais filtros definidos na seção. |
| Campos obrigatórios | Nenhum — todos os filtros são opcionais nesta baseline. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T07. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Cancelar/fechar retorna à interface que abriu o modal, preservando o contexto anterior. |
| Relação com outras interfaces | T07 |

```text
┌────────────────────────────────────┐
│         Filtrar produtos       ✕   │
│────────────────────────────────────│
│ Categoria                          │
│ [ Todas                        ▼ ] │
│                                    │
│ Marca                              │
│ [ Todas                        ▼ ] │
│                                    │
│ Linha                              │
│ [ Todas                        ▼ ] │
│                                    │
│ Disponibilidade                    │
│ □ Somente disponíveis              │
│                                    │
│ □ Somente promoções                │
│ □ Comprados pelo cliente           │
│ □ Favoritos                        │
│                                    │
│ [ LIMPAR ]        [ APLICAR ]      │
└────────────────────────────────────┘
```

Limpar → redefine os filtros no próprio modal.  
Aplicar → fecha M07.1 e atualiza **T07**.

---

# E07.2 — Produto não encontrado

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `E07.2` |
| Nome | Produto não encontrado |
| Objetivo | Informar que nenhum produto foi encontrado e oferecer limpeza dos filtros. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — estado vazio de produto. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T07. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Este registro é um estado específico; aplica também as regras globais de acessibilidade, retorno e mensagens. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Segue as ações de recuperação documentadas neste estado ou retorna automaticamente à interface-base quando a condição for resolvida. |
| Relação com outras interfaces | T07 |

```text
┌────────────────────────────────────┐
│              🔎                    │
│                                    │
│ Nenhum produto encontrado          │
│                                    │
│ Altere a busca ou remova algum     │
│ filtro.                            │
│                                    │
│ [       LIMPAR FILTROS       ]     │
└────────────────────────────────────┘
```

Limpar filtros → retorna para **T07** sem filtros aplicados.

---

# T08 — Produto

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T08` |
| Nome | Produto |
| Objetivo | Consultar detalhes do produto, definir quantidade e adicioná-lo ao pedido em edição. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Quantidade do produto no contexto do pedido. |
| Campos obrigatórios | Quantidade válida maior que zero para adicionar ao pedido. |
| Ações e destinos | `ADICIONAR AO PEDIDO` adiciona/atualiza o item e retorna para T10. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Volta para T07; ao adicionar ao pedido, retorna para T10. |
| Relação com outras interfaces | T07, T10 |

```text
┌────────────────────────────────────┐
│ ‹           Produto                │
│                                    │
│ ┌────────────────────────────────┐ │
│ │                                │ │
│ │            IMAGEM              │ │
│ │                                │ │
│ └────────────────────────────────┘ │
│                                    │
│ Produto ABC                        │
│ SKU 000123                         │
│                                    │
│ R$ 25,90 / UN                      │
│                                    │
│ ✓ Disponível                       │
│                                    │
│ Promoção                           │
│ A partir de 10 UN: R$ 24,50        │
│                                    │
│ Quantidade                         │
│                                    │
│       [ − ]    10    [ + ]         │
│                                    │
│ Total                              │
│ R$ 259,00                          │
│                                    │
│ [     ADICIONAR AO PEDIDO      ]   │
└────────────────────────────────────┘
```

Adicionar ao pedido → adiciona/atualiza o item no pedido em edição e retorna para **T10**.

T08 é acessada a partir de **T07** no contexto do pedido em edição. Voltar sem adicionar retorna para **T07**, preservando o contexto do pedido.

---

# 16. PEDIDO DE VENDA

O fluxo será um wizard.

```text
Cliente
  ↓
Itens
  ↓
Condições
  ↓
Revisão
```

---

# T09 — Pedido / Cliente

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T09` |
| Nome | Pedido / Cliente |
| Objetivo | Selecionar Cliente apto, endereço e tabela de preço para iniciar o Pedido de Venda. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Cliente, endereço de entrega e tabela de preço; vendedor e data são exibidos no contexto. |
| Campos obrigatórios | Cliente elegível, endereço de entrega e tabela de preço devem estar definidos antes de avançar. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: M09.1, T09.2, M09.3, T10. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Volta à interface de origem; o estado do pedido em edição deve ser preservado. |
| Relação com outras interfaces | M09.1, T09.2, M09.3, T10 |

## Regras

- o pedido somente poderá utilizar Cadastro Comercial com `Classificação = CLIENTE`;
- a situação operacional deverá ser `ATIVO`;
- Prospect, Cliente Bloqueado e Cliente Inativo não poderão avançar para a etapa de itens;
- quando um cliente deixar de estar apto durante um pedido em edição, o avanço deverá ser bloqueado e a interface deverá informar a restrição;
- a mensagem de impedimento deverá utilizar texto e, quando aplicável, ícone, nunca somente cor.

```text
┌────────────────────────────────────┐
│ ‹          Novo Pedido             │
│                                    │
│ ●────────○────────○────────○        │
│ Cliente   Itens    Cond.   Revisão │
│                                    │
│ Cliente *                          │
│ ┌────────────────────────────────┐ │
│ │ Mercado Central            🔎  │ │
│ └────────────────────────────────┘ │
│                                    │
│ Endereço de entrega            >   │
│ Rua Exemplo, 150                   │
│ Rio de Janeiro - RJ                │
│                                    │
│ Tabela de preço                >   │
│ Tabela Padrão                      │
│                                    │
│ Vendedor                           │
│ Carlos Silva                       │
│                                    │
│ Data                               │
│ 15/10/2026                         │
│                                    │
│ [          CONTINUAR           ]   │
└────────────────────────────────────┘
```

Destinos:

```text
🔎 Cliente             → M09.1
Endereço de entrega >  → T09.2
Tabela de preço >      → M09.3
Continuar              → T10
```

---

# M09.1 — Selecionar cliente

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `M09.1` |
| Nome | Selecionar cliente |
| Objetivo | Selecionar um Cliente ativo e apto para emissão do pedido. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Busca/seleção de Cliente elegível. |
| Campos obrigatórios | Um Cliente Ativo deve estar selecionado para habilitar a confirmação. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T09. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Cancelar/fechar retorna à interface que abriu o modal, preservando o contexto anterior. |
| Relação com outras interfaces | T09 |

## Regras

- somente Cadastros Comerciais classificados como **CLIENTE** serão apresentados neste seletor;
- Clientes **ATIVOS** poderão ser selecionados;
- Clientes **BLOQUEADOS** ou **INATIVOS** poderão aparecer no resultado da busca para explicar sua situação, porém permanecerão indisponíveis para seleção;
- Prospects não serão listados neste seletor;
- a indisponibilidade deverá ser indicada por texto/ícone além da cor.

```text
┌────────────────────────────────────┐
│        Selecionar cliente      ✕   │
│────────────────────────────────────│
│ 🔎 Nome, CNPJ ou código            │
│ [______________________________]   │
│                                    │
│ Mercado Central                    │
│ #001245                            │
│ ✓ Ativo • Rio de Janeiro - RJ ( )  │
│────────────────────────────────────│
│ Supermercado Vitória               │
│ #001280                            │
│ ⚠ Bloqueado • Niterói - RJ         │
│ Não pode emitir pedido             │
│────────────────────────────────────│
│ Loja Primavera                     │
│ #001300                            │
│ ○ Inativo • Rio de Janeiro - RJ    │
│ Não pode emitir pedido             │
│                                    │
│ [        SELECIONAR          ]     │
└────────────────────────────────────┘
```

A ação **SELECIONAR** somente ficará habilitada quando um Cliente Ativo estiver marcado.  
Selecionar → retorna para **T09** com o Cliente escolhido.

---

# T09.2 — Selecionar endereço de entrega

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T09.2` |
| Nome | Selecionar endereço de entrega |
| Objetivo | Selecionar o endereço de entrega do pedido. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Seleção de endereço de entrega disponível para o Cliente. |
| Campos obrigatórios | Um endereço deve ser selecionado para prosseguir. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T09. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Retorna para T09 com o endereço selecionado ou sem alterar a seleção quando cancelado. |
| Relação com outras interfaces | T09 |

## Regra

O cliente poderá possuir mais de um endereço.

Exemplos:

- principal;
- entrega;
- filial;
- depósito.

## Textframe

```text
┌────────────────────────────────────┐
│ ‹     Endereço de entrega          │
│                                    │
│ Mercado Central                    │
│                                    │
│ ● Principal                        │
│ Rua Exemplo, 150                   │
│ Centro                             │
│ Rio de Janeiro - RJ                │
│ CEP 20000-000                      │
│────────────────────────────────────│
│ ○ Depósito                         │
│ Rua das Flores, 900                │
│ Zona Norte                         │
│ Rio de Janeiro - RJ                │
│ CEP 21000-000                      │
│────────────────────────────────────│
│                                    │
│ [      USAR ESTE ENDEREÇO      ]   │
└────────────────────────────────────┘
```

Usar este endereço → retorna para **T09** com o endereço selecionado.

---

# M09.3 — Selecionar tabela de preço

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `M09.3` |
| Nome | Selecionar tabela de preço |
| Objetivo | Selecionar a tabela de preço aplicável ao pedido. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Seleção da tabela de preço disponível. |
| Campos obrigatórios | Uma tabela de preço deve ser selecionada para prosseguir. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T09. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Cancelar/fechar retorna à interface que abriu o modal, preservando o contexto anterior. |
| Relação com outras interfaces | T09 |

```text
┌────────────────────────────────────┐
│        Tabela de preço         ✕   │
│────────────────────────────────────│
│ ● Tabela Padrão                    │
│   Vigência atual                   │
│────────────────────────────────────│
│ ○ Atacado                          │
│   Condição especial                │
│────────────────────────────────────│
│ ○ Promocional Outubro              │
│   Válida até 31/10/2026            │
│                                    │
│ [          SELECIONAR          ]   │
└────────────────────────────────────┘
```

Selecionar → retorna para **T09** com a tabela de preço escolhida.

---

# T10 — Pedido / Itens

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T10` |
| Nome | Pedido / Itens |
| Objetivo | Montar e revisar os itens do Pedido de Venda. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Itens, quantidades e edição dos itens do pedido. |
| Campos obrigatórios | O pedido deve possuir ao menos um item válido para avançar. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T07, M10.1, T11. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Volta para T09 preservando o pedido em edição. |
| Relação com outras interfaces | T09, T07, M10.1, T11 |

```text
┌────────────────────────────────────┐
│ ‹        Pedido #NOVO              │
│                                    │
│ ●────────●────────○────────○        │
│ Cliente   Itens    Cond.   Revisão │
│                                    │
│ [      + ADICIONAR PRODUTO     ]   │
│                                    │
│ Produto ABC                        │
│ SKU 000123                         │
│ 10 UN × R$ 25,90                   │
│                          R$ 259,00 │
│ [ − ] 10 [ + ]      [ Editar ]     │
│────────────────────────────────────│
│ Produto XYZ                        │
│ 2 CX × R$ 48,50                    │
│                           R$ 97,00 │
│ [ − ] 2 [ + ]       [ Editar ]     │
│────────────────────────────────────│
│                                    │
│ 12 itens                           │
│ Subtotal                 R$ 356,00 │
│                                    │
│ [          CONTINUAR           ]   │
└────────────────────────────────────┘
```

Adicionar → **T07**

Editar → **M10.1**

Continuar → **T11**

---

# M10.1 — Editar item

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `M10.1` |
| Nome | Editar item |
| Objetivo | Editar quantidade, desconto ou remover um item do pedido em edição. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Quantidade e desconto do item; ação de remoção. |
| Campos obrigatórios | Quantidade válida; desconto sujeito às regras comerciais aplicáveis. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T10. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Cancelar/fechar retorna à interface que abriu o modal, preservando o contexto anterior. |
| Relação com outras interfaces | T10 |

```text
┌────────────────────────────────────┐
│          Editar item           ✕   │
│────────────────────────────────────│
│ Produto ABC                        │
│ SKU 000123                         │
│                                    │
│ Preço unitário                     │
│ R$ 25,90                           │
│                                    │
│ Quantidade                         │
│ [ − ]       10        [ + ]        │
│                                    │
│ Desconto                           │
│ [ 0,00 ] %                         │
│                                    │
│ Preço final                        │
│ R$ 25,90                           │
│                                    │
│ Total                              │
│ R$ 259,00                          │
│                                    │
│ [ REMOVER ITEM ]                   │
│                                    │
│ [        SALVAR ALTERAÇÕES      ]  │
└────────────────────────────────────┘
```

Remover item → remove o item e retorna para **T10**.  
Salvar alterações → aplica quantidade/desconto válidos e retorna para **T10**.

---

# T11 — Pedido / Condições comerciais

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T11` |
| Nome | Pedido / Condições comerciais |
| Objetivo | Definir as condições comerciais do Pedido de Venda. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Forma de pagamento, condição, desconto geral, frete, previsão de entrega, pedido do cliente e observação. |
| Campos obrigatórios | Forma de pagamento e Condição são obrigatórias; Desconto geral, Modalidade de frete, Previsão de entrega, Pedido do cliente e Observação são opcionais nesta baseline, respeitando validações comerciais aplicáveis quando informados. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T12. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Volta para T10 preservando o pedido em edição. |
| Relação com outras interfaces | T10, T12 |

## Campos

- forma de pagamento;
- condição;
- desconto geral;
- modalidade de frete;
- previsão de entrega;
- número do pedido do cliente;
- observação.

## Textframe

```text
┌────────────────────────────────────┐
│ ‹          Condições               │
│                                    │
│ ●────────●────────●────────○        │
│ Cliente   Itens    Cond.   Revisão │
│                                    │
│ Forma de pagamento *               │
│ [ Boleto                       ▼ ] │
│                                    │
│ Condição *                         │
│ [ 28 / 56 dias                 ▼ ] │
│                                    │
│ Desconto geral                     │
│ [ 5,00 ] %                         │
│                                    │
│ Frete                              │
│ [ CIF                          ▼ ] │
│                                    │
│ Previsão de entrega                │
│ [ 20/10/2026                   📅 ]│
│                                    │
│ Pedido do cliente                  │
│ [______________________________]   │
│                                    │
│ Observação                         │
│ ┌────────────────────────────────┐ │
│ │                                │ │
│ └────────────────────────────────┘ │
│                                    │
│ [          CONTINUAR           ]   │
└────────────────────────────────────┘
```

Continuar → **T12**.

---

# T12 — Revisão

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T12` |
| Nome | Revisão |
| Objetivo | Revisar os dados completos do pedido antes da confirmação. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — revisão somente leitura com atalhos de edição. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T09, T09.2, T10, T11, M12.1. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Volta para T11 preservando o pedido em edição. |
| Relação com outras interfaces | T09, T09.2, T10, T11, M12.1 |

```text
┌────────────────────────────────────┐
│ ‹         Revisar Pedido           │
│                                    │
│ ●────────●────────●────────●        │
│ Cliente   Itens    Cond.   Revisão │
│                                    │
│ CLIENTE                        >   │
│ Mercado Central                    │
│────────────────────────────────────│
│ ENTREGA                        >   │
│ Rua Exemplo, 150                   │
│────────────────────────────────────│
│ PRODUTOS                       >   │
│ Produto ABC                        │
│ 10 × R$25,90          R$259,00     │
│                                    │
│ Produto XYZ                        │
│ 2 × R$48,50            R$97,00     │
│────────────────────────────────────│
│ CONDIÇÕES                      >   │
│ Boleto • 28/56 dias                │
│────────────────────────────────────│
│ Subtotal               R$356,00    │
│ Desconto                -R$17,80   │
│ Frete                     R$0,00   │
│                                    │
│ TOTAL                  R$338,20    │
│                                    │
│ [       CONFIRMAR PEDIDO       ]   │
└────────────────────────────────────┘
```

Destinos:

```text
Cliente    → T09
Entrega    → T09.2
Produtos   → T10
Condições  → T11
Confirmar  → M12.1
```

---

# M12.1 — Confirmar pedido

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `M12.1` |
| Nome | Confirmar pedido |
| Objetivo | Solicitar confirmação final antes do envio do Pedido de Venda. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — confirmação do pedido. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T12, T13. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Cancelar/fechar retorna à interface que abriu o modal, preservando o contexto anterior. |
| Relação com outras interfaces | T12, T13 |

```text
┌────────────────────────────────────┐
│        Confirmar pedido?           │
│                                    │
│ Mercado Central                    │
│                                    │
│ 12 itens                           │
│                                    │
│ Total                              │
│ R$ 338,20                          │
│                                    │
│ Após a confirmação o pedido será   │
│ enviado para processamento.        │
│                                    │
│ [ VOLTAR ]        [ CONFIRMAR ]    │
└────────────────────────────────────┘
```

Voltar → **T12**.  
Confirmar → **T13**.

---

# T13 — Pedido confirmado

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T13` |
| Nome | Pedido confirmado |
| Objetivo | Confirmar ao vendedor a criação do pedido e oferecer acesso, compartilhamento ou retorno ao início. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — estado de sucesso do pedido. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T15, T02. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Após sucesso, permite seguir para T15 ou T02. |
| Relação com outras interfaces | T15, T02 |

```text
┌────────────────────────────────────┐
│                                    │
│               ✓                    │
│                                    │
│        Pedido realizado!           │
│                                    │
│             #10549                 │
│                                    │
│ Mercado Central                    │
│                                    │
│ Total                              │
│ R$ 338,20                          │
│                                    │
│ Status                             │
│ ● Enviado                          │
│                                    │
│ [     VISUALIZAR PEDIDO       ]    │
│                                    │
│ [        COMPARTILHAR         ]    │
│                                    │
│          Voltar ao início          │
└────────────────────────────────────┘
```

Visualizar → **T15**

Voltar → **T02**

### Ação externa — Compartilhar pedido

`COMPARTILHAR` deverá abrir o compartilhamento nativo do sistema operacional. O conteúdo compartilhado deverá conter, no mínimo: número do pedido, cliente, valor total e status atual. O sistema deverá permitir que o usuário escolha qualquer aplicativo compatível disponível no dispositivo. Se não houver destino de compartilhamento disponível, a tela deverá permanecer aberta e informar a indisponibilidade.


---

# 17. CONSULTA DE PEDIDOS

# T14 — Pedidos

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T14` |
| Nome | Pedidos |
| Objetivo | Consultar pedidos por busca, filtros e status. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Busca por número/Cliente e filtros via M14.1. |
| Campos obrigatórios | Nenhum campo de busca ou filtro é obrigatório nesta interface. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: M14.1, T15. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | C27 EmptyState deverá ser utilizado quando não houver registros a exibir. |
| Comportamento de retorno | É acessível pela navegação principal; retorno de T15 preserva busca/filtros quando possível. |
| Relação com outras interfaces | M14.1, T15 |

## Destinos

| Ação | Destino |
|---|---|
| Filtros | M14.1 |
| Selecionar pedido | T15 |

```text
┌────────────────────────────────────┐
│            Pedidos                 │
│                                    │
│ ┌────────────────────────────────┐ │
│ │ 🔎 Nº pedido ou cliente        │ │
│ └────────────────────────────────┘ │
│                                    │
│ [ ⚙ Filtros ]                     │
│                                    │
│ [Todos] [Abertos] [Faturados]      │
│                                    │
│ #10549                         >   │
│ Mercado Central                    │
│ R$ 338,20                          │
│ ● Enviado                          │
│────────────────────────────────────│
│ #10548                         >   │
│ Loja Primavera                     │
│ R$ 1.850,00                        │
│ ● Em análise                       │
│────────────────────────────────────│
│ #10547                         >   │
│ Supermercado Vitória               │
│ R$ 950,00                          │
│ ● Faturado                         │
│                                    │
│────────────────────────────────────│
│ Início │ Clientes │ + │ Pedidos │⋯ │
└────────────────────────────────────┘
```

---

# M14.1 — Filtros de pedidos

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `M14.1` |
| Nome | Filtros de pedidos |
| Objetivo | Refinar a consulta de pedidos por período, Cliente, status e valores. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Período, Cliente, status, valor mínimo e valor máximo. |
| Campos obrigatórios | Nenhum filtro é obrigatório. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T14. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Cancelar/fechar retorna à interface que abriu o modal, preservando o contexto anterior. |
| Relação com outras interfaces | T14 |

```text
┌────────────────────────────────────┐
│         Filtrar pedidos        ✕   │
│────────────────────────────────────│
│ Período                            │
│ [ 01/10/2026 ] [ 15/10/2026 ]      │
│                                    │
│ Cliente                            │
│ [ Todos                        ▼ ] │
│                                    │
│ Status                             │
│ [ Todos                        ▼ ] │
│                                    │
│ Valor mínimo                       │
│ [ R$ _________________________ ]   │
│                                    │
│ Valor máximo                       │
│ [ R$ _________________________ ]   │
│                                    │
│ [ LIMPAR ]        [ APLICAR ]      │
└────────────────────────────────────┘
```

Limpar → redefine os filtros no próprio modal.  
Aplicar → fecha M14.1 e atualiza **T14**.

---

# T15 — Detalhes do pedido

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T15` |
| Nome | Detalhes do pedido |
| Objetivo | Consultar o detalhamento e o andamento de um pedido. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — consulta de pedido. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T15.1, T15.2. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Volta para a lista ou contexto de origem preservando o pedido selecionado. |
| Relação com outras interfaces | T15.1, T15.2 |

```text
┌────────────────────────────────────┐
│ ‹         Pedido #10549            │
│                                    │
│ Mercado Central                    │
│ 15/10/2026 • 10:35                 │
│                                    │
│ ● Enviado                          │
│                                    │
│ Andamento                          │
│                                    │
│ ✓ Pedido criado                    │
│ │                                  │
│ ✓ Enviado                          │
│ │                                  │
│ ○ Aprovação                        │
│ │                                  │
│ ○ Faturamento                      │
│ │                                  │
│ ○ Entrega                          │
│────────────────────────────────────│
│ Produto ABC               R$259,00 │
│ Produto XYZ                R$97,00 │
│────────────────────────────────────│
│ Total                     R$338,20 │
│                                    │
│ Condições                      >   │
│ Endereço de entrega            >   │
│                                    │
│ [        COMPARTILHAR         ]    │
└────────────────────────────────────┘
```

Condições → **T15.1**

Endereço → **T15.2**

### Ação externa — Compartilhar pedido

`COMPARTILHAR` deverá abrir o compartilhamento nativo do sistema operacional. O conteúdo compartilhado deverá conter, no mínimo: número do pedido, cliente, valor total e status atual. O sistema deverá permitir que o usuário escolha qualquer aplicativo compatível disponível no dispositivo. Se não houver destino de compartilhamento disponível, a tela deverá permanecer aberta e informar a indisponibilidade.


---

# T15.1 — Condições do pedido

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T15.1` |
| Nome | Condições do pedido |
| Objetivo | Consultar as condições comerciais registradas no pedido. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — consulta das condições do pedido. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Somente navegação de retorno para T15; não possui edição nesta baseline. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Volta para T15. |
| Relação com outras interfaces | T15 |

```text
┌────────────────────────────────────┐
│ ‹     Condições do pedido          │
│                                    │
│ Pedido #10549                      │
│                                    │
│ Forma de pagamento                 │
│ Boleto                             │
│                                    │
│ Condição                           │
│ 28 / 56 dias                       │
│                                    │
│ Tabela de preço                    │
│ Padrão                             │
│                                    │
│ Desconto                           │
│ 5,00%                              │
│                                    │
│ Frete                              │
│ CIF                                │
│                                    │
│ Previsão                           │
│ 20/10/2026                         │
│                                    │
│ Observação                         │
│ Entregar pela manhã.               │
└────────────────────────────────────┘
```

---

# T15.2 — Endereço de entrega

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T15.2` |
| Nome | Endereço de entrega |
| Objetivo | Consultar o endereço de entrega do pedido e permitir abertura no serviço de mapas. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — consulta de endereço de entrega. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | `ABRIR NO MAPA` abre o serviço de mapas padrão; indisponibilidade mantém a tela aberta com mensagem textual. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Volta para T15. |
| Relação com outras interfaces | T15 |

```text
┌────────────────────────────────────┐
│ ‹      Endereço de entrega         │
│                                    │
│ Pedido #10549                      │
│ Mercado Central                    │
│                                    │
│ Rua Exemplo, 150                   │
│ Centro                             │
│ Rio de Janeiro - RJ                │
│ CEP 20000-000                      │
│                                    │
│ Referência                         │
│ Próximo à Praça Central            │
│                                    │
│ ┌────────────────────────────────┐ │
│ │             MAPA               │ │
│ │                                │ │
│ │              ●                 │ │
│ └────────────────────────────────┘ │
│                                    │
│ [        ABRIR NO MAPA        ]    │
└────────────────────────────────────┘
```

### Ação externa — Abrir no mapa

`ABRIR NO MAPA` deverá abrir o aplicativo de mapas padrão do dispositivo com o endereço exibido. Se o sistema operacional solicitar escolha de aplicativo, será utilizado o seletor nativo. Caso nenhum aplicativo ou serviço de mapas esteja disponível, a tela permanecerá aberta e exibirá mensagem textual de indisponibilidade.

---

# 18. AGENDA

# T16 — Agenda

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T16` |
| Nome | Agenda |
| Objetivo | Consultar a agenda de compromissos e visitas do vendedor. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — agenda/lista de compromissos. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T16.1, T16.2. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | C27 EmptyState deverá ser utilizado quando não houver registros a exibir. |
| Comportamento de retorno | É acessível por T17 e por atalhos; retorno preserva o período/posição da agenda quando possível. |
| Relação com outras interfaces | T17, T16.1, T16.2 |

```text
┌────────────────────────────────────┐
│ ‹            Agenda                │
│                                    │
│ ‹      15 OUTUBRO 2026       ›     │
│                                    │
│ Hoje                               │
│                                    │
│ 09:30                              │
│ ● Mercado Central             >    │
│   Visita comercial                 │
│   Rio de Janeiro                   │
│────────────────────────────────────│
│ 11:00                              │
│ ○ Loja Primavera              >    │
│   Prospecção                       │
│   Rio de Janeiro                   │
│────────────────────────────────────│
│ 15:00                              │
│ ○ Supermercado Vitória        >    │
│   Pós-venda                        │
│   Niterói                          │
│                                    │
│                    (+) Nova visita │
└────────────────────────────────────┘
```

Nova visita → **T16.1**

Compromisso → **T16.2**

---

# T16.1 — Agendar visita

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T16.1` |
| Nome | Agendar visita |
| Objetivo | Criar ou reagendar um compromisso de visita. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Cliente/Prospect, data, hora, tipo, objetivo, lembrete e observação. |
| Campos obrigatórios | Cliente/Prospect, Data e Hora são obrigatórios; Tipo, Objetivo, Lembrete e Observação são opcionais nesta baseline. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T16.2. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Cancelar/voltar retorna à origem; salvar abre ou retorna para T16.2. |
| Relação com outras interfaces | T16.2 |

## Campos

- cliente/prospect;
- data;
- hora;
- tipo;
- objetivo;
- lembrete;
- observação.

## Textframe

```text
┌────────────────────────────────────┐
│ ‹         Agendar visita           │
│                                    │
│ Cliente / Prospect *               │
│ [ Selecionar                   🔎 ]│
│                                    │
│ Data *                             │
│ [ 20/10/2026                   📅 ]│
│                                    │
│ Hora *                             │
│ [ 10:00                        🕒 ]│
│                                    │
│ Tipo                               │
│ [ Visita comercial            ▼ ] │
│                                    │
│ Objetivo                           │
│ [______________________________]   │
│                                    │
│ Lembrete                           │
│ [ 30 minutos antes            ▼ ] │
│                                    │
│ Observação                         │
│ [______________________________]   │
│                                    │
│ [         AGENDAR              ]   │
└────────────────────────────────────┘
```

Agendar → salva o compromisso e abre **T16.2**.  
Quando T16.1 for aberta por `Reagendar`, o mesmo botão salva as alterações e retorna para **T16.2** com os dados atualizados.

---

# T16.2 — Compromisso / Visita agendada

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T16.2` |
| Nome | Compromisso / Visita agendada |
| Objetivo | Consultar um compromisso agendado e permitir iniciar, reagendar ou cancelar a visita. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — consulta do compromisso com ações operacionais. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T06, T04.4, T16.1, M16.3. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Volta para T16. |
| Relação com outras interfaces | T16, T06, T04.4, T16.1, M16.3 |

```text
┌────────────────────────────────────┐
│ ‹        Visita agendada           │
│                                    │
│ Mercado Central                    │
│                                    │
│ 20/10/2026                         │
│ 10:00                              │
│                                    │
│ Tipo                               │
│ Visita comercial                   │
│                                    │
│ Objetivo                           │
│ Apresentar nova linha              │
│                                    │
│ Endereço                           │
│ Rua Exemplo, 150               >   │
│                                    │
│ [      INICIAR VISITA         ]    │
│                                    │
│ [        REAGENDAR            ]    │
│                                    │
│        Cancelar visita             │
└────────────────────────────────────┘
```

Iniciar → **T06**, com o Cliente/Prospect e o compromisso pré-selecionados.

Endereço → **T04.4**.

Reagendar → **T16.1 em modo de edição**, carregando os dados atuais do compromisso.

Cancelar visita → **M16.3**.

---

# M16.3 — Confirmar cancelamento da visita

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `M16.3` |
| Nome | Confirmar cancelamento da visita |
| Objetivo | Confirmar o cancelamento de uma visita agendada. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — confirmação de cancelamento. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T16.2, T16, E16.4. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Estados específicos relacionados: E16.4. Estados globais aplicam-se quando pertinentes. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Cancelar/fechar retorna à interface que abriu o modal, preservando o contexto anterior. |
| Relação com outras interfaces | T16.2, T16, E16.4 |

```text
┌────────────────────────────────────┐
│       Cancelar esta visita?        │
│                                    │
│ A visita será mantida no histórico │
│ com status Cancelada.              │
│                                    │
│ [ NÃO CANCELAR ]   [ CANCELAR ]    │
└────────────────────────────────────┘
```

Não cancelar → retorna para **T16.2**.  
Cancelar → altera o status para **Cancelada** e retorna para **T16**.  
Falha ao cancelar → **E16.4**.

---

# E16.4 — Falha ao cancelar visita

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `E16.4` |
| Nome | Falha ao cancelar visita |
| Objetivo | Informar falha ao cancelar a visita e permitir nova tentativa ou retorno. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — estado de erro. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: M16.3, T16.2. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Este registro é um estado específico; aplica também as regras globais de acessibilidade, retorno e mensagens. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Segue as ações de recuperação documentadas neste estado ou retorna automaticamente à interface-base quando a condição for resolvida. |
| Relação com outras interfaces | M16.3, T16.2 |

```text
┌────────────────────────────────────┐
│               ⚠                    │
│                                    │
│ Não foi possível cancelar a visita.│
│ Nenhuma alteração foi aplicada.    │
│                                    │
│ [        TENTAR NOVAMENTE       ]  │
│ [             VOLTAR           ]  │
└────────────────────────────────────┘
```

Tentar novamente → **M16.3**.  
Voltar → **T16.2**.

---

# 19. MAIS / CONFIGURAÇÕES

# T17 — Mais

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T17` |
| Nome | Mais |
| Objetivo | Centralizar perfil, agenda, sincronização, configurações, ajuda, informações do aplicativo e saída. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — menu de navegação. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T17.1, T16, T17.2, T17.3, T17.4, T17.5, M17.6. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | É tela raiz da navegação principal. |
| Relação com outras interfaces | T17.1, T16, T17.2, T17.3, T17.4, T17.5, M17.6 |

```text
┌────────────────────────────────────┐
│              Mais                  │
│                                    │
│           [ FOTO ]                 │
│           Carlos Silva             │
│           Vendedor                 │
│                                    │
│────────────────────────────────────│
│ 👤 Meu perfil                  >   │
│ 📅 Agenda                      >   │
│ ↻ Sincronização                >   │
│ ⚙ Configurações                >   │
│ ? Ajuda                        >   │
│ ℹ Sobre                        >   │
│ ↪ Sair                         >   │
│                                    │
│────────────────────────────────────│
│ Início │ Clientes │ + │ Pedidos │⋯ │
└────────────────────────────────────┘
```

### Destinos

| Item | Destino |
|---|---|
| Meu perfil | T17.1 |
| Agenda | T16 |
| Sincronização | T17.2 |
| Configurações | T17.3 |
| Ajuda | T17.4 |
| Sobre | T17.5 |
| Sair | M17.6 |

---

# T17.1 — Meu perfil

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T17.1` |
| Nome | Meu perfil |
| Objetivo | Consultar os dados do perfil do vendedor. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — dados de perfil somente leitura nesta baseline. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Somente navegação de retorno; perfil é somente leitura nesta baseline. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Volta para T17. |
| Relação com outras interfaces | T17, T02 |

```text
┌────────────────────────────────────┐
│ ‹          Meu perfil              │
│                                    │
│           [ FOTO ]                 │
│                                    │
│ Nome                               │
│ Carlos Silva                       │
│                                    │
│ Código                             │
│ V00025                             │
│                                    │
│ E-mail                             │
│ carlos@empresa.com                 │
│                                    │
│ Telefone                           │
│ (21) 99999-0000                    │
│                                    │
│ Região                             │
│ Rio de Janeiro                     │
└────────────────────────────────────┘
```

---

# T17.2 — Sincronização

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T17.2` |
| Nome | Sincronização |
| Objetivo | Consultar o estado de sincronização e iniciar sincronização manual. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — consulta de sincronização e ação manual. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | `SINCRONIZAR AGORA` → E17.7; sucesso → E17.8; falha → E17.9. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | E17.9 — Falha na sincronização. E17.7 representa processamento e E17.8 representa sucesso; estados globais aplicam-se quando pertinentes. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Volta para T17. |
| Relação com outras interfaces | T17, E17.7, E17.8, E17.9 |

Especialmente importante para vendedor externo.

```text
┌────────────────────────────────────┐
│ ‹        Sincronização             │
│                                    │
│ Status                             │
│ ● Sincronizado                     │
│                                    │
│ Última sincronização               │
│ Hoje às 13:45                      │
│                                    │
│ Clientes                           │
│ ✓ Atualizados                      │
│                                    │
│ Produtos                           │
│ ✓ Atualizados                      │
│                                    │
│ Preços                             │
│ ✓ Atualizados                      │
│                                    │
│ Pedidos pendentes                  │
│ 0                                  │
│                                    │
│ [       SINCRONIZAR AGORA      ]   │
└────────────────────────────────────┘
```

Sincronizar agora → **E17.7**.

---

# E17.7 — Sincronização em andamento

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `E17.7` |
| Nome | Sincronização em andamento |
| Objetivo | Representar uma sincronização manual em andamento. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — estado transitório. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: E17.8, E17.9. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Este registro é um estado específico; aplica também as regras globais de acessibilidade, retorno e mensagens. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Segue as ações de recuperação documentadas neste estado ou retorna automaticamente à interface-base quando a condição for resolvida. |
| Relação com outras interfaces | E17.8, E17.9, T17.2 |

```text
┌────────────────────────────────────┐
│ ‹        Sincronização             │
│                                    │
│               ◌                    │
│                                    │
│       Sincronizando dados...       │
│                                    │
│ Clientes              Em andamento │
│ Produtos              Aguardando   │
│ Preços                Aguardando   │
│ Pedidos pendentes     Aguardando   │
└────────────────────────────────────┘
```

Sucesso → **E17.8**.  
Falha → **E17.9**.

---

# E17.8 — Sincronização concluída

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `E17.8` |
| Nome | Sincronização concluída |
| Objetivo | Informar que a sincronização foi concluída com sucesso. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — estado de sucesso. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T17.2. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Este registro é um estado específico; aplica também as regras globais de acessibilidade, retorno e mensagens. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Segue as ações de recuperação documentadas neste estado ou retorna automaticamente à interface-base quando a condição for resolvida. |
| Relação com outras interfaces | T17.2 |

```text
┌────────────────────────────────────┐
│               ✓                    │
│                                    │
│      Sincronização concluída       │
│                                    │
│ Todos os dados disponíveis foram   │
│ atualizados com sucesso.            │
│                                    │
│ [              OK              ]   │
└────────────────────────────────────┘
```

OK → **T17.2** com data/hora da última sincronização atualizadas.

---

# E17.9 — Falha na sincronização

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `E17.9` |
| Nome | Falha na sincronização |
| Objetivo | Informar falha de sincronização e permitir nova tentativa ou retorno. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — estado de erro. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: E17.7, T17.2. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Este registro é um estado específico; aplica também as regras globais de acessibilidade, retorno e mensagens. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Segue as ações de recuperação documentadas neste estado ou retorna automaticamente à interface-base quando a condição for resolvida. |
| Relação com outras interfaces | E17.7, T17.2 |

```text
┌────────────────────────────────────┐
│               ⚠                    │
│                                    │
│ A sincronização não foi concluída. │
│ Os dados já existentes foram       │
│ preservados.                       │
│                                    │
│ [        TENTAR NOVAMENTE       ]  │
│ [             VOLTAR           ]  │
└────────────────────────────────────┘
```

Tentar novamente → **E17.7**.  
Voltar → **T17.2**.

---

# T17.3 — Configurações

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T17.3` |
| Nome | Configurações |
| Objetivo | Gerenciar preferências operacionais e acessar configurações técnicas e visuais. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Preferências por switches e acessos a configurações relacionadas. |
| Campos obrigatórios | Não há preferência obrigatória; cada switch possui valor persistido. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T00.1, T00.2, T00.3. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Volta para T17. |
| Relação com outras interfaces | T17, T00.1, T00.2, T00.3 |

## Objetivo

Centralizar preferências operacionais do usuário e fornecer acesso às configurações técnicas e visuais da aplicação.

## Destinos

| Item | Destino |
|---|---|
| API de acesso | T00.1 |
| Tema / Aparência | T00.2 |
| Diagnóstico | T00.3 |

## Preferências

Os switches de Notificações, Lembretes de visitas, Sincronização automática e Uso de dados móveis alteram a preferência na própria T17.3 e devem persistir localmente. Quando uma preferência depender de permissão do sistema operacional, a interface deverá informar essa dependência e direcionar o usuário para a configuração do sistema somente quando necessário.

## Textframe

```text
┌────────────────────────────────────┐
│ ‹        Configurações             │
│                                    │
│ PREFERÊNCIAS                       │
│                                    │
│ Notificações                       │
│ [ ON ]                             │
│                                    │
│ Lembretes de visitas               │
│ [ ON ]                             │
│                                    │
│ Sincronização automática           │
│ [ ON ]                             │
│                                    │
│ Usar dados móveis                  │
│ [ ON ]                             │
│────────────────────────────────────│
│ CONEXÃO                            │
│                                    │
│ API de acesso                  >   │
│ ● Conectada                        │
│                                    │
│ Diagnóstico                    >   │
│────────────────────────────────────│
│ APARÊNCIA                          │
│                                    │
│ Tema                           >   │
│ Claro / Escuro                     │
└────────────────────────────────────┘
```

---

# T17.4 — Ajuda

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T17.4` |
| Nome | Ajuda |
| Objetivo | Disponibilizar ajuda contextual e acesso ao suporte oficial por WhatsApp. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — tópicos expansíveis e ação externa de suporte. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Tópicos de ajuda expandem/recolhem inline; `Contatar suporte` abre WhatsApp; fallback web; indisponibilidade gera mensagem textual. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Volta para T17. |
| Relação com outras interfaces | T17 |

```text
┌────────────────────────────────────┐
│ ‹            Ajuda                 │
│                                    │
│ Como criar um pedido?          >   │
│                                    │
│ Como cadastrar um prospect?    >   │
│                                    │
│ Como registrar uma visita?     >   │
│                                    │
│ Problemas de sincronização     >   │
│                                    │
│ Perguntas frequentes           >   │
│                                    │
│ Contatar suporte               >   │
└────────────────────────────────────┘
```

### Comportamento

- os cinco tópicos de ajuda deverão abrir e recolher conteúdo **inline** na própria T17.4, em padrão expansível/accordion, sem criar nova rota;
- apenas um tópico poderá permanecer expandido por vez no mobile para reduzir rolagem excessiva;
- `Contatar suporte` deverá abrir uma conversa no **WhatsApp** com o canal oficial de suporte configurado para o ambiente;
- a mensagem inicial poderá ser pré-preenchida com identificação do aplicativo e versão, sem incluir credenciais, tokens ou dados sensíveis;
- se o aplicativo WhatsApp não estiver instalado, deverá ser tentada a versão web; se nenhum canal estiver disponível, T17.4 permanecerá aberta e exibirá mensagem textual de indisponibilidade.

---

# T17.5 — Sobre

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `T17.5` |
| Nome | Sobre |
| Objetivo | Exibir informações do aplicativo e acesso aos documentos legais. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — informações do aplicativo e links legais. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Política de privacidade e Termos de uso abrem as URLs oficiais no navegador padrão; link não configurado permanece indisponível com motivo textual. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Aplicam-se somente os estados globais pertinentes à natureza da interface, quando houver operação assíncrona ou consulta de dados. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Volta para T17. |
| Relação com outras interfaces | T17 |

```text
┌────────────────────────────────────┐
│ ‹            Sobre                 │
│                                    │
│             [ LOGO ]               │
│                                    │
│               SaOr                 │
│                                    │
│ Versão                             │
│ 1.0.0                              │
│                                    │
│ Ambiente                           │
│ Produção                           │
│                                    │
│ © 2026 RickSoluções                │
│                                    │
│ Política de privacidade        >   │
│ Termos de uso                  >   │
└────────────────────────────────────┘
```

### Documentos legais

- `Política de privacidade` abrirá a URL oficial de privacidade configurada para o ambiente no navegador padrão;
- `Termos de uso` abrirá a URL oficial de termos configurada para o ambiente no navegador padrão;
- os endereços e o conteúdo jurídico não fazem parte da especificação UX deste Documento Mestre e deverão ser fornecidos antes da publicação em produção;
- se uma URL não estiver configurada, a ação deverá permanecer indisponível e informar claramente o motivo, sem navegação para uma página vazia.

---

# M17.6 — Confirmar saída

## Ficha funcional de aceite

| Critério | Definição |
|---|---|
| ID | `M17.6` |
| Nome | Confirmar saída |
| Objetivo | Confirmar o encerramento da sessão do usuário. |
| Informações exibidas | O conteúdo visual e os dados apresentados no textframe e nas subseções desta interface são normativos para esta baseline. |
| Campos | Não se aplica — confirmação de saída. |
| Campos obrigatórios | Não se aplica. |
| Ações e destinos | Ações e destinos estão documentados nesta seção; relações de navegação/estado: T17, T01. |
| Textframe | Presente nesta seção e integrante do aceite funcional. |
| Estados de erro relevantes | Não possui estado de erro próprio; aplicam-se apenas regras globais pertinentes ao encerramento de sessão. |
| Estado vazio | Não se aplica — esta interface não depende de uma lista vazia nesta baseline. |
| Comportamento de retorno | Cancelar/fechar retorna à interface que abriu o modal, preservando o contexto anterior. |
| Relação com outras interfaces | T17, T01 |

```text
┌────────────────────────────────────┐
│            Sair?                   │
│                                    │
│ Deseja realmente encerrar sua      │
│ sessão no SaOr?                    │
│                                    │
│ [ CANCELAR ]           [ SAIR ]    │
└────────────────────────────────────┘
```

Cancelar → retorna para **T17**.  
Sair → encerra a sessão e segue para **T01**.

---

# 20. COMPONENTES REUTILIZÁVEIS

O Figma e a implementação definitiva deverão priorizar componentes compartilhados.

```text
C01  AppHeader
C02  BottomNavigation
C03  PrimaryButton
C04  SecondaryButton
C05  TextButton
C06  TextInput
C07  SearchInput
C08  SelectInput
C09  DateInput
C10  TimeInput
C11  TextArea
C12  Checkbox
C13  Switch
C14  StatusBadge
C15  MetricCard
C16  ClientCard
C17  ProspectCard
C18  ProductCard
C19  OrderCard
C20  VisitCard
C21  QuantitySelector
C22  FilterChip
C23  Stepper
C24  StatusTimeline
C25  Dialog
C26  BottomSheet
C27  EmptyState
C28  ErrorState
C29  LoadingState
C30  SyncStatus
C31  MoneyDisplay
C32  SectionHeader
C33  AddressCard
C34  ContactCard
C35  ThemeSelector
C36  ThemePreview
C37  ConnectionStatus
C38  ApiConfigurationForm
C39  SecretInput
C40  ConnectionTest
C41  DiagnosticsItem
C42  SettingsGroup
C43  SettingsItem
C44  ConnectionBadge
```

## 20.0.1 Comportamentos de componentes que abrem seleção

Para cumprir a regra de completude sem criar rotas artificiais para controles elementares:

- **C08 SelectInput**: abre a lista de opções como dropdown, popover ou bottom sheet responsivo; a seleção atualiza o campo e fecha a lista. Cancelar/fechar mantém o valor anterior. Não cria uma rota T/M própria.
- **C09 DateInput**: abre seletor de data nativo ou componente equivalente sobre a interface atual; confirmar aplica a data e cancelar mantém o valor anterior. Não cria uma rota independente.
- **C10 TimeInput**: abre seletor de horário nativo ou componente equivalente sobre a interface atual; confirmar aplica o horário e cancelar mantém o valor anterior. Não cria uma rota independente.
- **C12 Checkbox** e **C13 Switch**: alteram o valor diretamente na interface atual; quando uma alteração exigir permissão do sistema operacional, a dependência deverá ser informada textualmente.
- componentes de seleção deverão possuir foco visível, rótulo acessível e operação por teclado quando aplicável no dispositivo.

Esses comportamentos são parte da especificação UX. A implementação técnica definitiva dos componentes será definida nas etapas posteriores.

---

# 20.1 DESIGN SYSTEM, TEMAS E ACESSIBILIDADE

O SaOr possuirá dois temas visuais oficiais: **Claro** e **Escuro**.

Os dois temas utilizarão as mesmas telas, componentes, comportamentos, navegação e hierarquia. A diferença será aplicada por meio de tokens visuais.

## Regra obrigatória de acessibilidade

As decisões de cor deverão seguir os critérios da **WCAG 2.2**:

- **AA é o limite mínimo absoluto**;
- texto normal: contraste mínimo de **4,5:1**;
- texto grande: contraste mínimo de **3:1**;
- o objetivo padrão será **AAA** sempre que tecnicamente e visualmente viável;
- texto normal em AAA: **7:1**;
- texto grande em AAA: **4,5:1**;
- componentes e indicadores visuais relevantes deverão possuir contraste não textual mínimo de **3:1** quando aplicável;
- a cor **nunca** poderá ser o único meio para transmitir status, erro, sucesso, seleção, bloqueio ou qualquer informação funcional.

Sempre que um estado utilizar cor, deverá existir também texto, ícone, forma, rótulo ou outro indicador perceptível.

Exemplo:

```text
✓ Aprovado
⚠ Bloqueado
✕ Rejeitado
```

Em vez de depender apenas de verde, amarelo ou vermelho.

Os contrastes abaixo são valores estimados pela fórmula de luminância relativa da WCAG e deverão ser novamente validados na etapa de Design Visual, no Figma e no MVP HTML.

## Tema Claro — tokens cromáticos oficiais iniciais

| Token | HEX | Uso principal | Contraste de referência | Resultado |
|---|---|---|---:|---|
| `background.primary` | `#F8FAFC` | fundo principal | `#111827` sobre `#F8FAFC` ≈ **16,96:1** | AAA |
| `background.secondary` | `#F1F5F9` | áreas secundárias | `#111827` sobre `#F1F5F9` ≈ **16,19:1** | AAA |
| `surface.default` | `#FFFFFF` | cards e formulários | `#111827` sobre `#FFFFFF` ≈ **17,74:1** | AAA |
| `surface.elevated` | `#FFFFFF` | modal/menu | `#111827` sobre `#FFFFFF` ≈ **17,74:1** | AAA |
| `text.primary` | `#111827` | texto principal | sobre `#FFFFFF` ≈ **17,74:1** | AAA |
| `text.secondary` | `#475569` | texto secundário | sobre `#FFFFFF` ≈ **7,58:1** | AAA |
| `text.inverse` | `#FFFFFF` | texto sobre ações escuras | sobre `#004A99` ≈ **8,61:1** | AAA |
| `border.default` | `#64748B` | bordas de controles | contra `#FFFFFF` ≈ **4,76:1** | AA não textual |
| `action.primary` | `#004A99` | botão/ação principal | `#FFFFFF` sobre `#004A99` ≈ **8,61:1** | AAA |
| `action.hover` | `#003B7A` | hover/pressed | `#FFFFFF` sobre `#003B7A` ≈ **11,01:1** | AAA |
| `link.default` | `#004A99` | links | sobre `#FFFFFF` ≈ **8,61:1** | AAA |
| `focus.ring` | `#004A99` | foco visível | contra `#FFFFFF` ≈ **8,61:1** | AA não textual |
| `status.success` | `#166534` | sucesso | `#FFFFFF` sobre `#166534` ≈ **7,13:1** | AAA |
| `status.warning` | `#7C4A03` | aviso | `#FFFFFF` sobre `#7C4A03` ≈ **7,40:1** | AAA |
| `status.error` | `#991B1B` | erro | `#FFFFFF` sobre `#991B1B` ≈ **8,31:1** | AAA |
| `status.info` | `#004A99` | informação | `#FFFFFF` sobre `#004A99` ≈ **8,61:1** | AAA |

### Observação do texto secundário

`#475569` atinge AAA sobre `#FFFFFF` e sobre `#F8FAFC` (aprox. **7,24:1**). Sobre `#F1F5F9`, o contraste cai para aproximadamente **6,92:1**, ainda AA, porém abaixo do alvo AAA. Nessa superfície, deverá ser utilizado `text.primary` quando o conteúdo exigir o padrão AAA.

## Tema Escuro — tokens cromáticos oficiais iniciais

| Token | HEX | Uso principal | Contraste de referência | Resultado |
|---|---|---|---:|---|
| `background.primary` | `#0F1115` | fundo principal | `#F5F7FA` sobre `#0F1115` ≈ **17,61:1** | AAA |
| `background.secondary` | `#131720` | áreas secundárias | `#F5F7FA` sobre `#131720` ≈ **16,71:1** | AAA |
| `surface.default` | `#171A21` | cards e formulários | `#F5F7FA` sobre `#171A21` ≈ **16,22:1** | AAA |
| `surface.elevated` | `#1F2430` | modal/menu | `#F5F7FA` sobre `#1F2430` ≈ **14,46:1** | AAA |
| `text.primary` | `#F5F7FA` | texto principal | sobre `#0F1115` ≈ **17,61:1** | AAA |
| `text.secondary` | `#C7CDD6` | texto secundário | sobre `#1F2430` ≈ **9,70:1** | AAA |
| `text.inverse` | `#0F1115` | texto sobre ações claras | sobre `#8ABEFF` ≈ **9,80:1** | AAA |
| `border.default` | `#64748B` | bordas de controles | contra `#171A21` ≈ **3,66:1** | AA não textual |
| `action.primary` | `#8ABEFF` | botão/ação principal | `#0F1115` sobre `#8ABEFF` ≈ **9,80:1** | AAA |
| `action.hover` | `#A7CAFF` | hover/pressed | `#0F1115` sobre `#A7CAFF` ≈ **11,28:1** | AAA |
| `link.default` | `#8ABEFF` | links | sobre `#0F1115` ≈ **9,80:1** | AAA |
| `focus.ring` | `#8ABEFF` | foco visível | contra `#0F1115` ≈ **9,80:1** | AA não textual |
| `status.success` | `#A7F3D0` | sucesso | contra `#0F1115` ≈ **14,73:1** | AAA |
| `status.warning` | `#FDE68A` | aviso | contra `#0F1115` ≈ **15,17:1** | AAA |
| `status.error` | `#FCA5A5` | erro | contra `#0F1115` ≈ **9,96:1** | AAA |
| `status.info` | `#8ABEFF` | informação | contra `#0F1115` ≈ **9,80:1** | AAA |

## Tokens semânticos oficiais iniciais

```text
background.primary
background.secondary
surface.default
surface.elevated
text.primary
text.secondary
text.inverse
border.default
action.primary
action.hover
link.default
focus.ring
status.success
status.warning
status.error
status.info
```

Os valores acima são os **tokens cromáticos oficiais vigentes nesta versão do Documento Mestre**. Qualquer alteração futura deverá manter, no mínimo, os critérios AA estabelecidos neste documento e deverá ser validada novamente antes de aprovação.

Nenhuma funcionalidade, módulo ou fluxo poderá ser adicionado ou removido em razão de uma decisão puramente visual.

---

# 21. ESTADOS GLOBAIS

Todas as áreas que consultam dados deverão prever estados padrão.

## Carregando

```text
┌────────────────────────────────────┐
│                                    │
│               ◌                    │
│                                    │
│          Carregando...             │
│                                    │
└────────────────────────────────────┘
```

## Lista vazia

```text
┌────────────────────────────────────┐
│              ◯                     │
│                                    │
│       Nenhum registro ainda        │
│                                    │
│ [       CRIAR REGISTRO       ]     │
└────────────────────────────────────┘
```

## Erro

```text
┌────────────────────────────────────┐
│              ⚠                     │
│                                    │
│ Não foi possível carregar os dados │
│                                    │
│ [        TENTAR NOVAMENTE       ]  │
└────────────────────────────────────┘
```

## Sem conexão

```text
┌────────────────────────────────────┐
│ ⚠ Você está offline                │
│ Algumas informações podem estar    │
│ desatualizadas.                    │
└────────────────────────────────────┘
```

## Sessão expirada ou inválida

Quando uma área autenticada detectar que a sessão deixou de ser válida, a operação protegida deverá ser interrompida e o usuário deverá ser informado antes do retorno ao login. A opção `Lembrar-me` não elimina essa regra.

```text
┌────────────────────────────────────┐
│               ⚠                    │
│                                    │
│        Sua sessão expirou.         │
│                                    │
│ Entre novamente para continuar.    │
│                                    │
│ [         IR PARA LOGIN        ]   │
└────────────────────────────────────┘
```

`IR PARA LOGIN` → **T01**. Dados locais já preservados para sincronização não deverão ser descartados exclusivamente pela expiração da sessão.

## Acesso não autorizado

Quando o usuário tentar executar uma ação para a qual não possui autorização:

- se a restrição já for conhecida pela aplicação, a ação deverá permanecer indisponível com explicação textual;
- se a negativa ocorrer durante a operação, a interface atual deverá ser preservada e deverá informar que o usuário não possui autorização;
- a aplicação não deverá simular sucesso nem perder dados de edição por causa da negativa.

```text
┌────────────────────────────────────┐
│               ⚠                    │
│                                    │
│ Você não possui autorização para   │
│ executar esta ação.                │
│                                    │
│ [              OK              ]   │
└────────────────────────────────────┘
```

## Salvando

```text
┌────────────────────────────────────┐
│              ◌                     │
│                                    │
│            Salvando...             │
└────────────────────────────────────┘
```

## Sucesso

```text
┌────────────────────────────────────┐
│              ✓                     │
│                                    │
│        Registro salvo              │
└────────────────────────────────────┘
```

---

# 22. STATUS E CLASSIFICAÇÕES PADRONIZADOS

## Cadastro Comercial

A classificação comercial e a situação operacional são conceitos independentes.

### Classificação comercial

```text
PROSPECT
CLIENTE
```

### Situação operacional

```text
ATIVO
BLOQUEADO
INATIVO
```

### Combinações previstas nesta versão

| Classificação | Situação | Pode emitir pedido? | Regra |
|---|---|---:|---|
| Prospect | Bloqueado | Não | Novo cadastro ainda não aprovado |
| Cliente | Ativo | Sim | Cadastro aprovado e operacional |
| Cliente | Bloqueado | Não | Cliente permanece cliente, mas está impedido de operar |
| Cliente | Inativo | Não | Cliente permanece cliente, porém está inativo |

`Prospect + Ativo` não é uma combinação prevista pela regra atual.

A aprovação cadastral provoca a transição:

```text
PROSPECT + BLOQUEADO
        │
        │ cadastro aprovado
        ▼
CLIENTE + ATIVO
```

Um bloqueio ou inativação posterior **não** altera a classificação de Cliente para Prospect.

## Pedido

```text
Rascunho
Pendente de sincronização
Enviado
Em análise
Aprovado
Separação
Faturado
Em transporte
Entregue
Cancelado
Rejeitado
```

## Visita

```text
Agendada
Em andamento
Concluída
Cancelada
```

## Regra visual dos estados

Status não poderão ser comunicados somente por cor. Todo status deverá possuir pelo menos um rótulo textual e, quando fizer sentido, um ícone ou símbolo adicional.

Exemplos:

```text
✓ Ativo
⚠ Bloqueado
○ Inativo
```

---

# 23. REGRAS DE NAVEGAÇÃO

Toda tela secundária deverá apresentar retorno explícito.

Exemplo:

```text
‹ Tela anterior
```

Nenhuma operação iniciada dentro de um cliente deverá obrigar o vendedor a selecionar novamente aquele cliente.

Exemplo:

```text
T04 Mercado Central
       │
       └── Novo Pedido
                │
                ▼
        T09 Mercado Central
            já selecionado
```

Da mesma forma:

```text
T05.3 Prospect
        │
        └── Registrar visita
                 │
                 ▼
             T06 Prospect
             já selecionado
```

---

# 24. REGRAS DO PEDIDO

Durante o fluxo do pedido, os dados deverão ser preservados ao avançar e retornar entre etapas.

```text
Cliente
 ↓
Produtos
 ↓
Condições
 ↓
Revisão
```

Caso o usuário retorne:

```text
Revisão
  ↓
Produtos
```

os dados das outras etapas não deverão ser descartados.

A implementação deverá permitir um estado de pedido em edição.

---

# 25. USO OFFLINE

Como o usuário estará em campo, o produto deverá ser projetado visualmente considerando perda de conectividade.

Comportamento funcional previsto:

```text
PEDIDO CRIADO
     │
     ├── Online
     │      └── Enviado
     │
     └── Offline
            └── Pendente de sincronização
                     │
                     ▼
               Sincronização
                     │
                     ▼
                   Enviado
```

A implementação técnica será definida no Documento Técnico. Para esta etapa, ficam aprovados os estados funcionais **Online**, **Offline** e **Pendente de sincronização**, bem como a preservação do pedido até que seja possível sincronizá-lo.

Regras funcionais adicionais:

- falha ou rejeição durante a sincronização não deverá apagar o pedido local pendente;
- o item deverá permanecer identificável como pendente e a falha deverá ser apresentada por **E17.9** ou mensagem equivalente no contexto de sincronização;
- se for detectado conflito entre dados locais e remotos, a aplicação **não deverá sobrescrever silenciosamente** nenhum dos lados; o registro local deverá ser preservado e o motivo deverá ser informado ao usuário;
- a estratégia técnica de detecção, versionamento e resolução assistida de conflitos será definida no Documento Técnico sem alterar essas garantias funcionais.

---

# 26. RELACIONAMENTO ENTRE CLIENTE, VISITA E PEDIDO

A estrutura central do produto será:

```text
               CLIENTE
                  │
         ┌────────┴────────┐
         │                 │
         ▼                 ▼
      VISITA             PEDIDO
         │                 ▲
         │                 │
         └─────────────────┘
```

Isso significa que o sistema não deve ser somente um emissor de pedidos.

Ele deverá funcionar como ferramenta de trabalho do vendedor.

---

# 27. MAPA COMPLETO DE DESTINOS

```text
INICIALIZAÇÃO
 ├── E00.9 API não configurada
 │     └── T00.1 Configuração da API
 └── T01 Login

T00 Configurações
 ├── T00.1 API
 ├── T00.2 Aparência
 ├── T00.3 Diagnóstico
 └── M00.5 Restaurar

T01 Login
 ├── T00 Configurações
 ├── T01.1 Recuperar senha
 │     ├── E01.4 Recuperação solicitada
 │     └── E01.5 Falha na recuperação
 └── T02 Home

T02 Home
 ├── T02.1 Notificações
 │     ├── T15 Pedido
 │     └── T16.2 Compromisso / Visita
 ├── T03 Clientes
 ├── T05 Novo Prospect
 ├── T09 Novo Pedido
 ├── T15 Pedido
 ├── T16 Agenda
 └── T17.1 Perfil

T03 Clientes
 ├── M03.1 Filtros
 ├── T04 Cliente
 ├── T05.3 Prospect
 └── T05 Novo Prospect

T04 Cliente
 ├── T04.1 Pedidos
 ├── T04.2 Visitas
 ├── T04.3 Financeiro
 ├── T04.4 Endereço
 ├── T04.5 Cadastro
 ├── T06 Registrar Visita
 └── T09 Novo Pedido

T05 Novo Prospect
 └── T05.1 Endereço
        └── T05.2 Comercial
               └── T05.3 Prospect

T05.3 Prospect
 ├── T04.4 Endereço
 ├── T05.2 Comercial
 ├── T05.4 Histórico
 │     ├── T06.2 Detalhes da visita
 │     └── T06 Nova visita
 └── T06 Registrar Visita

T06 Registrar Visita
 ├── M06.1 Finalizar
 │     └── E06.3 Falha ao finalizar
 └── T09 Pedido

T06.2 Detalhes da Visita
 └── T15 Pedido relacionado

T07 Produtos
 ├── M07.1 Filtros
 ├── T08 Produto
 │     └── T10 Pedido
 └── T10 Pedido

T09 Pedido / Cliente
 ├── M09.1 Cliente
 ├── T09.2 Endereço
 ├── M09.3 Tabela
 └── T10 Itens

T10 Itens
 ├── T07 Produtos
 ├── M10.1 Editar item
 └── T11 Condições

T11 Condições
 └── T12 Revisão

T12 Revisão
 ├── T09 Cliente
 ├── T09.2 Endereço
 ├── T10 Produtos
 ├── T11 Condições
 └── M12.1 Confirmar

M12.1
 └── T13 Sucesso

T13
 ├── T15 Pedido
 ├── Compartilhamento nativo do sistema
 └── T02 Início

T14 Pedidos
 ├── M14.1 Filtros
 └── T15 Pedido

T15 Pedido
 ├── T15.1 Condições
 ├── T15.2 Endereço
 └── Compartilhamento nativo do sistema

T16 Agenda
 ├── T16.1 Agendar
 └── T16.2 Compromisso

T16.2
 ├── T04.4 Endereço
 ├── T06 Iniciar visita
 ├── T16.1 Reagendar em modo de edição
 └── M16.3 Cancelar visita
       └── E16.4 Falha ao cancelar

T17 Mais
 ├── T17.1 Perfil
 ├── T16 Agenda
 ├── T17.2 Sincronização
 │     ├── E17.7 Em andamento
 │     ├── E17.8 Concluída
 │     └── E17.9 Falha
 ├── T17.3 Configurações
 │     ├── T00.1 API
 │     ├── T00.2 Aparência
 │     └── T00.3 Diagnóstico
 ├── T17.4 Ajuda
 │     └── WhatsApp (ação externa de suporte)
 ├── T17.5 Sobre
 │     ├── Política de privacidade (navegador externo)
 │     └── Termos de uso (navegador externo)
 └── M17.6 Sair
```

---

# 28. CRITÉRIO DE ACEITE DE UMA TELA

Antes de uma tela ser considerada definida, deverá possuir:

```text
[ ] ID
[ ] Nome
[ ] Objetivo
[ ] Informações exibidas
[ ] Campos
[ ] Campos obrigatórios
[ ] Ações
[ ] Destino das ações
[ ] Textframe
[ ] Estados de erro relevantes
[ ] Estado vazio quando aplicável
[ ] Comportamento de retorno
[ ] Relação com outras telas
```

## 28.1 Forma de registro do aceite funcional

Cada interface `T`, `M` e `E` possui uma **Ficha funcional de aceite** imediatamente após seu título.

A ficha não substitui o textframe nem as regras específicas da interface. Ela consolida os critérios obrigatórios desta seção e torna explícito quando um item:

- está definido na própria interface;
- utiliza uma regra global;
- utiliza um componente reutilizável;
- não se aplica naquela interface.

A indicação **Não se aplica** somente poderá ser utilizada quando o critério realmente não fizer parte da interface nesta baseline. Ela não poderá ser utilizada para ocultar uma decisão funcional ainda pendente.

Durante a revisão final desta Documentação Mestre, a ficha e o conteúdo detalhado da interface deverão ser avaliados em conjunto.

Depois do aceite funcional, a evolução visual da interface deverá seguir:

```text
Textframe
   ↓
Wireframe conceitual em imagem
   ↓
Design visual em imagem
   ↓
Construção no Figma
   ↓
Navegação no protótipo
   ↓
MVP HTML
```

Somente depois do aceite funcional a tela poderá avançar para a criação do wireframe conceitual.

---

# 29. CRITÉRIO DE ACEITE DO FIGMA

O Figma será construído somente após a aprovação do textframe, do wireframe conceitual e do design visual da interface.

O Figma posteriormente deverá possuir correspondência com este documento.

Exemplo:

```text
Documento             Figma

T01 Login          → Frame / T01_Login
T02 Home           → Frame / T02_Home
T03 Clientes       → Frame / T03_Clientes
M03.1 Filtros      → Frame / M03_1_FiltroClientes
T04 Cliente        → Frame / T04_ClienteResumo
...
```

Isso facilitará posteriormente:

- comunicação com desenvolvimento;
- identificação das rotas;
- organização dos componentes;
- documentação;
- testes;
- implementação definitiva do frontend.

---

# 30. PRÓXIMAS FASES

A sequência oficial do projeto será composta por etapas com **validação obrigatória entre todas elas**.

```text
DOCUMENTO MESTRE / TEXTFRAMES
      │
      ▼
VALIDAÇÃO FUNCIONAL OBRIGATÓRIA
      │
      ▼
WIREFRAME CONCEITUAL EM IMAGEM
      │
      ▼
VALIDAÇÃO DO WIREFRAME OBRIGATÓRIA
      │
      ▼
DESIGN VISUAL DA TELA EM IMAGEM
      │
      ▼
VALIDAÇÃO VISUAL + WCAG OBRIGATÓRIA
      │
      ▼
CONSTRUÇÃO NO FIGMA
      │
      ▼
VALIDAÇÃO DO FIGMA OBRIGATÓRIA
      │
      ▼
PROTÓTIPO NAVEGÁVEL NO FIGMA
      │
      ▼
VALIDAÇÃO DE FLUXOS / JORNADAS OBRIGATÓRIA
      │
      ▼
MAPA / SLIDES DE NAVEGAÇÃO E APRESENTAÇÃO
      │
      ▼
VALIDAÇÃO DA APRESENTAÇÃO OBRIGATÓRIA
      │
      ▼
MVP HTML / CSS / JAVASCRIPT
      │
      ▼
VALIDAÇÃO FUNCIONAL + RESPONSIVA + ACESSIBILIDADE OBRIGATÓRIA
      │
      ▼
DOCUMENTO TÉCNICO DE ARQUITETURA
      │
      ▼
VALIDAÇÃO TÉCNICA OBRIGATÓRIA
      │
      ▼
DEFINIÇÃO DA LINGUAGEM OFICIAL DO BACKEND
E DEMAIS TECNOLOGIAS DEFINITIVAS
      │
      ▼
IMPLEMENTAÇÃO DEFINITIVA
```

Não haverá uma etapa genérica chamada apenas **“Validação de cada tela”**. A validação pertence a cada fase e terá critérios específicos.

## 30.1 Documento Mestre / Textframe

Antes de avançar, deverão ser validados:

- objetivo da interface;
- informações exibidas;
- campos e obrigatoriedade;
- ações;
- destino de todas as ações;
- regras de negócio;
- estados relevantes;
- textframe;
- relação com outras telas.

O resultado deverá estar **APROVADO** para liberar o wireframe.

## 30.2 Wireframe conceitual

O wireframe conceitual será criado em imagem para cada tela, subtela, modal ou estado relevante.

Seu objetivo será validar:

- hierarquia;
- posicionamento;
- proporção;
- agrupamento de informações;
- posição das ações;
- organização dos formulários;
- estrutura de navegação.

O wireframe responderá: **onde cada elemento ficará?**

O wireframe deverá ser validado e aprovado antes da criação do design visual.

## 30.3 Design visual

Após a aprovação do wireframe, será criada uma imagem com o design visual da interface.

Essa etapa definirá:

- aplicação dos temas;
- tipografia;
- cores e tokens oficiais;
- ícones;
- bordas;
- espaçamento;
- cards;
- botões;
- campos;
- estados visuais;
- contraste e acessibilidade WCAG.

O design responderá: **como cada elemento aparecerá?**

A validação visual deverá incluir obrigatoriamente contraste, foco, legibilidade e garantia de que a cor não é o único meio de transmitir informação.

## 30.4 Construção e validação no Figma

Somente após a aprovação do design visual, a interface será construída no Figma utilizando componentes, variantes, tokens e os dois temas.

Antes de avançar para o protótipo navegável, o frame deverá ser validado quanto à fidelidade com o design aprovado e à utilização correta do Design System.

## 30.5 Protótipo navegável no Figma

O protótipo deverá permitir validar jornadas completas e não apenas telas isoladas.

A validação deverá conferir:

- destinos de todas as ações;
- retorno entre telas;
- continuidade do contexto;
- modais e estados;
- fluxos de pedido;
- fluxos de clientes e prospects;
- visitas;
- agenda;
- sincronização;
- configuração e autenticação.

Somente após a aprovação das jornadas poderão ser consolidados os slides e o MVP HTML.

## 30.6 MVP HTML

O MVP em HTML, CSS e JavaScript será iniciado somente depois da validação do protótipo no Figma e dos materiais de apresentação correspondentes.

O objetivo do MVP será verificar o layout e a navegação em uma interface executável, incluindo:

- responsividade;
- comportamento de campos;
- modais;
- navegação;
- troca de tema;
- estados de erro e carregamento;
- interações principais;
- fluxos de pedido;
- fluxos de clientes, prospects, visitas, agenda e sincronização;
- acessibilidade em execução.

O MVP poderá utilizar dados simulados e não definirá o backend definitivo.

O MVP deverá ser validado e aprovado antes da elaboração da arquitetura definitiva.

## 30.7 Documento Técnico de Arquitetura

Depois da validação do MVP HTML será criado um documento técnico separado e detalhado.

Esse documento deverá definir, entre outros pontos:

```text
Linguagem oficial do backend
Framework e versões
Arquitetura
Frontend definitivo
Contrato definitivo da API
Autenticação e autorização
Banco de dados
Persistência
Segurança
Logs
Cache
Integrações
Ambientes
Deploy
Containers, quando aplicável
CI/CD
Monitoramento
Testes
Padrões de desenvolvimento
```

Nenhuma linguagem oficial de backend será considerada definida antes dessa etapa.

O Documento Técnico também estará sujeito a validação obrigatória antes da implementação definitiva.

---

# 31. REGRA PARA ALTERAÇÕES FUTURAS

Sempre que uma funcionalidade nova for identificada, o processo será:

```text
Necessidade
    ↓
Definir regra
    ↓
Adicionar ao Documento Mestre
    ↓
Criar ID da tela/modal/estado
    ↓
Criar ou atualizar textframe
    ↓
VALIDAR E APROVAR
    ↓
Definir navegação
    ↓
Criar ou atualizar wireframe conceitual
    ↓
VALIDAR E APROVAR
    ↓
Criar ou atualizar design visual
    ↓
VALIDAR WCAG E APROVAR
    ↓
Criar ou alterar o Figma
    ↓
VALIDAR E APROVAR
    ↓
Atualizar protótipo navegável
    ↓
VALIDAR FLUXOS E APROVAR
    ↓
Refletir no MVP HTML
    ↓
VALIDAR E APROVAR
```

Nenhuma alteração poderá pular uma validação obrigatória.

Assim, este documento continuará sendo a fonte principal de definição do projeto.

---

# 32. CONTROLE DE EVOLUÇÃO VISUAL

Cada interface deverá ter seu estágio acompanhado durante o projeto.

Estados permitidos para cada etapa:

```text
PENDENTE
EM VALIDAÇÃO
AJUSTES NECESSÁRIOS
APROVADO
```

Modelo resumido de acompanhamento:

| ID | Interface | Textframe | Wireframe | Design | Figma | Protótipo | HTML |
|---|---|---|---|---|---|---|---|
| T00 | Configuração da aplicação | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T00.1 | Configuração da API | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T00.2 | Aparência / Tema | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T00.3 | Diagnóstico de conexão | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| M00.4 | Confirmar alteração da API | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| M00.5 | Restaurar configuração | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| E00.6 | Testando conexão | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| E00.7 | Conexão realizada | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| E00.8 | Falha de conexão | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| E00.9 | API não configurada | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| E00.10 | API indisponível no login | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T01 | Login | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T01.1 | Recuperar senha | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| E01.2 | Login inválido | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| E01.3 | Sem conexão | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| E01.4 | Recuperação solicitada | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| E01.5 | Falha ao solicitar recuperação | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T02 | Início / Dashboard | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T02.1 | Notificações | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T03 | Clientes e Prospects | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| M03.1 | Filtros de clientes | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| E03.2 | Busca sem resultado | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T04 | Cliente — Resumo | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T04.1 | Cliente — Pedidos | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T04.2 | Cliente — Visitas | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T04.3 | Cliente — Financeiro | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T04.4 | Cliente — Endereço | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T04.5 | Cliente — Dados cadastrais | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T05 | Novo Prospect — Dados básicos | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T05.1 | Novo Prospect — Endereço | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T05.2 | Novo Prospect — Informações comerciais | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T05.3 | Prospect — Resumo | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T05.4 | Prospect — Histórico de visitas | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T06 | Registrar visita | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| M06.1 | Finalizar visita | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T06.2 | Detalhes da visita | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| E06.3 | Falha ao finalizar visita | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T07 | Catálogo de produtos | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| M07.1 | Filtros de produtos | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| E07.2 | Produto não encontrado | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T08 | Detalhes do produto | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T09 | Pedido — Cliente | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| M09.1 | Selecionar cliente | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T09.2 | Selecionar endereço | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| M09.3 | Selecionar tabela de preço | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T10 | Pedido — Itens | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| M10.1 | Editar item | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T11 | Pedido — Condições comerciais | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T12 | Pedido — Revisão | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| M12.1 | Confirmar pedido | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T13 | Pedido confirmado | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T14 | Pedidos | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| M14.1 | Filtros de pedidos | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T15 | Detalhes do pedido | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T15.1 | Condições do pedido | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T15.2 | Endereço de entrega | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T16 | Agenda | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T16.1 | Agendar visita | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T16.2 | Compromisso / Visita | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| M16.3 | Confirmar cancelamento da visita | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| E16.4 | Falha ao cancelar visita | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T17 | Mais | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T17.1 | Meu perfil | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T17.2 | Sincronização | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T17.3 | Configurações | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T17.4 | Ajuda | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T17.5 | Sobre | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| M17.6 | Confirmar saída | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| E17.7 | Sincronização em andamento | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| E17.8 | Sincronização concluída | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| E17.9 | Falha na sincronização | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |

A matriz completa deverá ser atualizada conforme os wireframes, designs, frames no Figma, protótipos e páginas HTML forem concluídos.

Uma etapa somente poderá assumir **APROVADO** depois de sua validação obrigatória.

A aprovação de uma etapa libera a execução da etapa imediatamente seguinte. Estados **PENDENTE**, **EM VALIDAÇÃO** ou **AJUSTES NECESSÁRIOS** não liberam avanço.

Nenhuma tela já documentada será removida desse controle sem uma decisão explícita registrada neste Documento Mestre.


## 32.1 Encerramento da etapa Documento Mestre

A versão **1.0 — APROVADO / BASELINE FUNCIONAL** encerra formalmente a etapa de Documentação Mestre.

A validação funcional foi concluída pelo responsável do projeto em **16/10/2026**, com os seguintes critérios atendidos:

```text
[x] todas as interfaces da matriz foram revisadas pelo responsável do projeto
[x] todos os Textframes foram marcados como APROVADO
[x] não existem ações visíveis sem destino ou comportamento documentado
[x] as regras de negócio transversais foram aceitas
[x] a revisão editorial e de nomenclatura foi concluída
[x] o responsável declarou explicitamente a aprovação da baseline funcional
```

A partir desta baseline:

- a **Documentação Mestre / Textframes** está **APROVADA**;
- **Wireframe, Design, Figma, Protótipo e HTML** permanecem **PENDENTE** até suas respectivas etapas;
- a próxima etapa liberada é **Wireframe Conceitual em Imagem**, que também exigirá validação obrigatória antes de qualquer avanço posterior;
- qualquer mudança funcional posterior à baseline deverá seguir o processo formal definido na seção 31 deste documento e no Registro Permanente de Fechamento da Documentação Mestre.

---

# 33. PRINCÍPIO DE PRESERVAÇÃO FUNCIONAL

As decisões de identidade visual, paleta, tema, tipografia ou acabamento não alteram automaticamente o escopo funcional do produto.

O **Pedido de Venda é o núcleo transacional do projeto**, e o projeto continuará contemplando os módulos de apoio necessários ao trabalho do vendedor em campo, incluindo clientes, prospects, visitas, agenda, produtos, informações comerciais, sincronização e demais funções definidas neste Documento Mestre.

