# SaOr — Formato integral do parecer de auditoria

## 1. Finalidade e regra de preenchimento

Este formato é o **contrato de apresentação** dos resultados produzidos pela [Skill de Auditoria](../SKILL.md), conforme [SPEC genérica](../../../.specs/auditor/PROCESSO-AUDITORIA.md), §13, e [Contrato Operacional](CONTRATO-OPERACIONAL.md). Aplica-se a qualquer domínio e a ambos os modos `SOB_DEMANDA` e `ENCERRAMENTO`; **não** é um template alternativo para Controle, TextFrame ou Composição da SPEC 3. Não acrescenta Gate ou requisito ao objeto auditado.

Emitir o parecer na conversa ou no meio autorizado. Não criar Markdown, arquivo de relatório, manifesto ou inventário persistente automaticamente. Quando a materialização for expressamente autorizada, conservar a mesma cobertura, conteúdo e evidências sem truncamentos. Títulos abaixo são a **estrutura do parecer de auditoria**, não campos de documentos funcionais. Cada seção deve ser efetivamente preenchida com o número real de entradas; ausência de objeto ou prova deve aparecer como `NÃO APLICÁVEL` ou `NÃO VALIDADO` fundamentado. Não deixar marcadores de preenchimento nem colunas fictícias numa entrega declarada concluída.

O relatório deve permitir a um auditor independente reproduzir todas as conclusões materiais com o clone e suas normas. Uma síntese executiva opcional **nunca substitui** as matrizes completas e os testes exigidos.

Em todas as tabelas usar **exclusivamente** os estados auditoriais da SPEC genérica: `CONFORME` (exigência comprovadamente atendida), `NÃO CONFORME` (violação demonstrada), `NÃO VALIDADO` (evidência insuficiente), `PENDENTE` (exigência legitimamente futura), `NÃO APLICÁVEL` (critério excluído por fundamento normativo) e `BLOQUEADO` (operação específica impedida, com causa e liberação). São diferentes dos estados do objeto e do Gate oficial. Uma linha não comprovada não recebe `CONFORME` por ausência de erro conhecido. O modo `SOB_DEMANDA` não penaliza Gates futuros; `ENCERRAMENTO` exige todas as obrigações finais aplicáveis comprovadas.

## 2. A. FATOS VERIFICADOS — identificação, escopo e limites

Registrar: identificador do parecer na conversa, data de execução comprovada, fonte local física, formato/caminho, tamanho, SHA-256 da base quando aplicável, modo, objeto, domínio, estágio documentado, versão formal/seleção vigente quando houver, autoria da decisão humana quando comprovada, autorização de leitura, exclusões e limitações de ferramenta.

| Campo | Conteúdo verificável necessário |
|---|---|
| Fonte e identidade | Container/caminho físico, bytes e SHA-256 realmente calculados |
| Modo e objeto | `SOB_DEMANDA`/`ENCERRAMENTO`, fronteira e motivação normativa |
| Estágio | Gate e decisão documental exatos, ou `NÃO VALIDADO` com motivo |
| Limites de acesso | Exclusões/LEGADOS normativos e operações não realizadas |
| Escopo expandido | Dependências justificadas, sem autorização automática de edição |
| Cópia comparativa | Caminho, hash/inventário, escopo e condição de reuso, ou ausência |

**Inventário dos arquivos efetivamente examinados:**

| Caminho relativo | Função e contrato | Tipo identificado | Tamanho (bytes) | SHA-256 | Método de leitura/inspeção efetivo | Limitação/estado |
|---|---|---|---:|---|---|---|

Repetir por arquivo elegível realmente lido; se a lista for extensa, não substituir por simples total sem inventário acessível no meio autorizado. Distinguir arquivos cujos bytes foram lidos, documentos semanticamente interpretados e imagens efetivamente inspecionadas. Não alegar que arquivo excluído foi aberto. Se um inventário físico for reutilizado, apresentar sua base, confrontos e limitações verificáveis, sem narrar releitura não feita.

## 3. B. AUTORIDADES E CRITÉRIOS EXIGÍVEIS

Confrontar as normas em ordem e registrar em tabela separada sua competência e hash/versão física quando pertinente:

| Fonte canônica | Caminho/trecho | Objeto ou competência | Obrigação verificável | Estágio de exigibilidade | Evidência de leitura | Limite |
|---|---|---|---|---|---|---|

