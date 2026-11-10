# SaOr — Contrato especializado de auditoria dos processos de wireframes

## 1. Natureza, autoridade e limite de aplicação

### 1.1. Função deste contrato

Este contrato é a **especialização operacional** de [`PROCESSO-AUDITORIA.md`](../PROCESSO-AUDITORIA.md) para os objetos governados pelas SPECs 1, 2 e 3 do domínio de wireframes. Define **o que confrontar, onde obter a regra, qual evidência verificar, como registrar o resultado e quando impedir avanço**; não cria uma SPEC 4 de construção de wireframes, não escolhe um template, não altera requisitos funcionais, não substitui decisões humanas e não aprova artefatos.

Aplicar primeiro o [processo global de alteração assistida](../../PROCESSO-ALTERACAO-ASSISTIDA.md), depois a [SPEC genérica de auditoria](../PROCESSO-AUDITORIA.md) e, para cada objeto, a norma especializada competente. A autoridade do **requisito ou Gate** é sempre a fonte especializada identificada abaixo; este contrato apenas torna sua auditoria reproduzível. Uma contradição não pode ser resolvida alterando este contrato para impor outra regra: registrar as fontes, os trechos, a autoridade e o bloqueio específico, solicitando decisão quando indispensável.

A aplicação é independente do identificador da interface, do nome do modelo, de uma versão concreta e de qualquer conversa. Uma implementação anterior pode servir como **amostra de teste**, nunca como fonte de regras para outra. A existência deste contrato não autoriza escrita em `.specs/`, `.skill/`, `docs/`, imagens ou qualquer outro caminho.

### 1.2. Três trilhas distintas, sem herança de Gates

| Trilha auditada | Objeto e autoridade | O que este contrato deve verificar | O que é proibido inferir |
|---|---|---|---|
| **SPEC 1 — Construção do template** | [PROCESSO-PRANCHA.md](../../wireframes/PROCESSO-PRANCHA.md), [WIREFRAME-TEXT.md](../../wireframes/WIREFRAME-TEXT.md), [MONTAGEM-IMAGEM.md](../../wireframes/MONTAGEM-IMAGEM.md) | Canvas vazio, definição e aprovação progressiva de geometria, Wireframe Text de template, execução da imagem e aceite final | Que o processo de construir o modelo deve ser refeito por interface ou pela mera seleção de versão vigente |
| **SPEC 2 — Seleção e vigência** | [REFERENCIA-TEMPLATE-OFICIAL.md](../../wireframes/REFERENCIA-TEMPLATE-OFICIAL.md) e [Registro de Controle do Template Oficial](../../../docs/wireframes/images/Registro_Controle_Template_Oficial.md) | Seleção expressa por tema, identidade dos seis objetos oficiais, origens, versões, decisões, integridade e contrato concreto de uso quando necessário | Que versão mais alta, nome, README operacional ou imagem similar determina vigência; que selecionar equivaleria a construir ou aprovar novo modelo |
| **SPEC 3 — Interface funcional** | [PROCESSO-TELA-PRANCHA.md](../../wireframes/PROCESSO-TELA-PRANCHA.md) e [GATE-IMPLEMENTACAO-TELAS.md](../../wireframes/GATE-IMPLEMENTACAO-TELAS.md) | Inventário GI-0, PNG visual GI-1, TextFrame derivado GI-2, nova Prancha GI-3, aceite GI-4, com controles por tema, página, estado e conjunto | Que o TextFrame pode preceder o PNG, que aceites são herdados de outra interface, tema ou versão, ou que os Gates 1–6 da SPEC 1 se aplicam à Tela funcional |

### 1.3. Fontes complementares e responsabilidades limitadas

| Fonte física a consultar | Competência para a auditoria | Limite de interpretação |
|---|---|---|
| [REGRAS-TECNICAS.md](../../wireframes/REGRAS-TECNICAS.md) | Canvas, viewport, margens, grid, paleta técnica, componentes, estados e acessibilidade estrutural, conforme objeto e momento | Não seleciona modelo nem define conteúdo individual de interface |
| [WIREFRAME-TEXT-TELA.md](../../wireframes/WIREFRAME-TEXT-TELA.md) | Contrato do TextFrame **posterior** ao PNG aprovado de GI-1 | Não autoriza TextFrame prévio nem aprova conteúdo funcional por semelhança |
| [Documento Mestre](../../../docs/Documento_Mestre.md) e [Registro de Fechamento](../../../docs/Registro_Fechamento_Documento_Mestre.md) | Autoridade da ficha, Textframe funcional, fluxo, estado, navegação, textos e baseline | Não alterar requisitos para justificar PNG/Prancha ou resultado do auditor |
| [README operacional de imagens](../../../docs/wireframes/images/README.md) | Inventário de arquivos, diretórios, matriz agregada e status registrados | Não substitui aprovação, seleção de template ou ficha funcional |
| [Registro de padrão visual funcional](../../../docs/wireframes/images/Registro_Padrao_Visual_Funcional_Mobile.md) | Identidade e vigência do perfil visual funcional no escopo correspondente | Não deduzir vigência pelo maior sufixo de versão |
| [Contrato técnico de utilização do Modelo C](../../../docs/wireframes/images/contratos/USO-TEMPLATE-C.md) | **Exemplo de contrato concreto existente**, cujos parâmetros só valem para o modelo, temas, versões e hashes ali declarados | Não transportar coordenadas, campos, status ou substituições para modelo futuro sem contrato próprio |
| [Skill documental](../../../.skill/saor-analise-documental/SKILL.md) e [Contrato Editorial](../../../.skill/saor-analise-documental/references/CONTRATO-EDITORIAL.md) | Geração, atualização, análise, migração e estrutura dos três registros Markdown da SPEC 3 | Não aprova Gates nem substitui validação de conteúdo ou identidade física |
| [Formato de relatório da Skill documental](../../../.skill/saor-analise-documental/references/FORMATO-RELATORIO.md) | Critérios editoriais de relatório quando a Skill documental for o objeto da operação | Não cria requisitos funcionais ou um novo Gate |

A lista é um **mapa de autoridades**, não a afirmação de que qualquer objeto da lista esteja vigente, íntegro ou aprovado em toda base futura. Conferir existência, conteúdo, hashes, registro de seleção e aplicabilidade no clone efetivo antes de usar. Se norma ou contrato mudar, registrar o novo hash, confrontar as cláusulas e revalidar este contrato na parte impactada; não pressupor sua compatibilidade só por manter o mesmo caminho.

### 1.4. Restrições físicas e de preservação

`assets/` permanece excluído: não abrir, enumerar internamente, decodificar nem alterar sem autorização específica. Objetos classificados pela fonte normativa como **LEGADOS** ficam preservados e fora da releitura de conteúdo por padrão; se indispensáveis, justificar e solicitar autorização. Arquivos antigos sem classificação normativa de LEGADO não recebem essa classificação por nome ou data. A documentação aprovada, templates congelados, origens oficiais, decisões e artefatos de outras interfaces permanecem preservados. A auditoria é inicialmente **somente leitura**.

## 2. Contrato de entrada, seleção da trilha e exigibilidade

### 2.1. Identificação obrigatória antes da auditoria

Registrar, antes de qualquer conclusão, a fonte física autorizada (caminho, formato, tamanho e SHA-256 do contêiner quando aplicável), o objeto, a unidade auditada, o domínio, o modo `SOB_DEMANDA` ou `ENCERRAMENTO`, o estágio documentado, as versões formais, o tema/página/estado aplicáveis, a autoridade responsável e as exclusões. Verificar os membros elegíveis do ZIP, seu CRC/tamanho, tipo, SHA-256 e segurança de caminhos; detectar duplicidades, links/entradas especiais indevidas e alterações de inventário. Não usar GitHub ou memória para substituir ZIP local disponibilizado. O hash calculado não comprova, por si só, conteúdo correto ou aceite.

Em primeira base não validada, seguir a leitura integral dos arquivos elegíveis exigida pelo processo global. Em base incremental com fonte anterior **fisicamente acessível**, inventário de hashes, registro de leituras e mesmo escopo comprovados, comparar caminho, tamanho e SHA-256 e reinterpretar arquivos novos/alterados e dependências afetadas. Sem essas condições, comparação incremental é `NÃO VALIDADA`. Leitura de bytes não equivale à inspeção semântica ou visual.

### 2.2. Selecionar por autoridade, não por identificador

