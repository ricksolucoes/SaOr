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
- tratamento cromático, cores semânticas e relação entre cor, superfície e estado;
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

### 3.1 Preservação cromática integral da prancha

A montagem deve preservar o **tratamento cromático esperado da composição inteira**, e não apenas de blocos que documentem paleta, tokens ou estados.

A cor de cada elemento deve ser obtida da fonte documental ou visual aplicável ao seu papel:

- ativo físico oficial preserva sua própria cromia;
- token ou regra cromática explícita deve ser aplicada ao elemento correspondente;
- o Wireframe Text específico prevalece quando registrar cor ou tratamento próprio da composição;
- referência visual contextual vigente pode orientar continuidade de uso de cor, contraste, destaque, superfície e semântica visual quando uma fonte superior não determinar tratamento diferente.

As variações `white` e `black` representam **temas de representação**, não modos monocromáticos. Uma prancha `white` ou `black` pode conter cores cromáticas, destaques e cores semânticas previstas pelas fontes vigentes.

É proibido durante a montagem:

- dessaturar a composição por simplificação;
- converter a prancha para escala de cinza sem determinação documental explícita;
- neutralizar cores cromáticas existentes em referências, ativos ou tokens aplicáveis;
- substituir `Primary`, `Secondary`, `Info`, `Success`, `Warning`, `Error` ou qualquer outra cor semântica aplicável por cinza apenas para uniformizar a prancha;
- remover cores de ações, estados, ícones, superfícies, destaques, bordas ou componentes quando a cromia fizer parte da representação esperada;
- inventar nova cor quando nenhuma fonte aplicável fornecer base suficiente.

Preservar a cromia não autoriza copiar a geometria, o conteúdo ou a composição específica de outra prancha.

Quando não for possível determinar com segurança a cor de um elemento exigido, tratar o caso como insuficiência documental conforme esta spec, em vez de convertê-lo automaticamente para um tom neutro.

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

### 5.1 Regra de execução restritiva

A montagem deve ser tratada como **execução determinística por etapas congeladas**.

Não existe liberdade para:

- reinterpretar a composição para fazê-la caber;
- criar fluxo paralelo de montagem;
- substituir uma etapa por outra estratégia;
- reduzir canvas, viewport, componente ou tipografia por conveniência;
- inventar ícone, modal, navegação, estado, componente ou tratamento visual sem antes consultar as fontes vigentes;
- continuar para a etapa seguinte quando a etapa atual apresentar overflow, colisão, compressão, dimensão incorreta ou conteúdo fora dos limites.

A execução deve parar na primeira inconformidade física ou documental encontrada.

A regra geral é:

```text
medida exata
→ conteúdo real
→ validação
→ congelamento
→ próxima etapa
```

Uma etapa congelada não pode ser redimensionada, deslocada ou reinterpretada para acomodar uma etapa posterior sem alteração documental autorizada.

### 5.2 Pré-layout obrigatório no tamanho final

Antes do acabamento visual de qualquer região, deve existir um **pré-layout no tamanho físico final**.

O pré-layout não é uma caixa vazia meramente ilustrativa. Ele deve usar:

- `x`, `y`, `w` e `h` reais;
- texto real ou conteúdo representativo suficiente para comprovar ocupação física;
- tipografia real prevista para a região;
- ícones, componentes e cotas em seus tamanhos reais quando já definidos;
- margens, paddings e gaps reais;
- ativos `1:1` em suas dimensões reais quando aplicáveis.

Objetivo obrigatório:

> comprovar que a informação cabe fisicamente dentro da área antes da montagem visual definitiva.

É proibido considerar um bloco aprovado apenas porque o retângulo externo cabe no canvas.

O bloco somente pode avançar quando seu conteúdo real também couber sem:

- clipping;
- overflow;
- colisão;
- compressão tipográfica;
- redução indevida de componente;
- saída de informação para fora do card;
- alteração de medida normativa.

### 5.3 Preservação dimensional durante toda revisão

As dimensões normativas devem ser verificadas **antes e depois de cada rodada de ajuste**.

Quando a prancha definir canvas `1280 × 1920 px` e viewport `360 × 800 px`, a condição de entrada e de saída da revisão deve permanecer:

```text
ANTES
canvas   = 1280 × 1920 px
viewport = 360 × 800 px em 1:1

DEPOIS
canvas   = 1280 × 1920 px
viewport = 360 × 800 px em 1:1
```

É proibido:

- editar em resolução reduzida e ampliar posteriormente;
- reduzir a prancha para facilitar a montagem;
- redimensionar o viewport junto com o canvas;
- exportar em outra resolução e reescalar;
- alterar coordenadas ou dimensões congeladas sem mudança documental autorizada.

