# SaOr - Sales Order
## Wireframes Conceituais em Imagem — Controle operacional

**Baseline funcional:** `v1.0 — APROVADO / BASELINE FUNCIONAL`  
**Etapa atual:** `Wireframe Conceitual em Imagem`  
**Fonte funcional:** [`docs/Documento_Mestre.md`](../../Documento_Mestre.md)  
**Não regressão funcional:** [`docs/Registro_Fechamento_Documento_Mestre.md`](../../Registro_Fechamento_Documento_Mestre.md)  
**Interfaces:** `71`  
**Variações funcionais obrigatórias:** Claro (`white`) e Escuro (`black`)  
**Viewport lógico oficial:** `360 × 800 px`  
**Canvas técnico das pranchas:** `1280 × 1920 px`  
**Template oficial atualmente vigente:** Modelo C (`white` v02 / `black` v01); arquivos `APROVADO E CONGELADO`, seleção revisável somente por aprovação formal  
**Vigência e histórico das decisões do template:** [`Registro_Controle_Template_Oficial.md`](Registro_Controle_Template_Oficial.md)  
**Padrão visual funcional Mobile vigente:** `Mobile-v02.md` (T00 V2 como fonte visual, sem herança de componentes individuais); seleção independente em [`Registro_Padrao_Visual_Funcional_Mobile.md`](Registro_Padrao_Visual_Funcional_Mobile.md)

---

# 1. Responsabilidade deste documento

Este README é um **inventário e controle operacional**: diretórios, referências físicas, histórico dos modelos A/B/C, identidade dos arquivos, matriz das 71 interfaces, estados agregados e contadores. Ele **não** define o processo normativo de construção nem seleciona um modelo por conta própria.

Autoridades (caminhos relativos à raiz do repositório):

```text
docs/Documento_Mestre.md — fonte de requisitos funcionais
.specs/wireframes/REGRAS-TECNICAS.md — invariantes de representação
.specs/wireframes/PROCESSO-PRANCHA.md — SPEC 1, Prancha do Template
.specs/wireframes/REFERENCIA-TEMPLATE-OFICIAL.md — SPEC 2, referência selecionada
docs/wireframes/images/Registro_Controle_Template_Oficial.md — vigência/histórico/hashes
.specs/wireframes/PROCESSO-TELA-PRANCHA.md — SPEC 3, fluxo funcional
.specs/wireframes/WIREFRAME-TEXT-TELA.md — contrato do texto individual da Tela
```

Este README não altera a baseline funcional nem os hashes do template. Não devem existir regras concorrentes aqui: quando necessário, a seção operacional aponta para a SPEC competente.

---

# 2. Estrutura da etapa

A estrutura física vigente é:

```text
docs/wireframes/images/
├── README.md
├── Registro_Controle_Template_Oficial.md
├── Registro_Padrao_Visual_Funcional_Mobile.md
├── contratos/USO-TEMPLATE-C.md
├── padroes-funcionais/Mobile-v02.md
├── references/
│   ├── Especificação Técnica - Prancha de Trabalho.png
│   ├── white/
│   │   ├── Especificação Técnica do Viewport Mobile.png
│   │   ├── WF-VIEWPORT-360x800-clean.png
│   │   ├── WF-VIEWPORT-360x800-clean_icone-esquerda.png
│   │   └── WF-VIEWPORT-360x800.png
│   ├── black/
│   │   └── WF-VIEWPORT-360x800.png
│   └── templates/
│       ├── white/
│       │   ├── <pranchas-modelo claras>.png
│       │   └── wiframetext/
│       │       └── <mesmo-nome-base>.md
│       └── black/
│           ├── <pranchas-modelo escuras>.png
│           └── wiframetext/
│               └── <mesmo-nome-base>.md
├── white/
│   ├── template/                # Modelo C oficial — arquivos congelados
│   │   ├── WF-TEMPLATE-C_v02.png
│   │   ├── WF-TEMPLATE-C_v02.md
│   │   └── WF-VIEWPORT-360x800.png
│   └── telas/
│       ├── controle/T00-01-01_v01.md, T00-01-01_v02.md
│       ├── wiframetext/T00-01-01_v01.md, T00-01-01_v02.md
│       ├── design/
│       │   ├── 01_Mobile_360x800/       # T00 V1 e V2; Conectada + Desconectada por versão
│       │   ├── 02_Tablet_768x1024/     # reserva para MVP posterior
│       │   ├── 03_Notebook_1366x768/   # reserva para MVP posterior
│       │   └── 04_Desktop_1920x1080/  # reserva para MVP posterior
│       └── pranchas/
│           ├── 01_Mobile_360x800/       # Pranchas e registros de composição T00 V1/V2
│           ├── 02_Tablet_768x1024/     # reserva para MVP posterior
│           ├── 03_Notebook_1366x768/   # reserva para MVP posterior
│           └── 04_Desktop_1920x1080/  # reserva para MVP posterior
└── black/
    ├── template/                # Modelo C oficial — arquivos congelados
    │   ├── WF-TEMPLATE-C_v01.png
    │   ├── WF-TEMPLATE-C_v01.md
    │   └── WF-VIEWPORT-360x800.png
    └── telas/
        ├── controle/T00-01-01_v01.md, T00-01-01_v02.md
        ├── wiframetext/T00-01-01_v01.md, T00-01-01_v02.md
        ├── design/
        │   ├── 01_Mobile_360x800/       # T00 V1 e V2; Conectada + Desconectada por versão
        │   ├── 02_Tablet_768x1024/     # reserva para MVP posterior
        │   ├── 03_Notebook_1366x768/   # reserva para MVP posterior
        │   └── 04_Desktop_1920x1080/  # reserva para MVP posterior
        └── pranchas/
            ├── 01_Mobile_360x800/       # Pranchas e registros de composição T00 V1/V2
            ├── 02_Tablet_768x1024/     # reserva para MVP posterior
            ├── 03_Notebook_1366x768/   # reserva para MVP posterior
            └── 04_Desktop_1920x1080/  # reserva para MVP posterior
```


Separação de responsabilidade:

```text
references/
→ referências técnicas compartilhadas ou específicas por variação

references/templates/white/
→ pranchas-modelo e Wireframe Text da variação clara

references/templates/black/
→ pranchas-modelo e Wireframe Text da variação escura

white/template/ e black/template/
→ conjunto oficial **atualmente vigente** por tema: Prancha C (PNG + Wireframe Text) + Viewport técnico (PNG), todos congelados; NÃO são interfaces funcionais

white/telas/design/01_Mobile_360x800/ e black/telas/design/01_Mobile_360x800/
→ PNGs independentes de Telas Mobile, incluindo estados alternativos; T00 já possui arquivos

white/telas/wiframetext/ e black/telas/wiframetext/
→ TextFrames individuais das Telas, derivados dos PNGs existentes

white/telas/controle/ e black/telas/controle/
→ controles GI-0/GI-1 e decisões específicas por tema

white/telas/pranchas/01_Mobile_360x800/ e black/telas/pranchas/01_Mobile_360x800/
→ PNGs de Prancha de Implementação Mobile (T00 existente) e, em `wiframetext/`, seu registro de composição

02_Tablet_768x1024/, 03_Notebook_1366x768/ e 04_Desktop_1920x1080/
→ somente diretórios de referência reservados a um **MVP posterior**; `.gitkeep` não autoriza produção atual
```

A estrutura anterior baseada em pastas de ciclo de vida não faz mais parte da organização vigente.

A evolução de uma prancha-modelo é registrada no próprio Wireframe Text pelos estados definidos em `.specs/wireframes/PROCESSO-PRANCHA.md`.

## 2.1 Estados de construção das pranchas-modelo

Durante a construção de uma prancha-modelo e do PNG correspondente, somente estes estados podem ser usados:

```text
PENDENTE
EM DEFINIÇÃO
AGUARDANDO APROVAÇÃO
APROVADO E CONGELADO
BLOQUEADO POR GATE ANTERIOR
NÃO APLICÁVEL
```

Os Gates 1, 4 e 5 são técnicos.

Os Gates 2, 3 e 6 exigem aprovação humana explícita.

A produção do PNG usa o mesmo conjunto de estados:

```text
BLOQUEADO POR GATE ANTERIOR
→ Gate 6 ainda não aprovado

PENDENTE
→ Gate 6 aprovado; produção ainda não iniciada

EM DEFINIÇÃO
→ imagem em construção ou correção

AGUARDANDO APROVAÇÃO
→ PNG construído e validado contra o Wireframe Text

APROVADO E CONGELADO
→ imagem aprovada explicitamente e congelada
```

Essa classificação pertence às pranchas-modelo e não substitui os estados da matriz funcional das 71 interfaces.

---

# 3. Referências técnicas e pranchas-modelo

`references/` concentra os artefatos de referência usados na etapa.

## 3.1 Referência neutra compartilhada

Arquivo atualmente existente:

```text
references/Especificação Técnica - Prancha de Trabalho.png
```

Esse PNG mede `1280 × 1920 px` e é fisicamente um canvas branco neutro. Ele serve como referência física de prancha, não como fonte normativa de medidas, regras ou conteúdo. As regras permanecem nas specs canônicas.

## 3.2 Referências específicas por variação

Variação clara:

```text
references/white/Especificação Técnica do Viewport Mobile.png
references/white/WF-VIEWPORT-360x800-clean.png
references/white/WF-VIEWPORT-360x800-clean_icone-esquerda.png
references/white/WF-VIEWPORT-360x800.png
```

Os bitmaps `WF-VIEWPORT-360x800*` medem `360 × 800 px` e representam variações físicas diferentes do mesmo viewport demonstrativo; `WF-VIEWPORT-360x800.png` é a variante gerada com a paleta técnica de `REGRAS-TECNICAS.md`, seção 6 (tabela 6.5). O Wireframe Text específico determina qual arquivo deve ser usado. O `clean.png` permanece preservado; não deve ser removido nem substituído silenciosamente pelo arquivo `_icone-esquerda.png`.

