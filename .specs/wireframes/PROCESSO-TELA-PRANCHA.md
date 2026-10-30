# SaOr — SPEC 3: Prancha de Implementação e produção das interfaces funcionais

## 1. Autoridade, limites e fontes

Esta SPEC governa **somente** a utilização de uma referência oficial aprovada para produzir os artefatos individuais das interfaces funcionais T/M/E. Ela não define nem constrói a Prancha do Template (SPEC 1) e não escolhe, altera ou reaproveita implicitamente um modelo (SPEC 2).

Autoridades distintas:

- **Fonte funcional:** [`docs/Documento_Mestre.md`](../../docs/Documento_Mestre.md), baseline v1.0, fichas, Textframes, navegação, estados e regras transversais.
- **Invariantes de representação:** [`REGRAS-TECNICAS.md`](REGRAS-TECNICAS.md), inclusive ViewPort `360 × 800` e regras `white`/`black`.
- **Contrato documental da Tela:** [`WIREFRAME-TEXT-TELA.md`](WIREFRAME-TEXT-TELA.md); o TextFrame será construído **após a aprovação visual do PNG** e documentará fielmente a imagem existente.
- **Referência selecionada:** SPEC 2 [`REFERENCIA-TEMPLATE-OFICIAL.md`](REFERENCIA-TEMPLATE-OFICIAL.md) e seu registro genérico de vigência. a seleção corrente é identificada exclusivamente pelo registro de vigência, **não por esta SPEC**.
- **Gate obrigatório desta SPEC:** [`GATE-IMPLEMENTACAO-TELAS.md`](GATE-IMPLEMENTACAO-TELAS.md); seus checkpoints GI-0 a GI-4 condicionam cada artefato, por ID/tema/página e conjunto completo.
- **Controle operacional:** [`docs/wireframes/images/README.md`](../../docs/wireframes/images/README.md), exclusivamente diretórios, nomes, inventário e matriz de estado.

Documentos históricos de construção do template (`PROCESSO-PRANCHA.md`, `WIREFRAME-TEXT.md`, `MONTAGEM-IMAGEM.md`) **não constituem Gates de aprovação das Telas** nem redefinem a composição selecionada. Suas regras técnicas comuns podem ser consultadas quando aplicáveis, sem executar novamente o processo de criação do template.

## 1.1 MVP vigente — somente Mobile

**Decisão de escopo vigente:** o MVP atual produz **somente interfaces Mobile**, nos temas `white` e `black`, com ViewPort funcional `360 × 800 px` e Prancha `1280 × 1920 px`. As pastas `02_Tablet_768x1024`, `03_Notebook_1366x768` e `04_Desktop_1920x1080` são **referências físicas reservadas ao MVP posterior**: sua existência não autoriza nem exige telas, pranchas, versionamento, Gates, adaptações responsivas ou atividades de desenvolvimento nessas resoluções no MVP atual. Não extrapolar regras Mobile para elas; eventual produção futura depende de especificação e autorização próprias. O catálogo de 71 interfaces do Documento Mestre permanece inalterado; o encerramento de T00 não significa encerramento do MVP nem das demais interfaces.

## 2. Três artefatos e processo linear bloqueante — PNG primeiro

**Tela de Referência:** PNG visual individual `360 × 800 px`, criado primeiro em canvas independente com base no Documento Mestre e nas regras técnicas; apresentado visualmente e aprovado antes da redação do TextFrame. Antes de GI-1 é uma proposta, não um artefato congelado.

**Wireframe Text/TextFrame individual da Tela:** documentação técnica **derivada do PNG visual aprovado**, com reprodução textual fiel, cotas exatas medidas na imagem, tokens, estados e rastreabilidade. Não determina retrospectivamente uma aparência que não foi vista e aprovada.

**Prancha de Implementação:** imagem nova `1280 × 1920 px` que consome o PNG + TextFrame aprovados e utiliza a referência vigente, sem editar os arquivos congelados do template. Não é código de aplicação.

