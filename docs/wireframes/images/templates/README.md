# SaOr - Sales Order
## Pranchas-modelo — governança, organização e ciclo de vida

**Diretório:** `docs/wireframes/images/templates/`  
**Specs canônicas:** [`../../../../.specs/wireframes/README.md`](../../../../.specs/wireframes/README.md)  
**Controle operacional:** [`../README.md`](../README.md)

---

# 1. Responsabilidade deste documento

Este README é a fonte de governança das pranchas-modelo.

Ele define somente:

- estrutura das referências, alternativas e aprovados;
- vínculo entre PNG e Wireframe Text;
- estados documentais;
- critérios mínimos de avaliação;
- preservação e versionamento;
- seleção, combinação e promoção;
- congelamento da composição aprovada;
- gate que libera os wireframes funcionais.

Dimensões, viewport, grid, tokens, tipografia, componentes, elevação, iconografia e demais regras técnicas pertencem às specs canônicas em `.specs/wireframes/`.

O processo obrigatório de construção da prancha e o padrão documental do Wireframe Text também pertencem a `.specs/wireframes/`.

---

# 2. Estrutura

```text
templates/
├── README.md
├── references/
│   ├── Especificação Técnica - Prancha de Trabalho.png
│   ├── Especificação Técnica do Viewport Mobile.png
│   └── WF-VIEWPORT-360x800-clean.png
├── alternatives/
│   ├── <prancha-em-avaliação>.png
│   └── wiframetext/
│       └── <mesmo-nome-base>.md
└── aprovados/
    ├── <prancha-aprovada>.png
    └── wiframetext/
        └── <mesmo-nome-base>.md
```

## 2.1 `references/`

Contém somente referências técnicas compartilhadas.

Esses arquivos:

- não são alternativas;
- não recebem status de aprovação de template;
- não são copiados para `alternatives/` ou `aprovados/`;
- são usados conforme a função normativa definida em `.specs/wireframes/REGRAS-TECNICAS.md`.

## 2.2 `alternatives/`

Contém pranchas-modelo que ainda não constituem a composição aprovada da etapa.

Podem permanecer aqui artefatos:

```text
HISTÓRICO
PENDENTE DE PRODUÇÃO
EM VALIDAÇÃO
AJUSTES NECESSÁRIOS
CANDIDATA
REJEITADA
SUPERADA
```

A imagem fica diretamente em `alternatives/`. O Wireframe Text correspondente, quando exigido, fica em `alternatives/wiframetext/`.

## 2.3 `aprovados/`

Contém somente pranchas-modelo com aprovação explícita.

A imagem fica diretamente em `aprovados/` e o Wireframe Text correspondente em `aprovados/wiframetext/`.

Um artefato somente entra em `aprovados/` quando o par PNG + Wireframe Text estiver compatível com as specs canônicas vigentes em `.specs/wireframes/`.

---

# 3. Estados e significado

| Estado | Significado |
|---|---|
| `HISTÓRICO` | versão preservada para auditoria; não é referência vigente |
| `PENDENTE DE PRODUÇÃO` | conceito autorizado, mas ainda sem artefato produzido |
| `EM VALIDAÇÃO` | artefato produzido e em revisão |
| `AJUSTES NECESSÁRIOS` | revisão encontrou correções obrigatórias |
| `CANDIDATA` | alternativa validada para participar da escolha final |
| `REJEITADA` | avaliada e não aceita para prosseguir |
| `SUPERADA` | preservada, mas substituída por versão ou abordagem posterior |
| `APROVADA` | composição explicitamente escolhida, validada e promovida para `aprovados/` |

Regras:

- `CANDIDATA` não significa `APROVADA`;
- silêncio não constitui aprovação;
- uma alternativa não pode ser promovida apenas por estar tecnicamente correta;
- `APROVADA` exige decisão explícita do responsável.

---

# 4. Pareamento PNG ↔ Wireframe Text

Toda nova prancha-modelo ou nova versão produzida após a adoção desta regra deve possuir Wireframe Text antes de ser considerada pronta para avaliação final.

Pareamento pelo mesmo nome-base:

```text
alternatives/WF-TEMPLATE-X_v01.png
alternatives/wiframetext/WF-TEMPLATE-X_v01.md
```

O mesmo padrão vale em `aprovados/`.

O Wireframe Text registra somente a composição específica da prancha e deve cumprir:

```text
../../../../.specs/wireframes/PROCESSO-PRANCHA.md
../../../../.specs/wireframes/WIREFRAME-TEXT.md
```

Não existe template visual universal de prancha.

