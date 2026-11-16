# SaOr — Estados globais — Mobile 360×800

Controle da versão vigente (com hash) e do histórico de versões das imagens dos estados globais do tema **white**. Escrito para o responsável humano, para o assistente de IA que gera ou usa as imagens e para qualquer LLM ou auditor que verifique o estado sem acesso a conversas. **Em caso de conflito com uma lembrança de conversa, vale este README.**

| Campo | Valor |
| --- | --- |
| Tema / resolução | `white` / Mobile 360 × 800 (única no escopo vigente do MVP) |
| Pasta | `docs/wireframes/images/white/Global/01_Mobile_360x800/` |
| Fonte funcional | `docs/Documento_Mestre.md`, seção 21 (Estados globais) |
| Fonte técnica | `.specs/wireframes/REGRAS-TECNICAS.md` (cores e componentes) |
| Tema equivalente | `../../../black/Global/01_Mobile_360x800/` (mesmos estados, versões equivalentes, mesmas caixas; só variam os tokens cromáticos) |
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
| Carregando | `GLOBAL-Carregando-v01.png` | v01 | 336 × 128 | APROVADO (15/11/2026, 21:30) |
| Lista vazia | `GLOBAL-ListaVazia-v01.png` | v01 | 336 × 260 | APROVADO (15/11/2026, 21:40) |
| Erro | `GLOBAL-Erro-v01.png` | v01 | 336 × 224 | APROVADO (16/11/2026, 09:11) |
| Sem conexão | `GLOBAL-SemConexao-v01.png` | v01 | 336 × 84 | APROVADO (16/11/2026, 09:17) |
| Sessão expirada ou inválida | `GLOBAL-SessaoExpirada-v01.png` | v01 | 336 × 260 | APROVADO (16/11/2026, 09:24) |
| Acesso não autorizado | `GLOBAL-AcessoNaoAutorizado-v01.png` | v01 | 336 × 248 | APROVADO (16/11/2026, 09:27) |
| Salvando | `GLOBAL-Salvando-v01.png` | v01 | 336 × 128 | APROVADO (16/11/2026, 09:31) |
| Sucesso | `GLOBAL-Sucesso-v01.png` | v01 | 336 × 156 | APROVADO (16/11/2026, 09:46) |
| Sucesso atualizado | `GLOBAL-SucessoAtualizado-v01.png` | v01 | 336 × 156 | APROVADO (16/11/2026, 09:46) |
| Sucesso excluído | `GLOBAL-SucessoExcluido-v01.png` | v01 | 336 × 156 | APROVADO (16/11/2026, 09:46) |
| Confirmação de exclusão | `GLOBAL-ConfirmarExclusao-v01.png` | v01 | 312 × 256 | APROVADO (16/11/2026, 09:46) |

### 3.1. Especificação

- **Cores:** utilizar obrigatoriamente os tokens técnicos oficiais definidos em `.specs/wireframes/REGRAS-TECNICAS.md`, seções 6.5 (White) e 6.6 (Black), respeitando a precedência normativa da seção 6.1.
- **Ícones:** utilizar exclusivamente Material Icons Outlined, conforme a seção 9 de `REGRAS-TECNICAS.md`, sem substituições por outras bibliotecas, emojis ou ícones personalizados.

**Carregando**

| Item | Valor |
| --- | --- |
| Conteúdo | logomarca SaOr centralizada (64 px de altura, proporção original) e, abaixo dela, o texto `Carregando...` (Inter Regular 16 px, TEXT `#1A1A1A`), centralizado; o conjunto é centralizado verticalmente |
| Dimensões | 336 × 128 px, raio 16 px, fundo SURFACE-ALT `#EAEAEA`; espaçamento de 8 px entre a logomarca e o texto |
| Logomarca | arquivo oficial `assets/logo/saor-logo-SSO-para_fundos_claros.png` (SHA-256 `dd4082946acfce2d25ccf2b154949ec3df8c1d36fe2a8cfa406e4054949cf419`), variante para fundos claros; sem inversão de cores nem filtros |
| Uso | todas as áreas que consultam dados devem prever este estado |
| Referência | logomarca, altura, espaçamento, dimensões e fundo: C29 LoadingState (white) |
| Não validado | tamanho e cor do texto (o C29 usa Inter Regular 14 px em TEXT-2 para `Aguarde...`); o catálogo de identidade visual não define tamanho mínimo nem área de proteção da logomarca; decisão do responsável |

