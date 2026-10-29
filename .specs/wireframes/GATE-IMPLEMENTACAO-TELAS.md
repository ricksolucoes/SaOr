# SaOr — Gate obrigatório de conformidade das Telas e Pranchas de Implementação

## 1. Autoridade e aplicação

Este é o **Gate auxiliar obrigatório da SPEC 3** [`PROCESSO-TELA-PRANCHA.md`](PROCESSO-TELA-PRANCHA.md), aplicado a **cada interface T/M/E**, temas `white` e `black`, cada página de continuidade e seu conjunto completo. **Não** é Gate de criação de Prancha do Template (SPEC 1), não define ou escolhe a referência selecionada (SPEC 2) e não altera os seis arquivos oficiais congelados. O Documento Mestre é a fonte dos requisitos funcionais; a SPEC 3 governa os procedimentos; este documento governa **somente o bloqueio, a evidência e a passagem verificável** entre etapas.

Ordem estrita: `GI-0 → GI-1 → GI-2 → GI-3 → GI-4`. A passagem requer checklist sem falhas, artefatos e registros existentes e, onde indicado, aprovação **humana explícita**. Nenhuma etapa é considerada aprovada por ter sido renderizada nem por aparecer em conversa. `PENDENTE`, `EM VERIFICAÇÃO`, `AGUARDANDO APROVAÇÃO`, `APROVADO E CONGELADO` e `BLOQUEADO` são estados internos do Gate; **não** substituem os estados agregados da matriz de 71 interfaces no README operacional.

## 2. GI-0 — Pré-condições documentais (técnico)

- [ ] ID e nome conferidos na ficha/Textframe da baseline funcional; nenhuma função ou campo acrescentado por inferência.
- [ ] Ambos os temas e a versão técnica `360 × 800 px` aplicável identificados; interface, estados, ações, ordem, regras de rolagem e páginas previstos.
- [ ] Referência aprovada e vigente verificada na SPEC 2 e no registro permanente por tema (modelo, versões, caminhos, SHA-256); nenhum arquivo congelado destinado a edição.
- [ ] Existência e acessibilidade do contrato do Wireframe Text da Tela, das invariantes e dos caminhos para saídas isoladas.
- [ ] Ambiguidades e contradições identificadas e bloqueadas até decisão documentada; aprovação do Gate não autoriza novo requisito funcional.

**Passagem:** evidência registrada, sem lacunas que comprometam a execução; senão `BLOQUEADO`. GI-0 não aprova previamente um futuro WT, PNG ou Prancha.

## 3. GI-1 — Wireframe Text completo antes de qualquer PNG (aprovação humana)

- [ ] Documento individual por **ID / tema / página / total / versão**, conforme `WIREFRAME-TEXT-TELA.md`, elaborado antes de gerar a imagem.
- [ ] **Inventário completo dos elementos** da interface: campos, textos, obrigatoriedade, componentes, ações/destinos, estados, origem funcional e página de aparição.
- [ ] AppBar de cada estado/posição especificada com **layout próprio** (ou ausência justificada), sem copiar a amostra demonstrativa; em cada item de lista, presença/ausência de ícone fundamentada.
- [ ] Continuidade real de rolagem especificada: página `XX / YY`, posição/trecho, ordem de elementos, limites, elementos realmente fixos e roláveis; **nenhum** campo eliminado, inventado, comprimido ou repetido como novo.
- [ ] Tema white/black funcionalmente equivalente, sem presumir equivalência de aprovação; `PÁGINA` distinta de `VERSÃO`.
- [ ] Medidas da Tela verificadas em `360 × 800`; layout e tokens justificados; componentes dos futuros Itens 10 e notas do Item 14 rastreáveis ao WT e à ficha.
- [ ] Decisão **humana explícita e datada** para a versão exata do WT, registrada no próprio documento (`APROVADO E CONGELADO`).

**Passagem:** todos os WT necessários da página/tema aprovados. A aprovação permite executar GI-2 e não constitui aprovação de PNG.

## 4. GI-2 — ViewPorts técnicos / Telas de Referência (aprovação humana)

- [ ] Um PNG **individual por ID/tema/página** tem `360 × 800 px` exatos e nome/caminho/versão do WT aprovado.
- [ ] Cada pixel/conteúdo representa a posição de rolagem aprovada; os campos e estados visíveis da página coincidem com o WT, inclusive a AppBar e ícones opcionais em itens de lista.
- [ ] Inventário de cobertura de **todas as páginas**: união dos campos/ações/estados exigidos completa; continuidade ordenada, sem exclusão e sem repetição funcional indevida.
- [ ] Elementos persistentes repetidos somente se documentados; não copiar o ViewPort demonstrativo como conteúdo funcional nem desenhar a Tela dentro da Prancha.
- [ ] Geometria, margens, tokens, legibilidade, comportamento de rolagem e equivalência entre temas verificados.
- [ ] Caminho, dimensões, SHA-256, WT vinculado e decisão **humana explícita** registrados por Tela/página/tema; todas as páginas dependentes aprovadas.

**Passagem:** todas as Telas necessárias aprovadas e `APROVADO E CONGELADO`, incluindo a verificação do conjunto. Se houver conteúdo excedente, retornar a GI-1 para **nova página de continuidade** e aprovação; mudar a especificação já aprovada exige **nova versão**, sem apagamento histórico.

