# SaOr — Contrato operacional da Skill de Auditoria

## 1. Autoridade, natureza e alcance

Este contrato **especifica como executar** a [Skill de Auditoria](../SKILL.md) nos termos da [SPEC genérica de Auditoria](../../../.specs/auditor/PROCESSO-AUDITORIA.md). É referência operacional, não uma autoridade nova para requisitos, Gates, versionamento formal ou critérios materiais de outro processo. A ordem de precedência é: processo global de alteração; autoridade material do objeto; SPEC genérica para procedimento; contrato especializado vigente para aplicação; Skill e este contrato como instruções operacionais. Se duas fontes se contradisserem, registrar os trechos e suas competências, não improvisar desempate.

Este contrato se aplica a qualquer domínio, arquivo, conjunto, etapa ou implementação que tenha uma fonte física autorizada. As verificações específicas de wireframes, quando exigíveis, estão no [Contrato de Auditoria de Wireframes](../../../.specs/auditor/wireframes/CONTRATO-AUDITORIA-WIREFRAMES.md). Não converter esse contrato em obrigação de PNG, White/Black, Mobile, Prancha ou GI-4 para outros domínios. É proibido substituir a Skill documental da SPEC 3 ou seus modelos editoriais.

Este arquivo contém procedimentos e dados contratuais; **não instala ferramenta** nem cria permissão de escrita. A existência de `scripts/` ou `tests/` na nova Skill, quando implementados em Gate futuro, exige verificação física antes da execução. GVA-3 não inclui comandos automáticos novos nem resultados supostamente executados.

## 2. Entrada obrigatória e validação prévia

### 2.1. Campos e provas

| Campo | Fonte e validação mínima | Resultado se não comprovado |
|---|---|---|
| `fonte_fisica` | Caminho de ZIP/clone/diretório realmente acessível e autorizado | `NÃO VALIDADO` para identidade e afirmações dela dependentes |
| `identidade_da_base` | Tipo, tamanho, hash SHA-256 de contêiner quando aplicável, leitura segura | `BLOQUEADO` para operação que demande base íntegra |
| `objeto` | Caminhos/identificador confirmados pela norma do domínio e inventário real | Não selecionar por nome semelhante; delimitar novamente |
| `fronteira` | Incluídos, excluídos, dependências diretas e motivo de expansão | Registrar objeto fora de escopo como somente consultado |
| `dominio` | Autoridade normativa competente lida por completo | Aplicar controles genéricos apenas; especializados `NÃO VALIDADOS` |
| `modo` | `SOB_DEMANDA` ou `ENCERRAMENTO`; pedido e estado confrontados | Não presumir encerramento pelo título |
| `estagio` | Documento/Gate/decisão real aplicável ao objeto | `NÃO VALIDADO` nos testes que dependam do estágio |
| `versao_formal` | Registro ou contrato de versionamento do objeto | Não inferir pelo maior sufixo encontrado |
| `vigencia` | Ato de seleção quando houver autoridade de vigência | Não equiparar aprovação e vigência |
| `baseline_anterior` | Origem física anterior + inventário hashes e leituras, se alegar comparação incremental | Diferença histórica `NÃO VALIDADA`; formar nova baseline |
| `autoridade_aplicavel` | Caminho, função, competência, seção, versão/hash da norma | Bloquear critério dependente se ausente |
| `autorizacoes` | Texto, escopo, objeto, limites e data comprovada quando existir | **Sem escrita** em ausência de autorização específica |
| `restricoes` | `assets/`, LEGADOS declarados, congelamentos e exclusões | Proteger por padrão; exceção só por aprovação específica |
| `recursos_de_verificacao` | Script/biblioteca/ferramenta fisicamente disponível e método testável | Não reivindicar execução ausente |

O auditor pode determinar os campos a partir do clone e do pedido, sem formular perguntas redundantes. Quando o dado é indispensável e ausente, indicar a pergunta exata, o objeto impedido e a alternativa de prosseguir nas verificações independentes. Nunca preencher uma lacuna material com valor de exemplo.

### 2.2. Contrato de fonte física segura