**Lista vazia**

| Item | Valor |
| --- | --- |
| Conteúdo | círculo de fundo de 48 px em SURFACE-ALT `#EAEAEA` com o ícone `assignment` (prancheta com lista) de 24 px em ACTION `#333333`, centralizado; título `Nenhum registro encontrado` em Inter SemiBold 20 px (`WF-TITLE`), TEXT `#1A1A1A`; descrição `Crie um novo registro para começar.` em Inter Regular 16 px (`WF-BODY`), TEXT-2 `#565656`; botão primário `CRIAR REGISTRO` de 288 × 48 px, raio 12 px, fundo Primary `#004A99`, rótulo em Inter Medium 16 px (`WF-ACTION-TEXT`), On Primary `#FFFFFF` |
| Dimensões | 336 × 260 px, raio 16 px, fundo SURFACE `#FFFFFF`; círculo com o topo a 32 px, título (linha de 28 px) a 104 px, descrição (linha de 24 px) a 140 px e botão a 188 px do topo, com 24 px de margem lateral e 24 px abaixo do botão |
| Referência | círculo de ícone de 48 px em SURFACE-ALT sobre SURFACE, margens, espaçamentos e botão: C25 Dialog (white) e E00.7; estilos de texto: tokens de `REGRAS-TECNICAS.md` §5; ícone, título e descrição: definidos pelo responsável em 15/11/2026, 21:36 |
| Não validado | a escolha do ícone `assignment` como equivalente do `clipboard-list` pedido (a correspondência dos ícones de estado com a família Material Icons Outlined não está verificada e a T02 registra a tabela de ícones de estado como pendente); a cor ACTION do ícone; o fundo SURFACE do bloco (o Carregando usa SURFACE-ALT como o C29, e o círculo em SURFACE-ALT só aparece sobre SURFACE); o destino do botão `CRIAR REGISTRO`, que a seção 21 não define; o título e a descrição divergem do texto da seção 21 (`Nenhum registro ainda`), que não foi alterada; o C27 EmptyState existente é só a mensagem, sem ícone e sem botão |

**Erro**

| Item | Valor |
| --- | --- |
| Conteúdo | círculo de fundo de 48 px em SURFACE-ALT `#EAEAEA` com o ícone `warning` (alerta) de 24 px em Error `#991B1B`, centralizado; mensagem `Não foi possível carregar os dados` centralizada em Inter Regular 16 px (`WF-BODY`), TEXT `#1A1A1A`; botão primário `TENTAR NOVAMENTE` de 288 × 48 px, raio 12 px, fundo Primary `#004A99`, rótulo em Inter Medium 16 px (`WF-ACTION-TEXT`), On Primary `#FFFFFF` |
| Dimensões | 336 × 224 px, raio 16 px, fundo SURFACE `#FFFFFF`; círculo com o topo a 32 px, mensagem (linha de 24 px) a 104 px e botão a 152 px do topo, com 24 px de margem lateral e 24 px abaixo do botão |
| Referência | círculo de ícone de 48 px em SURFACE-ALT sobre SURFACE, margens, espaçamentos e botão: Lista vazia aprovada (white), C25 Dialog (white) e E00.7; ícone de alerta em Error e mensagem em Inter Regular 16 px: C28 ErrorState (white); textos: seção 21 do Documento Mestre |
| Não validado | a escolha do ícone `warning` para o símbolo `⚠` (a correspondência dos ícones de estado com a família Material Icons Outlined não está verificada e a T02 registra a tabela de ícones de estado como pendente); o fundo SURFACE do bloco (o Carregando usa SURFACE-ALT como o C29); o destino do botão `TENTAR NOVAMENTE`, que a seção 21 não define (repetir a consulta que falhou é a leitura do rótulo, não regra documentada); a mensagem sem título e descrição separados, como na seção 21 |

**Sem conexão**