As pranchas-modelo white atuais `WF-TEMPLATE-A_v04`, `WF-TEMPLATE-B_v02` e `WF-TEMPLATE-C_v02` usam `WF-VIEWPORT-360x800.png`.

Variação escura:

```text
references/black/WF-VIEWPORT-360x800.png
```

A pasta `black/` recebe somente referências físicas específicas da variação escura. `WF-VIEWPORT-360x800.png` é o viewport black aprovado, gerado com a tabela 6.6 de `REGRAS-TECNICAS.md`.

Não utilizar um bitmap específico de `white` como referência de `black` por inferência.

As dimensões, cotas, grid e demais invariantes continuam pertencendo às specs canônicas, independentemente da existência de um bitmap específico.

## 3.3 Pranchas-modelo

As pranchas-modelo ficam separadas por variação:

```text
references/templates/white/
references/templates/black/
```

O Wireframe Text de cada prancha-modelo fica dentro da mesma variação:

```text
references/templates/<variação>/wiframetext/<nome>.md
```

A variação registrada no Wireframe Text deve coincidir com a pasta onde o artefato está localizado.

A construção e o acompanhamento de cada prancha-modelo obedecem a:

```text
../../../.specs/wireframes/REGRAS-TECNICAS.md
../../../.specs/wireframes/WIREFRAME-TEXT.md
../../../.specs/wireframes/MONTAGEM-IMAGEM.md
```

Este README não redefine dimensões, cotas ou geometria desses arquivos.

## 3.4 Referências históricas e seleção atualmente vigente

Os artefatos completos dos Modelos A/B/C permanecem em `references/templates/`, em `white` e `black`, conforme inventário na seção 3.3. O histórico não é uma lista de modelos intercambiáveis para nova produção funcional. **A vigência é determinada somente pelo registro genérico**, conforme a SPEC 2:

- [`.specs/wireframes/REFERENCIA-TEMPLATE-OFICIAL.md`](../../../.specs/wireframes/REFERENCIA-TEMPLATE-OFICIAL.md)
- [`Registro_Controle_Template_Oficial.md`](Registro_Controle_Template_Oficial.md)

**Seleção atual registrada em 28/10/2026:** Modelo C, `white` v02 e `black` v01. A/B e versões históricas do C permanecem como histórico/contexto; nenhuma substituição pode ser presumida por imagem, nome ou preferência. A referência de uma saída já aprovada é a **versão exata registrada naquela saída**, mesmo após uma eventual mudança de vigência.

### 3.4.1 Inventário visual contextual aprovado e histórico

As pranchas-modelo ainda podem servir como **referências contextuais de linguagem e acabamento**: densidade documental, hierarquia, cabeçalho, metadados, distribuição de regiões, tratamento cromático integral, contrastes, alinhamento, ritmo e qualidade de apresentação. Essa função **não as promove a modelo vigente** e não autoriza copiar sua geometria para uma interface funcional; a cromia normativa continua definida em `REGRAS-TECNICAS.md` e `MONTAGEM-IMAGEM.md`.

```text
white — conjunto contextual atualizado
references/templates/white/WF-TEMPLATE-A_v04.png
references/templates/white/WF-TEMPLATE-B_v02.png
references/templates/white/WF-TEMPLATE-C_v02.png

black — conjunto contextual atualizado
references/templates/black/WF-TEMPLATE-A_v01.png
references/templates/black/WF-TEMPLATE-B_v01.png
references/templates/black/WF-TEMPLATE-C_v01.png
```

Também permanecem as versões históricas white `A_v01`, `A_v02`, `A_v03`, `B_v01` e `C_v01`, preservadas para rastreabilidade de evolução. `white`/`black` são variações técnicas e cromáticas, **não** autorização para converter elementos em escala de cinza. A imagem contextual nunca se sobrepõe às especificações aprovadas.

## 3.5 Arquivos da referência oficial atualmente vigente

| Tema | Prancha aprovada | Wireframe Text da Prancha aprovada | ViewPort demonstrativo |
|---|---|---|---|
| `white` | `white/template/WF-TEMPLATE-C_v02.png` | `white/template/WF-TEMPLATE-C_v02.md` | `white/template/WF-VIEWPORT-360x800.png` |
| `black` | `black/template/WF-TEMPLATE-C_v01.png` | `black/template/WF-TEMPLATE-C_v01.md` | `black/template/WF-VIEWPORT-360x800.png` |

Os seis arquivos e as seis origens estão preservados. **Caminhos e hashes oficiais devem ser conferidos diretamente no registro genérico**, não inferidos desta tabela de estado. O ViewPort demonstrativo não constitui Tela funcional. A produção individual segue a SPEC 3 e não conta nenhum desses arquivos como saída T/M/E.

---

# 4. Viewport e geometria

Fonte canônica:

```text
../../../.specs/wireframes/REGRAS-TECNICAS.md
../../../.specs/wireframes/PROCESSO-PRANCHA.md
```

Este README não replica valores de viewport, canvas, cotas ou safe area.

---

# 5. Grid e espaçamento

Fonte canônica:

```text
../../../.specs/wireframes/REGRAS-TECNICAS.md
```

---

# 6. Tokens e tipografia técnica

Fonte canônica:

```text
../../../.specs/wireframes/REGRAS-TECNICAS.md
```

---

# 7. Componentes técnicos de representação

Fonte canônica:

```text
../../../.specs/wireframes/REGRAS-TECNICAS.md
```

---

# 8. Bordas, radius, elevação e iconografia

Fonte canônica:

```text
../../../.specs/wireframes/REGRAS-TECNICAS.md
```

---

# 9. Estados técnicos

Fonte canônica:

```text
../../../.specs/wireframes/REGRAS-TECNICAS.md
```

---

# 10. Acessibilidade estrutural

Fonte canônica:

```text
../../../.specs/wireframes/REGRAS-TECNICAS.md
```

O Documento Mestre continua sendo a autoridade para conteúdo e comportamento funcional.

---

# 11. Saídas funcionais Mobile no MVP vigente

Esta seção se aplica somente depois de existir uma prancha-modelo aprovada e congelada para a variação correspondente.

A construção histórica das pranchas-modelo ocorre em `references/templates/` e não deve ser confundida com as saídas funcionais atuais em `white/telas/` e `black/telas/`. **Somente Mobile** `01_Mobile_360x800` integra as entregas do MVP vigente. Tablet, Notebook e Desktop são referências físicas para um MVP posterior, sem pranchas, Telas ou Gates exigíveis agora.


Cada uma das 71 interfaces deve possuir, no mínimo, uma representação Claro em `white/` e uma representação Escuro em `black/`.

```text
Mínimo Claro: 71
Mínimo Escuro: 71
Mínimo funcional: 142
```

O total final pode aumentar por paginação.

## 11.1 Localização e nomenclatura operacional

Nomes, páginas, versões, procedimentos de criação/revisão e separação de pastas são definidos **somente** na [SPEC 3](../../../.specs/wireframes/PROCESSO-TELA-PRANCHA.md), seções 3–8. Para cada ID/tema/página/versão, o registro de GI-0/GI-1 fica em `<tema>/telas/controle/`; o PNG da Tela fica em `<tema>/telas/design/01_Mobile_360x800/`, antes do TextFrame em `<tema>/telas/wiframetext/`. A Prancha de Implementação fica em `<tema>/telas/pranchas/01_Mobile_360x800/` e o registro de composição em `wiframetext/` dessa mesma pasta. **A aprovação visual de uma Prancha não aprova automaticamente os TextFrames ou os estados alternativos da Tela.**

T00 Mobile possui versões `v01` (histórica aprovada) e `v02` (vigente após GV2-06) em ambas as variações, com PNGs principais/alternativos, TextFrames por versão, controles de aprovação e registros de composição. A fonte autoritativa da **vigência funcional** é `Registro_Padrao_Visual_Funcional_Mobile.md`, §5; o template vigente continua em `Registro_Controle_Template_Oficial.md`. T00.1 e demais IDs mantêm seus estados independentes; nenhuma aprovação passa de T00 para eles.

## 11.2 Conteúdo e produção

O conteúdo mínimo, a sequência de inventário GI-0 → PNG visual de Tela → aprovação visual GI-1 → TextFrame derivado do PNG → aprovação documental do conjunto GI-2 → Prancha de Implementação → aprovação GI-4, a paginação, a equivalência white/black e os critérios de exportação pertencem exclusivamente à [SPEC 3](../../../.specs/wireframes/PROCESSO-TELA-PRANCHA.md), ao [contrato textual da Tela](../../../.specs/wireframes/WIREFRAME-TEXT-TELA.md) e ao [Gate funcional GI-0 a GI-4](../../../.specs/wireframes/GATE-IMPLEMENTACAO-TELAS.md). Os requisitos funcionais permanecem no Documento Mestre. Não inferir conteúdo da demonstração de ViewPort ou da Prancha do Template. Os campos já existentes `PÁGINA` e `ETAPA` devem ser preenchidos conforme a SPEC 3; a matriz abaixo permanece agregada por ID/tema, não por página.

---

# 14. Estados de controle das interfaces funcionais

Os estados abaixo pertencem à matriz futura das 71 interfaces e permanecem alinhados ao Documento Mestre.

Eles não são os estados usados para acompanhar a construção das pranchas-modelo.


```text
PENDENTE
EM VALIDAÇÃO
AJUSTES NECESSÁRIOS
APROVADO
```

Silêncio não constitui aprovação. Artefato aprovado fica congelado naquela versão; alteração posterior exige nova versão.

---

# 15. Controle das 71 interfaces

O nome e a especificação funcional de cada ID permanecem exclusivamente no Documento Mestre. Este checklist controla apenas o estado resumido da etapa.

Autoridade operacional:

- `white/` e `black/` contêm os arquivos funcionais produzidos;
- o nome físico de cada arquivo é a fonte de verdade para página atual, total de páginas e versão;
- as colunas `Claro` e `Escuro` registram o estado agregado de cada variação;
- `Status geral` deriva do conjunto completo das duas variações;
- uma interface somente pode ficar `APROVADO` quando todas as páginas necessárias de Claro e Escuro estiverem aprovadas e o Gate GI-4 do conjunto estiver concluído;
- o checklist não deve duplicar versão/paginação já expressas nos nomes dos arquivos.

**Fechamento histórico de T00 V1 — 30/10/2026:** a linha T00 foi originalmente atualizada após conferência física dos quatro PNGs de Tela, dois TextFrames e duas Pranchas, com hashes registrados em `white/telas/controle/T00-01-01_v01.md` e `black/telas/controle/T00-01-01_v01.md`. O responsável autorizou o encerramento (“Pode concluir.”), vinculado aos artefatos identificados, sem inventar datas históricas anteriores.

**Atualização da versão vigente de T00 para V2 — registro de 30/10/2026:** GV2-04 concluiu o GI-2 dos TextFrames V2 identificados por SHA-256; GV2-05 comprovou GI-3 das Pranchas V2 e preservação do Modelo C; GV2-06 formalizou GI-4 e declarou o perfil visual funcional `Mobile-v02.md` como `VIGENTE` no registro genérico de seleção. Os documentos V1 permanecem preservados e a matriz continua agregada por ID/tema, não por versão. **O estado `APROVADO` da linha T00 refere-se agora à V2 vigente**, conforme os controles `white/black/telas/controle/T00-01-01_v02.md` (§§6–8), os registros de composição das Pranchas V2 (§§6–7) e `Registro_Padrao_Visual_Funcional_Mobile.md` (§5). Nenhuma das 70 interfaces restantes ou das resoluções futuras está incluída nessa aprovação.

**Fechamento funcional de T00.1 v01 — GI-4, 31/10/2026:** os PNGs individuais e TextFrames da T00.1 foram aprovados em GI-1/GI-2, com GI-0 documentado nos controles por tema; o GI-3 das Pranchas Mobile White/Black foi registrado como `CONFORME TÉCNICO`, e o responsável aprovou expressamente no GI-4 **cada Prancha final e o conjunto White/Black**. O aceite e os SHA-256 dos PNGs `1280 × 1920` constam nos registros de composição `white/telas/pranchas/01_Mobile_360x800/wiframetext/T00.1-01-01_v01.md` e `black/telas/pranchas/01_Mobile_360x800/wiframetext/T00.1-01-01_v01.md`, §11. A linha agregada de T00.1 passa a `APROVADO` em Claro, Escuro e Status geral. O encerramento limita-se à T00.1 `v01` Mobile: não muda a baseline, a seleção do template Modelo C, o perfil visual Mobile-v02 vigente, as outras interfaces nem os Gates históricos de T00.

**T00.1 v02 — GI-0/GI-1/GI-2 aprovados; GI-3 verificado tecnicamente com ressalva, GI-4 pendente (03/11/2026):** O responsável aprovou os dois TextFrames V2 White/Black anteriormente submetidos, vinculados aos SHA-256 pré-adendo `1ccd67638a248694ac69c2bf814120c3f6fbf084d876531a782fda852840cfba` (White) e `5912df752d5df4d54ce272c340a803d568a876af7fe005931d758569ad98a5b2` (Black), em continuidade às aprovações específicas GI-0/GI-1 dos dez PNGs V2. O aceite GI-2 foi transcrito em adendo posterior nos TextFrames `white/black/telas/wiframetext/T00.1-01-01_v02.md` (§7) e nos controles `white/black/telas/controle/T00.1-01-01_v02.md` (§9), sem mudar os PNGs. As duas Pranchas V2 preexistentes foram inspecionadas e receberam registros técnicos de composição `white/black/telas/pranchas/01_Mobile_360x800/wiframetext/T00.1-01-01_v02.md` (§§1–10); o recorte de ViewPort corresponde exatamente ao PNG principal V2 (288.000 pixels por tema) e não há diferenças fora da máscara de alterações permitidas pelo Modelo C. **Ressalva:** `APROVADO E CONGELADO` já está impresso nas duas imagens de Prancha, mas não substitui decisão humana GI-4 por versão, tema e hash; a ordem histórica original de edição também não pode ser demonstrada somente pelo bitmap. A V2 não deve ser declarada vigente e congelada até a aprovação GI-4 própria das duas Pranchas e do conjunto. A linha agregada `T00.1 = APROVADO` permanece fundamentada na V1 histórica e não foi modificada; os controles e artefatos V1, os PNGs V2, templates e normas permanecem preservados.

**Fechamento da T00.1 v02 — GI-4, 03/11/2026 (evento posterior ao registro de preparação acima):** o responsável confirmou **“Aprovado”** em resposta à solicitação que identificou as duas Pranchas T00.1 v02 pelos hashes, a decisão **individual White/Black e do conjunto**, e o reconhecimento do STATUS `APROVADO E CONGELADO` já impresso. A Prancha White `white/telas/pranchas/01_Mobile_360x800/T00.1-01-01_v02.png` foi aprovada sob SHA-256 `6094b6cdb011c48757c6c23e45c42acd9af8b165e6cd81a2b8c78669e0d24cbb`; a Black `black/telas/pranchas/01_Mobile_360x800/T00.1-01-01_v02.png` sob SHA-256 `7b591ef24dc4b8a962aa454813093c49caba59291ba17bbeee3736a6126d2963`. O registro formal posterior da decisão e a regularização da ocorrência histórica `GI3-STATUS-01` constam na **§11** de `white/telas/pranchas/01_Mobile_360x800/wiframetext/T00.1-01-01_v02.md` e `black/telas/pranchas/01_Mobile_360x800/wiframetext/T00.1-01-01_v02.md`. A documentação de GI-0/GI-1/GI-2 continua válida e a verificação técnica GI-3 permanece registrada, incluindo a limitação não comprovável da sequência original de montagem. **T00.1 v02 é agora a revisão vigente e aprovada** para White/Black; **v01 é histórico aprovado e preservado**. A matriz das 71 interfaces continua agregada e a linha `T00.1 = APROVADO` mantém exatamente seu valor, agora referindo-se à **v02**. A revisão não altera baseline, Modelo C, perfil Mobile-v02 nem outras interfaces; nenhum PNG, TextFrame, template ou norma foi alterado.

**Fechamento da revisão vigente de T00.2 V2 — GI-4, 03/11/2026:** a revisão `v02` da interface `T00.2 — Aparência / Tema` foi aprovada **individualmente para White e Black e como conjunto**, após a aprovação GI-0/GI-1 dos quatro PNGs funcionais v02, GI-2 dos TextFrames v02 e verificação técnica GI-3 das duas Pranchas v02. A decisão humana GI-4 identifica a Prancha White pelo SHA-256 `6f363fb2675d799b4ebaab0c89c67aac53198b4eee60b511e50480d35fdb2e2b` e a Prancha Black pelo SHA-256 `21dbfcf595fd9a568d0aedb469a81aeeaf3fc41880e7f1d97e93274aeb8992f3`, reconhecendo expressamente o STATUS `APROVADO E CONGELADO` já impresso. A aprovação vigente e sua ressalva histórica constam na **§10** dos registros `white/telas/pranchas/01_Mobile_360x800/wiframetext/T00.2-01-01_v02.md` e `black/telas/pranchas/01_Mobile_360x800/wiframetext/T00.2-01-01_v02.md`, associados aos controles `white/black/telas/controle/T00.2-01-01_v02.md` e TextFrames `white/black/telas/wiframetext/T00.2-01-01_v02.md`. A `v01` permanece histórico válido, com decisões e arquivos preservados; não há substituição global de referências nem transferência retroativa de hashes. A linha T00.2 da matriz mantém `APROVADO` para Claro, Escuro e geral, **agora referente à v02 vigente**. O template Modelo C e o perfil funcional `Mobile v02` têm vigências próprias, não alteradas por esta decisão. A condição sem preferência salva (O-01) permanece fora do escopo aprovado; a conclusão refere-se apenas aos wireframes Mobile, não ao software.

**T00.3 v01 — regularização documental GI-2/GI-3, 06/11/2026:** as seis Telas Mobile (`white`/`black`, principal, indisponível e testando) mantêm GI-1 aprovado; os dois TextFrames têm aprovação humana GI-2 registrada em 06/11/2026. Os TextFrames que estavam incorretamente sob `telas/pranchas/01_Mobile_360x800/wiframetext/` foram preservados por cópia integral de bytes nos caminhos canônicos `white/telas/wiframetext/T00.3-01-01_v01.md` (SHA-256 `ad14207bc46a032c4628f59eda81fbdc66b7d6bea6a4c0dc9a0ea604ff7efd21`) e `black/telas/wiframetext/T00.3-01-01_v01.md` (SHA-256 `98a56b491fcc7ac755d8aed3748fffdb0e1a46acf68f52668e78bef3d12f020f`); os diretórios de composição agora contêm os registros próprios GI-3. **GI-3 tecnicamente conforme em cada tema**: ViewPort `[40,272,360,800]`, zero pixels divergentes dos PNGs principais nos 288.000 pixels por tema; regiões fixas do Modelo C preservadas. Pranchas originais sem alterações: White SHA-256 `f4c161fd2c3f2a2c0113aded4f5f9b9efe9059634a15d9eb214532b242e1834b`, Black SHA-256 `8f97cbfead954d56de8a58a72ef620630837b63b6fef82471736384ab9fc2b46`. O STATUS `APROVADO E CONGELADO` já estava impresso; a declaração humana de aprovação visual do resultado foi identificada nos registros de composição, mas **a formalização GI-4 individual por hash para White/Black e do conjunto permanece PENDENTE** conforme GATE §6. A aprovação GI-2 original por hashes pré-adendo está registrada nos TextFrames; os bytes pré-adendo não estão disponíveis separadamente no clone (15), limitação explicitada. Por isso, a linha T00.3 passa de `PENDENTE` a **`EM VALIDAÇÃO`** (não `APROVADO`) para ambos os temas e geral; exigir somente o aceite GI-4 que faltar, sem reexecutar GI-0/GI-1/GI-2 por dedução ou alterar PNGs. Evidências completas: `white/black/telas/controle/T00.3-01-01_v01.md` §13 e `white/black/telas/pranchas/01_Mobile_360x800/wiframetext/T00.3-01-01_v01.md` §§1–8 e verificação GCP.