1. Se a atividade consiste em **definir/construir/revisar o template-modelo**, selecionar a trilha da SPEC 1 e seus Gates 1–6/PNG. Não executar GI-0 a GI-4 por esse motivo.
2. Se consiste em **identificar/ativar/substituir a referência aprovada vigente**, selecionar a SPEC 2 e seu registro de seleção. A SPEC 1 só será examinada na extensão necessária a comprovar uma nova versão formal do template; não reexecutá-la quando a seleção já estiver aprovada.
3. Se consiste em **produzir/regularizar uma interface funcional**, selecionar a SPEC 3, a ficha funcional, os GI-0 a GI-4 e a referência da SPEC 2 utilizada na data pertinente. Não importar Gates anteriores nem componentes demonstrativos do template.
4. Se o pedido engloba mais de uma trilha, criar **matrizes independentes por objeto**, com vínculos explícitos entre elas, sem mesclar aprovação, vigência e resultado técnico.
5. Se a natureza do objeto não puder ser comprovada, registrar `NÃO VALIDADO` e suspender apenas os testes que dependem dessa seleção; não classificar a partir de pasta, prefixo ou nome semelhante.

### 2.3. Modo e estágio: conjunto efetivamente exigível

- `SOB_DEMANDA`: auditar o estado real, os Gates já exigíveis e as dependências do próximo ato. Gates legitimamente futuros ficam `PENDENTE`, com pré-condições, e não são erros já ocorridos; falta de decisão humana bloqueia somente o avanço dependente.
- `ENCERRAMENTO`: conferir **todos** os Gates e entregáveis obrigatórios da trilha, aprovações individuais/de conjunto, integridade física, documentação e preservações. Somente emitir `CONFORME PARA ENCERRAMENTO` se a cobertura integral aplicável estiver demonstrada, sem impedimentos reais pendentes; ressalvas aceitas devem ser explicitadas, nunca convertidas em conformidade técnica irrestrita.
- Após edição autorizada: independentemente do modo, executar segunda auditoria dos bytes finais e de suas dependências. A auditoria de encerramento não substitui a comprovação de incorporação física posterior pelo responsável.

### 2.4. Unidade de rastreabilidade

Para SPEC 1, unidade = **prancha-modelo + tema + versão formal + etapa/Gate**. Para SPEC 2, unidade = **referência selecionada + tema + versão + objetos oficiais + decisão de vigência**. Para SPEC 3, unidade = **ID funcional + tema + página/total + estado/posição de rolagem + versão formal + Gate**, acrescentando a avaliação de **conjunto White/Black** quando exigida. Construir matriz `unidade → requisito → fonte e trecho → objeto → evidência → teste → estado → decisão/dependente` sem eliminar variantes reais nem inventar variantes ausentes.

## 3. Inventário físico e mapa de dependências

### 3.1. Fontes e arquivos por papel

Classificar cada arquivo antes de compará-lo: (a) autoridade normativa; (b) ficha funcional; (c) referência oficial/vigência; (d) contrato concreto de aplicação; (e) objeto visual do template; (f) PNG de Tela; (g) TextFrame da Tela; (h) Prancha funcional; (i) Controle GI-0/GI-1; (j) Composição GI-3/GI-4; (k) evidência de submissão/decisão; (l) inventário operacional. A classificação deve resultar do **conteúdo e dos contratos efetivos**, não exclusivamente do caminho.

Inventário mínimo por membro elegível: `caminho relativo → papel → tipo real → tamanho → CRC (se ZIP) → SHA-256 → operação de leitura/inspeção → estado normativo → referência que o utiliza → limitações`. Para PNG relevante, abrir/decodificar e conferir dimensão, perfil e conteúdo visual realmente representado. Para imagem usada em comparação pixel a pixel, registrar região, método, quantidade de pixels confrontados e quantidade de diferenças. Nenhuma inspeção visual pode ser alegada apenas por cálculo de hash.

### 3.2. Cadeias de dependência distintas

| Trilha | Cadeia a reconstruir | Relação que não pode ser presumida |
|---|---|---|
| SPEC 1 | Registro de Gate no Wireframe Text específico → geometria aprovada → artefato PNG → aprovação humana final | Que um outro modelo aprovado possua os mesmos parâmetros |
| SPEC 2 | Decisão de seleção → registro de vigência → seis artefatos oficiais/origens → versão e contrato de uso | Que a referência com nome/versão maiores seja vigente |
| SPEC 3 | Documento Mestre → Controle GI-0/GI-1 → PNG aprovado → TextFrame/GI-2 → contrato concreto/modelo vigente na data → nova Prancha e Composição/GI-3 → aprovação GI-4 → README operacional | Que o README ou uma composição prove sozinho todos os Gates |

Em cada vínculo verificar caminho, arquivo real, identificação, versão, tema, data/estado e **natureza do SHA** (§10). Uma referência antiga pode representar decisão real; uma referência corrente deve apontar para bytes atuais. A cadeia será auditada pelo contexto de cada campo, não por busca e substituição global de hashes. Registrar ciclos de dependência e autorreferência sem tentar estabilizar valores por substituições repetidas.

### 3.3. Aplicabilidade da resolução e do perfil

A SPEC 3, em seu escopo Mobile atual, exige Tela `360 × 800 px`, Prancha `1280 × 1920 px`, temas `white`/`black` e caminhos Mobile. Os diretórios reservados a Tablet, Notebook e Desktop **não** são entregáveis nem dão origem a Gates no MVP indicado pela norma. Antes de impor tais dimensões em base futura, verificar a vigência e o escopo da SPEC e dos registros aplicáveis. Perfis Mobile e identidade visual são selecionados pelas fontes próprias: não deduzir de uma Tela anterior nem de nome de arquivo.

## 4. Auditoria especializada da SPEC 1 — construção do template

### 4.1. Provas de início e ordem obrigatória

A autoridade é [SPEC 1, §§1–2.1](../../wireframes/PROCESSO-PRANCHA.md), em conjunto com [WIREFRAME-TEXT.md](../../wireframes/WIREFRAME-TEXT.md), [MONTAGEM-IMAGEM.md](../../wireframes/MONTAGEM-IMAGEM.md) e [REGRAS-TECNICAS.md](../../wireframes/REGRAS-TECNICAS.md). O processo inicia por **canvas vazio**; define título, viewport e demais elementos em sequência; aprova o Wireframe Text do template **antes** de construir seu PNG. Isto é diferente da SPEC 3 e deve ser avaliado apenas para a prancha-modelo. Se o objeto for apenas uma interface que utiliza modelo aprovado, esta trilha é `NÃO APLICÁVEL` com justificativa, e nunca reaberta por padrão.

Para cada novo modelo/versão formal submetido à SPEC 1, conferir a existência do Wireframe Text específico, as decisões por Gate, as medidas, a ordem dos eventos, o PNG final e o confronto da imagem com o texto aprovado. Evidência de um modelo anterior não é automaticamente evidência de outro.

### 4.2. Matriz obrigatória dos Gates da SPEC 1

| Controle | Tipo e fonte | Evidência e teste a executar | Resultado bloqueante |
|---|---|---|---|
| `S1-G1` Canvas | Técnico; SPEC 1 §3, Gate 1 | Canvas real `1280×1920`, orientação e margens previstas; evidência de que elementos posteriores não foram antecipados; registro do Gate no Wireframe Text | Dimensões incorretas ou etapas antecipadas; não declarar aprovado por arquivo existente |
| `S1-G2` Título/cabeçalho | Humano; SPEC 1 §4, Gate 2 | Conteúdo exato, `x/y/w/h`, sub-regiões, tipografia, alinhamento, padding, divisores, metadados, fontes de marca; decisão explícita do responsável e congelamento antes da etapa seguinte | Sem aceitação do cabeçalho não calcular a etapa seguinte como definitiva |
| `S1-G3` Viewport técnico | Humano; SPEC 1 §5, Gate 3 | Imagem de referência válida para o tema quando aplicável, `360×800` físico, escala `1:1`, coordenadas, cotas e relação com cabeçalho aprovado; aprovação e registro | Viewport redimensionado, geométrica de outro modelo inferida, decisão ausente |
| `S1-G4` Área restante | Técnico; SPEC 1 §6, Gate 4 | Cálculo reproduzível por canvas/margens/cabeçalho/viewport/gaps já aprovados; caixa e limites da área restante; ausência de movimento de regiões congeladas | Coordenadas inconsistentes ou cálculo feito antes de G2/G3 |
| `S1-G5` Demais elementos | Técnico; SPEC 1 §7, Gate 5 | Inventário completo dos elementos, conteúdo, dimensões e posições próprias, legibilidade, não extravasamento, tokens aprovados, paleta e contraste segundo a regra técnica | Elemento sem conteúdo/geometria comprovados, token fora de norma, região congelada alterada |
| `S1-G6` Wireframe Text completo | Humano; SPEC 1 §8, Gate 6 | Documento reproduzível sem inferência, todas as cotas, fontes e conteúdos fechados; ausência de lacunas materiais; decisão humana expressa | Sem G6 aprovado não iniciar produção do PNG |
| `S1-PNG` Execução + aprovação final | Humano; SPEC 1 §§9–10 | Imagem criada **depois** de G6, a partir do canvas, confronto PNG × Wireframe Text (conteúdo, posição, dimensão, tokens e states), inspeção visual e aprovação humana final vinculada ao objeto | PNG diferente do texto ou sem aceite; corrigir primeiro contrato textual e reavaliar Gates afetados, não só a imagem |

