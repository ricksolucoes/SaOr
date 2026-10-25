# Wireframes — Índice de especificações

Este diretório contém as regras canônicas aplicáveis à etapa de Wireframe Conceitual em Imagem.

## Princípio fundamental

**Não existe um template visual universal de prancha.**

Cada prancha-modelo é uma composição variável.

O que é padronizado é:

```text
- as regras técnicas invariantes;
- a sequência de construção;
- os gates técnicos e os gates de aprovação humana;
- o conjunto mínimo de informações que o Wireframe Text deve registrar;
- a obrigação de recalcular a geometria para o conteúdo real da prancha.
```

Não é padronizado:

```text
- a posição universal do viewport;
- a largura universal dos cartões documentais;
- a quantidade universal de colunas;
- a altura universal dos blocos;
- a geometria específica de uma alternativa;
- a distribuição visual de A, B, C ou futuras composições.
```

## Specs

1. [`REGRAS-TECNICAS.md`](REGRAS-TECNICAS.md)
   - canvas;
   - viewport;
   - grid e spacing;
   - tipografia técnica;
   - tokens;
   - componentes;
   - bordas, radius e elevação;
   - iconografia;
   - estados;
   - acessibilidade estrutural.

2. [`PROCESSO-PRANCHA.md`](PROCESSO-PRANCHA.md)
   - ordem obrigatória de construção;
   - congelamento por etapas;
   - cálculo do espaço restante;
   - aprovação antes da imagem;
   - validação do PNG contra a especificação.

3. [`WIREFRAME-TEXT.md`](WIREFRAME-TEXT.md)
   - função do Wireframe Text;
   - conteúdo mínimo;
   - contrato mínimo por elemento;
   - proibições;
   - relação entre texto, composição e imagem.

## Regra de uso

Antes de criar ou alterar um Wireframe Text:

```text
1. identificar a variação da prancha-modelo (`white` ou `black`) na estrutura operacional;
2. ler REGRAS-TECNICAS.md;
3. executar PROCESSO-PRANCHA.md;
4. registrar o resultado em conformidade com WIREFRAME-TEXT.md;
5. somente depois produzir a imagem.
```

A localização física das referências e das pranchas-modelo é definida em:

```text
docs/wireframes/images/README.md
```

Referências específicas de `white` e `black` não devem ser misturadas. Referências neutras compartilhadas podem permanecer diretamente em `docs/wireframes/images/references/`.
