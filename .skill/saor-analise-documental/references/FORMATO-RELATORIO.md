# SaOr — Formato de relatório de conformidade documental

Usar **somente** para parecer de análise, plano de atualização/migração ou auditoria de entrega. **Não inserir este relatório nos três documentos de interface.** Quando a tarefa for só gerar/atualizar, produzir o documento no template e uma síntese separada de verificações e limites.

## 1. FATOS VERIFICADOS — Base e limites

| Campo | Evidência executada |
|---|---|
| Fonte física / tamanho / SHA-256 | {{FONTE}} |
| Integridade ZIP / caminhos / CRC, quando aplicáveis | {{RESULTADO}} |
| Normas e contratos efetivamente lidos | {{CAMINHOS}} |
| Exclusões/LEGADOS observados | {{LIMITE}} |
| Interface, tema, página e versão examinados | {{IDENTIDADES}} |
| Inventário anterior fisicamente reutilizado, quando houver | {{FONTE OU AUSÊNCIA}} |

## 2. Inventário de objetos e aprovações

| Tipo | Caminho | Tamanho | SHA-256 | Estado/decisão comprovada | Dependências |
|---|---|---:|---|---|---|
| {{TIPO}} | {{CAMINHO}} | {{N}} | {{HASH}} | {{DECISAO}} | {{DEPENDENCIAS}} |

## 3. Comparação integral da estrutura (repetir por documento)

| H2/H3 esperado | Campos/tabelas e posições obrigatórias | Trecho atual | Resultado editorial | Fonte/linha |
|---|---|---|---|---|
| {{SUBTOPICO}} | {{ESQUEMA}} | {{LOCAL OU AUSENTE}} | {{CONFORME OU DESVIO EDITORIAL}} | {{FONTE}} |

Conferir **todos** os H3 do template, além de H1, abertura, nomes/ordem de tabelas, colunas, linhas fixas, rótulos e ausência de tópicos extras. A reprovação de formato **não revoga** automaticamente Gate aprovado.

## 4. Mapeamento e classificação sem perda

| ID | Documento e trecho | Conteúdo atual | Campo/H3 de destino | Classificação técnica ou editorial | Risco/impacto |
|---|---|---|---|---|---|
| {{ID}} | {{LOCAL}} | {{EXCERTO}} | {{H3}} | {{CLASSE}} | {{RISCO}} |

Utilizar categorias do processo de alteração assistida. Separar diferenças históricas legítimas de contradições atuais. Não usar `DESVIO EDITORIAL` como se fosse Gate normativo.

## 5. Verificação da geração/alteração e dependências

| Controle | Evidência | Resultado | Limitação |
|---|---|---|---|
| Template integral e estrutura | {{SCRIPT_E_INSPECAO}} | {{RESULTADO}} | {{LIMITE}} |
| Campos preenchidos e fontes | {{LEITURA_FATUAL}} | {{RESULTADO}} | {{LIMITE}} |
| Caminhos, hashes e referências cruzadas | {{CONFRONTO}} | {{RESULTADO}} | {{LIMITE}} |
| Decisões históricas/novas | {{REGISTROS}} | {{RESULTADO}} | {{LIMITE}} |
| Diff e escopo autorizado | {{COMPARACAO}} | {{RESULTADO}} | {{LIMITE}} |
| ZIP local de entrega, quando houver | {{CRC_E_ESTRUTURA}} | {{RESULTADO}} | {{LIMITE}} |

## 6. INTERPRETAÇÕES, IMPEDIMENTOS E APROVAÇÕES NECESSÁRIAS

| Natureza | Objeto | Evidência e motivo | Ação permitida/pendente |
|---|---|---|---|
| {{NATUREZA}} | {{OBJETO}} | {{PROVA}} | {{ACAO}} |

O relatório não é uma decisão humana e não substitui nenhuma SPEC. Não afirmar conformidade sem testes e evidências realmente executados.