| Item | Valor |
| --- | --- |
| Conteúdo | banner sem botão: ícone `wifi_off` de 24 px em Warning (texto/ícone) `#AC4F01`, título `Você está offline` em Inter SemiBold 14 px (`WF-SECTION`) e descrição `Algumas informações podem estar desatualizadas.` em Inter Regular 14 px, ambos em TEXT `#1A1A1A`, alinhados à esquerda a 52 px da borda, em linhas de 20 px |
| Dimensões | 336 × 84 px, raio 16 px, borda de 1 px em Warning `#AC4F01`; fundo derivado: Warning a 15% de opacidade sobre SURFACE `#FFFFFF` (`#F3E5D9`); ícone com a caixa de 24 px a 16 px da borda esquerda e a 12 px do topo; linhas de base do texto a 27, 47 e 67 px do topo |
| Referência | layout do banner offline aprovado da T02 (`T02-01-02_v01_estado-offline.png`, caixa `[12,153,336,84]`), do qual esta imagem foi isolada; textos: seção 21 do Documento Mestre; fundo derivado: `REGRAS-TECNICAS.md` §6.3 e DIF-09 do Controle da T02; cores: `REGRAS-TECNICAS.md` §6.5 |
| Não validado | a cor Warning difere da T02 white: a T02 usa `#7C4A03` (D-12, DM §20.1, "vale somente para o T02") com fundo `#EBE4D9`, e esta imagem usa o token `#AC4F01` da §6.5, com fundo derivado `#F3E5D9`; o contraste do ícone e da borda sobre o fundo derivado é 4,39:1 e o do texto é 14,11:1 (calculados, não medidos); o fundo derivado continua lacuna do §6.3 (PEND-01 da T02), aprovada só para a T02 (D-24); a equivalência dos nomes de ícone com a família Material Icons Outlined não está verificada; a seção 21 mostra `⚠` no início do texto e a T02 usa `wifi_off` |

**Sessão expirada ou inválida**

| Item | Valor |
| --- | --- |
| Conteúdo | círculo de fundo de 48 px em SURFACE-ALT `#EAEAEA` com o ícone `warning` (alerta) de 24 px em Warning (texto/ícone) `#AC4F01`, centralizado; título `Sua sessão expirou.` em Inter SemiBold 20 px (`WF-TITLE`), TEXT `#1A1A1A`; descrição `Entre novamente para continuar.` em Inter Regular 16 px (`WF-BODY`), TEXT-2 `#565656`; botão primário `IR PARA LOGIN` de 288 × 48 px, raio 12 px, fundo Primary `#004A99`, rótulo em Inter Medium 16 px (`WF-ACTION-TEXT`), On Primary `#FFFFFF` |
| Dimensões | 336 × 260 px, raio 16 px, fundo SURFACE `#FFFFFF`; círculo com o topo a 32 px, título (linha de 28 px) a 104 px, descrição (linha de 24 px) a 140 px e botão a 188 px do topo, com 24 px de margem lateral e 24 px abaixo do botão |
| Destino | `IR PARA LOGIN` → T01 |
| Comportamento | a operação protegida é interrompida e o usuário é informado antes do retorno ao login; `Lembrar-me` não elimina essa regra; dados locais já preservados para sincronização não são descartados exclusivamente pela expiração da sessão |
| Referência | composição, medidas e espaçamentos: Lista vazia aprovada (white), C25 Dialog (white) e E00.7; textos e destino: seção 21 do Documento Mestre |
| Não validado | a cor Warning do ícone (a seção 21 mostra `⚠` e não indica a cor; o Erro usa Error, o aviso do banner Sem conexão usa Warning); o Warning do white é o token `#AC4F01` da §6.5, e não o `#7C4A03` da T02 (D-12, "vale somente para o T02"); a escolha do ícone `warning` para o símbolo `⚠` (a correspondência dos ícones de estado com a família Material Icons Outlined não está verificada e a T02 registra a tabela de ícones de estado como pendente); o fundo SURFACE do bloco (o Carregando usa SURFACE-ALT como o C29); se o estado é bloco de página ou janela modal, que a seção 21 não define |

**Acesso não autorizado**