Se houver divergência, registrar ambas as fontes com cláusulas, objeto, autoridade, cronologia e causa investigada; não decidir por preferência. Diferenciar autoridade material, SPEC de procedimento, contrato especializado, Skill e validador. Uma referência do README não substitui a decisão da fonte competente.

**Matriz completa de rastreabilidade:**

| ID requisito | Texto/fonte e localização | Objeto/condição | Exigível agora? | Evidência/arquivo | Método/teste | Resultado e alcance | Estado |
|---|---|---|---|---|---|---|---|

A matriz deve abranger **cada requisito aplicável**, mesmo quando não foi possível validá-lo. Não marcar `NÃO APLICÁVEL` por dificuldade de obter prova. Diferenciar exigibilidade futura legítima (`PENDENTE`) de uma obrigação atual sem fonte (`NÃO VALIDADO`).

## 4. C. CONTROLES AU-00 a AU-12 — execução e prova

Para cada controle aplicável, registrar entrada, método, fontes, execução real, saída, interpretação, resultado e limite. A matriz seguinte não substitui matrizes específicas do domínio:

| AU | Objeto/fonte | Entrada e método | Teste/resultado bruto | Evidência física | Classificação do alcance | Estado | Próxima ação |
|---|---|---|---|---|---|---|---|
| AU-00 | Identidade, estágio e modo | Conferência do container/objeto | Hash, tamanho e fronteira | Fonte física | Prova de acesso/integridade delimitada | Estado comprovado | Prosseguir ou limitar |
| AU-01 | Hierarquia normativa | Leitura contextual das fontes | Fontes selecionadas | Trechos/hashes | Competência identificada | Estado comprovado | Definir critério |
| AU-02 | Inventário | Confronto exigível×existente | Itens presentes/ausentes | Caminhos/tipos | Inventário, sem aceite implícito | Estado comprovado | Buscar dependentes |
| AU-03 | Rastreabilidade | Matriz por requisito | Obrigações cobertas | Fonte+evidência | Sem inferência funcional | Estado comprovado | Identificar lacunas |
| AU-04 | Estrutura | Validador real/inspeção | Saída e retorno | Modelo/script/arquivo | Estrutura, não semântica | Estado comprovado | Confrontar conteúdo |
| AU-05 | Semântica | Leitura/inspeção visual real | Requisito vs. encontrado | Trechos/imagens/medidas | Limites do método | Estado comprovado | Classificar ocorrência |
| AU-06 | Referências/hash | Resolução e classificação | SHA atual, links/ciclos | Grafo/linhas/hash | Diferenciar evento e atual | Estado comprovado | Investigar diferença |
| AU-07 | Versões | Registros e cronologia | Versão formal/ajuste/aceite | Decisões e objetos | Sem criar histórico artificial | Estado comprovado | Avaliar impacto |
| AU-08 | Gates | Ordem, decisão, aceites | Estado por objeto | Texto, datas e hashes | Não aprova automaticamente | Estado comprovado | Autorizar só se exigido |
| AU-09 | Ocorrências | Investigação e classificação | Causa, risco, hipótese | Fontes e provas | Não inventar erro | Estado comprovado | Proposta necessária |
| AU-10 | Correções | Escopo, autorização e testes | Ações autorizáveis | Diff planejado | Nenhuma escrita presumida | Estado comprovado | Solicitar decisão |
| AU-11 | Segunda auditoria | Diff e testes dos bytes finais | Regresso/novos hashes | Cópia final e baseline | Apenas se houve correção | Estado comprovado | Resolver ou bloquear |
| AU-12 | Parecer/fechamento | Cobertura e decisões | Estado final do modo | Matrizes e aceites | Parecer distinto do aceite | Estado comprovado | Próximo Gate |

As linhas acima exemplificam **o tipo de conteúdo a registrar**, não constituem resultados preenchidos e **não podem ser copiadas como resultados de uma auditoria real**. Na execução, substituir por métodos e dados efetivos, com tantas linhas por item quanto necessário, e remover dados demonstrativos.

## 5. D. INTEGRIDADE, FORMATO E SEMÂNTICA