Os Gates técnicos são fechados por comprovação técnica; **G2, G3, G6 e PNG final** exigem decisão humana. Confrontar os estados permitidos da SPEC 1 (`PENDENTE`, `EM DEFINIÇÃO`, `AGUARDANDO APROVAÇÃO`, `APROVADO E CONGELADO`, `BLOQUEADO POR GATE ANTERIOR`, `NÃO APLICÁVEL`) com as evidências próprias do objeto. Se um Gate congelado foi reaberto, verificar o bloqueio dos dependentes e os novos aceites competentes; não criar nova aprovação por execução do auditor.

### 4.3. Verificações textuais e visuais adicionais

O Wireframe Text do template não é o TextFrame individual da Tela e **não usa** automaticamente os três templates editoriais da Skill de SPEC 3. Avaliar sua composição pelo [WIREFRAME-TEXT.md](../../wireframes/WIREFRAME-TEXT.md), inclusive conteúdo por elemento, geometria, paleta, campos de processo e evidência das aprovações. Para a imagem, utilizar o método de [MONTAGEM-IMAGEM.md](../../wireframes/MONTAGEM-IMAGEM.md): layout sobre tamanho final, hierarquia, controle de não regressão, exportação, revisão visual e distinção entre revisão do mesmo frame, mudança estrutural e versionamento conforme seus §§19–20. Não aplicar a esse objeto a sequência inversa PNG→TextFrame da SPEC 3.

**Retorno:** uma incompatibilidade entre PNG e Wireframe Text não autoriza ajustar arbitrariamente apenas o bitmap. Identificar a etapa de definição afetada, conferir decisões congeladas e exigir o retorno e o aceite estabelecidos pela SPEC 1. Nenhuma auditoria isolada cria novo template ou modifica o oficial.

## 5. Auditoria especializada da SPEC 2 — referência vigente e congelamento

### 5.1. Verificação da autoridade de seleção

Abrir o [Registro de Controle do Template Oficial](../../../docs/wireframes/images/Registro_Controle_Template_Oficial.md), localizar a decisão **vigente por tema** na data pertinente ao objeto auditado e conferir sua autoridade e eventual substituição posterior. O [README operacional](../../../docs/wireframes/images/README.md) pode localizar arquivos, mas não selecionar a referência. Não escolher pela maior versão, timestamp, nome semelhante, contrato ilustrativo nem memória. A SPEC 2 não reexecuta Gates da construção de modelo já aprovado.

### 5.2. Teste da integridade dos seis artefatos oficiais

Para cada tema (`white` e `black`), o registro deve permitir identificar separadamente **PNG do template, Wireframe Text do template e PNG do viewport demonstrativo**: são seis objetos no conjunto de dois temas, cada um com caminho, versão apropriada, origem/cópia oficial e SHA-256. Para cada objeto: confirmar existência, bytes, tipo, imagem decodificável quando aplicável, dimensões, SHA-256 declarado versus físico, identidade binária entre origem e cópia quando exigida e ausência de alteração de artefato congelado. A inspeção da estrutura geométrica exige abrir também o Wireframe Text aprovado; calcular hash sem confrontar as cotas não satisfaz a SPEC 2.

Não tratar ausência de um arquivo normativamente excluído ou formalmente LEGADO como erro de inventário; se tal arquivo for indispensável para provar a seleção, registrar o impedimento e solicitar autorização antes de acessá-lo. Um registro antigo de modelo substituído **não torna aquele modelo vigente**. Preservar versão formal anterior quando definida pela norma.

### 5.3. Contrato concreto de utilização

Para consumo em SPEC 3, conferir que o modelo/tema/versões selecionados possuam **contrato técnico de aplicação explícito**, íntegro e efetivamente vinculado aos hashes aprovados, como exige a [SPEC 2 §4](../../wireframes/REFERENCIA-TEMPLATE-OFICIAL.md) e a [SPEC 3 §6.1](../../wireframes/PROCESSO-TELA-PRANCHA.md). Ler o contrato completo: região de ViewPort com `x/y/w/h`, escala, áreas fixas e variáveis, textos demonstrativos substituíveis, campos e STATUS, regras de recorte, preservações e decisões. Validar a correspondência dessas regras ao Wireframe Text e à imagem oficial da mesma versão. **Nunca** transferir parâmetros do contrato de outro modelo; o [USO-TEMPLATE-C](../../../docs/wireframes/images/contratos/USO-TEMPLATE-C.md) só pode ser aplicado ao conjunto que ele identifica.

Se não existir contrato válido para a referência efetivamente selecionada, marcar **uso funcional da referência `BLOQUEADO`**, sem editar a cópia congelada e sem inventar coordenadas; as demais conclusões sobre existência ou vigência da seleção podem permanecer válidas, se comprovadas. Em auditoria histórica de interface concluída, verificar o contrato e a seleção efetivamente utilizados naquela criação: mudança posterior de vigência não exige migração retroativa.

### 5.4. Estados e encerramento da SPEC 2

Registrar separadamente `APROVADO E CONGELADO` da **versão física específica**, `VIGENTE` da **seleção ativa para novas saídas**, e a decisão com tema, data, caminho e hash. Em substituição formal, exigir necessidade comprovada, análise de dependentes, aprovação da nova versão pelo processo competente, ativação no registro e preservação da versão anterior. O auditor não decide qual versão deveria estar vigente nem altera o Registro de Controle; apenas confronta fatos e identifica eventual decisão faltante.

## 6. Auditoria especializada da SPEC 3 — interfaces funcionais

### 6.1. Identidade de cada unidade e origem funcional

Ler integralmente a ficha, o Textframe funcional e as regras transversais aplicáveis no [Documento Mestre](../../../docs/Documento_Mestre.md), inclusive origem, condição de apresentação, conteúdo literal, ações, destino/retorno, estados, paginação e dependências. A fonte funcional é a baseline, não o PNG ou documento de outra interface. Conferir o registro de fechamento dessa baseline quando relevante. Identificar o objeto por **ID/tema/página/total/estado/versão**, e não inferir funcionalidade pela proximidade entre IDs ou pelo nome do arquivo.

Conforme a [SPEC 3 §3](../../wireframes/PROCESSO-TELA-PRANCHA.md), para cada `<nome-base>` efetivo devem ser resolvidos os caminhos aplicáveis abaixo, quando seu Gate já for exigível:

| Objeto | Caminho canônico relativo à raiz do repositório | Regra de verificação |
|---|---|---|
| Controle GI-0/GI-1 | `docs/wireframes/images/<tema>/telas/controle/<nome-base>.md` | Registro de inventário e decisões anterior ao TextFrame; não é segunda Tela |
| PNG visual de Tela | `docs/wireframes/images/<tema>/telas/design/01_Mobile_360x800/<nome-base>.png` | Fonte visual do TextFrame; bytes aprovados em GI-1 |
| TextFrame da Tela | `docs/wireframes/images/<tema>/telas/wiframetext/<nome-base>.md` | Derivado **após** GI-1; exige aprovação GI-2 |
| Prancha funcional | `docs/wireframes/images/<tema>/telas/pranchas/01_Mobile_360x800/<nome-base>.png` | Nova cópia do modelo vigente; viewport fiel |
| Composição GI-3/GI-4 | `docs/wireframes/images/<tema>/telas/pranchas/01_Mobile_360x800/wiframetext/<nome-base>.md` | Método, identidade das fontes, verificações e GI-4 |

