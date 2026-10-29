# SaOr — Especificações canônicas

A pasta `.specs/` concentra normas reutilizáveis do projeto. **Toda intervenção assistida** começa por [`PROCESSO-ALTERACAO-ASSISTIDA.md`](PROCESSO-ALTERACAO-ASSISTIDA.md), que exige evidência contextual, autorização expressa, execução local delimitada e validação de regressão.

A documentação não depende de prompts ou memória de conversa. Uma regra possui **uma autoridade normativa principal**; outros documentos podem indicar dependências sem repeti-la ou reinterpretá-la.

## Autoridades distintas dos wireframes

| Autoridade | Documento canônico | Limite |
|---|---|---|
| Funcional | [`docs/Documento_Mestre.md`](../docs/Documento_Mestre.md) | Requisitos das 71 interfaces, Textframes e comportamento; não é editado para acomodar imagens |
| SPEC 1 — definição da Prancha do Template | [`wireframes/PROCESSO-PRANCHA.md`](wireframes/PROCESSO-PRANCHA.md) | Criação/revisão de pranchas-modelo e Gates, **não** produção T/M/E |
| SPEC 2 — referência selecionada | [`wireframes/REFERENCIA-TEMPLATE-OFICIAL.md`](wireframes/REFERENCIA-TEMPLATE-OFICIAL.md) | Identificação, integridade e preservação do modelo vigente; **não** criação de novo modelo |
| Registro de vigência e histórico | [`docs/wireframes/images/Registro_Controle_Template_Oficial.md`](../docs/wireframes/images/Registro_Controle_Template_Oficial.md) | Decisões, versões, caminhos, hashes e ativações, sem regras de construção funcional |
| SPEC 3 — utilização nas interfaces | [`wireframes/PROCESSO-TELA-PRANCHA.md`](wireframes/PROCESSO-TELA-PRANCHA.md) | PNG visual da Tela → GI-1 (aprovação visual) → TextFrame derivado → GI-2 (aprovação documental do conjunto) → Prancha de Implementação → GI-4 (aprovação) |

## Contratos auxiliares — sem autoridade concorrente

- [`wireframes/REGRAS-TECNICAS.md`](wireframes/REGRAS-TECNICAS.md) — invariantes técnicas e tokens das representações.
- [`wireframes/WIREFRAME-TEXT.md`](wireframes/WIREFRAME-TEXT.md) — contrato textual da **Prancha do Template** (SPEC 1).
- [`wireframes/MONTAGEM-IMAGEM.md`](wireframes/MONTAGEM-IMAGEM.md) — método de montagem visual da **Prancha do Template** (SPEC 1); a SPEC 3 pode consultar critérios de qualidade sem reabrir Gates do template.
- [`wireframes/WIREFRAME-TEXT-TELA.md`](wireframes/WIREFRAME-TEXT-TELA.md) — contrato do TextFrame individual derivado do PNG visual aprovado em GI-1 (SPEC 3).
- [`wireframes/GATE-IMPLEMENTACAO-TELAS.md`](wireframes/GATE-IMPLEMENTACAO-TELAS.md) — controle de conformidade GI-0 a GI-4 obrigatório na SPEC 3; sem nova autoridade concorrente sobre o template.
- [`docs/wireframes/images/README.md`](../docs/wireframes/images/README.md) — diretórios, nomes, estado e inventário operacional, não autoridade normativa concorrente.
- [`wireframes/README.md`](wireframes/README.md) — índice contextual e caminhos da etapa.

## Regras de precedência e execução

1. Requisitos funcionais vêm exclusivamente do Documento Mestre aprovado. Regras técnicas invariantes vêm de `REGRAS-TECNICAS.md`.
2. SPEC 1 define como construir/validar **um template novo**; SPEC 2 identifica **a referência que está aprovada e vigente**. Nenhuma interface funcional reexecuta os Gates da SPEC 1.
3. SPEC 3 inicia pela análise dos requisitos e **construção do PNG visual isolado da Tela**, aprovado em **GI-1 antes da redação do TextFrame**. O TextFrame documenta fielmente a imagem já aprovada e recebe aprovação em **GI-2**. Cada posição real de rolagem possui seu próprio ViewPort técnico `360 × 800`; os registros prévios GI-0/GI-1 ficam em `telas/controle/`. Depois da aprovação do conjunto visual/documental, o ViewPort é o **primeiro conteúdo substituído** na nova cópia de Prancha, seguindo GI-3/GI-4. Campos PÁGINA/ETAPA, itens 10/14 e aprovação da Prancha pertencem somente à SPEC 3.
4. O registro genérico é a **única fonte da seleção vigente**, e cada saída aponta para o modelo/versão/hash que utilizou. Aprovação histórica não equivale a vigência atual.
5. README, PNG histórico, nome de arquivo ou decisão em conversa não substitui uma aprovação ou norma; inconsistências bloqueiam a execução.

## Alterações

Antes de qualquer mudança, aplicar [`PROCESSO-ALTERACAO-ASSISTIDA.md`](PROCESSO-ALTERACAO-ASSISTIDA.md). A alteração normativa ocorre no documento responsável, nunca em uma cópia paralela da regra no README. Nenhum arquivo congelado é revisado sem justificativa e autorização explícitas.
