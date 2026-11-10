# SaOr — Processo genérico de auditoria de conformidade e integridade

## 1. Autoridade, finalidade e limites

### 1.1. Responsabilidade normativa

Esta SPEC estabelece **como auditar** um objeto do SaOr quanto à sua integridade física, aderência às normas responsáveis, rastreabilidade, comprovação, referências, versões, decisões e condições de encerramento. É genérica: aplica-se a qualquer domínio, etapa, tipo de arquivo ou conjunto de artefatos, desde que as fontes autorizadas e a abrangência real sejam identificadas. Sua validade **não depende** de uma conversa, implementação, ID, tema, linguagem, ferramenta ou versão de produto particular.

**Esta SPEC não cria nem redefine** requisitos funcionais, técnicos, visuais, editoriais ou de segurança do objeto auditado; não escolhe versões vigentes; não estabelece a sequência dos Gates de outros processos; não aprova artefatos; não substitui uma Skill ou um validador especializado. Ela prescreve o método de confronto e de registro de evidências. As regras específicas permanecem nas autoridades de origem.

### 1.2. Hierarquia e precedência

1. Aplicar antes de tudo [`.specs/PROCESSO-ALTERACAO-ASSISTIDA.md`](../PROCESSO-ALTERACAO-ASSISTIDA.md): fonte física, leitura contextual, autorização anterior à escrita, execução local, regressão e entrega. Esta SPEC não derroga nenhuma dessas obrigações.
2. Ler [`.specs/README.md`](../README.md) e localizar a autoridade do **assunto auditado**. Para cada requisito, sua fonte canônica prevalece sobre exemplos, índices, resumos, comentários, ferramentas e relatos da conversa.
3. Aplicar as SPECs responsáveis, contratos de domínio, regras técnicas, registros de seleção/vigência, Skills e decisões humanas documentadas **somente conforme suas competências e vigência comprovadas**. Uma Skill aplica uma norma; não concede autorização superior à norma. Um validador mede um critério implementado; não substitui todas as verificações exigidas.
4. Em conflito entre fontes, verificar primeiro objeto, escopo, autoridade, edição vigente, cronologia e natureza histórica. **Não inventar regra conciliatória**, não uniformizar decisões históricas e não alterar norma existente por conveniência. Registrar a contradição e impedir somente a operação que depender de sua resolução.
5. O contrato especializado, quando existir e estiver vigente, indica como executar os controles desta SPEC no domínio; não pode criar outra autoridade para os requisitos do domínio. Ausência de contrato especializado não autoriza transpor padrões de outro assunto nem impede os controles genéricos demonstráveis.

**Fonte versus exemplo:** nomes de interfaces, pastas, artefatos e fluxos existentes podem servir de dados de teste fora desta SPEC, mas não podem determinar seu comportamento. A lista de exemplos não é fonte normativa.

### 1.3. Proibições permanentes

É proibido inferir conteúdo, requisitos, estados, versões, aceitações ou correções com base em memória, título, caminho, semelhança visual, último commit, README operacional ou hash isolado; alegar leitura ou inspeção não realizada; transformar ausência de evidência em conformidade; declarar aprovação humana por execução de código; criar histórico artificial de ajustes da mesma versão; apagar provas de decisões existentes; substituir hashes indiscriminadamente; escrever sem autorização; alterar objeto congelado sem tratar seus Gates; publicar ou escrever no GitHub; acessar exclusões normativas sem autorização específica; ou apresentar relatório resumido como se fosse auditoria completa.

### 1.4. Alcance da comprovação

Uma leitura de bytes prova acesso físico, não compreensão do significado. SHA-256 e CRC provam propriedades de integridade identificadas, não correção funcional. Estrutura Markdown válida não prova veracidade do conteúdo. Imagem aberta não comprova eventos de interação. Teste automatizado não prova, sozinho, autorização humana. Cada resultado deve indicar exatamente qual propriedade foi testada e qual permaneceu não verificada.

## 2. Escopo, momentos e modos de auditoria

### 2.1. Modos de execução

| Modo | Momento permitido | Objetivo | Critério de abrangência |
|---|---|---|---|
| `SOB_DEMANDA` | Em qualquer estágio, inclusive após uma decisão ou em investigação pontual | Examinar a conformidade já exigível e identificar o que falta para avançar | Somente obrigações aplicáveis ao estágio comprovado; etapas futuras são registradas como pendentes, não como falhas consumadas |
| `ENCERRAMENTO` | Após as etapas e Gates exigidos pelo processo responsável e antes de declarar o fechamento definitivo | Examinar integralmente os requisitos de conclusão e a coerência final das fontes e artefatos | Todas as condições de encerramento aplicáveis devem ter comprovação suficiente |

**Reauditoria** é um ciclo de verificação posterior à correção, nos dois modos; não é um terceiro modo de aprovação. Quando a auditoria é acionada após uma edição, também permanecem obrigatórias as verificações pós-alteração do processo global, mesmo que o estágio do domínio ainda seja intermediário.

O procedimento genérico não pode exigir o encerramento integral para executar `SOB_DEMANDA`, nem aceitar `SOB_DEMANDA` como substituto de `ENCERRAMENTO` ao fechar uma atividade.

### 2.2. Gatilhos e integração

O processo especializado responsável deve prever, mediante integração autorizada na sua própria norma ou fluxo, a chamada desta auditoria **depois de cumprir seus Gates finais e antes do encerramento**. A auditoria também pode ser solicitada explicitamente a qualquer momento. Este texto não altera por si só outros arquivos de SPEC nem instala acionador automático.

Se uma execução por evento for requerida, sua existência, mecanismo e testes precisam ser comprovados na Skill/ferramenta correspondente. Uma referência Markdown à auditoria cria obrigação processual, **não execução automática de código**. Não declarar integração concluída quando o acionamento estiver apenas planejado.

### 2.3. Unidade auditada e expansão de dependências

