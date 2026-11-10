---
name: saor-auditoria
description: Executa a auditoria genérica de conformidade e integridade do SaOr sob demanda ou após o encerramento do processo responsável, aplicando a SPEC canônica, contratos de domínio, evidências físicas, rastreabilidade, hashes, versões, Gates e segunda auditoria, sem editar arquivos ou aprovar decisões humanas automaticamente.
---

# SaOr — Skill operacional de auditoria de conformidade e integridade

## 1. Papel, ativação e fronteiras

### 1.1. Missão operacional

Esta Skill **executa, conduz e documenta a auditoria** definida em [`.specs/auditor/PROCESSO-AUDITORIA.md`](../../.specs/auditor/PROCESSO-AUDITORIA.md). Sua finalidade é produzir um parecer **integral, rastreável e reproduzível**, a partir de evidências do projeto real, para qualquer objeto, domínio ou estágio. É procedimento de auditoria, não uma nova norma de requisitos, uma ferramenta de implementação de software ou um substituto da SPEC responsável pelo objeto.

Aplicar esta Skill quando (a) uma auditoria for solicitada em qualquer etapa (`SOB_DEMANDA`); (b) um processo especializado tiver cumprido suas etapas finais e precisar da auditoria obrigatória anterior ao encerramento (`ENCERRAMENTO`); ou (c) houver correção autorizada que exija segunda auditoria. No terceiro caso, identificar também o modo e o estágio do objeto. **Não antecipar a auditoria de encerramento apenas porque a Skill foi carregada.**

O gatilho obrigatório é uma **exigência do fluxo normativo** depois dos Gates finais, não prova de disparo automático por evento de sistema. Se não existir executor/acionador fisicamente instalado, iniciar a Skill por chamada explícita e registrar a limitação. Esta Skill Markdown não executa comandos por si mesma.

### 1.2. Autoridades e ordem imutável de consulta

1. Ler primeiro, na base física, [`.specs/PROCESSO-ALTERACAO-ASSISTIDA.md`](../../.specs/PROCESSO-ALTERACAO-ASSISTIDA.md) **integralmente**; depois [`.specs/README.md`](../../.specs/README.md).
2. Ler integralmente a [SPEC genérica de auditoria](../../.specs/auditor/PROCESSO-AUDITORIA.md), especialmente §§2–15, e o índice [`.specs/auditor/README.md`](../../.specs/auditor/README.md).
3. Identificar o domínio pelo contrato responsável e pela natureza comprovada do objeto. Se houver contrato especializado vigente, lê-lo **integralmente** e ler suas normas de origem. No domínio de wireframes, o contrato inicial é [`.specs/auditor/wireframes/CONTRATO-AUDITORIA-WIREFRAMES.md`](../../.specs/auditor/wireframes/CONTRATO-AUDITORIA-WIREFRAMES.md), que diferencia SPECs 1, 2 e 3.
4. Ler a documentação e os artefatos competentes e seus vínculos materiais; consultar Skills existentes somente para as operações sob sua autoridade. Para Markdown da SPEC 3, o formato continua pertencendo a [`.skill/saor-analise-documental/SKILL.md`](../saor-analise-documental/SKILL.md), seus templates e validadores, **não** a esta Skill.
5. Ler [CONTRATO-OPERACIONAL.md](references/CONTRATO-OPERACIONAL.md) para as entradas/saídas, estados, decisões, testes e limites de automação; usar [FORMATO-RELATORIO.md](references/FORMATO-RELATORIO.md) para emitir o parecer completo.

Conflito entre fontes: identificar texto exato, versão, objeto, competência e cronologia. Não produzir uma regra conciliatória sem autoridade. A norma do domínio continua autoridade **material** do objeto; a SPEC de auditoria é autoridade do **procedimento de verificação**; o processo global prevalece para qualquer escrita. Uma Skill não pode aprovar Gate, selecionar vigente ou modificar a baseline.

### 1.3. Proibições e preservações

