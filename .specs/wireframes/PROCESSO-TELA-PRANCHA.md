# SaOr — SPEC 3: Prancha de Implementação e produção das interfaces funcionais

## 1. Autoridade, limites e fontes

Esta SPEC governa **somente** a utilização de uma referência oficial aprovada para produzir os artefatos individuais das interfaces funcionais T/M/E. Ela não define nem constrói a Prancha do Template (SPEC 1) e não escolhe, altera ou reaproveita implicitamente um modelo (SPEC 2).

Autoridades distintas:

- **Fonte funcional:** [`docs/Documento_Mestre.md`](../../docs/Documento_Mestre.md), baseline v1.0, fichas, Textframes, navegação, estados e regras transversais.
- **Invariantes de representação:** [`REGRAS-TECNICAS.md`](REGRAS-TECNICAS.md), inclusive ViewPort `360 × 800` e regras `white`/`black`.
- **Contrato da Tela:** [`WIREFRAME-TEXT-TELA.md`](WIREFRAME-TEXT-TELA.md); a Tela será executada a partir do texto **aprovado previamente**.
- **Referência selecionada:** SPEC 2 [`REFERENCIA-TEMPLATE-OFICIAL.md`](REFERENCIA-TEMPLATE-OFICIAL.md) e seu registro genérico de vigência. Modelo C é a seleção atual, **não uma escolha perpetuamente irrevogável**.
- **Gate obrigatório desta SPEC:** [`GATE-IMPLEMENTACAO-TELAS.md`](GATE-IMPLEMENTACAO-TELAS.md); seus checkpoints GI-0 a GI-4 condicionam cada artefato, por ID/tema/página e conjunto completo.
- **Controle operacional:** [`docs/wireframes/images/README.md`](../../docs/wireframes/images/README.md), exclusivamente diretórios, nomes, inventário e matriz de estado.

Documentos históricos de construção do template (`PROCESSO-PRANCHA.md`, `WIREFRAME-TEXT.md`, `MONTAGEM-IMAGEM.md`) **não constituem Gates de aprovação das Telas** nem redefinem a composição selecionada. Suas regras técnicas comuns podem ser consultadas quando aplicáveis, sem executar novamente o processo de criação do template.

## 2. Três artefatos e processo linear bloqueante

**Wireframe Text da Tela:** especificação individual, anterior ao PNG; estabelece o conteúdo e a geometria da interface dentro do ViewPort.

**Tela de Referência:** imagem funcional isolada, `360 × 800 px`, construída e aprovada sem a Prancha.

**Prancha de Implementação:** nova imagem de apresentação, `1280 × 1920 px`, que utiliza o template vigente e recebe uma Tela já aprovada; **não** é uma edição do arquivo oficial congelado nem código de aplicativo.

```text
DOCUMENTO MESTRE + FICHA/TEXTFRAME DA INTERFACE
    ↓
GI-0: PRÉ-CONDIÇÕES FUNCIONAIS / REFERÊNCIA VIGENTE (SPEC 2)
    ↓
WIREFRAME TEXT INDIVIDUAL DA TELA (tema/página/versão)
    ↓
GI-1: VALIDAÇÃO E APROVAÇÃO HUMANA PRÉVIA DO WIREFRAME TEXT
    ↓
CONSTRUÇÃO DE TODOS OS VIEWPORTS ISOLADOS (360 × 800 POR PÁGINA)
    ↓
GI-2: VALIDAÇÃO E APROVAÇÃO HUMANA DAS TELAS E DA CONTINUIDADE
    ↓
REVERIFICAÇÃO DA REFERÊNCIA VIGENTE (SPEC 2)
    ↓
GI-3: NA CÓPIA NOVA, SUBSTITUIR PRIMEIRO O VIEWPORT APROVADO
    ↓
COMPLETAR CAMPOS DA PRANCHA E O REGISTRO DE COMPOSIÇÃO
    ↓
GI-4: VALIDAÇÃO E APROVAÇÃO HUMANA DA PRANCHA E DO CONJUNTO
    ↓
VERSIONAMENTO / RASTREABILIDADE / REFERÊNCIA PARA EVOLUÇÃO FUTURA
```