| Item | Valor |
| --- | --- |
| Conteúdo | círculo de fundo de 48 px em SURFACE-ALT `#EAEAEA` com o ícone `warning` (alerta) de 24 px em Warning (texto/ícone) `#AC4F01`, centralizado; mensagem `Você não possui autorização para executar esta ação.` centralizada, em duas linhas (`Você não possui autorização para` / `executar esta ação.`), em Inter Regular 16 px (`WF-BODY`), TEXT `#1A1A1A`; botão primário `OK` de 288 × 48 px, raio 12 px, fundo Primary `#004A99`, rótulo em Inter Medium 16 px (`WF-ACTION-TEXT`), On Primary `#FFFFFF` |
| Dimensões | 336 × 248 px, raio 16 px, fundo SURFACE `#FFFFFF`; círculo com o topo a 32 px, mensagem (duas linhas de 24 px) a 104 px e botão a 176 px do topo, com 24 px de margem lateral e 24 px abaixo do botão |
| Comportamento | restrição já conhecida: a ação permanece indisponível com explicação textual; negativa durante a operação: a interface atual é preservada e informa que o usuário não possui autorização; a aplicação não simula sucesso nem perde dados de edição |
| Referência | composição, medidas e espaçamentos: Erro aprovado (white), Lista vazia aprovada (white), C25 Dialog (white) e E00.7; textos e botão: seção 21 do Documento Mestre |
| Não validado | a cor Warning do ícone (a seção 21 mostra `⚠` e não indica a cor; o Erro usa Error e a Sessão expirada usa Warning); o Warning do white é o token `#AC4F01` da §6.5, e não o `#7C4A03` da T02 (D-12, "vale somente para o T02"); a escolha do ícone `warning` para o símbolo `⚠` (a correspondência dos ícones de estado com a família Material Icons Outlined não está verificada e a T02 registra a tabela de ícones de estado como pendente); o fundo SURFACE do bloco (o Carregando usa SURFACE-ALT como o C29); o destino do botão `OK`, que a seção 21 não define (a leitura do rótulo é fechar o aviso); se o estado é bloco de página ou janela modal, que a seção 21 não define; o bloco mostra a mensagem negada durante a operação, e a variante de ação indisponível com explicação textual não tem imagem |

**Salvando**

| Item | Valor |
| --- | --- |
| Conteúdo | logomarca SaOr centralizada (64 px de altura, proporção original) e, abaixo dela, o texto `Salvando...` (Inter Regular 16 px, TEXT `#1A1A1A`), centralizado; o conjunto é centralizado verticalmente |
| Dimensões | 336 × 128 px, raio 16 px, fundo SURFACE-ALT `#EAEAEA`; espaçamento de 8 px entre a logomarca e o texto |
| Logomarca | arquivo oficial `assets/logo/saor-logo-SSO-para_fundos_claros.png` (SHA-256 `dd4082946acfce2d25ccf2b154949ec3df8c1d36fe2a8cfa406e4054949cf419`), variante para fundos claros; sem inversão de cores nem filtros |
| Referência | mesma composição do Carregando aprovado (white), que segue o C29 LoadingState (white); texto: seção 21 do Documento Mestre, que usa o mesmo símbolo `◌` do Carregando |
| Não validado | a escolha de repetir a logomarca do Carregando para o Salvando (a seção 21 usa o mesmo `◌` nos dois estados e não define a imagem); a imagem é estática e não distingue Salvando de Carregando além do texto; tamanho e cor do texto (o C29 usa Inter Regular 14 px em TEXT-2 para `Aguarde...`); o catálogo de identidade visual não define tamanho mínimo nem área de proteção da logomarca; decisão do responsável |

**Sucesso**

| Item | Valor |
| --- | --- |
| Conteúdo | círculo de fundo de 48 px em SURFACE-ALT `#EAEAEA` com o ícone `check` (confirmação) de 24 px em Success `#166534`, centralizado; texto `Registro salvo` em Inter SemiBold 20 px (`WF-TITLE`), TEXT `#1A1A1A`, centralizado |
| Dimensões | 336 × 156 px, raio 16 px, fundo SURFACE `#FFFFFF`; círculo com o topo a 32 px e texto (linha de 28 px) a 104 px do topo, com 24 px abaixo do texto |
| Referência | composição, medidas e espaçamentos: Lista vazia aprovada (white), C25 Dialog (white) e E00.7; texto: seção 21 do Documento Mestre; cor Success: REGRAS-TECNICAS §6.5 |
| Não validado | a escolha do ícone `check` para o símbolo `✓` (a correspondência dos ícones de estado com a família Material Icons Outlined não está verificada e a T02 registra a tabela de ícones de estado como pendente); o uso do círculo de fundo e da cor Success no ícone (a seção 21 mostra apenas `✓`); o estilo do texto (a seção 21 não define tamanho nem peso); o fundo SURFACE do bloco (o Carregando usa SURFACE-ALT como o C29); se o estado é bloco de página ou janela modal, que a seção 21 não define; decisão do responsável |

