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

---

# 1. Responsabilidade deste documento

Este README é a fonte de **controle operacional** da etapa de wireframes.

As regras normativas reutilizáveis pertencem a:

```text
../../../.specs/wireframes/REGRAS-TECNICAS.md
../../../.specs/wireframes/PROCESSO-PRANCHA.md
../../../.specs/wireframes/WIREFRAME-TEXT.md
```

Este README mantém:

- estrutura operacional da etapa;
- referências físicas existentes no diretório;
- regras de paginação e nomenclatura;
- critérios operacionais de produção e aprovação;
- controle das 71 interfaces.

Ele não deve criar uma segunda definição para regras já canônicas em `.specs/`.

Ele **não redefine** regras de negócio, conteúdo funcional, Textframes, tokens visuais oficiais do produto ou arquitetura. Esses assuntos permanecem em seus documentos canônicos.

---

# 2. Estrutura da etapa

```text
docs/wireframes/images/
├── README.md
├── templates/
│   ├── README.md
│   ├── references/
│   │   ├── Especificação Técnica - Prancha de Trabalho.png
│   │   ├── Especificação Técnica do Viewport Mobile.png
│   │   └── WF-VIEWPORT-360x800-clean.png
│   ├── alternatives/
│   │   ├── <pranchas em avaliação>.png
│   │   └── wiframetext/
│   │       └── <mesmo-nome-base>.md
│   └── aprovados/
│       ├── <pranchas aprovadas>.png
│       └── wiframetext/
│           └── <mesmo-nome-base>.md
├── white/
└── black/
```

A organização, os estados, os critérios de avaliação, a promoção e o gate de liberação das pranchas-modelo são definidos exclusivamente em [`templates/README.md`](templates/README.md).

---

# 3. Referências técnicas compartilhadas

Os arquivos físicos de `templates/references/` permanecem neste diretório porque são artefatos utilizados na produção. Sua interpretação normativa pertence às specs canônicas.

| Arquivo | Função operacional | Regra canônica |
|---|---|---|
| `Especificação Técnica - Prancha de Trabalho.png` | referência física disponível para o canvas | `.specs/wireframes/REGRAS-TECNICAS.md` |
| `Especificação Técnica do Viewport Mobile.png` | referência visual disponível para cotas | `.specs/wireframes/REGRAS-TECNICAS.md` |
| `WF-VIEWPORT-360x800-clean.png` | bitmap mestre de demonstração para pranchas-modelo neutras | `.specs/wireframes/REGRAS-TECNICAS.md` |

Este README não redefine dimensões, cotas ou geometria desses arquivos.

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

# 11. Imagens funcionais

Cada uma das 71 interfaces deve possuir, no mínimo, uma representação Claro em `white/` e uma representação Escuro em `black/`.

```text
Mínimo Claro: 71
Mínimo Escuro: 71
Mínimo funcional: 142
```

O total final pode aumentar por paginação.

## 11.1 Nomenclatura

```text
<ID>-<PÁGINA>-<TOTAL>_v<VERSÃO>.png
```

Exemplos:

```text
T00-01-01_v01.png
T00-01-02_v01.png
T00-02-02_v01.png
```

Significado:

- `<ID>` — ID canônico da interface;
- `<PÁGINA>` — página documental atual;
- `<TOTAL>` — quantidade total de páginas daquela representação;
- `<VERSÃO>` — versão específica daquela página.

Regras de versionamento:

- uma correção que não altere a quantidade total de páginas pode incrementar somente a versão da página afetada;
- se a alteração modificar o total de páginas, toda a nova sequência deve refletir o novo total de forma consistente;
- uma versão preservada não deve ser sobrescrita silenciosamente.

## 11.2 Paginação

Quando o conteúdo exceder `360 × 800 px`:

- manter o viewport;
- não comprimir artificialmente;
- criar páginas sequenciais;
- repetir somente elementos persistentes;
- continuar o conteúdo no ponto correspondente;
- não inventar paginação funcional;
- usar indicador de rolagem somente quando necessário.

A interface só é aprovada quando todas as páginas Claro e Escuro estiverem aprovadas.

## 11.3 Equivalência Claro / Escuro

Devem permanecer iguais: informações, ações/destinos, campos, estados, hierarquia, agrupamentos, proporções, navegação, ordem de leitura, componentes, tipografia e paginação. A diferença permitida é a paleta técnica da representação.

---

# 12. Conteúdo obrigatório da prancha funcional

```text
Projeto: SaOr - Sales Order
Interface: <ID> — <Nome>
Baseline: v1.0
Etapa: Wireframe Conceitual em Imagem
Variação: Claro | Escuro
Status: PENDENTE | EM VALIDAÇÃO | AJUSTES NECESSÁRIOS | APROVADO
Página: <XX>/<YY>
Versão: vNN
Viewport: <valor vigente de REGRAS-TECNICAS.md>
Orientação: <valor vigente de REGRAS-TECNICAS.md>
Canvas: <valor vigente de REGRAS-TECNICAS.md>
Escala: <valor vigente de REGRAS-TECNICAS.md>
Fonte técnica: <valor vigente de REGRAS-TECNICAS.md>
```