```text
DOCUMENTO MESTRE + FICHA/TEXTFRAME FUNCIONAL DA INTERFACE
    ↓
GI-0: INVENTÁRIO E PRÉ-CONDIÇÕES DOCUMENTAIS / REFERÊNCIA VIGENTE
    ↓
CONSTRUÇÃO DE PNGs VISUAIS ISOLADOS (360 × 800, POR TEMA/ESTADO/PÁGINA)
    ↓
INSPEÇÃO REAL DAS IMAGENS, CONTEÚDO, LAYOUT E CONTINUIDADE
    ↓
GI-1: APROVAÇÃO HUMANA VISUAL DO PNG (HASH REGISTRADO)
    ↓
CRIAÇÃO DO TEXTFRAME / WIREFRAME TEXT FIEL AO PNG APROVADO
    ↓
CONFRONTO ELEMENTO A ELEMENTO: PNG ↔ TEXTFRAME ↔ COTAS ↔ REQUISITOS
    ↓
GI-2: APROVAÇÃO HUMANA DO CONJUNTO PNG + TEXTFRAME; CONGELAMENTO
    ↓
REVERIFICAÇÃO DA REFERÊNCIA VIGENTE (SPEC 2)
    ↓
GI-3: NA NOVA CÓPIA DA PRANCHA, SUBSTITUIR PRIMEIRO O VIEWPORT
    ↓
COMPLETAR METADADOS, ITEM 10, ITEM 14 E REGISTRO DE COMPOSIÇÃO
    ↓
GI-4: APROVAÇÃO DA PRANCHA / CONJUNTO / VERSIONAMENTO
```

**Inversão proibida:** não criar ou aprovar o Wireframe Text antes do PNG visual; não aceitar diagrama de bandas, árvore de componentes ou tabela de coordenadas como evidência visual. A tela deve ser vista em PNG e aprovada antes de ser documentada; o TextFrame não pode inventar detalhes para sanar lacunas da imagem. Aprovação do PNG não aprova o TextFrame, nem a Prancha. O [Gate GI-0 a GI-4](GATE-IMPLEMENTACAO-TELAS.md) condiciona cada avanço, sem reexecutar os Gates 1–6 da SPEC 1.

## 3. Identificação, diretórios e versionamento

Para cada ID, tema, página e versão, usar o mesmo nome-base `<ID>-<PÁGINA>-<TOTAL>_v<VERSÃO>`, com páginas em dois dígitos e versão `vNN`. Exemplo: `T00-01-01_v01`. O conjunto de 71 IDs é definido **somente** no Documento Mestre, não nos nomes de exemplos.

| Artefato | Caminho relativo à raiz do repositório |
|---|---|
| Wireframe Text individual | `docs/wireframes/images/<tema>/telas/wiframetext/<nome-base>.md` |
| Tela visual Mobile (proposta GI-1; congelada após GI-2) | `docs/wireframes/images/<tema>/telas/design/01_Mobile_360x800/<nome-base>.png` |
| Registro de verificações GI-0/GI-1 | `docs/wireframes/images/<tema>/telas/controle/<nome-base>.md` |
| Registro textual de composição da Prancha de Implementação Mobile | `docs/wireframes/images/<tema>/telas/pranchas/01_Mobile_360x800/wiframetext/<nome-base>.md` |
| Prancha de Implementação Mobile | `docs/wireframes/images/<tema>/telas/pranchas/01_Mobile_360x800/<nome-base>.png` |

`<tema>` é exclusivamente `white` ou `black`; `template/` contém apenas arquivos oficiais do modelo, nunca arquivos de interface. Os nomes das subpastas de resolução são parte dos caminhos físicos; para o MVP vigente usar **somente `01_Mobile_360x800`**. Os controles e TextFrames individuais continuam fora das pastas de resolução, em `telas/controle/` e `telas/wiframetext/`. Os PNGs alternativos de estado ficam ao lado do PNG principal em `telas/design/01_Mobile_360x800/`. Quando houver estados visuais alternativos aprovados, o PNG de cada variante usa a mesma base seguida de `__estado-<identificador>.png`, com entrada própria no controle GI-1 e no TextFrame derivado; o nome-base sem sufixo identifica o estado principal documentado, não autoriza omitir os demais estados realmente exigidos. Os arquivos de controle GI-0/GI-1 não são Wireframe Text; existem para registrar fonte, hash e aprovação **antes** de elaborar o texto. Diretórios de saída ainda não existentes devem ser criados **somente quando houver produção autorizada da primeira interface**, não pela simples aprovação desta SPEC. O README operacional apresenta a estrutura e o estado real, não escolhe versões.

