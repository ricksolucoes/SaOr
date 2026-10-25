# Wireframes — Montagem profissional da imagem

## 1. Escopo

Esta spec define **como executar visualmente um Wireframe Text já aprovado** e produzir a imagem final da prancha com qualidade profissional, consistência e controle de regressão.

Ela começa somente quando o artefato já possui autorização para produção visual conforme o processo vigente.

Esta spec não define:

- requisitos funcionais;
- conteúdo funcional;
- geometria específica de uma prancha;
- canvas, viewport, grid, tokens ou componentes técnicos canônicos;
- estados ou gates do processo;
- estrutura documental do Wireframe Text;
- uma composição universal para todos os templates.

Essas responsabilidades permanecem em suas fontes canônicas.

A montagem da imagem é **execução visual controlada**, não uma nova etapa de descoberta da composição.

---

## 2. Autoridade de entrada

Antes de iniciar a imagem, a execução deve consultar as fontes vigentes nesta ordem de responsabilidade:

```text
Documento Mestre, quando houver conteúdo funcional aplicável
        ↓
REGRAS-TECNICAS.md
→ invariantes técnicas
        ↓
PROCESSO-PRANCHA.md
→ liberação da produção e gates
        ↓
WIREFRAME-TEXT.md
→ contrato documental
        ↓
docs/wireframes/images/README.md
→ contexto operacional e localização das referências vigentes
        ↓
Wireframe Text específico aprovado
→ composição, conteúdo e geometria da prancha
        ↓
MONTAGEM-IMAGEM.md
→ método de execução visual profissional
        ↓
ativos oficiais aplicáveis
→ arquivos físicos que devem ser inseridos sem reconstrução
        ↓
PNG
```

`MONTAGEM-IMAGEM.md` não pode alterar silenciosamente uma decisão superior.

Se esta spec e um Wireframe Text específico parecerem incompatíveis, a execução deve identificar a incompatibilidade antes da exportação. Não corrigir a divergência inventando uma terceira regra durante a renderização.

---

## 3. Leitura contextual e uso das referências existentes

A montagem de uma prancha nova deve ocorrer dentro do contexto documental e visual vigente do projeto.

Antes de produzir a imagem, a execução deve consultar, quando aplicáveis:

- as specs canônicas da etapa;
- o Wireframe Text específico aprovado;
- `docs/wireframes/images/README.md`, para localizar a estrutura operacional e as referências vigentes;
- referências técnicas neutras ou específicas da mesma variação;
- pranchas-modelo existentes que estejam registradas como referência visual contextual da variação ou da etapa.

Referências visuais existentes podem ser usadas para compreender e preservar continuidade de:

- linguagem visual;
- nível de acabamento;
- densidade documental;
- hierarquia visual;
- tratamento de cabeçalhos, metadados e regiões documentais;
- ritmo, alinhamento e qualidade geral de apresentação.

Esse uso é **contextual**, não substitutivo.

Uma referência visual não possui autoridade para sobrescrever uma decisão explicitamente definida em fonte superior ou no Wireframe Text específico, incluindo:

- geometria;
- posição;
- dimensões;
- conteúdo;
- ordem;
- ativos obrigatórios;
- composição específica;
- separação `white` / `black`.

Quando a composição específica divergir visualmente de uma prancha de referência, preservar a composição específica e usar a referência somente para compreender o padrão de execução e acabamento que continue aplicável.

Não copiar automaticamente a geometria ou o conteúdo de outra prancha.

Não ignorar referências existentes apenas porque pertencem a outro frame, quando sua função documental for ajudar a compreender a linguagem visual esperada.

Uma imagem anterior do **mesmo frame** continua possuindo função adicional de baseline de **não regressão** durante uma revisão daquele frame, conforme a seção de versionamento desta spec.

Imagem histórica ou contextual não substitui spec nem Wireframe Text.

---

## 4. Fundamentos profissionais incorporados

Esta spec incorpora práticas atuais de sistemas de design e produção de interfaces, convertidas em regras internas do SaOr. Pesquisa metodológica consolidada em `2026-10-25`.

Princípios incorporados:

