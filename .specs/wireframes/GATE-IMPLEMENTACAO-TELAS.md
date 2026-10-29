# SaOr — Gate obrigatório de conformidade das Telas e Pranchas de Implementação

## 1. Autoridade, escopo e regra anti-regressão

Gate auxiliar **exclusivo da SPEC 3** [`PROCESSO-TELA-PRANCHA.md`](PROCESSO-TELA-PRANCHA.md), para interfaces T/M/E, temas white/black, estados aplicáveis e páginas de continuidade. Não se aplica à construção do template (SPEC 1), não muda a referência vigente (SPEC 2), não reexecuta Gates históricos 1–6 e não altera os arquivos congelados.

**Ordem obrigatória e bloqueante:** `GI-0 (requisitos) → PNG da Tela → GI-1 (aprovação visual do PNG) → TextFrame derivado → GI-2 (aprovação documental do conjunto PNG + TextFrame) → GI-3 (montagem técnica da Prancha) → GI-4 (aceite final)`. É proibido criar o TextFrame como base para adivinhar o PNG. Nenhuma etapa pode herdar aprovação nem ser aprovada apenas por existir arquivo ou por constar em conversa.

Usar `PENDENTE`, `EM VERIFICAÇÃO`, `AGUARDANDO APROVAÇÃO`, `APROVADO E CONGELADO` ou `BLOQUEADO` com decisão e evidência explícitas. Esses estados não substituem os estados agregados da matriz das 71 interfaces.

## 2. GI-0 — Pré-condições e inventário funcional (técnico)

- [ ] Ler ficha **e Textframe** da interface no Documento Mestre, regras transversais, estados, conteúdo, ações/destinos e relações; produzir inventário verificável dos elementos requeridos, sem introduzir outros.
- [ ] Conferir temas white/black, ViewPort técnico `360 × 800`, margens/tokens e padrões aplicáveis; inspecionar visualmente PNG e Wireframe Text oficiais da referência vigente por meio da SPEC 2.
- [ ] Registrar quais elementos são próprios da Tela e quais são apenas demonstrações do template; nenhum exemplo da Prancha vira componente da interface sem requisito.
- [ ] Mapear estados exigidos, variações reais de rolagem, comportamento fixo/rolável e potencial total de páginas; não assumir uma página sem inspeção geométrica posterior.
- [ ] Identificar qualquer lacuna de requisito, padrão técnico ou definição visual; se impedir representação fiel, `BLOQUEADO`, sem decisão estética inferida.
- [ ] Criar registro persistente no caminho `docs/wireframes/images/<tema>/telas/controle/<nome-base>.md`, contendo ID, tema, plano de páginas/estados, requisitos com fontes, referência vigente e hashes, evidências e decisão GI-0. **Esse registro não é um Wireframe Text e não define aparência concorrente.**

**Passagem:** inventário/autoridades completos e nenhuma lacuna impeditiva. GI-0 autoriza **propor um PNG visual**, mas não aprova a Tela.

## 3. GI-1 — PNG de proposta visual da Tela (aprovação humana)

- [ ] Produzir PNG isolado **antes de escrever o TextFrame** em `docs/wireframes/images/<tema>/telas/<nome-base>.png`, `360 × 800 px`, a partir do inventário e da fonte funcional; o template oficial não foi copiado nem modificado.
- [ ] Abrir o PNG fisicamente e **inspecionar a interface real** (não apenas metadados): composição, alinhamento, hierarquia, tamanhos, textos, superfícies, tipografia, cores, ícones, ações visíveis e estados correspondem à documentação e aos padrões aplicáveis do tema.
- [ ] AppBar é a da interface; item de lista tem ícone apenas quando documentado; cada indicador de estado tem ícone/rótulo conforme sua especificação e não é transformado em botão sem requisito.
- [ ] Nenhum texto solto, região vazia arbitrária, conteúdo demonstrativo do Modelo C, componente inventado, campo omitido, comprimido ou truncado. Qualquer elemento não verificável bloqueia a aprovação.
- [ ] Se houver rolagem, apresentar **todos** os PNGs da sequência, um por posição de rolagem, com inventário coberto e sem duplicações; white/black devem ter equivalência funcional. Representações adicionais de estados são PNGs distintos e só existem se os estados forem exigidos.
- [ ] Registrar no `telas/controle/<nome-base>.md`: caminho, dimensões, SHA-256 de cada PNG/estado/página, fonte de cada elemento, inspeção visual, pendências, responsável, data e **decisão humana expressa vinculada aos hashes**.

