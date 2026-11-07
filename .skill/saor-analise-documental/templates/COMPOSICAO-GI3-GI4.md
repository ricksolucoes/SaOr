# SaOr — {{ID}} — Registro de composição da Prancha Mobile — {{TEMA}} — {{VERSAO}}

**Estado vigente ({{DATA_DE_REFERENCIA_COMPROVADA}}):** GI-0 `{{ESTADO_GI0}}`; GI-1 `{{ESTADO_GI1}}`; GI-2 `{{ESTADO_GI2}}`; GI-3 `{{ESTADO_GI3_TECNICO}}`; GI-4 `{{ESTADO_GI4_HUMANO}}`. **Prancha atual:** {{CAMINHO_PNG_FINAL}}; SHA-256 `{{SHA_PRANCHA_FISICA}}`. Referência ao aceite: {{SECAO_E_REGISTRO}}.

## 1. Identidade, estado e artefatos

### 1.1. Identificação da composição

| Campo | Valor comprovado |
|---|---|
| Interface (ID — nome oficial) | {{ID_NOME}} |
| Tema | {{WHITE_OU_BLACK}} |
| Página / total | {{XX/YY}} |
| Versão | {{VNN}} |
| Baseline funcional | {{BASELINE}} |
| Prancha — formato | {{1280x1920_RGB_SE_VERIFICADO}} |
| Documento de composição | {{CAMINHO_RELATIVO_DESTE_MD}} |
| Estado atual e data da evidência | {{ESTADO_DATA_FONTE}} |

### 1.2. Identidade física de cada artefato vinculado

| Papel documental | Caminho relativo | Dimensões / formato | SHA-256 físico | Estado/decisão aplicável |
|---|---|---|---|---|
| Prancha final do tema | {{CAMINHO}} | {{1280x1920}} | {{SHA_FINAL}} | {{GI4}} |
| PNG visual fonte GI-1/GI-2 | {{CAMINHO}} | {{360x800}} | {{SHA_PNG}} | {{GI1_GI2}} |
| TextFrame aprovado GI-2 | {{CAMINHO}} | Markdown | {{SHA_TEXTFRAME}} | {{GI2}} |
| Controle GI-0/GI-1 | {{CAMINHO}} | Markdown | {{SHA_CONTROLE}} | {{GI0_GI1}} |
| Documento Mestre / seção da interface | {{CAMINHO_TRECHO}} | Markdown | {{SHA_SE_NECESSARIO}} | {{BASELINE}} |

### 1.3. Escopo e limites deste registro

**Objeto:** {{PRANCHA_TEMA_PAGINA_VERSAO}}.

**Não se confunde com:** {{TEMPLATE_FONTE_PNG_TELA_TEXTFRAME}}.

**Preservações aplicáveis:** {{LISTA_OBJETIVA_COM_FONTES}}.

## 2. Referência oficial utilizada

### 2.1. Modelo, tema e vigência na data de uso

| Referência | Valor | Registro/decisão de vigência | Data/alcance | Resultado de conferência |
|---|---|---|---|---|
| Modelo oficial | {{MODELO_VERSAO}} | {{REGISTRO_DE_SELECAO}} | {{DATA}} | {{RESULTADO}} |
| Tema | {{TEMA}} | {{FONTE}} | {{ALCANCE}} | {{RESULTADO}} |
| Contrato de aplicação selecionado | {{CAMINHO_VERSAO}} | {{AUTORIDADE}} | {{DATA_OU_CONDICAO}} | {{RESULTADO}} |

### 2.2. Inventário das fontes oficiais e integridade

| Fonte oficial do modelo | Caminho exato | SHA-256 | Método de conferência | Resultado |
|---|---|---|---|---|
| PNG oficial | {{CAMINHO}} | {{SHA}} | {{METODO}} | {{RESULTADO}} |
| TextFrame oficial do modelo | {{CAMINHO}} | {{SHA}} | {{METODO}} | {{RESULTADO}} |
| ViewPort demonstrativo | {{CAMINHO}} | {{SHA}} | {{METODO}} | {{RESULTADO}} |

### 2.3. Contratos de regiões, cabeçalho e STATUS

| Elemento do modelo | Parâmetro autorizado | Fonte/trecho do contrato efetivo | Evidência da aplicação |
|---|---|---|---|
| ViewPort | {{COORDENADAS_TAMANHO}} | {{FONTE}} | {{EVIDENCIA}} |
| Regiões fixas e variáveis | {{REGIOES}} | {{FONTE}} | {{EVIDENCIA}} |
| Cabeçalho e STATUS | {{CAMPOS_GLIFOS_VALORES_PERMITIDOS}} | {{FONTE}} | {{EVIDENCIA}} |