Cada composição deve ser calculada a partir do canvas vazio, congelando título e viewport antes de calcular e posicionar os demais elementos.

Não registrar conversa, memória de processo, tentativas descartadas, raciocínio interno ou histórico narrativo desnecessário.

---

# 5. Regra de transição para artefatos anteriores

`WF-TEMPLATE-A_v01.png` e `WF-TEMPLATE-A_v02.png` foram produzidos antes da exigência do Wireframe Text e antes da consolidação do canvas técnico vigente.

Por isso:

- permanecem preservados;
- não precisam ser regenerados somente para satisfazer retroativamente a nova estrutura;
- mantêm seu valor histórico e o estado de decisão já alcançado;
- não podem ser movidos diretamente para `aprovados/` como se já cumprissem a especificação atual.

Se uma alternativa anterior for escolhida para aprovação final, deve ser gerada **nova versão** compatível com:

- as specs canônicas vigentes em `.specs/wireframes/`;
- o canvas vigente;
- as referências técnicas vigentes;
- o Wireframe Text correspondente.

A nova versão é então avaliada antes de qualquer promoção para `aprovados/`.

---

# 6. Estado conhecido das alternativas

| Artefato | Estado | Função atual |
|---|---|---|
| `WF-TEMPLATE-A_v01.png` | `HISTÓRICO` | primeira proposta preservada |
| `WF-TEMPLATE-A_v02.png` | `CANDIDATA` | alternativa A validada para comparação em 24/10/2026 |
| Alternativa B | `PENDENTE DE PRODUÇÃO` | depende da governança e do Wireframe Text antes de nova geração |
| Alternativa C | `PENDENTE DE PRODUÇÃO` | ainda não produzida |

O estado acima registra decisões já tomadas. Ele não autoriza produzir, aprovar ou promover automaticamente qualquer alternativa.

## 6.1 Conceitos fixos das alternativas

Os identificadores A, B e C representam conceitos de composição já definidos e não podem ser reinterpretados silenciosamente:

- **A — viewport central dominante:** viewport como elemento visual principal; cabeçalho técnico na região superior; especificações distribuídas nas áreas restantes.
- **B — viewport à esquerda + painel técnico à direita:** viewport à esquerda em escala `1:1`; documentação técnica principal organizada em coluna lateral direita.
- **C — viewport superior + documentação inferior:** viewport na região superior/central; documentação técnica organizada predominantemente abaixo.

A produção de uma nova versão pode corrigir execução, legibilidade ou conformidade técnica, mas não muda o conceito da alternativa sem decisão explícita.

## 6.2 Ordem vigente de avaliação

A sequência vigente é:

```text
A_v01 — histórico preservado
        ↓
A_v02 — CANDIDATA
        ↓
Alternativa B — próxima produção
        ↓
avaliação da B
        ↓
Alternativa C
        ↓
avaliação da C
        ↓
comparação técnica A × B × C
        ↓
decisão explícita
```

A sequência organiza a avaliação e não autoriza gerar automaticamente a etapa seguinte.

---

# 7. Conteúdo de demonstração das pranchas-modelo

Pranchas-modelo não devem utilizar T00 nem outra interface funcional T/M/E como conteúdo de teste.

Podem usar conteúdo neutro e controlado para demonstrar:

- título e texto;
- campo;
- botões;
- item de lista;
- ícones;
- card;
- estados;
- scroll/continuidade;
- paginação documental.

Esse conteúdo não cria requisito funcional e não altera a baseline.

---

# 8. Critérios mínimos de avaliação

Toda alternativa deve cumprir integralmente as specs canônicas em `.specs/wireframes/`.

Além disso, deve ser avaliada quanto a:

1. viewport preservado fisicamente e sem invasão documental;
2. metadados legíveis;
3. espaço suficiente para os tokens e especificações realmente necessários;
4. tipografia documental legível;
5. identificação clara de página e versão;
6. capacidade de representar scroll/continuidade quando necessário;
7. equivalência geométrica entre Claro e Escuro;
8. funcionamento para página única e multipágina;
9. ausência de compactação que prejudique leitura;
10. reprodução consistente a partir do Wireframe Text;
11. ausência de informação redundante de conversa ou processo;
12. preservação das decisões técnicas vigentes sem regressão silenciosa.

A comparação deve registrar fatos observáveis. Preferência estética isolada não é critério suficiente.

## 8.1 Comparação final obrigatória

Antes de qualquer aprovação final, o resultado das alternativas avaliadas deve ser consolidado de forma objetiva.