Nenhuma etapa adquire aprovação por herança. O Gate funcional [GI-0 a GI-4](GATE-IMPLEMENTACAO-TELAS.md) exige evidência persistente e bloqueia o avanço sem o resultado anterior; **não** reexecuta os Gates 1–6 de construção do template. Falta de documento, aprovação, geometria aplicável ou arquivo físico gera `BLOQUEADO POR GATE ANTERIOR` ou pendência fundamentada; jamais uma composição inferida visualmente.

## 3. Identificação, diretórios e versionamento

Para cada ID, tema, página e versão, usar o mesmo nome-base `<ID>-<PÁGINA>-<TOTAL>_v<VERSÃO>`, com páginas em dois dígitos e versão `vNN`. Exemplo: `T00-01-01_v01`. O conjunto de 71 IDs é definido **somente** no Documento Mestre, não nos nomes de exemplos.

| Artefato | Caminho relativo à raiz do repositório |
|---|---|
| Wireframe Text individual | `docs/wireframes/images/<tema>/telas/wiframetext/<nome-base>.md` |
| Tela isolada | `docs/wireframes/images/<tema>/telas/<nome-base>.png` |
| Registro textual de composição da Prancha de Implementação | `docs/wireframes/images/<tema>/wiframetext/<nome-base>.md` |
| Prancha de Implementação | `docs/wireframes/images/<tema>/<nome-base>.png` |

`<tema>` é exclusivamente `white` ou `black`; `template/` contém apenas arquivos oficiais do modelo, nunca arquivos de interface. Diretórios de saída ainda não existentes devem ser criados **somente quando houver produção autorizada da primeira interface**, não pela simples aprovação desta SPEC. O README operacional apresenta a estrutura e o estado real, não escolhe versões.

Interpretação de `<ID>-<PÁGINA>-<TOTAL>_v<VERSÃO>`: `<ID>` é o ID canônico; `<PÁGINA>` é a página documental atual; `<TOTAL>` é o total de páginas da representação; `<VERSÃO>` é a versão daquela página. A correção localizada pode incrementar somente a versão da página afetada se a paginação total for preservada. Se o total mudar, toda a sequência nova deve refletir o total correto. Uma sequência de páginas é aprovada somente com todas as páginas dos temas exigidos conferidas.

Paginação **por continuidade de rolagem da mesma interface**: um ViewPort técnico individual de `360 × 800 px` deve existir para **cada página de cada ID e tema**, com os elementos que de fato aparecem naquela posição. Se todo o conteúdo não couber na região rolável, criar `P01`, `P02`, ... representando **posições sequenciais de rolagem**, sem cortar campos, ações ou textos, reduzir controles para caber ou criar novas interfaces. Cada página reproduz o estado esperado da interface na posição de rolagem explicitada no Wireframe Text: indicar deslocamento/trecho inicial e final, ordem integral dos campos, elementos fixos, roláveis e condicionais e eventuais sobreposições intencionais. Não reiniciar o conteúdo rolável nem repetir um campo como novo conteúdo; repetir somente elementos efetivamente persistentes segundo seu comportamento documentado. Se uma quebra de página fragmentar indevidamente um componente, ajustar o recorte/posição de rolagem no Wireframe Text antes de renderizar. Indicador de rolagem somente quando documentado ou tecnicamente justificado. **Página não é versão:** `01/03`, `02/03`, `03/03` representam posições da mesma Tela; `v01`, `v02` representam revisões. O total/ordem deve coincidir nos temas white/black.

Equivalência entre `white` e `black`: informações, campos, ações/destinos, estados, hierarquia, agrupamentos, proporções, navegação, ordem de leitura, tipos de componentes, tipografia e paginação devem ser equivalentes; as diferenças autorizadas são as regras de tokens/paleta específicas de cada tema.

Cada revisão preserva as versões aprovadas; não sobrescrever silenciosamente. Mudanças que afetem paginação exigem revisar os nomes `<PÁGINA>-<TOTAL>` de toda sequência dependente, mantendo registro do que foi substituído. Para novas saídas, sempre vincular a versão **exata** do template vigente no instante da aprovação, com caminho e hash — uma seleção futura não altera artefatos históricos.