1. decisões visuais reutilizáveis devem vir de fontes documentadas e tokens, evitando valores ad hoc;
2. espaçamento deve comunicar proximidade, agrupamento e hierarquia, não apenas preencher espaço;
3. tipografia deve ser aplicada por função semântica e hierarquia, não por escolha livre a cada bloco;
4. alinhamentos repetidos, ritmo espacial e consistência de componentes reduzem ruído visual;
5. densidade deve permitir leitura e escaneamento sem compactação prejudicial;
6. estados e informação relevante não podem depender exclusivamente de cor;
7. texto e elementos gráficos essenciais devem preservar contraste suficiente;
8. uma alteração controlada deve preservar tudo que ficou fora do seu escopo;
9. a saída final deve ser verificável contra as fontes documentais, não apenas avaliada por semelhança subjetiva.

Referências metodológicas consultadas na consolidação desta spec:

- Design Tokens Community Group — especificação estável 2025.10;
- Microsoft Fluent 2 — layout, spacing, proximity e hierarquia;
- IBM Carbon Design System — spacing e tipografia por escalas/tokens;
- WCAG 2.2 — contraste, estados perceptíveis e acessibilidade visual.

Essas referências são **metodológicas e não normativas para o SaOr**. Depois de incorporada uma regra aqui, a fonte normativa para a execução passa a ser esta spec e as demais specs canônicas do projeto.

Uma mudança futura nessas referências externas não altera automaticamente o SaOr.

---

## 5. Pré-condições para montagem

A montagem visual só pode começar quando o processo vigente liberar a produção do PNG.

Antes de desenhar qualquer elemento, confirmar:

```text
[ ] Wireframe Text específico identificado
[ ] variação identificada: white ou black
[ ] Gate 6 registrado conforme exigido por PROCESSO-PRANCHA.md
[ ] Produção do PNG liberada pelo estado vigente
[ ] REGRAS-TECNICAS.md vigente consultado
[ ] contexto operacional em docs/wireframes/images/README.md consultado
[ ] referências técnicas aplicáveis identificadas
[ ] referências visuais contextuais vigentes identificadas e inspecionadas quando existirem
[ ] geometria específica disponível no Wireframe Text
[ ] conteúdo textual exato disponível
[ ] ativos físicos obrigatórios localizados
[ ] fontes necessárias disponíveis quando exigidas
[ ] versão/frame corrente identificado
[ ] revisão anterior do mesmo frame identificada quando existir
```

Se um ativo obrigatório não estiver disponível para a execução, não o reconstruir por aproximação.

Se uma fonte oficial obrigatória não estiver disponível, não substituir silenciosamente por uma fonte parecida e tratar a saída como final.

---

## 6. Classificação dos elementos durante a montagem

Todo elemento da prancha deve ser tratado como um dos tipos abaixo.

### 6.1 Ativo físico oficial

Arquivo existente que precisa ser inserido como ativo, por exemplo:

- bitmap oficial;
- SVG oficial;
- logo;
- ícone mestre ou variante catalogada;
- referência física cuja inserção direta esteja exigida pela documentação.

Regras:

- usar o arquivo oficial;
- respeitar a variação correta;
- preservar proporção;
- preservar dimensões quando forem normativas;
- não redesenhar;
- não reconstruir por aproximação;
- não substituir por screenshot, emoji, caractere Unicode ou desenho semelhante;
- não aplicar filtros ou transformação não autorizada.

Quando a documentação exigir escala `1:1` ou `100%`, essa condição deve ser verificada fisicamente no PNG final.

### 6.2 Elemento técnico desenhado

Elemento que deve ser construído usando as specs vigentes, por exemplo:

- painel documental;
- divisor;
- borda;
- cota;
- amostra de componente;
- estado demonstrativo;
- área de texto;
- elemento de diagramação técnica.

Regras:

- usar somente tokens e medidas autorizados;
- não introduzir estilo decorativo sem função;
- não criar dimensão funcional inexistente;
- não usar defaults visuais da ferramenta de renderização como decisão de design.

### 6.3 Conteúdo tipográfico

Texto deve ser renderizado pelo papel que exerce na prancha.

Usar os tokens tipográficos de `REGRAS-TECNICAS.md` quando a tipografia for técnica.

Quando o Wireframe Text ou a identidade visual exigir tipografia de marca, usar a fonte oficial correspondente.

Não escolher tamanho, peso ou família por conveniência de encaixe.

### 6.4 Conteúdo específico da prancha

Textos, valores, metadados, posições, dimensões e composição definidos no Wireframe Text são dados de entrada.

A montagem não pode reescrevê-los para melhorar visualmente a imagem.

---

## 7. Hierarquia visual profissional