Apresentar resultados por objeto e teste; pelo menos: integridade de contêiner e membros elegíveis, leitura/decodificação, estrutura do formato exigido, validação editorial quando aplicável, confronto de conteúdo com fonte canônica, inspeção visual quando a norma exigir e limitações da ferramenta.

| Verificação | Objeto e caminho | Norma/contrato | Método e ferramenta real | Esperado | Encontrado | Evidência/medida | Estado |
|---|---|---|---|---|---|---|---|

Para imagem, registrar dimensão/recorte, método, pixels comparados/diferenças quando aplicáveis e qual propriedade **não** foi comprovada. Para Markdown, conferir estrutura completa do template, mas também atos, requisitos e conteúdo. Para arquivos não visuais, não exigir comparação de pixels; usar somente testes adequados ao domínio. Não declarar cobertura funcional com base em um parser de títulos.

## 6. E. REFERÊNCIAS, HASHES, VERSÕES E DEPENDÊNCIAS

**Inventário de referências:**

| Origem e linha/campo | Destino/versão | Papel da referência | Categoria do SHA | Hash citado | Hash físico verificado | Decisão/evento aplicável | Resultado/ação |
|---|---|---|---|---|---|---|---|

Classificar obrigatoriamente os SHA na nomenclatura da SPEC genérica: `HASH_FISICO_ATUAL`, `HASH_SUBMISSAO_OU_APROVACAO`, `HASH_VERSAO_FORMAL_ANTERIOR`, `HASH_AJUSTE_SUBSTITUIDO`, `HASH_DE_ORIGEM_DOCUMENTADA`, `HASH_SEM_CLASSIFICACAO`. Não apresentar todo SHA diferente como erro ou como nova versão. Se faltar snapshot físico de uma submissão, documentar que a prova do evento pode estar registrada, mas a comparação física da versão submetida é `NÃO VALIDADA`.

**Versionamento e histórico de decisões:** registrar separadamente: (a) versão formal vigente, se comprovada; (b) arquivo físico atual; (c) atos de aprovação, com objeto/hashes/data; (d) versões formais anteriores que a norma manda preservar; (e) referências correntes obsoletas que exigem correção autorizada. Ajustes dentro da mesma versão **não** geram versões históricas ou inventários de hashes transitórios. A evidência de Gate permanece evidência, **não** versão formal.

**Dependências e riscos:** representar as relações por direção e finalidade; identificar referências circulares/autorreferências, arquivos a preservar, dependentes impactados e impossibilidades técnicas de estabilização. Não tentar atualizar hashes cíclicos sem mecanismo documental aprovado.

## 7. F. GATES, APROVAÇÕES E CONGELAMENTO

Para cada Gate efetivamente aplicável e para cada unidade exigida, apresentar:

| Processo/Gate | Objeto, versão e unidade | Pré-condições | Prova física | Decisão humana (teor/data/abrangência) | Estado oficial | Estado da verificação | Risco de regressão |
|---|---|---|---|---|---|---|---|

Distinguir aprovações individuais de conjunto quando exigidas; um Gate técnico não substitui aceite humano. `APROVADO`, `CONGELADO`, `VIGENTE`, `CONCLUÍDO` e `CONFORME` não são equivalentes. Evento posterior não deve ser retrodatado. Não marcar Gate futuro como falha se o modo for `SOB_DEMANDA` e o processo ainda estiver em etapa anterior válida.

## 8. G. OCORRÊNCIAS — investigação completa, não apenas apontamentos

Registrar cada ocorrência com todos os campos: identificador; arquivo/caminho; seção, linha, imagem ou medida; regra/fonte; comportamento esperado; comportamento evidenciado; divergência comprovada; causa investigada; hipóteses remanescentes; classificação exata do processo global; estado auditorial; impacto funcional/editorial/material; dependentes; risco de regressão; necessidade real; alternativa e proposta; alteração permitida; autorização requerida; validação posterior.

| Ocorrência | Classificação | Fonte e evidência | Causa/limite | Impacto e dependências | Necessidade de alteração | Solução/decisão | Estado |
|---|---|---|---|---|---|---|---|

Ocorrência intencional, história válida e caso sem necessidade de alteração **não** devem ser transformados em correção por uniformização. Melhorias opcionais devem aparecer separadas dos impedimentos e das correções obrigatórias. Uma classificação não deve apagar o estado de verificação; os dois campos têm funções diferentes.

