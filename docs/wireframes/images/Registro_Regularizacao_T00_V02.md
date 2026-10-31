# SaOr — Registro sequencial da regularização V2 de T00 Mobile

**Natureza:** evidências de transição documental; não substitui as SPECs, decisões de aprovação de interface ou os registros canônicos de vigência.  
**Base inicial da análise (histórica):** `SaOr-main-Casa.zip` — SHA-256 `36cd7eb01486df0c220c1584fcdf16f5f863bc6da1e0b6361a271ea52e1636eb`. A base de execução atual está identificada no adendo final.  
**Data do registro técnico:** 30/10/2026.  
**Escopo:** somente Mobile `360 × 800`, white/black; não produzir T00.1 ou versões Tablet/Notebook/Desktop.

## GV2-00 — Fixação da base e classificação

**Situação:** `CONCLUÍDO — conferência técnica`, mediante os testes abaixo. Esta conclusão não é aprovação de uma nova interface.

| Evidência | Resultado verificado |
|---|---|
| Inventário | 105 arquivos físicos; 45 PNGs e 40 Markdown; quatro vídeos apenas inventariados (conteúdo não examinado) |
| Integridade ZIP | Sem membros inválidos no teste do arquivo físico |
| V1 | PNGs e documentos existentes não modificados; referências históricas permanecem no repositório |
| V2 | 6 PNGs: 2 Telas principais, 2 variantes Desconectada e 2 Pranchas; dimensões conforme os respectivos contratos |
| Aplicação no ViewPort | Recorte `(x=40,y=272,w=360,h=800)` idêntico, pixel a pixel, à Tela V2 principal de cada tema |
| Seleção de template | Registro oficial ainda seleciona Modelo C; nenhuma V2 de arquivo de template no clone |
| Classificação | V2 altera a interface funcional e o conteúdo demonstrativo de sua Prancha; **não** representa nova versão do template oficial |

| Tema | Pixels V1↔V2 | Pixels estados V2 | Caixa de diferenças dos estados | SHA Tela V2 | SHA estado V2 | SHA Prancha V2 |
|---|---:|---:|---|---|---|---|
| `white` | 48700 | 1428 | `(68, 150, 204, 174)` | `0442412875e3c45b85038d75d8b628f16c94c4ba06529d1c0c97a32d47761504` | `0e4a2da069611f52064c9a3e60f27536ebef21fd787ee9829a70d635de750e90` | `310bbac69366d6f57279ca30f2858d0489ca17e370120819b0594c18c06a9fae` |
| `black` | 47237 | 1410 | `(68, 150, 204, 174)` | `0d4baf7b7d4e12a59db8646dc6317976a860b573abd14745def152ea64b34950` | `d9d70702af9473bad1688faae215ca14fdd5e294c076e32a3c4526e3d33dbe77` | `564cddc9a492810298be96c811487e702ab8273ee1a6bfe8d153db6741354efd` |

### Classificação de diferenças visuais e documentais

| Diferença visível V2 | Responsabilidade | Fonte / restrição |
|---|---|---|
| Cartões individuais com tratamento de superfície, sem a borda V1 | Candidato a padrão visual funcional; só os parâmetros efetivamente verificados podem ser compartilhados | PNGs V2 white/black + `REGRAS-TECNICAS.md` |
| Ícones novos em API, Tema, Diagnóstico e Restaurar | Iconografia específica a cada finalidade; não impor glyph exclusivo de T00 a outras interfaces | PNGs V2 e requisitos individuais |
| Texto `Claro` (white) / `Escuro` (black) junto a Tema | Decisão individual da visualização T00 V2; não se torna texto obrigatório em outra interface | Documento Mestre / PNG V2; substitui a ocultação **histórica V1** |
| Subtítulo `Verificar integridade do app` | Texto visual específico de T00; não declara nova ação ou endpoint | PNG V2; comportamento funcional continua o da ficha T00 |
| Restaurar destacado como ação destrutiva em cartão próprio | Tratamento contextual de ação destrutiva, condicionada a requisito funcional | PNG V2 / destino `M00.5` |
| `Versão 1.0.0` no rodapé do conteúdo | Informação individual não interativa | PNG V2 / Documento Mestre |
| Item 10 e Item 14 específicos | Dados de composição da Prancha funcional, não parte do template congelado | PNGs das Pranchas V2 / contratos individuais |
| Nome `v02_estado-desconectada` (um `_`) | **Avaliação original posteriormente revogada**: o nome físico já atende à convenção corrigida de um sublinhado; não renomear a V2 | Contrato `WIREFRAME-TEXT-TELA.md` §2, corrigenda abaixo |

### Hashes protegidos do template oficial

| Arquivo | SHA-256 comprovado |
|---|---|
| `docs/wireframes/images/white/template/WF-TEMPLATE-C_v02.png` | `558d108e3b0fec923e478482749c678f4b50d8b09055441ee52a9392b0f4929d` |
| `docs/wireframes/images/white/template/WF-TEMPLATE-C_v02.md` | `89154c5c1dda6f1aa1a16ac85a641a3ddc3101da8011f727eaec2c68141980c7` |
| `docs/wireframes/images/white/template/WF-VIEWPORT-360x800.png` | `7de6522e31df89c8925093691442726ef7f72724bcde5905fb3380e4c5c5687c` |
| `docs/wireframes/images/black/template/WF-TEMPLATE-C_v01.png` | `a1c6816cd14e0ea74f1bfb02842581dd7f3fa400c190087cbfa33e93f3b3cb63` |
| `docs/wireframes/images/black/template/WF-TEMPLATE-C_v01.md` | `60e1a8f476fc36233033d3c99f1588f21ee560967c31d6a31f6fb13e43b1892b` |
| `docs/wireframes/images/black/template/WF-VIEWPORT-360x800.png` | `fde139557c36375f5ce569f4884822d4fd7c8344da1ce777b72873e1885a73fd` |