Mostrar somente tokens e observações realmente usados naquela representação.

---

# 13. Regra de produção funcional

Antes de produzir uma interface, consultar no Documento Mestre:

- Ficha funcional de aceite;
- objetivo;
- informações exibidas;
- campos e obrigatoriedade;
- ações e destinos;
- Textframe;
- estados;
- retorno;
- interfaces relacionadas;
- regras transversais aplicáveis.

É proibido inventar funcionalidade, remover ação, criar destino inexistente, fundir IDs, alterar Textframe por conveniência visual, introduzir componente funcional não documentado ou transformar referência conceitual em tecnologia definitiva.

## 13.1 Tratamento de ocorrências

Durante a produção, qualquer dúvida ou incompatibilidade deve ser classificada antes de alterar a representação:

| Classificação | Tratamento |
|---|---|
| `REPRESENTÁVEL` | produzir exatamente conforme a documentação vigente |
| `AMBIGUIDADE DE REPRESENTAÇÃO` | adotar interpretação conservadora, sem alterar função, e registrar a ambiguidade antes de consolidar |
| `CONTRADIÇÃO DOCUMENTAL` | não resolver por inferência; apresentar a contradição para decisão |
| `REQUISITO NOVO` | não incorporar à baseline vigente; encaminhar para o processo formal de alteração |

Essa classificação não cria uma segunda baseline e não autoriza modificar silenciosamente o Documento Mestre.

## 13.2 Gate técnico antes da exportação

Uma prancha somente pode ser considerada pronta para exportação quando a representação tiver sido conferida contra a documentação vigente.

Checklist obrigatório:

```text
[ ] canvas físico validado
[ ] viewport físico validado
[ ] escala 1:1 validada
[ ] textos conferidos
[ ] ícones conferidos
[ ] medidas e espaçamentos conferidos
[ ] componentes conferidos
[ ] tokens técnicos utilizados conferidos
[ ] estados representados conferidos
[ ] página, total de páginas e versão conferidos
[ ] equivalência Claro/Escuro preservada quando aplicável
[ ] nenhuma informação de conversa, processo interno ou validação temporária foi incorporada à prancha
```

Se qualquer item obrigatório falhar, o PNG não deve ser tratado como artefato pronto para validação ou aprovação.

A conferência é feita contra as fontes documentais vigentes; a aparência de uma prancha raster anterior não substitui esse gate.

---

# 14. Estados de controle

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
- uma interface somente pode ficar `APROVADO` quando todas as páginas necessárias de Claro e Escuro estiverem aprovadas;
- o checklist não deve duplicar versão/paginação já expressas nos nomes dos arquivos.

| # | ID | Claro | Escuro | Status geral |
|---:|---|---|---|---|
| 01 | `T00` | PENDENTE | PENDENTE | PENDENTE |
| 02 | `T00.1` | PENDENTE | PENDENTE | PENDENTE |
| 03 | `T00.2` | PENDENTE | PENDENTE | PENDENTE |
| 04 | `T00.3` | PENDENTE | PENDENTE | PENDENTE |
| 05 | `M00.4` | PENDENTE | PENDENTE | PENDENTE |
| 06 | `M00.5` | PENDENTE | PENDENTE | PENDENTE |
| 07 | `E00.6` | PENDENTE | PENDENTE | PENDENTE |
| 08 | `E00.7` | PENDENTE | PENDENTE | PENDENTE |
| 09 | `E00.8` | PENDENTE | PENDENTE | PENDENTE |
| 10 | `E00.9` | PENDENTE | PENDENTE | PENDENTE |
| 11 | `E00.10` | PENDENTE | PENDENTE | PENDENTE |
| 12 | `T01` | PENDENTE | PENDENTE | PENDENTE |
| 13 | `T01.1` | PENDENTE | PENDENTE | PENDENTE |
| 14 | `E01.2` | PENDENTE | PENDENTE | PENDENTE |
| 15 | `E01.3` | PENDENTE | PENDENTE | PENDENTE |
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

Pranchas-modelo de `templates/` não entram nessa contagem.

---

# 17. Autoridade documental

1. `docs/Documento_Mestre.md` — conteúdo e comportamento funcional;
2. `docs/Registro_Fechamento_Documento_Mestre.md` — proteção da baseline;
3. `.specs/wireframes/REGRAS-TECNICAS.md` — invariantes técnicos;
4. `.specs/wireframes/PROCESSO-PRANCHA.md` — sequência obrigatória de construção;
5. `.specs/wireframes/WIREFRAME-TEXT.md` — contrato documental;
6. `templates/README.md` — governança das pranchas-modelo;
7. este README — controle operacional;
8. Wireframe Text específico — composição reproduzível da prancha;
9. PNG correspondente — representação visual resultante.

Artefato inferior não altera silenciosamente uma regra de nível superior.
