# SaOr - Sales Order
## Controle da etapa — Wireframes Conceituais em Imagem

**Baseline funcional:** v1.0 — APROVADO / BASELINE FUNCIONAL  
**Etapa atual:** Wireframe Conceitual em Imagem  
**Status deste documento:** EM VALIDAÇÃO — especificação técnica em fechamento  
**Interfaces documentadas:** 71  
**Variações obrigatórias:** Claro (`white`) e Escuro (`black`)  
**Quantidade mínima de imagens funcionais:** 142  
**Quantidade final de imagens funcionais:** variável conforme paginação necessária por interface  
**Fonte funcional:** `docs/Documento_Mestre.md`  
**Registro de não regressão:** `docs/Registro_Fechamento_Documento_Mestre.md`

---

# 1. Finalidade

Este documento controla a produção, validação, aprovação e preservação dos wireframes conceituais em imagem do **SaOr - Sales Order**, incluindo a especificação técnica da prancha e o processo de seleção do template documental.

Cada interface `T`, `M` ou `E` da baseline funcional deve possuir, no mínimo:

- uma representação **Claro**, em `docs/wireframes/images/white`;
- uma representação **Escuro**, em `docs/wireframes/images/black`.

Quando todo o conteúdo funcional não puder ser representado em um único viewport de `360 × 800 px`, a interface será documentada em páginas sequenciais. Por isso, **142 é a quantidade mínima de imagens funcionais**, não um total rígido.

As pranchas-modelo armazenadas em `templates/` são artefatos de calibração e governança e **não entram na contagem das imagens funcionais das 71 interfaces**.

---

# 2. Estrutura oficial

```text
docs/
└── wireframes/
    └── images/
        ├── README.md
        ├── templates/
        │   ├── README.md
        │   ├── alternatives/
        │   │   ├── .gitkeep
        │   │   ├── WF-TEMPLATE-A_v01.png
        │   │   ├── WF-TEMPLATE-A_v02.png
        │   │   ├── WF-TEMPLATE-B_v01.png
        │   │   └── WF-TEMPLATE-C_v01.png
        │   └── official/
        │       ├── .gitkeep
        │       └── WF-TEMPLATE-OFFICIAL_v01.png
        ├── white/
        │   ├── .gitkeep
        │   └── T00-01-01_v01.png
        └── black/
            ├── .gitkeep
            └── T00-01-01_v01.png
```

Os `.gitkeep` existem somente para preservar no Git diretórios ainda vazios.

Regras de separação:

- `templates/alternatives/`: propostas de prancha técnica avaliadas;
- `templates/official/`: somente o template formalmente aprovado;
- `white/`: somente wireframes funcionais Claro;
- `black/`: somente wireframes funcionais Escuro.

Alternativas de template nunca devem ser armazenadas em `white/` ou `black/`.

---

# 3. Referência dimensional aprovada

## 3.1 Viewport mobile oficial

**Viewport lógico oficial: `360 × 800 px`.**

Regras:

- orientação: **retrato**;
- representa a **tela lógica completa do celular**;
- elementos que ocupem ou sobreponham a tela devem ser considerados dentro dos `360 × 800 px`;
- não acrescentar barras ou áreas por fora dos `800 px`;
- não desenhar moldura física de aparelho;
- não criar versão específica para iOS ou Android;
- paisagem será estudada posteriormente;
- tablet e desktop não serão produzidos automaticamente nesta etapa.

## 3.2 Safe areas técnicas

```text
Safe area superior de referência do wireframe: 24 px
Safe area inferior de referência do wireframe: 32 px
```

Esses valores são **reservas técnicas exclusivas da etapa de wireframe** e são neutros em relação ao sistema operacional.

Sua finalidade é garantir que, nas pranchas desta etapa, textos, controles e outros conteúdos sensíveis não sejam posicionados em regiões que podem ser ocupadas por elementos do sistema operacional.

Regras:

- os `24 px` superiores e `32 px` inferiores **não constituem paddings fixos do produto**;
- esses valores **não constituem constantes obrigatórias de implementação**;
- na implementação, background, superfícies e elementos visuais que admitam desenho edge-to-edge podem ocupar **100% da superfície disponível da tela**;
- textos, controles, ações e demais conteúdos sensíveis devem respeitar os **insets reais fornecidos pela plataforma/dispositivo em tempo de execução**;
- os insets reais de implementação podem ser diferentes de `24 px` e `32 px`;
- não deve existir dupla compensação de safe area quando a plataforma ou o framework já fornecer tratamento dos insets;
- a implementação futura deverá seguir o comportamento real da plataforma adotada, sem transformar a reserva técnica do wireframe em regra rígida de layout;
- não representar notch, Dynamic Island, barra Android ou outro chrome específico nas pranchas desta etapa.