### 5.4 Proibição de ramificação de solução

Durante a correção do mesmo frame, a execução deve permanecer no **mesmo fluxo de montagem e na mesma composição aprovada**.

Não criar:

- fluxo A / fluxo B;
- alternativa visual paralela;
- composição substituta;
- renderer conceitualmente diferente para resolver um problema local;
- nova interpretação completa da prancha.

Correções do mesmo frame devem ser incrementais e restritas ao escopo autorizado.

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

Para componentes técnicos e amostras de interface, usar somente quando houver necessidade real de distinguir profundidade ou sobreposição e somente com os valores `WF-ELEVATION-*` definidos em `REGRAS-TECNICAS.md`.

Uma sombra pode existir como **tratamento documental da própria prancha** quando o Wireframe Text específico aprovado a definir explicitamente para superfícies de apresentação, cabeçalhos ou cartões documentais. Essa sombra:

- pertence somente à composição específica documentada;
- não substitui os tokens `WF-ELEVATION-*` de componentes;
- não cria novo token universal;
- não deve ser herdada por outra prancha apenas por semelhança visual.

Na variação `black`, a sombra preta é pouco perceptível sobre superfície escura. Amostras de elevação do `black` seguem a regra de `REGRAS-TECNICAS.md`, seção 8: preenchimento em `WF-B-SURFACE-ALT`, sem criar token novo e sem copiar do white a percepção de sombra.

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

A fonte normativa das cores, dos níveis de contraste e das exceções registradas é `REGRAS-TECNICAS.md`, seção 6. Os critérios acima são conferidos contra as tabelas dessa seção.

Esses critérios não autorizam alterar tokens canônicos durante a montagem nem neutralizar a cromia esperada da prancha para obter contraste por conveniência.

Ajuste de contraste deve preservar a função cromática documentada. Se um par de tokens vigente não atender a um requisito necessário, a inconsistência deve ser devolvida para a fonte normativa correspondente, em vez de substituir silenciosamente a cor por cinza, preto ou branco.

---

## 15. Uso de ícones e consulta contextual obrigatória

A escolha ou desenho de qualquer ícone deve ocorrer **somente depois da consulta ao contexto vigente**.

A sequência obrigatória é:

```text
1. identificar que o elemento exige ícone
2. consultar REGRAS-TECNICAS.md
3. consultar o Wireframe Text específico
4. consultar docs/wireframes/images/README.md
5. localizar referências técnicas aplicáveis
6. localizar referências visuais contextuais aplicáveis
7. verificar se existe ativo, família, variante ou representação já definida
8. verificar como a iconografia já é usada em componentes equivalentes
9. somente então inserir o ícone
10. validar tamanho, alinhamento, estilo e touch target
```

Quando a documentação determinar uma família ou referência, essa definição é obrigatória.

Quando existir ativo oficial, usar o ativo oficial.

Quando existir representação visual já consolidada para o mesmo componente ou linguagem da etapa, ela deve ser consultada para preservar continuidade.

É proibido:

- desenhar um ícone próprio por conveniência;
- substituir ícone por emoji;
- substituir ícone por letra, símbolo ASCII ou glifo semelhante quando houver referência aplicável;
- inventar família visual;
- misturar famílias sem autorização;
- mudar o estilo de ícone durante correção de outro problema;
- usar memória de conversa como fonte primária quando o projeto contém referência documental ou visual aplicável.

Se as fontes vigentes não forem suficientes para determinar o ícone:

```text
→ classificar como LACUNA DE MONTAGEM
→ não inventar
→ não avançar como se estivesse resolvido
```

A mesma consulta contextual é obrigatória, quando houver representação já estabelecida, para:

- App Bar;
- Bottom Navigation;
- Modal / Dialog;
- campos;
- botões;
- listas;
- estados;
- indicadores;
- cotas técnicas;
- demais componentes demonstrativos.

---

## 16. White e black

Cada variação é executada com seus próprios tokens (`REGRAS-TECNICAS.md`, seção 6) e ativos específicos, incluindo o bitmap do viewport da própria variação.

`white` e `black` definem a variação de tema da representação. Eles **não significam escala de cinza** e não autorizam remover cores cromáticas ou semânticas que pertençam à composição esperada.

Destaques, ações, estados, feedbacks, ícones, superfícies e demais elementos coloridos devem preservar as cores aplicáveis à variação conforme as fontes vigentes.

É proibido:

- renderizar `black` usando bitmap específico de `white`;
- inverter automaticamente um ativo para criar a outra variação;
- aplicar filtro de luminosidade/contraste para simular outra variante;
- misturar tokens `WF-W-*` e `WF-B-*` sem regra explícita.

Quando um ativo físico específico de uma variação não existir, sua ausência não autoriza reconstruir ou adaptar o ativo da outra variação.

A solução deve seguir as regras superiores vigentes e, se necessário, registrar a ausência antes de tratar a imagem como final.

---

## 17. Sequência obrigatória de montagem da prancha

Esta sequência é **normativa, linear e bloqueante**.

Nenhuma etapa posterior pode ser usada para corrigir uma etapa anterior.

### 17.1 Etapa 1 — Criar a prancha no tamanho exato

Criar o canvas diretamente nas dimensões canônicas vigentes.

Quando o canvas aprovado for `1280 × 1920 px`:

```text
canvas = 1280 × 1920 px
escala = 1:1
orientação = retrato
```

Validar a dimensão física do documento antes de inserir qualquer conteúdo.

**Bloqueio:** se o canvas não estiver na dimensão normativa, não avançar.

### 17.2 Etapa 2 — Montar e validar título/cabeçalho

Montar o cabeçalho **dentro da prancha já criada**, usando:

- dimensões reais;
- textos reais;
- tipografia real;
- metadados reais;
- status real;
- divisões internas reais.

Verificar:

- se o título cabe;
- se o subtítulo cabe;
- se status e metadados permanecem dentro de suas células;
- se existe respiro suficiente;
- se nenhum texto está comprimido;
- se nenhuma informação toca ou atravessa os limites.

Ajustes de altura ou distribuição interna só podem ocorrer dentro da autoridade documental aplicável.

Depois da validação, congelar a geometria do cabeçalho.

**Bloqueio:** não montar viewport nem demais blocos enquanto o cabeçalho não estiver fisicamente correto.

### 17.3 Etapa 3 — Inserir e validar o viewport

Inserir o viewport oficial nas dimensões físicas definidas.

Quando a regra exigir `360 × 800 px` em `1:1`:

```text
viewport = 360 × 800 px
escala = 1:1
resize = proibido
crop = proibido
stretch = proibido
reconstrução = proibida quando existir ativo oficial
```

Montar também as cotas previstas no Wireframe Text.

Validar:

- posição;
- largura;
- altura;
- escala;
- relação das cotas com o bitmap;
- ausência de sobreposição indevida.

Depois da validação, congelar viewport e cotas.

**Bloqueio:** o viewport não pode ser redimensionado posteriormente para abrir espaço para outro conteúdo.

### 17.4 Etapa 4 — Calcular o espaço realmente restante

Somente depois de cabeçalho e viewport estarem congelados, calcular a área ainda disponível para os demais elementos.

É proibido diminuir, deslocar ou comprimir elementos congelados para criar espaço artificialmente.

### 17.5 Etapa 5 — Fazer o pré-layout dos demais blocos

Criar cada bloco no `x/y/w/h` final que terá na prancha.

O pré-layout deve conter informação real suficiente para validar ocupação física, conforme a seção 5.2.

Para cada bloco:

```text
1. criar caixa no tamanho final
2. inserir conteúdo real/representativo no tamanho real
3. aplicar tipografia real
4. reservar espaço real para ícones, cotas e ações
5. verificar limites internos
6. verificar overflow e colisão
7. verificar se toda informação permanece dentro do card
8. somente então congelar o bloco
```

**Bloqueio:** se qualquer informação ultrapassar o limite do bloco, o bloco está reprovado.

### 17.6 Etapa 6 — Consultar o contexto antes de montar cada componente

Antes de montar visualmente App Bar, Bottom Navigation, Modal, ícones, estados ou qualquer outro componente, executar a consulta contextual obrigatória:

```text
REGRAS-TECNICAS.md
→ Wireframe Text específico
→ docs/wireframes/images/README.md
→ referências técnicas aplicáveis
→ referências visuais contextuais aplicáveis
→ ativos/famílias/representações existentes
→ somente então montar
```

A ausência de consulta não autoriza dedução visual.

Quando o contexto não fornecer informação suficiente:

```text
→ LACUNA DE MONTAGEM
→ não inventar
```

### 17.7 Etapa 7 — Montar cada elemento separadamente

Montar cada elemento dentro da caixa já validada no pré-layout.

Para cada elemento:

- preservar `x/y/w/h` congelados;
- preservar tipografia;
- preservar dimensões de componente;
- preservar iconografia contextual;
- preservar cromia aplicável;
- preservar conteúdo;
- manter toda informação dentro dos limites.

