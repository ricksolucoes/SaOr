# SaOr — Especificações canônicas

A pasta `.specs/` concentra especificações normativas reutilizáveis do projeto.

Ela existe para impedir que regras técnicas e processos de construção sejam reinterpretados a partir de:

- memória de conversa;
- imagens históricas;
- versões anteriores de artefatos;
- decisões implícitas;
- cópias parciais de README.

## Autoridade

Para os wireframes, a autoridade é:

```text
docs/Documento_Mestre.md
→ conteúdo e comportamento funcional

.specs/wireframes/REGRAS-TECNICAS.md
→ invariantes técnicos da representação

.specs/wireframes/PROCESSO-PRANCHA.md
→ sequência obrigatória de construção e gates

.specs/wireframes/WIREFRAME-TEXT.md
→ contrato documental de cada Wireframe Text específico

Wireframe Text específico
→ composição particular daquela prancha

.specs/wireframes/MONTAGEM-IMAGEM.md
→ leitura contextual e método de execução visual profissional da composição aprovada

docs/wireframes/images/README.md
→ localização operacional das referências técnicas, visuais e pranchas-modelo vigentes

PNG correspondente
→ resultado visual da especificação aprovada dentro do contexto vigente
```

Um nível inferior não altera silenciosamente uma regra de nível superior.

## Índice

- [`wireframes/README.md`](wireframes/README.md) — índice das specs de wireframe.
- [`wireframes/REGRAS-TECNICAS.md`](wireframes/REGRAS-TECNICAS.md) — regras técnicas invariantes.
- [`wireframes/PROCESSO-PRANCHA.md`](wireframes/PROCESSO-PRANCHA.md) — processo sequencial de construção.
- [`wireframes/WIREFRAME-TEXT.md`](wireframes/WIREFRAME-TEXT.md) — padrão documental dos Wireframe Text.
- [`wireframes/MONTAGEM-IMAGEM.md`](wireframes/MONTAGEM-IMAGEM.md) — leitura contextual e montagem visual profissional das imagens aprovadas.

## Regra de alteração

Uma mudança normativa deve ser feita primeiro na spec canônica correspondente.

READMEs operacionais podem apontar para a spec, resumir responsabilidade local ou registrar estado, mas não devem criar uma segunda definição conflitante da mesma regra.