Em síntese:

```text
WIREFRAME
24 px superior / 32 px inferior
= referência padronizada de segurança visual

IMPLEMENTAÇÃO
superfície visual pode ocupar 100% da tela
+
conteúdo sensível respeita os insets reais da plataforma/dispositivo
```

## 3.3 Prancha técnica

```text
Canvas: 1024 × 1536 px
Orientação: retrato
Escala do viewport: 1:1
```

Consequência:

```text
1 px lógico do wireframe = 1 px na representação do viewport na prancha
```

A prancha deve conter:

- metadados;
- viewport `360 × 800 px`;
- wireframe;
- legenda cromática usada;
- legenda tipográfica usada;
- observações técnicas quando aplicáveis.

As coordenadas exatas dessas áreas serão congeladas somente após aprovação do template oficial.

---

# 4. Margens, grid e espaçamento

```text
Margem horizontal estrutural: 12 px
Base de espaçamento: 4 px
Escala: 4 / 8 / 12 / 16 / 24 / 32 px
Padding-base horizontal: 16 px
Padding-base vertical: 12 px
```

Espaçamentos fora da escala exigem justificativa registrada.

---

# 5. Convenção de arquivos funcionais

Formato oficial:

```text
<ID>-<PÁGINA>-<TOTAL>_v<VERSÃO>.png
```

Exemplos:

```text
T00-01-01_v01.png
T00-01-02_v01.png
T00-02-02_v01.png
```

Significado:

- `<ID>`: interface;
- `<PÁGINA>`: página atual;
- `<TOTAL>`: total de páginas daquela representação;
- `<VERSÃO>`: versão da página.

Uma correção pode incrementar somente a página afetada. Se a alteração mudar o total de páginas, a nova sequência deve refletir o novo total de forma consistente.

---

# 6. Paginação e continuidade vertical

Quando o conteúdo ultrapassar `360 × 800 px`:

- o viewport permanece fixo;
- o conteúdo não deve ser comprimido artificialmente;
- criar páginas documentais sequenciais;
- repetir somente elementos realmente persistentes;
- continuar o conteúdo não persistente a partir do ponto correspondente;
- não criar paginação funcional inexistente na baseline;
- utilizar indicador vertical de rolagem somente quando necessário.

A interface somente pode ser aprovada quando **todas as páginas Claro e Escuro** estiverem aprovadas.

---

# 7. Estados de controle documental

```text
PENDENTE
EM VALIDAÇÃO
AJUSTES NECESSÁRIOS
APROVADO
```

Silêncio não constitui aprovação.

Artefato aprovado:

```text
APROVADO → CONGELADO NESTA ETAPA
```

Não pode ser sobrescrito, regenerado ou substituído silenciosamente.

---

# 8. Equivalência Claro / Escuro

Para a mesma interface e página, Claro e Escuro devem possuir as mesmas:

- informações;
- ações;
- destinos;
- campos;
- estados;
- hierarquia;
- agrupamentos;
- proporções;
- navegação;
- ordem de leitura;
- componentes;
- tipografia;
- paginação.

A diferença permitida é a paleta técnica.

---

# 9. Paletas técnicas

## 9.1 Claro

| Token | Aplicação | HEX |
|---|---|---|
| `WF-W-BG` | fundo geral | `#F4F4F4` |
| `WF-W-SURFACE` | superfície principal | `#FFFFFF` |
| `WF-W-SURFACE-ALT` | superfície secundária | `#EAEAEA` |
| `WF-W-BORDER` | borda/divisor | `#B5B5B5` |
| `WF-W-TEXT` | texto principal | `#1A1A1A` |
| `WF-W-TEXT-2` | texto secundário | `#565656` |
| `WF-W-ACTION` | ação/interação | `#333333` |
| `WF-W-DISABLED` | desabilitado | `#9A9A9A` |
| `WF-W-FOCUS` | foco/seleção | `#4A4A4A` |
| `WF-W-STATUS` | status | `#626262` |