## GV2-01 — Reestruturação normativa

**Situação histórica deste registro de transição:** `EM EXECUÇÃO / AGUARDANDO ACEITE FORMAL DA REVISÃO`. O aceite posterior e a nova situação estão documentados no adendo de continuidade ao final.

A versão anterior de `PROCESSO-TELA-PRANCHA.md` possui SHA-256 `73f898cb7f30a3ad9c1cdb59ee435938206bff2900b9ce24886362578a9411ef`. Abaixo está preservado **integralmente** o conteúdo particular do Modelo C e de T00 que será retirado das regras permanentes neste Gate. O texto preservado é prova histórica de migração, **não** uma fonte normativa concorrente. Seu destino definitivo, sujeito ao GV2-02, será o contrato de utilização do template concreto e o controle específico da interface T00.


### Validação itemizada do GV2-01 — execução técnica parcial

| Critério | Resultado | Evidência |
|---|---|---|
| G01.1 Independência do modelo | **CONFORME, em leitura técnica** | `PROCESSO-TELA-PRANCHA.md`, §§6.1–6.3: valores/posições específicos substituídos por consulta ao contrato vinculado à versão da referência |
| G01.2 Não perda de conteúdo | **CONFORME, em verificação textual** | Anexo de transcrição literal abaixo, acompanhado da origem SHA-256; realocação definitiva ainda depende de GV2-02 |
| G01.3 Separação entre autoridades | **CONFORME, em leitura técnica** | `REFERENCIA-TEMPLATE-OFICIAL.md` consulta identidade e contrato; SPEC 3 define utilização; `GATE-IMPLEMENTACAO-TELAS.md` valida composição |
| G01.4 Contrato ausente bloqueia | **CONFORME, teste lógico normativo** | §§6.1–6.2 e Gate GI-3 explicitam `BLOQUEADO` quando contrato não existe / não corresponde ao modelo |
| G01.5 Preservação da baseline e da SPEC 1 | **CONFORME, comparação binária** | `docs/Documento_Mestre.md`, `PROCESSO-PRANCHA.md` e seis arquivos oficiais do Modelo C permanecem intactos |
| Aceite formal da revisão das quatro normas | **PENDENTE** | Aprovação original autorizou a execução do plano; não comprova aprovação dos textos revisados agora. Não inferir aceite do resultado |
| Realocação definitiva dos valores concretos | **PENDENTE para GV2-02** | Conteúdo integral preservado neste anexo, mas contrato técnico específico ainda não foi criado; não declarar operacional nova produção funcional |

**Conclusão:** não é possível declarar GV2-01 `CONCLUÍDO` sem aceite formal; **GV2-02 não foi iniciado**. O material abaixo é um changeset proposto e validado tecnicamente, não norma aceita pelo responsável.

### Quadro de transferência a validar no GV2-02

| Origem | Destino planejado | Condição de preservação |
|---|---|---|
| SPEC 3 §6.1, mapeamento de regiões e coordenadas do Modelo C | `docs/wireframes/images/contratos/USO-TEMPLATE-C.md` | Manter todas as regiões, números, conteúdos fixos/variáveis e restrições por tema |
| SPEC 3 §6.2, texto e cores/ícone de status para Modelo C | Mesmo contrato concreto | Preservar regra de status contextual, coordenadas, glyph e tokens sem generalizar |
| SPEC 3 §6.3, decisão T00 V1 `Claro / Escuro` | Registros individuais históricos V1 (já existentes) | Preservar somente o procedimento geral de desvio na SPEC; não alterar o histórico V1 |

<details><summary>Transcrição literal do conteúdo de origem antes da separação — prova de não perda</summary>

### 6.1 Mapeamento autorizado para novas Pranchas de Implementação (Modelo C vigente)

Este mapeamento aplica-se **somente às cópias de trabalho de saídas funcionais** feitas a partir da referência identificada pela SPEC 2. Não altera nem reinterpreta o PNG ou Wireframe Text oficiais aprovados; os números, cartões e coordenadas abaixo são os já documentados nos Wireframe Text **white C v02** e **black C v01**. Se outra referência passar a vigorar, sua aplicação deve ser verificada e formalmente documentada antes de usar este mapeamento: **não** presumir os mesmos campos.