## 3. Cadeia documental GI-0 → GI-2

### 3.1. Resultado dos Gates anteriores por objeto

| Gate | Objeto e versão | Arquivo/hash | Decisão e data | Estado comprovado |
|---|---|---|---|---|
| GI-0 | {{CONTROLE}} | {{CAMINHO_SHA}} | {{FONTE}} | {{ESTADO}} |
| GI-1 | {{PNG}} | {{CAMINHO_SHA}} | {{FONTE}} | {{ESTADO}} |
| GI-2 | {{PNG_TEXTFRAME_CONJUNTO}} | {{CAMINHOS_HASHES}} | {{FONTE}} | {{ESTADO}} |

### 3.2. Vínculo das evidências e limite de herança

| Dependência da composição | Evidência no documento de origem | Identidade física utilizada | Condição para GI-3 |
|---|---|---|---|
| PNG de Tela aprovado | {{CAMINHO_E_SECAO}} | {{SHA}} | {{RESULTADO}} |
| TextFrame derivado aprovado | {{CAMINHO_E_SECAO}} | {{SHA}} | {{RESULTADO}} |
| Mesmo tema/página/versão | {{CAMINHOS}} | {{IDENTIDADE}} | {{RESULTADO}} |

## 4. Método de composição

### 4.1. Base de montagem e preservação do modelo

**Fonte de cópia:** {{CAMINHO_MODELO_VIGENTE}}; SHA-256 {{SHA}}.

**Prancha produzida como arquivo próprio:** {{CAMINHO_NOVO}}.

**Template original preservado:** {{EVIDENCIA_DE_HASH_SEM_MODIFICACAO}}.

### 4.2. Sequência efetiva de operações

| Ordem | Operação realmente executada | Região/elemento | Parâmetro de aplicação | Fonte/método |
|---|---|---|---|---|
| 1 | {{SUBSTITUICAO_DO_VIEWPORT_COM_PNG_APROVADO_SE_EXECUTADA}} | {{X_Y_W_H}} | {{ESCALA_1_1_SE_COMPROVADA}} | {{EVIDENCIA}} |
| 2 | {{CABECALHO}} | {{REGIAO}} | {{PARAMETROS}} | {{FONTE}} |
| 3 | {{ITEM_10}} | {{REGIAO}} | {{PARAMETROS}} | {{FONTE}} |
| 4 | {{ITEM_14}} | {{REGIAO}} | {{PARAMETROS}} | {{FONTE}} |

### 4.3. Regiões permitidas e regiões preservadas

| Região contratual | Caixa `[x,y,w,h]` | Permitida/fixa | Modificação efetiva | Fonte |
|---|---|---|---|---|
| {{REGIAO}} | {{CAIXA}} | {{TIPO}} | {{ALTERACAO_OU_NENHUMA}} | {{FONTE}} |

## 5. Verificação geométrica e técnica — GI-3

### 5.1. Canvas, ViewPort e correspondência 1:1

| Verificação | Fonte de comparação | Método/quantidade verificada | Resultado | Limitação |
|---|---|---|---|---|
| Dimensões e modo da Prancha | {{ARQUIVO_FISICO}} | {{METODO}} | {{RESULTADO}} | {{LIMITE}} |
| ViewPort 360×800 na coordenada contratual | {{PNG_DE_TELA_E_PRANCHA}} | {{PIXEL_A_PIXEL_N_TOTAL}} | {{DIVERGENCIAS}} | {{LIMITE}} |
| Escala/reamostragem/corte | {{FONTE}} | {{METODO}} | {{RESULTADO}} | {{LIMITE}} |

### 5.2. Regiões fixas, variáveis e máscara de diferenças

| Região verificada | Fonte oficial | Área/caixa | Quantidade de pixels ou método | Resultado |
|---|---|---|---|---|
| {{REGIAO_DO_CONTRATO}} | {{MODELO}} | {{CAIXA}} | {{MEDICAO}} | {{DIVERGENCIAS}} |

### 5.3. Inspeção de conteúdo e resultado GI-3

| Critério técnico | Evidência física/documental | Resultado | Risco/limitação |
|---|---|---|---|
| {{CAMPOS_ITENS_TEXTO_ICONE_COTA_TRUNCAMENTO_ETC}} | {{EVIDENCIA}} | {{CONFORME_OU_NAO_CONFORME}} | {{LIMITE}} |