**Preparação da formalização GI-4 — T00.3 v01, 06/11/2026 (registro posterior):** após a regularização GI-2/GI-3, o responsável autorizou gerar os documentos para concluir o processo. Foram reconfirmados na base `SaOr-main (16).zip` os hashes das Pranchas White `f4c161fd2c3f2a2c0113aded4f5f9b9efe9059634a15d9eb214532b242e1834b` e Black `8f97cbfead954d56de8a58a72ef620630837b63b6fef82471736384ab9fc2b46`, bem como a integridade dos respectivos ViewPorts. A declaração visual de aprovação permanece registrada; a autorização documental atual não contém declaração inequívoca de aprovação GI-4 individual por hash e do conjunto. Os registros de composição White/Black, §9, identificam os objetos submetidos à confirmação. **Não presumir GI-4 concluído**: manter `EM VALIDAÇÃO` nos três campos de T00.3 até a decisão humana final expressa, a transcrição fiel e a validação dos hashes. Nenhum PNG, TextFrame aprovado, template, contrato ou histórico anterior foi alterado nesta preparação.

**Fechamento formal de T00.3 v01 — GI-4, 06/11/2026 (evento posterior à preparação acima):** o responsável aprovou expressamente o GI-4 da Prancha White `white/telas/pranchas/01_Mobile_360x800/T00.3-01-01_v01.png` (SHA-256 `f4c161fd2c3f2a2c0113aded4f5f9b9efe9059634a15d9eb214532b242e1834b`), da Prancha Black `black/telas/pranchas/01_Mobile_360x800/T00.3-01-01_v01.png` (SHA-256 `8f97cbfead954d56de8a58a72ef620630837b63b6fef82471736384ab9fc2b46`) **e do conjunto White/Black**, reconhecendo o STATUS `APROVADO E CONGELADO` já impresso nas duas imagens. A declaração de 06/11/2026 e a data de regularização estão transcritas na **§10** dos registros de composição `white/telas/pranchas/01_Mobile_360x800/wiframetext/T00.3-01-01_v01.md` e `black/telas/pranchas/01_Mobile_360x800/wiframetext/T00.3-01-01_v01.md`. As verificações GI-3 permanecem `CONFORME TECNICAMENTE` (ViewPort de cada Prancha igual ao PNG de Tela aprovado em seus 288.000 pixels; estrutura fixa do Modelo C preservada), e as aprovações GI-0/GI-1/GI-2 permanecem preservadas. A ressalva histórica do STATUS antecipado, a ordem original de montagem não comprovável e o limite dos bytes pré-adendo GI-2 continuam documentados, sem reabrir os Gates já aprovados. **T00.3 v01 Mobile está APROVADA E CONGELADA no processo SPEC 3**, individualmente para White/Black e como conjunto. Somente a linha T00.3 da matriz muda de `EM VALIDAÇÃO` para `APROVADO`; normas, Documento Mestre, PNGs, TextFrames, templates, registros históricos e demais interfaces permanecem intactos.

**M00.5 v01 — GI-2 aprovado, GI-3 conforme, GI-4 pendente (07/11/2026):** Tela Mobile `360 × 800` (modal de confirmação sobre a T00 v02) aprovada em GI-1 e TextFrame em GI-2, para White, Black e conjunto. As Pranchas `1280 × 1920` foram montadas sobre o Modelo C vigente e verificadas: ViewPort idêntico (288.000 de 288.000 pixels) e nenhuma alteração fora das regiões autorizadas. O STATUS impresso é `AGUARDANDO APROVAÇÃO`; **o GI-4 depende de aceite humano expresso por tema, hash e conjunto**. Evidências: `white|black/telas/controle/M00.5-01-01_v01.md` §§12–13 e `white|black/telas/pranchas/01_Mobile_360x800/wiframetext/M00.5-01-01_v01.md`. Divergências restritas à M00.5: ícone, texto E (Formal), subtítulo Light 15 px; o Documento Mestre não foi alterado.

**Fechamento formal de M00.5 v01 — GI-4, 07/11/2026:** o responsável respondeu **"Aprovado"** à solicitação que identificou a Prancha White (SHA-256 `4757b7d3cb357f771b4f9db2f48d76330b2f4eacece01088f13c1ed3ef5d38f1`), a Prancha Black (SHA-256 `6e08820d71441263b1a7d5391756718dac7bfa0fe8ee8f0c54dd5ca706b2bf5c`) e o conjunto. Após o aceite, o STATUS impresso passou a `APROVADO E CONGELADO`; hashes finais: White `918c6d7b1d6232269ed25757c378e1d94c995a90fb23146e6d97e60acbd500cf`, Black `9a3f87fc6db3cb09ce47f230d8e9687c038422b5fab7a9ab2909a21b4a400aff`. A linha M00.5 da matriz passa de `EM VALIDAÇÃO` a **`APROVADO`** nos três campos. Evidências: `white|black/telas/controle/M00.5-01-01_v01.md` §14 e `white|black/telas/pranchas/01_Mobile_360x800/wiframetext/M00.5-01-01_v01.md` §10.

**E00.6 v01 — GI-0 conforme, GI-1 aprovado; GI-2 pendente (08/11/2026):** Tela Mobile `360 × 800` (modal de processamento sobre a T00.1 v02 desfocada, superfície a 75% como na M00.5, sem botões) aprovada em GI-1 para White, Black e conjunto, com a declaração "Aprovado possa gerrar pelo zip." transcrita nos controles. PNGs: White SHA-256 `8d4e4920d163436808e94bbe657bfd37251b230149d789a32c1e76cacb36f2d6`; Black SHA-256 `bb09c8ac09c690f07dda1a885dfe41f8e6ab90e07bbc1a2546fe612778ab79f2`. Diferenças restritas ao E00.6: indicador em anel de progresso (V-01) e quebra automática do texto de apoio (V-02). A ficha funcional e o TextFrame da E00.6 no Documento Mestre permaneceram inalterados. No mesmo commit, ocorreu um ajuste visual no TextFrame ASCII da E00.8, modificando a disposição dos botões e o SHA-256 global do Documento Mestre, sem alterar os requisitos da E00.6. **na data deste parágrafo, TextFrames (GI-2), Pranchas (GI-3) e aceite GI-4 ainda não tinham sido produzidos (ver os parágrafos seguintes)**; a linha E00.6 ficava `EM VALIDAÇÃO` até o GI-4 do conjunto. Evidências: `white|black/telas/controle/E00.6-01-01_v01.md` §§5–8 e §10.

**E00.6 v01 — GI-2 aprovado, GI-3 conforme (08/11/2026):** os TextFrames White (SHA-256 `4b80e066f8f0fa0965a88c8d109fae522929309d73f93e102fb806d3a40c6def`) e Black (SHA-256 `b954e99f4edd50200b7591f3bbf6ba14cab1b164c7e73f72bd56d34e761ab39b`) foram aceitos em GI-2 com a resposta "Aceito.". As Pranchas `1280 × 1920` foram montadas sobre o Modelo C vigente e verificadas: ViewPort idêntico (288.000 de 288.000 pixels) e nenhuma alteração fora das regiões autorizadas. Evidências: `white|black/telas/wiframetext/E00.6-01-01_v01.md` §9 e `white|black/telas/pranchas/01_Mobile_360x800/wiframetext/E00.6-01-01_v01.md`.

**Fechamento formal de E00.6 v01 — GI-4, 08/11/2026:** o responsável respondeu **"Esta aprovado como me enviou."** à solicitação que identificou a Prancha White (SHA-256 `9650bf42440e69b88cefb603748a53e469f475741f3cf766ef234c0d9ea45d52`), a Prancha Black (SHA-256 `ec3bc9d74a4a7f57ad0292371395954599d73bf56526a1c5a86522a91185e4fa`) e o conjunto. Após o aceite, o STATUS impresso passou a `APROVADO E CONGELADO`; hashes finais: White `024accbdeb3d255c2412a2af4641fe93b2608e50839cadc7a426a6a2815cf00e`, Black `3eb71a57300c7d66cc79aa8a990c288a1f679eeabe60bb7bdb11fe32c817ade3`. Em seguida, às 10:33, o responsável declarou: **"Aprovo expressamente o GI-4 da E00.6 v01, individualmente para a Prancha White (SHA-256 `024accbdeb3d255c2412a2af4641fe93b2608e50839cadc7a426a6a2815cf00e`) e para a Prancha Black (SHA-256 `3eb71a57300c7d66cc79aa8a990c288a1f679eeabe60bb7bdb11fe32c817ade3`), bem como para o conjunto White/Black. Reconheço o STATUS `APROVADO E CONGELADO` já impresso. Autorizo atualizar exclusivamente os dois registros de composição e o README operacional para concluir GI-4, entregando um único ZIP local."** A linha E00.6 da matriz passa de `EM VALIDAÇÃO` a **`APROVADO`** nos três campos. Evidências: `white|black/telas/controle/E00.6-01-01_v01.md` §10 e `white|black/telas/pranchas/01_Mobile_360x800/wiframetext/E00.6-01-01_v01.md` §10.