Para ZIP, executar no mínimo: validar assinatura/estrutura de arquivo; construir inventário **somente dos membros elegíveis** sem explorar conteúdo de exclusões; inspecionar paths absolutos, traversal e duplicidades por normalização/case quando relevantes; detectar links simbólicos/entradas especiais; calcular tamanho, CRC e SHA-256 dos membros elegíveis; evitar extração não verificada. Para diretório, prevenir symlink escapando da raiz e observar permissões. Aplicar as leituras/inspeções determinadas por sua norma. Documentar qual método realmente executou cada conferência. Um teste parcial não pode ser anunciado como varredura completa.

Se o ZIP de origem contiver diretórios protegidos, não os listar internamente nem abrir os seus membros. A leitura dos bytes do contêiner para seu hash externo não autoriza inspeção interna das exclusões. Para arquivos LEGADOS, consultar somente a **classificação normativa autorizada**, sem interpretar seu conteúdo por padrão.

## 3. Contrato de resultado por controle AU-00 a AU-12

### 3.1. Colunas obrigatórias

Cada controle auditado deve produzir, no parecer ou registro autorizado: `ID`, `modo`, `objeto`, `estagio`, `fonte_normativa`, `localizacao_da_regra`, `arquivos_realmente_lidos`, `metodo`, `entrada`, `saida_observada`, `resultado_esperado`, `evidencia`, `estado`, `limites`, `dependencias`, `risco`, `decisao_ou_proxima_acao`. Sem fonte ou resultado demonstrável, não registrar `CONFORME`.

A evidência pode ser hash, medida, trecho, linha, screenshot/inspeção efetiva, resultado de teste ou transcrição fiel de decisão persistente conforme exigência do domínio. **Não** confundir execução de parser com compreensão funcional, comparação de pixels com comportamento interativo, nem hash de transporte com identidade aprovada de artefato.

### 3.2. Matriz de execução determinística e assistida

| Controle | Pré-condição | Execução exigida | Evidência/saída | Falha e avanço |
|---|---|---|---|---|
| AU-00 | Fonte acessível e objeto delimitado | Identificar container, escopo, estágio e modo; validar segurança inicial | Identidade da base, inventário de entrada | Fonte ilegível bloqueia verificação física dependente |
| AU-01 | Normas localizadas | Ler hierarquia, distinguir competências, selecionar contrato especializado correto | Matriz de autoridades com seção/trecho | Conflito ou norma ausente impede somente decisão dependente |
| AU-02 | Fonte e estágio | Relacionar exigidos, existentes, excluídos, dependentes e futuros | Inventário por função/estado com hash e tipo | Ausente exigível = ocorrência; futuro legítimo = `PENDENTE` |
| AU-03 | Requisitos/fontes aplicáveis | Ler ficha/contrato e mapear cada requisito à prova e teste | Matriz de rastreabilidade por ID | Obrigação sem evidência = `NÃO VALIDADO` ou desvio demonstrado |
| AU-04 | Modelo/validador vigente | Executar validação de estrutura pertinente ou inspeção formal equivalente identificada | Comando, versão/hash, saída e código de retorno | Não reivindicar execução de script ausente; estrutura não prova semântica |
| AU-05 | Texto/representação e autoridade | Confrontar fatos, ações, estados e conteúdo real; inspecionar visualmente quando preciso | Trecho/medição e parecer fundamentado | Sem ferramenta/visão suficiente = `NÃO VALIDADO` naquele item |
| AU-06 | Caminhos e referências existentes | Resolver destinos; classificar hashes por finalidade; calcular hash real; construir grafo | Matriz origem→destino com classes e SHA | Ciclos e referências ambíguas sem correção especulativa |
| AU-07 | Regra material de versão | Determinar ajustes, versões formais, vigência e cronologia | Registro que separa identidade atual, aceite e versão | Mudança de hash **não** gera versão automaticamente |
| AU-08 | Gates e decisões da norma | Verificar sequência, objeto, abrangência, aceites e dependências | Matriz por Gate e decisão real | Sem aceite obrigatório não avançar dependente; não revogar por conta própria |
| AU-09 | Desvios observados | Classificar, investigar causa, risco, necessidade e alternativas | Ocorrências com evidência e impacto | Crítica hipotética não deve virar erro comprovado |
| AU-10 | Ocorrência e possível correção | Delimitar arquivos, conteúdo, preservações, testes e aprovação humana | Proposta de intervenção por arquivo | Não executar escrita sem autorização específica |
| AU-11 | Correção previamente autorizada e efetiva | Conferir diff, novos bytes, referências, testes, regressões e limites | Segunda auditoria dos finais e dependentes | Nova alteração fora do escopo requer aprovação separada |
| AU-12 | Cobertura de todos os controles exigíveis | Emitir parecer integral e próximo ato permitido | Formato de Relatório com conclusão sustentada | Encerramento não é aceito sem provas e decisões humanas requeridas |

