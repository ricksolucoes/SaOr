# SaOr — {{ID}} — TextFrame da Tela — {{TEMA}} — {{VERSAO}}

**Estado vigente ({{DATA_DE_REFERENCIA_COMPROVADA}}):** GI-1 `{{ESTADO_GI1}}`; GI-2 `{{ESTADO_GI2}}`. **Origem visual aprovada:** {{CAMINHO_PNG}}; SHA-256 `{{HASH_FONTE_GI1}}`. **Fonte do aceite:** {{REFERENCIA_PERSISTENTE}}.

## 1. Identidade e origem visual aprovada

### 1.1. Identificação do TextFrame

| Campo | Valor comprovado |
|---|---|
| Interface (ID — nome oficial) | {{ID_NOME}} |
| Tema | {{WHITE_OU_BLACK}} |
| Página / total | {{XX/YY}} |
| Versão | {{VNN}} |
| Baseline funcional | {{BASELINE}} |
| Documento TextFrame | {{CAMINHO_RELATIVO_DESTE_MD}} |
| Unidade / estado principal representado | {{PAGINA_E_ESTADO}} |

### 1.2. PNG e controle GI-0/GI-1 de origem

| Fonte | Caminho | Dimensões | SHA-256 | Decisão / evidência de origem |
|---|---|---|---|---|
| PNG visual principal | {{CAMINHO}} | {{360x800}} | {{SHA}} | {{GI1}} |
| Controle GI-0/GI-1 | {{CAMINHO}} | {{TIPO}} | {{SHA}} | {{REFERENCIA}} |
| PNG alternativo, se aplicável | {{CAMINHO_OU_NAO_APLICAVEL_FUNDAMENTADO}} | {{DIMENSOES}} | {{SHA}} | {{REFERENCIA}} |

### 1.3. Estados e alcance visual documentado

| Estado ou variante | Identificador do PNG | Exigência / decisão funcional | Está abrangido neste TextFrame? |
|---|---|---|---|
| {{ESTADO}} | {{ARQUIVO}} | {{FONTE}} | {{SIM_NAO_FUNDAMENTADO}} |

## 2. Representação textual da Tela

### 2.1. TextFrame fiel em ordem de leitura

**Imagem representada:** {{CAMINHO_ESTADO}}. **Sequência:** {{ORDEM_DE_LEITURA_OBSERVADA}}.

**Representação textual completa:**

```text
{{DESCREVER_HIERARQUIA_VISUAL_DO_PNG_EM_ORDEM_DE_LEITURA_COM_ROTULOS_LITERAIS_SEM_CRIAR_COMPONENTES}}
```

**Estados com leitura distinta:** {{REFERENCIAS_AOS_ESTADOS_EM_LINHAS_DA_TABELA_2_3_OU_NAO_APLICAVEL_FUNDAMENTADO}}.

### 2.2. Elementos e agrupamentos na ordem visual

| Ordem | Estado/PNG | Grupo / elemento visível | Texto ou ícone literal | Relação pai/filho | Evidência da imagem |
|---|---|---|---|---|---|
| {{ORDEM}} | {{ESTADO}} | {{ELEMENTO}} | {{ROTULO_EXATO}} | {{GRUPO}} | {{PROVA}} |

### 2.3. Diferenças de representação entre estados

| Estado principal / alternativo | Elemento de referência | Conteúdo/posição que muda | Elementos que permanecem | PNG e fonte |
|---|---|---|---|---|
| {{ESTADO_OU_NAO_APLICAVEL_FUNDAMENTADO}} | {{ELEMENTO}} | {{DIFERENCA}} | {{PERSISTENTE}} | {{CAMINHO}} |

## 3. Geometria verificada

### 3.1. Convenção de coordenadas e método de medição

**Referencial:** origem local superior esquerda do PNG `360 × 800`, coordenadas inteiras `[x,y,w,h]`, salvo fonte/contrato aplicável em contrário.

**Método realmente executado:** {{METODO_DE_MEDICAO}}.

**Separação de provas:** {{CAIXAS_VISIVEIS_VS_HITBOX_OU_TOKENS_EXTERNOS}}.

### 3.2. Superfícies, containers e componentes

