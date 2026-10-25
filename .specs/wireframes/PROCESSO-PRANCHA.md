# Wireframes — Processo obrigatório de construção da prancha

## 1. Princípio

A prancha não nasce de um template visual pré-pronto.

Ela nasce de um **canvas vazio** e é construída por etapas sequenciais.

Cada etapa deve ser concluída antes de a próxima definir sua geometria.

Os gates são de dois tipos:

```text
GATE TÉCNICO
→ conclusão por verificação objetiva das specs;
→ não cria uma nova parada para aprovação humana.

GATE DE APROVAÇÃO HUMANA
→ exige decisão explícita do responsável;
→ a execução deve parar em AGUARDANDO APROVAÇÃO.
```

A geometria de uma etapa registrada como `APROVADO E CONGELADO` não pode ser alterada silenciosamente para fazer uma etapa posterior caber.

## 2. Sequência obrigatória

```text
PRANCHA VAZIA
    ↓
TÍTULO / CABEÇALHO
    ↓
APROVAÇÃO E CONGELAMENTO DO TÍTULO
    ↓
VIEWPORT TÉCNICO
    ↓
APROVAÇÃO E CONGELAMENTO DO VIEWPORT
    ↓
CÁLCULO DA ÁREA REAL RESTANTE
    ↓
DEFINIÇÃO DOS DEMAIS ELEMENTOS
    ↓
APROVAÇÃO COMPLETA DO WIREFRAME TEXT
    ↓
CONSTRUÇÃO VISUAL DE TODOS OS ELEMENTOS
    ↓
PNG
    ↓
VALIDAÇÃO PNG × WIREFRAME TEXT
```

## 2.1 Registro obrigatório do estado dos gates

Para que o processo possa continuar em outra conversa ou por outra execução sem memória anterior, o Wireframe Text específico deve registrar explicitamente o estado atual de cada gate.

Estados permitidos:

```text
PENDENTE
EM DEFINIÇÃO
AGUARDANDO APROVAÇÃO
APROVADO E CONGELADO
BLOQUEADO POR GATE ANTERIOR
NÃO APLICÁVEL
```

Significado dos estados:

| Estado | Significado |
|---|---|
| `PENDENTE` | etapa liberada, mas ainda não iniciada |
| `EM DEFINIÇÃO` | etapa em construção, cálculo, revisão ou correção |
| `AGUARDANDO APROVAÇÃO` | trabalho necessário concluído e parado aguardando decisão humana explícita |
| `APROVADO E CONGELADO` | etapa concluída e congelada; em gate técnico significa validação técnica concluída; em gate humano significa aprovação explícita registrada |
| `BLOQUEADO POR GATE ANTERIOR` | etapa não pode avançar porque uma dependência anterior ainda não foi concluída |
| `NÃO APLICÁVEL` | etapa comprovadamente não se aplica ao artefato, com justificativa registrada |

Classificação dos gates:

```text
Gate 1 — Canvas: TÉCNICO
Gate 2 — Título / Cabeçalho: APROVAÇÃO HUMANA
Gate 3 — Viewport Técnico: APROVAÇÃO HUMANA
Gate 4 — Área restante calculada: TÉCNICO
Gate 5 — Demais elementos definidos: TÉCNICO
Gate 6 — Wireframe Text completo: APROVAÇÃO HUMANA
Produção do PNG: EXECUÇÃO + APROVAÇÃO HUMANA FINAL
```

A execução deve parar para decisão humana nos Gates 2, 3 e 6 e na aprovação final do PNG. Os Gates 1, 4 e 5 não criam novas paradas humanas.

Registro mínimo obrigatório:

```text
Gate 1 — Canvas
Gate 2 — Título / Cabeçalho
Gate 3 — Viewport Técnico
Gate 4 — Área restante calculada
Gate 5 — Demais elementos definidos
Gate 6 — Wireframe Text completo
Produção do PNG
```

Regras:

- uma aprovação ocorrida fora do repositório deve ser refletida no Wireframe Text antes de depender dela em outra execução;
- ausência de registro explícito não equivale a aprovação;
- uma etapa somente pode ser tratada como congelada quando seu gate estiver registrado como `APROVADO E CONGELADO`;
- gates técnicos podem evoluir de `PENDENTE` para `EM DEFINIÇÃO` e, quando todos os critérios objetivos forem atendidos, para `APROVADO E CONGELADO` sem criar uma nova aprovação humana;
- gates humanos devem passar por `AGUARDANDO APROVAÇÃO` antes de `APROVADO E CONGELADO`;
- `BLOQUEADO POR GATE ANTERIOR` impede cálculo definitivo das etapas seguintes;
- a existência de coordenadas propostas não equivale à conclusão do gate correspondente;
- se uma etapa congelada for reaberta, ela volta para `EM DEFINIÇÃO` e as etapas dependentes voltam para `BLOQUEADO POR GATE ANTERIOR`;
- a produção do PNG permanece em `BLOQUEADO POR GATE ANTERIOR` até o Gate 6 estar `APROVADO E CONGELADO`.