### 3.3. Verificação manual/assistida e automação

Somente um procedimento cujos dados e critérios sejam mensuráveis por ferramenta efetivamente instalada pode ser marcado como **executado automaticamente**. Exemplos possíveis, após GVA-4/GVA-5: hash/CRC, tipo, links, matriz de arquivos, estrutura e comparações pixel a pixel quando houver biblioteca segura. Verificação de conteúdo funcional, interpretação de contratos, decisão humana e inspeção de qualidade visual permanecem explicitamente assistidas quando não existir método automático validado. A saída de ferramenta deve preservar `entrada + versão/hash da ferramenta + comando + retorno + alcance + limitações`.

Nenhum parâmetro CLI da Skill de Auditoria está estabelecido neste GVA-3. Antes de o executor ser implantado, utilizar os recursos disponíveis de inspeção sem criar comando inexistente; para a SPEC 3, pode-se executar o **validador editorial já instalado** nos termos da Skill documental, sem reimplementar sua lógica.

## 4. Distinção obrigatória entre os estados

### 4.1. Estado auditorial versus estado do objeto

| Estado de auditoria | Condição objetiva para atribuição | O que ele **não** afirma |
|---|---|---|
| `CONFORME` | Teste aplicável efetuado e evidência suficiente satisfaz a norma | Não aprova Gate humano nem declara sistema concluído |
| `NÃO CONFORME` | Violação material demonstrada por norma e evidência | Não equivale automaticamente à revogação de Gate anterior |
| `NÃO VALIDADO` | Falta evidência, ferramenta ou fonte confiável suficiente | Não é prova de inexistência ou de erro |
| `PENDENTE` | A obrigação ainda não é exigível naquele estágio | Não é reprovação antecipada |
| `NÃO APLICÁVEL` | A norma demonstra que o item não pertence ao estágio/objeto | Não é desculpa para ausência de dado obrigatório |
| `BLOQUEADO` | Uma operação concreta não pode avançar por causa específica | Não bloqueia universalmente trabalhos independentes |

Não colapsar `VIGENTE`, `APROVADO`, `CONGELADO`, `CONCLUÍDO` ou `CONFORME TECNICAMENTE` do domínio em um desses estados. O estado de auditoria reflete a **verificação**, não altera o estado persistente do objeto auditado. Comprovante humano exige decisão expressa, objeto e escopo correspondentes.

### 4.2. Cálculo da exigibilidade e encerramento

No modo `SOB_DEMANDA`, determinar Gate atual por prova: seus requisitos já exigíveis devem ser testados, e os futuros legitimamente pendentes não serão contabilizados como erros. No modo `ENCERRAMENTO`, identificar **todos** os requisitos obrigatórios e aceites, verificar fechamento real e ressalvas, e proibir conclusão favorável quando faltar evidência de alguma condição material. Resultado parcial ou `NÃO VALIDADO` que não afete o próximo passo pode coexistir com testes conformes, mas **nunca é substituído por CONFORME global**. Não usar contagem de testes como substituto de cobertura.

## 5. Referências, hashes e dependências

### 5.1. Registro por referência