Interpretação de `<ID>-<PÁGINA>-<TOTAL>_v<VERSÃO>`: `<ID>` é o ID canônico; `<PÁGINA>` é a página documental atual; `<TOTAL>` é o total de páginas da representação; `<VERSÃO>` é a versão daquela página. A correção localizada pode incrementar somente a versão da página afetada se a paginação total for preservada. Se o total mudar, toda a sequência nova deve refletir o total correto. Uma sequência de páginas é aprovada somente com todas as páginas dos temas exigidos conferidas.

Paginação **por continuidade de rolagem da mesma interface**: um ViewPort técnico individual de `360 × 800 px` deve existir para **cada página de cada ID e tema**, com os elementos que de fato aparecem naquela posição. Se todo o conteúdo não couber na região rolável, criar `P01`, `P02`, ... representando **posições sequenciais de rolagem**, sem cortar campos, ações ou textos, reduzir controles para caber ou criar novas interfaces. Cada página reproduz o estado esperado da interface na posição de rolagem aprovada no PNG, posteriormente documentada no Wireframe Text: indicar deslocamento/trecho inicial e final, ordem integral dos campos, elementos fixos, roláveis e condicionais e eventuais sobreposições intencionais. Não reiniciar o conteúdo rolável nem repetir um campo como novo conteúdo; repetir somente elementos efetivamente persistentes segundo seu comportamento documentado. Se uma quebra de página fragmentar indevidamente um componente, corrigir a proposta visual e reapresentá-la ao GI-1 antes de documentar a geometria no TextFrame. Indicador de rolagem somente quando documentado ou tecnicamente justificado. **Página não é versão:** `01/03`, `02/03`, `03/03` representam posições da mesma Tela; `v01`, `v02` representam revisões. O total/ordem deve coincidir nos temas white/black.

Equivalência entre `white` e `black`: informações, campos, ações/destinos, estados, hierarquia, agrupamentos, proporções, navegação, ordem de leitura, tipos de componentes, tipografia e paginação devem ser equivalentes; as diferenças autorizadas são as regras de tokens/paleta específicas de cada tema.

Cada revisão preserva as versões aprovadas; não sobrescrever silenciosamente. Mudanças que afetem paginação exigem revisar os nomes `<PÁGINA>-<TOTAL>` de toda sequência dependente, mantendo registro do que foi substituído. Para novas saídas, sempre vincular a versão **exata** do template vigente no instante da aprovação, com caminho e hash — uma seleção futura não altera artefatos históricos.

## 4. Etapa 1 — Construir e aprovar visualmente o PNG da Tela (GI-0 e GI-1)