**Parecer técnico GI-3:** {{PARECER_FUNDAMENTADO_NAO_APROVACAO_HUMANA}}.

## 6. Cabeçalho e campos variáveis

### 6.1. Valores impressos e fontes dos campos

| Campo no cabeçalho | Valor efetivamente impresso | Origem/contrato | Conferência |
|---|---|---|---|
| TÍTULO | {{VALOR}} | {{FONTE}} | {{RESULTADO}} |
| ID | {{VALOR}} | {{FONTE}} | {{RESULTADO}} |
| ETAPA | {{NOME_OFICIAL_SEM_ID}} | {{DOCUMENTO_MESTRE}} | {{RESULTADO}} |
| PÁGINA | {{XX_YY}} | {{PAGINACAO}} | {{RESULTADO}} |
| VERSÃO | {{VNN}} | {{VERSAO}} | {{RESULTADO}} |
| BASELINE | {{VALOR}} | {{AUTORIDADE}} | {{RESULTADO}} |
| VARIAÇÃO | {{WHITE_OU_BLACK}} | {{TEMA}} | {{RESULTADO}} |
| DATA | {{DATA_GRAFICA}} | {{EVIDENCIA}} | {{RESULTADO}} |
| STATUS | {{VALOR_IMPRESSO}} | {{CONTRATO_E_DECISAO}} | {{RESULTADO}} |

### 6.2. STATUS na submissão e no arquivo final

| Momento factual | Texto, ícone, cor e posição do STATUS | Arquivo/versão | SHA-256 | Decisão que autoriza o estado |
|---|---|---|---|---|
| Submissão GI-4 | {{VALORES_SE_EXISTIU}} | {{CAMINHO}} | {{SHA_SUBMISSAO}} | {{ESTADO_E_FONTE}} |
| Versão final | {{VALORES_SE_EXISTIU}} | {{CAMINHO}} | {{SHA_FINAL}} | {{DECISAO_E_FONTE}} |

### 6.3. Integridade dos campos e diferenças autorizadas

| Campo ou região | Substituição/omissão permitida no contrato | Diferença observada | Evidência de autorização | Resultado |
|---|---|---|---|---|
| {{CAMPO}} | {{REGRA}} | {{DIFERENCA}} | {{FONTE}} | {{RESULTADO}} |

## 7. Item 10 — componentes da Tela

### 7.1. Inventário dos componentes efetivamente utilizados

| Componente usado | Estado/PNG origem | Recorte `[x,y,w,h]` no PNG | Posição na Prancha | Dimensão/cota impressa | Evidência |
|---|---|---|---|---|---|
| {{COMPONENTE}} | {{ESTADO}} | {{RECORTE}} | {{POSICAO}} | {{COTA_OU_SEM_COTA_FUNDAMENTADA}} | {{PROVA}} |

### 7.2. Cotas, sobreposições e limites do raster

| Componente/cota | Dimensão verificada | Natureza da medição | Sobreposição intencional | Limite / fonte |
|---|---|---|---|---|
| {{COMPONENTE}} | {{VALOR}} | {{RASTER_OU_CONTRATO}} | {{SIM_NAO}} | {{LIMITE}} |

### 7.3. Fidelidade das amostras à Tela aprovada

| Amostra | Fonte exata no PNG | Método de confronto | Divergências / resultado | Ressalva justificada |
|---|---|---|---|---|
| {{AMOSTRA}} | {{RECORTE}} | {{MEDICAO}} | {{RESULTADO}} | {{RESSALVA}} |

## 8. Item 14 — observações técnicas

### 8.1. Observações pertinentes e individualizadas

| Número impresso | Texto efetivamente impresso | Fonte funcional/técnica | Relação com a interface | Verificação visual |
|---|---|---|---|---|
| {{N_REAL}} | {{TEXTO_LITERAL}} | {{FONTE}} | {{MOTIVO_DE_PERTINENCIA}} | {{RESULTADO}} |

### 8.2. Legibilidade, truncamento e pertinência

| Critério | Evidência sobre a Prancha | Resultado | Limite |
|---|---|---|---|
| {{COLUNAS_LINHAS_TRUNCAMENTO_CONTEUDO_REAL}} | {{PROVA}} | {{RESULTADO}} | {{LIMITE}} |

## 9. Resultado técnico e preservação

