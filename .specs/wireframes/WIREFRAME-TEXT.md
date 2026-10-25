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
estado
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
componentes demonstrados
ícones
estados
regras específicas
sequência de montagem
gate antes da imagem
checklist de validação
```

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

DEPENDÊNCIA
→ qual etapa anterior precisava estar aprovada

STATUS
→ definido / pendente / aprovado, quando necessário
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
```

## 8. Aprovação progressiva

O Wireframe Text deve refletir o processo de construção:

```text
canvas
→ título
→ aprovação
→ viewport
→ aprovação
→ área restante
→ elementos
→ aprovação integral
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
- geometria copiada por conveniência.

Não gerar PNG enquanto houver decisão geométrica pendente no Wireframe Text.

## 10. Relação com a imagem

```text
Wireframe Text aprovado
        ↓
execução visual
        ↓
PNG
        ↓
validação contra o Wireframe Text
```

Se houver incompatibilidade, corrigir primeiro a especificação e depois regenerar a imagem.