1. Ler a **ficha e o Textframe funcional do Documento Mestre**, ações, destinos, estados, componentes, retorno e regras transversais da interface. Executar GI-0 com inventário por elemento, requisito, condição e fonte; inspecionar os PNGs e Wireframe Text oficiais do tema conforme SPEC 2. Decisões sem fonte ou padrão visual insuficiente devem ser bloqueadas antes do desenho, e não resolvidas por adivinhação.
2. Identificar a composição efetiva exigida, sem importar componentes demonstrativos do template selecionado. A AppBar reproduz a interface específica; ícones de lista são opcionais **por item** conforme a fonte funcional; componentes informativos de status distinguem seus estados sem se tornarem botões por inferência.
3. **Criar primeiro o PNG visual de proposta** em canvas independente `360 × 800 px`, orientação retrato, margens técnicas de `12 px` e largura útil de `336 px`; não criar moldura ou régua documental no PNG, nem desenhar dentro da Prancha. Usar os tokens e padrões white/black aprovados. Não criar um Wireframe Text antes da imagem.
4. Quando o conteúdo exigir rolagem, criar PNGs por **posição sucessiva real** da mesma Tela, preservando todos os elementos, a distinção de elementos fixos/roláveis e a continuidade. Determinar `XX / YY` a partir da imagem e do inventário, não de uma página presumida. Produzir estados alternativos somente quando previstos/aprovados; cada PNG de estado deve ser visualmente examinável e identificado.
5. **Abrir e inspecionar fisicamente todos os PNGs** por tema/página/estado. Conferir textos, alinhamento, hierarquia, tipografia, ícones, cores, espaços, dimensões, proporções, estados, truncamentos e cobertura do inventário. Tabelas de coordenadas ou diagramas ASCII não substituem essa inspeção. Se faltar padrão visual, interromper e solicitar decisão explícita: não inventar layout.
6. Submeter a proposta visual real ao responsável para **aprovação humana GI-1**. Registrar em `telas/controle/<nome-base>.md` a decisão, data, arquivo, estado/página, dimensões e SHA-256 de cada imagem **antes de redigir seu TextFrame**. Imagem não aprovada fica como proposta; imagem aprovada não pode ter pixels alterados sem nova submissão. O controle GI-0/1 é registro de decisão, não especificação alternativa.

**GI-1 é visual, não documental.** Um PNG aparentemente bonito que viola requisitos é `NÃO CONFORME`; nenhuma decisão estética não documentada vira novo requisito funcional. Após GI-1 a imagem aprovada é a **fonte visual da versão** para GI-2.

## 5. Etapa 2 — Derivar e aprovar o TextFrame da imagem (GI-2)

1. Abrir o **PNG visual já aprovado em GI-1** e conferir o hash exato com o registro `telas/controle/`. Se não houver imagem real e aprovação prévia persistente, **bloquear**: não se admite TextFrame especulativo.
2. Criar **somente agora** o Wireframe Text individual sob [`WIREFRAME-TEXT-TELA.md`](WIREFRAME-TEXT-TELA.md), identificando PNG fonte, tema, página, versão e variantes de estado. Seu TextFrame textual deve refletir a composição observável, acompanhado de geometria local exata `x/y/w/h`, hierarquia, tokens, ícones, textos, alinhamentos e estados medidos/verificados contra a imagem.
3. Confrontar **cada elemento do PNG** com seu requisito funcional e com o TextFrame. Nenhum objeto da imagem pode ficar sem especificação, e nenhum objeto do texto pode estar ausente da imagem sem estado/condição explicitamente justificado. **É proibido aceitar banda y, pseudoimagem aproximada, lista de componentes ou régua como substituto da imagem**.
4. Validar cobertura da interface por conjunto de páginas, continuidade de rolagem, estados aplicáveis e equivalência white/black. Se o documento revelar erro visual, **corrigir a imagem e retornar ao GI-1**, submetendo novamente os hashes; não maquiar o texto para justificar o erro. Se o erro for apenas documental, corrigir o rascunho do TextFrame preservando os bytes do PNG aprovado.
5. Submeter o documento para **aprovação humana GI-2**, expressa e vinculada ao PNG e ao WT por caminho, versão e SHA-256, com registro no próprio documento e no controle. Somente com ambas as aprovações, visual e documental, o conjunto PNG + TextFrame torna-se `APROVADO E CONGELADO` e está apto à Prancha.

**Aprovação GI-1 não equivale a GI-2, e nenhuma delas aprova automaticamente a Prancha.** A imagem física permanece `360 × 800 px` e não é reexportada ou redimensionada durante a documentação.

## 6. Etapa 3 — Usar a referência vigente e construir a Prancha de Implementação