Estado da produção do PNG:

```text
BLOQUEADO POR GATE ANTERIOR
→ Gate 6 ainda não aprovado

PENDENTE
→ Gate 6 aprovado; produção ainda não iniciada

EM DEFINIÇÃO
→ imagem em construção ou correção

AGUARDANDO APROVAÇÃO
→ PNG construído e validado contra o Wireframe Text

APROVADO E CONGELADO
→ imagem aprovada explicitamente e congelada
```

`NÃO APLICÁVEL` somente pode ser usado quando a produção de PNG realmente não fizer parte do artefato.

---

# 3. Etapa 1 — Criar a prancha vazia

Criar somente:

```text
canvas 1280 × 1920 px
orientação retrato
margens estruturais aplicáveis
```

Nenhum cartão documental, viewport ou bloco deve ser posicionado nesta etapa.

## Gate 1 — validação técnica

Durante a construção, usar `EM DEFINIÇÃO`.

Confirmar:

```text
[ ] canvas correto
[ ] orientação correta
[ ] nenhum elemento antecipado
```

Quando os critérios forem atendidos, registrar:

```text
Gate 1 — Canvas: APROVADO E CONGELADO
```

Essa conclusão é técnica e não exige aprovação humana.

---

# 4. Etapa 2 — Adicionar o título / cabeçalho

O título é o primeiro elemento real da composição.

Antes de posicioná-lo, o Wireframe Text deve definir:

```text
conteúdo exato
x
y
largura
altura
sub-regiões internas
tipografia
alinhamento
padding
divisores
metadados
referências de marca
```

A largura e a altura devem ser calculadas para o conteúdo real do cabeçalho daquela prancha.

Não copiar dimensões de uma prancha anterior apenas porque ela possui cabeçalho semelhante.

## Gate 2 — aprovação humana do título

Enquanto o cabeçalho estiver sendo definido, registrar `EM DEFINIÇÃO`.

Quando a proposta estiver completa, registrar `AGUARDANDO APROVAÇÃO` e parar até existir decisão explícita.

Somente após aprovação explícita:

```text
[ ] conteúdo aprovado
[ ] largura aprovada
[ ] altura aprovada
[ ] posição aprovada
[ ] distribuição interna aprovada
```

o cabeçalho é considerado **congelado**.

A aprovação deve ser registrada no quadro de gates do Wireframe Text específico antes de prosseguir.

Após congelado, a próxima etapa deve trabalhar com o espaço que realmente restou.

---

# 5. Etapa 3 — Definir a posição do VIEWPORT TÉCNICO

O viewport só é posicionado depois do título aprovado.

Invariantes:

```text
viewport físico: 360 × 800 px
escala: 1:1
```

Para a variação atual (`white` ou `black`), usar a referência física específica da mesma variação quando ela existir e for aplicável. A ausência de referência física específica não altera as invariantes técnicas e não autoriza reutilizar por inferência um bitmap da outra variação.

O Wireframe Text deve definir:

```text
arquivo utilizado
x
y
largura = 360 px
altura = 800 px
cotas externas
espaço documental ao redor
relação com o cabeçalho
```

A posição do viewport é uma variável da composição.

A alternativa A, B, C ou qualquer futura composição pode colocá-lo em posição diferente, desde que respeite as regras técnicas.

## Proibição

Não diminuir o viewport para abrir espaço.

Não deslocar o cabeçalho aprovado para abrir espaço.

Não usar geometria de prancha anterior como atalho.

## Gate 3 — aprovação humana do viewport

Enquanto o viewport estiver sendo definido, registrar `EM DEFINIÇÃO`.

Quando a proposta estiver completa, registrar `AGUARDANDO APROVAÇÃO` e parar até existir decisão explícita.

Confirmar:

```text
[ ] posição aprovada
[ ] 360 × 800 físicos
[ ] escala 1:1
[ ] cotas coerentes
[ ] nenhuma invasão do cabeçalho
```

Após aprovação, cabeçalho + viewport ficam congelados. A aprovação do Gate 3 deve estar registrada no Wireframe Text específico antes de calcular a área restante.

---

# 6. Etapa 4 — Calcular a nova área disponível

Somente depois de cabeçalho e viewport congelados deve-se calcular o espaço restante.

O cálculo deve partir de coordenadas reais:

```text
canvas
- margens
- cabeçalho
- viewport
- gaps aprovados
= área documental restante
```

O Wireframe Text deve registrar a área restante com:

```text
x
y
largura
altura
limites
```

Não é permitido partir de uma grade visual presumida e tentar forçar o conteúdo a caber nela.

## Gate 4 — validação técnica da área restante

Durante o cálculo, registrar `EM DEFINIÇÃO`.

Confirmar:

```text
[ ] cálculo parte somente de elementos já congelados
[ ] coordenadas e limites fecham matematicamente
[ ] área restante permanece dentro do canvas
[ ] nenhum elemento congelado foi movido
```

Quando os critérios forem atendidos, registrar `APROVADO E CONGELADO`.

Essa conclusão é técnica e não exige aprovação humana.

---

# 7. Etapa 5 — Definir cada elemento restante

Cada elemento é definido de acordo com:

```text
conteúdo real que precisa mostrar
hierarquia do frame conceitual
área realmente disponível
regras técnicas invariantes
legibilidade
```

Para cada elemento, calcular:

```text
posição
largura
altura
padding
estrutura interna
conteúdo exato
tipografia
componentes demonstrados
gaps
referências normativas
```

## Regra de dimensionamento

O tamanho do cartão documental é consequência do conteúdo.

```text
conteúdo
→ necessidade espacial
→ dimensão do elemento
→ posição no espaço restante
```

Não usar:

```text
dimensão antiga
→ forçar conteúdo dentro
```

## Regra de readequação

Se o conteúdo não couber:

1. não comprimir arbitrariamente;
2. não reduzir o viewport;
3. não alterar silenciosamente o título;
4. recalcular a área do elemento;
5. redistribuir elementos ainda não congelados;
6. registrar o novo cálculo no Wireframe Text;
7. submeter novamente à aprovação quando a alteração afetar composição já aprovada.

## Gate 5 — validação técnica dos demais elementos

Durante a definição, registrar `EM DEFINIÇÃO`.

Confirmar:

```text
[ ] todos os elementos necessários foram definidos
[ ] todos possuem geometria, conteúdo e referências suficientes para reconstrução
[ ] nenhuma área excede os limites calculados
[ ] nenhuma geometria congelada foi alterada silenciosamente
```

Quando os critérios forem atendidos, registrar `APROVADO E CONGELADO`.

Essa conclusão é técnica e não exige aprovação humana.

---

# 8. Etapa 6 — Aprovar o Wireframe Text completo

Antes da imagem, o documento deve permitir reconstruir a prancha sem interpretação livre.

## Gate 6 — aprovação humana do Wireframe Text

Durante a conferência integral, registrar `EM DEFINIÇÃO`.

Confirmar:

```text
[ ] título completamente definido
[ ] viewport completamente definido
[ ] área restante calculada
[ ] todos os elementos posicionados
[ ] todas as dimensões definidas
[ ] todos os conteúdos exatos definidos
[ ] todas as referências técnicas identificadas
[ ] nenhuma medida depende de memória
[ ] nenhuma geometria foi copiada de outra prancha sem justificativa normativa
[ ] não existem lacunas que precisem ser resolvidas durante a geração da imagem
```

Enquanto qualquer item estiver aberto, **não gerar a imagem**.

Quando todos os itens estiverem fechados, registrar `AGUARDANDO APROVAÇÃO` e parar.

Somente após aprovação humana explícita registrar:

```text
Gate 6 — Wireframe Text completo: APROVADO E CONGELADO
Produção do PNG: PENDENTE
```

---


# 9. Etapa 7 — Construir a prancha visual

Depois do Wireframe Text aprovado, partir novamente do canvas vazio e executar exatamente o que foi especificado.

A construção visual deve seguir `MONTAGEM-IMAGEM.md` e consultar o contexto operacional e as referências aplicáveis localizadas por `docs/wireframes/images/README.md`, sem permitir que essas referências sobrescrevam a composição específica já aprovada.

Ao iniciar a construção visual, registrar:

```text
Produção do PNG: EM DEFINIÇÃO
```

```text
1. canvas;
2. título;
3. viewport;
4. cotas;
5. cada elemento documental;
6. conteúdo interno;
7. acabamentos técnicos.
```

A criação visual é execução, não descoberta.

Não decidir novas posições durante a produção da imagem.

---

# 10. Etapa 8 — Validar a imagem

Comparar a imagem produzida com o Wireframe Text.

Validar:

```text
x/y/w/h
conteúdo
ordem
alinhamento
tipografia
medidas
viewport
cotas
componentes
tokens
estados
margens
gaps
```

Se a imagem corresponder ao Wireframe Text, registrar:

```text
Produção do PNG: AGUARDANDO APROVAÇÃO
```

Após aprovação humana explícita da imagem, registrar:

```text
Produção do PNG: APROVADO E CONGELADO
```

Se a imagem revelar que a especificação não funciona:

```text
não corrigir somente a imagem
        ↓
Produção do PNG: EM DEFINIÇÃO
        ↓
corrigir primeiro o Wireframe Text
        ↓
reabrir somente os gates realmente afetados
        ↓
obter nova aprovação quando um gate humano for reaberto
        ↓
gerar novamente
```

## Resultado

O PNG é o resultado visual da especificação aprovada.

Ele não substitui a spec e não cria regra nova por conta própria.