## 9.2 Escuro

| Token | Aplicação | HEX |
|---|---|---|
| `WF-B-BG` | fundo geral | `#121212` |
| `WF-B-SURFACE` | superfície principal | `#1E1E1E` |
| `WF-B-SURFACE-ALT` | superfície secundária | `#2A2A2A` |
| `WF-B-BORDER` | borda/divisor | `#5E5E5E` |
| `WF-B-TEXT` | texto principal | `#F2F2F2` |
| `WF-B-TEXT-2` | texto secundário | `#C2C2C2` |
| `WF-B-ACTION` | ação/interação | `#E0E0E0` |
| `WF-B-DISABLED` | desabilitado | `#777777` |
| `WF-B-FOCUS` | foco/seleção | `#D0D0D0` |
| `WF-B-STATUS` | status | `#A8A8A8` |

Cor nunca pode ser o único indicador de estado.

---

# 10. Tipografia técnica

```text
WF-FONT-FAMILY: Inter
```

| Token | Peso | Tamanho | Line-height | Letter-spacing |
|---|---:|---:|---:|---|
| `WF-TITLE` | 600 | 20 px | 28 px | `normal` |
| `WF-SECTION` | 600 | 14 px | 20 px | `normal` |
| `WF-BODY` | 400 | 16 px | 24 px | `normal` |
| `WF-LABEL` | 500 | 14 px | 20 px | `normal` |
| `WF-ACTION-TEXT` | 500 | 16 px | 24 px | `normal` |
| `WF-CAPTION` | 400 | 12 px | 16 px | `normal` |

Inter é tipografia técnica do wireframe e não se torna automaticamente tipografia oficial do produto.

---

# 11. Componentes aprovados

MUI / Material UI é referência conceitual de componentes, estados e iconografia, **não escolha tecnológica definitiva**.

## 11.1 App Bar

```text
Altura: 56 px
```

## 11.2 Touch target

```text
Mínimo: 48 × 48 px
```

## 11.3 Campos

```text
Variante: Outlined
Altura: 56 px
Radius: 12 px
Borda: 1 px quando aplicável
Padding-base: 16 px horizontal / 12 px vertical
```

## 11.4 Botões

Categorias:

```text
Primary
Secondary
Text
Icon Button
```

```text
Altura mínima textual: 48 px
Touch target mínimo: 48 × 48 px
Radius: 12 px
```

## 11.5 Listas/configurações

```text
Item simples: mínimo 56 px
Item com secundário/status: mínimo 64 px
```

## 11.6 Cards

```text
Radius: 16 px
Borda: 1 px quando necessária
```

## 11.7 Modal/Dialog

```text
Margem lateral: 24 px
Radius: 16 px
```

## 11.8 Bottom Navigation

Quando prevista pela baseline:

```text
Altura: 64 px
```

---

# 12. Bordas, divisores, radius e elevação

```text
Bordas: 1 px quando necessárias
Divisores: 1 px
Campos/botões: radius 12 px
Cards/modais: radius 16 px
```

Elevação:

```text
WF-ELEVATION-0
offset-x: 0 px
offset-y: 0 px
blur: 0 px
opacidade: 0%

WF-ELEVATION-1
offset-x: 0 px
offset-y: 1 px
blur: 2 px
cor-base: preto neutro
opacidade: 12%

WF-ELEVATION-2
offset-x: 0 px
offset-y: 2 px
blur: 6 px
cor-base: preto neutro
opacidade: 16%

WF-ELEVATION-3
offset-x: 0 px
offset-y: 4 px
blur: 12 px
cor-base: preto neutro
opacidade: 20%
```

Referência de uso: E0 conteúdo integrado; E1 card destacado; E2 menu/dropdown; E3 modal/dialog.

---

# 13. Iconografia

Referência:

```text
Material Icons Outlined
```

Não obriga a implementação futura a utilizar MUI ou Material Icons.

```text
Ícone auxiliar: 20 px
Ícone de ação/navegação: 24 px
Touch target: mínimo 48 × 48 px
```

Ícone isolado somente quando a ação for inequívoca; caso contrário, associar texto.

---

# 14. Estados de componentes

Estados previstos:

```text
default
focus
pressed / selected
disabled
error
hover
```

`hover` fica documentado, mas não precisa ser exibido nas pranchas mobile salvo necessidade específica.

---

# 15. Componentes ainda não catalogados

