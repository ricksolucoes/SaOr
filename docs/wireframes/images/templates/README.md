# SaOr - Sales Order
## Pranchas-modelo — organização e ciclo de vida

**Diretório:** `docs/wireframes/images/templates/`  
**Especificação técnica superior:** [`../README.md`](../README.md)

---

# 1. Finalidade

Este documento define somente:

- estrutura das referências compartilhadas;
- armazenamento das pranchas em avaliação;
- armazenamento das pranchas aprovadas;
- vínculo entre PNG e Wireframe Text;
- versionamento, preservação e promoção dos artefatos.

Dimensões, viewport, safe areas, tokens, tipografia, componentes, elevação, iconografia e demais regras técnicas pertencem exclusivamente ao README superior.

---

# 2. Estrutura

```text
templates/
├── README.md
├── references/
│   ├── Especificação Técnica - Prancha de Trabalho.png
│   ├── Especificação Técnica do Viewport Mobile.png
│   └── WF-VIEWPORT-360x800-clean.png
├── alternatives/
│   ├── <prancha-em-avaliação>.png
│   └── wiframetext/
│       └── <mesmo-nome-base>.md
└── aprovados/
    ├── <prancha-aprovada>.png
    └── wiframetext/
        └── <mesmo-nome-base>.md
```

## 2.1 `references/`

Somente referências técnicas compartilhadas. Não são alternativas, não recebem status de template e não são copiadas para as outras pastas.

## 2.2 `alternatives/`

Somente pranchas-modelo em avaliação, rejeitadas ou preservadas como alternativas. A imagem fica diretamente na pasta e o Wireframe Text correspondente em `alternatives/wiframetext/`.

## 2.3 `aprovados/`

Somente pranchas-modelo explicitamente aprovadas. A imagem fica diretamente na pasta e o Wireframe Text correspondente em `aprovados/wiframetext/`.

---

# 3. Pareamento PNG ↔ Wireframe Text

Toda nova prancha-modelo deve possuir um Wireframe Text antes de sua imagem ser considerada pronta para avaliação.

Pareamento pelo mesmo nome-base:

```text
alternatives/WF-TEMPLATE-X_v01.png
alternatives/wiframetext/WF-TEMPLATE-X_v01.md
```

O mesmo padrão vale em `aprovados/`.

O Wireframe Text registra somente a composição específica da prancha:

```text
identificação e versão
conceito de composição
mapa de regiões
posições e dimensões específicas
cabeçalho e textos exatos
viewport utilizado e posição
seções presentes
tokens técnicos usados por nome
componentes usados por nome
ícones utilizados
regras específicas da composição
checklist visual da prancha
```

Não registrar conversa, memória de processo, tentativas descartadas, raciocínio interno, histórico narrativo desnecessário ou cópia integral das regras do README superior.

---

# 4. Nomenclatura

Prancha:

```text
WF-TEMPLATE-<IDENTIFICADOR>_v<VERSÃO>.png
```

Wireframe Text:

```text
WF-TEMPLATE-<IDENTIFICADOR>_v<VERSÃO>.md
```

Exemplo:

```text
WF-TEMPLATE-A_v02.png
wiframetext/WF-TEMPLATE-A_v02.md
```

Nova versão nunca sobrescreve silenciosamente versão preservada.

---

# 5. Fluxo de trabalho

```text
especificação técnica em ../README.md
        ↓
Wireframe Text em alternatives/wiframetext/
        ↓
PNG em alternatives/
        ↓
avaliação
        ↓
┌──────────────────────┬──────────────────────┐
│ não aprovada         │ aprovada             │
│ permanece em         │ mover o par para     │
│ alternatives/        │ aprovados/           │
└──────────────────────┴──────────────────────┘
```

A promoção para `aprovados/` exige aprovação explícita.

---

# 6. Promoção

Quando uma prancha for aprovada, mover o par:

```text
<nome>.png
wiframetext/<nome>.md
```

de `alternatives/` para `aprovados/`.

Não manter cópias canônicas simultâneas do mesmo par nas duas pastas. Alternativas não selecionadas permanecem preservadas em `alternatives/`.

---

# 7. Preservação

- não sobrescrever versão preservada;
- não excluir alternativa porque outra foi aprovada;
- não alterar prancha aprovada sem nova versão;
- não promover PNG sem seu Wireframe Text;
- não promover Wireframe Text sem seu PNG.

A pasta indica o estado documental; não é necessário duplicar esse estado em documentos auxiliares.

---

# 8. Relação com wireframes funcionais

Pranchas-modelo calibram e congelam a composição documental da etapa.

Elas:

- não representam interface funcional T/M/E;
- não entram na contagem mínima Claro/Escuro;
- não alteram a baseline funcional;
- não substituem os Textframes do Documento Mestre.