Depois de montado, validar o elemento isoladamente antes de integrá-lo à prancha.

### 17.8 Etapa 8 — Unir os elementos na prancha

Somente elementos já validados podem ser inseridos na composição final.

Durante a união é proibido:

- escalar o bloco para caber;
- redimensionar o canvas;
- redimensionar o viewport;
- alterar componente já validado;
- reinterpretar estilo;
- deslocar informação para fora do card.

### 17.9 Etapa 9 — Validar a prancha completa

Antes da exportação, validar obrigatoriamente:

```text
[ ] canvas mantém dimensão normativa
[ ] viewport mantém dimensão normativa em 1:1
[ ] cabeçalho permanece congelado e íntegro
[ ] todos os cards respeitam seus limites
[ ] nenhuma cota sai do card ao qual pertence
[ ] nenhum texto está comprimido ou cortado
[ ] ícones correspondem ao contexto vigente
[ ] Modal / Dialog preserva a linguagem contextual aplicável
[ ] Bottom Navigation preserva a linguagem contextual aplicável
[ ] nenhuma área fora do escopo foi reinterpretada
[ ] não ocorreu regressão de geometria, conteúdo, iconografia ou estilo
[ ] o inventário de cores da imagem contém somente tokens da variação (tolerância de antialias)
[ ] nenhum token da outra variação aparece na imagem
```

Se qualquer item falhar, não exportar como final.

### 17.10 Etapa 10 — Exportar sem redimensionamento

Exportar diretamente no tamanho físico da prancha.

Depois da exportação, reabrir o PNG e verificar novamente:

- largura;
- altura;
- viewport `1:1`;
- ausência de resize global;
- ausência de margem externa não documentada.

A exportação não pode corrigir ou compensar erro de montagem.

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
tratamento cromático
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
[ ] cores e tratamentos cromáticos correspondem às fontes vigentes
[ ] nenhum elemento cromático esperado foi neutralizado ou convertido para cinza por conveniência
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
[ ] consulta contextual de iconografia/componentes foi executada antes da montagem
[ ] nenhum ícone ou componente foi inventado por conveniência
[ ] nenhuma informação ultrapassa o limite do card ao qual pertence
[ ] contraste dos elementos essenciais é verificável
[ ] cromia, destaques e cores semânticas permanecem coerentes com a representação esperada
[ ] a prancha mantém aparência técnica deliberada, não de rascunho
```

### 21.3 Integridade física

```text
[ ] PNG possui as dimensões físicas corretas
[ ] dimensões normativas foram verificadas antes da revisão
[ ] dimensões normativas foram verificadas depois da revisão
[ ] pré-layout utilizou tamanho final e conteúdo real/representativo suficiente
[ ] cabeçalho foi congelado antes da inserção do viewport
[ ] viewport foi congelado antes da montagem dos demais blocos
[ ] viewport e ativos 1:1 continuam 1:1 quando exigido
[ ] viewport não foi redimensionado para acomodar a composição
[ ] nenhum bloco congelado foi redimensionado para abrir espaço
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
- pular a sequência obrigatória da seção 17;
- iniciar acabamento sem pré-layout físico validado;
- aprovar pré-layout apenas pela caixa externa sem verificar o conteúdo real;
- continuar a montagem com conteúdo fora do limite do card;
- alterar dimensão de etapa já congelada para acomodar etapa posterior;
- criar fluxo paralelo, alternativa visual ou nova composição para corrigir problema local;
- definir ícone ou componente sem executar a consulta contextual obrigatória;
- inventar ícone, modal, navegação ou estado quando houver contexto aplicável ou quando a informação for insuficiente;
- copiar estilo ou geometria de outro frame por conveniência;
- reconstruir ativo físico oficial por aproximação;
- usar bitmap da variação errada;
- substituir fonte oficial silenciosamente;
- criar cor, token, radius, sombra ou componente não autorizado;
- dessaturar, neutralizar ou converter para escala de cinza uma composição originalmente colorida sem determinação documental explícita;
- substituir uma cor semântica ou cromática aplicável por tom neutro apenas por simplificação visual;
- alterar texto para fazê-lo caber;
- alterar geometria aprovada para melhorar estética;
- reduzir viewport ou componente normativo;
- introduzir novo requisito durante a renderização;
- usar spacing arbitrário fora das regras vigentes;
- exportar em dimensão diferente e depois reescalar;
- pular a pré-validação geométrica e montar a prancha diretamente;
- redimensionar o viewport para fazer a composição caber;
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