Se uma interface exigir componente ainda não especificado:

```text
necessidade no Documento Mestre
        ↓
definir geometria e estados
        ↓
registrar neste README
        ↓
usar na primeira imagem
```

É proibido introduzir componente novo silenciosamente.

---

# 16. Acessibilidade estrutural

- cor nunca como único indicador;
- touch target mínimo respeitado;
- ordem de leitura clara;
- campos com rótulos;
- erros próximos ao contexto;
- foco e seleção distinguíveis;
- hierarquia tipográfica consistente;
- componentes sem compactação que prejudique operação.

A estrutura não pode impedir futura conformidade WCAG 2.2 AA.

---

# 17. Conteúdo obrigatório de uma prancha funcional

```text
Projeto: SaOr - Sales Order
Interface: <ID> — <Nome>
Baseline: v1.0
Etapa: Wireframe Conceitual em Imagem
Variação: Claro | Escuro
Status: EM VALIDAÇÃO | AJUSTES NECESSÁRIOS | APROVADO
Página: <XX>/<YY>
Versão: vNN
Viewport lógico: 360 × 800 px
Orientação: Retrato
Canvas: 1024 × 1536 px
Escala: 1:1
Fonte técnica: Inter
```

Também devem constar tokens cromáticos e tipográficos realmente usados e observações necessárias.

---

# 18. Regra de produção funcional

Antes de produzir qualquer interface, consultar no Documento Mestre:

- ficha funcional de aceite;
- objetivo;
- informações exibidas;
- campos e obrigatoriedade;
- ações e destinos;
- Textframe;
- estados;
- retorno;
- interfaces relacionadas;
- regras transversais.

É proibido inventar funcionalidade, remover ação, criar destino inexistente, fundir IDs, alterar Textframe por conveniência visual, adotar tecnologia definitiva ou introduzir componente não documentado.

---

# 19. Governança das pranchas-modelo

A especificação completa das alternativas e do histórico de decisão está em:

[`templates/README.md`](templates/README.md)

As pranchas-modelo:

- são produzidas separadamente;
- não representam T00 nem outra interface funcional;
- não contam para o mínimo de 142 imagens;
- devem permanecer no repositório após a escolha;
- não devem ser apagadas porque foram rejeitadas;
- servem como histórico de decisão e referência de auditoria.

## 19.1 Estado das alternativas

```text
WF-TEMPLATE-A_v01.png — HISTÓRICO / PRESERVADA
WF-TEMPLATE-A_v02.png — CANDIDATA
WF-TEMPLATE-B_v01.png — PRÓXIMA PRODUÇÃO
WF-TEMPLATE-C_v01.png — PENDENTE
```

Produção sequencial atual:

```text
A_v01 → histórico preservado
  ↓
A_v02 → validada / CANDIDATA
  ↓
B_v01 → próxima produção
  ↓
avaliação de B
  ↓
C_v01
  ↓
avaliação de C
  ↓
comparação técnica A × B × C
```

A produção sequencial não autoriza alterar silenciosamente o conceito de cada alternativa.

## 19.2 Conceitos

**A — viewport central dominante**  
Viewport como elemento principal; metadados no topo; especificações nas áreas restantes.

**B — viewport à esquerda + painel técnico à direita**  
Viewport à esquerda em escala 1:1 e documentação em coluna técnica lateral.

**C — viewport superior + documentação inferior**  
Viewport na região superior/central e documentação em blocos inferiores.

## 19.3 Critérios obrigatórios de comparação

Cada alternativa deve ser verificada quanto a:

1. viewport exatamente `360 × 800 px`;
2. escala `1:1`;
3. ausência de invasão do viewport por legendas;
4. legibilidade dos metadados;
5. espaço suficiente para tokens cromáticos;
6. especificação tipográfica cabe integralmente;
7. área utilizável de observações;
8. identificação clara de `XX/YY`;
9. identificação clara de `vNN`;
10. capacidade de indicar scroll/continuidade;
11. mesmas coordenadas possíveis em Claro/Escuro;
12. funcionamento para interface de uma ou várias páginas.

## 19.4 Seleção

Após avaliação de A/B/C, o responsável pode:

- aprovar A;
- aprovar B;
- aprovar C;
- solicitar ajustes em uma alternativa;
- solicitar combinação explícita de partes das alternativas.

Nenhuma combinação pode ser inferida automaticamente.

---