| Região aprovada | Regra de conteúdo variável na saída funcional | Restrição invariável |
|---|---|---|
| **Item 1 — VIEWPORT TÉCNICO** | Substituir a demonstração pelo PNG de **cada página** da Tela de Referência aprovada, por tema, incluindo campos e estados daquela posição de rolagem | `360 × 800 px`, inserção em `x=40`, `y=272`, escala 1:1, sem alterações de pixels; primeiro conteúdo substituído na nova cópia |
| **Cabeçalho — identidade documental, título, legenda e metadados** | Nas **Pranchas de Implementação**, omitir `WIREFRAME` e a legenda demonstrativa `(Viewport à esquerda + painel técnico à direita)`; exibir apenas `PRANCHA TÉCNICA` no título; preencher `ID` com o identificador funcional e `ETAPA` com **somente a descrição** da interface. `PÁGINA = XX / YY` representa a continuidade da mesma Tela, `VERSÃO = vNN` a revisão; `DATA`, `BASELINE`, `VARIAÇÃO` e `STATUS` descrevem a saída real | Preservar geometria, marca, regiões, divisores e coordenadas do cabeçalho da referência oficial; não deslocar o título nem expandir regiões para ocupar espaços deixados vazios |
| **Item 10 — COMPONENTES (MEDIDAS)** | Documentar e representar **exclusivamente os componentes efetivamente presentes na Tela correspondente**, nas formas e estados usados. AppBar: reproduzir fielmente o layout da própria Tela, inclusive textos, controles, ícones, ações e dimensões documentadas; **não** copiar a amostra simplificada do template. Itens de lista podem possuir ou não ícone, **por item**, quando exigido ou permitido pela ficha/WT; nunca acrescentar ícone por hábito | Preservar o card e a geometria da zona, sem adicionar componentes ilustrativos de outras Telas; medidas devem corresponder às da Tela aprovada |
| **Item 14 — OBSERVAÇÕES TÉCNICAS** | Registrar somente premissas, regras, limitações, comportamentos, estados, continuidade/rolagem e observações pertinentes **àquela Tela e, quando cabível, àquela página**, com fonte rastreável; quantidade e texto definidos pela necessidade real, não pelas dez observações demonstrativas do template | Preservar o card, as zonas e os limites físicos; se não houver observação adicional, registrar expressamente essa condição, sem inventar uma nota |

### 6.2 Tratamento obrigatório dos textos demonstrativos e do STATUS nas saídas funcionais

**Esta seção não altera o Modelo C nem suas especificações congeladas.** O modelo vigente contém `WIREFRAME`, `PRANCHA TÉCNICA - MODELO C` e a legenda `(Viewport à esquerda + painel técnico à direita)`: esses textos documentam a prancha-modelo e **não** são conteúdo compulsório da saída funcional. A utilização do template aplica substituições **exclusivamente em uma nova cópia de Prancha de Implementação**, após a substituição do ViewPort e com GI-2 aprovado.

1. Conservar posições, dimensões, marca SaOr e todas as regiões estruturais aprovadas. No cabeçalho funcional, **não renderizar** o texto `WIREFRAME` nem a legenda demonstrativa. O título, sem subtítulo ou sufixo de modelo, será exatamente `PRANCHA TÉCNICA`, mantendo sua posição original. Não apagar áreas físicas nem deslocar outros elementos para preencher o vazio.
2. `ID` = identificador canônico da ficha (ex.: `T00`); `ETAPA` = **apenas** o nome oficial da interface (ex.: `Configuração da aplicação`). É proibida a repetição de `T00 -` no campo ETAPA ou o uso do título do template como etapa. `PÁGINA` e `VERSÃO` mantêm as regras existentes.
3. O estado **`AGUARDANDO APROVAÇÃO`**, enquanto aplicável à Prancha funcional, terá **ícone `schedule` da família Material Icons Outlined**, 20 px, seguido do texto em duas linhas `AGUARDANDO / APROVAÇÃO`. A referência geométrica é a região aprovada de STATUS: ícone em `(1120,46)` e texto iniciando em `(1146,38)` com largura máxima `114 px`, sujeito à conferência de encaixe real; não reduzir arbitrariamente a fonte nem sair da região `x=1108`, `w=160`. Texto e ícone usam **Error white `#991B1B`** ou **Error black `#FCA5A5`**, conforme o tema definido em `REGRAS-TECNICAS.md`, como **destaque visual específico solicitado para espera por aprovação**. A cor não altera o estado para ERRO, nem ativa o Gate. Se a renderização não couber na região, o GI-3 fica bloqueado; não se altera o template.
4. Outros estados documentados conservam seus contratos próprios; `APROVADO E CONGELADO` não é transformado no estado anterior e não pode ser usado sem decisão humana válida. Status da Prancha é diferente dos indicadores informativos de conexão presentes na Tela T00.
5. **Item 10** e **Item 14** continuam obrigatoriamente particulares à Tela e sua página, segundo a tabela acima. Elementos demonstrativos das amostras de template não são copiados como componentes funcionais.
6. O registro de composição deve indicar: referência vigente com seus hashes, textos omitidos/substituídos, valores completos dos campos, token e glyph do STATUS, conferência geométrica e ligação com os GI anteriores. Não registrar visualização de trabalho como aprovada.

### 6.3 Divergência específica autorizada de uma Tela versus Documento Mestre

Uma decisão de ocultar um texto ou outra informação **específica de uma interface** não se transforma em regra genérica de template nem altera silenciosamente a Baseline 1.0. A divergência deverá constar do registro `telas/controle/` do ID/tema com: trecho original da baseline; alteração visual deliberada; justificativa e alcance; elemento/destino preservado; decisão do responsável e data; evidências dos PNGs e seus hashes; avaliação de impacto e condição de aceite GI-1/GI-2. Se não houver autorização expressa e rastreável para uma divergência normativa, o Gate fica `BLOQUEADO`, independentemente da estética do PNG. A autorização da **exceção visual** não equivale à aprovação humana de todos os PNGs nem altera a ficha funcional original; requisitos funcionais adicionais continuam sob controle da baseline.

**Aplicação específica já comunicada para T00:** ocultar o subtítulo `Claro / Escuro` abaixo de `Tema`, sem remover o item nem seu destino `T00.2`. A decisão é restrita a T00 white/black e seus estados de conexão; a documentação individual deve declarar explicitamente o desvio e o vínculo com a baseline. Outras telas não herdam essa ocultação. O campo técnico `VARIAÇÃO` da Prancha continua visível e não é o mesmo texto da Tela.