**Passagem:** PNGs visualmente aprovados, com hashes congelados para documentação. **Aprovação GI-1 não aprova TextFrame nem autoriza montar Prancha.** Se a imagem for alterada depois dessa decisão, GI-1 perde validade para os novos bytes; exigir nova apresentação e aprovação, preservando o histórico dos hashes aprovados.

## 4. GI-2 — TextFrame derivado e aprovação documental do conjunto (aprovação humana)

- [ ] O TextFrame/Wireframe Text da Tela foi **criado somente após GI-1**, no contrato [`WIREFRAME-TEXT-TELA.md`](WIREFRAME-TEXT-TELA.md), a partir dos PNGs cujos hashes e aprovações constam no controle.
- [ ] O documento contém vínculo exato com os PNGs, fontes, textos, estados, tokens e **cotas x/y/w/h medidas na imagem**, além do TextFrame textual refletindo a disposição visual aprovada.
- [ ] Inspeção cruzada **PNG ↔ TextFrame ↔ geometria ↔ requisito** para todos os elementos: nenhum componente fora do PNG, nenhum elemento do PNG sem especificação, nenhum posicionamento aproximado como definição final.
- [ ] A documentação visual não se resume a desenho ASCII, tabela, régua `y` ou inventário. A **evidência visual é o próprio PNG aprovado**; texto e tabelas só documentam o que já existe nele.
- [ ] Completude do conjunto de páginas, estados e continuidade comprovada. White e black têm a mesma semântica funcional e suas cores/estilos autorizados, com revisões e aprovações independentes.
- [ ] Confrontar novamente SHA-256 dos PNGs com os aprovados em GI-1. Se os bytes mudaram, **retornar ao GI-1**, não aceitar mera mudança textual.
- [ ] Registrar decisão humana **expressa, datada e vinculada à versão e aos hashes** do TextFrame, do PNG e do controle. Só após esse aceite o par Tela + documento pode ficar `APROVADO E CONGELADO`.

**Passagem:** todas as páginas e temas e os estados requeridos estão aprovados **como conjunto visual e documental**. Falha bloqueia montagem. Se mudar paginação/geométrica/estado do PNG, voltar a GI-1; se apenas o texto tiver erro, corrigir o rascunho textual sem alterar o PNG e reapresentar GI-2.

## 5. GI-3 — Uso da referência vigente e montagem da Prancha (técnico)

- [ ] Conferir novamente seleção vigente e os hashes dos arquivos oficiais via SPEC 2. A cópia de trabalho é **nova**, `1280 × 1920 px`, e a referência congelada permanece intacta.
- [ ] **Primeiro ato de alteração da nova cópia:** substituir o ViewPort demonstrativo pelo PNG **já aprovado em GI-2** da mesma página e tema, `360 × 800 px`, para Modelo C em `x=40, y=272`, `1:1`, sem recorte, recoloração ou alteração de pixels. Conferir recorte contra fonte pixel a pixel. Outro modelo exige mapeamento previamente autorizado, nunca coordenadas inferidas.
- [ ] **Somente depois** preencher cabeçalho/quadros variáveis: `ETAPA = <ID> - <Nome>` da ficha, `PÁGINA = XX / YY` da continuidade e `VERSÃO = vNN` da revisão. Preservar a estrutura do modelo vigente.
- [ ] **Item 10** contém apenas componentes usados na Tela aprovada, suas amostras/medidas reais; a AppBar é específica e os ícones de lista seguem requisitos individuais, não o exemplo do template.
- [ ] **Item 14** contém apenas observações técnicas relevantes àquela interface/página; nada genérico é inserido para preencher espaço.
- [ ] Registro textual de composição contém fontes, nome/hash da Tela e do TextFrame, controle GI-0/1/2, modelo/versão/hash, campos específicos, coordenadas, dados de página e decisão técnica GI-3.
- [ ] Se uma informação técnica não couber nas áreas fixas, bloquear; não reduzir Tela nem gerar página fictícia de rolagem para acomodar notas da Prancha.

