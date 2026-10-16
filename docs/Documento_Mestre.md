# SaOr - Sales Order
## Documento Mestre de UX, Telas e Navegação

**Versão:** 0.6  
**Status:** Em definição  
**Etapa:** Arquitetura funcional + UX + Textframes + Planejamento de Prototipação  
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

## 1.3 Alterações consolidadas na versão 0.5

Esta revisão formaliza:

- a definição de **Prospect** e **Cliente** como classificações do mesmo Cadastro Comercial;
- a regra de conversão de Prospect em Cliente após aprovação cadastral;
- a separação entre classificação comercial e situação operacional;
- a regra de emissão de pedido somente para **Cliente + Ativo**;
- a paleta cromática inicial oficial dos temas Claro e Escuro com valores HEX;
- WCAG 2.2 nível AA como mínimo obrigatório e AAA como objetivo padrão;
- a proibição de utilizar cor como único meio de transmitir informação;
- validação obrigatória em todas as etapas do processo de construção.

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

### Aprovação cadastral

A origem operacional da aprovação — por exemplo, sistema integrado, backoffice ou futuro perfil administrativo — ainda não está definida neste documento e **não deverá ser inventada nesta etapa**.

O Documento Mestre registra apenas a regra de negócio confirmada:

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

O React permanece como referência prevista para a futura implementação do frontend, porém a arquitetura definitiva do frontend e a linguagem oficial do backend serão formalizadas somente no Documento Técnico, após a validação do MVP HTML.

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

A configuração da aplicação é transversal e deverá estar acessível antes e depois da autenticação.

Antes do login, sua finalidade principal será permitir configurar ou corrigir o acesso à API. Depois do login, as mesmas configurações poderão ser acessadas pela área **Mais / Configurações**.

## T00 — Configuração da aplicação

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

### Regras

- credenciais não deverão ser exibidas abertas por padrão;
- valores sensíveis não deverão aparecer em mensagens de erro, logs ou telas de diagnóstico;
- uma alteração de servidor deverá solicitar confirmação;
- o formato definitivo de autenticação será definido posteriormente no Documento Técnico.

---

## T00.2 — Aparência / Tema

### Objetivo

Permitir escolher entre os temas **Claro** e **Escuro**.

### Regras

- o tema selecionado deverá ser persistido localmente;
- o tema deverá ser aplicado antes da renderização da tela de login para evitar troca visual após o carregamento;
- a estrutura e as funcionalidades deverão permanecer idênticas nos dois temas;
- somente os tokens visuais serão alterados.

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
│ │ SaOr                     │ │
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

### Objetivo

Permitir diferenciar problemas de internet, API, autenticação e sincronização.

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

---

## M00.5 — Restaurar configuração

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

---

## E00.6 — Testando conexão

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

---

## E00.7 — Conexão realizada

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

---

## E00.8 — Falha de conexão

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

---

## E00.9 — API não configurada

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

Ver configuração da API → **T00.1**

---

# 10. AUTENTICAÇÃO

# T01 — Login

## Objetivo

Autenticar o vendedor.

## Campos

| Campo | Obrigatório | Regra |
|---|---:|---|
| Usuário/e-mail | Sim | Identificação do usuário |
| Senha | Sim | Campo protegido |
| Lembrar-me | Não | Preservar sessão conforme regra futura |

## Ações

| Ação | Destino |
|---|---|
| Configurações | T00 |
| Entrar | T02 |
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
│            SaOr              │
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

## Objetivo

Solicitar recuperação da senha.

## Campo

- e-mail ou usuário.

## Ações

- Enviar recuperação.
- Voltar ao login.

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

---

# E01.3 — Sem conexão

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

---

# 11. DASHBOARD

# T02 — Início

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
│ Última compra: 10/10/2026          │
│────────────────────────────────────│
│ Supermercado Vitória           >   │
│ #001280                            │
│ Niterói - RJ                       │
│ Última compra: 02/10/2026          │
│                                    │
│                   (+) Novo Prospect│
│────────────────────────────────────│
│ Início │ Clientes │ + │ Pedidos │⋯ │
└────────────────────────────────────┘
```

---

# M03.1 — Filtros de clientes

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
│ □ Sem compras recentes             │
│ □ Somente ativos                   │
│                                    │
│ [ LIMPAR ]       [ APLICAR FILTRO ]│
└────────────────────────────────────┘
```

---

# E03.2 — Busca sem resultado

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

---

# T04 — Cliente / Resumo

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

---

# T04.2 — Cliente / Visitas

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

---

# T04.3 — Cliente / Financeiro

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

---

# T04.5 — Cliente / Dados cadastrais

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

Continuar → **T05.1**

---

# T05.1 — Novo Prospect / Endereço

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

Continuar → **T05.2**

---

# T05.2 — Novo Prospect / Informações comerciais

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

## Textframe

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

Salvar → **T05.3**

---

# T05.3 — Prospect / Resumo

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
- Histórico → **T05.4**.

---

# T05.4 — Prospect / Histórico de visitas

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

Iniciar Pedido → **T09**

Finalizar → **M06.1**

---

# M06.1 — Confirmar finalização da visita

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

# T06.2 — Detalhes da visita

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

---

# 15. PRODUTOS

# T07 — Catálogo

## Destinos

