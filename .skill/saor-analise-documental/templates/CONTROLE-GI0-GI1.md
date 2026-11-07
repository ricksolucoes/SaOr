# SaOr — {{ID}} — Controle GI-0/GI-1 — {{TEMA}} — {{VERSAO}}

**Estado vigente ({{DATA_DE_REFERENCIA_COMPROVADA}}):** GI-0 `{{ESTADO_GI0}}`; GI-1 `{{ESTADO_GI1}}`; GI-2 `{{ESTADO_GI2_SE_DOCUMENTADO}}`; GI-3 `{{ESTADO_GI3_SE_DOCUMENTADO}}`; GI-4 `{{ESTADO_GI4_SE_DOCUMENTADO}}`. **Fonte do estado:** {{DECISOES_PERSISTENTES}}. Os estados futuros ainda não verificados não são aprovações.

## 1. Identidade e fontes

### 1.1. Identificação da unidade documental

| Campo | Valor comprovado |
|---|---|
| Interface (ID — nome oficial) | {{ID_NOME}} |
| Tipo de interface | {{TIPO_CONFORME_BASELINE}} |
| Tema | {{WHITE_OU_BLACK}} |
| Página / total | {{XX/YY}} |
| Versão | {{VNN}} |
| Baseline funcional | {{VERSAO_BASELINE}} |
| Documento de controle | {{CAMINHO_RELATIVO_DESTE_MD}} |
| Registro de data/estado | {{DATA_E_EVIDENCIA}} |

### 1.2. Fontes funcionais, normativas e contratos aplicáveis

| Responsabilidade | Caminho e seção/trecho | Identificação física, se aplicável |
|---|---|---|
| Fonte funcional | {{CAMINHO_E_TRECHO_DOCUMENTO_MESTRE}} | {{SHA_SE_EXIGIDO}} |
| SPEC 3 | {{CAMINHO_E_SECAO}} | {{VERSAO_OU_SHA_SE_VERIFICADO}} |
| Gates oficiais | {{CAMINHO_E_SECAO}} | {{VERSAO_OU_SHA_SE_VERIFICADO}} |
| Regras técnicas | {{CAMINHO_E_SECAO}} | {{VERSAO_OU_SHA_SE_VERIFICADO}} |
| Seleção do template / contrato | {{CAMINHOS_REAIS}} | {{VERSAO_E_HASHES}} |
| Perfil visual | {{CAMINHO_DE_VIGENCIA}} | {{VERSAO_E_HASH}} |

### 1.3. Escopo do registro e fronteiras de preservação

**Objeto desta documentação:** {{UNIDADE_PAGINA_ESTADO_TEMA}}.

**Dependências consultadas:** {{CAMINHOS_RELATIVOS_PERTINENTES}}.

**Artefatos preservados/excluídos:** {{IDENTIFICACAO_E_FUNDAMENTO_NORMATIVO}}.

## 2. Inventário funcional — GI-0

### 2.1. Ficha funcional e condições de aplicação

| Propriedade | Evidência do Documento Mestre / decisão existente |
|---|---|
| Objetivo funcional | {{OBJETIVO_COM_FONTE}} |
| Contexto de entrada | {{CONTEXTO_COM_FONTE}} |
| Condição de exibição | {{CONDICOES_COM_FONTE}} |
| Resultado esperado | {{RESULTADO_COM_FONTE}} |
| Dependências entre interfaces | {{IDs_E_FONTES_OU_NAO_APLICAVEL_FUNDAMENTADO}} |

### 2.2. Matriz de requisitos rastreáveis

| ID requisito | Requisito exato | Fonte/trecho | Elemento ou comportamento esperado | Condição/estado | Evidência / lacuna | Situação fundamentada |
|---|---|---|---|---|---|---|
| {{ID_R}} | {{REQUISITO}} | {{FONTE}} | {{ELEMENTO}} | {{CONDICAO}} | {{EVIDENCIA}} | {{RESULTADO}} |

### 2.3. Cobertura e dependências do inventário

| Verificação de cobertura | Requisitos abrangidos | Evidência | Resultado |
|---|---|---|---|
| Textos e rótulos | {{IDs}} | {{EVIDENCIA}} | {{RESULTADO}} |
| Componentes e dados | {{IDs}} | {{EVIDENCIA}} | {{RESULTADO}} |
| Ações e destinos | {{IDs}} | {{EVIDENCIA}} | {{RESULTADO}} |
| Estados, exceções e condições | {{IDs}} | {{EVIDENCIA}} | {{RESULTADO}} |
| Acessibilidade, paginação e rolagem, se aplicáveis | {{IDs}} | {{EVIDENCIA}} | {{RESULTADO}} |