| Campo | Evidência exigida |
|---|---|
| Origem | Caminho e seção/linha da referência, com identidade física do arquivo de origem |
| Destino | Caminho verificável, versão do objeto e ligação normativa |
| Tipo | Categoria canônica da SPEC genérica §8.1; sem categoria, `HASH_SEM_CLASSIFICACAO` |
| SHA declarado | Valor integral na fonte, identificado por propósito |
| SHA recalculado | Valor obtido de **bytes reais** do objeto correspondente, ou ausência justificada |
| Evento | Data/decisão quando é identidade de aprovação ou origem |
| Estado da comparação | Corrente igual, divergente, snapshot não acessível, inaplicável etc., com evidência |
| Tratamento | Preservar, propor atualizar referência **corrente**, solicitar decisão ou não alterar |
| Dependências | Objetos e referências que poderão mudar após alteração autorizada |

Valores correntes se relacionam aos bytes finais do documento presente; a versão formal é conceito distinto. Um hash de submissão aprovada pode divergir do arquivo pós-registro e continuar sendo evidência válida do ato; conferir data, objeto e sequência antes de classificá-lo. Sem bytes do snapshot, a identidade do evento pode estar documentada, mas sua nova verificação física é `NÃO VALIDADA`.

### 5.2. Sequência de correção de referências (sujeita a autorização)

1. Investigar o contexto **de cada** SHA divergente; classificar referência e localizar destino.
2. Determinar se o hash citado representa bytes atuais ou evento anterior documentado.
3. Para `HASH_FISICO_ATUAL` incorreto, conferir bytes, causa, autoridade e necessidade; não alterar apenas porque a sequência hexadecimal não coincide.
4. Para `HASH_AJUSTE_SUBSTITUIDO` dentro da mesma versão, não criar histórico de versões ou catálogo de revisões intermediárias; propor substituir somente vínculos correntes obsoletos.
5. Para `HASH_SUBMISSAO_OU_APROVACAO`, preservar os valores de submissão e a decisão, mesmo que o objeto físico atual inclua adendo posterior; não trocar a evidência pelo hash presente.
6. Para `HASH_VERSAO_FORMAL_ANTERIOR`, preservar o artefato e seu vínculo de versão segundo sua norma; não tratar como corrente.
7. Para `HASH_DE_ORIGEM_DOCUMENTADA`, verificar o objeto realmente utilizado e a exigência de prova de origem; preservar sua função documental.
8. Para `HASH_SEM_CLASSIFICACAO`, registrar incerteza, obter fonte/autorização e **não** substituir.
9. Mapear todas as referências correntes e dependentes; detectar autorreferência/ciclos antes de propor edição.
10. Obter autorização expressa para cada caminho; editar em cópia local, calcular hashes só depois da última edição; reauditar todos os vínculos afetados.

Se dois documentos dependem mutuamente dos hashes finais um do outro, não é possível estabilizá-los por atualização alternada. Registrar o ciclo, buscar mecanismo expressamente permitido pelo contrato (por exemplo, uma referência temporal de origem ou decisão), **sem criá-lo por preferência do auditor**. O próprio SHA final não pode ser incluído como literal dentro do próprio arquivo e permanecer igual após gravá-lo.

### 5.3. Preservação sem histórico artificial

**Ajuste na mesma versão** altera a identidade física, não a versão formal por si. Os SHA substituídos por esse ajuste não viram histórico de versões, não recebem nova `vNN` e não serão mantidos como lista de revisões. **Evidência de decisão ou origem comprovada** pode continuar apontando para bytes de um evento anterior da mesma `vNN`; deve permanecer identificada como evidência, sem ser classificada como versão histórica. **Nova versão formal** exige preservar a anterior conforme a autoridade especializada. Nenhuma dessas regras permite editar artefato congelado sem autorização, nem ignora Gates impactados.

## 6. Gates, decisões humanas, riscos e correções

### 6.1. Matriz por Gate

| Dado | Como demonstrar |
|---|---|
| Processo e Gate | Autoridade canônica e etapa exata |
| Unidade | Objeto, versão, tema/página/estado ou outra dimensão exigida |
| Pré-condições | Artefatos, aprovações e dependências anteriores necessários |
| Operação | O que a norma permitiu realizar no estágio |
| Evidência | Caminho, hash físico, teste, decisão ou registro comprovado |
| Decisão humana | Responsável, data real, teor e abrangência quando exigidos |
| Resultado | Estado oficial no processo responsável; separado do auditor |
| Regressão | Mudanças que podem exigir reavaliação ou retorno específico |
| Próximo ato | Operação permitida pela norma, ou causa do bloqueio |