O objeto pode ser um arquivo, grupo, etapa, domínio ou o projeto. Delimitar seu conjunto primário e acrescentar dependências somente quando um contrato, referência ou impacto real exigir. Registrar cada expansão de escopo com justificativa. Dependência examinada não é, por isso, automaticamente arquivo a alterar.

Em auditoria pontual, ler integralmente os arquivos pertinentes e ampliar para suas dependências afetadas. Na primeira base ainda não validada, cumprir a leitura integral de todos os arquivos elegíveis conforme o processo global e as exclusões aplicáveis; não usar leitura por palavra-chave como substituto. Em base repetida, reutilizar verificações físicas somente segundo §5, sem afirmar compreensão que a evidência anterior não possui.

### 2.4. Exclusões e preservações

`assets/` é excluído: não abrir, listar internamente, interpretar ou modificar sem autorização expressa e específica. Arquivos classificados **LEGADOS** pela autoridade competente permanecem preservados e fora da releitura de conteúdo por padrão; se indispensáveis, justificar e solicitar autorização específica. A exclusão é registrada como aplicação da norma, não como falha de auditoria. Não confundir arquivos antigos com LEGADOS normativamente classificados. Um caminho protegido não deve ser inspecionado simplesmente porque um verificador o enumerou.

## 3. Contrato de entrada e condições para iniciar

### 3.1. Entradas obrigatórias

| Campo | Como obter e verificar | Ausência ou ambiguidade |
|---|---|---|
| Base física primária | Clone/ZIP/diretório fornecido e acessível; registrar origem autorizada, caminho, tamanho, identificação e hash do contêiner quando aplicável | `NÃO VALIDADO` para identidade da base; suspender conclusões que dependam dela |
| Objeto e fronteira | Caminhos físicos e/ou ID comprovado por fonte canônica; declarar incluídos e excluídos | Solicitar delimitação somente se interpretações mudarem materialmente a operação |
| Domínio e autoridades | Ler índice normativo e contratos efetivamente aplicáveis; determinar prioridade por escopo e decisão | Não aplicar regras de outro domínio por analogia |
| Modo | `SOB_DEMANDA` ou `ENCERRAMENTO`; em falta, determinar o propósito pelo pedido e declarar o enquadramento adotado | Não presumir encerramento aprovado |
| Estágio real | Estados, Gates e decisões persistentes pertinentes; não deduzir do nome do arquivo | `NÃO VALIDADO` do estágio; não antecipar verificações dependentes |
| Versão formal e vigência | Identificadores e registros de autoridade, com comprovação de seleção e aprovação quando relevante | Não selecionar pelo maior número de versão |
| Restrições | Exclusões, congelamentos, limites de leitura/escrita, versões legadas e autorização anterior específica | Preservar por padrão; bloquear somente operação que as violaria |
| Baseline comparativa, se necessária | Fonte anterior física e inventário verificável de conteúdo/hash/escopo | Comparação incremental `NÃO VALIDADA`; usar nova baseline, sem inventar diffs |

A identificação de uma fonte de dados não implica autorização para escrita. O fornecimento do ZIP autoriza leitura/auditoria dentro das exclusões; criação, edição, exclusão, substituição e empacotamento exigem autorização expressa e delimitada.

### 3.2. Registro de início

Antes de emitir conclusões, registrar: data da auditoria como data da execução (não da decisão analisada), fonte física, identificador/hash da base, domínio, modo, objeto, versão/estado quando verificáveis, normas selecionadas, critérios de exclusão, riscos de acesso, limites das ferramentas e responsável pela decisão. Quando a data/hora local não puder ser confirmada, não inventar precisão temporal; usar a evidência disponível.

### 3.3. Confirmação de pré-condições

Executar checks não destrutivos de leitura do ZIP/arquivo e da estrutura mínima das normas. Falha de integridade, fonte ilegível ou caminho inseguro é motivo para `BLOQUEADO` na operação dependente; o relatório parcial deve expor a causa. Não mascarar a falha substituindo o ZIP por GitHub ou por outra base.

## 4. Autoridades, critérios exigíveis e rastreabilidade

### 4.1. Descoberta normativa

1. Ler integralmente o processo global e o índice canônico antes das normas específicas.
2. Identificar os contratos aplicáveis pela responsabilidade declarada no conteúdo das normas e pela natureza verificada do objeto; não pelo nome semelhante da pasta.
3. Ler integralmente os contratos diretamente pertinentes e todas as dependências normativas que definam requisitos ou seleção de versões.
4. Diferenciar **requisito**, **invariante**, **método técnico**, **decisão humana**, **registro de estado**, **exemplo**, **referência histórica** e **hipótese**.
5. Para cada exigência, registrar fonte/caminho, seção/linha/trecho, autoridade, condição de aplicabilidade, objeto, critério de verificação, evidência esperada e destino do resultado.
6. Quando documentos parecerem divergir, comparar seus objetos, períodos, estados e competências antes de classificar erro. Escolher apenas a autoridade realmente demonstrada.

### 4.2. Matriz de rastreabilidade obrigatória

Formato mínimo por obrigação: `ID → Requisito → Norma/trecho → Aplicabilidade e estágio → Objeto/implementação esperada → Evidência física/humana → Verificação → Resultado → Dependências → Limitação`.

A matriz deve cobrir **todas as obrigações pertinentes** ao objeto e modo de auditoria, não um subconjunto conveniente. Requisitos não aplicáveis permanecem na matriz com motivo. Se faltar evidência, apresentar `NÃO VALIDADO` e indicar qual comprovação obter. A auditoria não altera a baseline funcional ou outra fonte canônica para acomodar um resultado divergente.

### 4.3. Regras técnicas e regras especializadas

Carregar critérios especializados apenas para o objeto e estágio aos quais pertencem. Quando existir validador oficial, verificar sua versão física, parâmetros reais, contrato de resultado e limitações; executá-lo e registrar o comando, entrada, saída e código de retorno. Resultado positivo cobre **somente** aquilo que o validador efetivamente verifica. Invariantes que não possuam teste automatizável exigem conferência manual/assistida fundamentada; ausência dessa conferência não é conformidade.