A imagem deve permitir identificar rapidamente:

1. identidade da prancha;
2. objeto principal de demonstração;
3. regiões técnicas principais;
4. subseções;
5. conteúdo de apoio;
6. observações e metadados de menor prioridade.

A hierarquia deve resultar da combinação controlada de:

- tipografia;
- posição;
- espaçamento;
- agrupamento;
- superfície;
- borda/divisor quando necessário;
- contraste;
- alinhamento.

Não criar hierarquia apenas aumentando indiscriminadamente fonte, borda ou peso.

Elementos equivalentes devem receber tratamento equivalente.

Elementos subordinados não devem competir visualmente com o elemento principal.

---

## 8. Regra de spacing, proximidade e ritmo

A escala permitida continua sendo definida por `REGRAS-TECNICAS.md`.

Esta spec define **como escolher dentro da escala**, quando o Wireframe Text não fixa um valor específico.

Aplicar a relação:

```text
espaço interno de um grupo
<
espaço entre grupos relacionados
<
espaço entre regiões principais
```

Objetivo:

- itens semanticamente próximos parecem pertencer ao mesmo grupo;
- grupos distintos são percebidos como unidades diferentes;
- regiões principais têm respiro suficiente para leitura;
- o canvas não fica simultaneamente apertado em algumas áreas e vazio sem função em outras.

Regras:

- usar o menor valor da escala que preserve clareza dentro de grupos densos;
- aumentar o spacing ao mudar de nível hierárquico;
- manter ritmo consistente entre blocos equivalentes;
- não preencher espaço vazio aumentando gaps sem função;
- não comprimir conteúdo para evitar retornar ao processo documental quando a geometria aprovada se mostrar insuficiente;
- valores fora da escala continuam exigindo justificativa documental conforme a spec técnica.

Se o Wireframe Text fornecer spacing explícito, ele prevalece quando estiver conforme as specs superiores.

---

## 9. Alinhamento e estrutura óptica

A montagem deve usar alinhamento como mecanismo de organização.

Regras obrigatórias:

- compartilhar eixos entre elementos relacionados;
- alinhar títulos de cartões equivalentes pela mesma linha-base ou pelo mesmo eixo;
- alinhar listas e pares rótulo/valor de forma consistente dentro da mesma região;
- preservar margens internas equivalentes em componentes equivalentes;
- evitar deslocamentos de poucos pixels sem motivo documental;
- evitar centralização quando a leitura sequencial ou comparação de valores exigir alinhamento por borda;
- evitar desalinhamento entre ícone e texto causado pelo bounding box da fonte ou do ícone;
- manter elementos de 1 px posicionados de forma a evitar aparência borrada na exportação raster.

Alinhamento óptico pode corrigir a percepção sem alterar a geometria estrutural documentada somente quando o Wireframe Text não tiver fixado a coordenada interna exata do detalhe ajustado e desde que:

- não mude x/y/w/h normativos do elemento;
- ocorra apenas dentro da área interna permitida;
- não altere conteúdo ou hierarquia;
- não crie valor fora das regras técnicas.

---

## 10. Tipografia na imagem

A tipografia técnica deve usar exclusivamente os tokens definidos em `REGRAS-TECNICAS.md`.

Mapeamento por função:

```text
título principal de região técnica
→ WF-TITLE quando o papel for de título principal

seção / título de bloco
→ WF-SECTION

texto corrente / valor principal
→ WF-BODY

rótulo / nome de propriedade / metadado curto
→ WF-LABEL

ação demonstrativa
→ WF-ACTION-TEXT

nota / cota / legenda / informação auxiliar
→ WF-CAPTION
```

O Wireframe Text pode determinar um token específico e, nesse caso, essa decisão prevalece.

Regras de qualidade:

- não reduzir fonte para fazer texto caber;
- não condensar horizontalmente a fonte;
- não usar escala não documentada;
- não alterar tracking técnico de forma arbitrária;
- não misturar famílias sem função definida;
- não usar faux bold ou faux italic quando a fonte correta estiver disponível;
- não rasterizar texto em resolução inferior e depois ampliar;
- manter quebras de linha coerentes com a largura disponível e a hierarquia.

Texto técnico deve permanecer legível em visualização do PNG a 100%.

---

## 11. Superfícies, bordas, divisores e elevação

A função visual deve determinar o recurso usado.

### Superfícies