As demais regiões técnicas da Prancha conservam a **estrutura e função documental** da referência aprovada. Suas demonstrações não autorizam acrescentar elementos à Tela nem declarar que um componente foi usado. Uma região que deva representar dados específicos só pode ser preenchida quando houver referência técnica verificável e espaço na geometria aprovada; caso contrário, aplicar bloqueio, não converter suposições em conteúdo. A fidelidade da saída funcional é aferida principalmente pelo **ViewPort por página e o Wireframe Text individual**, complementados pelos Itens 10 e 14.

Para toda interface, manter um **inventário de cobertura dos campos** no Wireframe Text e no registro de composição: nome/ID do elemento, origem funcional, condição/estado, página de rolagem em que aparece, geometria e ação/destino. Conferir que a união das páginas contempla todos os elementos aplicáveis e que a continuidade não cria campos novos nem perde campos existentes. Se o conteúdo real exigir mais posições de rolagem, **ampliar o total de páginas da Tela e das Pranchas correspondentes**, com especificação e aprovação próprias; jamais criar outra versão física do template para simular rolagem. Para a interface com `YY` páginas, produzir `YY` ViewPorts individuais e `YY` Pranchas por tema (salvo desvio funcional explicitamente aprovado na baseline).

O Item 10 ou Item 14 não pode ser preenchido com exemplos genéricos só para ocupar espaço. **Excedente de documentação da Prancha** não é prova de rolagem da Tela: se a área do próprio Item 10/14 não suportar os dados efetivamente necessários sem omissão ou redução indevida, `GI-3 = BLOQUEADO` até análise de revisão de template ou solução expressamente aprovada. A rolagem pertence ao ViewPort e não autoriza alterar as dimensões do canvas `1280 × 1920`.

O registro de composição **não é outro Wireframe Text de construção de template**. Sua função é registrar as escolhas da aplicação da referência fixa naquela interface. A especificação interna da Tela permanece no seu próprio Wireframe Text.



</details>

**Regra de passagem:** somente encerrar GV2-01 quando as quatro normas forem verificadas individualmente, todas as realocações estiverem preservadas e existir **aceite formal da revisão**. Enquanto `PENDENTE`, GV2-02 e seguintes ficam `NÃO INICIADOS`.

## GV2-02 a GV2-08

**Estado:** `NÃO INICIADOS`. A abertura depende do registro de encerramento do Gate imediatamente anterior. Nenhuma declaração ou imagem dispensa essa dependência.


---

# Adendo de continuidade — clone físico `SaOr-main-Casa (2).zip` (30/10/2026)

**O conteúdo anterior deste documento é preservado como evidência histórica da base `SaOr-main-Casa.zip`; não deve ser interpretado como inventário atual do novo clone.** Nova fonte física primária: `/SaOr-main-Casa (2).zip`, SHA-256 `4fbfceacb5b273d7e58408d875446e4b6f43bd997c36d2c79da713bec6fb8717` (caminho do upload fora do repositório). Integridade interna do ZIP: conforme.

## GV2-00 — Reconferência e encerramento na nova base

- Inventário do ZIP recebido: **115 arquivos**, entre eles **54 PNGs** e **41 Markdown**. Os 4 MP4 foram apenas identificados por nome/bytes, **sem processamento do conteúdo**.
- O novo clone contém as quatro normas GV2-01 no mesmo conteúdo binário do pacote revisado. Existem ainda dez PNGs preliminares de T00.1, **fora do escopo da regularização de T00 V2**; não foram modificados, aprovados nem utilizados para inferir padrões.
- **Não conformidade material localizada e resolvida na cópia de trabalho:** o novo clone omitira `docs/wireframes/images/white/telas/pranchas/01_Mobile_360x800/T00-01-01_v02.png`, embora o registro original GV2-00 (acima) o identifique pelo SHA-256 `310bbac69366d6f57279ca30f2858d0489ca17e370120819b0594c18c06a9fae`. O arquivo foi recuperado como **bytes exatos** de outro clone físico previamente fornecido pelo responsável, `SaOr-main-Casa.zip`, somente após conferir identidade integral com o hash prescrito no documento do **novo** clone. Essa cópia anterior serviu exclusivamente como repositório de bytes, não como autoridade normativa ou de seleção. A recuperação deve integrar o pacote de atualização; sem ela, o conjunto de seis PNGs V2 continuaria incompleto.
- No conjunto de trabalho, as duas Pranchas V2 têm `1280 × 1920 px`, os dois PNGs principais e estados alternativos têm `360 × 800 px`, e o recorte `x40,y272,360×800` de cada Prancha corresponde à respectiva Tela principal com **0 pixels divergentes**. Regiões diferentes de cada estado: `white 1428 pixels`, `black 1410 pixels`, ambas na caixa `(68,150,204,174)`.
- Todos os artefatos congelados do Modelo C e os documentos/PNGs históricos V1 foram mantidos sem alterações; os dois nomes V2 fora do padrão são corrigidos no GV2-03, não neste Gate.

**GV2-00: `CONCLUÍDO — verificação física atualizada, com recuperação binária explicitada`.** Esta conclusão não presume que GIF, GI-1 ou GI-2 estejam aprovados.

## GV2-01 — Verificação binária da revisão implementada e aceite de prosseguimento

