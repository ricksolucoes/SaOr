---
name: saor-analise-documental
description: Gera, atualiza, padroniza e audita os três registros Markdown de interfaces SaOr (Controle GI-0/GI-1, TextFrame GI-2 e Composição GI-3/GI-4), usando obrigatoriamente os templates completos e a validação estrutural; não redefine as SPECs nem aprova Gates.
---

# SaOr — Skill de geração, atualização e análise documental

## 1. Missão e alcance

**Esta Skill executa três operações distintas:** (a) **GERAR** documento de uma interface nova, utilizando o template integral do tipo correspondente; (b) **ATUALIZAR** documento existente, preenchendo as seções já previstas e preservando decisões e evidências; (c) **ANALISAR/MIGRAR** a estrutura de documentos anteriores, inclusive encerrados, mediante autorização específica para qualquer modificação. Também verifica a conformidade editorial dos arquivos produzidos ou examinados.

A Skill **não** desenha PNG, não aprova Gate, não cria requisito, não seleciona template visual vigente e não muda a sequência de produção das interfaces. O objeto são exclusivamente os três documentos Markdown determinados na SPEC 3; seus **templates são o formato fechado**. Para autoria e revisão, não basta aplicar nomes de seções: utilizar também todos os H3, os rótulos, as tabelas, as colunas e as linhas fixas de cada modelo.

A Skill mantém o nome e o diretório `.skill/saor-analise-documental/` referenciados pela SPEC 3, inclusive seus três arquivos `templates/*.md`.

## 2. Fontes, precedência e inspeção física

1. Trabalhar sobre cópia física autorizada; conferir integridade, caminhos e hashes necessários, sem usar memória ou respostas anteriores como prova. Em ZIP, verificar CRC/tamanho/SHA-256 dos membros elegíveis. Respeitar exclusão de `assets/` (não listar internamente nem abrir) e classificação normativa de LEGADOS.
2. **Ler primeiro, integralmente**, `.specs/PROCESSO-ALTERACAO-ASSISTIDA.md` e `.specs/README.md` da base real. Em seguida ler a ficha da interface em `docs/Documento_Mestre.md` e as fontes pertinentes: `.specs/wireframes/PROCESSO-TELA-PRANCHA.md` (SPEC 3), `.specs/wireframes/GATE-IMPLEMENTACAO-TELAS.md`, `.specs/wireframes/WIREFRAME-TEXT-TELA.md`, `.specs/wireframes/REGRAS-TECNICAS.md`, `.specs/wireframes/REFERENCIA-TEMPLATE-OFICIAL.md`, registros de vigência e contrato aplicável da referência oficial. Ler os documentos de origem/destino, suas decisões e dependências. Inspecionar efetivamente os PNGs relevantes quando a operação depender de conteúdo visual.
3. A autoridade **funcional** é o Documento Mestre, a dos **Gates** é a SPEC 3 com seu Gate auxiliar, e a das **invariantes técnicas** são os contratos existentes. A Skill padroniza **somente a documentação**. Divergência entre template editorial e norma: interromper a criação/atualização e submeter ajuste delimitado, sem inventar regra concorrente.
4. A fonte de trabalho é local. GitHub, quando necessário, somente leitura; nunca publicar ou transmitir os artefatos locais ao remoto.

**Antes de criar, substituir, editar ou empacotar:** reconstruir contexto; identificar alterações, arquivos preservados, impactos e validações; obter **autorização humana expressa e específica** segundo o processo global. Análise não autoriza escrita. Após a autorização, editar somente cópia local aprovada, manter a versão original para diff e entregar apenas arquivos autorizados.

**Auditoria complementar:** a [SPEC genérica de Auditoria](../../.specs/auditor/PROCESSO-AUDITORIA.md), seu [contrato especializado de wireframes](../../.specs/auditor/wireframes/CONTRATO-AUDITORIA-WIREFRAMES.md) e a [Skill operacional de Auditoria](../saor-auditoria/SKILL.md) controlam a verificação transversal sob demanda e após a conclusão do processo competente. Esta Skill permanece a única responsável por seus três modelos editoriais e seus validadores; a auditoria transversal não altera Gates, templates nem aceita artefatos automaticamente.

