# SaOr — Estados globais — Mobile 360×800

Controle da versão vigente (com hash) e do histórico de versões das imagens dos estados globais do tema **black**. Escrito para o responsável humano, para o assistente de IA que gera ou usa as imagens e para qualquer LLM ou auditor que verifique o estado sem acesso a conversas. **Em caso de conflito com uma lembrança de conversa, vale este README.**

| Campo | Valor |
| --- | --- |
| Tema / resolução | `black` / Mobile 360 × 800 (única no escopo vigente do MVP) |
| Pasta | `docs/wireframes/images/black/Global/01_Mobile_360x800/` |
| Fonte funcional | `docs/Documento_Mestre.md`, seção 21 (Estados globais) |
| Fonte técnica | `.specs/wireframes/REGRAS-TECNICAS.md` (cores e componentes) |
| Tema equivalente | `../../../white/Global/01_Mobile_360x800/` (mesmos estados, versões equivalentes, mesmas caixas; só variam os tokens cromáticos) |
| Última atualização | 15/11/2026 |

---

## 1. Regras

1. Documentação em português do Brasil.
2. **Só existe o que está na seção 3.** Estado fora dela não tem imagem oficial: não presumir, não desenhar de memória, não inventar. Tela nova consulta esta pasta antes de desenhar e reutiliza a versão vigente; se faltar estado, registra a lacuna.
3. Estado sem tela aprovada que o defina fica como `Montar` e aguarda: não se cria por padrão visual.
4. **Toda versão criada é registrada** no histórico (seção 5), vigente ou não.
5. **Nunca sobrescrever** uma versão. Mudança gera `v02`, `v03`… e entra no histórico (seção 5).
6. **O hash é a identidade.** Conferir o SHA-256 (seção 4) antes de usar; hash diferente = arquivo não confiável.
7. **Aprovação não é presumida:** só vale `APROVADO` com data e hora registradas pelo responsável.
8. O que não puder ser medido ou comprovado fica `NÃO VALIDADO`; nunca afirmar.
9. Não herdar estados particulares de uma tela para outras telas sem decisão e registro próprios.
10. Quem gera os arquivos os entrega ao responsável; commit e publicação são decisão dele.

---

## 2. Convenção de nome

```text
GLOBAL-[NomeDoEstado]-[versão].png
```

- `[NomeDoEstado]`: nome do estado na seção 21 do Documento Mestre, em PascalCase, sem espaços nem acentos (por exemplo `Carregando`, `ListaVazia`, `SessaoExpirada`). Os estados globais não têm ID no catálogo; o nome é a chave.
- `[versão]`: `v` + 2 dígitos, como nas demais imagens do repositório.
- **Variação:** sufixo no final do nome, depois da versão, com `_` e a variação em PascalCase sem acentos. O arquivo sem sufixo é o estado base.
- Formato: PNG RGBA, tamanho exato do estado, escala 1:1, sem redimensionar, fundo fora do estado **transparente**.

---

## 3. Versão vigente (a ser utilizada)

| Estado | Arquivo | Versão | Dimensões (px) | Aprovação do responsável |
| --- | --- | --- | --- | --- |
| Carregando | `GLOBAL-Carregando-v01.png` | v01 | 336 × 128 | APROVADO (15/11/2026, 21:29) |
| Lista vazia | `GLOBAL-ListaVazia-v01.png` | v01 | 336 × 260 | APROVADO (15/11/2026, 21:38) |
| Erro | — | — | — | Nenhuma imagem criada até esta data |
| Sem conexão | — | — | — | Nenhuma imagem criada até esta data |
| Sessão expirada ou inválida | — | — | — | Nenhuma imagem criada até esta data |
| Acesso não autorizado | — | — | — | Nenhuma imagem criada até esta data |
| Salvando | — | — | — | Nenhuma imagem criada até esta data |
| Sucesso | — | — | — | Nenhuma imagem criada até esta data |

### 3.1. Especificação

- **Cores:** utilizar obrigatoriamente os tokens técnicos oficiais definidos em `.specs/wireframes/REGRAS-TECNICAS.md`, seções 6.5 (White) e 6.6 (Black), respeitando a precedência normativa da seção 6.1.
- **Ícones:** utilizar exclusivamente Material Icons Outlined, conforme a seção 9 de `REGRAS-TECNICAS.md`, sem substituições por outras bibliotecas, emojis ou ícones personalizados.

**Carregando**

| Item | Valor |
| --- | --- |
| Conteúdo | logomarca SaOr centralizada (64 px de altura, proporção original) e, abaixo dela, o texto `Carregando...` (Inter Regular 16 px, TEXT `#F2F2F2`), centralizado; o conjunto é centralizado verticalmente |
| Dimensões | 336 × 128 px, raio 16 px, fundo SURFACE-ALT `#2A2A2A`; espaçamento de 8 px entre a logomarca e o texto |
| Logomarca | arquivo oficial `assets/logo/saor-logo-SSO-para_fundos_escuro.png` (SHA-256 `302f1b6453bb39929c4635ffbd26fc96d05c45c34998df4b00359242004bbc94`), variante para fundos escuros; sem inversão de cores nem filtros |
| Uso | todas as áreas que consultam dados devem prever este estado |
| Referência | logomarca, altura, espaçamento, dimensões e fundo: C29 LoadingState (black) |
| Não validado | tamanho e cor do texto (o C29 usa Inter Regular 14 px em TEXT-2 para `Aguarde...`); o catálogo de identidade visual não define tamanho mínimo nem área de proteção da logomarca; decisão do responsável |

