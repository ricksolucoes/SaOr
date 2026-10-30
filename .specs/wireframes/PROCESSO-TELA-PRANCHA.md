# SaOr — SPEC 3: Prancha de Implementação e produção das interfaces funcionais

## 1. Autoridade, limites e fontes

Esta SPEC governa **somente** a utilização de uma referência oficial aprovada para produzir os artefatos individuais das interfaces funcionais T/M/E. Ela não define nem constrói a Prancha do Template (SPEC 1) e não escolhe, altera ou reaproveita implicitamente um modelo (SPEC 2).

Autoridades distintas:

- **Fonte funcional:** [`docs/Documento_Mestre.md`](../../docs/Documento_Mestre.md), baseline v1.0, fichas, Textframes, navegação, estados e regras transversais.
- **Invariantes de representação:** [`REGRAS-TECNICAS.md`](REGRAS-TECNICAS.md), inclusive ViewPort `360 × 800` e regras `white`/`black`.
- **Contrato documental da Tela:** [`WIREFRAME-TEXT-TELA.md`](WIREFRAME-TEXT-TELA.md); o TextFrame será construído **após a aprovação visual do PNG** e documentará fielmente a imagem existente.
- **Referência selecionada:** SPEC 2 [`REFERENCIA-TEMPLATE-OFICIAL.md`](REFERENCIA-TEMPLATE-OFICIAL.md) e seu registro genérico de vigência. Modelo C é a seleção atual, **não uma escolha perpetuamente irrevogável**.
- **Gate obrigatório desta SPEC:** [`GATE-IMPLEMENTACAO-TELAS.md`](GATE-IMPLEMENTACAO-TELAS.md); seus checkpoints GI-0 a GI-4 condicionam cada artefato, por ID/tema/página e conjunto completo.
- **Controle operacional:** [`docs/wireframes/images/README.md`](../../docs/wireframes/images/README.md), exclusivamente diretórios, nomes, inventário e matriz de estado.

Documentos históricos de construção do template (`PROCESSO-PRANCHA.md`, `WIREFRAME-TEXT.md`, `MONTAGEM-IMAGEM.md`) **não constituem Gates de aprovação das Telas** nem redefinem a composição selecionada. Suas regras técnicas comuns podem ser consultadas quando aplicáveis, sem executar novamente o processo de criação do template.

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
| Tela visual (proposta GI-1; congelada após GI-2) | `docs/wireframes/images/<tema>/telas/<nome-base>.png` |
| Registro de verificações GI-0/GI-1 | `docs/wireframes/images/<tema>/telas/controle/<nome-base>.md` |
| Registro textual de composição da Prancha de Implementação | `docs/wireframes/images/<tema>/wiframetext/<nome-base>.md` |
| Prancha de Implementação | `docs/wireframes/images/<tema>/<nome-base>.png` |

`<tema>` é exclusivamente `white` ou `black`; `template/` contém apenas arquivos oficiais do modelo, nunca arquivos de interface. Quando houver estados visuais alternativos aprovados, o PNG de cada variante usa a mesma base seguida de `__estado-<identificador>.png`, com entrada própria no controle GI-1 e no TextFrame derivado; o nome-base sem sufixo identifica o estado principal documentado, não autoriza omitir os demais estados realmente exigidos. Os arquivos de controle GI-0/GI-1 não são Wireframe Text; existem para registrar fonte, hash e aprovação **antes** de elaborar o texto. Diretórios de saída ainda não existentes devem ser criados **somente quando houver produção autorizada da primeira interface**, não pela simples aprovação desta SPEC. O README operacional apresenta a estrutura e o estado real, não escolhe versões.

Interpretação de `<ID>-<PÁGINA>-<TOTAL>_v<VERSÃO>`: `<ID>` é o ID canônico; `<PÁGINA>` é a página documental atual; `<TOTAL>` é o total de páginas da representação; `<VERSÃO>` é a versão daquela página. A correção localizada pode incrementar somente a versão da página afetada se a paginação total for preservada. Se o total mudar, toda a sequência nova deve refletir o total correto. Uma sequência de páginas é aprovada somente com todas as páginas dos temas exigidos conferidas.