`<nome-base>` tem identidade canônica `<ID>-<PÁGINA>-<TOTAL>_v<VERSÃO>` nos formatos estipulados pela SPEC 3. Sufixos de estado só se aplicam a estados adicionais **previstos e aprovados**; preservar exceções de nome históricas reconhecidas pelas normas sem renomear automaticamente. Diretórios reservados para outros tamanhos não são exigíveis pelo simples fato de existirem.

### 6.2. Matriz de verificação GI-0 a GI-4

| Controle | Norma responsável | Pré-condição e evidências obrigatórias | Teste e condição impeditiva |
|---|---|---|---|
| `S3-GI0` Inventário | [Gate de Telas §2](../../wireframes/GATE-IMPLEMENTACAO-TELAS.md) e SPEC 3 §4 | Ficha e Textframe funcional efetivos, matriz de requisitos com fonte, tema, estados, continuidade, padrões selecionados, distinção entre conteúdo funcional e demonstração do template, Controle persistente GI-0 | Ausência de requisito essencial ou incompatibilidade que impeça representar fielmente: `BLOQUEADO` para produzir PNG; não inventar solução visual |
| `S3-GI1` PNG da Tela | [Gate de Telas §3](../../wireframes/GATE-IMPLEMENTACAO-TELAS.md) e SPEC 3 §4 | GI-0 comprovado; PNG isolado real antes do TextFrame, todos os temas/estados/páginas exigíveis, dimensão vigente, inspeção visual, decisão humana datada com nome, tema, versão e SHA-256 no Controle | Comparar conteúdo real ao requisito e padrões, sem extra/omissão/truncamento; PNG alterado depois do aceite exige novo GI-1 para novos bytes, não simples troca de hash |
| `S3-GI2` TextFrame e conjunto | [Gate de Telas §4](../../wireframes/GATE-IMPLEMENTACAO-TELAS.md) e [Contrato do TextFrame da Tela](../../wireframes/WIREFRAME-TEXT-TELA.md) | GI-1 anterior com PNG por hash; documento derivado, texto fiel, caixas `x/y/w/h` mensuradas, vínculo com todos os estados/páginas e decisão expressa para **PNG + TextFrame**, por tema | Confrontar elemento por elemento PNG↔TextFrame↔cotas↔requisito; sem raster comprovado ou com discrepância, não declarar GI-2; mudança de PNG remete ao GI-1 |
| `S3-GI3` Composição | [Gate de Telas §5](../../wireframes/GATE-IMPLEMENTACAO-TELAS.md), SPEC 3 §§6–6.3 e contrato concreto da referência | GI-2 válido; nova cópia do template selecionado e íntegro; contrato concreto de aplicação; substituição inicial do viewport, preenchimento de campos e itens variáveis, registro de composição | Confrontar recorte **pixel a pixel** com PNG aprovado, sem resize/recolor; verificar regiões fixas, Item 10/14, STATUS e metadados; qualquer contrato faltante bloqueia montagem, não autoriza inventar valores |
| `S3-GI4` Aceite final | [Gate de Telas §6](../../wireframes/GATE-IMPLEMENTACAO-TELAS.md), SPEC 3 §7 | Pranchas `1280×1920` por página/tema; GI-3 conforme; provas, hashes, textos, conjunto de estados e páginas, decisões individuais das Pranchas e decisão **do conjunto White/Black**, quando exigido; matriz operacional coerente | Sem decisões humanas precisas não declarar `APROVADO E CONGELADO`; existência da imagem, STATUS impresso ou validador técnico não substituem aceite |

**Condição de sequência:** `GI-0 → PNG → GI-1 → TextFrame → GI-2 → GI-3 → GI-4`. O Controle GI-0/GI-1 deve existir com evidências antes do TextFrame. O TextFrame não pode ser usado para inventar a proposta visual; a Prancha não é fonte alternativa dos requisitos da Tela. Não herdar aceites de outra página, tema, estado, versão ou interface. A auditoria de um objeto já encerrado deve reconstruir a cronologia e observar decisões posteriores válidas, em vez de reexecutar Gates por padrão.

### 6.3. Inspeção visual e geométrica auditável

Para cada PNG exigível, decodificar o arquivo e registrar dimensões reais, hash, tema, página, estado, textos e componentes efetivamente visíveis. Inspecionar hierarquia, recortes, colisões, truncamento, cores e elementos declarados, confrontando com requisitos e tokens aplicáveis; marcar propriedades não recuperáveis do raster como `NÃO VALIDADO` em vez de afirmar dados paramétricos que não foram medidos. Para TextFrame, conferir caixas inteiras `x/y/w/h`, referencial, origem da medida e relação entre componentes/estados; não aceitar coordenada aproximada como cota exata.

Para cada Prancha, abrir o contrato concreto **da versão efetivamente utilizada** e extrair dele `x/y/w/h` e escala do viewport. Validar que a região possui mesma dimensão do PNG aprovado, não apresenta reamostragem nem diferenças de pixels. Registrar `quantidade de pixels confrontados`, `quantidade de diferenças`, `método de recorte/comparação` e `hashes dos objetos`. A igualdade pixel a pixel de um recorte **não** comprova a fidelidade do Item 10, Item 14 ou dos campos; confrontá-los separadamente. A geometria `x=40,y=272,w=360,h=800` existente no contrato Modelo C **não pode** ser codificada como constante universal do auditor.

Em rolagem, confrontar todas as páginas/posições reais, offsets/marcos, elementos fixos e roláveis, continuidade, ordem e ausência de omissão/duplicação; não criar página extra para resolver falta de espaço de Item 10/14 sem requisito de rolagem real. Em estados, exigir cada variante comprovadamente prevista ou aprovada, sem gerar variantes hipotéticas. White/Black podem ter diferenças cromáticas autorizadas, mas devem manter equivalência de semântica, componentes requeridos, navegação e paginação. Verificar a seleção do perfil Mobile por seu registro vigente, não por imitação de Tela anterior.

### 6.4. Estados, STATUS e limites de interpretação

A matriz operacional do [README de imagens](../../../docs/wireframes/images/README.md) deve refletir somente os Gates e decisões efetivamente concluídos, por tema e conjunto. Distinguir os estados **da interface**, os estados **do Gate**, os valores de **STATUS impressos na Prancha**, a **vigência da referência** e o parecer **do auditor**. Um `AGUARDANDO APROVAÇÃO` registrado no passado pode ter sido superado por decisão posterior; um `APROVADO` agregado não dispensa prova individual. Transcrever decisão posterior com sua data real; não reescrever a decisão original nem atribuir-lhe abrangência que não tinha.

O comportamento executável do produto (p. ex., eventos, fechamento, navegação, persistência e acessibilidade em execução) só pode ser classificado como comprovado se houver fonte e teste adequados. PNG e TextFrame de wireframe não provam, isoladamente, execução de software. Limites devem permanecer registrados para o processo futuro competente, sem criar regra funcional ou estado na interface.

## 7. Auditoria da Skill documental e dos três modelos oficiais da SPEC 3

### 7.1. Fonte e comando oficial de validação

O contrato da [Skill documental](../../../.skill/saor-analise-documental/SKILL.md), seu [Contrato Editorial](../../../.skill/saor-analise-documental/references/CONTRATO-EDITORIAL.md), o [Padrão Documental](../../../.skill/saor-analise-documental/references/PADRAO-DOCUMENTAL.md) e os três templates são as referências de **estrutura editorial** para as unidades da SPEC 3. Conferir fisicamente a existência e integridade do validador antes de executar. Os comandos previstos na SPEC 3 §3, a partir da raiz do clone, são:

```bash
python3 .skill/saor-analise-documental/scripts/validar_estrutura.py --templates
python3 .skill/saor-analise-documental/scripts/validar_estrutura.py --tipo controle --arquivo CAMINHO_DO_CONTROLE.md
python3 .skill/saor-analise-documental/scripts/validar_estrutura.py --tipo textframe --arquivo CAMINHO_DO_TEXTFRAME.md
python3 .skill/saor-analise-documental/scripts/validar_estrutura.py --tipo composicao --arquivo CAMINHO_DA_COMPOSICAO.md
```

`CAMINHO_DO_*` é uma variável operacional a substituir pelo arquivo físico elegível, não um nome literal a executar. Registrar comandos reais, versão/hash do validador, entradas, saída e código de retorno. Se o script não puder ser executado na fonte aprovada, registrar `NÃO VALIDADO` quanto ao teste oficial, explicando a limitação; comparação em memória ou verificação equivalente deve ser rotulada como equivalente, nunca falsamente declarada como execução do processo oficial por CLI.