**Lista vazia**

| Item | Valor |
| --- | --- |
| Conteúdo | círculo de fundo de 48 px em SURFACE-ALT `#2A2A2A` com o ícone `assignment` (prancheta com lista) de 24 px em ACTION `#E0E0E0`, centralizado; título `Nenhum registro encontrado` em Inter SemiBold 20 px (`WF-TITLE`), TEXT `#F2F2F2`; descrição `Crie um novo registro para começar.` em Inter Regular 16 px (`WF-BODY`), TEXT-2 `#C2C2C2`; botão primário `CRIAR REGISTRO` de 288 × 48 px, raio 12 px, fundo Primary `#8ABEFF`, rótulo em Inter Medium 16 px (`WF-ACTION-TEXT`), On Primary `#0F1115` |
| Dimensões | 336 × 260 px, raio 16 px, fundo SURFACE `#1E1E1E`; círculo com o topo a 32 px, título (linha de 28 px) a 104 px, descrição (linha de 24 px) a 140 px e botão a 188 px do topo, com 24 px de margem lateral e 24 px abaixo do botão |
| Referência | círculo de ícone de 48 px em SURFACE-ALT sobre SURFACE, margens, espaçamentos e botão: C25 Dialog (black) e E00.7; estilos de texto: tokens de `REGRAS-TECNICAS.md` §5; ícone, título e descrição: definidos pelo responsável em 15/11/2026, 21:36 |
| Não validado | a escolha do ícone `assignment` como equivalente do `clipboard-list` pedido (a correspondência dos ícones de estado com a família Material Icons Outlined não está verificada e a T02 registra a tabela de ícones de estado como pendente); a cor ACTION do ícone; o fundo SURFACE do bloco (o Carregando usa SURFACE-ALT como o C29, e o círculo em SURFACE-ALT só aparece sobre SURFACE); o destino do botão `CRIAR REGISTRO`, que a seção 21 não define; o título e a descrição divergem do texto da seção 21 (`Nenhum registro ainda`), que não foi alterada; o C27 EmptyState existente é só a mensagem, sem ícone e sem botão |

**Erro**

| Item | Valor |
| --- | --- |
| Conteúdo | ícone de alerta (`⚠`), texto `Não foi possível carregar os dados` e botão `TENTAR NOVAMENTE` |
| Não validado | dimensões, token de cor por elemento e ícone Material Outlined do símbolo |

**Sem conexão**

| Item | Valor |
| --- | --- |
| Conteúdo | `⚠ Você está offline` e o texto `Algumas informações podem estar desatualizadas.` |
| Não validado | dimensões, token de cor por elemento e ícone Material Outlined do símbolo |

**Sessão expirada ou inválida**

| Item | Valor |
| --- | --- |
| Conteúdo | ícone de alerta, `Sua sessão expirou.`, `Entre novamente para continuar.` e botão `IR PARA LOGIN` |
| Destino | `IR PARA LOGIN` → T01 |
| Comportamento | a operação protegida é interrompida e o usuário é informado antes do retorno ao login; `Lembrar-me` não elimina essa regra; dados locais já preservados para sincronização não são descartados exclusivamente pela expiração da sessão |
| Não validado | dimensões, token de cor por elemento e ícone Material Outlined do símbolo |

**Acesso não autorizado**

| Item | Valor |
| --- | --- |
| Conteúdo | ícone de alerta, `Você não possui autorização para executar esta ação.` e botão `OK` |
| Comportamento | restrição já conhecida: a ação permanece indisponível com explicação textual; negativa durante a operação: a interface atual é preservada e informa que o usuário não possui autorização; a aplicação não simula sucesso nem perde dados de edição |
| Não validado | dimensões, token de cor por elemento e ícone Material Outlined do símbolo |

**Salvando**

| Item | Valor |
| --- | --- |
| Conteúdo | indicador de carregamento (`◌`) e o texto `Salvando...` |
| Não validado | dimensões, token de cor por elemento e ícone Material Outlined do símbolo |

**Sucesso**

| Item | Valor |
| --- | --- |
| Conteúdo | ícone de confirmação (`✓`) e o texto `Registro salvo` |
| Não validado | dimensões, token de cor por elemento e ícone Material Outlined do símbolo |

---

## 4. Integridade (SHA-256)

Os hashes ficam na tabela de histórico (seção 5). O arquivo `SHA256SUMS`, nesta pasta, traz os hashes das versões **vigentes** no formato do `sha256sum`. Em divergência, vale a tabela da seção 5.