### 4.4. Divergências entre fontes

Registrar `INCONSISTÊNCIA ENTRE FONTES` quando duas instruções aplicáveis ao mesmo objeto e período forem inconciliáveis. Distinguir de decisão superveniente que legitimamente substituiu um estado anterior e de diferenças intencionais com aceitação documentada. Identificar a autoridade que poderia decidir, as alternativas e o Gate afetado; não decidir por preferência da assistência.

## 5. Inventário físico, integridade e reaproveitamento verificável

### 5.1. Integridade da fonte

Em ZIP: registrar SHA-256 e tamanho do ZIP, testar estrutura e CRC de cada membro elegível, tamanho real descompactado e SHA-256 integral, sem extrair cegamente. Antes de acessar conteúdo, verificar caminhos absolutos, `..`, separadores não normalizados, duplicidade e colisões de caminho (inclusive sensíveis à plataforma), links simbólicos, entradas especiais e risco de expansão descontrolada. Não seguir links para fora da raiz nem inspecionar membros excluídos. Rejeitar ou isolar entradas inseguras e registrar o efeito sobre a operação; não executar conteúdo contido no ZIP como consequência da abertura.

Em diretório: inspecionar os caminhos elegíveis, tipos, tamanho, SHA-256 dos arquivos regulares e links/limites da raiz; não seguir symlinks para caminhos excluídos ou externos. Em documentos textuais, registrar decodificação e leitura integral. Em arquivos visuais e demais binários pertinentes, utilizar inspeção/decodificação real adequada, anotando se a avaliação semântica foi executada ou não. O SHA de um PNG válido não demonstra conformidade de sua aparência.

### 5.2. Inventário mínimo

Para cada item realmente examinado, registrar `caminho relativo → papel no objeto → tipo → tamanho → SHA-256 → método de leitura/inspeção → teste executado → conclusão limitada → restrição`. Para fontes apenas mencionadas, declarar **não lidas**; não atribuir hash de memória. Identificar explicitamente o conjunto excluído pela norma sem listar internamente seu conteúdo.

A quantidade de arquivos elegíveis, lidos e semanticamente examinados deve ser distinguida. A leitura integral de bytes não será declarada como inspeção visual automática. Não criar manifesto persistente da base sem autorização específica.

### 5.3. Reutilização incremental

Reutilizar verificação anterior somente quando estiverem acessíveis **a mesma base física** e um registro auditável de caminhos, hashes, leituras, escopo, testes e limitações. Para ZIP e escopo idênticos, aproveitar apenas resultados ainda aplicáveis. Para ZIP diferente, comparar membros elegíveis por `caminho → tamanho → SHA-256`; interpretar novamente os arquivos novos/alterados e dependências impactadas. A verificação de hash pode exigir reler bytes sem exigir reinterpretação semântica do mesmo arquivo. Mudança de norma, contrato, seleção de versão ou Gate pode exigir ampliação do escopo.

Sem a base anterior física ou seu inventário verificável, marcar comparação anterior `NÃO VALIDADA` e estabelecer nova base; nunca reconstruir diff usando memória, nome ou data do ZIP. Registrar inclusões, exclusões, inalterados e justificativas de não releitura. Não afirmar que a base local é idêntica ao GitHub sem confronto físico específico.

## 6. Auditoria estrutural, semântica e de evidências

### 6.1. Estrutura e formato

Obter da norma competente o formato obrigatório do objeto: esquema de campos, posições, seções, ordem, arquivos auxiliares, nomenclatura e outras invariantes. Validar todos os elementos prescritos, não apenas os títulos. Relatar presença, ausência, ordem, tipo, conteúdo exigível, preenchimento indevido e referências. Preservar esquemas fechados, mesmo que algum campo esteja legitimamente pendente. É proibido trocar um template completo por um resumo, rascunho ou modelo criado por analogia.

### 6.2. Fidelidade e coerência semântica

Para cada requisito rastreado, confrontar a fonte normativa com o conteúdo efetivamente observado no artefato e em seus dependentes. Analisar textos literais, objetos, propriedades, estados, exceções, fluxos, relações e restrições **somente quando prescritos ao domínio**. Registrar por requisito o trecho ou referência física, o esperado, o observado e a conclusão. Buscar omissões, contradições, premissas implícitas, generalizações de casos individuais e afirmações não comprováveis pela mídia examinada.

Declarações sobre funcionamento executável não são comprovadas por uma imagem estática ou por um texto descritivo. Aprovações declaradas em documento não provam sua ocorrência sem evidência da decisão. Comparação de estilo deve avaliar **fidelidade aos modelos e contratos vigentes**, sem uniformizar decisões, exemplos e eventos de versões anteriores.

### 6.3. Níveis de evidência

- **Física:** bytes, dimensão, cor ou conteúdo inspecionado com método identificado.
- **Normativa:** exigência e vigência extraídas da fonte canônica.
- **Humana:** decisão explícita com objeto, alcance, data/fonte e identidade exigida pelo contrato.
- **Derivada:** resultado de teste ou cálculo reproduzível, com entrada e método.
- **Interpretativa:** hipótese ou dedução explicitamente separada de fatos, jamais suficiente sozinha para concluir requisito bloqueante.

Sempre ligar a conclusão ao nível de evidência necessário; um nível não substitui outro. Quando um validador não cobre semântica ou uma imagem não comprova navegação, usar `NÃO VALIDADO` na propriedade sem prova, não `CONFORME`.

### 6.4. Integridade de decisões e estados

Para cada decisão aplicável, identificar responsável documentado, data comprovada, objeto exato, versão, hashes quando exigidos, texto/escopo fiel, Gate associado, condições e decisões posteriores. Diferenciar: existência do artefato, conformidade técnica, aprovação, vigência, congelamento e conclusão. Um registro de aprovação em uma versão/tema/página/estado não se estende silenciosamente a outro objeto. Um registro anterior `PENDENTE` pode ter sido superado: reconstruir cronologia e autoridade antes de determinar o estado corrente.