## 4. Etapa 1 — Especificar e aprovar o Wireframe Text da Tela

1. Ler a ficha, o Textframe, ações, destinos, campos, estados, retorno, regras transversais e interfaces relacionadas no Documento Mestre, para o ID efetivo.
2. Criar o documento com o contrato integral de [`WIREFRAME-TEXT-TELA.md`](WIREFRAME-TEXT-TELA.md), incluindo as posições locais dentro de `360 × 800`, hierarquia, textos, estados, tokens do tema, **inventário integral de campos/ações**, comportamento de AppBar e listas e o mapa de continuidade/rolagem com justificativa de cada página. A identificação do campo `ETAPA` da futura prancha será `<ID> - <Nome da interface>` conforme a ficha do Documento Mestre.
3. Identificar lacunas antes de desenhar. `REPRESENTÁVEL` quando documentado; `AMBIGUIDADE DE REPRESENTAÇÃO` exige decisão explícita registrada antes de congelar geometria; `CONTRADIÇÃO DOCUMENTAL` bloqueia; `REQUISITO NOVO` é encaminhado ao processo formal da baseline, não incorporado.
4. Verificar texto, cálculos, cobertura funcional e impossibilidade de dependências circulares. Registrar `AGUARDANDO APROVAÇÃO`.
5. Exigir aprovação humana expressa, identificada e registrada no próprio Wireframe Text. Somente `APROVADO E CONGELADO` permite avançar ao PNG.

**É proibido construir primeiro o PNG e depois inferir ou redigir retroativamente seu Wireframe Text.** A ordem vale para ambas as variações.

## 5. Etapa 2 — Construir e aprovar a Tela de Referência

1. Ler o Wireframe Text da Tela **aprovado** e as invariantes em `REGRAS-TECNICAS.md`.
2. Abrir o PNG de ViewPort oficial **do mesmo tema**, identificado pela SPEC 2, somente como referência dimensional e técnica. Ele contém **demonstração**, não deve ser copiado como conteúdo funcional nem editado.
3. Construir em canvas **independente de `360 × 800 px`**, orientação retrato, sem criar moldura de aparelho e sem trabalhar dentro de uma Prancha; largura útil interna `336 px` com margens de `12 px`.
4. Materializar fielmente **todos** os campos, conteúdos, ações, elementos e estados previstos no Wireframe Text da Tela, distribuídos por suas páginas de continuidade, sem inventar conteúdo nem importar componentes demonstrativos do template. A AppBar reproduz o layout, os elementos e o comportamento definidos **para esta interface**, independentemente da AppBar de exemplo. Ícone em item de lista é **opcional por item** e só aparece se documentado. Se não couber, revisar/aprovar a especificação da continuidade e gerar outra **página**, não reduzir ou eliminar conteúdo; uma revisão da especificação gera nova **versão**, não uma página adicional por si só.
5. Salvar PNG no caminho especificado na seção 3. Reabrir e verificar dimensões físicas, textos, componentes, estados, geometria, tokens, margens, acessibilidade e paginação contra o Wireframe Text aprovado.
6. Para cada página e tema, registrar caminho, nome, versão, SHA-256, trecho/posição de rolagem, inventário de campos efetivamente representados, critérios técnicos, divergências e decisão humana **específica da Tela**. Validar também a **cobertura do conjunto completo**, incluindo as páginas seguintes. Só após `APROVADO E CONGELADO` de todas as páginas dependentes existe conjunto de Telas apto a ser apresentado (GI-2).

Uma correção que mude o conteúdo aprovado do Wireframe Text exige sua revisão/versão e nova aprovação. Uma aprovação da Tela não pode suprir a ausência de aprovação prévia do texto.

## 6. Etapa 3 — Usar a referência vigente e construir a Prancha de Implementação