Conferir, a partir desta pasta:

```text
sha256sum -c SHA256SUMS
```

Regenerar o `SHA256SUMS` a partir da tabela (após qualquer mudança na seção 5):

```text
grep -E '^\| [0-9/]+ \|.*\| VIGENTE \|' README.md | sed -E 's/.*`(GLOBAL-[^`]+)`.*`([0-9a-f]{64})`.*/\2  \1/' > SHA256SUMS
```

Esperado na conferência: tudo `OK`. Qualquer `FAILED` bloqueia o uso até decisão do responsável.

---

## 5. Histórico de versões

Registra **todas as versões criadas**, vigentes ou não. A versão em uso é a de situação `VIGENTE` (e é a da seção 3). Os arquivos de versões antigas permanecem na pasta.

| Data | Estado | Versão | Arquivo | SHA-256 | Situação | Motivo |
| --- | --- | --- | --- | --- | --- | --- |
| 15/11/2026 | Carregando | v01 | `GLOBAL-Carregando-v01.png` | `d59eed6745c39821b6497ba89ddb5c16fd8af21e602948d1618bdd3a8fbc18cb` | VIGENTE | Versão inicial |
| 15/11/2026 | Lista vazia | v01 | `GLOBAL-ListaVazia-v01.png` | `d27bbb4ea98d1bfba1e668bd12c52cff11b4b67acffcf7a9642894c44b8922f6` | VIGENTE | Versão inicial |

Situação: `VIGENTE`, `SUBSTITUÍDA por vNN` ou `RETIRADA (motivo)`.

---

## 6. Procedimentos

**Registrar um estado novo**
1. Conferir na seção 7 que ele é da seção 21 do Documento Mestre e ainda não existe. Se for `Montar`, parar.
2. Gerar o arquivo com o nome da seção 2, no tamanho exato do estado, escala 1:1.
3. Abrir a imagem e inspecionar: nada cortado, nada de elemento vizinho.
4. Calcular o SHA-256 e regenerar o `SHA256SUMS` (seção 4).
5. Registrar: seção 3 (arquivo, versão, dimensões, aprovação `PENDENTE`), seção 3.1 (especificação), seção 5 (linha `VIGENTE` com data, hash e motivo) e seção 7 (situação `Existe` e Feito ✅).
6. Entregar ao responsável. A aprovação só muda para `APROVADO` com a data e a hora da decisão dele.

**Mudar a versão:** gerar a versão seguinte sem sobrescrever a anterior; na seção 5, mudar a linha antiga para `SUBSTITUÍDA por vNN` e acrescentar a nova como `VIGENTE`, com data, hash e motivo; atualizar as seções 3 e 3.1; registrar a nova aprovação.

**Retirar:** na seção 5, marcar a linha como `RETIRADA (motivo)` e remover da seção 3.

---

## 7. Catálogo e situação

- **Feito** (✅): a imagem vigente já foi criada nesta pasta (situação `Existe`); ⬜ = ainda não feita.
- **Existe**: há imagem vigente aqui · **Parcial**: existe só dentro de uma tela aprovada (`telas/design/01_Mobile_360x800/`), precisa ser isolado e verificado · **Montar**: sem tela aprovada que o defina; **não criar** até autorização do responsável.
- A classificação veio dos nomes dos arquivos de `telas/design/01_Mobile_360x800/`; confirmar na imagem antes de produzir.
- Os estados globais não têm ID no catálogo do Documento Mestre; a chave é o nome do estado na seção 21.

| Estado | Situação | Onde já aparece | Feito |
| --- | --- | --- | --- |
| Carregando | Existe | `GLOBAL-Carregando-v01.png`; também aparece na T02: `T02-01-01_v01_estado-carregando.png` | ✅ |
| Lista vazia | Existe | `GLOBAL-ListaVazia-v01.png`; também aparece na T02: `T02-01-01_v01_estado-vazio.png` | ✅ |
| Erro | Parcial | T02: `T02-01-01_v01_estado-erro.png` | ⬜ |
| Sem conexão | Parcial | T02: `T02-01-02_v01_estado-offline.png` e `T02-02-02_v01_estado-offline.png` | ⬜ |
| Sessão expirada ou inválida | Montar | nenhuma tela aprovada | ⬜ |
| Acesso não autorizado | Montar | nenhuma tela aprovada | ⬜ |
| Salvando | Montar | nenhuma tela aprovada | ⬜ |
| Sucesso | Montar | nenhuma tela aprovada | ⬜ |

---

## 8. Documentos relacionados

| Documento | Para quê |
| --- | --- |
| `docs/Documento_Mestre.md` §21 | fonte dos estados globais |
| `docs/wireframes/images/black/componentes/01_Mobile_360x800/README.md` | README de referência (formato) |
| `.specs/wireframes/PROCESSO-TELA-PRANCHA.md` | pastas, nomes e Gates das telas |
| `.specs/wireframes/REGRAS-TECNICAS.md` | tokens, componentes técnicos, acessibilidade |