A Skill governa o procedimento `GERAR`, `ATUALIZAR`, `ANALISAR` e `MIGRAR` somente dos três Markdown. `preparar_documento.py` copia um template para um rascunho quando autorizado: não preenche requisitos, não aprova Gates e **não** deverá ser executado para criar/editar registros durante auditoria somente leitura.

### 7.2. Mapa completo dos registros e respectivas seções

| Tipo de registro | Template canônico e estrutura | Campos/grupos a confrontar semanticamente |
|---|---|---|
| Controle GI-0/GI-1 | [CONTROLE-GI0-GI1.md](../../../.skill/saor-analise-documental/templates/CONTROLE-GI0-GI1.md), **10 H2 e 28 H3** | §1 identidade/fontes/limites; §2 inventário GI-0 e matriz; §3 fluxos/estados/paginação; §4 seleção/padrões; §5 lacunas/decisões; §6 resultado GI-0; §7 inspeção PNG GI-1; §8 decisão GI-1 e hash; §9 vínculo GI-2; §10 estado vigente e eventos |
| TextFrame GI-2 | [TEXTFRAME-GI2.md](../../../.skill/saor-analise-documental/templates/TEXTFRAME-GI2.md), **9 H2 e 28 H3** | §1 identidade e PNG aprovado; §2 representação textual da Tela; §3 geometria; §4 aparência; §5 conteúdo/ações; §6 matriz requisito→PNG→caixa→texto; §7 rolagem/variantes; §8 testes e limites; §9 aprovação GI-2 e eventos posteriores |
| Composição GI-3/GI-4 | [COMPOSICAO-GI3-GI4.md](../../../.skill/saor-analise-documental/templates/COMPOSICAO-GI3-GI4.md), **10 H2 e 30 H3** | §1 identidade/fonte física; §2 modelo oficial/contrato; §3 cadeia GI-0→GI-2; §4 método; §5 viewport e regiões; §6 cabeçalho/STATUS; §7 Item 10; §8 Item 14; §9 resultado/preservação; §10 decisão GI-4, hash e adendos |

Para cada arquivo, conferir **H1/H2/H3, sequência, textos dos títulos, campos, tabelas, colunas e linhas fixas**, não apenas totais. As quantidades acima descrevem os modelos fisicamente examinados na base da implementação; após alteração formal autorizada de template, o auditor deverá ler o modelo então vigente e obter sua estrutura real, sem continuar usando valores embutidos como prova suficiente. Preservar **todos os campos e subtópicos**. Sem evidência para preencher um campo, registrar pendência ou inaplicabilidade fundamentada na posição própria; não inventar conteúdo nem introduzir seções alternativas para facilitar relato.

### 7.3. Verificação semântica obrigatória, independente do validador

O validador estrutural não autentica o teor de uma aprovação, a identidade da referência, um requisito funcional, um texto em PNG ou um hash mencionado. Portanto, para cada Markdown validar além da estrutura: (a) cada ID e nome contra a ficha; (b) versão/tema/página/estado e objeto associado; (c) cada requisito e componente com fonte e evidência; (d) valores de dimensões/cotas contra imagem ou contrato válido; (e) links relativos e SHA classificados; (f) Gate, decisão, responsável, data, abrangência e sequência temporal; (g) estados atuais separados de eventos passados; (h) tratamento das divergências autorizadas; (i) equivalência White/Black; (j) informações não comprováveis do raster claramente limitadas.

Comparar **estilo e completude editorial** pelos três modelos oficiais e pelo Contrato Editorial, não pelo tamanho ou redação de documento de interface anterior. Uma seção válida do template pode conter dados individualizados sem alterar a estrutura. A diferença textual entre duas interfaces não é erro de estilo quando decorre de requisitos ou decisões específicos. Templates de SPEC 3 **não se aplicam automaticamente** ao Wireframe Text de construção do template da SPEC 1.

### 7.4. Atualizações de documentos aprovados

Antes de revisar qualquer Markdown aprovado ou congelado: confirmar autorização, Gate, dependências e se o ajuste é editorial, factual ou material; calcular hash físico inicial; mapear referências atuais e de aprovação. Uma correção dentro da mesma versão **não cria nova versão formal nem histórico de hashes descartados** por esse simples motivo. Entretanto, aprovações de submissões, hashes de origem exigidos e decisões persistentes não podem ser apagados nem reescritos como se tivessem ocorrido sobre bytes posteriores. Determinar retorno ao Gate competente se a alteração material atingir a identidade do objeto aprovado, conforme a SPEC 3, a norma do objeto e a decisão humana. A Skill não pode conceder esse aceite.

## 8. Regras técnicas e testes por imagem

### 8.1. Seleção e aplicabilidade

Aplicar [REGRAS-TECNICAS.md](../../wireframes/REGRAS-TECNICAS.md) às propriedades realmente exigíveis do objeto: canvas, ViewPort, margem, grid, tipografia, paleta/token vigente, componentes, bordas, ícones, estados e acessibilidade estrutural. Confrontar tokens nas tabelas dos temas e a autoridade funcional dos tokens; não impor cor de uma variante à outra. Não usar o texto de uma SPEC como substituto de teste físico da imagem. A auditoria pode verificar contraste e geometria quando possuir imagem, composição e condições necessárias; a aprovação do token por norma não dispensa confronto de sua aplicação efetiva.

### 8.2. Testes mínimos e suas evidências

| Teste | Dados necessários | Evidência a registrar | Limite |
|---|---|---|---|
| Dimensão do canvas/PNG | Bytes do PNG elegível e dimensão determinada pela norma aplicável | Largura, altura, decodificação, identidade do arquivo | Não comprova que a imagem é correta semanticamente |
| ViewPort e escala | Contrato concreto de referência e PNG de Tela aprovado | Região e escala declaradas, pixels totais comparados, diferenças | Não utilizar coordenada fixada por outro modelo |
| Preservação de regiões | Modelo de origem comprovado e máscara de alterações permitidas | Pixels modificados dentro/fora da máscara, hashes da origem e nova cópia | Diferença legítima requer permissão explícita do contrato |
| Cores/tokens | Tabelas técnicas vigentes por tema e pixels/renderização pertinentes | Valores de teste, regiões, tolerâncias **somente se previstas** e violações | Não declarar cor conforme por observação aproximada |
| Conteúdo funcional | Ficha, estados e PNGs efetivamente abertos | Inventário visual por página/estado; texto/componentes presentes e ausentes | Raster não prova eventos de navegação, hitbox lógica ou fonte original |
| Geometria do TextFrame | PNG, caixa descrita, referencial e método | Coordenadas `x/y/w/h`, confronto individual, discrepâncias | Não substituir medição por estimativa |
| Paginação e variantes | Requisitos de rolagem, todos os PNGs e registros | Ordem, offsets/marcos, campos fixos, continuidade e cobertura | Não inventar página ou variante para preencher espaço |
| Equivalência dos temas | Fichas, documentos e PNGs White/Black da mesma unidade | Matriz de semântica, ações, conteúdo, estados e páginas | Diferenças cromáticas previstas não exigem pixels idênticos entre temas |

Qualquer recurso técnico não mensurável pela ferramenta disponível deve permanecer `NÃO VALIDADO`, indicando prova e método faltantes. Um número de diferenças de pixels não substitui a inspeção de texto, recorte, ícones e componentes por interpretação visual efetiva.

## 9. Auditoria dos Gates, decisões e consolidação operacional

### 9.1. Identificação de cada decisão

Para cada decisão requerida pelas SPECs 1–3, registrar `processo → Gate → unidade/versão/tema/página/estado → objeto(s) → SHA de submissão se exigido → responsável → data comprovada → teor e abrangência → estado produzido → decisão posterior`. Confrontar o registro persistente correspondente, a fonte de sua autoridade e os bytes físicos disponíveis. Uma declaração humana aprova somente os objetos que identifica; aprovação de PNG não aprova TextFrame, aprovação de Prancha individual não aprova automaticamente conjunto ou tema diferente. Se a decisão tiver sido posteriormente transcrita, distinguir **data original da decisão** da **data da regularização documental**.

### 9.2. Ordem e efeitos sobre dependentes