**E00.7 v01 — GI-0 aprovado, GI-1 aprovado, GI-2 aprovado, GI-3 conforme, GI-4 aprovado (08/11/2026):** Tela Mobile `360 × 800` (modal de resultado do teste de conexão sobre a T00.1 v02 desfocada, superfície a 75% como na M00.5 e na E00.6) com **quatro estados por tema**: principal `online` (textos do Documento Mestre) e auxiliares `offline`, `instavel` e `nao-verificado`, por decisão do responsável (D-03). O bloco `Status` do textframe do Documento Mestre **não é representado** (D-04) e **todas as cores vêm das tabelas 6.5/6.6 das regras técnicas, sem paleta nova** (D-06; o fundo do ícone usa `SURFACE-ALT`). O GI-1 foi aceito com a resposta "Com isto pode ralizar a entrega" (D-07), transcrita nos controles junto com a instrução de não registrar histórico de hashes durante a montagem da v01. PNGs White: `online` `b06439c042a1a112f5fcac4f7f283f9e68b3aa7a3c0d1bdfd40ca6e9e6d212e1`, `offline` `bd094e90153c0868daa16cfaffdab0307e5b4f26e5ac23d87fddc0022b51197d`, `instavel` `59e7c7589182f659f63e450fbae062ce1f95e74ddb4b177174a4731799f1ea70`, `nao-verificado` `71e3ecfdef6fa51d5f2e54be83ada2c231a9a668c6a3e6d5e46783042c05eaf7`. PNGs Black: `online` `409a3fdfeab2212c27c00b63ea6ed106fd5c2ea4d14cb8a61b85e66fdb2d595b`, `offline` `ec23ceeb536caa24b047e77de58c1e2d4d4458d3dd073f2ad48c4ee9c1e5abb9`, `instavel` `eeaa7c3badf547255191879a9ab31f69b3e81e079945f98b611d8828fad487ae`, `nao-verificado` `2a2a9324a04ac3fa0b65c08a72518f6314347f4d376ea25e5098c0d08a5bb6a4`. TextFrames (GI-2) submetidos para aceite: White SHA-256 `017214fb2de246d2cb2d6f3f3105c7b60cd6c09eefa14cccd816e616d12a9bd7` e Black SHA-256 `33d8c38323f39c7c9bed0e2da49f326fbda10ff469ce71f7cd55ad9c70b6a709`; controles GI-0/GI-1 vinculados: White `77ff2d21f3a61959bc2cba258a848466f8fce8143ed368a96fb42b0a72f447a4` e Black `cb0423461f99016ff2d7d1e33d44f64f7c9da0e9228b53533f89d164b5bd83c9`. Diferenças restritas à E00.7: V-01 (Status não representado), V-02 (ícone em círculo no lugar de `✓`) e V-03 (estados auxiliares fora do Documento Mestre, em parte sobrepostos à E00.8); o Documento Mestre não foi alterado. O GI-2 foi aceito com a resposta "Aceito." (08/11/2026), que confirmou também as pendências L-01 (textos e condições dos estados auxiliares) e L-02 (destino do OK nos estados auxiliares); o registro está no TextFrame §9.1 e no Controle §9.2 de cada tema, e os TextFrames/controles atuais têm bytes diferentes dos submetidos devido aos registros de aceite e à regularização editorial posterior autorizada; o snapshot dos seis Markdown regularizados recebeu aceite humano específico posterior, distinto do aceite original dos objetos GI-0 a GI-4. GI-3: Pranchas 1280×1920 montadas sobre cópias do Modelo C (White v02, Black v01) com o PNG `online` no ViewPort 1:1 (0 divergências em 288,000 pixels), STATUS final impresso `APROVADO E CONGELADO`; White SHA-256 `ac43c453f0b3b8c7812137b444cb1afd704ae1e89c0ea0cce89965aa87ab01ee` (final; submetida `7b999988c43eac28546454933134549d1b26283e5e2b334d3b3345cc19b1fe5d`), Black SHA-256 `ae7fb2a49060db5c2ac3f038fd8e5de6a1754ea72a00206c37f4057a42f5f400` (final; submetida `6e7e2410aaeebe67e1bba7f30e51f51b38020c9ac5b78e1938cd144949837c88`); registros em `white|black/telas/pranchas/01_Mobile_360x800/wiframetext/E00.7-01-01_v01.md`. O GI-4 foi aprovado com a resposta "Aprovado" (08/11/2026) para as duas Pranchas e o conjunto (registro de composição §10.2); em seguida o responsável confirmou, em 08/11/2026 (12:18), as declarações formais "Aprovo expressamente" do GI-0, do GI-2 e do GI-4 ("Confirmo as três declarações acima"), transcritas no Controle §6.2 e §9.2, no TextFrame §9.1 e no registro de composição §10.4 de cada tema; a linha E00.7 passa a `APROVADO`. Hashes físicos anteriores à regularização editorial, após os registros de aceite (08/11/2026): White: TextFrame `836f2e451c392edd8ae8d93027e87875092d7a2521697c6de1c5f2828b34baff`, Controle `e06488ccdced6e71eb62440af623fd0135eb278c4e8737d031e759f75afcc111`, registro de composição `b4d4abc0a63c18af50ea238debb629e544337b8b8cdbde520777e6ec3af8c41b`; Black: TextFrame `4101a40b8a01b62c43060fbd91a5c7e579291b6a91a5f0f4128a7ab717b3e0a8`, Controle `e5c21d111a73bc7e542731540d9b726eecabf6edb521f0bc4fac9b5de5b5601d`, registro de composição `8d423180f82eb9dba6f148e6bfe798c316afec0776e049e9749d64a05ff4204a`. Hashes do snapshot regularizado em 08/11/2026 e posteriormente aceito (versão anterior à inclusão deste registro de aceite): White: TextFrame `43cecaca465660d425678b426d2f2fdcffa4ade9f9ff18f2d1a2599f0ad7baab`, Controle `7f845b9db30ba965e1bb01523dbbb1599f37837c8be24418e987ab71ded7bb19`, Composição `c96da26cc26d3f87e414db0fe8ccd315eb80ede9cd88122bfcdd64aac2b58c95`; Black: TextFrame `f00479ec3a59da5f024381aae8363e35a136526722a6b4cfac61db27fe552da6`, Controle `c8409c550c704897e3f4eb1f4a1434e6fec263cfa2ed7d4b5a7b26cb2c9bd0c2`, Composição `e80b6a750523e73b6ec1cf4d8eaaab89c089d1d9c937b042a0bf12fae184a6c2`. Os hashes de submissão citados acima identificam as versões aprovadas; cada documento não registra o próprio hash. Evidências: `white|black/telas/controle/E00.7-01-01_v01.md` §§5–9 e §10; `white|black/telas/wiframetext/E00.7-01-01_v01.md`.


**E00.7 — consolidação do aceite editorial (08/11/2026):** após a entrega do pacote de regularização dos seis documentos Markdown White/Black, o responsável declarou literalmente **"Viladado e aceito as mudanças."**. A aprovação refere-se aos seis snapshots documentais de SHA-256 registrados no parágrafo anterior; é independente dos aceites humanos originais GI-0, GI-1, GI-2 e GI-4, cujos objetos e hashes históricos permanecem preservados. Após a incorporação e a verificação física do clone local atualizado, à proposta específica de registrar esse aceite e atualizar os hashes decorrentes sem reabrir Gates visuais, respondeu literalmente **"Autorizado a realizar a conclusão."**. As alterações pós-aceite executadas nessa autorização consistem exclusivamente no registro documental da decisão e na atualização de referências; não modificam PNGs, Pranchas, templates nem Documento Mestre.

**E00.7 — hashes físicos vigentes após o registro documental autorizado (08/11/2026):** White: Controle `d8eb7ab4e64ff9c92638c8fd751b4e31eb630b480a6b49e05c6b5d727078c443`, TextFrame `9840789bd52b7d5bb70cee9d2d12d2aef498b9710249683f060832c3f75c6eea`, Composição `217894b14480d8578631be16e127d0b674d32ac5c95e3fe6081554a50d6254b3`; Black: Controle `a0309d96707fca3f0431ccf8e2fd9586647b49e3ae936809509c8e2732d9b85f`, TextFrame `2e516d3f60e48ccfe6657cd4debe44f28deceabd88d5837d31785d2619f5dea2`, Composição `e3d404f18a29d3d8c2bb0018714a866da62e1c6a6e49d6ba77a0e2fe2720e8df`. Os seis hashes anteriores, descritos acima, identificam os bytes efetivamente aceitos antes da inserção do registro; os hashes desta linha identificam os novos bytes físicos com a decisão já incorporada. A linha E00.7 da matriz permanece `APROVADO` nos dois temas e no conjunto, sem reabrir Gates visuais.

