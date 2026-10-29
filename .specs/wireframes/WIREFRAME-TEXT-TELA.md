# SaOr — Contrato documental do Wireframe Text individual da Tela

## 1. Natureza e autoridade

Este contrato auxiliar pertence à **SPEC 3** ([`PROCESSO-TELA-PRANCHA.md`](PROCESSO-TELA-PRANCHA.md)). Define o documento que especifica **cada Tela funcional** antes de existir seu PNG. Não especifica a Prancha do Template e **não altera** o Wireframe Text congelado do Modelo C. O contrato histórico [`WIREFRAME-TEXT.md`](WIREFRAME-TEXT.md) aplica-se à **Prancha do Template**, não serve de substituto ao documento individual da Tela.

Fonte funcional: [`docs/Documento_Mestre.md`](../../docs/Documento_Mestre.md), baseline v1.0; fonte dimensional/tokens: [`REGRAS-TECNICAS.md`](REGRAS-TECNICAS.md). O conteúdo documental da interface sempre prevalece sobre demonstrações gráficas do ViewPort ou do template.

## 2. Unidade de especificação e identificação

Criar um documento **por ID funcional, tema, página e versão**, antes de gerar a respectiva Tela de Referência. Armazenar em `docs/wireframes/images/<tema>/telas/wiframetext/<ID>-<PÁGINA>-<TOTAL>_v<VERSÃO>.md`; por exemplo `white/telas/wiframetext/T00-01-01_v01.md`. Uma página white não é aprovação automática da equivalente black.

O nome registra versão documental, não cria um ID funcional novo. Os IDs e a lógica de paginação devem vir do Documento Mestre e da SPEC 3. O arquivo não deve compartilhar o diretório nem substituir o Wireframe Text congelado do template.

## 3. Conteúdo mínimo verificável

Documentar **explicitamente**, sem depender de prompts:

1. identificação: ID, nome, variação, página/total, versão, data, baseline funcional e estado de aprovação;
2. rastreabilidade das fontes: seção/ficha/Textframe do Documento Mestre, regras transversais aplicáveis, elementos que não puderam ser resolvidos;
3. escopo funcional da página: informações obrigatórias, campos, obrigatoriedade, ações/destinos, retornos, estados e relações com outras telas; não acrescentar requisitos novos;
4. composição lógica: árvore/ordem de leitura, agrupamentos, hierarquia, componentes, rótulos e conteúdo textual exato;
5. geometria da Tela: canvas próprio de `360 × 800 px`, margens horizontais de `12 px`, largura interna útil de `336 px`, posições `x/y`, dimensões `w/h`, alinhamentos, espaçamentos e limites de cada região/componente (coordenadas locais à Tela, não à Prancha);
6. tokens do tema, tipografia técnica, iconografia, cores, superfícies, bordas e estados, identificando suas fontes; ausência de especificação não autoriza inventar um token;
7. safe areas e limites conforme regras vigentes, sem importar coordenadas do ViewPort demonstrativo nem aplicar as posições de cabeçalho da Prancha;
8. regras de paginação e continuidade de conteúdo: elementos persistentes, fragmentação justificada, ordem, páginas equivalentes white/black;
9. descrição determinística da montagem de **cada elemento da Tela** (tipo, posição, tamanho, texto, estado, origem); decisões ainda não resolvidas ficam marcadas como bloqueio;
10. checklist técnico com resultado, pendências, decisão humana explícita, data, estado e identidade da versão aprovada.

Não usar imagem visual existente como autoridade para criar comportamento novo. Uma proposta com informação insuficiente fica `EM DEFINIÇÃO` ou `BLOQUEADO`, nunca `APROVADO E CONGELADO`.

## 4. Estados e gate do documento

Estados documentais: `PENDENTE`, `EM DEFINIÇÃO`, `AGUARDANDO APROVAÇÃO`, `APROVADO E CONGELADO`, `BLOQUEADO POR GATE ANTERIOR` e `NÃO APLICÁVEL` somente com justificativa expressa. São estados do **Wireframe Text da Tela**, não os Gates 1–6 históricos da SPEC 1.

- Iniciar como `PENDENTE` e, ao redigir, `EM DEFINIÇÃO`.
- Só passar a `AGUARDANDO APROVAÇÃO` após leitura completa dos requisitos, cálculos de geometria e verificação de ausência de contradições e campos vazios essenciais.
- Somente decisão humana **expressa**, registrada neste arquivo com data/versão e objeto aprovado, altera para `APROVADO E CONGELADO`.
- A aprovação autoriza produzir o PNG da Tela correspondente. **Não** aprova automaticamente a Tela PNG nem a Prancha de Implementação.
- Alteração depois de aprovada exige nova versão ou revisão formal documentada, mantendo a versão aprovada anterior e registrando os artefatos dependentes afetados.

## 5. Validação anterior ao PNG

Verificar: (a) todos os requisitos funcionais aplicáveis estão representados ou possuem bloqueio registrado; (b) todos os elementos possuem dados suficientes para execução sem decisões visuais adicionais; (c) toda caixa está dentro de `360 × 800`, respeitando margens e limites; (d) não houve compressão indevida de conteúdo ou supressão de ações; (e) paginação está reproduzível; (f) tokens e componentes pertencem ao tema; (g) equivalente white/black preserva conteúdo e comportamento; (h) versões e aprovação foram registradas no próprio arquivo.

Se não for possível satisfazer uma regra técnica sem violar a baseline, interromper e registrar **CONTRADIÇÃO DOCUMENTAL**, sem editar o Documento Mestre ou o template.

## 6. Vínculo com o PNG da Tela

A Tela deve ser gerada **depois** desta aprovação, em `docs/wireframes/images/<tema>/telas/<mesmo-nome-base>.png`. Na validação do PNG, comparar posições, textos, componentes, estados, dimensões e paginação com o documento aprovado; registrar caminho, dimensões e SHA-256 do PNG, resultado técnico, aprovação humana específica e versão vinculada. Pode-se registrar essa evidência em uma seção de **resultados posteriores** no mesmo Wireframe Text, sem alterar retroativamente sua especificação geométrica aprovada. O PNG permanece um artefato separado.

**Saída do contrato:** Wireframe Text **prévio, completo e aprovado** que permite construir a Tela isolada sem consultar conversas e sem depender da Prancha de Implementação.