Quando a composição exigir separação de região e o Wireframe Text não indicar outro tratamento:

- usar o token de fundo da variação para o canvas;
- usar o token de superfície da variação para regiões documentais principais;
- usar a superfície alternativa somente quando uma segunda camada de agrupamento for necessária.

Não criar novas cores por conveniência.

### Bordas e divisores

Usar borda/divisor somente quando spacing, superfície ou alinhamento não forem suficientes para comunicar o limite necessário.

Quando usados:

- respeitar espessura e token vigentes;
- manter aplicação consistente entre regiões equivalentes;
- não criar caixas em todos os textos apenas para preencher a composição.

### Elevação

Elevação indica camada, não decoração.

Usar somente quando houver necessidade real de distinguir profundidade ou sobreposição e somente com valores definidos em `REGRAS-TECNICAS.md`.

Não aplicar sombra genérica a todos os painéis para “deixar bonito”.

---

## 12. Densidade e legibilidade

Uma prancha profissional deve equilibrar quantidade de informação e capacidade de leitura.

Regras:

- conteúdo deve caber sem clipping;
- textos não podem colidir com bordas ou outros elementos;
- títulos não devem parecer comprimidos para caber no bloco;
- blocos equivalentes devem manter densidade visual comparável;
- não reduzir tipografia, ícones ou componentes abaixo das regras para ganhar espaço;
- não aumentar artificialmente o canvas ou alterar o viewport para acomodar conteúdo;
- não usar áreas vazias como justificativa para ampliar elementos sem função;
- não criar excesso de linhas, bordas e caixas que aumentem ruído sem aumentar compreensão.

Quando o conteúdo real não funcionar dentro da geometria aprovada, a montagem não deve improvisar uma solução estrutural. O caso deve retornar ao processo que governa o Wireframe Text.

---

## 13. Componentes e estados demonstrativos

Amostras de componentes devem usar as medidas e tokens vigentes.

Componentes equivalentes devem manter:

- mesma lógica de superfície;
- mesma borda aplicável;
- mesmo radius aplicável;
- mesmo alinhamento interno;
- mesma tipografia por função;
- mesma lógica de ícone;
- mesmo padrão de espaçamento.

Estados devem ser perceptíveis sem depender exclusivamente de cor.

Quando o Wireframe Text solicitar demonstração de estado sem especificar uma aparência exclusiva, usar a menor mudança visual necessária para comunicar o estado com os tokens vigentes, preservando a geometria do componente.

Exemplos de recursos permitidos quando semanticamente aplicáveis:

- mudança de borda;
- indicador de foco;
- mudança de superfície;
- ícone;
- rótulo textual;
- alteração de contraste;
- marca de seleção.

Não inventar uma cor de erro, sucesso ou alerta que não exista nas fontes vigentes.

Se o estado exigir semântica cromática que as specs ainda não fornecem, registrar a insuficiência em vez de criar uma paleta paralela durante a montagem.

---

## 14. Contraste e percepção

A montagem deve preservar legibilidade e percepção dos elementos essenciais.

Critérios adotados para a representação visual:

- texto normal essencial: contraste mínimo de `4.5:1` quando aplicável;
- texto grande: mínimo de `3:1` quando aplicável;
- indicadores visuais essenciais de componentes e estados: mínimo de `3:1` contra cores adjacentes quando aplicável;
- elementos desabilitados podem usar o tratamento técnico previsto para esse estado;
- logotipo preserva sua identidade oficial e não deve ser recolorido apenas para satisfazer um cálculo genérico.

Esses critérios não autorizam alterar tokens canônicos durante a montagem.

Se um par de tokens vigente não atender a um requisito necessário, a inconsistência deve ser devolvida para a fonte normativa correspondente.

---

## 15. Uso de ícones

Quando a documentação exigir iconografia técnica:

- usar a família/referência definida em `REGRAS-TECNICAS.md`;
- usar o tamanho definido para o papel do ícone;
- respeitar o touch target quando o componente demonstrado for interativo;
- preservar alinhamento óptico com texto e componente;
- não substituir ícone por emoji;
- não substituir ícone por letra, símbolo ASCII ou glifo semelhante quando existir referência oficial;
- não misturar famílias de ícone na mesma prancha sem autorização documental.

---

## 16. White e black

Cada variação é executada com seus próprios tokens e ativos específicos.

É proibido:

- renderizar `black` usando bitmap específico de `white`;
- inverter automaticamente um ativo para criar a outra variação;
- aplicar filtro de luminosidade/contraste para simular outra variante;
- misturar tokens `WF-W-*` e `WF-B-*` sem regra explícita.

Quando um ativo físico específico de uma variação não existir, sua ausência não autoriza reconstruir ou adaptar o ativo da outra variação.

A solução deve seguir as regras superiores vigentes e, se necessário, registrar a ausência antes de tratar a imagem como final.

---

## 17. Sequência de montagem visual

Depois de a produção estar liberada, executar a imagem nesta ordem lógica:

```text
01. criar o canvas exatamente nas dimensões canônicas vigentes
02. aplicar o fundo técnico da variação
03. montar o cabeçalho conforme o Wireframe Text
04. inserir ativos físicos oficiais já definidos
05. montar viewport e cotas conforme o Wireframe Text
06. criar regiões documentais na geometria especificada
07. aplicar superfícies, bordas/divisores e elevação somente quando cabíveis
08. inserir títulos e estrutura tipográfica
09. montar componentes e amostras
10. inserir textos, valores, notas e legendas
11. aplicar ícones e estados
12. executar alinhamento óptico interno permitido
13. revisar clipping, colisão, overflow e consistência
14. validar qualidade visual e fidelidade documental
15. exportar PNG sem redimensionamento final
```

Essa sequência não substitui a sequência de construção e gates de `PROCESSO-PRANCHA.md`; ela detalha somente a execução visual depois da liberação da imagem.

---

## 18. Exportação

A saída final deve preservar o canvas canônico em escala `1:1`.

Regras:

- formato final: PNG;
- exportar no tamanho físico definido pelas specs;
- não redimensionar depois da montagem;
- não aplicar compressão destrutiva;
- não converter para JPEG;
- não alterar aspect ratio;
- não adicionar margem externa que não pertença ao canvas;
- usar espaço de cor sRGB quando a ferramenta de exportação permitir controle explícito;
- verificar dimensões do arquivo exportado, não apenas do documento de trabalho.

A ferramenta usada para construir a imagem é intercambiável. O resultado deve obedecer às specs independentemente de ter sido produzido por código, editor gráfico, ferramenta vetorial ou outro meio.

---

## 19. Controle de regressão

### 19.1 Princípio

Depois de existir uma imagem vigente de um frame, uma revisão daquele **mesmo frame** não pode reinterpretar toda a prancha.

Regra obrigatória:

> Tudo que não estiver explicitamente dentro do escopo da alteração deve permanecer equivalente à versão vigente anterior do mesmo frame.

A versão anterior é usada apenas para detectar regressão no mesmo frame.

Ela não substitui o Wireframe Text nem as specs como fonte normativa.

### 19.2 O que comparar

Em uma revisão do mesmo frame, comparar versão nova e versão anterior em todas as áreas não afetadas pelo pedido:

```text
geometria
conteúdo
hierarquia
alinhamento
spacing
quebras de linha
tratamento tipográfico
superfícies
bordas/divisores
radius
elevação
ícones
componentes
estados
ativos físicos
variação white/black
```

Mudança fora do escopo é regressão, mesmo quando isoladamente pareça uma melhoria estética.

### 19.3 Primeira imagem de um frame

Na primeira imagem de um frame ainda não existe baseline raster anterior.

Validar contra:

```text
specs canônicas
+
Wireframe Text específico aprovado
+
contexto operacional e referências vigentes aplicáveis
+
ativos oficiais
+
esta MONTAGEM-IMAGEM.md
```

Uma referência visual de outro frame pode ser consultada para verificar coerência de linguagem e qualidade quando estiver registrada ou for pertinente ao contexto da etapa, mas não substitui a baseline estrutural inexistente nem o Wireframe Text específico.

---

## 20. Versionamento de frame e revisão visual

As regras desta seção se aplicam a **pranchas-modelo e demais artefatos cuja identidade seja versionada por frame/concepção**.

Elas **não redefinem a nomenclatura nem o versionamento das saídas funcionais** controladas por `docs/wireframes/images/README.md`. Quando uma saída funcional possuir regra operacional própria, essa regra permanece vigente.

### 20.1 Versão de frame

O identificador `vNN` representa a versão do **frame/concepção**.

Formato genérico:

```text
<NOME-BASE>_v<FRAME>.png
```