| Estado/PNG | ID do elemento | Componente / container | Caixa `[x,y,w,h]` | Pai / alinhamento | Método / evidência |
|---|---|---|---|---|---|
| {{ESTADO}} | {{ID}} | {{COMPONENTE}} | {{CAIXA_MEDIDA}} | {{RELACAO}} | {{MEDICAO}} |

### 3.3. Textos, ícones e subelementos visíveis

| Estado/PNG | Elemento pai | Subitem / linha literal | Caixa `[x,y,w,h]` | Espaçamento/sobreposição | Prova / limite |
|---|---|---|---|---|---|
| {{ESTADO}} | {{PAI}} | {{SUBITEM}} | {{CAIXA_MEDIDA}} | {{RELACAO}} | {{EVIDENCIA}} |

### 3.4. Medidas verificáveis e propriedades não recuperáveis

| Propriedade | Valor medido ou fonte externa | Evidência/método | Pode ser inferida somente do raster? | Limite declarado |
|---|---|---|---|---|
| {{PROPRIEDADE}} | {{VALOR_OU_NAO_COMPROVADO}} | {{PROVA}} | {{SIM_NAO}} | {{LIMITACAO}} |

## 4. Aparência e propriedades técnicas

### 4.1. Paleta, tokens, superfícies e contraste

| Elemento/estado | Token ou papel | Valor verificado | Fonte técnica / raster | Resultado/limite |
|---|---|---|---|---|
| {{ELEMENTO}} | {{TOKEN}} | {{COR}} | {{FONTE}} | {{RESULTADO}} |

### 4.2. Tipografia observada e especificada

| Texto/elemento | Conteúdo literal | Fonte/peso/tamanho comprovados | Fonte de comprovação | Limite raster |
|---|---|---|---|---|
| {{ELEMENTO}} | {{TEXTO}} | {{PARAMETROS_OU_NAO_COMPROVADO}} | {{EVIDENCIA}} | {{LIMITE}} |

### 4.3. Ícones, contornos e elevação

| Elemento | Glyph ou forma observável | Dimensão/cor/raio/sombra | Fonte técnica | Evidência / ressalva |
|---|---|---|---|---|
| {{ELEMENTO}} | {{GLYPH}} | {{VALORES}} | {{FONTE}} | {{PROVA}} |

### 4.4. Aparência dos estados e das ações

| Estado | Componente | Diferença visual | Token/variante permitida | Evidência |
|---|---|---|---|---|
| {{ESTADO}} | {{COMPONENTE}} | {{DIFERENCA}} | {{TOKEN}} | {{FONTE}} |

## 5. Conteúdo e comportamento funcional

### 5.1. Textos, dados e indicadores

| ID requisito | Texto/dado/rótulo literal | Elemento visível | Condição de exibição | Fonte funcional |
|---|---|---|---|---|
| {{ID}} | {{LITERAL}} | {{ELEMENTO}} | {{CONDICAO}} | {{FONTE}} |

### 5.2. Ações, destinos, cancelamentos e efeitos

| Ação | Estado/condição | Componente visual correspondente | Destino/retorno/efeito | Fonte |
|---|---|---|---|---|
| {{ACAO}} | {{CONDICAO}} | {{COMPONENTE}} | {{DESTINO}} | {{FONTE}} |

### 5.3. Exceções e decisões específicas da interface

| ID de decisão/diferença | Baseline original | Diferença aprovada | Abrangência | Documento e trecho de evidência |
|---|---|---|---|---|
| {{ID_OU_NAO_APLICAVEL_FUNDAMENTADO}} | {{FONTE}} | {{DIFERENCA}} | {{TEMA_ESTADO}} | {{REGISTRO}} |

## 6. Inventário de completude

### 6.1. Matriz requisito → PNG → caixa → TextFrame

| Requisito/elemento | Fonte | PNG/página/estado | Caixa `[x,y,w,h]` | Referência no TextFrame | Resultado |
|---|---|---|---|---|---|
| {{REQUISITO}} | {{FONTE}} | {{PNG}} | {{CAIXA}} | {{LOCAL}} | {{RESULTADO}} |

### 6.2. Confronto de ausências e excedentes

