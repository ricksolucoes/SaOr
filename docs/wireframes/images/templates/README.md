# SaOr - Sales Order
## Registro das pranchas técnicas-modelo

**Diretório:** `docs/wireframes/images/templates/`  
**Finalidade:** preservar, comparar, selecionar, versionar e auditar as alternativas de prancha técnica utilizadas na etapa de Wireframe Conceitual em Imagem.  
**Documento superior:** `../README.md`

---

# 1. Regra de preservação

As pranchas-modelo são artefatos de decisão.

Elas devem permanecer no repositório mesmo quando:

- forem rejeitadas;
- forem superadas;
- outra alternativa for aprovada;
- partes de mais de uma alternativa forem combinadas no modelo oficial.

A finalidade é permitir consulta futura sobre:

- quais opções foram consideradas;
- quais problemas foram encontrados;
- por que determinada composição foi escolhida;
- de qual alternativa surgiu o modelo oficial.

A aprovação de um template **não autoriza apagar as alternativas**.

---

# 2. Estrutura

```text
templates/
├── README.md
├── alternatives/
│   ├── .gitkeep
│   ├── WF-TEMPLATE-A_v01.png
│   ├── WF-TEMPLATE-A_v02.png
│   ├── WF-TEMPLATE-B_v01.png
│   └── WF-TEMPLATE-C_v01.png
└── official/
    ├── .gitkeep
    └── WF-TEMPLATE-OFFICIAL_v01.png
```

`alternatives/` e `official/` possuem finalidades diferentes e não devem ser misturados.

---

# 3. Convenções de nomes

Alternativas:

```text
WF-TEMPLATE-<LETRA>_v<VERSÃO>.png
```

Exemplos:

```text
WF-TEMPLATE-A_v01.png
WF-TEMPLATE-A_v02.png
WF-TEMPLATE-B_v01.png
```

Modelo oficial:

```text
WF-TEMPLATE-OFFICIAL_v<VERSÃO>.png
```

Exemplo:

```text
WF-TEMPLATE-OFFICIAL_v01.png
```

Uma nova versão nunca substitui fisicamente a anterior.

---

# 4. Estados das alternativas

Estados permitidos:

```text
PENDENTE DE PRODUÇÃO
EM VALIDAÇÃO
AJUSTES NECESSÁRIOS
CANDIDATA
REJEITADA
SUPERADA
SELECIONADA
```

`CANDIDATA` significa que a alternativa foi validada para participar da comparação final entre A/B/C.  
`SELECIONADA` somente pode ser usada depois da comparação final e de decisão explícita do responsável.

`REJEITADA` e `SUPERADA` não significam exclusão do arquivo.

---

# 5. Estado do modelo oficial

Estados permitidos:

```text
NÃO DEFINIDO
EM VALIDAÇÃO
AJUSTES NECESSÁRIOS
APROVADO
SUPERADO POR NOVA VERSÃO
```

Somente declaração explícita do responsável pode definir `APROVADO`.

---

# 6. Alternativa A — viewport central dominante

**Versão histórica:** `alternatives/WF-TEMPLATE-A_v01.png`  
**Versão validada para comparação:** `alternatives/WF-TEMPLATE-A_v02.png`  
**Status atual da alternativa:** `CANDIDATA`

Conceito:

- viewport `360 × 800 px` como elemento visual dominante;
- escala rigorosa `1:1`;
- cabeçalho técnico na região superior;
- metadados e especificações distribuídos nas áreas restantes;
- prioridade visual para a interface.

Resultado da avaliação:

- a v01 permanece preservada como histórico da primeira proposta;
- a v02 incorpora os ajustes realizados durante a avaliação da Alternativa A;
- a v02 foi validada explicitamente pelo responsável em 24/10/2026;
- a alternativa A passa a `CANDIDATA` para comparação posterior com B e C;
- a validação da A não significa que ela já foi `SELECIONADA` como template oficial.

Registro:

```text
Data da validação: 24/10/2026
Arquivo validado: alternatives/WF-TEMPLATE-A_v02.png
Versão: v02
Status anterior: EM VALIDAÇÃO
Status novo: CANDIDATA
Decisão: Alternativa A validada para comparação com B e C.
Observação: v01 preservada como histórico; v02 é a referência vigente da Alternativa A.
```

---

# 7. Alternativa B — viewport à esquerda + painel técnico à direita