# 20. Template oficial

Após escolha explícita:

```text
templates/official/WF-TEMPLATE-OFFICIAL_v01.png
```

O registro deve indicar se sua origem foi A, B, C ou combinação autorizada.

A aprovação do template oficial:

- não apaga alternativas;
- congela o arquivo aprovado;
- não autoriza sobrescrita;
- exige nova versão para qualquer alteração posterior.

Exemplo:

```text
WF-TEMPLATE-OFFICIAL_v01.png
WF-TEMPLATE-OFFICIAL_v02.png
```

A versão anterior permanece preservada.

---

# 21. Gate antes de T00

## 21.1 Especificação já aprovada

```text
[x] viewport 360 × 800 px
[x] retrato
[x] safe area 24 / 32 px
[x] canvas 1024 × 1536 px
[x] escala 1:1
[x] margem 12 px
[x] spacing e padding
[x] paletas Claro/Escuro
[x] Inter e escala tipográfica
[x] componentes-base
[x] bordas/radius/elevação
[x] iconografia
[x] estados
[x] scroll e paginação
[x] nomenclatura e versionamento
[x] governança e preservação das pranchas-modelo
```

## 21.2 Estado do gate das alternativas

```text
[x] WF-TEMPLATE-A_v01 produzido e preservado como histórico
[x] WF-TEMPLATE-A_v02 produzido e validado como CANDIDATA
[ ] WF-TEMPLATE-B_v01 produzido e avaliado
[ ] WF-TEMPLATE-C_v01 produzido e avaliado
[ ] comparação técnica registrada
[ ] alternativa/combinação escolhida explicitamente
[ ] WF-TEMPLATE-OFFICIAL_v01 produzido
[ ] coordenadas exatas aprovadas
[ ] cabeçalho técnico aprovado
[ ] legendas aprovadas
[ ] área de observações aprovada
[ ] safe areas visualmente aprovadas
[ ] scroll/continuidade visualmente aprovado
[ ] template oficial aprovado e congelado
```

Enquanto esses itens permanecerem pendentes, `T00` não está liberada para produção definitiva.

---

# 22. Fluxo operacional

```text
ESPECIFICAÇÃO DOCUMENTADA
        ↓
WF-TEMPLATE-A_v01
        ↓
ajustes
        ↓
WF-TEMPLATE-A_v02
        ↓
CANDIDATA
        ↓
WF-TEMPLATE-B_v01
        ↓
avaliação
        ↓
WF-TEMPLATE-C_v01
        ↓
avaliação
        ↓
COMPARAÇÃO TÉCNICA
        ↓
ESCOLHA EXPLÍCITA
        ↓
WF-TEMPLATE-OFFICIAL_v01
        ↓
APROVAÇÃO EXPLÍCITA
        ↓
TEMPLATE CONGELADO
        ↓
T00 Claro
        ↓
T00 Escuro
        ↓
EM VALIDAÇÃO
```

---

# 23. Classificação de ocorrências

```text
A — baseline representável exatamente
B — ambiguidade de representação sem mudança funcional
C — contradição documental objetiva
D — requisito novo posterior à baseline
```

Tratamento:

- A: produzir normalmente;
- B: representação conservadora + registro;
- C: apresentar contradição;
- D: não alterar baseline.

---

# 24. Checklist mestre