- SPEC 1: Gate técnico não exige nova decisão humana; Gates 2/3/6 e imagem final sim. Reabertura de componente congelado implica reavaliar etapas dependentes nos termos da SPEC 1; não redimensionar viewport ou mover cabeçalho silenciosamente.
- SPEC 2: a versão pode permanecer `APROVADO E CONGELADO` após deixar de ser `VIGENTE`; não modificar retrospectivamente Pranchas que a utilizaram. Nova referência depende de seleção formal, não de contagem crescente de versões.
- SPEC 3: alterações de pixels de Tela após GI-1 podem exigir novo GI-1 e validação GI-2/GI-3/GI-4 dependentes; alterações apenas textuais exigem avaliar conteúdo, GI-2 e sua aprovação, não reabrir automaticamente imagem imutável. Alteração de rolagem, estados ou total de páginas exige avaliação do Gate de origem e dos dependentes. Mudança de versão formal segue a autoridade da SPEC 3, sem confundir simples atualização de hash do registro com nova versão.

### 9.3. Consolidação sem transformar README em autoridade

Ao comparar os registros com a matriz do [README operacional](../../../docs/wireframes/images/README.md), conferir o **estado corrente por tema e conjunto** e suas referências atuais, a existência das evidências de Gate em cada documento e as ressalvas aprovadas. Classificar separadamente `documentação desatualizada`, `registro histórico válido`, `aprovação não comprovada` e `erro real do artefato`. Um README contendo `APROVADO` não dispensa as decisões e hashes pertinentes. Correção de estado/hashes no README requer autorização de edição desse arquivo; leitura/auditoria não concede autorização.

## 10. Identidades, hashes, ajustes e versões no domínio

### 10.1. Classificação obrigatória antes de qualquer correção

Aplicar o [processo genérico §8](../PROCESSO-AUDITORIA.md) para cada SHA encontrado. A classificação deve considerar campo, caminho, versão, decisão, data e objeto associado:

| Tipo de hash | Prova requerida e tratamento |
|---|---|
| `HASH_FISICO_ATUAL` | Calcular sobre os bytes atuais do destino; divergência corrente investigada e corrigida somente mediante autorização |
| `HASH_SUBMISSAO_OU_APROVACAO` | Verificar decisão, objeto e data; conservar a identidade do snapshot aceito mesmo que registro receba adendo posterior; não transformar em versão histórica formal |
| `HASH_VERSAO_FORMAL_ANTERIOR` | Verificar transição formal e norma de preservação; conservar artefato e identidade da versão realmente substituída |
| `HASH_AJUSTE_SUBSTITUIDO` | Identidade intermediária descartada durante ajustes na mesma versão, sem obrigação autônoma de comprovação: **não armazenar como histórico**; eliminar referências correntes obsoletas dentro do escopo autorizado |
| `HASH_DE_ORIGEM_DOCUMENTADA` | Verificar a fonte efetivamente usada, quando contrato exige prova de composição; preservar como origem vinculada, não como versão formal anterior |
| `HASH_SEM_CLASSIFICACAO` | `NÃO VALIDADO`; não executar substituição automática de valor |

**Não criar `v02` por uma edição de Markdown ainda na `v01`**. O identificador de versão muda apenas segundo a norma competente e decisão aplicável. A referência física **atual** deve representar os bytes atuais após a última edição; jamais declarar hash de uma versão anterior do mesmo documento como se fosse atual. Ao mesmo tempo, não sobrescrever hashes de decisões de GI-1/2/4, assinaturas de origem ou versões formais para forçar igualdade com arquivo corrente. Se houver dúvida de origem, preservar evidência e declarar o alcance da verificação `NÃO VALIDADO`, sem inventar histórico de revisão.

### 10.2. Sequência determinística de investigação

1. Localizar **todas as referências materialmente relevantes** nos documentos elegíveis e distinguir corrente, aprovação, origem e versão formal.
2. Recalcular hash do arquivo referenciado e verificar sua existência física; registrar hash completo e tamanho.
3. Ler campos e eventos de aprovação, a cronologia e regras do contrato apropriado. Não inferir correção por igualdade/desigualdade do hash isoladamente.
4. Identificar se os bytes posteriores resultaram de aprovação, mudança de STATUS, registro documental, correção, alteração de conteúdo ou nova versão formal, conforme evidência efetiva.
5. Caso seja indispensável e autorizado, confrontar snapshots de aprovação disponíveis, sem presumir equivalência ao GitHub. Se snapshot não estiver acessível, a comparação histórica permanece `NÃO VALIDADA`.
6. Classificar ocorrência, dependentes e risco; propor correção **somente da referência corrente** quando cabível. Separar evidências de submissão e versionamento formal a preservar.
7. Obter autorização específica, editar somente a cópia local permitida e recalcular hashes **após estabilizar todos os bytes**.
8. Rebuscar referências desatualizadas e reauditar cadeia, incluindo White/Black, composição e README, sem criar registro de cada hash transitório.

O arquivo não consegue conter literalmente seu próprio SHA-256 final verificável dentro dos próprios bytes. Referências bidirecionais entre documentos podem criar ciclo equivalente; usar o mecanismo documental permitido pela autoridade competente ou declarar bloqueio, nunca fazer substituição iterativa até suposta convergência. O executor futuro não deve realizar uma substituição global por correspondência de 64 caracteres.

### 10.3. Congelamento versus manutenção do mesmo rótulo de versão

Manter o rótulo `vNN` não autoriza substituir PNG, TextFrame ou Prancha aprovados. Antes de ajuste em objeto congelado, verificar o efeito do diff na identidade aprovada, o retorno ao Gate exigível e a necessidade de nova decisão. Preservar **as aprovações reais e as versões formalmente anteriores**, mas não catalogar como versões históricas as edições intermediárias da mesma `vNN` que não são provas de decisão. Não uniformizar documentos históricos válidos ao estado atual só para igualar hashes. Uma decisão humana posterior deve ser registrada em campo apropriado com data própria, sem editar retroativamente a decisão anterior.

## 11. Taxonomia, tratamento de falhas e decisões necessárias

### 11.1. Classificação e estado da verificação

Utilizar exclusivamente, como classificação, as categorias do processo global: `ERRO COMPROVADO`, `DOCUMENTAÇÃO DESATUALIZADA`, `LEGADO VÁLIDO`, `DECISÃO HISTÓRICA`, `INCONSISTÊNCIA ENTRE FONTES`, `REFERÊNCIA QUEBRADA`, `DIFERENÇA INTENCIONAL`, `LACUNA DOCUMENTAL`, `SEM NECESSIDADE DE ALTERAÇÃO`. Aplicar os **estados da auditoria** da SPEC genérica (§10.2): `CONFORME`, `NÃO CONFORME`, `NÃO VALIDADO`, `PENDENTE`, `NÃO APLICÁVEL`, `BLOQUEADO`. Não substituir estados originais de Gates pelos do auditor.

| Ocorrência | Prova e resposta obrigatórias |
|---|---|
| Falha de estrutura Markdown | Identificar template, H2/H3, campo/linha faltante, comando/retorno e impacto; não corrigir documento aprovado sem autorização |
| Diferença visual | Identificar arquivo, tema/estado, região/pixels, requisito e contrato; propor Gate de retorno conforme origem |
| Hash corrente divergente | Localizar referência e objeto; classificar o tipo antes de propor atualizar valor |
| Hash de aprovação distinto do atual | Reconstruir eventos/edições; não criar nova versão nem declarar revogação automática |
| Aprovação de conjunto ausente | Identificar objetos e declaração original; `NÃO VALIDADO` do aceite coletivo; solicitar decisão humana se exigida |
| Arquivo normativamente LEGADO | Preservar/excluir da releitura de conteúdo; justificar eventual acesso excepcional |
| Falta de contrato concreto | `BLOQUEADO` apenas o consumo/composição que dele depende, mesmo que a seleção da SPEC 2 seja válida |
| Gate futuro no modo `SOB_DEMANDA` | `PENDENTE`, sem declarar regressão; informar pré-condição de avanço |
| Estado do README distinto dos registros | Distinguir estado atual e histórico; propor atualização documental pontual autorizada se necessária |
| Ausência de bytes históricos | `NÃO VALIDADO` para comparação que exigia o snapshot; nunca inventar conteúdo ou SHA |

### 11.2. Registro mínimo de ocorrência