A existência de uma correção, refinamento visual ou ajuste do mesmo frame **não cria automaticamente um novo `vNN`**.

Uma nova versão de frame somente nasce mediante decisão explícita de **NOVO FRAME** e deve possuir o Wireframe Text correspondente adequado à nova concepção antes da produção da imagem.

A montagem da imagem não possui autoridade para promover `v01` para `v02` por conta própria.

### 20.2 Revisão do mesmo frame

Quando uma alteração pertence ao mesmo frame:

1. identificar o arquivo corrente `<NOME-BASE>_v<FRAME>.png`;
2. identificar exatamente o escopo da alteração;
3. preservar a imagem corrente antes de substituí-la;
4. arquivar a imagem substituída com o próximo sufixo sequencial de revisão;
5. executar somente as alterações autorizadas;
6. validar a nova imagem contra as fontes vigentes;
7. comparar contra a imagem arquivada para detectar regressões fora do escopo;
8. a nova imagem continua ocupando o nome canônico do frame, sem o sufixo de revisão.

Histórico:

```text
<NOME-BASE>_v<FRAME>-01.png
<NOME-BASE>_v<FRAME>-02.png
<NOME-BASE>_v<FRAME>-03.png
...
```

Corrente:

```text
<NOME-BASE>_v<FRAME>.png
```

O sufixo `-RR` identifica **snapshots históricos substituídos do mesmo frame**. A localização física desses snapshots deve seguir a estrutura operacional vigente; esta spec não cria nova pasta de ciclo de vida.

Ele não significa novo frame.

Ele não altera o `vNN`.

### 20.3 Ajuste que também altera o Wireframe Text

Se o ajuste visual exigir mudança em decisão documentada no Wireframe Text:

```text
não corrigir apenas o PNG
        ↓
atualizar o Wireframe Text segundo sua própria spec e processo
        ↓
reabrir/aprovar somente os gates realmente afetados
        ↓
liberar novamente a produção da imagem
        ↓
preservar o PNG corrente como revisão histórica do mesmo frame
        ↓
gerar o novo PNG corrente
```

Esta spec **não define o versionamento interno do arquivo Wireframe Text**. Essa responsabilidade permanece no contrato documental e no processo próprios.

### 20.4 Mudança estrutural

Uma mudança estrutural não incrementa `vNN` automaticamente.

Primeiro deve ser classificada pelo responsável:

```text
continua sendo o mesmo frame
→ atualizar o Wireframe Text quando necessário
→ preservar revisão anterior do PNG
→ gerar novamente <NOME-BASE>_v<FRAME>.png

é um NOVO FRAME
→ criar/adequar Wireframe Text do novo frame
→ usar novo vNN explicitamente autorizado
```

A classificação entre “mesmo frame” e “novo frame” não pode ser inferida silenciosamente pela ferramenta de renderização.

---

## 21. Validação profissional antes da aprovação

A validação final possui quatro eixos.

### 21.1 Fidelidade documental

```text
[ ] geometria corresponde ao Wireframe Text
[ ] textos correspondem ao Wireframe Text
[ ] conteúdo não foi resumido ou reescrito
[ ] ativos obrigatórios são os arquivos oficiais
[ ] variação correta foi usada
[ ] tokens correspondem às specs vigentes
[ ] nenhum requisito foi inventado durante a montagem
```

### 21.2 Qualidade visual

```text
[ ] hierarquia é clara na primeira leitura
[ ] regiões principais são distinguíveis sem excesso de decoração
[ ] spacing comunica agrupamento e prioridade
[ ] alinhamentos recorrentes são consistentes
[ ] tipografia segue papéis e tokens previstos
[ ] não há texto comprimido, esticado ou reduzido por conveniência
[ ] não há clipping, overflow ou colisão
[ ] não há ruído excessivo de bordas, linhas ou sombras
[ ] componentes equivalentes possuem tratamento equivalente
[ ] ícones estão alinhados e pertencem à referência correta
[ ] contraste dos elementos essenciais é verificável
[ ] a prancha mantém aparência técnica deliberada, não de rascunho
```

### 21.3 Integridade física

```text
[ ] PNG possui as dimensões físicas corretas
[ ] viewport e ativos 1:1 continuam 1:1 quando exigido
[ ] nenhuma etapa de exportação redimensionou a prancha
[ ] linhas e divisores não ficaram borrados por posicionamento inadequado
[ ] não existe margem externa não documentada
[ ] o arquivo abre sem erro e não está corrompido
```