| # | ID | Interface | Claro | Versão/Páginas | Escuro | Versão/Páginas | Interface |
|---:|---|---|---|---|---|---|---|
| 01 | `T00` | Configuração da aplicação | PENDENTE | — | PENDENTE | — | PENDENTE |
| 02 | `T00.1` | Configuração da API | PENDENTE | — | PENDENTE | — | PENDENTE |
| 03 | `T00.2` | Aparência / Tema | PENDENTE | — | PENDENTE | — | PENDENTE |
| 04 | `T00.3` | Diagnóstico de conexão | PENDENTE | — | PENDENTE | — | PENDENTE |
| 05 | `M00.4` | Confirmar alteração da API | PENDENTE | — | PENDENTE | — | PENDENTE |
| 06 | `M00.5` | Restaurar configuração | PENDENTE | — | PENDENTE | — | PENDENTE |
| 07 | `E00.6` | Testando conexão | PENDENTE | — | PENDENTE | — | PENDENTE |
| 08 | `E00.7` | Conexão realizada | PENDENTE | — | PENDENTE | — | PENDENTE |
| 09 | `E00.8` | Falha de conexão | PENDENTE | — | PENDENTE | — | PENDENTE |
| 10 | `E00.9` | API não configurada | PENDENTE | — | PENDENTE | — | PENDENTE |
| 11 | `E00.10` | API indisponível no login | PENDENTE | — | PENDENTE | — | PENDENTE |
| 12 | `T01` | Login | PENDENTE | — | PENDENTE | — | PENDENTE |
| 13 | `T01.1` | Recuperar senha | PENDENTE | — | PENDENTE | — | PENDENTE |
| 14 | `E01.2` | Login inválido | PENDENTE | — | PENDENTE | — | PENDENTE |
| 15 | `E01.3` | Sem conexão | PENDENTE | — | PENDENTE | — | PENDENTE |
| 16 | `E01.4` | Recuperação solicitada | PENDENTE | — | PENDENTE | — | PENDENTE |
| 17 | `E01.5` | Falha ao solicitar recuperação | PENDENTE | — | PENDENTE | — | PENDENTE |
| 18 | `T02` | Início / Dashboard | PENDENTE | — | PENDENTE | — | PENDENTE |
| 19 | `T02.1` | Notificações | PENDENTE | — | PENDENTE | — | PENDENTE |
| 20 | `T03` | Clientes e Prospects | PENDENTE | — | PENDENTE | — | PENDENTE |
| 21 | `M03.1` | Filtros de clientes | PENDENTE | — | PENDENTE | — | PENDENTE |
| 22 | `E03.2` | Busca sem resultado | PENDENTE | — | PENDENTE | — | PENDENTE |
| 23 | `T04` | Cliente — Resumo | PENDENTE | — | PENDENTE | — | PENDENTE |
| 24 | `T04.1` | Cliente — Pedidos | PENDENTE | — | PENDENTE | — | PENDENTE |
| 25 | `T04.2` | Cliente — Visitas | PENDENTE | — | PENDENTE | — | PENDENTE |
| 26 | `T04.3` | Cliente — Financeiro | PENDENTE | — | PENDENTE | — | PENDENTE |
| 27 | `T04.4` | Cliente — Endereço | PENDENTE | — | PENDENTE | — | PENDENTE |
| 28 | `T04.5` | Cliente — Dados cadastrais | PENDENTE | — | PENDENTE | — | PENDENTE |
| 29 | `T05` | Novo Prospect — Dados básicos | PENDENTE | — | PENDENTE | — | PENDENTE |
| 30 | `T05.1` | Novo Prospect — Endereço | PENDENTE | — | PENDENTE | — | PENDENTE |
| 31 | `T05.2` | Novo Prospect — Informações comerciais | PENDENTE | — | PENDENTE | — | PENDENTE |
| 32 | `T05.3` | Prospect — Resumo | PENDENTE | — | PENDENTE | — | PENDENTE |
| 33 | `T05.4` | Prospect — Histórico de visitas | PENDENTE | — | PENDENTE | — | PENDENTE |
| 34 | `T06` | Registrar visita | PENDENTE | — | PENDENTE | — | PENDENTE |
| 35 | `M06.1` | Finalizar visita | PENDENTE | — | PENDENTE | — | PENDENTE |
| 36 | `T06.2` | Detalhes da visita | PENDENTE | — | PENDENTE | — | PENDENTE |
| 37 | `E06.3` | Falha ao finalizar visita | PENDENTE | — | PENDENTE | — | PENDENTE |
| 38 | `T07` | Catálogo de produtos | PENDENTE | — | PENDENTE | — | PENDENTE |
| 39 | `M07.1` | Filtros de produtos | PENDENTE | — | PENDENTE | — | PENDENTE |
| 40 | `E07.2` | Produto não encontrado | PENDENTE | — | PENDENTE | — | PENDENTE |
| 41 | `T08` | Detalhes do produto | PENDENTE | — | PENDENTE | — | PENDENTE |
| 42 | `T09` | Pedido — Cliente | PENDENTE | — | PENDENTE | — | PENDENTE |
| 43 | `M09.1` | Selecionar cliente | PENDENTE | — | PENDENTE | — | PENDENTE |
| 44 | `T09.2` | Selecionar endereço | PENDENTE | — | PENDENTE | — | PENDENTE |
| 45 | `M09.3` | Selecionar tabela de preço | PENDENTE | — | PENDENTE | — | PENDENTE |
| 46 | `T10` | Pedido — Itens | PENDENTE | — | PENDENTE | — | PENDENTE |
| 47 | `M10.1` | Editar item | PENDENTE | — | PENDENTE | — | PENDENTE |
| 48 | `T11` | Pedido — Condições comerciais | PENDENTE | — | PENDENTE | — | PENDENTE |
| 49 | `T12` | Pedido — Revisão | PENDENTE | — | PENDENTE | — | PENDENTE |
| 50 | `M12.1` | Confirmar pedido | PENDENTE | — | PENDENTE | — | PENDENTE |
| 51 | `T13` | Pedido confirmado | PENDENTE | — | PENDENTE | — | PENDENTE |
| 52 | `T14` | Pedidos | PENDENTE | — | PENDENTE | — | PENDENTE |
| 53 | `M14.1` | Filtros de pedidos | PENDENTE | — | PENDENTE | — | PENDENTE |
| 54 | `T15` | Detalhes do pedido | PENDENTE | — | PENDENTE | — | PENDENTE |
| 55 | `T15.1` | Condições do pedido | PENDENTE | — | PENDENTE | — | PENDENTE |
| 56 | `T15.2` | Endereço de entrega | PENDENTE | — | PENDENTE | — | PENDENTE |
| 57 | `T16` | Agenda | PENDENTE | — | PENDENTE | — | PENDENTE |
| 58 | `T16.1` | Agendar visita | PENDENTE | — | PENDENTE | — | PENDENTE |
| 59 | `T16.2` | Compromisso / Visita | PENDENTE | — | PENDENTE | — | PENDENTE |
| 60 | `M16.3` | Confirmar cancelamento da visita | PENDENTE | — | PENDENTE | — | PENDENTE |
| 61 | `E16.4` | Falha ao cancelar visita | PENDENTE | — | PENDENTE | — | PENDENTE |
| 62 | `T17` | Mais | PENDENTE | — | PENDENTE | — | PENDENTE |
| 63 | `T17.1` | Meu perfil | PENDENTE | — | PENDENTE | — | PENDENTE |
| 64 | `T17.2` | Sincronização | PENDENTE | — | PENDENTE | — | PENDENTE |
| 65 | `T17.3` | Configurações | PENDENTE | — | PENDENTE | — | PENDENTE |
| 66 | `T17.4` | Ajuda | PENDENTE | — | PENDENTE | — | PENDENTE |
| 67 | `T17.5` | Sobre | PENDENTE | — | PENDENTE | — | PENDENTE |
| 68 | `M17.6` | Confirmar saída | PENDENTE | — | PENDENTE | — | PENDENTE |
| 69 | `E17.7` | Sincronização em andamento | PENDENTE | — | PENDENTE | — | PENDENTE |
| 70 | `E17.8` | Sincronização concluída | PENDENTE | — | PENDENTE | — | PENDENTE |
| 71 | `E17.9` | Falha na sincronização | PENDENTE | — | PENDENTE | — | PENDENTE |