1. Consultar **SPEC 2** e seu registro de vigência: verificar modelo, PNG, Wireframe Text de referência, ViewPort, temas e hashes. Atualmente é Modelo C, white v02 e black v01; a regra deve funcionar se isso mudar futuramente.
2. Ler a geometria estrutural do modelo aprovado e aplicar **exclusivamente às novas saídas funcionais** o mapeamento de conteúdo variável autorizado pela seção 6.1 desta SPEC. A Prancha de Implementação é um **novo artefato**; não editar, reexportar nem sobrescrever qualquer arquivo de `template/`. O conteúdo de demonstração dos PNGs/WT congelados não é obrigação funcional nem autorização para inventar elementos.
3. Criar o **registro textual específico de composição** no caminho da seção 3: ID/tema/página/versão, requisitos de apresentação, caminhos e hashes do Wireframe Text aprovado e da Tela aprovada, versão exata da referência e hashes dos três artefatos oficiais, dimensões, região de inserção, coordenadas `x/y`, escala `1:1`, campos variáveis, textos/metadados e validações GI-3/GI-4. Esse registro especifica **somente os dados particulares da apresentação**, sem reproduzir ou reaprovar a estrutura fixa já congelada do template. Identificar no cabeçalho os valores por interface/página: `ID: <ID>`; **`ETAPA: <ID> - <Nome da interface>`** (por exemplo, `T00 - Configuração da aplicação`, conforme a ficha funcional); `PÁGINA: XX / YY` (continuidade da rolagem); `VERSÃO: vNN` (revisão, independente do número da página); `BASELINE: v1.0`; `VARIAÇÃO: white | black`; `DATA`; `STATUS` do artefato. Manter a identidade SaOr e a geometria de apresentação. **Nunca** utilizar `ETAPA: Wireframe Conceitual em Imagem` como identificação funcional: esse texto pertence ao exemplo histórico do template. Registrar os elementos e notas **efetivamente aplicados à interface**, sem copiar automaticamente demonstrações.
4. Se algum dado não se enquadrar no mapeamento de variabilidade autorizado na seção 6.1, ou se a geometria fixa não comportar sua representação fiel, **bloquear** e solicitar avaliação justificada conforme SPECs 1/2; não inventar zonas, alterar a geometria, diminuir a Tela, ocultar componentes/observações ou inventar uma página de rolagem apenas para comportar documentação lateral. Páginas de rolagem representam somente a continuidade **real da interface**.
5. Produzir uma nova **cópia de trabalho** de Prancha `1280 × 1920 px` preservando a estrutura fixa. **Primeira alteração na cópia: substituir o conteúdo do ViewPort técnico** pelo PNG aprovado da página correspondente em `360 × 800 px`, na região original, em escala `1:1`, **sem redimensionar, recortar, recolorir nem alterar pixels**; verificar identidade pixel a pixel (GI-3). Só depois completar o cabeçalho, Item 10, Item 14 e demais informações autorizadas da Prancha. Não editar o PNG do ViewPort oficial nem o template congelado. Nenhum elemento demonstrativo apresentado na prancha substitui um componente ou requisito efetivo da Tela.
6. Conferir o novo PNG com o registro de composição e os arquivos oficiais. Não aplicar os Gates 1–6 de **construção de novo template** a uma Prancha de Implementação; sua aprovação é a do artefato funcional descrita na seção 7.

### 6.1 Mapeamento autorizado para novas Pranchas de Implementação (Modelo C vigente)

Este mapeamento aplica-se **somente às cópias de trabalho de saídas funcionais** feitas a partir da referência identificada pela SPEC 2. Não altera nem reinterpreta o PNG ou Wireframe Text oficiais aprovados; os números, cartões e coordenadas abaixo são os já documentados nos Wireframe Text **white C v02** e **black C v01**. Se outra referência passar a vigorar, sua aplicação deve ser verificada e formalmente documentada antes de usar este mapeamento: **não** presumir os mesmos campos.