**E00.8 v01 — GI-0 aprovado, GI-1 aprovado, GI-2 aprovado, GI-3 conforme, GI-4 aprovado (08/11/2026):** Tela Mobile `360 × 800` (modal de falha de conexão sobre a T00.1 v02 desfocada, superfície a 75% como na M00.5, na E00.6 e na E00.7) com estado único, os textos do Documento Mestre e dois botões lado a lado (`EDITAR API` em texto à esquerda e `TESTAR NOVAMENTE` preenchido à direita, por decisão do responsável, D-02); linhas adicionais foram testadas e descartadas (D-04). Diferenças restritas à E00.8: V-01 (ordem e hierarquia dos botões), V-02 (ícone `warning_amber` de 28 px em círculo no lugar de `⚠`) e V-03 (rótulos dos botões em 14 px); o Documento Mestre não foi alterado. Todas as cores vêm das tabelas 6.5/6.6 das regras técnicas. PNGs: White SHA-256 `203330f8ffec77e6e7765849c523f62559004d645cc5e9471775cf7b7de17335`; Black SHA-256 `13964cb9afe8ba36fed0d40a37ec77442dc5aeefd989c30dd02447d048719e63`. TextFrames submetidos ao GI-2: White `d6e8c10b4d61976e18a3555d6e193759732c30a2fe8ae47f7199a1e66fefe3ef`, Black `7e233b71fc809829efed566b8b3582cec14181e2ef7b499cf1873ea70bb77591`; hashes físicos vigentes após o registro do aceite: White TextFrame `ab83b72fad6fdd73d45ea99ef8f54f972cfdbb9ec283b686f9686acb8c1ddb72`, Controle `72515a19e30950a81306fba9d7b87a040f767c16de79f4a774e8aef88df52cdd`; Black TextFrame `bbc2ac04ea0308b26741187abbae21d4f9013fef05556614cbc4eee5b494f65f`, Controle `e1a0142105fee63aeebb18c1f4be5d4d7f8b361afd80d0e38d9e2df3d163f6d4`. GI-3: Pranchas `1280 × 1920` montadas sobre cópias do Modelo C (White v02, Black v01) com o PNG da Tela no ViewPort 1:1 (0 divergências em 288,000 pixels) e 0 pixels alterados fora das regiões autorizadas. GI-4: Pranchas submetidas (STATUS AGUARDANDO APROVAÇÃO): White `89e7d40e2e668121b1c48815437abe36f416c701f8a51b296d9d965379cb9168`, Black `962c700a79f1303451df685bce96e3aa3b21c79e8beab75c7fcea2fdf2bd1505`; Pranchas finais (STATUS APROVADO E CONGELADO): White `65fbb119481f37ae1fffa4b0cb7559a48595211b773edb52f678f8a914dcb0dc`, Black `972bd05de41a9ee4a277017b6e19679c4ffd8567343a626a7bb1c38a763ac86c`; registros em `white|black/telas/pranchas/01_Mobile_360x800/wiframetext/E00.8-01-01_v01.md` §10. As declarações "Aprovo expressamente" de GI-0, GI-2 e GI-4 estão transcritas no Controle §6.2 e §9.2, no TextFrame §9.1 e no registro de composição §10.4 de cada tema. A linha E00.8 da matriz é `APROVADO`. Evidências: `white|black/telas/controle/E00.8-01-01_v01.md` §§5–10, `white|black/telas/wiframetext/E00.8-01-01_v01.md` §9 e os registros de composição.

**E00.9 v01 — GI-0 aprovado, GI-1 aprovado, GI-2 aprovado, GI-3 conforme, GI-4 aprovado (09/11/2026):** Tela Mobile `360 × 800` (modal sobre a T00.1 v02 desfocada, superfície a 75% como na M00.5, na E00.6, na E00.7 e na E00.8) com estado único, o título e o botão `CONFIGURAR AGORA` do Documento Mestre, texto de apoio escolhido pelo responsável (sugestão G2, V-01) e ícone `settings` de 28 px em círculo no lugar de `⚙` (V-02); sem botão secundário e sem `X`. **GI-1:** o responsável respondeu **"Aprovado."** (09:53) à apresentação das imagens com o texto G2, registrado como aceite visual com a ressalva L-02. PNGs aprovados: White SHA-256 `ea208c1f403aa30bb0638a3222a0350f8d32bd1254f7cb48c84837409fae02ed`; Black SHA-256 `3fd30aa061116389053e1fd4f5694992b35eabdf40b4e6b73197c22d50a17098`. **GI-0:** declaração das 10:35: **"Aprovo expressamente o GI-0 da E00.9 v01, para os temas White e Black, conforme os respectivos controles documentais publicados no repositório, confirmando as pendências L-04 e L-08."** **GI-2:** a declaração das 10:35 citava prefixos de hash que não correspondiam aos TextFrames entregues (erro do assistente na redação proposta) e não foi aplicada (Controle L-09, resolvida). Às 10:44 o responsável declarou: **"Aprovo expressamente o GI-2 da E00.9 v01, para os conjuntos PNG + TextFrame White e Black"**, vinculando os PNGs acima e os TextFrames submetidos White SHA-256 `13f32cb0ae11425d9ec6ebf19e318d6f641bfa878ebac8af04db58b4af48514f` e Black SHA-256 `460bc574f5c0ca554d85edcb9a3b87ec6fad9adf4adc9552baaa1b7d056caa01`, e confirmando as pendências L-01, L-02, L-03 e L-07 (Controle D-09). Hashes físicos vigentes na consolidação documental de 09/11/2026: TextFrame White `cd6860b8ed41b4c7404985358848e35dc2e370cc0a94d0467672980a822c712c`, Controle White `3fb4a4bae73d160ee73b46fc73198a865840a4578e04ae15e841eec51110b13d`; TextFrame Black `38a357c421647556906e6fbdbfc9450b35379f925b6187b44a4b384300ed5e8a`, Controle Black `f2fc1f34d5427ef104026d16ab34f655449753bf8aa7b17265d8129320ecbce6`. **GI-3:** repetido formalmente após o GI-2, em instância limpa: ViewPort 1:1 com 0 divergências em 288.000 pixels por tema; CONFORME TECNICAMENTE, com a ressalva histórica de que a montagem precedeu o aceite do GI-2 (L-08 regularizada). **GI-4:** às 10:59 o responsável declarou: **"Aprovo expressamente o GI-4 da E00.9 v01, para as Pranchas White SHA-256 `89cfac13c35c3d7b9d5fa9dad4cc9c1b65839868ed1587f4d4d833f2b9c3b246` e Black SHA-256 `195e43710a1c45da1155e604b8b2e5256ecf7b469b839c10f955b4474c6e164e`, vinculadas aos PNGs aprovados no GI-2 e à conformidade técnica do GI-3, confirmando as pendências L-03, L-04, L-05 e L-06 como ressalvas."** Pranchas submetidas (STATUS AGUARDANDO APROVAÇÃO): White `89cfac13c35c3d7b9d5fa9dad4cc9c1b65839868ed1587f4d4d833f2b9c3b246`, Black `195e43710a1c45da1155e604b8b2e5256ecf7b469b839c10f955b4474c6e164e`; Pranchas finais (STATUS APROVADO E CONGELADO, única diferença: bloco STATUS): White `7e0a1e4c14459496fe19c7aee35c4914a6d5de1fd53cb8c857147f94a12c3749`, Black `6508ff37e2139afda5cfbb9c5dca7b618e4a205814fd38edd8471fdd54c0314f`. **Confirmação coletiva GI-4 (09/11/2026):** o responsável confirmou expressamente que a D-10 também abrange o conjunto White/Black, além das Pranchas individuais (Composições §10.4), sem nova versão visual. Registros de composição (hashes físicos): White `f90cf0e0bbd522ab4e6869dcd9385daf9ce8d11bb0bb0c59775d4bed52b6ac8d`, Black `6beabac3930c13ff9274800498378967233d1bd2566908ab3fa3ed3125403763`; as declarações de GI-0, GI-2 e GI-4 estão transcritas no Controle §6.2, §9.2 e D-08 a D-10, no TextFrame §9.1 e no registro de composição §10.4. Ressalvas abertas (Controle §5.3): L-03 (pixels de reamostragem fora da faixa dos tokens nos PNGs aprovados), L-04 (hash do Documento Mestre diferente do registrado na E00.8), L-05 e L-06. O Documento Mestre não foi alterado. A linha E00.9 da matriz é **`APROVADO`** nos três campos. Evidências: `white|black/telas/controle/E00.9-01-01_v01.md` §§5–10, `white|black/telas/wiframetext/E00.9-01-01_v01.md` §§8–9 e `white|black/telas/pranchas/01_Mobile_360x800/wiframetext/E00.9-01-01_v01.md` §§5 e 10.

**T01 v01 — GI-0 aprovado (11/11/2026, 10:04; declaração explícita D-T01-08, 10:50), GI-1 aprovado (D-T01-07, 10:45), GI-2 aprovado (D-T01-10, 10:57), GI-3 conforme e GI-4 aprovado (D-T01-11, 11:05):** Tela Mobile `360 × 800` de Login com seis estados (principal, foco, erro, senha visível, Lembrar-me marcado e API desconectada), em White e Black, com as decisões D-T01-01 a D-T01-10 registradas nos controles. No GI-4 o responsável respondeu **"Aprovo com esta frase"** para "Aprovo expressamente o GI-4 da T01 v01, para os temas White e Black, conforme as Pranchas publicadas." e "Autorizo, se GI-4 aprovado" para atualizar esta linha e gerar o ZIP final (D-T01-11). Hashes das Pranchas submetidas: White `27e1acdf1b8f2cf2230160395061fae1145bd034ebe1e93b9c18ee937e5048a8`; Black `02252381baaa9d2a922275a7745b3bd051d21b587718a6ccc6ac97e9f287897d`. Hashes das Pranchas finais (STATUS APROVADO E CONGELADO, somente a região do STATUS alterada): White `cf053b6813bfa7df9d2a411f1364019bf0ee4e0b89a3a5870c434f5159f29ca7`; Black `5253c7a8788a2968184afa940a8085d5a50a5d08ea7ccf90309f5bd90386b898`. TextFrames (GI-2): White `4b8d6358e392dca05adbb16e99b76106ee2723427229269a1ff33003a57a390d`; Black `2bcbf10c9100c6c571b0622d9d44c3e927f04428f0c510543531ebc6ad4b2dd3`. A linha T01 passa a `APROVADO`. T01.1, E01.2 e E01.3 permanecem PENDENTES.