Não usar memória de conversa, nomes, commit, README operacional, semelhança com outro módulo ou suposição de estrutura como prova. Não declarar como efetuada a leitura de um arquivo apenas porque seu hash foi calculado. Não declarar inspeção de imagem sem abri-la e interpretar visualmente suas características. Não inventar entradas, scripts, comandos, parâmetros, resultados, aprovações, datas ou mecanismos automáticos. Não criar relatório/manifesto persistente, cópia alterada, correção ou ZIP sem autorização específica. Nunca escrever no GitHub nem transmitir conteúdo local ao repositório remoto.

`assets/` é imutável e excluído: não listar internamente, abrir, decodificar ou alterar. Materiais que a fonte canônica classificar como **LEGADOS** permanecem fora da releitura por padrão e preservados; exceção exige justificativa e autorização específica. Um arquivo antigo não é LEGADO apenas por seu nome. Nas demais áreas, preservar artefatos congelados, decisões e versões formalmente anteriores de acordo com sua autoridade, sem reconstruí-los por conveniência.

## 2. Seleção da operação e pré-voo obrigatório

### 2.1. Modo e estágio

| Pedido/condição | Modo operacional | Critério de execução | Resultado permitido |
|---|---|---|---|
| Verificar um objeto durante sua implementação, revisão ou investigação | `SOB_DEMANDA` | Auditar somente obrigações já exigíveis e dependências do próximo ato | Parecer do estágio; Gate futuro `PENDENTE`, nunca reprovação antecipada |
| Verificar objeto após conclusão das etapas e Gates competentes | `ENCERRAMENTO` | Auditar integralmente todas as condições finais e aceites requeridos | Parecer de conformidade para encerramento **somente com cobertura e prova completas** |
| Verificar um lote previamente corrigido | O modo que corresponde ao objeto + ciclo de reauditoria | Usar bytes finais, autorização e diff; testar todos os dependentes impactados | Parecer do lote, sem declaração prematura de incorporação |

Se a expressão “encerrado” constar somente em conversa ou título, comprovar o estágio por fonte persistente. Ausência de estágio comprovável = `NÃO VALIDADO` para as operações dependentes. Perguntar apenas quando dado indispensável não puder ser reconstruído da fonte autorizada e alterar materialmente o resultado.

### 2.2. Ficha de entrada obrigatória

Antes de qualquer conclusão, reunir a ficha: fonte e caminho físico, tipo, tamanho e SHA-256 da base; objeto e fronteira; domínio; modo; estágio; versão formal/vigência quando aplicáveis; autoridades selecionadas; cópia anterior para comparação se houver; restrições, exclusões, LEGADOS, decisões e autorização existente; limitações da ferramenta. Preencher cada campo com evidência ou `NÃO VALIDADO — motivo e operação afetada`. Usar a tabela de contrato do [CONTRATO-OPERACIONAL.md](references/CONTRATO-OPERACIONAL.md) §2. Não transformar fonte de leitura em permissão de edição.

### 2.3. Segurança física antes de inspecionar

1. Identificar container ZIP/diretório, calcular SHA-256 e tamanho do container, se aplicável; verificar legibilidade e integridade estrutural.
2. Em ZIP, identificar membros elegíveis sem entrar no conteúdo interno de `assets/`; rejeitar caminhos absolutos, `..`, ambiguidades de normalização, duplicidades perigosas, links simbólicos e entradas especiais incompatíveis. Não extrair um ZIP não verificado diretamente sobre a baseline.
3. Verificar CRC e tamanho de cada membro elegível e calcular seu hash pelos bytes integrais. Identificar tipo por conteúdo quando pertinente, não só extensão; evitar executar fontes não confiáveis.
4. Aplicar leitura contextual integral exigida pelo processo global à primeira base ainda não validada; interpretar semanticamente normas/contratos/documentos e inspecionar realmente imagens/bibliotecas/binários pertinentes.
5. Havendo base física anterior com inventário de hashes, leituras e limites verificáveis, comparar `caminho → tamanho → SHA-256`; reinterpretar arquivos novos/alterados e dependências afetadas. Não usar memória como baseline. Falta de base física comparável = comparação incremental `NÃO VALIDADA`.
6. Produzir inventário na resposta, com caminho, função, tipo, tamanho, SHA-256, método de leitura/inspeção e limitação. Não persistir inventário por iniciativa própria.

