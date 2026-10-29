# SaOr — SPEC 3: Prancha de Implementação e produção das interfaces funcionais

## 1. Autoridade, limites e fontes

Esta SPEC governa **somente** a utilização de uma referência oficial aprovada para produzir os artefatos individuais das interfaces funcionais T/M/E. Ela não define nem constrói a Prancha do Template (SPEC 1) e não escolhe, altera ou reaproveita implicitamente um modelo (SPEC 2).

Autoridades distintas:

- **Fonte funcional:** [`docs/Documento_Mestre.md`](../../docs/Documento_Mestre.md), baseline v1.0, fichas, Textframes, navegação, estados e regras transversais.
- **Invariantes de representação:** [`REGRAS-TECNICAS.md`](REGRAS-TECNICAS.md), inclusive ViewPort `360 × 800` e regras `white`/`black`.
- **Contrato da Tela:** [`WIREFRAME-TEXT-TELA.md`](WIREFRAME-TEXT-TELA.md); a Tela será executada a partir do texto **aprovado previamente**.
- **Referência selecionada:** SPEC 2 [`REFERENCIA-TEMPLATE-OFICIAL.md`](REFERENCIA-TEMPLATE-OFICIAL.md) e seu registro genérico de vigência. Modelo C é a seleção atual, **não uma escolha perpetuamente irrevogável**.
- **Controle operacional:** [`docs/wireframes/images/README.md`](../../docs/wireframes/images/README.md), exclusivamente diretórios, nomes, inventário e matriz de estado.

Documentos históricos de construção do template (`PROCESSO-PRANCHA.md`, `WIREFRAME-TEXT.md`, `MONTAGEM-IMAGEM.md`) **não constituem Gates de aprovação das Telas** nem redefinem a composição selecionada. Suas regras técnicas comuns podem ser consultadas quando aplicáveis, sem executar novamente o processo de criação do template.

## 2. Três artefatos e processo linear bloqueante

**Wireframe Text da Tela:** especificação individual, anterior ao PNG; estabelece o conteúdo e a geometria da interface dentro do ViewPort.

**Tela de Referência:** imagem funcional isolada, `360 × 800 px`, construída e aprovada sem a Prancha.

**Prancha de Implementação:** nova imagem de apresentação, `1280 × 1920 px`, que utiliza o template vigente e recebe uma Tela já aprovada; **não** é uma edição do arquivo oficial congelado nem código de aplicativo.

```text
DOCUMENTO MESTRE + FICHA/TEXTFRAME DA INTERFACE
    ↓
WIREFRAME TEXT INDIVIDUAL DA TELA (tema/página/versão)
    ↓
VALIDAÇÃO TÉCNICA + APROVAÇÃO HUMANA DO WIREFRAME TEXT
    ↓
CONSTRUÇÃO DA TELA DE REFERÊNCIA ISOLADA (360 × 800)
    ↓
VALIDAÇÃO TÉCNICA + APROVAÇÃO HUMANA DA TELA
    ↓
VERIFICAÇÃO DA REFERÊNCIA OFICIAL VIGENTE (SPEC 2)
    ↓
REGISTRO DE COMPOSIÇÃO E PRODUÇÃO DA PRANCHA DE IMPLEMENTAÇÃO
    ↓
VALIDAÇÃO TÉCNICA + APROVAÇÃO HUMANA DA PRANCHA
    ↓
VERSIONAMENTO / RASTREABILIDADE / REFERÊNCIA PARA EVOLUÇÃO FUTURA
```

Nenhuma etapa adquire aprovação por herança. Falta de documento, aprovação, geometria aplicável ou arquivo físico gera `BLOQUEADO POR GATE ANTERIOR` ou pendência fundamentada; jamais uma composição inferida visualmente.

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

Paginação: se o conteúdo exceder `360 × 800`, manter o ViewPort e criar páginas sequenciais, repetindo apenas elementos persistentes, continuando o conteúdo no ponto correto; não comprimir artificialmente, omitir ações ou inventar paginação funcional. Adotar indicador de rolagem apenas quando houver requisito ou necessidade documentada.

Equivalência entre `white` e `black`: informações, campos, ações/destinos, estados, hierarquia, agrupamentos, proporções, navegação, ordem de leitura, tipos de componentes, tipografia e paginação devem ser equivalentes; as diferenças autorizadas são as regras de tokens/paleta específicas de cada tema.