**Arquivo planejado:** `alternatives/WF-TEMPLATE-B_v01.png`  
**Status atual:** `PENDENTE DE PRODUÇÃO`  
**Próxima alternativa autorizada para produção:** **SIM**

Conceito:

- viewport à esquerda;
- escala rigorosa `1:1`;
- painel técnico vertical à direita;
- interface e especificação simultaneamente visíveis.

Regra de não regressão em relação à A validada:

- B deve herdar as decisões técnicas e visuais já validadas em `WF-TEMPLATE-A_v02.png`;
- B não deve reabrir tipografia, paleta, componentes, estados, safe areas, medidas, radius, elevação, iconografia, metadados ou regras multipágina;
- a diferença deliberada da B é a **composição documental**: viewport à esquerda + painel técnico principal à direita;
- qualquer outra mudança exige justificativa explícita antes de ser incorporada.

Objetivo da avaliação:

- verificar legibilidade de uma coluna técnica lateral;
- testar leitura comparativa interface/especificação;
- confirmar que o viewport não perde prioridade excessivamente.

Registro:

```text
Data da produção:
Arquivo:
Versão:
Status após avaliação:
Pontos positivos:
Problemas encontrados:
Ajustes solicitados:
Decisão:
```

---

# 8. Alternativa C — viewport superior + documentação inferior

**Arquivo planejado:** `alternatives/WF-TEMPLATE-C_v01.png`  
**Status atual:** `PENDENTE DE PRODUÇÃO`

Conceito:

- viewport na região superior/central;
- escala rigorosa `1:1`;
- blocos documentais na região inferior;
- leitura predominantemente vertical.

Objetivo da avaliação:

- verificar se a documentação inferior comporta todos os dados;
- testar clareza da leitura vertical;
- confirmar que o modelo funciona para páginas únicas e multipágina.

Registro:

```text
Data da produção:
Arquivo:
Versão:
Status após avaliação:
Pontos positivos:
Problemas encontrados:
Ajustes solicitados:
Decisão:
```

---

# 9. Ordem de produção

Estado atual:

```text
1. WF-TEMPLATE-A_v01 — produzido / histórico
2. WF-TEMPLATE-A_v02 — CANDIDATA
3. WF-TEMPLATE-B_v01 — PRÓXIMA PRODUÇÃO
4. avaliação da B
5. WF-TEMPLATE-C_v01
6. avaliação da C
7. comparação técnica A × B × C
8. escolha explícita
```

Motivo da produção sequencial:

- defeitos objetivos descobertos cedo não devem ser repetidos;
- decisões já validadas devem ser preservadas;
- aprendizados de legibilidade podem ser aplicados às alternativas seguintes;
- o conceito próprio de cada alternativa deve ser preservado;
- nenhuma nova alternativa pode regredir decisões já aceitas sem justificativa explícita.

---

# 10. Conteúdo de demonstração

As pranchas-modelo não utilizarão T00 nem outra interface funcional como conteúdo de teste.

Podem utilizar amostras neutras e controladas para verificar espaço e legibilidade, por exemplo:

- título;
- texto;
- campo Outlined;
- botões;
- item de lista;
- ícone;
- card;
- estado disabled;
- estado error;
- indicador de scroll.

Essas amostras não criam requisitos funcionais e não pertencem às 71 interfaces.

---

# 11. Critérios obrigatórios de avaliação

Cada alternativa deve ser medida quanto aos seguintes critérios:

```text
01. viewport exatamente 360 × 800 px
02. escala exatamente 1:1
03. nenhuma legenda invade o viewport
04. metadados permanecem legíveis
05. tokens cromáticos cabem de forma legível
06. especificação tipográfica cabe integralmente
07. observações técnicas possuem área utilizável
08. página XX/YY fica claramente identificável
09. versão vNN fica claramente identificável
10. scroll/continuidade pode ser representado
11. Claro/Escuro podem usar exatamente as mesmas coordenadas
12. template funciona para uma página e para multipágina
```

Também devem ser observados:

- consistência com canvas `1024 × 1536 px`;
- respeito, na prancha-modelo, às safe areas de referência do wireframe (`24 px` superior / `32 px` inferior);
- ausência de interpretação dessas safe areas como paddings ou constantes obrigatórias da implementação;
- ausência de redução do viewport;
- ausência de fonte documental ilegível;
- capacidade de congelar coordenadas para reprodução posterior;
- preservação das decisões já validadas em alternativas anteriores, exceto quando a própria diferença conceitual da alternativa exigir mudança.