Se a decisão não estiver persistentemente registrada conforme a norma do domínio, não inventar aceite nem presumir incorporação. Diante de evidência material conflitante, indicar a parte do Gate que permanece não comprovada. A auditoria **não revoga nem aprova automaticamente** Gates de outro processo.

## 7. Auditoria de referências e dependências

### 7.1. Inventário de vínculos

Construir matriz `origem/campo/linha → referência declarada → objeto de destino → relação declarada → norma competente → verificação → impacto`. Resolver caminhos relativos contra a raiz ou o documento de origem conforme o contrato; verificar segurança e existência física sem resolver por aproximação. Separar links normativos, dados de origem, dependências de construção, identidades de versão e comprovações de Gate.

### 7.2. Integridade de links e referências

Confirmar que o destino existe na versão/base apropriada; quando necessário, confrontar seção, rótulo ou alvo específico. Uma referência a um objeto anterior formal e legitimamente preservado não deve ser automaticamente atualizada para o objeto mais recente. Se a fonte citar um hash, primeiro atribuir-lhe uma categoria do §8. Uma referência pode ser válida historicamente e não ser a referência corrente: registrar essa distinção.

### 7.3. Dependência, propagação e ciclos

Representar dependências entre arquivos e referências por direção e papel. Identificar quais vínculos correntes precisam ser recalculados depois de uma edição autorizada, quais são registros de decisão imutáveis e quais são referências de origem. Detectar ciclos (`A → B → A`) e autorreferências; não tentar corrigir hashes em loop. Não usar referências circulares como substitutos de prova temporal. Quando o contrato não oferecer uma representação válida do vínculo, classificar como lacuna impeditiva da atualização dependente e solicitar decisão competente.

### 7.4. Abrangência da busca

Não confiar apenas na ocorrência de uma string hexadecimal. Investigar contexto, rótulo, caminho, evento e norma de cada referência. Revisar todos os documentos elegíveis e dependências materialmente afetados, preservando arquivos históricos e excluídos. Uma substituição textual global não é método suficiente para comprovar a integridade referencial.

## 8. Política de SHA-256, ajustes, versões e aprovações

### 8.1. Identidades e categorias normativas

O auditor diferencia **identidade física** (hash dos bytes), **versão formal** (estado/identificador definido pela norma do objeto), **seleção vigente** (ato/registro da autoridade) e **prova de decisão** (objeto submetido e aceito). Essas identidades podem coexistir e **não são equivalentes**.

| Categoria da referência | Significado e verificação | Tratamento admitido |
|---|---|---|
| `HASH_FISICO_ATUAL` | Referência que afirma identificar os bytes correntes do caminho/versão vigente; calcular SHA-256 do objeto presente | Se divergir, investigar; atualizar somente referência corrente autorizada, após ajuste efetivo |
| `HASH_SUBMISSAO_OU_APROVACAO` | Identidade de bytes ligada a evento humano/tecnicamente documentado em data e escopo específicos | Preservar a evidência da decisão; não a substituir retroativamente pelo hash de uma edição posterior nem chamá-la de versão histórica por isso |
| `HASH_VERSAO_FORMAL_ANTERIOR` | Identidade de artefato de versão formalmente anterior comprovada por registro de versionamento | Preservar a versão e sua identidade conforme a autoridade especializada; não substituir pelo arquivo vigente |
| `HASH_AJUSTE_SUBSTITUIDO` | Hash intermediário superado por edição autorizada dentro da **mesma** versão, sem obrigação autônoma de prova de Gate ou versão formal | Não criar histórico artificial de revisão; eliminar/substituir a referência corrente obsoleta no escopo autorizado |
| `HASH_DE_ORIGEM_DOCUMENTADA` | Identidade da fonte efetivamente utilizada em composição ou produção, quando o contrato exige essa comprovação | Preservar somente enquanto constituir evidência necessária da operação, identificada como origem e não como versão anterior |
| `HASH_SEM_CLASSIFICACAO` | Propósito não demonstrado por campo, norma ou decisão | `NÃO VALIDADO`; proibir correção automática ou atualização especulativa |

O simples fato de o SHA atual divergir de um SHA descrito não estabelece, por si, erro, regressão, nova versão, revogação de aprovação ou dever de armazenar histórico.

### 8.2. Ajuste dentro da mesma versão

Quando a norma competente e as decisões autorizadas permitirem corrigir um objeto preservando sua versão formal, manter o mesmo identificador de versão. Corrigir todas as referências **correntes** impactadas para os hashes dos bytes finais. Não acumular como histórico de versões os hashes intermediários descartados por esses ajustes; não gerar número de versão novo apenas porque o hash do Markdown, script, imagem ou artefato mudou.

**Limite obrigatório:** uma alteração em objeto aprovado/congelado pode exigir decisão e retorno ao Gate correspondente **mesmo permanecendo na mesma versão**, conforme a norma específica. A política de não criar histórico artificial não concede autorização para sobrescrever artefatos aprovados silenciosamente. Preservar eventuais evidências de submissão, aprovação e origem quando elas forem exigidas e efetivamente comprovadas; não confundi-las com histórico de revisões editoriais.

### 8.3. Mudança formal de versão

Uma nova versão existe quando o processo/autoridade competente define a transição e seus requisitos, não por suposição a partir de um diff. Em transição formal, preservar obrigatoriamente os artefatos da versão anterior que a norma mandar manter, suas identidades e decisões pertinentes, e registrar a seleção vigente separadamente da aprovação. Não converter ajuste da mesma versão em transição formal; não tratar versão antiga aprovada como vigente por padrão.

### 8.4. Sequência de verificação de divergências

