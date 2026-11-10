# GVA-5 — Suíte de testes da Skill de Auditoria

## 1. Autoridade, finalidade e fronteira

Esta suíte valida **o comportamento determinístico** de
`../scripts/auditar_integridade.py`, conforme `.specs/auditor/PROCESSO-AUDITORIA.md`,
`.specs/auditor/wireframes/CONTRATO-AUDITORIA-WIREFRAMES.md`,
`../SKILL.md`, `../references/CONTRATO-OPERACIONAL.md` e
`../references/FORMATO-RELATORIO.md`.

Não substitui esses contratos, não aprova Gates do domínio e não dispensa GVA-6
(validação cruzada) nem GVA-7 (segunda auditoria integral da implementação).
Os testes usam fontes **sintéticas e efêmeras**; seus hashes e decisões fictícios
**não** representam aprovadores nem objetos reais do SaOr. A suíte não altera a
SPEC, a Skill aprovada, o executor aprovado ou qualquer artefato funcional.

**Escopo original do GVA-5:** somente esta pasta `tests/`; o executor GVA-4
foi tratado como componente previamente aprovado. Se testes expuserem defeito
fora do lote autorizado, não alterar o executor: registrar reprodução, evidência,
risco e escopo para autorização separada. Em GVA-6 foram autorizadas correções
pontuais no executor e nesta suíte (T51–T60). No lote GVA-7, a autorização
específica abrange executor, testes, este README e a Skill operacional
(temporariedade documental), preservando os demais arquivos.

## 2. Pré-requisitos e execução reproduzível

- Python 3.9 ou superior (usa `pathlib.Path.is_relative_to` no executor).
- Biblioteca Pillow disponível para os testes de ViewPort. Ausência de Pillow
  não autoriza classificar a verificação de imagens como conforme.
- Sistema com suporte operacional a links simbólicos para os testes
  de segurança de filesystem (padrão Linux); ausência de permissão é limitação
  do ambiente e precisa ser relatada.
- A suíte não requer rede, GitHub, serviços externos, uploads ou acesso a `assets/`.

Executar na **raiz do clone ou da cópia local que contenha a Skill**:

```bash
PYTHONDONTWRITEBYTECODE=1 python -B -m unittest discover \
  -s .skill/saor-auditoria/tests -p 'test_*.py' -v
```

Para executar de forma dividida, preservando a seleção de casos e sem modificar
arquivos normativos:

```bash
cd .skill/saor-auditoria/tests
python -B -m unittest test_auditar_integridade.TestFonteEIntegridade -v
python -B -m unittest test_auditar_integridade.TestReferencias -v
python -B -m unittest test_auditar_integridade.TestHashesEVersoes -v
python -B -m unittest test_auditar_integridade.TestComparacoesEEstado -v
python -B -m unittest test_auditar_integridade.TestRegressoesGVA6 -v
python -B -m unittest test_auditar_integridade.TestRegressoesGVA7 -v
```

O resultado esperado é `Ran 73 tests` e `OK`, sem testes pulados, falhas ou erros.
Um resultado diferente **não** deve ser reinterpretado como sucesso. O relatório
de execução precisa conservar comando, Python e Pillow efetivos, SHA-256 do
executor, total de casos, falhas, erros, omissões e limitações. Saída `OK` testa
somente os comportamentos explicitamente assertados.

Os casos geram ZIPs, Markdown, catálogos SHA e PNGs **somente dentro de
`tempfile.TemporaryDirectory`**, destruído ao terminar cada caso. O executor
é invocado com `-B` e em modo somente leitura. A suíte não gera manifestos
persistentes ou pacotes de entrega; qualquer relatório materializado exige
aprovação própria pelo processo global.

## 3. Mapa completo de casos e evidências esperadas

