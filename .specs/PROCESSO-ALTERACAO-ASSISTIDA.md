# SaOr — Processo de alteração assistida

## 1. Escopo

Este documento define o processo obrigatório para qualquer análise, criação, correção, substituição ou empacotamento de arquivos do projeto realizada com apoio de IA ou assistência automatizada.

O objetivo é impedir alterações reativas, inferências por memória, decisões baseadas em títulos/comentários e mudanças sem verificação contextual do projeto real.

Este processo é global. Ele se aplica antes das specs específicas de wireframe, identidade visual, documentação funcional ou qualquer outra área do repositório.

---

## 2. Princípio central

Antes de procurar o que alterar, a assistência deve compreender o projeto pelos artefatos reais.

É proibido alterar arquivos a partir do primeiro sintoma encontrado sem reconstruir o contexto, verificar dependências e comprovar a necessidade da mudança.

Neste projeto, esse comportamento é tratado como **vibe coding documental/técnico** e não é permitido.

---

## 3. Fonte de trabalho

1. Quando o responsável fornecer uma cópia física local do projeto, ela passa a ser a fonte de trabalho da análise.
2. Não substituir essa cópia por memória de conversa, resultados de conectores, mensagens de commit, nomes de arquivo ou descrições externas.
3. GitHub permanece somente leitura para esta assistência. Nenhuma alteração deve ser feita diretamente no repositório remoto.
4. Quando for necessário comparar remoto e local, a comparação deve ocorrer antes da alteração.
5. Não baixar repetidamente uma versão já validada sem mudança detectada, salvo quando o responsável determinar explicitamente novo download.
6. Se o responsável excluir explicitamente uma categoria do escopo — por exemplo, vídeos — a exclusão deve ser respeitada e registrada, sem ser tratada como falha de rigor.

---

## 4. Leitura contextual obrigatória

Antes de propor mudança:

- inspecionar a árvore real do projeto;
- em auditorias globais ou de continuidade estrutural do SaOr, percorrer **todo o projeto físico**, arquivo por arquivo, antes de concluir o contexto;
- ler integralmente todos os arquivos textuais do projeto que não tenham sido explicitamente excluídos do escopo;
- ler integralmente `docs/` e suas subpastas em auditorias globais/documentais;
- ler as specs e demais dependências apontadas pela documentação;
- inspecionar visualmente imagens relevantes;
- verificar SVGs, pacotes, fontes e demais binários quando não estiverem explicitamente excluídos; para binários, validar os bytes, tipo, tamanho e hash e inspecionar seu conteúdo com ferramenta adequada quando houver conteúdo interpretável;
- verificar caminhos, referências cruzadas e artefatos físicos citados;
- confrontar documentação, código, configuração e ativos quando coexistirem.

Não é permitido concluir conteúdo apenas por:

- nome de arquivo;
- título;
- comentário;
- pasta;
- mensagem de commit;
- histórico de conversa;
- aparência aproximada;
- suposição de que um arquivo citado existe ou contém determinado conteúdo.

Toda afirmação material deve ser sustentada pelo conteúdo efetivamente inspecionado no arquivo, código, configuração, imagem ou ativo correspondente.

Quando um arquivo não puder ser inspecionado, a limitação deve ser declarada. Não afirmar como fato o conteúdo não verificado.

---

## 5. Classificação antes da alteração

Toda ocorrência encontrada deve ser classificada antes de qualquer edição, por exemplo:

```text
ERRO COMPROVADO
DOCUMENTAÇÃO DESATUALIZADA
LEGADO VÁLIDO
DECISÃO HISTÓRICA
INCONSISTÊNCIA ENTRE FONTES
REFERÊNCIA QUEBRADA
DIFERENÇA INTENCIONAL
LACUNA DOCUMENTAL
SEM NECESSIDADE DE ALTERAÇÃO
```

A classificação deve respeitar a autoridade documental da área correspondente.

Não atualizar um artefato histórico apenas para fazê-lo parecer contemporâneo.

---

## 6. Gate obrigatório antes de criar ou modificar arquivo

Antes de criar, modificar, substituir, excluir ou empacotar qualquer arquivo, a assistência deve apresentar ao responsável:

- contexto reconstruído;
- problema comprovado;
- arquivos que pretende alterar;
- mudança prevista em cada arquivo;
- arquivos analisados que deliberadamente não serão alterados;
- riscos ou efeitos esperados.

A execução só pode começar após **aprovação explícita do responsável**.

Silêncio não constitui aprovação.

Uma autorização cobre somente o escopo apresentado. Mudança adicional exige nova autorização.

---

## 7. Execução local

Depois da aprovação:

1. trabalhar somente na cópia local autorizada;
2. preservar uma base original para comparação;
3. alterar apenas os arquivos aprovados;
4. não modificar arquivos remotos;
5. não introduzir requisito novo por conveniência;
6. não resolver contradição criando uma terceira regra sem autoridade documental;
7. preservar caminhos, nomes e ativos que não pertençam ao escopo;
8. manter histórico válido quando ele for necessário para compreender o projeto.

---

## 8. Auditoria pós-alteração

Antes da entrega, verificar:

```text
[ ] somente arquivos autorizados foram alterados
[ ] nenhum arquivo autorizado foi omitido
[ ] referências e caminhos continuam válidos
[ ] estados e vocabulários permanecem coerentes com suas specs
[ ] não foi criada duplicidade normativa
[ ] não houve regressão em conteúdo fora do escopo
[ ] arquivos gerados abrem e possuem o formato esperado
[ ] diferenças contra a base original são explicáveis e intencionais
```

Se a alteração revelar nova necessidade fora do escopo aprovado, não incorporá-la silenciosamente. Registrar para decisão posterior.

---

## 9. Entrega

Quando a entrega envolver arquivos para substituição no projeto:

- entregar um único ZIP;
- preservar os caminhos relativos à raiz do repositório;
- incluir somente os arquivos que precisam ser criados ou substituídos;
- não incluir arquivos temporários, relatórios internos ou cópias desnecessárias, salvo se forem parte explícita do escopo aprovado;
- validar a estrutura interna do ZIP antes da entrega.

A geração do ZIP não significa aceitação final da solução.

O responsável pelo projeto implementa/testa os arquivos no ambiente real e decide depois se a solução deve ser aceita, ajustada, continuada ou descartada.

---

## 10. Resultado esperado

Uma alteração assistida deve ser:

```text
contextualizada
+
comprovada pelos artefatos reais
+
restrita ao escopo aprovado
+
reproduzível sem memória de conversa
+
validada antes da entrega
+
reversível pela preservação da base original
```
