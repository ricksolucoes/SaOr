# SaOr — Contrato documental do Wireframe Text individual da Tela

## 1. Natureza, autoridade e ordem obrigatória

Este contrato é auxiliar da **SPEC 3** ([`PROCESSO-TELA-PRANCHA.md`](PROCESSO-TELA-PRANCHA.md)) e trata **somente da documentação da Tela funcional**, não da criação de uma Prancha do Template (SPEC 1) nem da referência selecionada e congelada (SPEC 2). O contrato histórico [`WIREFRAME-TEXT.md`](WIREFRAME-TEXT.md) continua exclusivo da Prancha do Template. Os requisitos funcionais vêm de [`docs/Documento_Mestre.md`](../../docs/Documento_Mestre.md); as dimensões, tokens e invariantes vêm de [`REGRAS-TECNICAS.md`](REGRAS-TECNICAS.md).

**Ordem obrigatória:** inventário funcional GI-0 → **PNG de proposta da Tela isolada** → inspeção e aprovação visual GI-1 → **Wireframe Text/TextFrame construído a partir desse PNG aprovado** → confronto e aprovação documental GI-2 → composição e aprovação da Prancha GI-3/GI-4. **É proibido utilizar o Wireframe Text como substituto de um PNG visual prévio**, iniciar por um esquema de coordenadas para deduzir a aparência ou declarar aprovado um TextFrame sem o PNG que lhe deu origem.

O PNG de GI-1 é a **proposta visual da Tela de Referência**, não um template, uma Prancha nem um PNG já congelado. Ao receber aprovação visual, fica vinculado a um SHA-256 imutável; somente após o GI-2 o **conjunto PNG + Wireframe Text** é considerado documentalmente aprovado e congelado para montagem. Correção de pixels após aprovação GI-1 exige nova submissão visual e invalida a aprovação documental dependente; nunca reescrever a imagem aprovada silenciosamente.

## 2. Unidade, caminhos e origem da evidência

O Wireframe Text nasce **somente depois da aprovação GI-1**, para cada ID funcional, tema, página e versão, em:

`docs/wireframes/images/<tema>/telas/wiframetext/<ID>-<PÁGINA>-<TOTAL>_v<VERSÃO>.md`.

Ele referencia obrigatoriamente o **PNG visual que já existe**, em `docs/wireframes/images/<tema>/telas/design/01_Mobile_360x800/<mesmo-nome-base>.png`, e o registro de decisões GI-0/GI-1 em `docs/wireframes/images/<tema>/telas/controle/<mesmo-nome-base>.md`. Os registros de controle são provas de aprovações anteriores ao TextFrame, **não são TextFrames, não contêm uma composição alternativa e não substituem esta SPEC**. Somente criar essas pastas na produção autorizada de uma interface; não criar arquivos funcionais por alteração normativa.

O PNG principal mostra o estado/posição selecionado e documentado. Quando houver estados alternativos **realmente previstos ou aprovados**, conservar PNGs individualizados com sufixo `_estado-<identificador>.png`, mesma base de nome, dimensão e tema. O documento deve listar cada estado/variante, caminho, hash e diferença em relação ao PNG principal; não presumir que todo elemento possui variantes. Os IDs são os do Documento Mestre. A quantidade `PÁGINA/TOTAL` descreve posições da mesma interface durante rolagem; `vNN` descreve revisão, não nova página.

**Compatibilidade histórica:** artefatos V1 já aprovados e congelados que tenham sido entregues com `__estado-` conservam seus nomes e vínculos originais, sem renomeação retroativa. O padrão normativo **para novos artefatos e para T00 V2** é um único `_estado-`. A documentação histórica V1 não é redefinida por esta atualização.

**Escopo de execução do MVP vigente:** somente Mobile `360 × 800 px`, white e black. Os diretórios Tablet, Notebook e Desktop são reservas físicas para MVP futuro, **não** autorizam produção de variantes nem mudanças dos contratos nesta etapa. O caminho do PNG de estado alternativo usa o mesmo diretório `design/01_Mobile_360x800/` e o sufixo `_estado-<identificador>.png`; o arquivo `.md` mantém sua pasta `telas/wiframetext/`.

## 3. Fonte de verdade e fidelidade visual

O **PNG visual aprovado em GI-1 é a fonte verificável da composição visual desta versão**. O Documento Mestre e as regras técnicas são as autoridades de requisitos e invariantes: se o PNG contrariá-los, **reprovar GI-1**, não reescrever a baseline nem fazer o TextFrame justificar um erro visual. O template vigente orienta padrões técnicos aplicáveis e a futura Prancha; não impõe componentes demonstrativos à Tela.

O TextFrame deve **representar a Tela que já foi aprovada em imagem**. Exigir simultaneamente:

1. **Referência visual inequívoca:** caminho do PNG original, tema, ID, página/total, versão, estado, dimensões `360 × 800`, SHA-256 e referência à decisão GI-1. O leitor deve poder abrir a imagem verdadeira sem interpretar um diagrama.
2. **TextFrame fiel ao PNG:** representação textual organizada na mesma ordem de leitura, com agrupamento, alinhamento, rótulos exatos, indicadores, estados e relações visuais. Elementos adicionais ou ausentes em relação ao PNG são **NÃO CONFORMES**. Um desenho em caracteres não substitui o PNG; serve de índice textual fiel à imagem aprovada.
3. **Geometria exata e completa:** para cada elemento visível, caixa local `x/y/w/h` em pixels, alinhamento, espaçamentos, limites, sobreposições intencionais e relações pai/filho, confrontadas com a imagem em `360 × 800`. **Não utilizar coordenadas aproximadas, 'a critério', 'ajustar depois' ou intervalos genéricos** como definição final.
4. **Aparência por tema:** tokens e cores efetivamente usados, superfícies, tipografia/peso/tamanho, ícones/glyphs, contornos, estados, contraste e espaçamento, com identificação da fonte normativa; discriminar white e black sem impor uma única representação cromática aos dois.
5. **Conteúdo e comportamento:** cada texto/campo/ação/destino/retorno/estado e sua fonte funcional; AppBar específica da Tela; indicação de presença ou ausência de ícone em **cada** item de lista conforme requisito. Indicador de status é componente **informativo**, não botão, salvo requisito funcional expresso em contrário; documentar variantes somente quando exigidas/autorizadas e representar texto e ícone juntos.
6. **Inventário de completude:** mapear cada elemento exigido → página/estado → caixa na imagem → componente no TextFrame → origem funcional. Não copiar o catálogo do template; registrar somente componentes efetivamente usados, com notas técnicas pertinentes aos futuros Itens 10 e 14 da Prancha.
7. **Rolagem real:** cada PNG/página `360 × 800` mostra uma posição efetiva da mesma interface; registrar offset ou marco de deslocamento, elementos fixos (apenas com fonte comprovada), elementos roláveis, continuidade e cobertura integral. Não cortar, reduzir, omitir ou reiniciar campos. A paginação e as variantes devem refletir o que foi efetivamente aprovado visualmente.
8. **Rastreabilidade e aceite:** status, responsável e data da aprovação GI-1 vinculados a cada hash; avaliação de conformidade do TextFrame contra o PNG; decisão humana GI-2 datada e vinculada à versão exata. Registrar pendências e retorno ao Gate correto.

**Critério eliminatório:** um mapa com 'banda y', régua, árvore de componentes, tabela de coordenadas ou pseudoimagem com posição horizontal aproximada **não constitui, isoladamente, um TextFrame visual suficiente**, mesmo que contenha as palavras corretas. É obrigatório o PNG real aprovado, sua inspeção visual e a correspondência pixel/geometria/conteúdo verificável. Se qualquer reprodução depender de interpretação do executor ou de um prompt, o GI-2 fica `NÃO CONFORME`.

## 4. Estados, aprovações e revisão

Estados próprios do Wireframe Text: `PENDENTE`, `EM DEFINIÇÃO`, `AGUARDANDO APROVAÇÃO`, `APROVADO E CONGELADO` e `BLOQUEADO` (ou `NÃO APLICÁVEL` fundamentado). **GI-1 aprova somente o PNG visual**, não o texto futuro. GI-2 requer simultaneamente: PNG visual previamente aprovado e íntegro, TextFrame reproduzindo esse PNG, verificação de requisitos e aprovação humana específica do documento. Apenas então a Tela de Referência **e o Wireframe Text** podem ficar `APROVADO E CONGELADO` para montagem da Prancha.

Mudança de conteúdo, geometria, estado, paginação ou pixels após GI-1 exige nova versão ou nova revisão aprovada com cadeia de evidências, preservando artefatos já aprovados. Modificar apenas o TextFrame para mascarar discrepância com PNG é proibido. O conjunto completo white/black deve ter aprovações específicas por tema/página/estado aplicável e avaliação de equivalência funcional.

### Medidas verificáveis versus informações não recuperáveis do raster

A medição de bordas, regiões e caixas visíveis deve indicar **coordenadas inteiras mensuradas no PNG**, seu método e a convenção `[x,y,w,h]`; não converter estimativas em cotas exatas. O bitmap **não permite inferir com certeza** família tipográfica, peso, padding original, tamanho lógico de fonte nem nomes de componentes de uma ferramenta externa. Essas propriedades só serão declaradas como normativas quando tiverem fonte técnica independente; caso contrário, registrar `não comprovado no raster` e bloquear a afirmação de reprodução paramétrica exata, sem inventar valores. A reprodução **visual** continua ancorada no PNG aprovado por hash.

## 5. Testes obrigatórios de correspondência (GI-2)

- [ ] Existe PNG da Tela do mesmo ID/tema/página/versão, fisicamente aberto e inspecionado; seu SHA-256 coincide com a aprovação GI-1 registrada **antes** da elaboração do TextFrame.
- [ ] Tela e estados exigidos são visualmente fiéis às fontes funcionais e técnicas; não foram inventados componentes ou interações.
- [ ] Todos os componentes exibidos no PNG constam no TextFrame e na tabela geométrica; todos os componentes descritos aparecem no PNG ou têm condição de estado justificada.
- [ ] Textos, ícones, tipografia, superfícies, alinhamentos, dimensões e posicionamentos coincidem com a imagem; **nenhuma cota aproximada** substitui medida verificável.
- [ ] O mapa de páginas/rolagem preserva campos, ordem e comportamento, sem duplicação indevida ou compressão.
- [ ] White e black preservam semântica, navegação, hierarquia e páginas e respeitam seus tokens próprios.
- [ ] Evidências GI-0 e GI-1 estão em arquivos do repositório com caminho, hash, data e decisão; GI-2 possui resultado itemizado e aprovação humana explícita.

**Falha em qualquer item obrigatório bloqueia GI-2.** Não criar Prancha de Implementação a partir de PNG ou TextFrame não aprovados. Não reexecutar os Gates da construção do Modelo C.