| Caso | Verificação | Oráculo independente / condição esperada |
|---|---|---|
| T01 | Diretório físico regular | SHA calculado de bytes de fixture e retorno automático 0, sem aceite de encerramento |
| T02 | ZIP com raiz de repositório | CRC validado e caminhos normalizados sem raiz duplicada |
| T03 | Conteúdo ZIP com CRC adulterado | BLOQUEADO, ocorrência `integridade_zip`, membro não aprovado no inventário |
| T04 | Travessia `..` em ZIP | BLOQUEADO, `caminho_inseguro` |
| T05 | Nome absoluto em ZIP | BLOQUEADO, `caminho_inseguro` |
| T06 | Entradas repetidas de ZIP | BLOQUEADO, `duplicidade` |
| T07 | Colisão entre nomes por caixa | BLOQUEADO, `colisao_case_unicode` |
| T08 | Link simbólico em ZIP | BLOQUEADO, `entrada_especial` |
| T09 | Diretório simbólico | BLOQUEADO, sem seguir destino externo |
| T10 | Arquivo simbólico | BLOQUEADO, sem ler bytes externos |
| T11 | Conteúdo excluído em `assets/` | Arquivo/bytes/sha não aparecem no inventário/relatório |
| T12 | Tentativa de selecionar `assets/` | Rejeição explícita antes da auditoria |
| T13 | LEGADO declarado no fixture | Excluído; o relatório registra que a declaração não autentica a norma |
| T14 | Ausência de revisão declarada | Entrada rejeitada; não produzir conformidade |
| T15 | Escopo sem arquivos elegíveis | BLOQUEADO, `escopo_sem_arquivos` |
| T16 | Limite por arquivo | BLOQUEADO, `limite_expansao` |
| T17 | Limites totais contraditórios | Entrada inválida e BLOQUEADA |
| T18 | Fonte regular que não é ZIP | Entrada inválida e BLOQUEADA |
| T19 | Link Markdown local válido | Destino existente, estado CONFORME |
| T20 | Link para diretório existente | Resolvido sem referência quebrada falsa |
| T21 | Link para arquivo ausente | NÃO CONFORME, `referencia_quebrada` |
| T22 | Link saindo da raiz | BLOQUEADO, `link_inseguro` |
| T23 | URL externa | NÃO APLICÁVEL à resolução de caminhos locais |
| T24 | Link dentro de bloco de código | Não avaliado como referência ativa |
| T25 | Link direcionado a `assets/` | NÃO VALIDADO sem acessar arquivo protegido |
| T26 | Link para fora do escopo | NÃO VALIDADO, não declarar link quebrado |
| T27 | Link Markdown por referência | Limitação do parser explicitamente presente, nenhuma falsa cobertura |
| T28 | SHA-256 corrente correto | Igualdade com SHA de bytes sintéticos independentes |
| T29 | SHA-256 corrente incorreto | NÃO CONFORME, `hash_corrente_divergente` |
| T30 | Hash de submissão/aprovação distinto do arquivo atual | NÃO VALIDADO, sem erro automático nem mudança de Gate |
| T31 | Hash de ajuste da mesma versão | NÃO VALIDADO; não cria v02 nem histórico artificial |
| T32 | Hash de versão formal anterior | NÃO VALIDADO até verificação histórica; não sobrescreve atual |
| T33 | Hash de origem documentada | NÃO VALIDADO; não confunde com corrente |
| T34 | Hash não classificado | NÃO VALIDADO; nenhuma correção presumida |
| T35 | Hash ausente da linha física informada | NÃO VALIDADO, rejeita catálogo que não reflete a origem |
| T36 | Falta de indicação da autoridade | NÃO VALIDADO |
| T37 | Catálogo SHA incompleto | NÃO VALIDADO, sem substituição arbitrária |
| T38 | Hash referindo ao próprio arquivo | Ciclo identificado e divergência física detectada |
| T39 | Dois arquivos com referências SHA circulares | Ciclo identificado; não tenta estabilizar por edições |
| T40 | ViewPort idêntico | 12 pixels idênticos ao PNG do fixture |
| T41 | ViewPort com um pixel alterado | Exatamente 1 diferença, estado NÃO CONFORME |
| T42 | Geometria excede a Prancha | NÃO CONFORME, `geometria_viewport` |
| T43 | Conteúdo não é imagem decodificável | NÃO VALIDADO, sem alegar inspeção visual |
| T44 | Base incremental com inclusão/exclusão/alteração | Identifica exatamente 1 arquivo em cada categoria e 1 inalterado |
| T45 | Base incremental idêntica | Nenhuma alteração e 2 membros inalterados |
| T46 | Base anterior com link simbólico | `baseline_insegura`, resultado incremental com limitação explícita |
| T47 | Dois domínios, modos sob demanda e encerramento | Nenhum Gate ou encerramento é inferido automaticamente |
| T48 | Falha de link e invariância de bytes | Sem modificar fontes, sem relatório persistente nem `__pycache__` |
| T49 | Reexecução sem mudança física | Estruturas de saída JSON idênticas, ignorando nenhum campo |
| T50 | Controles sem automação semântica | AU-04/06/07/08/12 ficam NÃO VALIDADOS; encerramento não presumido |
| T51 | Cadeia acíclica de 1.350 arquivos | Retorna JSON, não lança `RecursionError` e não relata ciclos inexistentes |
| T52 | Ciclo único de 1.350 arquivos | Identifica o ciclo completo, sem depender do limite recursivo do Python |
| T53 | Dois ciclos independentes com ramificação | Retorna dois ciclos determinísticos e seus integrantes corretos |
| T54 | Arquivo regular como ancestral implícito em ZIP | BLOQUEADO com `colisao_arquivo_diretorio` |
| T55 | Mesma colisão, membros em ordem inversa | BLOQUEADO, independente da ordem de enumeração |
| T56 | Arquivo e diretório explícitos com mesmo caminho | BLOQUEADO, distinguindo diretório de arquivo |
| T57 | Colisão arquivo/diretório por caixa | BLOQUEADO mesmo com caminhos textuais diferentes |
| T58 | ZIP válido com diretório explícito e conteúdo | Aceito, sem falso positivo; arquivos inventariados |
| T59 | Colisão por equivalência Unicode NFC | BLOQUEADO sem tratar os nomes como independentes |
| T60 | Arquivo e diretório explícito com caixa diferente | BLOQUEADO por conflito de tipos entre os caminhos |
| T61 | Categoria de SHA-256 em JSON como lista | `NÃO VALIDADO` na referência; nenhuma exceção nem encerramento automático |
| T62 | Categoria de SHA-256 em JSON como objeto | `NÃO VALIDADO` na referência; nenhuma exceção nem encerramento automático |
| T63 | Categoria de SHA-256 em JSON como lista aninhada | `NÃO VALIDADO`, sem divergência de SHA inventada |
| T64 | ZIP com tipo Unix diretório, nome sem barra final | BLOQUEADO, `tipo_zip_incompativel`; membro não incorporado ao inventário |
| T65 | ZIP com tipo Unix arquivo regular, nome com barra final | BLOQUEADO, `tipo_zip_incompativel` |
| T66 | ZIP com tipo Unix diretório e nome canônico | Aceito sem falso positivo |
| T67 | ZIP com tipo Unix arquivo regular e nome canônico | Aceito, inventário correto |
| T68 | ZIP sem tipo Unix declarado | Aceito, ausência de tipo não confundida com incompatibilidade |
| T69 | ZIP com duas barras finais | BLOQUEADO, `caminho_inseguro` |
| T70 | ZIP com três barras finais | BLOQUEADO, `caminho_inseguro` |
| T71 | Diretório ZIP canônico terminado em uma barra | Aceito; arquivos descendentes inventariados |
| T72 | ZIP com separadores repetidos internos | BLOQUEADO, `caminho_inseguro` |
| T73 | Diretório-raiz ZIP com metadado Unix de arquivo regular | BLOQUEADO, `tipo_zip_incompativel` |