Cada revisão preserva as versões aprovadas; não sobrescrever silenciosamente. Mudanças que afetem paginação exigem revisar os nomes `<PÁGINA>-<TOTAL>` de toda sequência dependente, mantendo registro do que foi substituído. Para novas saídas, sempre vincular a versão **exata** do template vigente no instante da aprovação, com caminho e hash — uma seleção futura não altera artefatos históricos.

## 4. Etapa 1 — Especificar e aprovar o Wireframe Text da Tela

1. Ler a ficha, o Textframe, ações, destinos, campos, estados, retorno, regras transversais e interfaces relacionadas no Documento Mestre, para o ID efetivo.
2. Criar o documento com o contrato integral de [`WIREFRAME-TEXT-TELA.md`](WIREFRAME-TEXT-TELA.md), incluindo as posições locais dentro de `360 × 800`, hierarquia, textos, estados, tokens do tema e justificativa de paginação.
3. Identificar lacunas antes de desenhar. `REPRESENTÁVEL` quando documentado; `AMBIGUIDADE DE REPRESENTAÇÃO` exige decisão explícita registrada antes de congelar geometria; `CONTRADIÇÃO DOCUMENTAL` bloqueia; `REQUISITO NOVO` é encaminhado ao processo formal da baseline, não incorporado.
4. Verificar texto, cálculos, cobertura funcional e impossibilidade de dependências circulares. Registrar `AGUARDANDO APROVAÇÃO`.
5. Exigir aprovação humana expressa, identificada e registrada no próprio Wireframe Text. Somente `APROVADO E CONGELADO` permite avançar ao PNG.

**É proibido construir primeiro o PNG e depois inferir ou redigir retroativamente seu Wireframe Text.** A ordem vale para ambas as variações.

## 5. Etapa 2 — Construir e aprovar a Tela de Referência

1. Ler o Wireframe Text da Tela **aprovado** e as invariantes em `REGRAS-TECNICAS.md`.
2. Abrir o PNG de ViewPort oficial **do mesmo tema**, identificado pela SPEC 2, somente como referência dimensional e técnica. Ele contém **demonstração**, não deve ser copiado como conteúdo funcional nem editado.
3. Construir em canvas **independente de `360 × 800 px`**, orientação retrato, sem criar moldura de aparelho e sem trabalhar dentro de uma Prancha; largura útil interna `336 px` com margens de `12 px`.
4. Materializar fielmente cada região e componente conforme Wireframe Text da Tela; não inventar conteúdo nem usar posições demonstrativas do template. Se não couber, corrigir a especificação por revisão aprovada ou paginar segundo a norma, nunca comprimir silenciosamente.
5. Salvar PNG no caminho especificado na seção 3. Reabrir e verificar dimensões físicas, textos, componentes, estados, geometria, tokens, margens, acessibilidade e paginação contra o Wireframe Text aprovado.
6. Registrar caminho, nome, versão, SHA-256, critérios técnicos, divergências e decisão humana **específica da Tela**. Só após `APROVADO E CONGELADO` existe Tela apta a ser apresentada.

Uma correção que mude o conteúdo aprovado do Wireframe Text exige sua revisão/versão e nova aprovação. Uma aprovação da Tela não pode suprir a ausência de aprovação prévia do texto.

## 6. Etapa 3 — Usar a referência vigente e construir a Prancha de Implementação