Se um teste de acesso, caminho ou integridade falhar, marcar o item e **somente a operação dependente** como `BLOQUEADO`, mantendo resultados independentes verificáveis. Falha de biblioteca ou impossibilidade de decodificar imagem não deve ser convertida em inspeção visual bem-sucedida.

## 3. Sequência única de auditoria (AU-00 a AU-12)

A sequência abaixo executa os controles da SPEC genérica. Cada controle exige **entrada, fonte, operação, evidência, classificação, limite e condição de avanço**; a matriz do Contrato Operacional especifica esse esquema. Não pular controles porque se espera que o objeto esteja aprovado. `NÃO APLICÁVEL` requer prova de inaplicabilidade.

### AU-00 — Identificação física, estágio e modo

Entrada: fonte e objeto. Verificar container, exclusões, tipo, hash, estado verificável e se existe base anterior. Produzir ficha inicial e inventário preliminar; confrontar o modo com a intenção e o estágio. Falha de identidade não permite afirmar conformidade física. Evidência: metadados da fonte e leitura dos controles de autoridade.

### AU-01 — Descoberta de normas e autoridade competente

Ler o processo global, índice, SPEC genérica, contratos de domínio e normas diretamente aplicáveis. Elaborar matriz `norma → competência → requisito/controle → versão/vigência → evidência → limites`. Se a autoridade material for ambígua, identificar conflito e suspender apenas a verificação dependente; não importar regras de outra área. No domínio de wireframes, selecionar separadamente a trilha de construção de template, referência oficial ou interface funcional conforme seu contrato, sem herança dos Gates entre trilhas.

### AU-02 — Inventário completo do que é exigível

Determinar arquivos esperados, arquivos existentes, dependências, exclusões, Gate atual, versões formais, temas/páginas/estados quando o contrato exigir. Comparar o conjunto esperado com o físico; não considerar a simples existência como aprovação. Registrar ausentes, divergentes e não aplicáveis com sua fonte. Dependências verificadas para análise não são automaticamente candidatas a alteração.

### AU-03 — Matriz de requisitos e rastreabilidade

Para cada obrigação: `ID → texto/trecho fonte → situação de exigibilidade → objeto → componente/comportamento/documento → evidência física → método → resultado → decisão/limite`. Reler integralmente a ficha/contrato pertinente; separar requisito explícito, regra técnica, decisão humana e hipótese. Obrigações ainda futuras recebem `PENDENTE`; ausência de evidência obrigatória já exigível recebe `NÃO VALIDADO`, `NÃO CONFORME` ou `BLOQUEADO` conforme prova e efeito. Não criar requisito substituto para lacuna.

### AU-04 — Conformidade de formato e estrutura

Selecionar somente modelos/validadores fisicamente instalados e efetivamente aplicáveis. Confrontar títulos, ordem, campos, tabelas, placeholders e formatos com o contrato vigente. No domínio de wireframes, reutilizar os três modelos/validador da Skill documental **somente para documentos da SPEC 3** e conferir também conteúdo. Registrar comando real, arquivo, hash do script/modelo, saída, retorno e alcance do teste; não inventar uma chamada CLI ainda inexistente nesta Skill. Ausência de validador aplicável não autoriza alegar execução.

### AU-05 — Semântica, fatos e evidências

Confrontar a interpretação de todo conteúdo material com a fonte competente e, quando aplicável, a representação realmente examinada. Registrar linha/trecho, comportamento esperado, observado e limite. Inspecionar diretamente imagens necessárias, identificar dimensões, textos, recortes e componentes; validar parâmetros impossíveis de inferir do raster somente quando houver fonte técnica adicional. Aprovado no validador estrutural não implica correto em semântica ou funcionalidade. Não reproduzir como fatos decisões apenas narradas em conversa.