O registro mínimo da comparação deve indicar, para cada alternativa:

```text
estado final da avaliação
critérios atendidos
critérios não atendidos
regressões identificadas
restrições relevantes
conclusão
```

A escolha final deve ser rastreável até essa comparação. Não é permitido aprovar uma alternativa sem que o resultado comparativo das alternativas efetivamente avaliadas esteja registrado.

Alternativa ainda não produzida ou não avaliada deve ser marcada como `NÃO AVALIADA`; não deve receber pontuação ou conclusão presumida.

---

# 9. Seleção e combinação

Depois de avaliar as alternativas, as decisões permitidas são:

```text
APROVAR UMA ALTERNATIVA
SOLICITAR NOVA VERSÃO DE UMA ALTERNATIVA
COMBINAR PARTES EXPLICITAMENTE IDENTIFICADAS
MANTER TODAS PENDENTES
```

Nenhuma seleção ou combinação pode ser inferida automaticamente.

Se houver combinação, devem ser definidos explicitamente:

```text
origem estrutural
origem do cabeçalho
origem da posição do viewport
origem da distribuição documental
outros elementos incorporados
motivo da combinação
```

A combinação resulta em uma nova versão que também deve possuir Wireframe Text e passar por avaliação antes da aprovação.

---

# 10. Promoção para `aprovados/`

Quando uma prancha for aprovada, mover o par:

```text
<nome>.png
wiframetext/<nome>.md
```

de `alternatives/` para `aprovados/`.

Não manter duas cópias canônicas do mesmo par nas duas pastas.

Alternativas não aprovadas permanecem preservadas em `alternatives/` com seu estado documental correspondente.

---

# 11. Congelamento

Após a aprovação:

- o PNG aprovado é congelado naquela versão;
- o Wireframe Text correspondente é congelado naquela versão;
- as coordenadas, regiões, textos e composição descritos pelo par tornam-se a referência documental aprovada da etapa;
- nenhuma melhoria, reorganização ou regeneração pode substituir silenciosamente a versão aprovada;
- qualquer mudança posterior exige nova versão e nova aprovação.

A pasta `aprovados/` contém somente artefatos que já passaram por esse processo.

---

# 12. Preservação

- não sobrescrever versão preservada;
- não excluir alternativa apenas porque outra foi aprovada;
- não apagar histórico necessário para explicar a decisão;
- não promover PNG sem Wireframe Text quando a regra já for aplicável à versão;
- não promover Wireframe Text sem o PNG correspondente;
- não transformar artefato histórico em referência vigente apenas por conveniência;
- não regenerar artefato histórico somente porque a especificação técnica evoluiu.

---

# 13. Gate antes dos wireframes funcionais

A produção definitiva das interfaces funcionais começa somente depois de existir uma composição documental aprovada e congelada.

```text
specs canônicas estabilizadas
        ↓
alternativas avaliadas
        ↓
decisão explícita
        ↓
PNG + Wireframe Text compatíveis com a regra vigente
        ↓
par promovido para aprovados/
        ↓
composição congelada
        ↓
T00 Claro
        ↓
T00 Escuro
```

Enquanto não houver um par aprovado e congelado em `aprovados/`, T00 e as demais interfaces permanecem pendentes para produção definitiva.

## 13.1 Checklist final do gate

Antes de liberar T00, todos os itens abaixo devem estar confirmados:

```text
[ ] specs canônicas vigentes aplicadas
[ ] alternativas previstas para a decisão foram avaliadas ou formalmente dispensadas
[ ] comparação final registrada
[ ] decisão final explícita registrada
[ ] PNG e Wireframe Text possuem o mesmo nome-base e versão
[ ] composição reproduzível a partir do Wireframe Text
[ ] viewport e canvas validados fisicamente
[ ] cabeçalho e regiões documentais validados
[ ] cotas do viewport representáveis sem conflito e sem reserva fixa de safe area
[ ] página/versão, scroll e continuidade representáveis
[ ] página única e multipágina suportadas
[ ] equivalência geométrica Claro/Escuro preservada
[ ] par final promovido para `aprovados/`
[ ] composição final congelada
```

Se qualquer item obrigatório permanecer pendente, o gate continua aberto e a produção funcional definitiva não é liberada.

---

# 14. Relação com os wireframes funcionais

As pranchas-modelo:

- não representam interface funcional T/M/E;
- não entram na contagem mínima Claro/Escuro;
- não alteram a baseline funcional;
- não substituem os Textframes do Documento Mestre;
- definem somente a composição documental usada para representar os wireframes na etapa atual.