Paginação **por continuidade de rolagem da mesma interface**: um ViewPort técnico individual de `360 × 800 px` deve existir para **cada página de cada ID e tema**, com os elementos que de fato aparecem naquela posição. Se todo o conteúdo não couber na região rolável, criar `P01`, `P02`, ... representando **posições sequenciais de rolagem**, sem cortar campos, ações ou textos, reduzir controles para caber ou criar novas interfaces. Cada página reproduz o estado esperado da interface na posição de rolagem aprovada no PNG, posteriormente documentada no Wireframe Text: indicar deslocamento/trecho inicial e final, ordem integral dos campos, elementos fixos, roláveis e condicionais e eventuais sobreposições intencionais. Não reiniciar o conteúdo rolável nem repetir um campo como novo conteúdo; repetir somente elementos efetivamente persistentes segundo seu comportamento documentado. Se uma quebra de página fragmentar indevidamente um componente, corrigir a proposta visual e reapresentá-la ao GI-1 antes de documentar a geometria no TextFrame. Indicador de rolagem somente quando documentado ou tecnicamente justificado. **Página não é versão:** `01/03`, `02/03`, `03/03` representam posições da mesma Tela; `v01`, `v02` representam revisões. O total/ordem deve coincidir nos temas white/black.

Equivalência entre `white` e `black`: informações, campos, ações/destinos, estados, hierarquia, agrupamentos, proporções, navegação, ordem de leitura, tipos de componentes, tipografia e paginação devem ser equivalentes; as diferenças autorizadas são as regras de tokens/paleta específicas de cada tema.

Cada revisão preserva as versões aprovadas; não sobrescrever silenciosamente. Mudanças que afetem paginação exigem revisar os nomes `<PÁGINA>-<TOTAL>` de toda sequência dependente, mantendo registro do que foi substituído. Para novas saídas, sempre vincular a versão **exata** do template vigente no instante da aprovação, com caminho e hash — uma seleção futura não altera artefatos históricos.

## 4. Etapa 1 — Construir e aprovar visualmente o PNG da Tela (GI-0 e GI-1)

1. Ler a **ficha e o Textframe funcional do Documento Mestre**, ações, destinos, estados, componentes, retorno e regras transversais da interface. Executar GI-0 com inventário por elemento, requisito, condição e fonte; inspecionar os PNGs e Wireframe Text oficiais do tema conforme SPEC 2. Decisões sem fonte ou padrão visual insuficiente devem ser bloqueadas antes do desenho, e não resolvidas por adivinhação.
2. Identificar a composição efetiva exigida, sem importar componentes demonstrativos do Modelo C. A AppBar reproduz a interface específica; ícones de lista são opcionais **por item** conforme a fonte funcional; componentes informativos de status distinguem seus estados sem se tornarem botões por inferência.
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