- O ZIP atualizado incorpora exatamente os **quatro arquivos normativos** anteriormente revisados e validados tecnicamente, com bytes idênticos ao pacote GV2-01. As SPECs 1, o Documento Mestre e o conjunto oficial do Modelo C não foram alterados.
- **Manifestação do responsável nesta etapa:** “Arquivo ja com spec implementado para poder prosseguir.” Trata-se de autorização expressa de continuidade **com a revisão aplicada na nova base**, não de aprovação automática de Telas, TextFrames, Pranchas ou de todos os Gates futuros.
- Conferidos os critérios G01.1–G01.5 documentados anteriormente: separação de autoridades; ausência de parâmetros do Modelo C como normas universais; transcrição completa dos conteúdos migrados neste registro; bloqueio por ausência de contrato; preservação da baseline. O destino concreto dos parâmetros foi preenchido no GV2-02.

**GV2-01: `CONCLUÍDO PARA CONTINUIDADE`, com aceitação da revisão implementada evidenciada pela manifestação acima.** Se o responsável contestar a abrangência desse aceite, a decisão deverá ser reavaliada antes de utilizar os contratos em produção funcional.

## GV2-02 — Contratos técnicos versionados (checagem técnica)

Os seguintes documentos foram criados após o GV2-01, cada qual com responsabilidade separada:

| Documento | SHA-256 |
|---|---|
| `.specs/wireframes/PROCESSO-TELA-PRANCHA.md` | `635e7a7212c59d37e175ac27826909109b6060c67f77dc1cc9fa40a206da89b7` |
| `.specs/wireframes/GATE-IMPLEMENTACAO-TELAS.md` | `2086c846237ae0628e4b7b7ba29c02ac3351211c23484da08eef3c29dc8d8cff` |
| `.specs/wireframes/REFERENCIA-TEMPLATE-OFICIAL.md` | `c0b7c56ac76a58f12eff2db25f45c27be02852dd1ad3e050e3141893437625d1` |
| `.specs/wireframes/README.md` | `3847e785edd0e13875cd03b7f85da361777fe9c226ec4610da4c1ee293249dde` |
| `docs/wireframes/images/contratos/USO-TEMPLATE-C.md` | `0a095edcf4bfb3252d8ae3c18ce810d119d1747f188bd090232c362cf5b13fe4` |
| `docs/wireframes/images/padroes-funcionais/Mobile-v02.md` | `7aab2650d9c6fb492656c189fcea6432b988a89bcecc96c34fd238896777af94` |
| `docs/wireframes/images/Registro_Padrao_Visual_Funcional_Mobile.md` | `0bcc3e7de752b8141c3e7bf58033f9f197db11d0ee1da9913911dfde0d178f61` |

- `contratos/USO-TEMPLATE-C.md` conserva a geometria e as condições concretas de substituição anteriormente na SPEC 3, sem alterar os seis arquivos oficiais. As versões de template white/black e seis hashes foram verificados contra `Registro_Controle_Template_Oficial.md`.
- `padroes-funcionais/Mobile-v02.md` delimita os padrões visuais que podem ser considerados para novos requisitos, distingue os conteúdos exclusivos de T00 e identifica fisicamente as duas Telas principais e dois estados V2 por hash. Não cria requisito funcional de T00.1.
- `Registro_Padrao_Visual_Funcional_Mobile.md` é registro genérico de futura vigência; mantém **V2 como candidata em formalização**, sem marcar padrão V2 vigente antes de GV2-06.
- Teste lógico de independência: para V1 e V2 a SPEC 3 exige a **mesma sequência**, fonte funcional e contrato técnico concreto; nenhuma mudança de versão exige mudar seus §§6.1–6.3. As informações específicas de cada versão ficam nos documentos individuais. Teste de reprodução visual integral de T00 v02 dependerá do TextFrame e GI-2, não é declarado concluído aqui.

**GV2-02: `CONCLUÍDO — contratos e separação normativa verificadas tecnicamente`; a vigência funcional V2 continua pendente do GV2-06.** As referências atuais do índice operacional serão consolidadas no GV2-07; até lá a pasta `contratos/` contém o vínculo concreto por modelo e hashes.

## GV2-03 — Regularização de PNGs/controles V2

- **Registro histórico da tentativa anterior:** havia sido proposta uma mudança de `_estado-desconectada.png` para `__estado-desconectada.png` nos temas white/black. **Essa mudança nominal foi revogada pela corrigenda posterior neste documento; o nome original com um `_` prevalece**. O conteúdo binário não se altera; os SHA-256 são `0e4a2da069611f52064c9a3e60f27536ebef21fd787ee9829a70d635de750e90` e `d9d70702af9473bad1688faae215ca14fdd5e294c076e32a3c4526e3d33dbe77`.
- Foram criados `white/telas/controle/T00-01-01_v02.md` e `black/telas/controle/T00-01-01_v02.md` com caminhos, hashes, fontes funcionais, diferenças V1/V2 e alcance documentado das manifestações do responsável.
- **Pendência bloqueante G03:** a adoção visual da V2 e a aprovação visual das Pranchas foram comunicadas, mas não há **decisão GI-1 humana individual identificando expressamente os quatro PNGs das Telas por hash**. A aprovação das Pranchas não se estende automaticamente a GI-1 ou GI-2 pela regra do `GATE-IMPLEMENTACAO-TELAS.md`, §3–4. Não atribuir aprovação por inferência.