| Ação | Destino |
|---|---|
| Filtros | M07.1 |
| Produto | T08 |
| Adicionar | Adiciona ao pedido |
| Ver pedido | T10 |

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

---

# E07.2 — Produto não encontrado

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

---

# T08 — Produto

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

---

# T09.2 — Selecionar endereço de entrega

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

---

# M09.3 — Selecionar tabela de preço

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

---

# T10 — Pedido / Itens

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

---

# T11 — Pedido / Condições comerciais

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

---

# T12 — Revisão

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

Confirmar → **T13**

---

# T13 — Pedido confirmado

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

---

# 17. CONSULTA DE PEDIDOS

# T14 — Pedidos

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

---

# T15 — Detalhes do pedido

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

---

# T15.1 — Condições do pedido

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

---

# 18. AGENDA

# T16 — Agenda

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

---

# T16.2 — Compromisso / Visita agendada

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

Iniciar → **T06**

Endereço → **T04.4**

---

# 19. MAIS / CONFIGURAÇÕES

# T17 — Mais

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

---

# T17.1 — Meu perfil

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

---

# T17.3 — Configurações

## Objetivo

Centralizar preferências operacionais do usuário e fornecer acesso às configurações técnicas e visuais da aplicação.

## Destinos

| Item | Destino |
|---|---|
| API de acesso | T00.1 |
| Tema / Aparência | T00.2 |
| Diagnóstico | T00.3 |

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

Os itens poderão inicialmente abrir conteúdo interno expansível, sem criar nova rota.

---

# T17.5 — Sobre

```text
┌────────────────────────────────────┐
│ ‹            Sobre                 │
│                                    │
│             [ LOGO ]               │
│                                    │
│           SaOr               │
│                                    │
│ Versão                             │
│ 1.0.0                              │
│                                    │
│ Ambiente                           │
│ Produção                           │
│                                    │
│ © Empresa                          │
│                                    │
│ Política de privacidade        >   │
│ Termos de uso                  >   │
└────────────────────────────────────┘
```

---

# M17.6 — Confirmar saída

```text
┌────────────────────────────────────┐
│            Sair?                   │
│                                    │
│ Deseja realmente encerrar sua      │
│ sessão no SaOr?               │
│                                    │
│ [ CANCELAR ]           [ SAIR ]    │
└────────────────────────────────────┘
```

Sair → **T01**

---

# 20. COMPONENTES REUTILIZÁVEIS

O Figma e posteriormente o React deverão priorizar componentes compartilhados.

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
C44  ThemeProvider
C45  ConnectionBadge
```

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

Os valores acima são os **tokens cromáticos iniciais oficiais da versão 0.5**. Qualquer alteração futura deverá manter, no mínimo, os critérios AA estabelecidos neste documento e deverá ser validada novamente antes de aprovação.

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

Exemplo de comportamento futuro:

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

A definição técnica será feita posteriormente, mas os estados de UX já precisam existir.

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
 └── T02 Home

T02 Home
 ├── T02.1 Notificações
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
 └── T06 Registrar Visita

T06 Registrar Visita
 ├── M06.1 Finalizar
 └── T09 Pedido

T07 Produtos
 ├── M07.1 Filtros
 ├── T08 Produto
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
 └── T02 Início

T14 Pedidos
 ├── M14.1 Filtros
 └── T15 Pedido

T15 Pedido
 ├── T15.1 Condições
 └── T15.2 Endereço

T16 Agenda
 ├── T16.1 Agendar
 └── T16.2 Compromisso

T16.2
 ├── T04.4 Endereço
 └── T06 Iniciar visita

T17 Mais
 ├── T17.1 Perfil
 ├── T16 Agenda
 ├── T17.2 Sincronização
 ├── T17.3 Configurações
 │     ├── T00.1 API
 │     ├── T00.2 Aparência
 │     └── T00.3 Diagnóstico
 ├── T17.4 Ajuda
 ├── T17.5 Sobre
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
- implementação React.

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
| T00 | Configuração da aplicação | Em validação | Pendente | Pendente | Pendente | Pendente | Pendente |
| T01 | Login | Em validação | Pendente | Pendente | Pendente | Pendente | Pendente |
| T01.1 | Recuperar senha | Em validação | Pendente | Pendente | Pendente | Pendente | Pendente |
| T02 | Início / Dashboard | Em validação | Pendente | Pendente | Pendente | Pendente | Pendente |

A matriz completa deverá ser atualizada conforme os wireframes, designs, frames no Figma, protótipos e páginas HTML forem concluídos.

Uma etapa somente poderá assumir **APROVADO** depois de sua validação obrigatória.

A aprovação de uma etapa libera a execução da etapa imediatamente seguinte. Estados **PENDENTE**, **EM VALIDAÇÃO** ou **AJUSTES NECESSÁRIOS** não liberam avanço.

Nenhuma tela já documentada será removida desse controle sem uma decisão explícita registrada neste Documento Mestre.

---

# 33. PRINCÍPIO DE PRESERVAÇÃO FUNCIONAL

As decisões de identidade visual, paleta, tema, tipografia ou acabamento não alteram automaticamente o escopo funcional do produto.

O **Pedido de Venda é o núcleo transacional do projeto**, e o projeto continuará contemplando os módulos de apoio necessários ao trabalho do vendedor em campo, incluindo clientes, prospects, visitas, agenda, produtos, informações comerciais, sincronização e demais funções definidas neste Documento Mestre.