| Elemento confrontado | Consta no PNG? | Consta no TextFrame? | Requisito de origem | Ocorrência/justificativa |
|---|---|---|---|---|
| {{ELEMENTO_OU_NENHUM_APOS_VERIFICACAO}} | {{SIM_NAO}} | {{SIM_NAO}} | {{FONTE}} | {{RESULTADO}} |

## 7. Paginação, estados e variantes

### 7.1. Posições sequenciais de rolagem

| Página `XX/YY` | Offset/marco inicial e final | Elementos fixos | Elementos roláveis | Continuidade comprovada |
|---|---|---|---|---|
| {{PAGINA}} | {{MARCO_OU_NAO_APLICAVEL_FUNDAMENTADO}} | {{FIXOS}} | {{ROLAVEIS}} | {{EVIDENCIA}} |

### 7.2. Cobertura de estados/variantes exigidos

| Estado exigido | PNG e SHA-256 | Seção/linha de representação | Geometria correspondente | Cobertura/resultados |
|---|---|---|---|---|
| {{ESTADO}} | {{PNG_HASH}} | {{LOCAL}} | {{LOCAL_GEOMETRIA}} | {{RESULTADO}} |

### 7.3. Equivalência funcional entre temas

| Critério | White — referência | Black — referência | Resultado / diferença temática permitida |
|---|---|---|---|
| {{CRITERIO}} | {{FONTE}} | {{FONTE}} | {{RESULTADO}} |

## 8. Verificação de correspondência — GI-2

### 8.1. Testes oficiais executados

| Critério GI-2 previsto no contrato | Evidência física de confronto | Resultado | Pendência ou limitação |
|---|---|---|---|
| {{CRITERIO}} | {{PNG_TEXTFRAME_GEOMETRIA_REQUISITO}} | {{RESULTADO}} | {{LIMITACAO}} |

### 8.2. Resultado técnico e impedimentos

**Resultado técnico GI-2:** {{PARECER_COM_EVIDENCIAS}}.

**Pendências impeditivas:** {{ID_E_FUNDAMENTO_OU_NENHUMA}}.

**Dependência da decisão humana:** {{AGUARDANDO_OU_APROVACAO_COMPROVADA}}.

### 8.3. Limites de medição e reprodução

| Item | Informação verificável | Informação não comprovada | Fonte/método | Consequência |
|---|---|---|---|---|
| {{ITEM}} | {{VERIFICAVEL}} | {{NAO_COMPROVAVEL}} | {{METODO}} | {{IMPACTO}} |

## 9. Aprovação humana GI-2 e histórico

### 9.1. Decisão humana de GI-2 e abrangência

**Data comprovada:** {{DATA_DA_DECISAO_OU_AINDA_NAO_OCORRIDA}}.

**Declaração transcrita fielmente:** {{TEOR_OU_SEM_DECISAO}}.

**Objetos abrangidos (tema, página, estado, conjunto):** {{OBJETOS}}.

**Fonte persistente:** {{LOCALIZACAO_NO_REPOSITORIO}}.

### 9.2. Identidades da submissão e do conjunto aprovado

| Objeto | Tema/página/versão | Caminho | SHA-256 na decisão | Estado específico |
|---|---|---|---|---|
| PNG fonte | {{IDENTIDADE}} | {{CAMINHO}} | {{SHA}} | {{ESTADO}} |
| TextFrame | {{IDENTIDADE}} | {{CAMINHO}} | {{HASH_DA_VERSAO_APROVADA}} | {{ESTADO}} |
| Controle de origem | {{IDENTIDADE}} | {{CAMINHO}} | {{HASH_VINCULADO}} | {{ESTADO_REFERENCIADO}} |

### 9.3. Eventos posteriores, revisões e congelamento

| Data efetiva | Evento posterior | Versão/hash afetado | Decisão e abrangência | Resultado para o GI-2 |
|---|---|---|---|---|
| {{DATA_OU_NAO_APLICAVEL_FUNDAMENTADO}} | {{EVENTO}} | {{ARQUIVO_HASH}} | {{FONTE}} | {{RESULTADO}} |

**Estado vigente ao final do registro:** {{ESTADO_COMPROVADO}}.