**E00.10 v01 — GI-0 aprovado (10/11/2026, 13:21), GI-1 aprovado; GI-2 aprovado (10/11/2026, 13:48); GI-3 conforme tecnicamente e GI-4 aprovado (10/11/2026, 15:06); aceites GI-2 e GI-4 reconfirmados (15:14, D-10); conjunto do GI-4 confirmado (15:32, D-11); versão FECHADA E CONGELADA (15:43, D-12):** Tela Mobile `360 × 800` (modal de API indisponível no login sobre a T00.1 v02 desfocada, superfície a 75% como na M00.5, na E00.6 a E00.9) com estado único, o texto do Documento Mestre apresentado como título em duas linhas, ícone `warning_amber` de 28 px em círculo no lugar de `⚠` e dois botões lado a lado como na E00.8: `VER CONFIGURAÇÃO` em botão de texto à esquerda e `TENTAR NOVAMENTE` preenchido à direita, com rótulos de 14 px em duas linhas. **GI-1:** o responsável respondeu **"Aprovado este modelo"** (13:07) à apresentação das imagens, registrado como aceite visual com a ressalva L-02. PNGs aprovados: White SHA-256 `2f3e60d775052ca398f7499127db334d9550f683d43fc6950e0721c56c2e1147`; Black SHA-256 `037b8d3fa6add0d2b1cbce075a684cf669da4bb1fe14e65a058d9555ab987f23`. Diferenças restritas ao E00.10: V-01 (mensagem como título), V-02 (ícone), V-03 (ordem e hierarquia dos botões) e V-04 (rótulos em duas linhas); o Documento Mestre não foi alterado. Uma proposta anterior com botões empilhados foi rejeitada antes do aceite e não foi persistida. **Na data deste parágrafo, os TextFrames (GI-2) foram derivados dos PNGs aprovados e o responsável os aprovou em 10/11/2026 às 13:48 (D-08, "Aprovado os arquivos.", com o anexo dos quatro hashes; versões submetidas e aprovadas: White SHA-256 `a5de9378fc6c74a28847830c51167ecf6ada36e11e08d6d96ea83126bf3e2352`; Black SHA-256 `4dbaa0c1c7832b0c7982c1177d50fa8876969f4356f30956f915ea4d282bf952`), e as Pranchas (GI-3) foram produzidas depois, submetidas ao GI-4 e aprovadas pelo responsável em 10/11/2026 às 15:06 (D-09, "APROVADO E CONGELADO", com o anexo dos dois hashes)**; a linha E00.10 passa a `APROVADO`. **GI-0:** o responsável declarou **"Aprovo expressamente o GI-0 da E00.10 v01, para os temas White e Black, conforme os controles publicados, confirmando explicação do L-06 e L-07"** (13:21), registrado como D-06; L-06 (comparação de hashes só com mais de um commit; com commit único o repositório é a verdade absoluta) e L-07 (histórico apenas na mudança de versão A→B) ficam resolvidas. Implementação sobre a base com commit único `84f277c45d54b1ab6080ec2b6e800ddac5682e8a`: PNGs, TextFrames, controles, Pranchas e registros de composição da E00.10 v01 (white e black), com alteração apenas deste README. **Ressalvas:** em 10/11/2026 (13:33), D-07, o responsável fechou as ressalvas L-01 a L-05 e L-08 (hashes atuais dos PNGs verificados e iguais aos acima; botão de texto correto para o padrão de modal; clique fora da janela sem escolher opção equivale a janela fechada; pesquisa é informação de apoio; pequena variação do ícone aceitável); nenhuma ressalva permanece aberta. Os TextFrames `white|black/telas/wiframetext/E00.10-01-01_v01.md` e as Pranchas `white|black/telas/pranchas/01_Mobile_360x800/E00.10-01-01_v01.png` (1280 × 1920), com os registros de composição `white|black/telas/pranchas/01_Mobile_360x800/wiframetext/E00.10-01-01_v01.md`, completam o conjunto; o GI-4 imprime o STATUS final `APROVADO E CONGELADO`. Pranchas submetidas e aprovadas: White SHA-256 `304efcc506f74c53e30c9e0aa3fd26ec351d5bb096689e1c5e3f4ab93ac6cb25`; Black SHA-256 `e8fe8ec89981907a1460452b0ca6e9ad384cda26e5b01fb2c9990a6a7fc8c32e`. Pranchas finais (STATUS impresso): White SHA-256 `e18ffc2a6b4f6503f4574d8d348847ee1baa7be3e0d98f7ec5b0d26b9df75043`; Black SHA-256 `755cb983c08498adc49b01846f64a263fad7b7ec8dd67ac42d114895827c7b9f`. **GI-3:** CONFORME TECNICAMENTE (ViewPort 0 divergências em 288.000 pixels; 0 pixels fora das regiões autorizadas); **GI-4:** APROVADO E CONGELADO (D-09), com a ressalva de interpretação L-10, FECHADA em D-10. **Reconfirmação (D-10, 10/11/2026, 15:14):** o responsável declarou "Aprovo expressamente o GI-2 da E00.10 v01" (L-09) e "APROVADO E CONGELADO" (L-10), afirmando que os aceites foram decisão sua; L-09 e L-10 fechadas, sem alterar PNGs, Pranchas nem hashes aprovados. **Confirmação do conjunto (D-11, 10/11/2026, 15:32):** o responsável confirmou que o GI-4 da E00.10 v01 abrange as Pranchas White e Black e o conjunto (achado F-01 da auditoria). **Fechamento (D-12, 10/11/2026, 15:43):** auditoria aprovada pelo responsável (commit auditado `8a0a461`) e E00.10 v01 FECHADA E CONGELADA; mudança de versão passa a gerar histórico de hashes. Evidências: `white|black/telas/controle/E00.10-01-01_v01.md` §§5–10 e D-10, `white|black/telas/wiframetext/E00.10-01-01_v01.md` e `white|black/telas/pranchas/01_Mobile_360x800/wiframetext/E00.10-01-01_v01.md`.

**T01.1 v01 — GI-1 aprovado (D-T01.1-07), GI-2 aprovado (D-T01.1-08), GI-3 corretivo conforme tecnicamente, GI-4 aprovado e congelado (D-T01.1-10, 11/11/2026):** o responsável aprovou expressamente a Prancha corrigida White SHA-256 `140709f4843c3305633afd743ee7b760152abc95548f682c52a4c723c4c68384`, a Prancha corrigida Black SHA-256 `721e19fe2d841d426128fec11b313136cd1a40bc8c57f27d09d33b87cacf2bb0` e o conjunto White/Black. A nova montagem GI-3 corrigiu os campos do cabeçalho e STATUS, Item 10 (amostras da interface) e Item 14 (observações específicas), mantendo a Tela Mobile `360 × 800` aprovada em quatro estados por tema. Nos novos PNGs, o STATUS impresso `AGUARDANDO APROVAÇÃO` reflete a submissão, preservado byte a byte após a decisão humana; o estado documental posterior é `APROVADO E CONGELADO`. Os registros de composição White/Black em `telas/pranchas/01_Mobile_360x800/wiframetext/T01.1-01-01_v01.md` preservam a decisão histórica D-T01.1-09, limitada às Pranchas anteriores White SHA-256 `fb0a3e08db6da3cb463802db9bb0682580f11b253474146476b3ada55b81da1e` e Black SHA-256 `ea16c7707f4a2586f22ee06ed745f4065ba344e3f20b320e004261f2e11b7ff1`. A aprovação GI-4 desta interface é exclusivamente visual/documental; não representa implementação em Design/Figma/Protótipo/HTML. A auditoria transversal de encerramento exigida pela SPEC 3 é uma verificação distinta e não é declarada concluída por esta atualização operacional.

**E01.2 v01 — GI-0 aprovado (D-E01.2-04, 11/11/2026, 18:29), GI-1 aprovado (D-E01.2-02, 17:03), GI-2 aprovado (D-E01.2-05, 18:29), GI-3 conforme tecnicamente e GI-4 aprovado e congelado (D-E01.2-06, 11/11/2026, 18:37; GI-1, GI-2 e GI-4 reconfirmados em D-E01.2-08, 19:29):** Tela Mobile `360 × 800` de Login inválido com estado único (credencial recusada), em White e Black, que reproduz o estado de erro já aprovado da T01 (sem modal e sem novo desenho), conforme D-E01.2-01; os PNGs têm bytes idênticos aos de `T01-01-01_v01_estado-erro.png` e os Gates são próprios da E01.2. No GI-4 o responsável respondeu **"Aprovo com esta frase"** para "Aprovo expressamente o GI-4 do E01.2 v01, para os temas White e Black, conforme as Pranchas publicadas." e "Autorizo, se GI-4 aprovado" para atualizar esta linha e o Controle de Evolução Visual e gerar o ZIP único (D-E01.2-06). Hashes das Pranchas submetidas e aprovadas no GI-4 (D-E01.2-06): White `c4115e146dda2ed0b537c34348fcdfbf57cbc0d6e81b6e5eaff8e5c3d432a8d1`; Black `533853933edc4a498c40d00855a9252e3b3c936f6a438cce9d801faa197efd1e`. Em D-E01.2-08 (11/11/2026, 19:29) o responsável reconfirmou o GI-1 e o GI-2 e aprovou o GI-4 sobre as Pranchas finais, com STATUS impresso APROVADO E CONGELADO (somente a região do STATUS alterada): White `e0c828d736c0d73cbef86d0be95104b2a6a87e7bbf2525339bf9cd2afce7674c`; Black `a74099393b21086c75c96b70545262b12b9b5f33b9145070abbf04204c317d68`. Hashes dos PNGs de Tela: White `8f4fdf30d061bb7487df3428bf36c2a6727e0b5fbb001f793bae4facc623ce7b`; Black `23be80f647f9de22652660b87b69356a93b80376a10f3e5487fab63d87bf555a`. TextFrames (versão final, GI-2): White `a64330cd7d35b7a7caeed2a6e87e9822fea1c313465595fb79d124a535b1184c`; Black `1c1abc6ee5621ece34aad4297402a150ea025c40cd4a849b88088d7912b0e37d`. A linha E01.2 passa a `APROVADO`. E01.3 e as demais interfaces seguintes permanecem PENDENTES.