1. Consultar **SPEC 2** e seu registro de vigência: verificar modelo, PNG, Wireframe Text de referência, ViewPort, temas e hashes. Não inferir a versão pela numeração do arquivo; consultar o registro de vigência e os contratos aplicáveis.
2. Ler a geometria estrutural do modelo aprovado e aplicar **exclusivamente às novas saídas funcionais** o contrato técnico versionado exigido pela seção 6.1 desta SPEC. A Prancha de Implementação é um **novo artefato**; não editar, reexportar nem sobrescrever qualquer arquivo de `template/`. O conteúdo de demonstração dos PNGs/WT congelados não é obrigação funcional nem autorização para inventar elementos.
3. Criar o **registro textual específico de composição** no caminho da seção 3: ID/tema/página/versão, requisitos de apresentação, caminhos e hashes do PNG aprovado em GI-1, do TextFrame e do conjunto aprovado em GI-2, versão exata da referência e hashes dos três artefatos oficiais, dimensões, região de inserção, coordenadas `x/y`, escala comprovada pelo contrato vigente, campos variáveis, textos/metadados e validações GI-3/GI-4. Esse registro especifica **somente os dados particulares da apresentação**, sem reproduzir ou reaprovar a estrutura fixa já congelada do template. Identificar no cabeçalho os valores por interface/página: `ID: <ID>`; **`ETAPA: <Nome da interface>`** (por exemplo, `Configuração da aplicação`, conforme a ficha funcional; o identificador existe somente no campo `ID`); `PÁGINA: XX / YY` (continuidade da rolagem); `VERSÃO: vNN` (revisão, independente do número da página); `BASELINE` conforme a versão funcional aprovada aplicável; `VARIAÇÃO: white | black`; `DATA`; `STATUS` do artefato. Manter a identidade SaOr e a geometria de apresentação. **Nunca** utilizar `ETAPA: Wireframe Conceitual em Imagem` como identificação funcional: esse texto pertence ao exemplo histórico do template. Registrar os elementos e notas **efetivamente aplicados à interface**, sem copiar automaticamente demonstrações. O título e as legendas variáveis são definidos no contrato da referência, não por esta SPEC.
4. Se algum dado não se enquadrar nos campos autorizados pelo contrato técnico vigente, ou se a geometria fixa não comportar sua representação fiel, **bloquear** e solicitar avaliação justificada conforme SPECs 1/2; não inventar zonas, alterar a geometria, diminuir a Tela, ocultar componentes/observações ou inventar uma página de rolagem apenas para comportar documentação lateral. Páginas de rolagem representam somente a continuidade **real da interface**.
5. Produzir uma nova **cópia de trabalho** da Prancha com o canvas documentado no contrato da referência, observando a restrição Mobile do MVP vigente, preservando a estrutura fixa. **Primeira alteração na cópia: substituir o conteúdo do ViewPort técnico** pelo PNG aprovado da página correspondente em `360 × 800 px`, na região e escala indicadas no contrato concreto, **sem redimensionar, recortar, recolorir nem alterar pixels da Tela-fonte**; verificar identidade pixel a pixel (GI-3). Só depois completar o cabeçalho, Item 10, Item 14 e demais informações autorizadas da Prancha. Não editar o PNG do ViewPort oficial nem o template congelado. Nenhum elemento demonstrativo apresentado na prancha substitui um componente ou requisito efetivo da Tela.
6. Conferir o novo PNG com o registro de composição e os arquivos oficiais. Não aplicar os Gates 1–6 de **construção de novo template** a uma Prancha de Implementação; sua aprovação é a do artefato funcional descrita na seção 7.

### 6.1 Contrato técnico da referência selecionada — obrigatório e versionado

A SPEC 2 determina a **identidade da referência vigente**. A SPEC 3 determina **como utilizá-la**: nenhuma destas normas define diretamente os campos, as posições, os glyphs ou as cores de um modelo concreto. Para iniciar GI-3, o executor deve localizar o **contrato técnico de utilização explicitamente vinculado ao modelo, à versão e ao tema selecionados** no registro da referência. O contrato contém a lista de regiões estruturais fixas, campos documentais parametrizáveis, canvas, ViewPort, posição e escala de inserção, ícones, textos demonstrativos substituíveis, tratamentos cromáticos e limites de conteúdo.