### 21.4 Não regressão

Aplicável quando existe versão anterior do mesmo frame:

```text
[ ] escopo da alteração foi identificado
[ ] versão anterior foi preservada antes da substituição
[ ] áreas fora do escopo permanecem equivalentes
[ ] nenhuma mudança estética incidental alterou outra região
[ ] nenhuma geometria foi reinterpretada sem alteração documental
[ ] a nova corrente continua com o nome canônico do frame
```

A imagem somente pode avançar para o estado de aprovação definido em `PROCESSO-PRANCHA.md` quando os eixos aplicáveis estiverem satisfeitos.

---

## 22. Falhas que impedem a aprovação

São falhas de montagem:

- depender de memória de conversa para completar aparência;
- copiar estilo ou geometria de outro frame por conveniência;
- reconstruir ativo físico oficial por aproximação;
- usar bitmap da variação errada;
- substituir fonte oficial silenciosamente;
- criar cor, token, radius, sombra ou componente não autorizado;
- alterar texto para fazê-lo caber;
- alterar geometria aprovada para melhorar estética;
- reduzir viewport ou componente normativo;
- introduzir novo requisito durante a renderização;
- usar spacing arbitrário fora das regras vigentes;
- exportar em dimensão diferente e depois reescalar;
- alterar áreas fora do escopo em revisão do mesmo frame;
- criar novo `vNN` apenas porque houve uma correção;
- tratar snapshot `-RR` como nova versão de frame;
- tratar uma imagem de outro frame como baseline obrigatória.

---

## 23. Tratamento de insuficiência documental

Durante a montagem podem ocorrer três situações.

### EXECUTÁVEL

As specs e o Wireframe Text fornecem informação suficiente.

```text
→ executar
→ validar
→ exportar
```

### LACUNA DE MONTAGEM

A composição está definida, mas falta uma decisão necessária exclusivamente para renderizar de forma determinística e a decisão não pode ser obtida pelas regras desta spec.

```text
→ não inventar
→ identificar exatamente a lacuna
→ corrigir a spec de montagem se a regra for genérica
→ corrigir o Wireframe Text se a decisão for específica da prancha
→ gerar novamente
```

### CONTRADIÇÃO

Duas fontes vigentes exigem resultados incompatíveis.

```text
→ não escolher silenciosamente uma delas
→ seguir a hierarquia documental
→ apresentar a contradição quando a hierarquia não for suficiente para resolver
```

Uma lacuna descoberta durante uma imagem serve para evoluir a documentação somente quando representar uma necessidade real e reproduzível.

Não adicionar regras especulativas “para o futuro” sem ocorrência concreta ou fundamento técnico.

---

## 24. Critério de evolução desta spec

Esta spec deve evoluir a partir de:

- problemas reais encontrados na montagem;
- regressões comprovadas;
- necessidades repetíveis entre diferentes templates;
- mudanças nas specs superiores;
- pesquisa técnica atual quando houver benefício concreto para o processo.

Antes de adicionar uma nova regra, verificar:

```text
1. o problema pertence realmente à montagem da imagem?
2. já existe regra equivalente em outra spec?
3. a regra é genérica ou específica de uma prancha?
4. ela reduz ambiguidade real?
5. ela pode ser verificada objetivamente?
6. ela cria conflito com uma responsabilidade existente?
```

Se a regra for específica de uma prancha, ela pertence ao Wireframe Text específico e não a este arquivo.

Se a regra redefinir uma invariante técnica, ela pertence a `REGRAS-TECNICAS.md`.

Se a regra alterar gates ou sequência do processo, ela pertence a `PROCESSO-PRANCHA.md`.

Se a regra for de estrutura operacional de diretório, ela pertence ao README operacional correspondente.

---

## 25. Resultado esperado

A aplicação desta spec deve permitir que uma execução sem memória anterior produza uma imagem que seja simultaneamente:

```text
fiel ao Wireframe Text
+
compatível com as regras técnicas
+
visualmente profissional
+
consistente entre regiões equivalentes
+
executável com ativos oficiais
+
verificável objetivamente
+
protegida contra regressão em revisões do mesmo frame
```

O objetivo não é fazer todas as pranchas parecerem iguais.

O objetivo é fazer todas as pranchas serem construídas com o **mesmo nível de disciplina visual e técnica**, preservando a composição específica de cada frame.