## 3. Seleção obrigatória de um modelo

| Documento efetivamente solicitado | Modelo editorial completo | Primeiro momento de criação permitido pela SPEC 3 |
|---|---|---|
| `docs/wireframes/images/<tema>/telas/controle/<nome-base>.md` | `templates/CONTROLE-GI0-GI1.md` | GI-0: inventário, antes do PNG/GI-1 |
| `docs/wireframes/images/<tema>/telas/wiframetext/<nome-base>.md` | `templates/TEXTFRAME-GI2.md` | **Somente depois** de GI-1 humano aprovado, com PNG real |
| `docs/wireframes/images/<tema>/telas/pranchas/01_Mobile_360x800/wiframetext/<nome-base>.md` | `templates/COMPOSICAO-GI3-GI4.md` | Após GI-2 aprovado e durante a montagem/registro de GI-3 |

Aplicar **uma cópia literal integral** do modelo correspondente. O documento final (ou rascunho autorizado) mantém os mesmos títulos H1/H2/H3, a mesma ordem, os mesmos esquemas de tabela, os rótulos e as linhas fixas. Não substituir o template por um exemplo M00.4, M00.5 ou de outra interface. Não acrescentar H2, H3, H4, tabela alternativa ou campo rotulado novo para acomodar um caso. Casos particulares entram **nas linhas e campos previstos**. A estrutura é igual em `white` e `black`; seus valores são verificados e independentes.

**Diretório e nomes** são os da SPEC 3; `<nome-base>` e resolução somente conforme a interface/página/versão realmente autorizada. Os três arquivos são independentes por tema/versão/página. A ausência ou corrupção de um modelo ou incompatibilidade normativa **bloqueia** a operação — nunca improvisar outro layout.

## 4. GERAÇÃO — procedimento operacional, passo a passo

1. **Identificar** ID, nome oficial, tema, versão, página/total, tipo de documento e situação real dos Gates; levantar fontes, estados, páginas, variantes, hashes e decisões já comprovadas. Identificar o que **ainda não existe**. Obter autorização para criar o(s) arquivo(s) determinado(s).
2. **Copiar integralmente** o `templates/<tipo>.md` correspondente como **rascunho local**, preservando todos os H2/H3, tabelas e campos. Opcionalmente usar `python3 scripts/preparar_documento.py --tipo <tipo> --destino <arquivo> --autorizado`, apenas após autorização; o script gera um **rascunho com placeholders**, não um documento aprovado.
3. **Preencher TODOS os `{{CAMPOS}}`** com informação física/documental, no H3 previsto. Cada célula tem conteúdo verificável e citação de fonte quando material. Copiar textos e decisões fielmente; nunca completar com hipótese, hash presumido, data inventada, elemento funcional de outra tela ou geometria aproximada. Linhas variáveis podem se repetir conforme o número real de elementos.
4. Para uma **etapa futura ainda não realizada**, manter a seção fixa e indicar expressamente `PENDENTE — ainda não executado; sem decisão humana`, ou o estado efetivo da SPEC, **sem simular resultados**. Não empregar `NÃO APLICÁVEL` para um Gate apenas pendente. Para requisito realmente inaplicável, registrar `NÃO APLICÁVEL — <fundamento/fonte>` no campo próprio. Para dado exigido porém desconhecido, `NÃO VALIDADO — <dado/fonte ausente>` e bloquear o avanço que dependa dele; não transformar isso em aprovação.
5. **Controle GI-0/GI-1:** preencher de fato §§1–6 com a ficha do Documento Mestre, matriz de requisitos, estados/fluxos, vigência e resultado do GI-0; §§7–8 somente recebem inspeção PNG real e aceite GI-1 após sua ocorrência; §9 vincula GI-2 sem pretender aprová-lo; §10 apresenta estados comprovados e cronologia (nunca um futuro como concluído).
6. **TextFrame GI-2:** antes de criar, conferir GI-1 e SHA dos PNGs. Documentar a leitura visual efetiva, a reprodução textual, medições, tokens com fontes, estado, rolagem e matriz de completude nas §§1–8. A §9 recebe decisão/hashes da aprovação GI-2 **somente quando concedida**. Não declarar hitbox, fonte tipográfica ou blur como mensuráveis no raster se exigem outra fonte.
7. **Composição GI-3/GI-4:** exigir GI-2, referência vigente e contrato. §§1–9 identificam artefatos, modelo, método real, medições da Prancha, cabeçalho, Item 10, Item 14 e resultado técnico; §10 registra submissão e decisão humana GI-4, **após** aprovação. Não atribuir GI-4 a uma verificação meramente técnica de GI-3.
8. **Validar** estrutura com `python3 scripts/validar_estrutura.py --tipo controle|textframe|composicao --arquivo <documento>`, abrir o arquivo, reler integralmente e confrontar conteúdo com as fontes. Enquanto houver placeholder, desvio estrutural ou lacuna impeditiva, o documento **não** pode ser apresentado como concluído/conforme. A validação formal não autentica fatos.
9. Só após evidência/decisão humana e permissões do processo global, registrar efetivamente novos estados nos locais fixos, conferir hashes atualizados e avaliar dependências. Na entrega de alterações autorizadas, preservar caminhos originais num único ZIP local e verificar o ZIP reaberto, seu diff e integridade.