1. Localizar referência, arquivo de origem, campo e objeto exato.
2. Verificar a fonte normativa da identidade e sua finalidade (§8.1), assim como o estágio de revisão.
3. Confirmar existência física do destino e recalcular SHA-256 com bytes integrais.
4. Determinar se o valor citado se refere a **agora**, a uma **submissão/aprovação**, a uma **origem exigida** ou a outra **versão formal**.
5. Investigar alterações autorizadas, datas, decisões, dependências, estágio e efeitos sobre Gates. Se indispensável, localizar versão física anterior permitida; não baixar automaticamente nem supor equivalência com remoto.
6. Comparar conteúdo e bytes das versões disponíveis; quando ausentes, registrar limite `NÃO VALIDADO` para a comparação indisponível.
7. Classificar a ocorrência, causa e impacto; decidir se há correção realmente necessária. A ausência de erro demonstrado não comprova cobertura completa.
8. Propor mudança somente das referências **correntes** afetadas; preservar eventos de aprovação e versões anteriores formais nos termos de sua norma.
9. Obter autorização específica antes de editar; executar sobre cópia local e calcular hashes **depois** da edição final.
10. Atualizar dependências autorizadas, confrontar novamente todas as referências e repetir testes impactados. Havendo ciclo insolúvel, interromper a operação e registrar o bloqueio sem inventar hash.

### 8.5. Autorreferência e integridade temporal

Um arquivo não pode conter, dentro de seus próprios bytes, a representação literal de seu **SHA-256 final** e simultaneamente esperar que esse literal seja igual ao SHA calculado dos mesmos bytes após a inserção. Proibir esse ciclo lógico; utilizar referência externa, snapshot de decisão ou mecanismo expressamente autorizado pelo contrato aplicável, sem criar mecanismo novo por iniciativa da auditoria. Em cadeias de dependências, distinguir o hash efetivo de origem do hash corrente após atualizações, de acordo com sua função normativa.

### 8.6. Conflito com regras especializadas

Esta política define **como auditar e classificar** identidades, não altera condições de versionamento, congelamento ou reabertura formal estabelecidas por outra SPEC. Se a regra material específica determinar nova versão ou preservação adicional, ela deve ser aplicada ao objeto correspondente. Caso uma terminologia existente seja ambígua, apontar precisamente a cláusula e propor harmonização em operação separada e autorizada; não reinterpretar documentos já aprovados como se a harmonização tivesse ocorrido.

## 9. Gates, decisões humanas e congelamento

### 9.1. Reconstruir a sequência competente

A partir do contrato responsável, identificar os Gates existentes, pré-condições, objetos, provas e aceites exigidos; não importar nomes ou quantidade de Gates de outro domínio. Para cada Gate aplicável, confrontar `condição → operação → artefato → teste → evidência → decisão humana (se exigida) → efeito sobre dependentes`.

### 9.2. Distinguir estados

`APROVADO`, `VIGENTE`, `CONGELADO`, `CONFORME TECNICAMENTE`, `PENDENTE` e `CONCLUÍDO` têm significados próprios definidos pela norma responsável. Não os fundir em um único booleano. Uma nova leitura de arquivos não promove o objeto a aprovado. A falta de aprovação humana não se resolve por executor, nem por ausência de erro técnico.

### 9.3. Evidência de aprovação

Verificar texto fiel, responsável, data comprovada, objeto e escopo; hashes/versões, tema/estado/página ou atributos equivalentes **quando o contrato os exigir**. Diferenciar aprovações individuais e de conjunto. Evidência da decisão pode ser um hash de submissão anterior ao hash físico pós-registro; isso exige reconstrução cronológica, não substituição automática. Se uma decisão registrada for contradita por evidência física, indicar exatamente o alcance não validado; não declarar sua revogação sem autoridade.

### 9.4. Reabertura e regressão

Se uma correção afetar objeto congelado, definir pela norma competente o Gate de retorno e dependentes; solicitar aprovação humana somente onde a fonte exige. Mudança em documentação auxiliar não abre automaticamente todos os Gates do domínio. A auditoria pode recomendar ou bloquear uma alteração material sem invalidar decisões anteriores por mera divergência superficial.

## 10. Classificação de ocorrências e estados auditoriais

### 10.1. Taxonomia das ocorrências

Utilizar as categorias do processo global: `ERRO COMPROVADO`, `DOCUMENTAÇÃO DESATUALIZADA`, `LEGADO VÁLIDO`, `DECISÃO HISTÓRICA`, `INCONSISTÊNCIA ENTRE FONTES`, `REFERÊNCIA QUEBRADA`, `DIFERENÇA INTENCIONAL`, `LACUNA DOCUMENTAL`, `SEM NECESSIDADE DE ALTERAÇÃO`. Um desvio editorial isolado pode ser anotado como atributo da ocorrência, mas **não substitui** essas classes nem revoga Gate.

Para cada ocorrência registrar: ID, caminho, seção/linha ou referência visual, fonte normativa, comportamento esperado, evidência encontrada, divergência comprovada, causa investigada, hipóteses ainda abertas, impacto, risco de regressão, necessidade real, correção proposta, dependentes e autorização necessária.

### 10.2. Estados da verificação

| Estado | Critério de atribuição | Consequência |
|---|---|---|
| `CONFORME` | Teste aplicável executado com evidência suficiente e resultado correspondente à norma | Pode satisfazer o critério específico; não implica aprovação humana |
| `NÃO CONFORME` | Violação demonstrada de exigência aplicável com evidência e fonte | Investigar causa e impacto; corrigir somente quando autorizado |
| `NÃO VALIDADO` | Fonte, acesso ou evidência insuficiente para decidir com rigor | Identificar prova faltante; não inferir conformidade |
| `PENDENTE` | Operação ainda não executada e legitimamente futura no estágio atual | Registrar condição de início; não tratar como regressão já ocorrida |
| `NÃO APLICÁVEL` | Critério fora do objeto/estágio, com justificativa normativa | Excluir do cálculo das obrigações efetivas, mantendo registro |
| `BLOQUEADO` | Operação específica impedida por condição não satisfeita, conflito ou falta de autorização | Identificar operação, causa e condição exata de liberação |

