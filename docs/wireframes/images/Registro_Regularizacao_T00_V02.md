# SaOr — Registro sequencial da regularização V2 de T00 Mobile

**Natureza:** evidências de transição documental; não substitui as SPECs, decisões de aprovação de interface ou os registros canônicos de vigência.  
**Base física:** `SaOr-main-Casa.zip` — SHA-256 `36cd7eb01486df0c220c1584fcdf16f5f863bc6da1e0b6361a271ea52e1636eb`.  
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
| Nome `v02_estado-desconectada` (um `_`) | Inconsistência de nomenclatura física; a convenção aprovada usa `__estado-` | SPEC 3, §3; corrigir apenas em GV2-03 |

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

**Situação:** `EM EXECUÇÃO / AGUARDANDO ACEITE FORMAL DA REVISÃO`.

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
