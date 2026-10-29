# SaOr — Wireframes: índice de autoridades e contratos

**Fase:** Wireframe Conceitual em Imagem. A baseline funcional `v1.0` é definida em [`docs/Documento_Mestre.md`](../../docs/Documento_Mestre.md). Este README é índice, não um quarto processo normativo.

## Três SPECs distintas

### SPEC 1 — Prancha do Template: definição técnica

[`PROCESSO-PRANCHA.md`](PROCESSO-PRANCHA.md): processo de construção da **estrutura de uma nova prancha-modelo** a partir de canvas vazio, com Gates 1–6, aprovação de texto e PNG. Contratos auxiliares: [`WIREFRAME-TEXT.md`](WIREFRAME-TEXT.md) (especificação textual da Prancha do Template) e [`MONTAGEM-IMAGEM.md`](MONTAGEM-IMAGEM.md) (execução visual profissional). Não governa interfaces T/M/E já baseadas em referência aprovada.

### SPEC 2 — Prancha de Modelo (Template): referência selecionada

[`REFERENCIA-TEMPLATE-OFICIAL.md`](REFERENCIA-TEMPLATE-OFICIAL.md): como identificar, validar e preservar a **referência aprovada e vigente**, **não** como desenhar outra prancha. A fonte de verdade da seleção atual e de todas as decisões históricas é o [`Registro_Controle_Template_Oficial.md`](../../docs/wireframes/images/Registro_Controle_Template_Oficial.md).

**Seleção vigente na atualização deste índice:** Modelo C, `white` v02 e `black` v01, aprovado em 28/10/2026. As seis cópias oficiais ficam em `docs/wireframes/images/<tema>/template/`, com hashes e origens inventariados no registro. Uma versão aprovada permanece congelada mesmo quando deixa de ser vigente; revisão exige justificativa, autorização, nova versão e atualização formal do registro.

### SPEC 3 — Prancha de Implementação: utilização funcional

[`PROCESSO-TELA-PRANCHA.md`](PROCESSO-TELA-PRANCHA.md) governa **cada interface T/M/E**, nos dois temas, com o contrato auxiliar de **TextFrame posterior ao PNG** [`WIREFRAME-TEXT-TELA.md`](WIREFRAME-TEXT-TELA.md) e o [Gate obrigatório de conformidade GI-0 a GI-4](GATE-IMPLEMENTACAO-TELAS.md):

```text
Documento Mestre + ficha/Textframe funcional → GI-0 / inventário
→ PNG VISUAL da Tela isolada (360 × 800 por tema/página/estado aplicável)
→ GI-1 / INSPEÇÃO E APROVAÇÃO VISUAL do PNG e do seu hash
→ TextFrame / Wireframe Text DERIVADO do PNG já aprovado
→ GI-2 / CONFRONTO E APROVAÇÃO DOCUMENTAL do conjunto PNG + TextFrame
→ verificação da referência vigente (SPEC 2)
→ GI-3 / substituição inicial do ViewPort na nova cópia de Prancha
→ preenchimento fiel dos campos PÁGINA, ETAPA, Item 10 e Item 14
→ GI-4 / APROVAÇÃO da Prancha e do conjunto / VERSIONAMENTO
```

Não desenhar a Tela diretamente na Prancha. O PNG visual é a primeira representação da Tela e deve ser aprovado antes de escrever seu TextFrame; um esquema ASCII não substitui a imagem. Os registros GI-0/GI-1 ficam em `telas/controle/` e são distintos do TextFrame. A Tela não herda medidas de componentes demonstrativos da Prancha e não deve ser redimensionada para caber nela. Se a interface precisar de rolagem, produzir **um ViewPort técnico aprovado e uma nova Prancha por posição/página**, mantendo todos os campos, sem reduzir ou omitir conteúdos; o campo `PÁGINA = XX / YY` controla a sequência e `ETAPA = <ID> - <Nome>` identifica a mesma interface. O Item 10 só registra componentes usados (AppBar fiel; ícones de lista opcionais) e o Item 14 só observações pertinentes à Tela. Uma Prancha de Implementação **não modifica** o template congelado. Os Gates 1–6 da SPEC 1 não são reexecutados por interface funcional.

## Norma técnica transversal

[`REGRAS-TECNICAS.md`](REGRAS-TECNICAS.md) determina canvas, ViewPort, margens, tokens, componentes, estados e acessibilidade da representação. Uma norma compartilhada não escolhe um modelo oficial e não define conteúdo individual das interfaces.

## Consulta por tarefa

| Tarefa | Consultar nesta ordem de responsabilidade |
|---|---|
| Definir/revisar prancha-modelo | SPEC 1 → regras técnicas → Wireframe Text da Prancha → montagem visual → aprovações |
| Identificar referência oficial | SPEC 2 → registro genérico → seis artefatos físicos e hashes |
| Produzir uma interface funcional | Documento Mestre → SPEC 3 → contrato do Wireframe Text da Tela → normas técnicas → SPEC 2 → arquivos funcionais e registros de aprovação |
| Localizar arquivos, versões e estados | [`docs/wireframes/images/README.md`](../../docs/wireframes/images/README.md) |
| Solicitar mudança de qualquer norma ou versão congelada | [`.specs/PROCESSO-ALTERACAO-ASSISTIDA.md`](../PROCESSO-ALTERACAO-ASSISTIDA.md) |

**Proibição:** nenhuma instrução de README, referência visual, geometria histórica, nome de arquivo ou prompt altera os contratos aprovados ou substitui uma decisão explícita. Conteúdo insuficiente bloqueia a etapa, em vez de autorizar inferências.