Estados de auditoria são **distintos** dos estados documentais ou Gates do objeto, que devem permanecer com a semântica da respectiva norma. Uma pendência pode coexistir com conformidade das demais verificações. `BLOQUEADO` não deve ser atribuído genericamente a todo o projeto se somente um ato for impedido.

### 10.3. Conclusão por modo

No modo `SOB_DEMANDA`, concluir por requisito exigível; relatar os Gates futuros como pendentes e só impedir o avanço que depender de lacuna ou desconformidade material. No modo `ENCERRAMENTO`, declarar `CONFORME PARA ENCERRAMENTO` somente quando **todos** os requisitos de fechamento aplicáveis tiverem comprovação suficiente, nenhuma divergência impeditiva permanecer e os aceites humanos obrigatórios estiverem documentados. Não usar ausência de erros conhecidos como substituto de cobertura completa. Uma auditoria tecnicamente conforme não supre o aceite humano do próprio encerramento.

## 11. Investigação, correção e autorizações

### 11.1. Ciclo obrigatório de tratamento

`IDENTIFICAR → LISTAR → INVESTIGAR CAUSA → BUSCAR ALTERNATIVAS → AVALIAR A NORMA E IMPACTOS → REVISAR ESCOPO → SOLICITAR AUTORIZAÇÃO → CORRIGIR LOCALMENTE → LISTAR DIFERENÇAS → BUSCAR ERROS RESIDUAIS → SOLUCIONAR NO ESCOPO → DOCUMENTAR → REAUDITAR → VALIDAR ENTREGA`.

A sequência não autoriza antecipar etapas bloqueadas pela norma competente. Se a ação se limitar à análise, executar apenas até a proposta; **nenhum arquivo é modificado**. Se a execução detectar nova necessidade fora do escopo, registrar a ocorrência e solicitar nova autorização antes de agir.

### 11.2. Proposta de correção obrigatória

Para cada modificação pretendida, apresentar ao responsável: ocorrência comprovada, regra/autoridade, causa, caminho completo relativo, linha/objeto, alteração exata, alternativas avaliadas, versões/hashes envolvidos, referências e dependentes, objetos protegidos, Gates impactados, riscos, testes e forma de reversão pela baseline preservada. Distinguir correções necessárias de melhorias opcionais e decisões humanas.

### 11.3. Autorização e escopo

Apenas uma autorização humana **expressa e específica** concede permissão para criar, modificar, excluir, substituir ou empacotar. A aprovação de arquitetura ou de um Gate anterior não abrange automaticamente todos os arquivos posteriores. Não editar documento, Skill, template, binário ou norma adicional por ter descoberto dependência: demonstrar necessidade e solicitar autorização própria. GitHub é estritamente somente leitura; alterações e entregas são locais.

### 11.4. Execução local e preservação

Trabalhar em cópia separada da baseline autorizada. Aplicar somente alterações necessárias e aprovadas; registrar diff e hashes novos. Preservar decisões, versões formalmente anteriores, evidências de Gate, normas, LEGADOS e exclusões. Não substituir globalmente tokens, caminhos, estados ou hashes. Recalcular referências correntes **após** estabilizar os bytes dos documentos afetados; detectar circularidade; não criar manifestos internos não autorizados.

### 11.5. Fora de escopo e falhas residuais

Uma falha descoberta durante a correção não será ignorada nem tratada como autorização implícita para ampliar a alteração. Registrar, classificar, indicar impacto real e bloquear só a parte dependente; reavaliar alternativas e pedir aprovação se nova mudança for indispensável. Não declarar conclusão do lote com falhas materiais não classificadas.

## 12. Segunda auditoria independente e controle de regressões

### 12.1. Obrigatoriedade

Após cada lote autorizado e antes de entregar, executar segunda auditoria sobre os **bytes finais**, não reutilizar cegamente resultados da primeira versão do arquivo. Reabrir cada item modificado e confrontá-lo com a baseline e com a norma aplicável. Uma nova auditoria da alteração não precisa reexecutar toda a auditoria global se os demais arquivos permanecem fisicamente idênticos e há inventário de hashes válido.

### 12.2. Testes mínimos da segunda auditoria

- Comparar conjunto exato de arquivos criados, modificados, excluídos e preservados com o escopo autorizado.
- Examinar diff completo: campos, estrutura, comentários, estados, semântica, ordem das decisões, termos e comportamento.
- Conferir que cada ocorrência prevista recebeu tratamento; buscar ativamente problemas adicionais, regressões, omissões, referências quebradas e implicações não antecipadas.
- Reexecutar validadores oficiais pertinentes e registrar seu alcance real; comparar resultados com o esperado.
- Recalcular SHA-256 e verificar links, identidades vigentes, evidências de aprovação, versões, dependências e ciclos, sem substituir hashes de decisões.
- Quando aplicável, inspecionar novamente as representações visuais, cálculos, configurações e binários dependentes e verificar invariantes com método apropriado.
- Validar preservações dos arquivos fora do escopo por comparação física; alterações não autorizadas são não conformidade.
- Avaliar novamente efeitos sobre Gates, aprovações e documentos congelados; registrar limitações não solucionadas.

### 12.3. Tratamento de falha

Corrigir somente dentro do escopo autorizado, repetir testes impactados e reabrir os objetos corrigidos. Se a falha exigir mudança fora da autorização, registrar impedimento específico e solicitar nova decisão. Resultado de teste `PASS` desacompanhado de entrada/método/saída não é prova suficiente.

## 13. Relatório, evidências e reprodução independente

### 13.1. Produto obrigatório da auditoria