Os casos T01–T73 são identificados pelo prefixo numérico dos métodos
`test_01_...` a `test_73_...`. Os valores das fixtures são calculados ou
explicitamente construídos nos testes, sem usar hashes ou aprovações de outras
interfaces como oráculo. As afirmações de `CONFORME` representam somente a
capacidade especificada nos testes, não a auditoria da aplicação SaOr.

## 4. Relação com os controles AU e Gates de implementação

| Fonte de responsabilidade | Casos | Limite de cobertura |
|---|---|---|
| AU-00/AU-02, integridade física e seleção de escopo | T01–T18 | Byte/CRC/segurança nas fixtures; não comprova interpretação de normas |
| AU-06, resolução de referências | T19–T27 | Apenas links Markdown inline reconhecidos pelo executor |
| AU-06/AU-07/AU-08, identidade/versão/evidência | T28–T39 | Sem confirmar legitimidade de decisões humanas ou versões históricas |
| Verificação geométrica de domínio | T40–T43 | Comparação mensurável; não comprova semântica ou aprovação de imagens |
| AU-00/AU-02/AU-09, incremental e risco | T44–T46 | Hash/tamanho e erros de base; não valida diffs semânticos |
| AU-01/AU-08/AU-12, limites de inferência | T47/T50 | Rejeita encerramento automático; depende de auditoria assistida |
| AU-10/AU-11, autorização e preservação | T48/T49 | Somente ausência de escrita e determinismo do executor; não simula correção real |
| GVA6-OC-01, robustez do grafo de referências | T51–T53, além de T38/T39 | DFS iterativa e identificação de ciclos reais; não interpreta decisões de Gate |
| GVA6-OC-02, segurança de ZIP e caminhos | T54–T60, além de T02–T10 | Detecta colisão arquivo/diretório sem rejeitar diretórios legítimos |
| GVA7-OC-01, validação de categoria JSON | T61–T63, além de T28–T39 | Rejeição sem traceback; categorias não textuais nunca ganham estado CONFORME |
| GVA7-OC-02, tipo de membro ZIP | T64–T68 e T73, além de T02–T10 e T54–T60 | Bloqueia tipo Unix incompatível, preserva casos válidos e membros sem tipo explícito |
| GVA7-OC-03, caminho ZIP não canônico | T69–T72, além de T04–T05 | Rejeita barras finais repetidas, preserva uma barra terminal válida |