### AU-06 — Referências, dependências e hashes

Resolver links, objetos referidos, relações de origem e documentos afetados. Para cada SHA: localizar referência, campo, objeto, evento, norma e tipo de identidade; calcular o hash físico do destino e aplicar **antes de decidir ajuste** a classificação canônica da SPEC genérica §8. Distinguir `HASH_FISICO_ATUAL`, `HASH_SUBMISSAO_OU_APROVACAO`, `HASH_VERSAO_FORMAL_ANTERIOR`, `HASH_AJUSTE_SUBSTITUIDO`, `HASH_DE_ORIGEM_DOCUMENTADA` e `HASH_SEM_CLASSIFICACAO`. Construir matriz `fonte → destino → classe → SHA citado → SHA calculado → decisão → resultado`. Detectar autorreferência e ciclos; não tentar corrigi-los em loop ou por substituição global.

### AU-07 — Versão formal, vigência e cronologia

Verificar o contrato de versionamento específico. Correção dentro da **mesma versão formal** não cria versão nova nem histórico artificial de hashes intermediários. Quando autorizado e necessário, referências correntes passam a apontar para bytes finais. Preservar, porém, `HASH_SUBMISSAO_OU_APROVACAO` e `HASH_DE_ORIGEM_DOCUMENTADA` comprovados como evidências de atos, **não** como histórico de versões. Versão anterior formalmente substituída exige preservação conforme sua norma. Mudança de bytes em objeto congelado requer análise dos Gates mesmo sem mudança no rótulo `vNN`. Divergência de SHA isolada não demonstra nova versão ou defeito.

### AU-08 — Gates e aceites humanos

Reconstruir os Gates da norma especializada, as condições de entrada, objetos de cada decisão, ordem, data, abrangência e efeitos sobre dependentes. Verificar versões, hashes de submissão e aceites individuais/de conjunto quando exigidos. Separar estados `APROVADO`, `VIGENTE`, `CONGELADO`, `CONFORME TECNICAMENTE`, `CONCLUÍDO` e `PENDENTE`. Auditor técnico e validador não podem conceder nem revogar aprovação humana. Falta de aceite obrigatório bloqueia somente a operação dependente; não reabrir todos os Gates sem causa.

### AU-09 — Classificação e investigação de ocorrências

Registrar cada caso com a taxonomia **exata** do processo global, além do estado de auditoria da SPEC §10; são campos independentes. Investigar causa raiz, hipótese remanescente, impacto, regressão, vínculo com decisões e necessidade real de correção. Distinguir erro material, documentação desatualizada, histórico legítimo, diferença intencional, lacuna e ausência de necessidade de alteração. Não propor mudanças artificiais apenas para uniformizar documentos antigos.

### AU-10 — Propostas de regularização, sem escrita presumida

Para cada correção necessária, demonstrar `arquivo/caminho/trecho → fonte → causa → mudança exata → dependências → preservações → Gates → riscos → testes → autorização`. Se não houver autorização expressa e específica, **parar antes de criar ou modificar**. Uma autorização limitada a um arquivo não autoriza modificar seus dependentes; registrar consequência e solicitar aprovação adicional. Melhoria opcional não se transforma automaticamente em correção exigida.

### AU-11 — Reauditoria após alteração autorizada

Somente quando houve autorização e implementação do lote por processo competente: reabrir bytes finais, calcular SHA-256, conferir diff e escopo, reexecutar testes afetados, percorrer dependências, buscar regressões/erros novos, classificar resíduos e corrigir somente dentro do escopo. Não editar objetos em uma auditoria de leitura apenas porque a causa foi determinada. Se houver dependente fora do escopo, separar bloqueio e proposta de autorização.

### AU-12 — Parecer e condição de encerramento