## 3. Fluxos, estados e paginação

### 3.1. Origem, ações, destino e retorno

| Evento / ação | Origem | Condição | Destino / retorno | Efeito comprovado | Fonte |
|---|---|---|---|---|---|
| {{EVENTO}} | {{ORIGEM}} | {{CONDICAO}} | {{DESTINO}} | {{EFEITO}} | {{FONTE}} |

### 3.2. Estados e variantes da interface

| Estado / variante | É exigido? | Gatilho / condição | Elementos distintos | Evidência / decisão |
|---|---|---|---|---|
| {{ESTADO}} | {{SIM_NAO_COM_FONTE}} | {{CONDICAO}} | {{ELEMENTOS}} | {{FONTE}} |

### 3.3. Páginas, rolagem e persistência visual

| Página / posição de rolagem | Marco inicial / final | Elementos fixos | Elementos roláveis | Continuidade / evidência |
|---|---|---|---|---|
| {{XX/YY}} | {{MARCO_OU_NAO_APLICAVEL_FUNDAMENTADO}} | {{ITENS}} | {{ITENS}} | {{EVIDENCIA}} |

## 4. Referências visuais e técnicas

### 4.1. Seleção e vigência por tema

| Fonte de seleção | Modelo / versão | Tema | Autoridade de vigência | Data/condição da seleção | Evidência |
|---|---|---|---|---|---|
| {{FONTE}} | {{MODELO_VNN}} | {{TEMA}} | {{REGISTRO}} | {{DATA}} | {{EVIDENCIA}} |

### 4.2. Arquivos oficiais, perfil Mobile e hashes

| Arquivo de referência | Caminho | Dimensões / tipo | SHA-256 | Verificação executada |
|---|---|---|---|---|
| {{FONTE_OFICIAL}} | {{CAMINHO}} | {{TIPO}} | {{SHA}} | {{METODO_RESULTADO}} |

### 4.3. Requisitos técnicos aplicáveis e limites de prova

| Parâmetro | Valor / critério aplicável | Fonte técnica | Evidência/limite |
|---|---|---|---|
| {{TOKEN_GRID_ESPACAMENTO_TIPOGRAFIA_ACESSIBILIDADE}} | {{REGRA}} | {{FONTE}} | {{EVIDENCIA_OU_NAO_COMPROVADO}} |

## 5. Lacunas, decisões e exceções

### 5.1. Diferenças entre a baseline e a representação

| ID ocorrência | Exigência original e fonte | Diferença identificada | Componente/efeito impactado | Evidência | Classificação |
|---|---|---|---|---|---|
| {{ID_OCORRENCIA}} | {{ORIGINAL}} | {{DIFERENCA}} | {{IMPACTO}} | {{PROVA}} | {{CLASSE}} |

### 5.2. Decisões humanas específicas e alcance

| ID decisão | Data comprovada | Texto/teor fiel da decisão | Objeto/tema/versão | Arquivos/hashes abrangidos | Resultado e fonte persistente |
|---|---|---|---|---|---|
| {{ID_DECISAO}} | {{DATA}} | {{TEOR}} | {{OBJETO}} | {{HASHES}} | {{EFEITO_FONTE}} |

### 5.3. Lacunas abertas e impedimentos reais

| ID pendência | Informação faltante | Evidência da lacuna | Impacto em Gate | Situação / decisão exigida |
|---|---|---|---|---|
| {{ID_PENDENCIA_OU_NAO_APLICAVEL}} | {{LACUNA}} | {{EVIDENCIA}} | {{GATE}} | {{SITUACAO}} |

## 6. Resultado técnico GI-0

### 6.1. Pré-condições e verificações GI-0

| Critério GI-0 conforme SPEC | Evidência verificada | Resultado técnico | Limitação |
|---|---|---|---|
| {{CRITERIO}} | {{PROVA_FISICA_DOCUMENTAL}} | {{CONFORME_NAO_CONFORME_BLOQUEADO}} | {{LIMITE}} |

### 6.2. Parecer e possibilidade de avançar

**Resultado GI-0:** {{RESULTADO_FUNDAMENTADO}}.

**Pendências impeditivas:** {{PENDENCIAS_OU_NENHUMA_COM_EVIDENCIA}}.

**Próxima operação permitida pelo Gate:** {{OPERACAO_SE_COMPROVADAMENTE_LIBERADA}}.

## 7. Inspeção visual GI-1

### 7.1. Inventário dos PNGs de Tela por página e estado