1. Consultar **SPEC 2** e seu registro de vigência: verificar modelo, PNG, Wireframe Text de referência, ViewPort, temas e hashes. Atualmente é Modelo C, white v02 e black v01; a regra deve funcionar se isso mudar futuramente.
2. Ler a geometria estrutural e os campos de apresentação **expressamente autorizados** no modelo aprovado. A Prancha de Implementação é um **novo artefato**; não editar, reexportar nem sobrescrever qualquer arquivo de `template/`.
3. Criar o **registro textual específico de composição** no caminho da seção 3: ID/tema/página/versão, requisitos de apresentação, caminhos e hashes do Wireframe Text aprovado e da Tela aprovada, versão exata da referência e hashes dos três artefatos oficiais, dimensões, região de inserção, coordenadas `x/y`, escala `1:1`, campos variáveis, textos/metadados e validações. Esse registro especifica **somente os dados particulares da apresentação**, sem reproduzir ou reaprovar a estrutura fixa já congelada do template. Metadados mínimos a apresentar, quando aplicáveis: `Projeto: SaOr - Sales Order`; `Interface: <ID> — <Nome>`; `Baseline: v1.0`; `Etapa: Wireframe Conceitual em Imagem`; `Variação: Claro | Escuro`; `Status: PENDENTE | EM VALIDAÇÃO | AJUSTES NECESSÁRIOS | APROVADO`; `Página: <XX>/<YY>`; `Versão: vNN`; ViewPort, orientação, canvas, escala e fonte técnica conforme normas vigentes. Mostrar somente tokens e notas efetivamente aplicados à representação.
4. Se os campos variáveis não estiverem documentados ou a estrutura não comportar o conteúdo exigido, **bloquear** e solicitar análise de revisão do template; não inventar novas zonas, adaptar geometria, diminuir a Tela nem omitir informações. A revisão do template segue SPECs 1/2 e aprovação independente.
5. Produzir o novo PNG `1280 × 1920 px` com a estrutura fixa da referência preservada. Inserir o PNG de Tela aprovado na região indicada em `360 × 800`, **sem redimensionar, recortar, recolorir ou alterar pixels**. Somente campos previamente variáveis podem receber dados da interface.
6. Conferir o novo PNG com o registro de composição e os arquivos oficiais. Não aplicar os Gates 1–6 de **construção de novo template** a uma Prancha de Implementação; sua aprovação é a do artefato funcional descrita na seção 7.

O registro de composição **não é outro Wireframe Text de construção de template**. Sua função é registrar as escolhas da aplicação da referência fixa naquela interface. A especificação interna da Tela permanece no seu próprio Wireframe Text.

## 7. Validação, aprovação e independência dos resultados

Antes de solicitar aprovação humana da Prancha de Implementação, conferir:

```text
[ ] Wireframe Text da Tela aprovado antes do PNG da Tela
[ ] Tela PNG existe, foi aprovada e mede exatamente 360 × 800
[ ] conteúdo e estados idênticos ao Wireframe Text da Tela
[ ] referência de template vigente identificada por tema, versão e hashes
[ ] os arquivos oficiais e históricos do template permanecem íntegros
[ ] PNG da Prancha é novo e mede exatamente 1280 × 1920
[ ] região e coordenadas de inserção comprovadas pelo modelo oficial
[ ] Tela presente em 1:1, comparada pixel a pixel na região da Prancha
[ ] campos variáveis e metadados conferem com o registro de composição
[ ] não existe alteração da geometria estrutural congelada
[ ] correspondência white/black, conteúdo, estados e paginação conferidos
[ ] versão, caminhos, hashes e aprovações independentes registrados
[ ] nenhum texto foi cortado, comprimido ou colocado fora dos cards
[ ] ícones, medidas, espaçamentos, componentes e tokens utilizados conferidos
[ ] nenhuma informação temporária de conversas ou do processo interno foi incorporada à imagem
```

Aprovador registra decisão humana expressa para a Prancha, independente das duas aprovações anteriores. Falha da Tela bloqueia a composição até nova aprovação dela; falha da apresentação corrige **somente o novo artefato e seu registro**, sem adulterar o template ou a Tela aprovada.

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
```

As evidências de aprovação devem existir nos arquivos do repositório, não somente em conversa ou ferramenta externa. A cadeia de aprovação não pode ser invertida ou herdada.

## 9. Limite de implementação em código

As Telas e Pranchas desta etapa são **referências documentais e visuais**, não interfaces de software já implementadas. Elas fornecem contrato de requisitos e fidelidade para etapas posteriores do Documento Mestre (design, Figma, protótipo e MVP). A implementação em código deverá referenciar os artefatos aprovados, validar conteúdo, navegação, estados e responsividade contra a arquitetura e os componentes **efetivamente formalizados naquela fase**. Não presumir framework, estrutura de frontend/backend, APIs ou componentes inexistentes no repositório atual.

**Critério de conclusão da SPEC 3:** é possível identificar e reconstruir cada Tela e sua apresentação no modelo aprovado, com origem, versões e aprovações próprias, apenas pelos arquivos versionados do projeto.