1. Consultar **SPEC 2** e seu registro de vigência: verificar modelo, PNG, Wireframe Text de referência, ViewPort, temas e hashes. Atualmente é Modelo C, white v02 e black v01; a regra deve funcionar se isso mudar futuramente.
2. Ler a geometria estrutural do modelo aprovado e aplicar **exclusivamente às novas saídas funcionais** o mapeamento de conteúdo variável autorizado pela seção 6.1 desta SPEC. A Prancha de Implementação é um **novo artefato**; não editar, reexportar nem sobrescrever qualquer arquivo de `template/`. O conteúdo de demonstração dos PNGs/WT congelados não é obrigação funcional nem autorização para inventar elementos.
3. Criar o **registro textual específico de composição** no caminho da seção 3: ID/tema/página/versão, requisitos de apresentação, caminhos e hashes do PNG aprovado em GI-1, do TextFrame e do conjunto aprovado em GI-2, versão exata da referência e hashes dos três artefatos oficiais, dimensões, região de inserção, coordenadas `x/y`, escala `1:1`, campos variáveis, textos/metadados e validações GI-3/GI-4. Esse registro especifica **somente os dados particulares da apresentação**, sem reproduzir ou reaprovar a estrutura fixa já congelada do template. Identificar no cabeçalho os valores por interface/página: `ID: <ID>`; **`ETAPA: <Nome da interface>`** (por exemplo, `Configuração da aplicação`, conforme a ficha funcional; o identificador existe somente no campo `ID`); `PÁGINA: XX / YY` (continuidade da rolagem); `VERSÃO: vNN` (revisão, independente do número da página); `BASELINE: v1.0`; `VARIAÇÃO: white | black`; `DATA`; `STATUS` do artefato. Manter a identidade SaOr e a geometria de apresentação. **Nunca** utilizar `ETAPA: Wireframe Conceitual em Imagem` como identificação funcional: esse texto pertence ao exemplo histórico do template. Registrar os elementos e notas **efetivamente aplicados à interface**, sem copiar automaticamente demonstrações.
4. Se algum dado não se enquadrar no mapeamento de variabilidade autorizado na seção 6.1, ou se a geometria fixa não comportar sua representação fiel, **bloquear** e solicitar avaliação justificada conforme SPECs 1/2; não inventar zonas, alterar a geometria, diminuir a Tela, ocultar componentes/observações ou inventar uma página de rolagem apenas para comportar documentação lateral. Páginas de rolagem representam somente a continuidade **real da interface**.
5. Produzir uma nova **cópia de trabalho** de Prancha `1280 × 1920 px` preservando a estrutura fixa. **Primeira alteração na cópia: substituir o conteúdo do ViewPort técnico** pelo PNG aprovado da página correspondente em `360 × 800 px`, na região original, em escala `1:1`, **sem redimensionar, recortar, recolorir nem alterar pixels**; verificar identidade pixel a pixel (GI-3). Só depois completar o cabeçalho, Item 10, Item 14 e demais informações autorizadas da Prancha. Não editar o PNG do ViewPort oficial nem o template congelado. Nenhum elemento demonstrativo apresentado na prancha substitui um componente ou requisito efetivo da Tela.
6. Conferir o novo PNG com o registro de composição e os arquivos oficiais. Não aplicar os Gates 1–6 de **construção de novo template** a uma Prancha de Implementação; sua aprovação é a do artefato funcional descrita na seção 7.

### 6.1 Mapeamento autorizado para novas Pranchas de Implementação (Modelo C vigente)

Este mapeamento aplica-se **somente às cópias de trabalho de saídas funcionais** feitas a partir da referência identificada pela SPEC 2. Não altera nem reinterpreta o PNG ou Wireframe Text oficiais aprovados; os números, cartões e coordenadas abaixo são os já documentados nos Wireframe Text **white C v02** e **black C v01**. Se outra referência passar a vigorar, sua aplicação deve ser verificada e formalmente documentada antes de usar este mapeamento: **não** presumir os mesmos campos.