**GV2-03: `PENDENTE — GI-1 dos PNGs de Tela não comprovado`.** GV2-04 a GV2-08 permanecem `NÃO INICIADOS`. A recuperação da Prancha White e os arquivos de controle são uma **entrega intermediária**; não representam aprovação ou vigência V2. Quando o responsável confirmar expressamente as Telas/estados identificados nos registros por hash, incorporar fielmente a decisão, validar e encerrar GV2-03 antes de criar os TextFrames.


# Adendo de aceite específico — GV2-03 e início controlado do GV2-04

**Manifestação humana vinculada ao turno de continuação:** após a exposição individual dos **quatro arquivos PNG**, com temas, estados e respectivos hashes, o responsável declarou expressamente: **“Sim estão aprovados”**. O objeto dessa decisão são as Telas de Referência T00 V2 **white/black**, nos estados **Conectada e Desconectada**, identificadas a seguir; não é aprovação do TextFrame futuro, da aplicação em código nem um novo aceite da Prancha.

| Tela/estado aprovado | Caminho relativo à raiz | SHA-256 revalidado |
|---|---|---|
| White, Conectada | `docs/wireframes/images/white/telas/design/01_Mobile_360x800/T00-01-01_v02.png` | `0442412875e3c45b85038d75d8b628f16c94c4ba06529d1c0c97a32d47761504` |
| White, Desconectada | `docs/wireframes/images/white/telas/design/01_Mobile_360x800/T00-01-01_v02_estado-desconectada.png` | `0e4a2da069611f52064c9a3e60f27536ebef21fd787ee9829a70d635de750e90` |
| Black, Conectada | `docs/wireframes/images/black/telas/design/01_Mobile_360x800/T00-01-01_v02.png` | `0d4baf7b7d4e12a59db8646dc6317976a860b573abd14745def152ea64b34950` |
| Black, Desconectada | `docs/wireframes/images/black/telas/design/01_Mobile_360x800/T00-01-01_v02_estado-desconectada.png` | `d9d70702af9473bad1688faae215ca14fdd5e294c076e32a3c4526e3d33dbe77` |

**Verificações físicas executadas no fechamento:** os quatro arquivos abrem como PNG RGB `360 × 800` e os SHA-256 coincidem; ambas as variantes mudam apenas a caixa `(68,150)–(204,174)` do status; a Tela principal de cada tema é bit a bit igual à área `x=40,y=272,w=360,h=800` de sua Prancha, cuja dimensão é `1280 × 1920`. Os seis arquivos protegidos do Modelo C e os artefatos V1 não foram modificados. A decisão visual V2 e o inventário funcional de T00 foram confrontados com `docs/Documento_Mestre.md`, §T00; os novos subtítulos/ícones/agrupamentos são decisões de **representação visual de T00 V2**, não novos comportamentos funcionais.

| Critério GV2-03 | Resultado e evidência |
|---|---|
| Conjunto V2 completo | **CONFORME** — seis PNGs presentes no changeset/base consolidada, dois por estado e uma Prancha por tema |
| Nomenclatura do estado | **CONFORME à convenção revisada** — sufixo `_estado-desconectada` original; não remover os PNGs originais. Os nomes com `__estado-` são duplicatas da tentativa revogada e devem ser removidos somente se existirem e após conferir o SHA-256. |
| Identidade binária dos quatro PNGs | **CONFORME** — tamanhos, hashes e inspeção visual registrada acima |
| GI-0 da Tela | **CONFORME quanto a inventário e fontes** — T00 §9.1 e `REGRAS-TECNICAS.md`; diferenças V1/V2 classificadas neste registro |
| GI-1 dos quatro PNGs individuais | **APROVADO EXPRESSAMENTE** — confirmação “Sim estão aprovados” após identificação individual com hash |
| Integridade e preservação histórica | **CONFORME** — V1 e Modelo C preservados, sem edição de pixels |

**Encerramento formal GV2-03: `CONCLUÍDO`**, com os critérios acima verificados. A origem da decisão é a manifestação atual do responsável; não se atribui data histórica fictícia às imagens ou a aprovações anteriores. **GV2-04: `EM EXECUÇÃO`** para elaboração dos TextFrames a partir das Telas aprovadas, sem antecipação do aceite GI-2. **GV2-05 a GV2-08: `NÃO INICIADOS`** até encerramento comprovado de GV2-04.


## GV2-04 — TextFrames V2 produzidos e submetidos a GI-2

**Abertura:** somente após GV2-03 formalmente encerrado no adendo imediatamente anterior. Foram criados a partir dos PNGs de GI-1 aprovados:

| Tema | Arquivo TextFrame | SHA-256 do TextFrame |
|---|---|---|
| white | `docs/wireframes/images/white/telas/wiframetext/T00-01-01_v02.md` | `51fc0b44db607522618dcb9e321602e442e4c90a0c2da86597328a0ad6226089` |
| black | `docs/wireframes/images/black/telas/wiframetext/T00-01-01_v02.md` | `2d7d16b74ae00bb9f33a75c9e9a8015ea9661f55295e3f710ed90f790941d25e` |

**Conferências técnicas realizadas:** dimensões e hashes das quatro Telas; superfícies dos quatro cartões por tema; regiões de tinta/caixas identificáveis; textos presentes; quatro destinos de T00; estados e posição do indicador; equivalência funcional white/black; regiões do ViewPort idênticas nas Pranchas preexistentes. Os TextFrames indicam expressamente o método e os limites da medição raster, sem atribuir automaticamente à fonte editável original uma família tipográfica, peso ou glyph exato não comprovados.