| Tema | Página/estado | Caminho da Tela isolada | Dimensões | SHA-256 | Data/condição da inspeção |
|---|---|---|---|---|---|
| {{TEMA}} | {{PAGINA_ESTADO}} | {{CAMINHO_RELATIVO}} | {{360x800_OU_RESULTADO}} | {{SHA}} | {{EVIDENCIA}} |

### 7.2. Inspeção física e visual itemizada

| Critério de inspeção | PNG/estado | Evidência visual ou técnica | Resultado | Limite |
|---|---|---|---|---|
| {{TEXTO_ALINHAMENTO_TOKENS_COMPONENTES_TRUNCAMENTO_ETC}} | {{PNG}} | {{EVIDENCIA}} | {{RESULTADO}} | {{LIMITE}} |

### 7.3. Confronto de equivalência White/Black

| Critério de equivalência | Evidência White | Evidência Black | Resultado / diferença autorizada |
|---|---|---|---|
| {{TEXTOS_ACOES_ORDEM_ESTADOS_PAGINAS}} | {{PROVA}} | {{PROVA}} | {{RESULTADO}} |

## 8. Aprovação humana GI-1

### 8.1. Manifestação humana e identificação da decisão

**Data comprovada:** {{DATA_DECISAO_OU_AUSENCIA}}.

**Texto/teor fiel:** {{DECLARACAO_OU_AINDA_NAO_OCORRIDA}}.

**Abrangência declarada:** {{TEMA_PAGINAS_ESTADOS_CONJUNTO}}.

**Fonte persistente:** {{LOCAL_DA_TRANSCRICAO}}.

### 8.2. Objetos e hashes efetivamente aprovados

| Objeto aprovado | Tema/página/estado | Caminho | SHA-256 da submissão aprovada | Resultado da decisão |
|---|---|---|---|---|
| {{PNG}} | {{TEMA_ESTADO}} | {{CAMINHO}} | {{SHA}} | {{ESTADO}} |

### 8.3. Ocorrências posteriores ao aceite visual

| Data | Evento posterior | Bytes/hash afetados | Decisão aplicável | Consequência para o GI-1 |
|---|---|---|---|---|
| {{DATA_OU_NAO_APLICAVEL_FUNDAMENTADO}} | {{EVENTO}} | {{OBJETO}} | {{FONTE}} | {{IMPACTO}} |

## 9. Vinculação ao GI-2

### 9.1. Identidade física do TextFrame associado

| Objeto | Tema/página/versão | Caminho | SHA-256 comprovado | Situação do documento |
|---|---|---|---|---|
| {{TEXTFRAME}} | {{IDENTIFICACAO}} | {{CAMINHO}} | {{SHA_OU_AINDA_INEXISTENTE}} | {{ESTADO}} |

### 9.2. Registro de referência ao aceite GI-2

| Decisão GI-2 no documento próprio | Data e abrangência | Hash da versão textual | PNG vinculado | Estado referido, sem herdar aceite |
|---|---|---|---|---|
| {{CAMINHO_SECAO_OU_PENDENTE}} | {{DATA_OBJETO}} | {{HASH}} | {{PNG_HASH}} | {{ESTADO}} |

## 10. Estado consolidado e histórico

### 10.1. Quadro vigente de Gates e referências

| Gate | Estado vigente comprovado | Objeto e versão | Decisão / evidência persistente |
|---|---|---|---|
| GI-0 | {{ESTADO}} | {{OBJETO}} | {{EVIDENCIA}} |
| GI-1 | {{ESTADO}} | {{OBJETO}} | {{EVIDENCIA}} |
| GI-2 | {{ESTADO}} | {{OBJETO}} | {{EVIDENCIA}} |
| GI-3 | {{ESTADO}} | {{OBJETO}} | {{EVIDENCIA}} |
| GI-4 | {{ESTADO}} | {{OBJETO}} | {{EVIDENCIA}} |

### 10.2. Linha do tempo documental (sem reescrever decisões)

| Data efetiva | Evento / Gate | Objeto | Evidência e hash da época | Estado após o evento |
|---|---|---|---|---|
| {{DATA}} | {{EVENTO}} | {{OBJETO}} | {{FONTE_HASH}} | {{ESTADO}} |

### 10.3. Preservações, dependências e próximo passo

**Arquivos que permanecem preservados:** {{CAMINHOS_E_VERSOES}}.

**Dependências pendentes:** {{REFERENCIAS_E_CONDICOES_OU_NENHUMA}}.

**Próximo passo permitido:** {{PASSO_E_GATE_APLICAVEL_COM_FONTE}}.