| Região aprovada | Regra de conteúdo variável na saída funcional | Restrição invariável |
|---|---|---|
| **Item 1 — VIEWPORT TÉCNICO** | Substituir a demonstração pelo PNG de **cada página** da Tela de Referência aprovada, por tema, incluindo campos e estados daquela posição de rolagem | `360 × 800 px`, inserção em `x=40`, `y=272`, escala 1:1, sem alterações de pixels; primeiro conteúdo substituído na nova cópia |
| **Cabeçalho — identidade documental, título, legenda e metadados** | Nas **Pranchas de Implementação**, omitir `WIREFRAME` e a legenda demonstrativa `(Viewport à esquerda + painel técnico à direita)`; exibir apenas `PRANCHA TÉCNICA` no título; preencher `ID` com o identificador funcional e `ETAPA` com **somente a descrição** da interface. `PÁGINA = XX / YY` representa a continuidade da mesma Tela, `VERSÃO = vNN` a revisão; `DATA`, `BASELINE`, `VARIAÇÃO` e `STATUS` descrevem a saída real | Preservar geometria, marca, regiões, divisores e coordenadas do cabeçalho da referência oficial; não deslocar o título nem expandir regiões para ocupar espaços deixados vazios |
| **Item 10 — COMPONENTES (MEDIDAS)** | Documentar e representar **exclusivamente os componentes efetivamente presentes na Tela correspondente**, nas formas e estados usados. AppBar: reproduzir fielmente o layout da própria Tela, inclusive textos, controles, ícones, ações e dimensões documentadas; **não** copiar a amostra simplificada do template. Itens de lista podem possuir ou não ícone, **por item**, quando exigido ou permitido pela ficha/WT; nunca acrescentar ícone por hábito | Preservar o card e a geometria da zona, sem adicionar componentes ilustrativos de outras Telas; medidas devem corresponder às da Tela aprovada |
| **Item 14 — OBSERVAÇÕES TÉCNICAS** | Registrar somente premissas, regras, limitações, comportamentos, estados, continuidade/rolagem e observações pertinentes **àquela Tela e, quando cabível, àquela página**, com fonte rastreável; quantidade e texto definidos pela necessidade real, não pelas dez observações demonstrativas do template | Preservar o card, as zonas e os limites físicos; se não houver observação adicional, registrar expressamente essa condição, sem inventar uma nota |

### 6.2 Tratamento obrigatório dos textos demonstrativos e do STATUS nas saídas funcionais

**Esta seção não altera o Modelo C nem suas especificações congeladas.** O modelo vigente contém `WIREFRAME`, `PRANCHA TÉCNICA - MODELO C` e a legenda `(Viewport à esquerda + painel técnico à direita)`: esses textos documentam a prancha-modelo e **não** são conteúdo compulsório da saída funcional. A utilização do template aplica substituições **exclusivamente em uma nova cópia de Prancha de Implementação**, após a substituição do ViewPort e com GI-2 aprovado.

1. Conservar posições, dimensões, marca SaOr e todas as regiões estruturais aprovadas. No cabeçalho funcional, **não renderizar** o texto `WIREFRAME` nem a legenda demonstrativa. O título, sem subtítulo ou sufixo de modelo, será exatamente `PRANCHA TÉCNICA`, mantendo sua posição original. Não apagar áreas físicas nem deslocar outros elementos para preencher o vazio.
2. `ID` = identificador canônico da ficha (ex.: `T00`); `ETAPA` = **apenas** o nome oficial da interface (ex.: `Configuração da aplicação`). É proibida a repetição de `T00 -` no campo ETAPA ou o uso do título do template como etapa. `PÁGINA` e `VERSÃO` mantêm as regras existentes.
3. O estado **`AGUARDANDO APROVAÇÃO`**, enquanto aplicável à Prancha funcional, terá **ícone `schedule` da família Material Icons Outlined**, 20 px, seguido do texto em duas linhas `AGUARDANDO / APROVAÇÃO`. A referência geométrica é a região aprovada de STATUS: ícone em `(1120,46)` e texto iniciando em `(1146,38)` com largura máxima `114 px`, sujeito à conferência de encaixe real; não reduzir arbitrariamente a fonte nem sair da região `x=1108`, `w=160`. Texto e ícone usam **Error white `#991B1B`** ou **Error black `#FCA5A5`**, conforme o tema definido em `REGRAS-TECNICAS.md`, como **destaque visual específico solicitado para espera por aprovação**. A cor não altera o estado para ERRO, nem ativa o Gate. Se a renderização não couber na região, o GI-3 fica bloqueado; não se altera o template.
4. Outros estados documentados conservam seus contratos próprios; `APROVADO E CONGELADO` não é transformado no estado anterior e não pode ser usado sem decisão humana válida. Status da Prancha é diferente dos indicadores informativos de conexão presentes na Tela T00.
5. **Item 10** e **Item 14** continuam obrigatoriamente particulares à Tela e sua página, segundo a tabela acima. Elementos demonstrativos das amostras de template não são copiados como componentes funcionais.
6. O registro de composição deve indicar: referência vigente com seus hashes, textos omitidos/substituídos, valores completos dos campos, token e glyph do STATUS, conferência geométrica e ligação com os GI anteriores. Não registrar visualização de trabalho como aprovada.