Consolidar todos os AU aplicáveis no formato integral do [FORMATO-RELATORIO.md](references/FORMATO-RELATORIO.md), distinguindo fato, interpretação, pendência e aprovação solicitada. No `ENCERRAMENTO`, só declarar `CONFORME PARA ENCERRAMENTO` quando **todas** as obrigações finais aplicáveis estiverem demonstradas, com aceites humanos necessários e nenhuma lacuna impeditiva. Aprovação técnica e geração de ZIP não equivalem a aceite nem a incorporação física; verificar a incorporação apenas após receber clone atualizado. No `SOB_DEMANDA`, relatar estado atual e próximo Gate permitido sem reprovar trabalhos legitimamente futuros.

## 4. Instruções de execução por especialização

### 4.1. Contrato de domínio e seleção da trilha

Ao identificar um domínio, verificar fisicamente se seu contrato de auditoria existe e foi aprovado. A Skill não fixa uma lista fechada de domínios nem cria critérios especializados por analogia. Se o contrato for ausente, executar só controles genéricos que possam ser comprovados e declarar `NÃO VALIDADO` nos critérios especializados indispensáveis. Para wireframes, usar o [contrato autorizado](../../.specs/auditor/wireframes/CONTRATO-AUDITORIA-WIREFRAMES.md), §§2–15; selecionar por natureza do objeto e fonte: SPEC 1 para criação do modelo, SPEC 2 para seleção da referência, SPEC 3 para interfaces funcionais. Uma chamada de auditoria pode ter mais de uma trilha, mas as matrizes de Gate permanecem separadas.

### 4.2. Skill documental da SPEC 3 — reutilização sem concorrência

Quando o objeto auditado incluir os Markdown do Controle GI-0/GI-1, TextFrame GI-2 ou Composição GI-3/GI-4, ler os templates integrais existentes e aplicar o validador oficial conforme a [Skill documental](../saor-analise-documental/SKILL.md) e contrato especializado §7. As formas de uso autorizadas no repositório são `--templates` e `--tipo ... --arquivo ...`, sempre com caminhos físicos reais e os arquivos instalados na base; executar a partir da raiz conforme os parâmetros documentados pelo script. A estrutura não deve ser reproduzida em novo template da auditoria. A SPEC 1 possui Wireframe Text próprio; não aplicar os três modelos da SPEC 3 ao objeto errado. Resultado do script não valida semântica.

### 4.3. Verificações de imagem e evidências materiais

Somente quando o contrato especializado exigir e houver acesso físico, inspecionar PNG/representações relevantes e medir dimensões e pixels com ferramentas apropriadas. ViewPort, escala, máscaras e limites devem ser obtidos do contrato vigente daquele objeto; **nunca usar medidas concretas de um modelo como regra universal**. Relatar comparações de pixels, coordenadas, recortes, falhas e limitações. Não confundir imagem estática com prova de navegação ou implementação executável.

### 4.4. Generalidade em outros domínios

Para outra área, repetir os controles AU-00 a AU-12, selecionando as autoridades reais e verificações próprias. Não exigir White/Black, Mobile, GI-4, PNG, TextFrame, Prancha nem modelo de template se não forem exigíveis na norma do objeto. Não apresentar ausência desses artefatos como erro num domínio não visual. Se o domínio exigir outra modalidade de prova (código, testes de API, configuração, planilha ou documentação), somente usá-la quando a norma competente e as ferramentas permitirem comprovação.

## 5. Política de execução de ferramentas e automação

### 5.1. Disponibilidade real

O GVA-3 produziu **documentação operacional e referências**, sem antecipar o executor do GVA-4 ou os testes do GVA-5. O executor e a suíte foram implementados posteriormente sob autorizações próprias; sua presença nesta cópia de trabalho **não comprova instalação** no clone do responsável. Antes de qualquer uso, verificar fisicamente `.skill/saor-auditoria/scripts/auditar_integridade.py` e `.skill/saor-auditoria/tests/test_auditar_integridade.py`, suas versões, integridade e disponibilidade na base efetivamente auditada. Não citar comandos como executados sem evidência, não declarar auto-disparo por evento e não atribuir à Skill capacidade de corrigir hashes automaticamente.