**Pendências de GI-2:** (1) aprovação humana do par **PNG + TextFrame** de cada tema ainda não apresentada; (2) nomes exatos de glyphs e parâmetros editáveis originais não recuperáveis univocamente apenas do PNG, devendo ser fundamentados em fontes normativas/ativos de origem ou receber decisão registrada de equivalência visual, se exigidos para reprodução paramétrica. Estas pendências não são resolvidas por aprovação GI-1 anterior nem pela mera existência dos documentos.

**GV2-04: `PENDENTE — TextFrames produzidos, aceite GI-2 não comprovado`.** GV2-05, GV2-06, GV2-07 e GV2-08 continuam `NÃO INICIADOS`. Não criar registros de composição V2 nem declarar padrão Mobile V2 oficialmente vigente antes dos Gates correspondentes. Os arquivos de T00.1 permanecem fora do escopo deste changeset.

## Corrigenda normativa posterior — variante V2 com um único `_`

**Decisão expressa posterior do responsável:** manter `T00-01-01_v02_estado-desconectada.png`, com um único sublinhado, como nome canônico nos temas `white` e `black`. A exigência anterior de `__estado-` não demonstrou dependência técnica e foi substituída no contrato `.specs/wireframes/WIREFRAME-TEXT-TELA.md`, §2.

- **Sem alteração de imagem:** os PNGs originais com `_estado-` são mantidos com os hashes `0e4a2da069611f52064c9a3e60f27536ebef21fd787ee9829a70d635de750e90` (white) e `d9d70702af9473bad1688faae215ca14fdd5e294c076e32a3c4526e3d33dbe77` (black).
- **Histórico preservado:** a classificação anterior e a proposta de renomeação no GV2-03 ficam registradas como ocorrências históricas, **não** instruções ativas. Os PNGs e documentos da V1 já aprovados permanecem intactos, inclusive os nomes históricos com dois sublinhados.
- **Cópias adicionais:** se uma aplicação anterior criou arquivos físicos `T00-01-01_v02__estado-desconectada.png`, eles são duplicatas sem função. Só removê-los após conferir a existência e o hash correspondente do PNG canônico com um `_`. Não excluir os arquivos originais.
- **Estado dos Gates:** a correção de nomenclatura não concede nem revoga aprovação visual GI-1; os quatro PNGs já aprovados continuam identificados pelos mesmos SHA-256. O GV2-04/GI-2 permanece pendente de aceite humano dos TextFrames; GV2-05 e posteriores continuam não iniciados.
- **Rastreabilidade documental:** hashes dos dois TextFrames e do perfil `Mobile-v02.md` foram recalculados nas tabelas anteriores para refletir exclusivamente a correção das referências textuais.


---

## Execução sequencial adicional — 30/10/2026 (base `SaOr-mai-Casa (2).zip`)

**Objeto:** execução autorizada do plano de regularização da T00 V2, etapas 0 a 7. **Regra:** nenhuma etapa seguinte é iniciada enquanto a anterior não tiver todos os critérios verificados e seu fechamento registrado. Este adendo prevalece para a *situação atual* sobre entradas históricas de Gate, sem alterar ou apagar a cronologia anterior.

### Etapa 0 — Fixação da base: `CONCLUÍDA`

- **Base física:** arquivo ZIP `SaOr-mai-Casa (2).zip`; SHA-256 `b748e3cc2b0860ea2adcc8c694496f7e8ae44f5c63337f84f52001566783b0c0`; integridade de arquivo ZIP verificada, sem entrada corrompida.
- **Inventário observado:** 123 arquivos físicos, 48 documentos Markdown, 55 PNGs; vídeos excluídos da análise de conteúdo. Nenhum arquivo fonte editável para os componentes/glyphs individuais da Tela V2 foi identificado.
- **Fontes:** `docs/Documento_Mestre.md` §T00; `.specs/wireframes/REGRAS-TECNICAS.md` §§3–9; `.specs/wireframes/WIREFRAME-TEXT-TELA.md` §§2–5; `.specs/wireframes/GATE-IMPLEMENTACAO-TELAS.md` §§2–4; controles e TextFrames `v02` de White/Black; registro de seleção e contrato do Modelo C.
- **Conjunto V2:** PNGs principais/alternativos `white` e `black` têm `360×800`; Pranchas V2 têm `1280×1920`; o recorte `(x=40,y=272,w=360,h=800)` de ambas as Pranchas é idêntico pixel a pixel ao PNG principal correspondente. As diferenças entre Conectada e Desconectada ficam em `x=68..203,y=150..173` em ambos os temas.
- **GI-1:** aprovação humana já registrada para os quatro PNGs por hash (§GV2-03 deste registro); mantida, sem reabertura. **GI-2:** não aprovado nos TextFrames físicos, §6 dos dois documentos. **GV2-05 a GV2-08:** não iniciados.
- **Preservação:** seis arquivos oficiais do Modelo C conferidos contra `Registro_Controle_Template_Oficial.md` por SHA-256; V1 preservada integralmente. Não foi constatada necessidade de editar imagens.
- **Critérios E0.1–E0.5:** conformes por inspeção do arquivo ZIP, leitura dos documentos, abertura e comparação dos PNGs, conferência dos hashes e inventário de versões. **Decisão:** `CONCLUÍDA`; permitida abertura da Etapa 1.

### Etapa 1 — Correção normativa do sufixo: `CONCLUÍDA`