| Região aprovada | Regra de conteúdo variável na saída funcional | Restrição invariável |
|---|---|---|
| **Item 1 — VIEWPORT TÉCNICO** | Substituir a demonstração pelo PNG de **cada página** da Tela de Referência aprovada, por tema, incluindo campos e estados daquela posição de rolagem | `360 × 800 px`, inserção em `x=40`, `y=272`, escala 1:1, sem alterações de pixels; primeiro conteúdo substituído na nova cópia |
| **Cabeçalho — ID, PÁGINA, VERSÃO, DATA, STATUS, BASELINE, VARIAÇÃO, ETAPA** | Usar metadados reais da saída; `PÁGINA = XX / YY` é a sequência de rolagem da **mesma Tela**; `ETAPA = <ID> - <Nome da interface>` da ficha funcional, igual em todas as suas páginas | Manter posições, tipografia técnica e regiões do cabeçalho; não confundir versão documental com página |
| **Item 10 — COMPONENTES (MEDIDAS)** | Documentar e representar **exclusivamente os componentes efetivamente presentes na Tela correspondente**, nas formas e estados usados. AppBar: reproduzir fielmente o layout da própria Tela, inclusive textos, controles, ícones, ações e dimensões documentadas; **não** copiar a amostra simplificada do template. Itens de lista podem possuir ou não ícone, **por item**, quando exigido ou permitido pela ficha/WT; nunca acrescentar ícone por hábito | Preservar o card e a geometria da zona, sem adicionar componentes ilustrativos de outras Telas; medidas devem corresponder às da Tela aprovada |
| **Item 14 — OBSERVAÇÕES TÉCNICAS** | Registrar somente premissas, regras, limitações, comportamentos, estados, continuidade/rolagem e observações pertinentes **àquela Tela e, quando cabível, àquela página**, com fonte rastreável; quantidade e texto definidos pela necessidade real, não pelas dez observações demonstrativas do template | Preservar o card, as zonas e os limites físicos; se não houver observação adicional, registrar expressamente essa condição, sem inventar uma nota |

As demais regiões técnicas da Prancha conservam a **estrutura e função documental** da referência aprovada. Suas demonstrações não autorizam acrescentar elementos à Tela nem declarar que um componente foi usado. Uma região que deva representar dados específicos só pode ser preenchida quando houver referência técnica verificável e espaço na geometria aprovada; caso contrário, aplicar bloqueio, não converter suposições em conteúdo. A fidelidade da saída funcional é aferida principalmente pelo **ViewPort por página e o Wireframe Text individual**, complementados pelos Itens 10 e 14.

Para toda interface, manter um **inventário de cobertura dos campos** no Wireframe Text e no registro de composição: nome/ID do elemento, origem funcional, condição/estado, página de rolagem em que aparece, geometria e ação/destino. Conferir que a união das páginas contempla todos os elementos aplicáveis e que a continuidade não cria campos novos nem perde campos existentes. Se o conteúdo real exigir mais posições de rolagem, **ampliar o total de páginas da Tela e das Pranchas correspondentes**, com especificação e aprovação próprias; jamais criar outra versão física do template para simular rolagem. Para a interface com `YY` páginas, produzir `YY` ViewPorts individuais e `YY` Pranchas por tema (salvo desvio funcional explicitamente aprovado na baseline).

O Item 10 ou Item 14 não pode ser preenchido com exemplos genéricos só para ocupar espaço. **Excedente de documentação da Prancha** não é prova de rolagem da Tela: se a área do próprio Item 10/14 não suportar os dados efetivamente necessários sem omissão ou redução indevida, `GI-3 = BLOQUEADO` até análise de revisão de template ou solução expressamente aprovada. A rolagem pertence ao ViewPort e não autoriza alterar as dimensões do canvas `1280 × 1920`.

O registro de composição **não é outro Wireframe Text de construção de template**. Sua função é registrar as escolhas da aplicação da referência fixa naquela interface. A especificação interna da Tela permanece no seu próprio Wireframe Text.

## 7. Validação, aprovação e independência dos resultados

Antes de solicitar aprovação humana da Prancha de Implementação, conferir:

```text
[ ] Wireframe Text da Tela aprovado antes do PNG da Tela
[ ] Tela PNG existe, foi aprovada e mede exatamente 360 × 800
[ ] conteúdo, estados, AppBar e ícones opcionais de lista idênticos ao Wireframe Text da Tela
[ ] inventário dos campos completo no conjunto das páginas de rolagem, sem omissão nem repetição indevida
[ ] referência de template vigente identificada por tema, versão e hashes
[ ] os arquivos oficiais e históricos do template permanecem íntegros
[ ] PNG da Prancha é novo e mede exatamente 1280 × 1920
[ ] região e coordenadas de inserção comprovadas pelo modelo oficial
[ ] a primeira substituição na cópia de trabalho foi o ViewPort técnico, usando a Tela aprovada da página correta
[ ] Tela presente em 1:1, comparada pixel a pixel na região da Prancha
[ ] campo PÁGINA no formato XX / YY representa a continuidade real; ETAPA contém ID e nome da interface
[ ] Item 10 contém apenas componentes usados; AppBar fiel e ícones de lista só quando previstos
[ ] Item 14 contém somente observações técnicas individualizadas e pertinentes
[ ] campos variáveis e metadados conferem com o registro de composição
[ ] não existe alteração da geometria estrutural congelada
[ ] correspondência white/black, conteúdo, estados e paginação conferidos
[ ] versão, caminhos, hashes e aprovações independentes registrados
[ ] nenhum texto foi cortado, comprimido ou colocado fora dos cards
[ ] ícones, medidas, espaçamentos, componentes e tokens utilizados conferidos
[ ] nenhuma informação temporária de conversas ou do processo interno foi incorporada à imagem
```

Aprovador registra decisão humana expressa para a Prancha, independente das duas aprovações anteriores, após verificar o [Gate GI-4](GATE-IMPLEMENTACAO-TELAS.md). Falha da Tela bloqueia a composição até nova aprovação dela; falha da apresentação corrige **somente o novo artefato e seu registro**, sem adulterar o template ou a Tela aprovada.

## 8. Estados e rastreabilidade

Cada artefato tem `PENDENTE`, `EM DEFINIÇÃO`, `AGUARDANDO APROVAÇÃO`, `APROVADO E CONGELADO`, `BLOQUEADO POR GATE ANTERIOR` (ou `NÃO APLICÁVEL` com justificativa). Esses **estados de produção** não substituem os estados agregados da matriz operacional (`PENDENTE`, `EM VALIDAÇÃO`, `AJUSTES NECESSÁRIOS`, `APROVADO`). Para marcar a interface como `APROVADO`, todas as páginas de ambos os temas devem estar aprovadas.

Os registros persistentes devem conter, no mínimo:

```text
ID / nome / tema / página / total / versão / baseline funcional
Wireframe Text da Tela: caminho + versão + aprovação anterior + SHA-256
Tela de Referência: caminho + versão + dimensão + SHA-256 + aprovação
Template utilizado: modelo + tema + versão + caminhos + hashes + decisão de vigência na data
Registro de composição: caminho + versão + campos variáveis + coordenadas + aprovação
Prancha de Implementação: caminho + versão + dimensões + SHA-256 + aprovação
Ocorrências, dependências e decisão de revisão quando houver
Evidências do Gate GI-0 a GI-4: resultados por página/tema, bloqueios, aprovações humanas e decisão do conjunto
```

As evidências de aprovação devem existir nos arquivos do repositório, não somente em conversa ou ferramenta externa. A cadeia de aprovação não pode ser invertida ou herdada.

## 9. Limite de implementação em código

As Telas e Pranchas desta etapa são **referências documentais e visuais**, não interfaces de software já implementadas. Elas fornecem contrato de requisitos e fidelidade para etapas posteriores do Documento Mestre (design, Figma, protótipo e MVP). A implementação em código deverá referenciar os artefatos aprovados, validar conteúdo, navegação, estados e responsividade contra a arquitetura e os componentes **efetivamente formalizados naquela fase**. Não presumir framework, estrutura de frontend/backend, APIs ou componentes inexistentes no repositório atual.

**Critério de conclusão da SPEC 3:** é possível identificar e reconstruir cada Tela e sua apresentação no modelo aprovado, com origem, versões e aprovações próprias, apenas pelos arquivos versionados do projeto.