### 9.1. Parecer GI-3 e controles de conformidade pertinentes

| Controle/critério realmente aplicável | Objeto | Evidência específica | Resultado | Limitação |
|---|---|---|---|---|
| {{GI3_OU_CONTROLE_PARALELO_EXISTENTE}} | {{OBJETO}} | {{PROVA}} | {{RESULTADO}} | {{LIMITE}} |

### 9.2. Inventário dos arquivos preservados

| Artefato preservado | Caminho | SHA-256 antes / referência | SHA-256 verificado | Resultado |
|---|---|---|---|---|
| {{ARTEFATO}} | {{CAMINHO}} | {{HASH_ORIGEM}} | {{HASH_ATUAL}} | {{RESULTADO}} |

### 9.3. Estado consolidado, riscos e pendências

| Gate | Resultado atual | Evidência persistente | Ressalva / pendência |
|---|---|---|---|
| GI-0 | {{ESTADO}} | {{FONTE}} | {{PENDENCIA_OU_NENHUMA}} |
| GI-1 | {{ESTADO}} | {{FONTE}} | {{PENDENCIA_OU_NENHUMA}} |
| GI-2 | {{ESTADO}} | {{FONTE}} | {{PENDENCIA_OU_NENHUMA}} |
| GI-3 | {{ESTADO}} | {{FONTE}} | {{PENDENCIA_OU_NENHUMA}} |
| GI-4 | {{ESTADO}} | {{FONTE}} | {{PENDENCIA_OU_NENHUMA}} |

## 10. Aprovação humana GI-4 e histórico

### 10.1. Submissão e identificação das Pranchas

| Objeto | Caminho da Prancha | SHA-256 da submissão | Data/estado na submissão | Fonte da identidade |
|---|---|---|---|---|
| White | {{CAMINHO}} | {{SHA_SE_EXISTE}} | {{DATA_ESTADO}} | {{PROVA}} |
| Black | {{CAMINHO}} | {{SHA_SE_EXISTE}} | {{DATA_ESTADO}} | {{PROVA}} |
| Conjunto | {{REFERENCIAS_WHITE_BLACK}} | {{AMBOS_HASHES}} | {{DATA_ESTADO}} | {{PROVA}} |

### 10.2. Decisão original humana e escopo do GI-4

**Data original da decisão:** {{DATA_COMPROVADA_OU_AINDA_SEM_DECISAO}}.

**Pergunta/objeto submetido, quando comprovados:** {{PERGUNTA_E_HASHES_OU_NAO_DOCUMENTADO}}.

**Resposta efetiva transcrita fielmente:** {{RESPOSTA_OU_AINDA_NAO_APROVADO}}.

**Abrangência comprovada:** {{WHITE_BLACK_CONJUNTO_PAGINAS}}.

**Fonte persistente da decisão:** {{DOCUMENTO_LOCAL_E_TRECHO}}.

### 10.3. Hashes e estado das Pranchas finais

| Objeto | SHA-256 da submissão | SHA-256 físico final | STATUS final impresso | Resultado de GI-4 vinculado a decisão |
|---|---|---|---|---|
| White | {{SHA_HISTORICO}} | {{SHA_FINAL}} | {{STATUS}} | {{DECISAO}} |
| Black | {{SHA_HISTORICO}} | {{SHA_FINAL}} | {{STATUS}} | {{DECISAO}} |
| Conjunto | {{HASHES_HISTORICOS}} | {{HASHES_FINAIS}} | {{STATUS}} | {{DECISAO_CONJUNTO}} |

### 10.4. Decisões posteriores e ratificações, se existirem

| Data da decisão posterior | Data da formalização documental | Teor fiel / referência da declaração | Objetos e hashes abrangidos | Efeito comprovado, sem alterar decisão original |
|---|---|---|---|---|
| {{DATA_OU_NAO_APLICAVEL_FUNDAMENTADO}} | {{DATA_REGISTRO}} | {{TEOR_FIEL}} | {{OBJETO_HASHES}} | {{EFEITO}} |

### 10.5. Encerramento, congelamento e próxima etapa

**Resultado GI-4:** {{ESTADO_COMPROVADO_E_ABRANGENCIA}}.

**Resultado da interface no README operacional, se verificado:** {{SITUACAO_E_FONTE}}.

**Preservação e dependências:** {{ARQUIVOS_VERSOES_HASHES}}.

**Próxima ação documental permitida:** {{ACAO_CONDICIONADA_AO_GATE_E_AUTORIZACAO}}.