Não importar GI-0–GI-4 para outras áreas. No domínio de wireframes, não herdar Gates da SPEC 1 na SPEC 3, e não chamar a seleção de referência da SPEC 2 de aprovação de PNG. A decisão sobre um conjunto exige a abrangência coletivamente aprovada quando essa norma o determinar.

### 6.2. Registro de ocorrência e decisão de intervenção

Para cada divergência identificar: ID; norma e cláusula; caminho/linha/visão; esperado; encontrado; evidência; classificação taxonômica; estado de auditoria; causa investigada; hipóteses remanescentes; impacto; regressões; dependentes; necessidade real; alternativas; solução autorizável; preservações; Gate afetado; autorização requerida. Distinguir necessidade de correção, melhoria opcional e decisão humana. Uma diferença legitimamente histórica não pode ser "corrigida" só para parecer vigente.

### 6.3. Autorizações e execução local

Uma solicitação de auditoria não é autorização para editar. Antes de escrever/empacotar: apresentar necessidade, fonte, caminhos, conteúdo proposto, riscos, testes e preservações; obter autorização humana **expressa e delimitada**. Editar apenas numa cópia local autorizada; conservar a baseline original e comparação de hashes/diff. Reabrir arquivos, conferir vínculos, reexecutar validadores e executar segunda auditoria dos bytes finais. Se surgir dependência não autorizada, registrar e solicitar extensão de escopo, sem edição silenciosa.

## 7. Segundo ciclo de verificação e entrega

### 7.1. Segunda auditoria, independente do primeiro resultado

Depois de correção autorizada: confrontar lista de arquivos criados/modificados/excluídos com autorização; reabrir **todos** os arquivos alterados; comparar diffs; rastrear novo hash corrente; verificar que decisões e versões formais não foram reescritas; resolver novamente caminhos e referências; executar testes afetados; investigar erros residuais e regressões; classificar cada ocorrência. A revisão precisa buscar erros novos e não apenas demonstrar que o erro inicial desapareceu. Quando novo problema exigir outra autorização, limitar o bloqueio ao ato dependente.

### 7.2. Entrega e incorporação

Se e somente se houver autorização de entrega: testar aplicação limpa sobre cópia da baseline autorizada; empacotar **um ZIP local** com somente alterações aprovadas e caminhos relativos originais; reabrir ZIP, confirmar integridade/CRC/tamanhos/SHA e conferir ausência de extras. Não enviar ao GitHub. Após aceite, exigir clone físico atualizado para verificar realmente incorporação; pacote entregue não equivale a arquivo incorporado nem a novo aceite de Gate.

## 8. Regras de reprodutibilidade e qualidade documental

| Controle de qualidade | Critério obrigatório |
|---|---|
| Completude | Todos os requisitos exigíveis têm fonte, método, evidência, resultado/limite e estado |
| Consistência | SPEC, contrato de domínio, Skill e relatório expressam **o mesmo comportamento** |
| Fidelidade | Normas originais e decisões humanas têm precedência; não copiar regra de exemplo |
| Precisão de SHA | Não atualizar evidências de aprovação como se fossem referências correntes |
| Independência | Um auditor com somente o clone e as normas consegue repetir o procedimento |
| Segurança | Exclusões respeitadas, sem acesso a arquivos protegidos ou escrita não autorizada |
| Transparência de ferramenta | Comando e versão reais; não declarar scripts não instalados nem testes não executados |
| Escopo | Alterações delimitadas, diffs auditáveis, sem regressão fora do aprovado |
| Relatório | Aplicar [FORMATO-RELATORIO.md](FORMATO-RELATORIO.md) integralmente |
| Encerramento | Nenhuma pendência impeditiva e todos os aceites exigidos comprovados |

Não reduzir este contrato a uma checklist de etiquetas. O estado `CONFORME` só decorre de evidências e testes efetivamente executados. Se faltar prova material para um requisito, registrar `NÃO VALIDADO` com consequência precisa. Se o objeto estiver num Gate futuro, registrar `PENDENTE` sem fabricar falha. Se a regra especializada impuser preservação ou nova versão, aplicá-la sem substituir por preferência do auditor.