## 5. ATUALIZAÇÃO — procedimento operacional, passo a passo

1. Ler arquivo **inteiro**, identificar versão física e SHA-256, cotejar com o template e verificar se seu estado é rascunho ou documento já aprovado/congelado. Levantar onde seu hash é referenciado por outros documentos; identificar Gate afetado pela mudança de bytes.
2. Para documento já conforme ao modelo: **editar somente o H3/linha/campo que recebe o novo fato** (ex.: decisão GI-1 em Controle §8; GI-2 no TextFrame §9; GI-4 na Composição §10) e atualizar a linha `Estado vigente` apenas com suporte em evidências. Manter H1/H2/H3, rótulos e colunas. Inserir novo evento como linha de histórico no H3 existente, nunca como `§11`, `§10.1` arbitrário ou apêndice ao fim.
3. Distinguir **estado atual** de **evento de aprovação comprovado**. O hash da submissão/aceite identifica os bytes objeto da decisão, quando exigido pela norma; o hash físico atual identifica o arquivo após eventuais registros ou correções. **Ajustes autorizados dentro da mesma versão formal não criam nova versão nem histórico de hashes intermediários descartados.** Preservar a prova de aprovação e a versão formal anterior somente quando existirem e forem exigidas; não atribuir aos novos bytes um aceite que não os abrange. Se a mudança afetar artefato congelado, verificar a necessidade de revalidação conforme a SPEC 3. Evitar autorreferência e ciclos de hash sem solução contratual.
4. **Se o documento antigo não seguir o modelo**, primeiro executar análise/mapeamento de migração (§6); não fazer reorganização incidental numa atualização de Gate. Migrar somente com autorização específica e avaliar hashes dos documentos dependentes.
5. Revisar referências entre Controle ↔ TextFrame ↔ Composição e entre temas. Uma referência de aprovação, origem comprovada ou versão formal anterior mantém sua finalidade e decisão associada; uma referência denominada **atual** deve corresponder aos bytes atuais. Hash de mero ajuste substituído dentro da mesma versão não será acumulado como histórico. Não tentar «corrigir» ciclos de hash com valores inventados.
6. Aplicar validação formal, semântica e de diff; conferir que nenhuma alteração não autorizada entrou na cópia final. Se surgirem necessidades fora do escopo, parar e submetê-las.

## 6. ANALISAR E MIGRAR documentos existentes/encerrados