**Sucesso atualizado**

| Item | Valor |
| --- | --- |
| Conteúdo | variação do Sucesso: mesmo círculo de fundo de 48 px em SURFACE-ALT `#EAEAEA` e ícone `check` de 24 px em Success `#166534`; texto `Registro atualizado` em Inter SemiBold 20 px (`WF-TITLE`), TEXT `#1A1A1A` |
| Dimensões | 336 × 156 px, raio 16 px, fundo SURFACE `#FFFFFF`; mesmas medidas do Sucesso |
| Referência | Sucesso (white) |
| Não validado | o texto `Registro atualizado`, que não consta na seção 21 do Documento Mestre (solicitado pelo responsável); demais itens, os mesmos do Sucesso |

**Sucesso excluído**

| Item | Valor |
| --- | --- |
| Conteúdo | variação do Sucesso: mesmo círculo de fundo de 48 px em SURFACE-ALT `#EAEAEA` e ícone `check` de 24 px em Success `#166534`; texto `Registro excluído` em Inter SemiBold 20 px (`WF-TITLE`), TEXT `#1A1A1A` |
| Dimensões | 336 × 156 px, raio 16 px, fundo SURFACE `#FFFFFF`; mesmas medidas do Sucesso |
| Referência | Sucesso (white) |
| Não validado | o texto `Registro excluído`, que não consta na seção 21 do Documento Mestre (solicitado pelo responsável); o ícone `check` para uma exclusão; demais itens, os mesmos do Sucesso |

**Confirmação de exclusão**

| Item | Valor |
| --- | --- |
| Conteúdo | círculo de fundo de 48 px em tom translúcido de Error sobre SURFACE (`#F2E1E1`) com o ícone `error_outline` (advertência) de 24 px em Error `#991B1B`; título em duas linhas, `Deseja excluir` / `este registro?`, em Inter SemiBold 20 px (`WF-TITLE`), TEXT `#1A1A1A`, centralizado; ações no fim da linha, como no M00.5: `CANCELAR` como rótulo sem superfície em Primary `#004A99` e botão preenchido `EXCLUIR` de 140 × 48 px, raio 12 px, fundo Error `#991B1B`, rótulo em On Primary `#FFFFFF`; rótulos em Inter Medium 16 px (`WF-ACTION-TEXT`) |
| Dimensões | 312 × 256 px (largura do C25 Dialog e do M00.5), raio 16 px, fundo SURFACE `#FFFFFF`; círculo com o topo a 32 px, título (duas linhas de 28 px) a 104 px e ações a 184 px do topo, com 24 px de margem lateral e 24 px abaixo das ações |
| Destino | `CANCELAR` fecha a janela sem excluir; `EXCLUIR` executa a exclusão e leva ao Sucesso excluído |
| Referência | M00.5 Restaurar configuração (white): círculo de ícone, ações no fim da linha, `CANCELAR` sem superfície e botão destrutivo preenchido em Error; C25 Dialog (largura 312, margem 24, raio 16); versão black aprovada |
| Não validado | o estado não consta na seção 21 do Documento Mestre (solicitado pelo responsável); o tom do círculo (derivado por mistura de Error sobre SURFACE, sem token próprio); a cor On Primary no rótulo sobre Error (a REGRAS-TECNICAS não define "On Error"); a quebra do título em duas linhas; os destinos descritos; a escolha do ícone `error_outline`; se é janela modal com escurecimento do fundo, que a imagem não desenha |