As safe areas avaliadas nas pranchas são **referências documentais desta etapa**. Elas não determinam os insets finais do produto. Na implementação futura, superfícies visuais poderão ocupar a tela edge-to-edge, enquanto conteúdos sensíveis deverão respeitar os insets reais fornecidos pela plataforma/dispositivo.

---

# 12. Matriz de comparação

Preencher após as três avaliações.

| Critério | A | B | C | Observação |
|---|---|---|---|---|
| Viewport 360 × 800 / 1:1 | CANDIDATA | — | — | A validada em v02 |
| Legibilidade dos metadados | CANDIDATA | — | — | A validada em v02 |
| Espaço para cores | CANDIDATA | — | — | A validada em v02 |
| Espaço para tipografia | CANDIDATA | — | — | A validada em v02 |
| Espaço para observações | CANDIDATA | — | — | A validada em v02 |
| Página/versão legíveis | CANDIDATA | — | — | A validada em v02 |
| Scroll/continuidade | CANDIDATA | — | — | A validada em v02 |
| Equivalência Claro/Escuro | CANDIDATA | — | — | A validada em v02 |
| Multipágina | CANDIDATA | — | — | A validada em v02 |
| Consistência/reprodutibilidade | CANDIDATA | — | — | A validada em v02 |

A marcação `CANDIDATA` na coluna A registra que a alternativa foi aceita para comparação. Ela não antecipa a seleção final.

A matriz deve registrar fatos observáveis; preferência estética isolada não é critério suficiente.

---

# 13. Escolha do modelo

Após avaliação de A/B/C, as decisões permitidas são:

```text
A
B
C
AJUSTAR UMA ALTERNATIVA
COMBINAR PARTES EXPLICITAMENTE IDENTIFICADAS
```

Se houver combinação, registrar exatamente:

```text
Origem estrutural:
Cabeçalho proveniente de:
Posição do viewport proveniente de:
Painel/rodapé técnico proveniente de:
Outros elementos:
Motivo:
```

Não inferir uma combinação automaticamente.

---

# 14. Modelo oficial

Depois da decisão explícita, gerar:

```text
official/WF-TEMPLATE-OFFICIAL_v01.png
```

Registro obrigatório:

```text
Data:
Arquivo:
Versão:
Origem: A | B | C | combinação
Decisão que originou o modelo:
Coordenadas congeladas:
Status: EM VALIDAÇÃO | APROVADO
Observação:
```

---

# 15. Congelamento

Após aprovação explícita:

```text
WF-TEMPLATE-OFFICIAL_v01.png
Status: APROVADO / CONGELADO
```

Não pode ser:

- sobrescrito;
- regenerado;
- melhorado automaticamente;
- substituído sem nova versão.

Nova alteração:

```text
WF-TEMPLATE-OFFICIAL_v02.png
```

A versão `v01` permanece preservada.

---

# 16. Relação com os wireframes funcionais

Somente depois do modelo oficial aprovado e congelado:

```text
template oficial
        ↓
fechamento do gate em ../README.md
        ↓
T00 Claro
        ↓
T00 Escuro
```

As pranchas-modelo:

- não são T00;
- não recebem ID funcional T/M/E;
- não são contabilizadas entre as imagens funcionais;
- não alteram a baseline;
- não autorizam Design Visual ou Figma antecipadamente.

---

# 17. Registro atual

| Artefato | Caminho | Status |
|---|---|---|
| Alternativa A v01 | `alternatives/WF-TEMPLATE-A_v01.png` | HISTÓRICO / PRESERVADA |
| Alternativa A v02 | `alternatives/WF-TEMPLATE-A_v02.png` | CANDIDATA |
| Alternativa B | `alternatives/WF-TEMPLATE-B_v01.png` | PENDENTE DE PRODUÇÃO |
| Alternativa C | `alternatives/WF-TEMPLATE-C_v01.png` | PENDENTE DE PRODUÇÃO |
| Modelo oficial | `official/WF-TEMPLATE-OFFICIAL_v01.png` | NÃO DEFINIDO |

A Alternativa A está validada para comparação. A próxima produção autorizada é `WF-TEMPLATE-B_v01.png`.
