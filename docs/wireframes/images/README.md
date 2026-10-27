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
../../../.specs/wireframes/MONTAGEM-IMAGEM.md
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

A estrutura física vigente é:

```text
docs/wireframes/images/
├── README.md
├── references/
│   ├── Especificação Técnica - Prancha de Trabalho.png
│   ├── white/
│   │   ├── Especificação Técnica do Viewport Mobile.png
│   │   ├── WF-VIEWPORT-360x800-clean.png
│   │   └── WF-VIEWPORT-360x800-clean_icone-esquerda.png
│   ├── black/
│   │   └── <referências específicas da variação, quando existirem>
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
│   └── <saídas funcionais claras, em etapa posterior>
└── black/
    └── <saídas funcionais escuras, em etapa posterior>
```

Separação de responsabilidade:

```text
references/
→ referências técnicas compartilhadas ou específicas por variação

references/templates/white/
→ pranchas-modelo e Wireframe Text da variação clara

references/templates/black/
→ pranchas-modelo e Wireframe Text da variação escura

white/ e black/ na raiz de images/
→ saídas funcionais futuras produzidas a partir da prancha-modelo aprovada
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

A prancha-modelo white atual `WF-TEMPLATE-A_v04` usa `WF-VIEWPORT-360x800.png`. As pranchas-modelo white `WF-TEMPLATE-B_v01` e `WF-TEMPLATE-C_v01` continuam usando `WF-VIEWPORT-360x800-clean_icone-esquerda.png` até que suas novas versões sejam aprovadas.

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
../../../.specs/wireframes/PROCESSO-PRANCHA.md
../../../.specs/wireframes/WIREFRAME-TEXT.md
../../../.specs/wireframes/MONTAGEM-IMAGEM.md
```

Este README não redefine dimensões, cotas ou geometria desses arquivos.

## 3.4 Referências visuais contextuais vigentes

Pranchas-modelo existentes também podem exercer função de **referência visual contextual** quando isso estiver registrado operacionalmente.

Essa função serve para ajudar a compreender a linguagem visual já alcançada na etapa, incluindo:

- nível de acabamento;
- densidade documental;
- hierarquia visual;
- tratamento de cabeçalhos, metadados e regiões documentais;
- tratamento cromático integral, destaques, cores semânticas e contraste;
- ritmo, alinhamento e qualidade geral de apresentação.

A referência visual contextual não substitui `REGRAS-TECNICAS.md`, o Wireframe Text específico nem os ativos físicos obrigatórios. Se a composição específica de uma nova prancha divergir da referência, prevalece a composição documentada para a nova prancha.

A função contextual também inclui compreender a cromia esperada da composição completa. `white` e `black` identificam variações de tema e não devem ser interpretados como instrução para converter a prancha em escala de cinza. A regra normativa de preservação cromática permanece em `MONTAGEM-IMAGEM.md`.

Registro operacional vigente:

```text
white
→ references/templates/white/WF-TEMPLATE-A_v04.png
→ references/templates/white/WF-TEMPLATE-B_v01.png
→ references/templates/white/WF-TEMPLATE-C_v01.png
→ conjunto de referências visuais contextuais aprovadas da variação clara

black
→ references/templates/black/WF-TEMPLATE-A_v01.png
```

`WF-TEMPLATE-A_v01.png`, `WF-TEMPLATE-A_v02.png` e `WF-TEMPLATE-A_v03.png` permanecem como referências históricas da evolução do Modelo A. Não devem ser promovidos novamente a referência vigente apenas por existirem no diretório.

Nenhuma das três referências white atuais define geometria universal. Cada Wireframe Text preserva sua própria composição; o conjunto serve para compreender linguagem, acabamento e decisões já aprovadas, sem copiar automaticamente layout ou conteúdo.

Esse registro pode evoluir quando outra referência for explicitamente adotada para a etapa ou para a variação, sem transformar a geometria de uma prancha específica em template universal.

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

# 11. Saídas funcionais futuras

Esta seção se aplica somente depois de existir uma prancha-modelo aprovada e congelada para a variação correspondente.

A construção atual das pranchas-modelo ocorre em `references/templates/` e não deve ser confundida com as saídas funcionais em `white/` e `black/`.


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

A conferência é feita contra as fontes documentais vigentes; a aparência de uma prancha raster anterior não substitui esse gate. Quando houver referência visual contextual vigente aplicável, ela também deve ser observada para verificar continuidade de linguagem e qualidade, sem substituir a validação documental.

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

Pranchas-modelo de `references/templates/` não entram nessa contagem.

---

# 17. Autoridade documental

1. `docs/Documento_Mestre.md` — conteúdo e comportamento funcional;
2. `docs/Registro_Fechamento_Documento_Mestre.md` — proteção da baseline;
3. `.specs/wireframes/REGRAS-TECNICAS.md` — invariantes técnicos;
4. `.specs/wireframes/PROCESSO-PRANCHA.md` — sequência obrigatória de construção;
5. `.specs/wireframes/WIREFRAME-TEXT.md` — contrato documental;
6. `.specs/wireframes/MONTAGEM-IMAGEM.md` — leitura contextual e método de execução visual profissional;
7. este README — estrutura operacional, localização e papel contextual das referências vigentes;
8. Wireframe Text específico em `references/templates/<variação>/wiframetext/` — composição reproduzível da prancha-modelo;
9. PNG correspondente em `references/templates/<variação>/` — representação visual resultante da prancha-modelo.

Artefato inferior não altera silenciosamente uma regra de nível superior.