O parecer deve ser entregue na conversa ou no meio autorizado. **Não criar arquivo persistente de relatório, inventário ou manifesto por iniciativa própria.** Se a norma/etapa exigir relatório materializado, solicitar autorização de criação com caminho e finalidade antes de escrevê-lo. Parecer resumido pode orientar, mas não substitui o registro integral das evidências exigíveis para concluir a auditoria.

### 13.2. Estrutura mínima do parecer

1. **FATOS VERIFICADOS:** identidade da base, modo, escopo, inventário dos arquivos efetivamente examinados (caminho, tipo, tamanho, SHA-256, finalidade e método), exclusões e limites.
2. **AUTORIDADES E RASTREABILIDADE:** fontes lidas, hierarquia, obrigações exigíveis, matriz por requisito com evidências e testes.
3. **CONFRONTOS FÍSICOS E DOCUMENTAIS:** integridade, estrutura, semântica, referências, hashes, versões, decisões e dependentes.
4. **INTERPRETAÇÕES:** hipóteses e inferências separadas de fatos; conflitos de autoridade e limitações verificáveis.
5. **OCORRÊNCIAS:** classificação, causa, impacto, urgência, necessidade real e alternativas.
6. **GATES E ESTADOS:** resultado de cada Gate aplicável do domínio e de cada controle da auditoria, sem aprovação presumida.
7. **IMPEDIMENTOS E PENDÊNCIAS:** operação afetada, prova faltante, correção autorizável, preservações e risco.
8. **PROPOSTA DE AÇÃO:** caminhos exatos, mudança, dependências, testes e autorização necessária; ou nenhuma alteração justificada.
9. **REVISÃO/ENTREGA, SE EXECUTADAS:** diff, resultados da segunda auditoria, ZIP/teste de aplicação e aceite/incorporação verificados.
10. **PRÓXIMO PASSO:** única operação admissível segundo normas e autorizações efetivas.

Em cada conclusão relevante, fornecer linha/trecho ou referência física e método, quando cabíveis. Não imprimir um inventário fictício de fontes não lidas; mencionar limitações com o estado `NÃO VALIDADO` adequado.

### 13.3. Reprodução sem contexto conversacional

Uma pessoa com o clone e as normas deve conseguir identificar: qual arquivo foi lido, em qual versão, com qual hash, qual fonte definiu a regra, qual decisão aprovou o objeto, como o teste foi feito, qual limite restou e que ação poderia ser tomada. Não depender de mensagens antigas para descobrir o significado de um estado ou de uma exceção. Decisão humana ocorrida na conversa só pode ser tratada como evidência persistente quando registrada conforme o contrato próprio, mediante autorização para modificar o documento correspondente.

## 14. Encerramento, entrega e comprovação de incorporação

### 14.1. Checklist de encerramento

A auditoria de encerramento deve demonstrar, para todos os itens aplicáveis: (a) base íntegra e fontes certas; (b) requisitos inventariados; (c) evidência física/documental suficiente; (d) contratos e estrutura cumpridos; (e) semântica confrontada; (f) referências e hashes correntes coerentes; (g) versões formais e evidências de Gate preservadas; (h) aprovações humanas específicas existentes; (i) dependências e regressões verificadas; (j) ressalvas legítimas explicitadas; (k) problemas impeditivos solucionados ou classificados como impedimento, sem declarar fechamento; (l) segunda auditoria após correções; (m) preservações demonstradas; (n) entrega e incorporação verificadas quando exigidas pelo objeto e pela etapa.

Uma ressalva aceita com escopo e decisão comprovados pode permanecer como limitação da conclusão; não converter ressalva em conformidade técnica irrestrita. Uma lacuna impeditiva bloqueia apenas o fechamento dependente até regularização.

### 14.2. Entrega local quando autorizada

Somente após autorização específica para empacotar: produzir um único ZIP local contendo **exclusivamente** arquivos criados/modificados autorizados, com caminhos relativos originais. Reabrir todos os arquivos e o pacote, conferir CRC, tamanhos, SHA-256, caminhos seguros, diff, referências e teste de aplicação limpa sobre uma cópia da baseline. Não incorporar arquivos temporários ou relatórios não autorizados. Não publicar ou escrever no GitHub.

### 14.3. Aceite e incorporação

Entrega do ZIP não constitui aceite humano nem prova de incorporação no clone. O responsável decide aceitar, ajustar ou rejeitar. A incorporação só é `CONFORME` após receber uma fonte física atualizada e conferir os bytes dos objetos incorporados e seus dependentes. Sem clone atualizado, registrar **incorporação não validada**, mesmo que o pacote esteja íntegro. Não declarar fechamento total antes de cumprir as condições efetivamente exigidas pela etapa responsável.

## 15. Contrato de integração com Skills, validadores e domínios

### 15.1. Relação SPEC → Skill → validação

- Esta SPEC é a **autoridade do método genérico de auditoria**; uma Skill operacional deverá aplicar seus controles, especificar comandos reais, entradas/saídas, interpretação de resultados e limites, sem redefinir decisões humanas ou requisitos dos domínios.
- Um contrato especializado deverá mapear `controle genérico → autoridade do domínio → objeto → procedimento concreto → evidência → teste`, sem copiar integralmente a norma específica. Na ausência desse contrato, o núcleo genérico aplica apenas os controles demonstráveis e declara o limite da especialização.
- Os validadores de cada domínio permanecem autoridades técnicas **somente das propriedades que efetivamente testam**; qualquer novo script deve declarar formatos de entrada, segurança, estados, códigos de retorno, verificações implementadas e não implementadas.
- A execução automatizada inicial da futura Skill deverá ser **somente leitura**, sem `--fix` implícito, gravações indiretas ou atualização de hashes sem autorização. A revisão assistida decide a necessidade e obtém autorização antes de qualquer escrita.
- A instalação de nova Skill, contrato especializado, script ou integração em processo existente é uma intervenção distinta, sujeita ao processo global e ao Gate de implementação correspondente. Esta SPEC sozinha não afirma que essas capacidades já existem.

### 15.2. Matriz de coerência e cobertura