---

# 25. Contadores

```text
Interfaces previstas:                    71
Mínimo de imagens Claro:                 71
Mínimo de imagens Escuro:                71
Mínimo de imagens funcionais:           142

Total funcional final:          VARIÁVEL POR PAGINAÇÃO

Pranchas-modelo alternativas:             3 planejadas
Template oficial:                         1 após aprovação

Páginas Claro aprovadas:                  0
Páginas Escuro aprovadas:                 0
Interfaces totalmente aprovadas:        0 / 71
```

Pranchas-modelo não entram na contagem de imagens funcionais.

---

# 26. Registro de aprovação e reabertura

Página funcional:

```text
Data:
Interface:
Variação:
Página:
Arquivo:
Versão:
Status anterior:
Status novo:
Observação:
```

Interface completa somente é aprovada quando todas as páginas Claro/Escuro estiverem aprovadas.

---

# 27. Preservação documental

Autoridade documental:

1. `docs/Documento_Mestre.md`;
2. `docs/Registro_Fechamento_Documento_Mestre.md`;
3. `README.md`;
4. este documento;
5. `templates/README.md` para histórico específico das pranchas-modelo.

Este documento não altera baseline funcional, não define arquitetura definitiva, não transforma MUI em tecnologia oficial e não autoriza Figma, protótipo ou implementação antes das etapas correspondentes.