**Passagem:** GI-3 `CONFORME` com evidências técnicas, não aprovação final. Os Gates 1–6 de construção de template não são executados.

## 6. GI-4 — Conferência e aprovação da Prancha e do conjunto (aprovação humana)

- [ ] PNG novo da Prancha `1280 × 1920` com identificação, versão e caminho corretos; template oficial preservado por hash.
- [ ] Recorte da região de ViewPort da Prancha **pixel a pixel idêntico** ao PNG aprovado do GI-2.
- [ ] ID, `ETAPA`, `PÁGINA`, `VERSÃO`, temas, datas, status e referências exatas em conformidade com arquivos e aprovações.
- [ ] Item 10, Item 14 e demais regiões variáveis conferidos com Tela real e documentos, não com exemplos históricos.
- [ ] Todas as páginas necessárias e estados aplicáveis estão representados conforme a decisão, sem campos faltantes ou duplicados e com equivalência white/black.
- [ ] Evidências de cada gate, aprovações humanas independentes, nomes, hashes e referências históricas constam dos registros persistentes.
- [ ] Aprovação humana expressa, datada e vinculada à versão exata **de cada Prancha**; decisão final sobre o conjunto completo dos dois temas.

**Passagem:** `GI-4 = APROVADO E CONGELADO` somente com aprovação individual e do conjunto completo. Só então a interface pode receber `APROVADO` na matriz operacional. Falha na apresentação não autoriza alterar os artefatos anteriores já aprovados.

## 7. Evidência persistente, regressão e independência de conversa

**GI-0 e GI-1 devem existir no registro `telas/controle/<nome-base>.md` ANTES da criação do Wireframe Text individual.** Esse registro é evidência factual do processo, não um segundo contrato visual. GI-2 e as referências aos GI-0/1 devem constar no Wireframe Text e no registro; GI-3/4 devem constar no registro de composição da Prancha. Não criar uma aprovação fictícia para preencher campos e não depender de chat para comprovar decisões.

Campos mínimos: `ID / nome / tema / página XX/YY / versão / Gate / regra e fonte / resultado CONFORME ou NÃO CONFORME / arquivo e SHA-256 / dimensões / parecer / responsável / data / decisão / impactos`. Se não houver prova persistente, o Gate é `BLOQUEADO` ou `AGUARDANDO APROVAÇÃO`; aprovação em conversa só vale quando transcrita fielmente para o documento antes do avanço.

**Regressão:** alterações de PNG depois de GI-1 exigem reavaliação GI-1/2/3/4 dependentes; alterações apenas do TextFrame antes de GI-2 preservam o PNG aprovado, mas devem passar pela validação cruzada; mudanças na rolagem, total de páginas, estados ou conteúdo funcional exigem voltar ao Gate correspondente com nova versão/rastreabilidade. As alterações não autorizam modificar template, Documento Mestre ou outras interfaces.

**Critério final:** uma pessoa sem acesso a conversas consegue abrir o PNG aprovado, verificar todos os componentes/estados, reproduzir suas especificações a partir do TextFrame derivado, montar a Prancha com a referência vigente e comprovar cada decisão pelo repositório. **Um esquema textual isolado nunca satisfaz o GI-1 nem o GI-2.**
