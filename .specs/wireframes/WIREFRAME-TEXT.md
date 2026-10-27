# Wireframe Text — Especificação documental

## 1. Função

O Wireframe Text é a especificação reproduzível de uma prancha específica.

Ele deve permitir que outra execução construa a imagem sem depender de:

- memória;
- conversa anterior;
- tentativa visual;
- aproximação;
- interpretação de imagem histórica.

## 2. Não é um template visual

Não existe uma geometria universal obrigatória para todos os Wireframe Text.

O documento específico pode organizar seus tópicos conforme a composição que está descrevendo.

O que é obrigatório é o **conteúdo mínimo e a ordem de decisão**, não uma distribuição visual fixa.

Para pranchas-modelo, a variação (`white` ou `black`) também deve ser explícita. A localização operacional é definida em `docs/wireframes/images/README.md`.

## 3. O frame conceitual inicial

Quando uma prancha possui uma reprodução textual inicial aprovada, ela registra a intenção de composição:

```text
quais regiões existem
quais elementos estão próximos
quais elementos ficam lado a lado
ordem visual
hierarquia
```

Essa reprodução:

- não deve ser alterada silenciosamente;
- não é automaticamente uma escala de caracteres para pixels;
- orienta o cálculo específico da prancha;
- deve ser reconciliada com as regras técnicas vigentes antes da imagem.

## 4. Conteúdo mínimo do Wireframe Text específico

O documento deve registrar, quando aplicável:

```text
identificação e versão
variação da prancha-modelo: white ou black
estado do artefato
estado dos gates do processo
estado da produção do PNG
conceito de composição
canvas
cabeçalho
viewport
arquivo de viewport utilizado
cotas
mapa das regiões calculadas
posição e dimensão de cada elemento
conteúdo textual exato
tipografia
tokens técnicos usados
paleta técnica da variação e pares texto/fundo (seção 4.2)
componentes demonstrados
ícones
estados
regras específicas
sequência de montagem
gate antes da imagem
checklist de validação
```

## 4.1 Estado obrigatório do processo

Todo Wireframe Text específico deve permitir que uma execução nova determine, sem consultar conversa anterior, em qual etapa o trabalho está.

Deve registrar:

```text
Gate 1 — Canvas: <ESTADO>
Gate 2 — Título / Cabeçalho: <ESTADO>
Gate 3 — Viewport Técnico: <ESTADO>
Gate 4 — Área restante calculada: <ESTADO>
Gate 5 — Demais elementos definidos: <ESTADO>
Gate 6 — Wireframe Text completo: <ESTADO>
Produção do PNG: <ESTADO>
```

Os estados válidos são definidos em `PROCESSO-PRANCHA.md` e são exclusivamente:

```text
PENDENTE
EM DEFINIÇÃO
AGUARDANDO APROVAÇÃO
APROVADO E CONGELADO
BLOQUEADO POR GATE ANTERIOR
NÃO APLICÁVEL
```

Classificação:

```text
Gate 1 — Canvas: TÉCNICO
Gate 2 — Título / Cabeçalho: APROVAÇÃO HUMANA
Gate 3 — Viewport Técnico: APROVAÇÃO HUMANA
Gate 4 — Área restante calculada: TÉCNICO
Gate 5 — Demais elementos definidos: TÉCNICO
Gate 6 — Wireframe Text completo: APROVAÇÃO HUMANA
```

Gates técnicos não criam novas paradas humanas quando seus critérios objetivos forem atendidos. Gates humanos devem parar em `AGUARDANDO APROVAÇÃO`.

Se uma aprovação não estiver registrada no próprio Wireframe Text, uma nova execução deve tratá-la como não comprovada e não pode inferi-la a partir de memória, conversa, commit ou existência de medidas posteriores.

## 4.2 Cores no Wireframe Text

A fonte única das cores é `REGRAS-TECNICAS.md`, seção 6. O Wireframe Text deve:

```text
citar as cores pelo nome do token;
registrar o HEX somente no bloco de paleta;
manter o bloco de paleta como cópia da tabela vigente da variação (white ou black),
  com a indicação da revisão da seção 6 usada;
listar cada par texto/fundo usado e a razão de contraste correspondente da tabela;
registrar qualquer exceção de nível (AA onde o alvo é AAA) já prevista na tabela.
```

Cor que não esteja na tabela vigente é lacuna: não entra no Wireframe Text até ser definida e aprovada em `REGRAS-TECNICAS.md`.

---

## 5. Contrato mínimo por elemento

Para cada elemento visual da prancha, registrar o que for aplicável:

```text
NOME
→ identificação inequívoca

FUNÇÃO NA PRANCHA
→ por que o elemento existe

CONTEÚDO EXATO
→ texto, valores, rótulos e itens

ÁREA
→ x
→ y
→ largura
→ altura

ESTRUTURA INTERNA
→ padding
→ alinhamento
→ linhas
→ colunas
→ gaps
→ ordem de leitura

TIPOGRAFIA / TOKENS
→ somente os que realmente forem usados

COMPONENTES / ÍCONES
→ somente os que realmente forem demonstrados

REFERÊNCIA
→ spec ou documento que sustenta a decisão
→ referência física da mesma variação, quando aplicável

DEPENDÊNCIA
→ qual etapa anterior precisava estar `APROVADO E CONGELADO`

STATUS
→ usar um dos estados canônicos quando o elemento precisar de acompanhamento próprio
```

Isso é um contrato documental; **não é um template de layout**.

## 6. Geometria específica

Toda coordenada ou dimensão que não seja uma regra técnica invariável deve ser tratada como específica daquela prancha.

O documento deve deixar claro quando uma medida significa:

```text
REGRA NORMATIVA
ou
GEOMETRIA DESTA PRANCHA
```

Exemplo:

```text
viewport 360 × 800
→ regra normativa

x = 40 / y = 224
→ posição específica de uma prancha
```

## 7. Recalcular, não copiar

É proibido usar a geometria de uma prancha anterior como fonte automática de medidas.

A nova prancha deve calcular sua geometria a partir de:

```text
canvas vigente
elementos já congelados
conteúdo real
área restante
regras técnicas
conceito da composição atual
variação atual
```

Para pranchas-modelo, os arquivos ficam separados por variação:

```text
docs/wireframes/images/references/templates/white/
docs/wireframes/images/references/templates/black/
```

O Wireframe Text correspondente fica em `wiframetext/` dentro da mesma variação. Referências específicas de `white` e `black` não devem ser misturadas por inferência.

### 7.1 Variação black derivada de uma white aprovada

Um Wireframe Text `black` pode ser derivado de um Wireframe Text `white` **somente quando o `black` registrar, no próprio documento**:

```text
- o Wireframe Text white de origem (nome e versão) e seu estado (APROVADO E CONGELADO);
- a regra: geometria e composição herdadas; mudam apenas paleta, ativos físicos e as
  decisões que dependem da paleta (por exemplo, sombra que não é perceptível sobre fundo escuro);
- cada diferença em relação ao white, classificada como DIFERENÇA INTENCIONAL.
```

Regras:

- a geometria herdada continua `GEOMETRIA DESTA PRANCHA`, e não passa a regra normativa;
- tokens `WF-B-*`, viewport e cabeçalho (logo para fundos escuros) são os da variação `black`; nenhum ativo ou bitmap `white` é reutilizado;
- os gates **não são herdados**: o `black` começa em `PENDENTE` e registra seus próprios estados, e os Gates 2, 3 e 6 voltam a exigir aprovação humana;
- a numeração do `black` é própria (primeira versão = `v01`), independente da versão `white` de origem.

## 8. Aprovação progressiva

O Wireframe Text deve refletir o processo de construção:

```text
canvas
→ validação técnica
→ título
→ aprovação humana
→ viewport
→ aprovação humana
→ área restante
→ validação técnica
→ elementos
→ validação técnica
→ aprovação humana integral do Wireframe Text
→ imagem
```

Uma etapa posterior não pode reescrever silenciosamente a geometria de uma etapa aprovada.

## 9. Proibições

Não registrar como regra:

- memória de conversa;
- tentativa descartada;
- raciocínio interno;
- medida inferida de raster histórico;
- escolha visual não aprovada;
- funcionalidade inexistente;
- geometria copiada por conveniência;
- mistura implícita de referências específicas de `white` e `black`;
- estado de processo fora do conjunto canônico;
- cor fora das tabelas vigentes de `REGRAS-TECNICAS.md`, seção 6;
- HEX de cor fora do bloco de paleta;
- ajuste de token dentro do Wireframe Text (a inconsistência volta para `REGRAS-TECNICAS.md`).

Não gerar PNG enquanto o Gate 6 não estiver `APROVADO E CONGELADO`.

## 10. Relação com a imagem

```text
Wireframe Text aprovado
        ↓
Produção do PNG: PENDENTE
        ↓
execução visual
Produção do PNG: EM DEFINIÇÃO
        ↓
PNG
        ↓
validação contra o Wireframe Text
        ↓
Produção do PNG: AGUARDANDO APROVAÇÃO
        ↓
aprovação explícita
        ↓
Produção do PNG: APROVADO E CONGELADO
```

Se houver incompatibilidade, corrigir primeiro a especificação e depois regenerar a imagem.