`ID → trilha e Gate → unidade/tema/página/estado/versão → origem/caminho → seção/linha ou região visual → norma e cláusula → resultado esperado → objeto físico e SHA → método executado → resultado observado → divergência/classificação → causa investigada → hipóteses restantes → impacto/dependências → preservações → ajuste necessário/opcional → autorização exigida → teste de confirmação`.

Propostas de correção não podem ser simples “corrigir hashes”, “ajustar documentação” ou “validar imagens”: identificar quais referências são correntes, o texto/valor efetivamente errado, a natureza da alteração e o Gate potencialmente afetado. Nenhuma correção poderá ser aplicada em auditoria **somente leitura**.

## 12. Procedimento de execução do auditor por trilha

### 12.1. Sequência comum, sem antecipação

1. Confirmar base física, exclusões, normas e inventário (§§1–3).
2. Selecionar trilha e modo por fontes oficiais (§2); estabelecer a unidade de cobertura, versões e estágios reais.
3. Construir matriz de requisitos aplicáveis da trilha e, para cada requisito, identificar objeto, prova, método e Gate.
4. Executar as matrizes da SPEC 1 (§4), SPEC 2 (§5) ou SPEC 3 (§6), separadamente, juntamente com os controles visuais e editoriais aplicáveis (§§7–8).
5. Classificar hashes (§10), reconstruir decisões (§9), verificar links/dependências (§3) e registrar as propriedades não comprováveis.
6. Confrontar resultados contra exigibilidades do modo (§2.3), sem antecipar Gate, inventar aprovação ou tratar ausência de erro como prova de cobertura completa.
7. Consolidar todas as ocorrências (§11), causas, decisões humanas e riscos; se necessário, preparar proposta detalhada para autorização.
8. Somente após autorização específica, aplicar a intervenção local pelo processo global, reabrir os arquivos, recalcular hashes e executar segunda auditoria (§13).
9. Concluir com parecer rastreável (§14), declarando limitações, estado de encerramento e incorporação separadamente.

### 12.2. Bloqueios por competência

Se uma norma ou decisão não fornecer parâmetro que **materialmente impede** o teste exigível, `BLOQUEADO` somente o ato dependente. Exemplo de competência: ausência de parâmetro de viewport impede GI-3, não converte automaticamente GI-1 válido em erro; ausência de aceite GI-4 impede fechamento da interface, não torna o PNG intrinsecamente inválido. O resultado `NÃO VALIDADO` deve identificar a prova faltante e o que não se pode afirmar; `NÃO APLICÁVEL` exige justificativa, não é atalho para encerrar uma obrigação não cumprida.

## 13. Segunda auditoria, testes e não regressão

### 13.1. Pós-correção autorizada

Reabrir os **bytes finais** de cada arquivo autorizado; calcular SHA-256 e comparar diff contra a baseline. Conferir o conjunto exato de caminhos criados/modificados/excluídos, inclusive mudança indireta de referência e arquivos preservados. Reexecutar o validador documental quando qualquer dos três Markdown da SPEC 3 tiver sido modificado e confrontar semanticamente seções, decisões, status e hashes. Reexecutar teste visual/pixel a pixel somente quando objeto/dependência realmente demandar ou o contrato exigir confirmação. Buscar problemas novos, não somente a falha original. Caso outra alteração seja necessária fora do escopo, registrar e obter nova autorização; não ampliar silenciosamente.

### 13.2. Matriz de regressão por mudança

| Mudança detectada | Dependências mínimas a reavaliar | Preservações e decisão |
|---|---|---|
| Controle GI-0/GI-1 | Referências correntes em TextFrame, Composições, README; decisões e identidades de GI-0/GI-1 | Não substituir hash de submissão/aprovação nem criar versão histórica por edição simples |
| TextFrame | PNG aprovado, requisitos/cotas, decisão GI-2, referências da Composição e README | Não mudar PNG para mascarar erro textual; verificar necessidade de ratificação GI-2 |
| PNG de Tela | GI-1, GI-2 e GI-3/GI-4 dependentes, estado/páginas correspondentes | Novo bytes após aceite exige decisão competente; não reescrever PNG aprovado silenciosamente |
| Prancha funcional | Referência de origem, viewport, campos, composição, GI-4 e README | Não editar template oficial; avaliar nova aprovação da Prancha exata |
| Composição documental | Hashes correntes nos vínculos, README, evidência GI-4 | Preservar decisões originais; edições dentro da versão não criam vNN automaticamente |
| Registro de vigência | SPEC 2, seis fontes e dependentes que consomem a seleção para novas saídas | Não migrar interfaces históricas automaticamente |
| Normas, Skill ou templates | Contratos e comandos pertinentes, referências cruzadas, resultados e estrutura dos registros dependentes | Não alterar artefatos aprovados apenas para uniformizar estilo |

### 13.3. Testes mínimos de aceite da própria especialização

A futura Skill de Auditoria deverá conseguir demonstrar, com fontes e resultados reproduzíveis, ao menos estas classes de caso:

| Caso | Resultado esperado |
|---|---|
| Novo template em Gate 2 sem aprovação | Identificar bloqueio humano do Gate 2 sem aplicar GI-1/GI-2 de interface |
| Referência oficial com seleção vigente e seis hashes válidos | Registrar SPEC 2 conforme sem executar construção do template |
| Interface em GI-0 ainda sem PNG | Auditar requisitos, marcar PNG/GI-1 futuro `PENDENTE`, não reprovar como encerramento |
| TextFrame escrito antes de GI-1 | Não conformidade com sequência, com fonte precisa |
| Markdown estruturalmente válido e dado funcional falso | Não declarar conformidade semântica |
| PNG/Prancha com dimensões certas, mas viewport diferente | `NÃO CONFORME` ao requisito pixel a pixel, mesmo com dimensões corretas |
| Hash de aprovação e hash físico pós-registro distintos | Investigar cronologia; não classificar nova versão automaticamente |
| Dois ajustes documentais dentro da mesma vNN | Uma identidade física atual, sem histórico artificial de ajustes |
| Mudança formal de vNN com anterior congelada | Preservar identidade e aprovação da versão antiga, consultar seleção vigente |
| Temas individualmente aprovados sem conjunto GI-4 | Aceite coletivo `NÃO VALIDADO` até comprovação expressa |
| Ausência de contrato técnico para modelo selecionado | GI-3 `BLOQUEADO`, sem inventar coordenadas de outro modelo |
| Arquivo `assets/` ou LEGADO excluído | Nenhuma leitura de conteúdo indevida |
| Auditoria de outro domínio | Não aplicar controles específicos de wireframes fora de sua competência |
| Tentativa de edição sem autorização | Nenhuma escrita; proposta detalhada de intervenção |

Esses casos são requisitos de teste **para uma etapa futura da Skill**, não alegação de que um executor automatizado já existe ou de que os testes foram executados neste GVA-2. A revisão documental deste contrato deve ser feita agora; implementação da Skill e seus testes pertencem aos Gates posteriores.

## 14. Relatório, cobertura e encerramento por modo

### 14.1. Produto mínimo do parecer especializado

O parecer deve conter: (A) FATOS VERIFICADOS e inventário de arquivos lidos, tamanhos, hashes, métodos e limitações; (B) INTERPRETAÇÕES separadas das provas; (C) TRILHA/ESTÁGIO E AUTORIDADES; (D) MATRIZ POR GATE OU CONDIÇÃO VIGENTE; (E) CONFRONTO VISUAL/EDITORIAL E HASHES; (F) OCORRÊNCIAS E RISCOS; (G) DEPENDÊNCIAS E PRESERVAÇÕES; (H) AJUSTES PROPOSTOS E AUTORIZAÇÕES; (I) SEGUNDA AUDITORIA se houve correções; (J) ESTADO E PRÓXIMA OPERAÇÃO PERMITIDA. Registrar `teste → entrada → resultado → alcance de prova → fonte`, sem reivindicar inspeções não realizadas. Relatório na conversa ou no meio autorizado; **não criar arquivo, manifesto ou registro persistente sem autorização específica**.

### 14.2. Cobertura por trilha e por requisito

| Trilha | `SOB_DEMANDA` | `ENCERRAMENTO` |
|---|---|---|
| SPEC 1 | Até o Gate efetivamente exigível, com dependentes futuros `PENDENTE` | G1–G6, PNG final e aceitações humanas próprias, estrutura de Wireframe Text do template e não regressão comprovados |
| SPEC 2 | Vigência/objetos exigíveis à consulta concreta | Seleção formal e integridade de todos os objetos exigidos e versões preservadas, para a decisão de referência analisada |
| SPEC 3 | GI-0 até último Gate exigível, por tema/página/estado; futuro pendente | GI-0–GI-4 aplicáveis, documentos integrais, todos os PNGs/Pranchas, decisões individuais e conjunto, referências e README coerentes |