**Ordem de validação:** registro de vigência da SPEC 2 → seis artefatos físicos e hashes → contrato técnico aplicável à identidade/versionamento do conjunto → PNG e TextFrame GI-2 da interface → registro de composição individual. A ausência de qualquer elo, ou divergência entre contrato e imagem oficial, estabelece `BLOQUEADO`. Não reutilizar campos, coordenadas ou estilos de uma versão anterior por semelhança visual ou por nome.

A primeira substituição na **nova cópia funcional** continua sendo o ViewPort pela Tela aprovada da página e tema; as dimensões, coordenadas e escala serão exatamente as do contrato aprovado, sem alterar pixels. Somente depois preencher as regiões variáveis autorizadas. O resultado deve permanecer fiel à estrutura imutável do modelo selecionado e aos requisitos da interface.

### 6.2 Campos e STATUS — regra estável de preenchimento

O `ID` identifica a interface funcional; `ETAPA` contém **somente sua descrição oficial**, sem repetição do ID. `PÁGINA` identifica continuidade real de rolagem; `VERSÃO` é a revisão do artefato; DATA/BASELINE/VARIAÇÃO/STATUS são preenchidos segundo evidências e campos disponíveis no contrato selecionado. O **título, as legendas demonstrativas, os glyphs, as cores, a posição do STATUS e o conjunto de campos substituíveis** são obtidos do contrato da versão vigente, nunca copiados por inferência de um exemplo histórico. Status de aprovação não pode ser convertido em erro funcional apenas por receber destaque cromático; uma imagem que desenhe `APROVADO` sem decisão comprovada não constitui evidência de aprovação.

O registro de composição contém os valores efetivos, as omissões/substituições **autorizadas naquele contrato**, referência e hashes, coordenadas da inserção e vínculo com GI-1/GI-2. Item 10 contém apenas os componentes usados na Tela individual; Item 14 contém somente observações técnicas pertinentes; os componentes demonstrativos não são obrigatórios. Se faltar espaço ou autorização para qualquer campo, o GI-3 será `BLOQUEADO`, sem alterar o modelo congelado.

### 6.3 Desvios específicos entre Tela e baseline

Para cada divergência, registrar no controle da interface: exigência original com caminho/seção; diferença visual exata; justificativa, alcance, data e decisão do responsável quando comprovada; componente/destino preservado; imagens e hashes; impacto e resultado dos Gates. O texto de um exemplo de interface **não pode integrar esta SPEC como regra permanente**, nem ser estendido a outros IDs. Se faltar aprovação/autoridade aplicável, bloquear e solicitar decisão, sem reescrever a baseline.

## 7. Validação, aprovação e independência dos resultados

Antes de solicitar aprovação humana da Prancha de Implementação, conferir:

```text
[ ] PNG visual da Tela aprovado em GI-1 antes da criação do Wireframe Text
[ ] o TextFrame foi derivado e aprovado em GI-2, com confronto exato contra o PNG de 360 × 800
[ ] conteúdo, estados, AppBar e ícones opcionais de lista conferidos entre PNG visual, requisitos e TextFrame derivado
[ ] inventário dos campos completo no conjunto das páginas de rolagem, sem omissão nem repetição indevida
[ ] referência de template vigente identificada por tema, versão e hashes
[ ] os arquivos oficiais e históricos do template permanecem íntegros
[ ] PNG da Prancha é novo e mede exatamente 1280 × 1920
[ ] região e coordenadas de inserção comprovadas pelo modelo oficial
[ ] a primeira substituição na cópia de trabalho foi o ViewPort técnico, usando a Tela aprovada da página correta
[ ] Tela presente em 1:1, comparada pixel a pixel na região da Prancha
[ ] campo PÁGINA no formato XX / YY representa a continuidade real; ID identifica a interface e ETAPA contém somente sua descrição funcional (sem ID repetido)
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

Aprovador registra decisão humana expressa para a Prancha, independente das aprovações GI-1 (PNG visual) e GI-2 (conjunto PNG + TextFrame), após verificar o [Gate GI-4](GATE-IMPLEMENTACAO-TELAS.md). Falha da Tela ou do TextFrame bloqueia a composição até a aprovação GI-1/GI-2 correspondente; falha da apresentação corrige **somente o novo artefato e seu registro**, sem adulterar o template ou a Tela aprovada.

### 7.1 Regularização de decisão de aprovação já concedida

Quando o responsável declarar que uma **Prancha já foi aprovada**, registrar a declaração nos **registros de composição** das versões físicas envolvidas, com nome, caminho, SHA-256, tema, página, escopo da decisão, texto efetivo do STATUS, fonte/teor da declaração e **data da regularização separada da data original da decisão**. Não presumir que a data desenhada na Prancha seja a data da aprovação. A transcrição fiel da decisão **não é nova avaliação visual nem exige gerar outro PNG**. A decisão não se estende automaticamente ao PNG-fonte de estados alternativos ou ao aceite documental GI-2, salvo evidência específica.

A revisão técnica de caminhos, medidas, integridade e vínculos continua obrigatória. Registrar separadamente (i) **aprovação visual da Prancha já declarada**, (ii) conformidade técnica GI-3 verificável, (iii) estado documental GI-1/GI-2 e (iv) condição para encerramento na matriz funcional. Se faltar aceite documental próprio para GI-2, **não registrar GI-2 como aprovado**, não inventar ordem/data de Gates anteriores e manter a matriz `EM VALIDAÇÃO` até completar as evidências. Isso não revoga a aprovação visual das Pranchas existentes.

## 8. Estados e rastreabilidade

Cada artefato tem `PENDENTE`, `EM DEFINIÇÃO`, `AGUARDANDO APROVAÇÃO`, `APROVADO E CONGELADO`, `BLOQUEADO POR GATE ANTERIOR` (ou `NÃO APLICÁVEL` com justificativa). Esses **estados de produção** não substituem os estados agregados da matriz operacional (`PENDENTE`, `EM VALIDAÇÃO`, `AJUSTES NECESSÁRIOS`, `APROVADO`). Para marcar a interface como `APROVADO`, todas as páginas de ambos os temas devem estar aprovadas.

Os registros persistentes devem conter, no mínimo:

```text
ID / nome / tema / página / total / versão / baseline funcional
Registro GI-0/GI-1: caminho + inventário + aprovação visual anterior à criação do TextFrame + SHA-256 do PNG
Tela de Referência: caminho + versão + dimensão + SHA-256 + aprovação visual GI-1
Wireframe Text derivado: caminho + versão + SHA-256 + aprovação documental GI-2
Template utilizado: modelo + tema + versão + caminhos + hashes + decisão de vigência na data
Registro de composição: caminho + versão + campos variáveis + coordenadas + aprovação
Prancha de Implementação: caminho + versão + dimensões + SHA-256 + aprovação
Ocorrências, dependências e decisão de revisão quando houver
Evidências do Gate GI-0 a GI-4: resultados por página/tema, bloqueios, aprovações humanas e decisão do conjunto
```

As evidências de aprovação devem existir nos arquivos do repositório, não somente em conversa ou ferramenta externa. A cadeia de aprovação não pode ser invertida ou herdada. O PNG visual vem **antes** do TextFrame; ambos, aprovados como conjunto em GI-2, vêm antes da Prancha.

## 9. Limite de implementação em código

As Telas e Pranchas desta etapa são **referências documentais e visuais**, não interfaces de software já implementadas. Elas fornecem contrato de requisitos e fidelidade para etapas posteriores do Documento Mestre (design, Figma, protótipo e MVP). A implementação em código deverá referenciar os artefatos aprovados, validar conteúdo, navegação, estados e responsividade contra a arquitetura e os componentes **efetivamente formalizados naquela fase**. Não presumir framework, estrutura de frontend/backend, APIs ou componentes inexistentes no repositório atual.

**Critério de conclusão da SPEC 3:** é possível abrir primeiro a Tela visual aprovada, conferir sua fidelidade ao Documento Mestre e às regras técnicas, ler o TextFrame **derivado dessa imagem** e reproduzir fielmente sua apresentação na referência selecionada, com hashes, decisões e versões persistentes, sem acesso a conversas ou a prompts complementares.