**GVA-5 não comprova sozinho AU-R01 a AU-R30.** Procedimentos que dependem de
SPEC, Skill, decisões humanas, completude editorial ou interpretação funcional
continuam reservados às verificações cruzadas e assistidas GVA-6/GVA-7.

## 5. Procedimento de segunda auditoria do GVA-5

1. Reabrir integralmente os arquivos de testes depois de todas as correções.
2. No GVA-5 original, conferir a identidade do executor aprovado. Na correção
   GVA6-OC-01/GVA6-OC-02 autorizada, conferir que somente o executor e os dois
   arquivos desta pasta foram modificados; preservar os demais artefatos.
3. Executar os seis grupos e, ao final, a descoberta integral com o comando
   da seção 2; documentar eventuais limites de tempo do ambiente.
4. Confirmar que T01–T73 foram descobertos exatamente uma vez, sem skipped,
   errors ou failures; verificar se os critérios positivos e negativos foram
   realmente assertados no código.
5. Investigar falsos positivos, validações apenas textuais e as dependências
   normativas que ainda não são verificáveis pelo executor.
6. Defeito novo no executor fora do escopo corretivo: **não** ampliar a
   alteração sem autorização específica. Preservar a evidência e delimitar
   o bloqueio. A correção autorizada de GVA6-OC-01/OC-02 deve ser revalidada.
7. Na etapa original do GVA-5, não antecipar GVA-6. Em reauditorias posteriores, revalidar apenas os Gates impactados conforme as autorizações; nunca declarar encerramento global sem os aceites necessários.

A ausência de erros conhecidos em 73 fixtures não constitui prova de ausência
de outros defeitos. O relatório do GVA-5 deverá separar resultados executados,
controles não cobertos e hipóteses não confirmadas.

## 6. Regularização GVA-6 — duas ocorrências comprovadas

A correção autorizada de `GVA6-OC-01` substitui a busca recursiva de
`hash_cycles` por travessia iterativa. O teste reproduz cadeias acíclicas
longas, ciclos longos e ciclos independentes ramificados (T51–T53), além
das autorreferências/ciclos curtos originais (T38–T39). A classificação
`NÃO VALIDADO` do vínculo temporal permanece e o código não corrige hashes.

A correção autorizada de `GVA6-OC-02` rejeita arquivos ZIP regulares que
sejam simultaneamente diretórios explícitos ou ancestrais implícitos de
outros membros elegíveis, inclusive sob normalização Unicode/casefold
(T54–T57, T59–T60). Diretórios válidos, explícitos ou implícitos, não
constituem colisão (T58). O auditor não extrai nem altera os ZIPs.

A validação de GVA-6 exige os resultados efetivos, a verificação de
regressão dos 50 casos anteriores, o diff dos três arquivos alterados
e o confronto físico dos demais artefatos com os hashes aprovados.
Passar 60 testes **não** significa aprovação automática do GVA-6 ou
liberação do GVA-7.

## 7. Regularização GVA-7 — três erros e referências temporais

O lote autorizado de GVA-7 corrige exclusivamente:

- **GVA7-OC-01:** `hash_checks()` verifica o tipo da categoria antes de consultar
  o conjunto `HASH_CLASSES`; valores JSON não textuais ficam `NÃO VALIDADO`,
  nunca lançam `TypeError` por teste de pertinência não hashable. T61–T63.
- **GVA7-OC-02:** `enumerate_zip()` compara tipo Unix explícito (`S_IFREG` ou
  `S_IFDIR`) com `ZipInfo.is_dir()`, incluindo o diretório-raiz explícito. O
  conflito bloqueia a verificação antes da leitura de conteúdo. Ausência de
  tipo Unix explícito não é motivo automático de rejeição. T64–T68 e T73.
- **GVA7-OC-03:** `archive_path()` aceita uma única barra final para diretório,
  mas não remove silenciosamente barras extras. Nomes com segmentos vazios
  continuam bloqueados. T69–T72.
- **GVA7-OC-04:** a Skill registra a existência **condicional à inspeção física**
  do executor e da suíte, sem prometer execução, instalação ou aceite automático.

Para encerrar a reauditoria deste lote, comparar os quatro arquivos modificados
com a identidade anterior, executar T01–T73, repetir casos adversariais de forma
independente dos próprios testes, confrontar os dez arquivos fora do escopo com
seus SHA-256 aprovados, verificar referências e registrar limitações. **Aprovação
de testes não substitui o aceite humano do GVA-7 nem libera automaticamente o
GVA-8.** Nenhum arquivo será empacotado sem autorização do Gate correspondente.