--- | --- |
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
| 15/11/2026 | Carregando | v01 | `GLOBAL-Carregando-v01.png` | `446cf705af2f922d80132e96d26501e423bac93e9ebf5d27cb464816df8079c2` | VIGENTE | Versão inicial |
| 15/11/2026 | Lista vazia | v01 | `GLOBAL-ListaVazia-v01.png` | `2701ea32fc321b8c63e0a594944043a9328e04ce93ff1e862442fec0ccddbcad` | VIGENTE | Versão inicial |
| 16/11/2026 | Erro | v01 | `GLOBAL-Erro-v01.png` | `5377d2abf6ace8179fbc14ea9516ea9a8ed70bed467e15f1fbfa4dd03483f099` | VIGENTE | Versão inicial |
| 16/11/2026 | Sem conexão | v01 | `GLOBAL-SemConexao-v01.png` | `5bd91f697395680b7a0fe18d2c3ca75f558a814a26bdaa0fab7572f28bf39c89` | VIGENTE | Versão inicial |
| 16/11/2026 | Sessão expirada ou inválida | v01 | `GLOBAL-SessaoExpirada-v01.png` | `b14c4a246a4fccc4f7246fd1db7e97feeb4466b302b41d4c0779393952fef5ad` | VIGENTE | Versão inicial |
| 16/11/2026 | Acesso não autorizado | v01 | `GLOBAL-AcessoNaoAutorizado-v01.png` | `992797d3143f9a1fa399b7665e9fe5e2a66919746aaaffe8ddb8913afd10633c` | VIGENTE | Versão inicial |
| 16/11/2026 | Salvando | v01 | `GLOBAL-Salvando-v01.png` | `b0a8a70ced01af2672b83a0ba5b0933ab83c270b9d044d08ffb837b51af41360` | VIGENTE | Versão inicial |
| 16/11/2026 | Sucesso | v01 | `GLOBAL-Sucesso-v01.png` | `716f927c9676856deba628bb2c025c65985bf4af51ffa4404d613d2bceae2932` | VIGENTE | Versão inicial |
| 16/11/2026 | Sucesso atualizado | v01 | `GLOBAL-SucessoAtualizado-v01.png` | `590160e54d8102aa81bdb224e8237abfaa9e504122da2e5ee5118a4c5523499b` | VIGENTE | Versão inicial |
| 16/11/2026 | Sucesso excluído | v01 | `GLOBAL-SucessoExcluido-v01.png` | `fd8e3303909625fe5fe6ea26770b7cf5867c733b9dccf8bc8bbce06b67c5330e` | VIGENTE | Versão inicial |
| 16/11/2026 | Confirmação de exclusão | v01 | `GLOBAL-ConfirmarExclusao-v01.png` | `459787c5db279b6f1f7fcab004c19e688d679d17683c53bf7022dcd8ad4e2c7a` | VIGENTE | Versão inicial |

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
| Erro | Existe | `GLOBAL-Erro-v01.png`; também aparece na T02: `T02-01-01_v01_estado-erro.png` | ✅ |
| Sem conexão | Existe | `GLOBAL-SemConexao-v01.png`; também aparece na T02: `T02-01-02_v01_estado-offline.png` e `T02-02-02_v01_estado-offline.png` | ✅ |
| Sessão expirada ou inválida | Existe | `GLOBAL-SessaoExpirada-v01.png` | ✅ |
| Acesso não autorizado | Existe | `GLOBAL-AcessoNaoAutorizado-v01.png` | ✅ |
| Salvando | Existe | `GLOBAL-Salvando-v01.png` | ✅ |
| Sucesso | Existe | `GLOBAL-Sucesso-v01.png` | ✅ |
| Sucesso atualizado | Existe | `GLOBAL-SucessoAtualizado-v01.png` | ✅ |
| Sucesso excluído | Existe | `GLOBAL-SucessoExcluido-v01.png` | ✅ |
| Confirmação de exclusão | Existe | `GLOBAL-ConfirmarExclusao-v01.png` | ✅ |

---

## 8. Documentos relacionados

| Documento | Para quê |
| --- | --- |
| `docs/Documento_Mestre.md` §21 | fonte dos estados globais |
| `docs/wireframes/images/white/componentes/01_Mobile_360x800/README.md` | README de referência (formato) |
| `.specs/wireframes/PROCESSO-TELA-PRANCHA.md` | pastas, nomes e Gates das telas |
| `.specs/wireframes/REGRAS-TECNICAS.md` | tokens, componentes técnicos, acessibilidade |