## 9. H. AUTORIZAÇÕES, INTERVENÇÕES E PRESERVAÇÕES

Para toda escrita sugerida, detalhar:

| Arquivo exato | Fonte da necessidade | Alteração proposta e limite | Autorizações existentes | Dependências/Gates | Preservações | Testes planejados | Estado |
|---|---|---|---|---|---|---|---|

A autorização deve ser expressa e específica por operação/escopo. Em auditoria somente leitura, indicar claramente `NENHUM ARQUIVO MODIFICADO`; não presumir autorização porque o usuário forneceu ZIP ou aceitou arquitetura. Se arquivos aprovados ou congelados dependem da mudança, avaliar reabertura do Gate pela fonte material antes de alterar. Não criar artefatos de correção na expectativa de autorização posterior.

## 10. I. SEGUNDA AUDITORIA E REGRESSÕES — somente se houve correção

Identificar a baseline preservada, o lote autorizado, os arquivos efetivamente criados/modificados/excluídos, os preservados e seus hashes. Comparar diff completo antes/depois e conferir que todas as alterações pertencem ao escopo. Verificar cada dependência material, repetir testes afetados e procurar novos problemas, não apenas a ausência do erro inicial. Mostrar resultados brutos e critérios de sucesso/falha.

| Arquivo/teste | Original SHA-256 | Novo SHA-256 | Diferença autorizada | Teste repetido | Resultado e alcance | Regressão/limite |
|---|---|---|---|---|---|---|

Se não houve alteração, registrar `NÃO APLICÁVEL — esta auditoria foi somente leitura`, **sem simular execução de uma segunda auditoria pós-edição**. Se o problema exigir escrita fora do lote autorizado, registrar operação bloqueada e solicitar aprovação específica.

## 11. J. RESULTADO GLOBAL, LIMITAÇÕES E PRÓXIMO PASSO

O fechamento do parecer deve conter: modo, critérios exigíveis atendidos e pendentes, resultados `NÃO VALIDADOS` e seus impactos, ocorrências materiais remanescentes, decisões humanas necessárias, condições de avanço e **somente a próxima ação realmente permitida**. Declarar `CONFORME PARA ENCERRAMENTO` exclusivamente se todo requisito final aplicável estiver comprovado e houver decisões exigidas. `CONFORME` técnico da auditoria **não** concede aceite humano nem comprova incorporação física da entrega.

### 11.1. Condições mínimas para concluir o relatório

- A identidade da fonte e os limites de leitura estão explicitados.
- Todas as normas e versões materiais aplicáveis foram identificadas e lidas.
- O inventário dos objetos exigíveis está completo, incluindo arquivos realmente inspecionados.
- Todas as exigências possuem linha de rastreabilidade, evidência e estado.
- Verificações de integridade, semântica, referências e decisões foram executadas ou têm limites `NÃO VALIDADOS` fundamentados.
- As ocorrências têm causa, impacto, classificação e tratamento proposto ou justificativa para preservação.
- Mudanças autorizadas foram submetidas à segunda auditoria, sem alegações falsas de execução.
- Estados de Gates e decisões humanas não foram inferidos de testes ou títulos.
- A próxima operação e a autorização necessária estão explícitas; nenhuma ação fora do escopo foi efetuada.

### 11.2. Entrega e incorporação, quando aplicáveis

Somente com autorização de empacotar: registrar o ZIP local contendo apenas mudanças autorizadas, sua integridade, hashes, caminhos e aplicação limpa na cópia da baseline. Não declarar incorporação apenas pela entrega. Depois de receber novo clone, registrar os hashes confrontados e o aceite humano correspondente; se o clone não foi fornecido, a incorporação permanece `NÃO VALIDADA`.

## 12. Reprodutibilidade e proibições finais

O parecer deve ser independente do histórico de conversa, suficiente para que outro profissional com o clone e as normas localize as fontes, execute as verificações e compreenda as limitações. Não usar exemplos de interface como autoridade para outros objetos. Não entregar versão resumida da auditoria no lugar das matrizes e resultados exigidos. Não incluir tabelas demonstrativas como se contivessem resultados reais. Não transmitir arquivos ao GitHub, nem tratar uma ferramenta futura como instalada. Não converter hashes substituídos durante ajuste da mesma versão em histórico de revisões; preservar evidências de submissão e versões formais anteriores quando a norma exigir.