1. Em pedido de **análise**, executar leitura e confronto sem modificar arquivos. Usar `references/FORMATO-RELATORIO.md` para apresentar inventário de documentos examinados (caminho/tamanho/SHA-256), todos os H2/H3 e campos divergentes, conteúdo que deve ser realocado, fatos/decisões/hashes, classificação e risco de regressão.
2. Distinguir `DESVIO EDITORIAL` de `ERRO COMPROVADO`, `DOCUMENTAÇÃO DESATUALIZADA`, `LEGADO VÁLIDO`, `DECISÃO HISTÓRICA`, `INCONSISTÊNCIA ENTRE FONTES`, `REFERÊNCIA QUEBRADA`, `DIFERENÇA INTENCIONAL`, `LACUNA DOCUMENTAL` e `SEM NECESSIDADE DE ALTERAÇÃO`. Um documento fechado pode ser editorialmente diferente sem que seu Gate seja automaticamente inválido.
3. Identificar para **cada bloco de conteúdo** a célula/linha/H3 de destino no template. Não apagar uma decisão, exceção, restrição, evidência ou hash para caber em estrutura mais curta. Duplicações factuais podem ser consolidadas sem apagar o evento que lhes dá validade. Se faltar campo no template para um conteúdo obrigatório, **não criar novo tópico**: demonstrar a incompatibilidade e solicitar aprovação de revisão do próprio modelo.
4. Antes de **migração**, submeter escopo exato, documentos a alterar e preservar, plano de mudança de hashes/referências e efeitos nos Gates para autorização. Após autorização, produzir documentos reestruturados a partir do template, com todos os eventos originais reacomodados e auditados; não alterar PNGs/Pranchas/Documento Mestre/SPECs por consequência automática.
5. Revalidar a cadeia de decisões; alteração de bytes em documento congelado exige avaliação segundo a norma e eventual decisão humana específica, não «herança» de aceite. Reabrir/atualizar somente o Gate realmente impactado se exigido. Entregar ZIP local só com arquivos aprovados para modificação.

## 7. Contrato de preenchimento e checagem (obrigatório)

- Ler `references/CONTRATO-EDITORIAL.md` para o significado preciso dos campos e a política de células/linhas em cada tipo; `references/PADRAO-DOCUMENTAL.md` é **índice**, não um modelo substituto.
- O `validador` verifica **H1/H2/H3, H4 proibido, abertura, tabelas/cabeçalhos, rótulos, linhas fixas, conteúdo mínimo de tabelas e ausência de placeholders**. Execute `--templates` para conferir a integridade formal dos modelos, e `--tipo ... --arquivo ...` para o documento gerado/alterado. A análise visual, normativa, factual, de Gates, estado/cronologia e hashes permanece obrigatória e **não é substituída** por resultado `CONFORME ESTRUTURAL`.
- Não criar campo livre intitulado `Notas`, `Adendo`, `Outras decisões`, `Histórico adicional` ou equivalente fora das estruturas já existentes. Texto livre somente no espaço claramente reservado pelo template, com fontes quando material. Não copiar textos de um exemplo de interface para outro.
- Nenhum relatório operacional, comentário sobre a conversa, trajetória de um assistente ou embalagem ZIP deve ser inserido como autoridade permanente num documento de interface. Uma referência histórica verdadeira e necessária não é apagada por preferência de estilo.
- Se a versão da SPEC 3 na base efetiva não contiver o vínculo aos templates, relatar essa dependência documental; **não editar a SPEC por iniciativa da Skill**. Não presumir que a versão modificada tenha sido incorporada sem verificação física.

## 8. Produtos esperados por modo

| Modo solicitado | Resultado | O que é proibido inferir |
|---|---|---|
| GERAR | Documento Markdown no **template literal completo**, preenchido segundo os Gates alcançados, validado e entregue somente após autorização | Gate futuro aprovado; valor de PNG não existente; hash calculado sem arquivo |
| ATUALIZAR | Alteração **local e delimitada** nos H3 existentes, com registro de decisões e impacto de hashes, diff e validação | Que edição editorial preserva hash ou aprovação de versão diferente |
| ANALISAR | Inventário e parecer estruturais/factuais com mapeamento H3, sem escrita | Que um desvio editorial revoga Gate anterior |
| MIGRAR | Documentos antigos reorganizados nos três modelos, após autorização de escopo e análise de impactos | Que padronização dá novo aceite humano |

**Gate de entrega da Skill:** se a conformidade do template e a aderência normativa não puderem ser comprovadas, declarar `NÃO VALIDADO` e não concluir criação/atualização/migração como aprovada.