### 6.3 Divergência específica autorizada de uma Tela versus Documento Mestre

Uma decisão de ocultar um texto ou outra informação **específica de uma interface** não se transforma em regra genérica de template nem altera silenciosamente a Baseline 1.0. A divergência deverá constar do registro `telas/controle/` do ID/tema com: trecho original da baseline; alteração visual deliberada; justificativa e alcance; elemento/destino preservado; decisão do responsável e data; evidências dos PNGs e seus hashes; avaliação de impacto e condição de aceite GI-1/GI-2. Se não houver autorização expressa e rastreável para uma divergência normativa, o Gate fica `BLOQUEADO`, independentemente da estética do PNG. A autorização da **exceção visual** não equivale à aprovação humana de todos os PNGs nem altera a ficha funcional original; requisitos funcionais adicionais continuam sob controle da baseline.

**Aplicação específica já comunicada para T00:** ocultar o subtítulo `Claro / Escuro` abaixo de `Tema`, sem remover o item nem seu destino `T00.2`. A decisão é restrita a T00 white/black e seus estados de conexão; a documentação individual deve declarar explicitamente o desvio e o vínculo com a baseline. Outras telas não herdam essa ocultação. O campo técnico `VARIAÇÃO` da Prancha continua visível e não é o mesmo texto da Tela.

As demais regiões técnicas da Prancha conservam a **estrutura e função documental** da referência aprovada. Suas demonstrações não autorizam acrescentar elementos à Tela nem declarar que um componente foi usado. Uma região que deva representar dados específicos só pode ser preenchida quando houver referência técnica verificável e espaço na geometria aprovada; caso contrário, aplicar bloqueio, não converter suposições em conteúdo. A fidelidade da saída funcional é aferida principalmente pelo **ViewPort por página e o Wireframe Text individual**, complementados pelos Itens 10 e 14.

Para toda interface, manter um **inventário de cobertura dos campos** no Wireframe Text e no registro de composição: nome/ID do elemento, origem funcional, condição/estado, página de rolagem em que aparece, geometria e ação/destino. Conferir que a união das páginas contempla todos os elementos aplicáveis e que a continuidade não cria campos novos nem perde campos existentes. Se o conteúdo real exigir mais posições de rolagem, **ampliar o total de páginas da Tela e das Pranchas correspondentes**, com especificação e aprovação próprias; jamais criar outra versão física do template para simular rolagem. Para a interface com `YY` páginas, produzir `YY` ViewPorts individuais e `YY` Pranchas por tema (salvo desvio funcional explicitamente aprovado na baseline).

O Item 10 ou Item 14 não pode ser preenchido com exemplos genéricos só para ocupar espaço. **Excedente de documentação da Prancha** não é prova de rolagem da Tela: se a área do próprio Item 10/14 não suportar os dados efetivamente necessários sem omissão ou redução indevida, `GI-3 = BLOQUEADO` até análise de revisão de template ou solução expressamente aprovada. A rolagem pertence ao ViewPort e não autoriza alterar as dimensões do canvas `1280 × 1920`.

O registro de composição **não é outro Wireframe Text de construção de template**. Sua função é registrar as escolhas da aplicação da referência fixa naquela interface. A especificação interna da Tela permanece no seu próprio Wireframe Text.

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