- **Arquivo alterado:** `.specs/wireframes/PROCESSO-TELA-PRANCHA.md`, §3, parágrafo da identificação e versionamento. Substituída **somente** a ocorrência normativa de `` `__estado-<identificador>.png` `` por `` `_estado-<identificador>.png` ``.
- **Fonte da decisão e norma compatível:** `.specs/wireframes/WIREFRAME-TEXT-TELA.md`, §2, determina `_estado-` para artefatos novos e preserva os nomes históricos V1; corrigenda anterior neste registro revoga a tentativa de renomeação de T00 V2. Os quatro PNGs V2 originais mantêm nomes e hashes.
- **Verificação física pós-edição:** o arquivo foi reaberto e confrontado byte a byte com a versão-base, confirmando alteração localizada. Busca das normas ativas confirmou ausência de nova exigência `__estado-`; as ocorrências remanescentes nos documentos V1 e no histórico são exclusivamente **históricas**, não instruções vigentes.
- **SHA-256 anterior da SPEC 3:** `635e7a7212c59d37e175ac27826909109b6060c67f77dc1cc9fa40a206da89b7` (mantido nos registros históricos anteriores).
- **SHA-256 da SPEC 3 corrigida:** `66a40eaa91b3ca83a31fa28ddde1a1c01b89c445f113aeae0e34c66e933e57d9`.
- **Critérios E1.1–E1.6:** conformes; a correção de texto não altera dimensão, pixels, aprovações visuais, BaseLine ou contrato das versões V1. **Decisão:** `CONCLUÍDA`; permitida abertura da Etapa 2.

### Etapa 2 — Conferência técnica dos TextFrames V2: `PENDENTE` (sem encerramento)

**Reabertura física e fontes:**

- `docs/wireframes/images/white/telas/wiframetext/T00-01-01_v02.md`, §§2–6; SHA-256 original `51fc0b44db607522618dcb9e321602e442e4c90a0c2da86597328a0ad6226089`;
- `docs/wireframes/images/black/telas/wiframetext/T00-01-01_v02.md`, §§2–6; SHA-256 original `2d7d16b74ae00bb9f33a75c9e9a8015ea9661f55295e3f710ed90f790941d25e`;
- Quatro PNGs V2 aprovados e hashes registrados nos controles `white/black/telas/controle/T00-01-01_v02.md`, §6;
- `.specs/wireframes/REGRAS-TECNICAS.md` §§5, 6, 8, 9 (tipografia `Inter`, tokens de cor, radius e iconografia `Material Icons Outlined`); `.specs/wireframes/WIREFRAME-TEXT-TELA.md` §§3–5 (critério de reprodução determinística).

| Critério | Verificação realizada | Situação |
|---|---|---|
| E2.1 — Geometria | PNGs `360×800`; cartões `[12,108,336,80]`, `[12,240,336,72]`, `[12,364,336,72]`, `[12,452,336,56]` confrontados com os TextFrames; caixa de diferença de estados confirmada | `CONFORME` para caixas verificadas; não extrapolar para hit-targets editáveis |
| E2.2 — Conteúdo | Inspeção visual dos dois PNGs; textos, quatro cartões, seções, versão e navegação confrontados com §§2–5 dos TextFrames | `CONFORME` para conteúdo visível |
| E2.3 — Estados | Imagens de Conectada e Desconectada diferem apenas na região `(68,150)–(204,174)` | `CONFORME` |
| E2.4 — Temas | White/Black têm mesma composição e destinos, com paletas distintas | `CONFORME` |
| E2.5 — Requisitos | Documento Mestre §T00 × inventário de ambos os TextFrames: destinos T00.1, T00.2, T00.3 e M00.5 sem nova ação funcional | `CONFORME` quanto aos destinos; diferenças visuais V2 descritas nos controles |
| E2.6 — Propriedades técnicas | A SPEC técnica fornece famílias/tokens **normativos**, mas nenhum arquivo editável ou fonte de exportação comprova os **identificadores exatos de glyphs** e os parâmetros originais de renderização dos PNGs gerados externamente; os próprios TextFrames, §4/§6, registram essas limitações | **`PENDENTE — IMPEDITIVO`** para afirmar reprodução paramétrica exata |
| E2.7 — Integridade | SHA-256 dos quatro PNGs coincide com controles; os seis artefatos oficiais do Modelo C foram verificados por hash | `CONFORME` |
| E2.8 — Documentos | Os dois TextFrames foram integralmente relidos: já declaram com clareza a ausência de fonte original e conservam `GI-2: AGUARDANDO APROVAÇÃO HUMANA`; não foi encontrada informação adicional verificável que justificasse alterar seus textos para afirmar valores desconhecidos | `CONFORME` quanto à leitura; **não supre E2.6** |

**Pendência objetiva:** comprovação dos identificadores dos glyphs e parâmetros editáveis relevantes em arquivos de origem, **ou decisão técnica explícita e documentada que estabeleça uma equivalência visual suficiente e seus limites**, quando compatível com o contrato normativo. Não preencher a lacuna por aproximação, dedução de família de ícones ou aceitação fictícia. O aceite humano GI-2 de ambos os TextFrames ainda não foi concedido e é requisito separado da conclusão técnica.

**Decisão:** **Etapa 2 `PENDENTE`; GV2-04/GI-2 continuam abertos.** Etapas 3–7 e GV2-05 a GV2-08 permanecem **`NÃO INICIADOS`**. Preservar as aprovações GI-1 e Pranchas visuais existentes; nenhuma inferência de aceite GI-2, GI-3 ou GI-4. A SPEC, este registro e o restante da árvore deverão ser auditados fisicamente antes de utilizar este adendo como prova de resultado.