### 5.2. Automação apenas de verificações demonstráveis

O verificador implementado no GVA-4, **quando fisicamente disponível e validado na fonte auditada**, calcula hashes, inventaria membros elegíveis e verifica CRC, caminhos, links Markdown inline e pixels mediante parâmetros e bibliotecas aplicáveis. A suíte do GVA-5 testa os comportamentos automatizados explicitamente cobertos, sem substituir auditoria semântica. O contrato de entrada/saída, os limites e os testes de regressão precisam ser conferidos antes da execução. O verificador **não** autentica decisões humanas, interpreta integralmente textos funcionais ou aprova Gates por análise sintática. Operação sem prova confiável deve resultar `NÃO VALIDADO`, acompanhada da evidência faltante. É proibida autoedição implícita.

### 5.3. Correções autorizadas e separação de papéis

Esta Skill opera **somente leitura por padrão**. Se o responsável autorizar um lote de correção, a execução material ocorrerá em cópia local pelo processo global, exclusivamente nos arquivos autorizados; a Skill delimita e depois reaudita a mudança. Não combinar descoberta de erro e escrita silenciosa em uma única rotina. Solicitação de auditoria não autoriza criar relatório, manifesto, arquivos de teste ou ZIP persistentes. A validação de entrega e incorporação só ocorrerá quando a fase e autorização correspondentes exigirem.

## 6. Formato de evidência e resultado obrigatório

### 6.1. Registro mínimo por controle

Para todo AU aplicável, manter: `ID; modo; estágio; fonte e trecho; objeto; método; arquivos lidos/inspecionados; entrada; resultado bruto; verificação; estado; alcance; limitações; dependentes; decisão de avanço`. Confrontar o contrato operacional §3. Não apenas informar “PASS”; registrar o que foi realmente testado e não transformar inspeção indireta em prova semântica.

### 6.2. Classificações e estados permitidos

Classificação de ocorrência: **ERRO COMPROVADO; DOCUMENTAÇÃO DESATUALIZADA; LEGADO VÁLIDO; DECISÃO HISTÓRICA; INCONSISTÊNCIA ENTRE FONTES; REFERÊNCIA QUEBRADA; DIFERENÇA INTENCIONAL; LACUNA DOCUMENTAL; SEM NECESSIDADE DE ALTERAÇÃO.** Estado de verificação: **CONFORME; NÃO CONFORME; NÃO VALIDADO; PENDENTE; NÃO APLICÁVEL; BLOQUEADO.** Diferenciar de estados dos Gates e do artefato; os termos não são conversíveis automaticamente. Em `BLOQUEADO`, identificar precisamente a operação e a condição para liberação.

### 6.3. Parecer integral, independente desta conversa

Utilizar integralmente o [FORMATO-RELATORIO.md](references/FORMATO-RELATORIO.md). Incluir inventário auditável, autoridades, matriz de requisitos, testes por controle, decisões, referências classificadas, limites, ocorrências, riscos, ações autorizáveis, estado e próximo Gate. Relatórios de comparação incremental precisam nomear base anterior física, hashes e arquivos interpretados ou reutilizados. Não inserir dados inventados para preencher modelo nem usar tabelas vazias como prova de auditoria. Não criar arquivo materializado sem autorização.

## 7. Matriz de cobertura AU-R01 a AU-R30 — SPEC → Skill → prova

Cada requisito é definido na matriz da SPEC genérica §16. Esta tabela indica a seção operacional que o executa e a evidência mínima correspondente. Os números não concedem aprovação automática à implementação do validador; os testes de GVA-5 confirmarão a execução posterior.

