# SaOr — Contrato editorial dos três modelos (orientação da Skill)

Documento de **orientação de preenchimento**, não uma SPEC. As regras funcionais, técnicas, Gates e aprovações são definidos exclusivamente pelas fontes normativas existentes. Em conflito, não produzir um terceiro padrão: registrar a incompatibilidade para decisão.

## 1. Estrutura obrigatória — sem decisões de estilo por executor

- O arquivo começa com um único H1 e a linha `Estado vigente (...)`, no formato **literal** do template selecionado.
- Todos os H2 e H3 devem existir, **na sequência original**. Seção não usada ainda **continua existindo**. Nunca acrescentar H2, H3, H4 nem seção final denominada `Adendo`, `Notas`, `Análise`, `Regularização` ou similar.
- Cada H3 conserva os **rótulos, cabeçalhos de tabela, sequência de colunas e linhas fixas** do modelo. Não mudar `Tema` para `Variação`, `Evidência` para `Justificativa` ou nomes de colunas por preferência pessoal.
- Em tabelas repetíveis, incluir uma linha por ocorrência efetiva, sem criar tabelas novas. Textos de múltiplas linhas ficam em descrição/parágrafo do H3 correspondente, ou em células Markdown tecnicamente válidas; não transformar transcrição em subtítulo.
- Usar campos prefixados `**Nome do campo:**` somente quando existem no template, em seus H3 correspondentes. São proibidos rótulos extras inventados, mesmo em negrito, para novas decisões.
- **Mesmo esqueleto** para `white` e `black`. Pode haver valores distintos conforme a fonte visual e seu contrato; equivalência funcional não significa identidade de cores/estilos.

## 2. Preenchimento de um documento novo em estágio parcial

Os templates abrangem **todo o ciclo documental**, mas não autorizam executar etapas futuras.

| Situação verificável | Como registrar no campo existente | O que evitar |
|---|---|---|
| Etapa ainda não iniciada | `PENDENTE — ainda não executada; sem decisão humana` (ou estado normativo efetivo) | Declarar `APROVADO` por existir o tópico |
| Aguardando aceite humano real | `AGUARDANDO APROVAÇÃO — <objeto/caminho/hash de submissão verificado>` | Inventar data, aprovador, abrangência ou hash |
| Informação indispensável sem evidência | `NÃO VALIDADO — <qual evidência falta>` e indicar bloqueio do Gate dependente | Tratar lacuna como `NÃO APLICÁVEL` |
| Requisito/estado realmente fora do escopo | `NÃO APLICÁVEL — <fonte/justificativa>` | Deixar célula vazia ou apagar H3 |
| Item repetível sem ocorrências | Linha de ausência fundamentada na tabela do H3, sem simular objeto aprovado | Criar valor fictício para preencher colunas |
| Controle técnico concluído, sem aceite humano | `CONFORME TECNICAMENTE` somente quando respaldado pela fonte do respectivo Gate | Transmutar conformidade em decisão humana |

Não deixar `{{PLACEHOLDERS}}` no documento apresentado como concluído. Durante edição local, placeholders podem existir **apenas como rascunho**, até o preenchimento e validação. Não são dados normativos nem evidências.

## 3. Destino fixo de informações e decisões

| Informação | Controle GI-0/GI-1 | TextFrame GI-2 | Composição GI-3/GI-4 |
|---|---|---|---|
| Identidade, tema, página, versão, baseline | §1 | §1 | §1 |
| Requisitos e relações funcionais | §§2–3 | §§5–6 | Referências em §§3/8, sem duplicar a baseline |
| Seleção e fonte visual/contratual | §4 | §1 e §4 conforme evidência | §2 |
| Exceções e decisões funcionais específicas | §5 | §5 (como referência) | §§6–8 (somente reflexos verificáveis) |
| Evidência técnica GI-0 | §6 | Referência de origem §1 | Referência §3 |
| PNG, inspeção e decisão GI-1 | §§7–8 | PNG aprovado como entrada §1 | Referência §3 |
| Representação textual, geometria e completude | Referência GI-2 em §9 | §§2–8 | Referência §3 e amostras §7 |
| Decisão GI-2, hash do TextFrame | §9 como vínculo com documento próprio | §9, responsável pela decisão textual | Referência §3 |
| Método, comparação técnica GI-3, preservações | Apenas status referenciado §10 | Não se aprova Prancha neste documento | §§4–9 |
| Aprovação/ratificação GI-4 e hashes finais | Status referido §10, não autoridade substituta | Não se aprova Prancha neste documento | §10 |
| Linha do tempo e eventos posteriores | §10 | §9 | §10 |