## 5. GI-3 — Uso do template vigente e sequência da montagem (técnico)

- [ ] A cópia de trabalho da Prancha usa **exatamente** a referência vigente verificada (ou a versão historicamente vinculada a uma revisão autorizada); a origem congelada permanece intacta.
- [ ] **Primeiro ato de alteração da nova cópia:** substituir o ViewPort técnico demonstrativo pelo PNG da Tela **da mesma página e tema**, `360 × 800 px`, no Modelo C em `x=40`, `y=272`, escala `1:1`, sem recorte, recoloração ou redimensionamento. Conferir identidade pixel a pixel. Coordenadas de outros modelos não podem ser presumidas.
- [ ] Só **depois** dessa substituição preencher metadados e quadros variáveis: `PÁGINA = XX / YY` da rolagem, `ETAPA = <ID> - <Nome da interface>` da ficha (por exemplo `T00 - Configuração da aplicação`), `VERSÃO = vNN` da revisão e os demais identificadores.
- [ ] **Item 10 — COMPONENTES:** contém somente tipos, amostras, estados e dimensões dos componentes realmente usados na Tela; AppBar fiel àquela interface (sem depender do exemplo), ícones de lista apenas quando previstos, nenhum item incluído só por existir no template.
- [ ] **Item 14 — OBSERVAÇÕES TÉCNICAS:** contém somente particularidades, premissas ou restrições comprovadas da Tela/posição, sem copiar notas padrão do template ou inventar preenchimento.
- [ ] Geometria fixa, painéis e áreas do Modelo C preservados; variabilidade somente conforme seção 6.1 da SPEC 3. Impossibilidade de acomodar informações técnicas na área aprovada **bloqueia**, não cria rolagem falsa da documentação nem autoriza alterar o modelo.
- [ ] Registro de composição textual preenchido **antes da aprovação final**, com os hashes exatos da Tela, WT, modelo, ViewPort oficial e identidade da página/rolagem.

**Passagem:** `GI-3 = CONFORME` com evidências técnicas persistentes. Não é aprovação da Prancha e não requer reexecutar Gates 1–6 da SPEC 1.

## 6. GI-4 — Conferência e aprovação da Prancha funcional e do conjunto (aprovação humana)

- [ ] PNG da Prancha de Implementação **novo** com `1280 × 1920 px` e caminho/versão corretos; cópia de referência preservada por SHA-256.
- [ ] Recorte da região ViewPort é **pixel a pixel idêntico** ao PNG isolado aprovado correspondente.
- [ ] `ETAPA`, `PÁGINA`, `VERSÃO`, ID, tema e status correspondem ao WT, à Tela e ao registro; todas as páginas possuem total `YY` correto.
- [ ] Item 10 e Item 14 conferidos contra a **Tela efetiva** e o Wireframe Text aprovado, sem itens demonstrativos incorretos, campos omitidos ou notas genéricas.
- [ ] Todas as Pranchas de todas as posições de rolagem estão presentes, com continuidade completa e equivalência white/black; itens fixos/roláveis preservam comportamento.
- [ ] Versões antigas e decisões históricas mantidas; todas as fontes, hashes e aprovações independentes estão registradas por tema e página.
- [ ] **Aprovação humana expressa, datada e vinculada à versão** para cada Prancha; avaliação do conjunto confirma zero campo faltante, zero conteúdo inventado, zero regressão do template.

**Passagem:** `GI-4 = APROVADO E CONGELADO` somente após aprovação individual e do **conjunto completo dos dois temas**. Só então a interface pode receber estado agregado `APROVADO` no inventário. Falha de apresentação não autoriza editar Tela/WT aprovados nem template.

## 7. Evidência persistente e consequência de falhas

Registrar **nos próprios Wireframe Text individuais e registros de composição existentes**, sem criar formulário paralelo ou depender da conversa:

```text
ID funcional / Nome / Tema / Página XX / YY / Versão
Gate: GI-0 | GI-1 | GI-2 | GI-3 | GI-4
Critério avaliado / Fonte normativa + localização / Resultado CONFORME ou NÃO CONFORME
Arquivo de evidência / SHA-256 / dimensão quando aplicável
Decisão técnica / pendências / impacto sobre as páginas e temas relacionados
Aprovação humana quando exigida: responsável / data / versão exata / decisão
Estado final: PENDENTE | EM VERIFICAÇÃO | AGUARDANDO APROVAÇÃO | APROVADO E CONGELADO | BLOQUEADO
```

Não declarar `CONFORME` quando a evidência faltar. Divergência não resolvida bloqueia todos os artefatos descendentes daquele trecho, sem invalidar silenciosamente outros aprovados. Alteração na ordem de rolagem, campos ou total de páginas obriga revisar GI-1/GI-2/GI-3/GI-4 das páginas/temas afetados, com versões e aprovações próprias. Revisão da referência oficial só pela SPEC 2 e processo formal de alteração; não deve ser provocada automaticamente pelo Gate funcional.

**Critério final de saída:** uma pessoa ou execução independente pode reproduzir todos os ViewPorts e Pranchas por página, conferir os 14 blocos de apresentação aplicáveis e rastrear cada elemento à sua origem funcional, utilizando apenas os artefatos aprovados e as evidências persistentes no repositório.