`CONFORME PARA ENCERRAMENTO` requer todas as obrigações exigíveis comprovadas, limitações não impeditivas fundamentadas e inexistência de desvio impeditivo. Uma ressalva aceita **não** apaga não conformidade técnica estrita: sua natureza e seu alcance permanecem registrados. A entrega de ZIP não comprova incorporação; só uma base física atualizada do responsável permite verificá-la. A auditoria não entrega software funcional e não aprova produto executável a partir de PNG.

### 14.3. Falhas de completude e independência de contexto

Reprovar como documento auditorial insuficiente um parecer que: omita qualquer objeto exigível; use somente títulos de arquivo; não identifique fonte e evidência; declare `CONFORME` apenas pelo validador Markdown; aplique coordenadas de Modelo C como universais; herde aprovação; transforme ajustes vNN em versões históricas; reabra Gates sem causa; confunda data de aprovação e adendo; escreva sem autorização; reproduza um resumo superficial no lugar de testes; dependa de memória da conversa. Outra pessoa com o clone e as normas deve conseguir reproduzir a seleção das fontes e cada conclusão material.

## 15. Matriz de integração com os controles genéricos AU-R01 a AU-R30

Esta matriz identifica a **aplicação especializada**; não substitui os procedimentos dos §§1–14. Todo requisito continua definido pela [SPEC genérica](../PROCESSO-AUDITORIA.md), enquanto as fontes dos objetos são as SPECs 1–3 e os respectivos contratos. A futura Skill deverá mapear cada linha para instrução operacional, evidência e teste pertinente, sem lacunas ocultas.

| Requisito | Aplicação específica ao domínio | Procedimento neste contrato | Evidência/teste |
|---|---|---|---|
| AU-R01 | Três trilhas sem dependência de interface/versão concreta | §§1–2 | Seleção por autoridade e objeto |
| AU-R02 | Auditar qualquer estágio de Gate existente | §§2.2–2.3, 14.2 | Futuro legítimo classificado `PENDENTE` |
| AU-R03 | Auditoria integral após processo especializado | §§2.3, 14.2 | Critérios de fechamento da trilha |
| AU-R04 | ZIP/clone como fonte primária | §2.1 | Inventário/hashes e exclusões |
| AU-R05 | Preservar `assets/` e LEGADOS | §§1.4, 2.1 | Ausência de acesso indevido |
| AU-R06 | Localizar autoridades SPEC 1/2/3 | §§1.2–1.3, 2.2 | Matriz de precedência por regra |
| AU-R07 | Bytes, CRC, SHA, tipos e imagens reais | §§2.1, 3.1, 8 | Testes físicos por tipo |
| AU-R08 | Requisito até evidência por unidade | §§2.4, 6.1–6.2 | Matriz funcional/por Gate |
| AU-R09 | Template editorial aplicável da SPEC 3 | §§7.1–7.2 | Validador oficial e confronto completo |
| AU-R10 | Semântica de ficha/PNG/TextFrame/Prancha | §§6.3–6.4, 7.3, 8 | Leitura/inspeção fundamentada |
| AU-R11 | Caminhos/links/origem/dependência | §§3.1–3.2, 10.2 | Matriz de referências e destinos |
| AU-R12 | Hash físico **corrente** | §§3.1, 10.1–10.2 | SHA recalculado e contextualizado |
| AU-R13 | Ajuste da vNN sem histórico artificial | §§7.4, 10.1–10.3 | Correção de referências correntes, se autorizada |
| AU-R14 | Preservação de versões formais anteriores | §§5.4, 10.1–10.3 | Registro de transição e integridade |
| AU-R15 | Snapshots de submissão e aprovação | §§9.1–9.2, 10.1 | Decisões vinculadas aos hashes reais |
| AU-R16 | Reavaliação de Gates por mudança material | §§9.2, 10.3, 13.2 | Análise de impacto e retorno necessário |
| AU-R17 | Ocorrências tipificadas por fonte | §11 | Registro de causa/evidência/classificação |
| AU-R18 | Autorização antes de escrita | §§1.1, 11.2, 12 | Autorização com escopo exato |
| AU-R19 | Correção mínima e dependências | §§10.2, 13.1–13.2 | Diff e rastreio de referências |
| AU-R20 | Segunda auditoria pós-correção | §13.1 | Releitura dos bytes finais/testes impactados |
| AU-R21 | Parecer completo e limitações | §§11.2, 14.1 | Relatório rastreável |
| AU-R22 | Independência de conversas | §§1.1, 14.3 | Reprodução no clone sem memória |
| AU-R23 | Sem aprovação humana automática | §§4.2, 6.2, 9.1 | Decisão humana específica conferida |
| AU-R24 | Não duplicação de autoridades normativas | §§1.1–1.3 | Comparação de competência das fontes |
| AU-R25 | Equivalência SPEC/Skill/testes | §§7, 13.3, 15 | Cobertura cruzada verificável no GVA posterior |
| AU-R26 | Documento completo, sem resumo substitutivo | §§7.2–7.3, 14.3 | Seções/campos/contratos presentes |
| AU-R27 | Auditoria automatizada inicial somente leitura | §§1.4, 7.1, 12 | Nenhuma escrita no modo de auditoria |
| AU-R28 | Núcleo genérico + contrato especializado | §§1.1–1.3, 2.2 | SPEC 1/2/3 aplicadas somente no domínio |
| AU-R29 | ZIP local e incorporação | §§13–14 | CRC, aplicação limpa e confronto com clone posterior quando autorizado |
| AU-R30 | Não regressão de normas/artefatos atuais | §§1.4, 9.2, 13 | Preservação e diff de objetos impactados |

## 16. Critérios bloqueantes de aceite deste contrato (GVA-2)

A validação do **documento de GVA-2** deverá comprovar cumulativamente:

1. **Autoridade e não duplicação:** cada critério aponta para a SPEC, contrato ou Skill realmente responsável; não foi criada aprovação, versão, dimensão universal ou Gate concorrente.
2. **Completude das trilhas:** SPEC 1 (G1–G6/PNG), SPEC 2 (seleção/vigência/seis objetos) e SPEC 3 (GI-0–GI-4) possuem matrizes próprias com método, evidência, falha e competência de decisão.
3. **Processo linear correto:** SPEC 1 Wireframe Text→PNG e SPEC 3 PNG→TextFrame são distinguidos; SPEC 2 não constrói o objeto; nenhum Gate é herdado.
4. **Documentação integral:** os três templates da Skill da SPEC 3 são identificados por caminho, estrutura, escopo e teste oficial; validação estrutural é separada de semântica e evidência.
5. **Integridade material:** hashes atuais versus hashes de aprovação/origem/versão formal são classificados; simples edição da mesma versão não gera histórico, sem apagar decisões aprovadas.
6. **Generalidade real:** nenhum ID de interface, versão numérica, modelo específico ou parâmetro de contrato concreto determina universalmente o processo; valores atuais só aparecem como propriedade condicional da fonte vigente ou exemplo explicitamente delimitado.
7. **Estados e aprovação:** os estados do auditor não substituem os Gates de construção; decisões humanas são explicitamente exigidas apenas onde suas normas determinam.
8. **Rastreabilidade:** todas as linhas AU-R01 a AU-R30 possuem procedimento, fonte, prova/teste e limite; sem requisito órfão.
9. **Referências físicas:** todos os links Markdown relativos deste arquivo resolvem para os arquivos do clone/GVA-1 fisicamente disponíveis, sem acessar conteúdo excluído.
10. **Segunda revisão:** reabrir o arquivo produzido, verificar sua integridade, confrontar conteúdo com as fontes, procurar regras conflitantes, lacunas e texto superficial, executar análise de diff e confirmar que nenhum outro arquivo foi criado/modificado.

**Proibição de avanço:** uma validação superficial por quantidade de seções, tamanho, links ou presença de palavras não substitui a leitura crítica. GVA-2 só poderá receber parecer `CONFORME TECNICAMENTE` após todos os critérios acima e a segunda revisão material; o **aceite humano** permanece distinto. Este contrato não cria ou executa a nova Skill, seus scripts ou o GVA-3. Um resultado aprovado não significa que a integração, automação ou implantação no clone já existam.