**Quando a decisão envolver White, Black e conjunto:** transcrever somente a abrangência efetivamente concedida; registrar hashes separados por tema. Uma decisão isolada não aprova automaticamente o outro tema, uma página adicional ou uma versão nova.

## 4. Transcrições, referências e integridade temporal

- `Estado vigente` no topo: **fotografia comprovada do estado atual** do objeto. Eventos anteriores ficam no H3 de Gate/histórico correspondente. Um texto `AGUARDANDO APROVAÇÃO` anterior não deve ser tratado como estado atual após aceite comprovado.
- Para cada decisão: registrar **objeto**, **Gate**, **data comprovada**, **teor fiel**, **abrangência** e **hash/versão da submissão** quando aplicáveis. A fonte persistente é o próprio registro com a transcrição auditável; a história em conversa, isoladamente, não substitui a formalização requerida.
- Hash histórico ≠ hash do arquivo atual. Se houver alteração posterior de STATUS, adendo ou reestruturação, preservar as identidades distintas e a decisão que abrange cada uma; não usar um SHA antigo rotulado como atual.
- **Evitar autoreferência de hash:** inserir o SHA atual do próprio Markdown dentro de seus bytes mudaria o SHA. O campo do modelo destinado a versão aprovada deve referenciar expressamente o snapshot da decisão e/ou registro externo, nunca pretender representar o próprio arquivo pós-edição com valor impossível de estabilizar.
- **Evitar ciclos entre documentos:** TextFrame pode referenciar a versão do Controle usada em GI-1; se o Controle for atualizado depois, esse hash é **histórico de origem**, não alegar que é o hash atual. O Controle pode referenciar uma versão textual posterior, preservando a ordem das decisões.
- Nomes, datas, condições, versões e coordenadas só vêm de evidências físicas ou humanas conferidas. Referenciar fontes por caminho relativo e seção/trecho; SHA-256 integral quando exigido pelo Gate/contrato. Uma informação histórica comprovada pode mencionar sua procedência quando relevante; não inserir o nome do ZIP de transporte como substituto da identidade de um artefato do repositório.

## 5. Geometria e alcance de prova

- `[x,y,w,h]` descreve a região realmente medida e seu referencial; indicar método e unidade; não inventar cotas para parecer preencher um formulário.
- Raster não comprova sozinho hitbox, família/peso de fonte, valores lógicos de padding ou parâmetros não recuperáveis. Registrar limitações; usar fonte técnica independente apenas quando realmente existente.
- O Item 10 relaciona **componentes usados na interface**, não exemplos ilustrativos do template; uma cota de recorte não é automaticamente área de toque.
- O Item 14 contém observações pertinentes à página/estado. Não inserir observações genéricas ou fabricar dez itens para imitar exemplo anterior; sua efetiva composição obedece ao contrato vigente.

## 6. Atualização e migração sem regressão

1. Antes de modificar bytes: confirmar versão do objeto e dos documentos que o referenciam; registrar SHA, referências e histórico, mapear mudanças e obter autorização específica.
2. **Atualizar** documento já conforme alterando campos/linhas preexistentes e, quando necessário, `Estado vigente`; manter a estrutura integral e as decisões anteriores.
3. **Migrar** documento divergente construindo a versão normalizada a partir do **template integral**, redistribuindo todo o conteúdo para H3s predeterminados, sem transcrever interpretações como fatos nem apagar decisões.
4. Classificar a alteração como editorial, factual ou normativa; alteração editorial **modifica hash** e pode afetar a identidade de bytes anteriormente aprovados. A consequência sobre o Gate depende da SPEC e da autorização humana, não da Skill.
5. Confrontar White/Black/páginas/estados e referências históricas/dependentes; atualizar apenas vínculos autorizados. Um arquivo congelado não perde seu histórico nem é reaberto automaticamente por comparação de formato.
6. Validar scripts, diff e leitura semântica. Falha estrutural obriga correção da redação; falta de prova material obriga registrar `NÃO VALIDADO` e bloquear a afirmação correspondente.

## 7. Limite técnico do validador

`../scripts/validar_estrutura.py` comprova **somente** a presença e ordenação do esqueleto editorial: títulos e níveis, campos rotulados, tabelas, nomes de colunas, linhas fixas, dados mínimos e ausência de placeholders. Ele não confere se os valores são verdadeiros, se o PNG é fiel, se a data/hora ocorreu, nem se o responsável aprovou. Essas verificações dependem da leitura física, das normas e da manifestação humana.
