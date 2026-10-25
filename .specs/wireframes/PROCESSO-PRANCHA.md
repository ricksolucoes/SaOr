# Wireframes — Processo obrigatório de construção da prancha

## 1. Princípio

A prancha não nasce de um template visual pré-pronto.

Ela nasce de um **canvas vazio** e é construída por etapas sequenciais.

Cada etapa deve ser aprovada antes de a próxima definir sua geometria.

A geometria de uma etapa já aprovada não pode ser alterada silenciosamente para fazer uma etapa posterior caber.

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

---

# 3. Etapa 1 — Criar a prancha vazia

Criar somente:

```text
canvas 1280 × 1920 px
orientação retrato
margens estruturais aplicáveis
```

Nenhum cartão documental, viewport ou bloco deve ser posicionado nesta etapa.

## Gate 1

Confirmar:

```text
[ ] canvas correto
[ ] orientação correta
[ ] nenhum elemento antecipado
```

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

## Gate 2 — aprovação do título

Somente após aprovação explícita:

```text
[ ] conteúdo aprovado
[ ] largura aprovada
[ ] altura aprovada
[ ] posição aprovada
[ ] distribuição interna aprovada
```

o cabeçalho é considerado **congelado**.

Após congelado, a próxima etapa deve trabalhar com o espaço que realmente restou.

---

# 5. Etapa 3 — Definir a posição do VIEWPORT TÉCNICO

O viewport só é posicionado depois do título aprovado.

Invariantes:

```text
viewport físico: 360 × 800 px
escala: 1:1
```

Para prancha-modelo neutra, usar o bitmap oficial quando aplicável.

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

## Gate 3 — aprovação do viewport

Confirmar:

```text
[ ] posição aprovada
[ ] 360 × 800 físicos
[ ] escala 1:1
[ ] cotas coerentes
[ ] nenhuma invasão do cabeçalho
```

Após aprovação, cabeçalho + viewport ficam congelados.

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

---

# 8. Etapa 6 — Aprovar o Wireframe Text completo

Antes da imagem, o documento deve permitir reconstruir a prancha sem interpretação livre.

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

---

# 9. Etapa 7 — Construir a prancha visual

Depois do Wireframe Text aprovado, partir novamente do canvas vazio e executar exatamente o que foi especificado:

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

Se a imagem revelar que a especificação não funciona:

```text
não corrigir somente a imagem
        ↓
corrigir primeiro o Wireframe Text
        ↓
aprovar a correção
        ↓
gerar novamente
```

## Resultado

O PNG é o resultado visual da especificação aprovada.

Ele não substitui a spec e não cria regra nova por conta própria.