**E01.3 v01 — GI-0 aprovado (D-E01.3-07, 11/11/2026, 20:27), GI-1 aprovado após a revisão de texto (D-E01.3-16, 21:55; ajuste e auditoria em D-E01.3-15), GI-2 aprovado (D-E01.3-17, 22:03), GI-3 conforme tecnicamente e GI-4 aprovado e congelado (D-E01.3-18, 11/11/2026, 22:06):** Tela Mobile `360 × 800` de Sem conexão com estado único (modal de falha de conexão sobre a T01 principal desfocada e escurecida), em White e Black, com ícone `cloud_off` (Material Icons Outlined), título "Falha na conexão", descrição "Não foi possível estabelecer conexão com o serviço. Tente novamente em instantes." em três linhas e botão único TENTAR NOVAMENTE; clique fora do modal equivale a fechá-lo (D-E01.3-07). Os Gates GI-1, GI-2 e GI-4 do primeiro ciclo (D-E01.3-12 a D-E01.3-14) foram superados pela revisão de texto e não valem para os arquivos atuais. Hashes das Pranchas submetidas e aprovadas no GI-4 (D-E01.3-18): White `fda86524f2da77d19ac9fe4d70c06232de467a1a5992cfac39c81c91f265f386`; Black `18b80b33ea9580e8e10365aed66353299a62e3eac93e620e1ddf89c8c3416f50`. Pranchas finais, com STATUS impresso APROVADO E CONGELADO (somente a região do STATUS alterada): White `01e217b5f6f8d186d956af5255019046c4695a6c50c788e1707db73ed48ca70d`; Black `ef2fdd82707f7f2f9a69a113f7fa20a1313afed68a5517b96eb23c811580f94b`. PNGs de Tela: White `a93ffe9f77de7622b3765ff40c845ca7d74be75c2eaa99cbe6081c01e17c6023`; Black `97caeb51d591bd9c8818070175557692f9d9e041d4adba31c15e3c5e6389f75c`. TextFrames (versão submetida e aprovada no GI-2): White `49ca8045fe750d4ae7324faa9b6289540544962684336774c69ff480f982479f`; Black `fb8f4809ff19ce59ef36d5e8b3d8a7c30708967cb02d2dc19da2b8dad28fb46a`. A linha E01.3 passa a `APROVADO`. E01.4 e as demais interfaces seguintes permanecem PENDENTES.

| # | ID | Claro | Escuro | Status geral |
|---:|---|---|---|---|
| 01 | `T00` | APROVADO | APROVADO | APROVADO |
| 02 | `T00.1` | APROVADO | APROVADO | APROVADO |
| 03 | `T00.2` | APROVADO | APROVADO | APROVADO |
| 04 | `T00.3` | APROVADO | APROVADO | APROVADO |
| 05 | `M00.4` | APROVADO | APROVADO | APROVADO |
| 06 | `M00.5` | APROVADO | APROVADO | APROVADO |
| 07 | `E00.6` | APROVADO | APROVADO | APROVADO |
| 08 | `E00.7` | APROVADO | APROVADO | APROVADO |
| 09 | `E00.8` | APROVADO | APROVADO | APROVADO |
| 10 | `E00.9` | APROVADO | APROVADO | APROVADO |
| 11 | `E00.10` | APROVADO | APROVADO | APROVADO |
| 12 | `T01` | APROVADO | APROVADO | APROVADO |
| 13 | `T01.1` | APROVADO | APROVADO | APROVADO |
| 14 | `E01.2` | APROVADO | APROVADO | APROVADO |
| 15 | `E01.3` | APROVADO | APROVADO | APROVADO |
| 16 | `E01.4` | PENDENTE | PENDENTE | PENDENTE |
| 17 | `E01.5` | PENDENTE | PENDENTE | PENDENTE |
| 18 | `T02` | PENDENTE | PENDENTE | PENDENTE |
| 19 | `T02.1` | PENDENTE | PENDENTE | PENDENTE |
| 20 | `T03` | PENDENTE | PENDENTE | PENDENTE |
| 21 | `M03.1` | PENDENTE | PENDENTE | PENDENTE |
| 22 | `E03.2` | PENDENTE | PENDENTE | PENDENTE |
| 23 | `T04` | PENDENTE | PENDENTE | PENDENTE |
| 24 | `T04.1` | PENDENTE | PENDENTE | PENDENTE |
| 25 | `T04.2` | PENDENTE | PENDENTE | PENDENTE |
| 26 | `T04.3` | PENDENTE | PENDENTE | PENDENTE |
| 27 | `T04.4` | PENDENTE | PENDENTE | PENDENTE |
| 28 | `T04.5` | PENDENTE | PENDENTE | PENDENTE |
| 29 | `T05` | PENDENTE | PENDENTE | PENDENTE |
| 30 | `T05.1` | PENDENTE | PENDENTE | PENDENTE |
| 31 | `T05.2` | PENDENTE | PENDENTE | PENDENTE |
| 32 | `T05.3` | PENDENTE | PENDENTE | PENDENTE |
| 33 | `T05.4` | PENDENTE | PENDENTE | PENDENTE |
| 34 | `T06` | PENDENTE | PENDENTE | PENDENTE |
| 35 | `M06.1` | PENDENTE | PENDENTE | PENDENTE |
| 36 | `T06.2` | PENDENTE | PENDENTE | PENDENTE |
| 37 | `E06.3` | PENDENTE | PENDENTE | PENDENTE |
| 38 | `T07` | PENDENTE | PENDENTE | PENDENTE |
| 39 | `M07.1` | PENDENTE | PENDENTE | PENDENTE |
| 40 | `E07.2` | PENDENTE | PENDENTE | PENDENTE |
| 41 | `T08` | PENDENTE | PENDENTE | PENDENTE |
| 42 | `T09` | PENDENTE | PENDENTE | PENDENTE |
| 43 | `M09.1` | PENDENTE | PENDENTE | PENDENTE |
| 44 | `T09.2` | PENDENTE | PENDENTE | PENDENTE |
| 45 | `M09.3` | PENDENTE | PENDENTE | PENDENTE |
| 46 | `T10` | PENDENTE | PENDENTE | PENDENTE |
| 47 | `M10.1` | PENDENTE | PENDENTE | PENDENTE |
| 48 | `T11` | PENDENTE | PENDENTE | PENDENTE |
| 49 | `T12` | PENDENTE | PENDENTE | PENDENTE |
| 50 | `M12.1` | PENDENTE | PENDENTE | PENDENTE |
| 51 | `T13` | PENDENTE | PENDENTE | PENDENTE |
| 52 | `T14` | PENDENTE | PENDENTE | PENDENTE |
| 53 | `M14.1` | PENDENTE | PENDENTE | PENDENTE |
| 54 | `T15` | PENDENTE | PENDENTE | PENDENTE |
| 55 | `T15.1` | PENDENTE | PENDENTE | PENDENTE |
| 56 | `T15.2` | PENDENTE | PENDENTE | PENDENTE |
| 57 | `T16` | PENDENTE | PENDENTE | PENDENTE |
| 58 | `T16.1` | PENDENTE | PENDENTE | PENDENTE |
| 59 | `T16.2` | PENDENTE | PENDENTE | PENDENTE |
| 60 | `M16.3` | PENDENTE | PENDENTE | PENDENTE |
| 61 | `E16.4` | PENDENTE | PENDENTE | PENDENTE |
| 62 | `T17` | PENDENTE | PENDENTE | PENDENTE |
| 63 | `T17.1` | PENDENTE | PENDENTE | PENDENTE |
| 64 | `T17.2` | PENDENTE | PENDENTE | PENDENTE |
| 65 | `T17.3` | PENDENTE | PENDENTE | PENDENTE |
| 66 | `T17.4` | PENDENTE | PENDENTE | PENDENTE |
| 67 | `T17.5` | PENDENTE | PENDENTE | PENDENTE |
| 68 | `M17.6` | PENDENTE | PENDENTE | PENDENTE |
| 69 | `E17.7` | PENDENTE | PENDENTE | PENDENTE |
| 70 | `E17.8` | PENDENTE | PENDENTE | PENDENTE |
| 71 | `E17.9` | PENDENTE | PENDENTE | PENDENTE |

---

# 16. Contadores

```text
Interfaces previstas:              71
Mínimo de imagens Claro:           71
Mínimo de imagens Escuro:          71
Mínimo de imagens funcionais:     142
Total final: variável por paginação
```

Pranchas-modelo de `references/templates/` **e os seis arquivos oficiais de template em `white/template/` e `black/template/`** não entram nessa contagem. Telas isoladas não são Pranchas funcionais; a matriz mantém o controle das saídas funcionais conforme seus critérios próprios.

---

# 17. Autoridade documental

- Documento Mestre: requisitos, fichas funcionais e Textframes das 71 interfaces.
- SPEC 1 `PROCESSO-PRANCHA.md`: definição/construção técnica de uma **Prancha do Template**; não governa saídas T/M/E.
- SPEC 2 `REFERENCIA-TEMPLATE-OFICIAL.md`: contrato permanente da referência oficialmente selecionada.
- [`Registro_Controle_Template_Oficial.md`](Registro_Controle_Template_Oficial.md): única fonte da decisão vigente, histórico das substituições, caminhos e hashes.
- SPEC 3 `PROCESSO-TELA-PRANCHA.md`: produção e aprovação de Wireframe Text da Tela, Tela de Referência e Prancha de Implementação.
- `WIREFRAME-TEXT-TELA.md`: contrato de TextFrame individual **derivado do PNG visual previamente aprovado em GI-1**, com confronto e aprovação documental em GI-2.
- `REGRAS-TECNICAS.md`: invariantes de representação; `WIREFRAME-TEXT.md` e `MONTAGEM-IMAGEM.md`: contratos auxiliares da **Prancha do Template**.
- Este README: **estrutura, inventário, matriz de 71 IDs e contadores**, sem autorização para redefinir qualquer regra anterior.