| ID | Procedimento desta Skill | Prova a apresentar / limite |
|---|---|---|
| AU-R01 | §§1.1, 4.4 | Objeto não predeterminado; teste em domínio distinto |
| AU-R02 | §§1.1, 2.1, 3.AU-12 | Estágio real; futuros legítimos pendentes |
| AU-R03 | §§1.1, 2.1, 3.AU-12 | Cobertura final e aceites do domínio |
| AU-R04 | §§2.2–2.3, AU-00 | Identidade da fonte física; inventário |
| AU-R05 | §§1.3, 2.3 | Exclusões comprovadas sem inspeção indevida |
| AU-R06 | §§1.2, AU-01 | Matriz de autoridades e competências |
| AU-R07 | §§2.3, AU-00–AU-02 | Tipo/tamanho/CRC/SHA do objeto elegível |
| AU-R08 | AU-03 | Matriz requisito → fonte → evidência |
| AU-R09 | AU-04, §4.2 | Template/validador autorizado; estrutura e limites |
| AU-R10 | AU-05, §4.3 | Confronto semântico ou `NÃO VALIDADO` fundamentado |
| AU-R11 | AU-06 | Matriz de links e dependências |
| AU-R12 | AU-06 | Hash físico dos destinos correntes |
| AU-R13 | AU-07 | Ajuste sem histórico artificial de hash |
| AU-R14 | AU-07 | Versão anterior formal comprovada e preservada |
| AU-R15 | AU-06–AU-08 | Hash de aceite e evento humano separados do atual |
| AU-R16 | AU-08, AU-10 | Impactos de Gates/congelamento |
| AU-R17 | AU-09, §6.2 | Ocorrências classificadas sem falso positivo |
| AU-R18 | AU-10, §5.3 | Escopo e autorização antes de escrita |
| AU-R19 | AU-10–AU-11 | Diff mínimo e dependências atingidas |
| AU-R20 | AU-11 | Segunda auditoria dos bytes finais |
| AU-R21 | §6.3 | Parecer completo com limitações |
| AU-R22 | §§1.2, 6.3 | Fontes físicas, sem contexto de conversa |
| AU-R23 | AU-08 | Aceite humano efetivo e limitado por objeto |
| AU-R24 | §§1.2, 4.1–4.2 | Fonte canônica, sem norma concorrente |
| AU-R25 | §§6–7 | Matriz SPEC → Skill → testes; revalidar quando bytes, escopo ou dependências mudarem |
| AU-R26 | §§3, 6.3 | Todas as seções e provas, não resumo substitutivo |
| AU-R27 | §§1.3, 5.1–5.3 | Auditoria somente leitura; conferir identidade e disponibilidade física do script |
| AU-R28 | §§4.1, 4.4 | Aplicação apenas do contrato especializado vigente |
| AU-R29 | AU-11–AU-12, §5.3 | ZIP local somente quando autorizado e confronto posterior |
| AU-R30 | §§1.2–1.3, AU-11 | Preservações, comparação e regressão |

## 8. Condições bloqueantes para uso, revisão e aceite

A integração operacional da Skill no clone do responsável permanece **NÃO VALIDADA até confronto com uma base física atualizada**; o aceite dos Gates e a presença nesta cópia local não provam incorporação. Na revisão histórica do GVA-3 exigiu-se cumulativamente: (1) SPEC genérica e contrato de domínio GVA-1/GVA-2 íntegros; (2) instruções completas sem atalhos; (3) mesma classificação e semântica em SPEC/Skill/contratos; (4) nenhum script GVA-4 ou teste GVA-5 antecipado **naquele Gate**; (5) validação dos links relativos; (6) preservação do processo global e das competências de outras Skills; (7) tratamento explícito de versões/ajustes/aprovações; (8) matriz AU-R integral; (9) inspeção do diff e regressões; (10) segunda leitura dos bytes finais; e (11) escopo de edição estritamente autorizado. Para uso atual, conferir também a identidade física do executor e a execução da suíte conforme a autorização aplicável.

Se requisito obrigatório não tiver fonte/resultado/limite, ou se existir inconsistência entre SPEC e Skill, classificar o Gate `NÃO CONFORME` ou `BLOQUEADO` segundo a evidência e **não** apresentar um documento resumido como entrega integral. Conteúdo de um Gate anterior deve ser preservado; mudança desse conteúdo exige autorização separada.