Cada regra desta SPEC deve ter um identificador estável na matriz de construção. Para a implantação completa, exigir `regra → seção canônica → instrução executável da Skill → evidência produzida → teste determinístico ou avaliação humana justificada`. **Cobertura exigida: todas as regras aplicáveis**, sem esconder lacunas sob um percentual agregado. Se não houver automação segura para uma verificação, a Skill deverá indicar como obter/comprovar a evidência manualmente e como registrar `NÃO VALIDADO` quando faltar.

É proibido reduzir a Skill a um resumo superficial desta SPEC ou criar uma SPEC de domínio que repita e altere a autoridade existente. Documentos complementares devem ser completos em suas próprias responsabilidades, consistentes no significado dos estados, hashes e versões, e sem instruções incompatíveis.

### 15.3. Gates de construção da auditoria

A implementação da própria auditoria é controlada pelos Gates GVA definidos no plano autorizado: GVA-0 (baseline), GVA-1 (SPEC genérica integral), GVA-2 (contrato especializado), GVA-3 (Skill e integração), GVA-4 (verificações automatizáveis), GVA-5 (testes), GVA-6 (validação cruzada), GVA-7 (segunda auditoria) e GVA-8 (entrega/incorporação). Esses Gates **não são novos Gates de produto** nem aprovam automaticamente qualquer artefato dos processos auditados.

Cada Gate só avança mediante critérios e autorização correspondentes: leitura integral, completude, cobertura, testes, preservações, diff e revisão conforme sua natureza. A aprovação da arquitetura, de um Gate anterior ou desta SPEC **não autoriza automaticamente** produzir arquivos dos Gates posteriores. A SPEC deve permanecer utilizável para auditar outro domínio mesmo que a implantação inicial do contrato especializado ainda esteja pendente.

## 16. Matriz normativa de cobertura da implantação

A tabela vincula os requisitos de construção da auditoria aos locais em que esta **SPEC genérica** estabelece seu procedimento e aos métodos de verificação exigidos. Uma referência a Skill, contrato ou executor não comprova sua instalação; confirmar existência, integridade e estado dos componentes em cada clone examinado.

| ID | Exigência de GVA-0 | Seção canônica desta SPEC | Aplicação / verificação na implantação posterior |
|---|---|---|---|
| AU-R01 | Independência de assunto | 1.1, 15.1 | Conferir generalidade em domínios distintos |
| AU-R02 | Sob demanda em qualquer estágio | 2.1, 10.3 | Casos intermediários sem reprovação de futuro |
| AU-R03 | Auditoria de encerramento | 2.2, 10.3, 14 | Critérios finais do domínio exigíveis |
| AU-R04 | Fonte física antes da conclusão | 3.1–3.3, 5.1 | Inventário físico auditável |
| AU-R05 | Exclusões e LEGADOS | 2.4, 5.1 | Não acessar conteúdos excluídos |
| AU-R06 | Autoridades aplicáveis | 1.2, 4.1 | Matriz de precedência por requisito |
| AU-R07 | Bytes, tamanho, tipo, CRC e SHA-256 | 5.1–5.2 | Verificações por tipo e formato |
| AU-R08 | Rastreabilidade de requisitos | 4.2 | Matriz completa, sem requisitos omitidos |
| AU-R09 | Estrutura oficial especializada | 4.3, 6.1 | Reutilizar validador contratual aplicável |
| AU-R10 | Conformidade semântica | 6.2–6.3 | Conferência de fatos e limites |
| AU-R11 | Referências e dependências | 7.1–7.4 | Resolver destinos e vínculos |
| AU-R12 | Hash físico vigente | 8.1, 8.4 | Calcular e confrontar bytes atuais |
| AU-R13 | Ajustes sem histórico artificial | 8.1–8.2 | Não criar transição por edição simples |
| AU-R14 | Versões formais anteriores | 8.1, 8.3 | Preservação segundo norma do domínio |
| AU-R15 | Evidências de submissão e aprovação | 8.1, 9.3 | Não retroagir ou substituir decisão |
| AU-R16 | Impacto sobre Gates | 8.2, 9.4 | Teste de efeitos antes de editar |
| AU-R17 | Classificação objetiva | 10.1–10.2 | Ocorrência com evidência e classificação |
| AU-R18 | Autorização anterior à escrita | 1.2, 11.2–11.3 | Verificação de escopo autorizado |
| AU-R19 | Correção localizada e dependências | 11.4–11.5 | Diff e cadeia referencial |
| AU-R20 | Segunda auditoria | 12.1–12.3 | Reabrir e reexecutar testes impactados |
| AU-R21 | Relatório completo e evidências | 13.1–13.3 | Parecer rastreável e sem inferências |
| AU-R22 | Independência de conversa | 1.1, 13.3 | Reproduzir apenas com clone e normas |
| AU-R23 | Sem aprovação automática | 1.3, 9.2–9.4 | Gate humano mantém sua autoridade |
| AU-R24 | Não duplicar normas | 1.2, 15.1 | Teste de autoridade única |
| AU-R25 | Equivalência SPEC/Skill/testes | 15.2 | Matriz de cobertura cruzada |
| AU-R26 | Documento integral | 6.1, 13.1, 15.2 | Reprovar resumo e campo incompleto |
| AU-R27 | Executor inicial somente leitura | 11.3, 15.1 | Não escrever na auditoria por padrão |
| AU-R28 | Generalidade com especialização | 1.1–1.2, 4.3, 15.1 | Contrato de domínio isolado |
| AU-R29 | ZIP local e incorporação | 14.2–14.3 | Aplicação limpa e confronto físico |
| AU-R30 | Preservação dos processos atuais | 1.1–1.3, 9.4, 15.3 | Testes de não regressão normativa |

**Critério de completude:** ausência de uma obrigação, de procedimento verificável, de limite explícito ou de indicação da autoridade responsável impede o avanço da construção. A matriz não serve como substituto dos procedimentos dos §§1–15.
