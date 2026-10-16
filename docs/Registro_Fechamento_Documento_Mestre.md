# SaOr - Sales Order
## Registro Permanente de Fechamento da Documentação Mestre

**Finalidade:** manter um registro canônico dos problemas já identificados, decisões já fechadas, correções realizadas e critérios de promoção da Documentação Mestre, evitando reabrir decisões concluídas ou introduzir requisitos sem base documental.

**Base utilizada:** `docs/Documento_Mestre.md` do branch `main` antes desta rodada de ajustes.  
**Versão funcional em revisão:** `0.7 — Candidata final à aprovação`.  
**Arquivo candidato revisado:** `SaOr_Documento_Mestre_v0.7_Candidata_Final_Rev3.md`.

> Antes de propor qualquer alteração funcional futura, este registro deve ser consultado. Um item marcado como **RESOLVIDO** somente deve ser reaberto por decisão explícita do responsável do projeto ou por nova contradição comprovada no Documento Mestre.

---

# 1. Regras permanentes para evitar regressões

1. Não inventar telas, fluxos, permissões, tecnologias ou regras de negócio sem base no Documento Mestre ou decisão explícita do responsável.
2. Não remover telas, módulos ou regras já aprovadas sem decisão explícita registrada.
3. Toda ação visível deve possuir destino ou comportamento documentado.
4. Toda interface T/M/E deve manter Ficha funcional de aceite com os 12 critérios definidos na seção 28.
5. Prospect e Cliente continuam classificações do mesmo Cadastro Comercial.
6. Somente `CLIENTE + ATIVO` pode iniciar/avançar/confirmar Pedido de Venda.
7. Cliente Bloqueado ou Inativo continua sendo Cliente.
8. `PROSPECT + ATIVO` não é combinação prevista na baseline atual.
9. Aprovação cadastral é externa ao fluxo funcional do vendedor nesta baseline; o SaOr recebe o resultado e aplica a transição definida.
10. Suporte oficial da interface é por WhatsApp, com fallback web e mensagem textual de indisponibilidade.
11. WCAG 2.2 AA é o mínimo obrigatório; AAA é o alvo quando viável; cor nunca é o único indicador.
12. Tecnologias definitivas pertencem ao Documento Técnico de Arquitetura, não à Documentação Mestre.
13. GitHub permanece somente para leitura por esta assistência; nenhuma alteração deve ser feita diretamente no repositório.
14. O Documento Mestre só passa para v1.0 após aprovação explícita do responsável.

---

# 2. Problemas históricos — situação atual na candidata Rev3

| Problema | Situação |
|---|---|
| Referências a versões antigas | **RESOLVIDO** |
| Nomes antigos do produto | **RESOLVIDO** |
| Recuperação de senha sem sucesso/erro | **RESOLVIDO** — E01.4 / E01.5 |
| Compartilhar pedido sem comportamento | **RESOLVIDO** — compartilhamento nativo |
| Reagendar visita sem destino | **RESOLVIDO** — T16.1 em modo de edição |
| Cancelar visita sem confirmação/erro | **RESOLVIDO** — M16.3 / E16.4 |
| Sincronização sem estados | **RESOLVIDO** — E17.7 / E17.8 / E17.9 |
| Ajuda/suporte sem canal | **RESOLVIDO** — WhatsApp |
| Política de Privacidade/Termos sem comportamento | **RESOLVIDO** |
| Abrir no mapa sem comportamento | **RESOLVIDO** |
| Notificações sem destinos | **RESOLVIDO** |
| Histórico de visitas do Prospect sem destinos | **RESOLVIDO** |
| Finalização de visita sem retorno/erro | **RESOLVIDO** — M06.1 / E06.3 |
| “Lembrar-me” indefinido | **RESOLVIDO** |
| Permissão para alterar API indefinida | **RESOLVIDO funcionalmente** |
| Matriz incompleta | **RESOLVIDO** — 71 interfaces |
| Interfaces sem Ficha funcional de aceite | **RESOLVIDO** — 71/71 |
| E01.3 “Tentar novamente” implícito | **RESOLVIDO** |
| M03.1 Limpar/Aplicar implícito | **RESOLVIDO** |
| Consulta de CEP implícita | **RESOLVIDO** |
| “Novo pedido” da prévia de tema parecendo interativo | **RESOLVIDO** |
| `ThemeProvider` na documentação UX | **RESOLVIDO** |
| Aprovação cadastral parecendo pendência do Documento Mestre | **RESOLVIDO** |
| Estados de sucesso/processamento classificados como erro | **RESOLVIDO** |
| M03.1 divergente entre campos e textframe | **RESOLVIDO** |
| Campos obrigatórios descritos genericamente | **RESOLVIDO** |
| T17.2 sem relação completa com E17.7/E17.8/E17.9 | **RESOLVIDO** |
| T05.2 citado em modo edição sem comportamento definido | **RESOLVIDO** — dois modos sob o mesmo ID |
| T04.1 Novo Pedido sem regra explícita de elegibilidade | **RESOLVIDO** |
| T06 Iniciar Pedido disponível para Prospect/Cliente impedido | **RESOLVIDO** |
| Catálogo/produto com possibilidade implícita de inclusão fora de pedido | **RESOLVIDO** — nesta baseline T07/T08 operam no pedido em edição |
| Situação operacional não aparecendo no exemplo de lista de Clientes | **RESOLVIDO** |
| Sessão expirada sem comportamento global | **RESOLVIDO** |
| Acesso não autorizado sem comportamento global | **RESOLVIDO** |
| Falha/conflito offline sem garantia funcional de preservação | **RESOLVIDO** — dados pendentes preservados; sem sobrescrita silenciosa |
| Relações de retorno ausentes em algumas Fichas | **RESOLVIDO** |

---

# 3. Auditoria estrutural da candidata Rev3

- **71** interfaces T/M/E.
- **71** IDs únicos.
- **0** referências T/M/E sem definição correspondente.
- **71/71** interfaces com Ficha funcional de aceite.
- **0** Fichas faltando qualquer um dos 12 critérios estruturais.
- **0** ocorrências dos nomes antigos do projeto.
- **0** referências às versões 0.5 ou 0.6.
- **0** ocorrências de `React`, `ThemeProvider` ou `C45`.
- **0** fórmulas genéricas remanescentes de obrigatoriedade do tipo “a obrigatoriedade é indicada...” ou “conforme regras da seção” nas Fichas revisadas.
- Matriz de evolução com **71** linhas.
- Textframes permanecem **Em validação**.
- Wireframe, Design, Figma, Protótipo e HTML permanecem **Pendente**.

---

# 4. Pendência atual para fechar a Documentação Mestre

Não existe, nesta auditoria, bloqueador funcional conhecido que exija nova tela ou nova regra de negócio antes da revisão humana.

Falta somente o processo de aprovação:

1. revisar a candidata Rev3;
2. registrar eventuais correções encontradas pelo responsável;
3. declarar explicitamente a aprovação da baseline funcional;
4. promover o Documento Mestre para `v1.0 — APROVADO / BASELINE FUNCIONAL`;
5. alterar as 71 linhas de Textframe de `Em validação` para `Aprovado`;
6. manter Wireframe, Design, Figma, Protótipo e HTML como `Pendente`;
7. somente então iniciar a etapa de Wireframe.

---

# 5. README

Foi preparada uma versão corrigida do README para conferência com os dois problemas editoriais conhecidos resolvidos:

- removida a frase `Sugestão mais clara e madura para o README:`;
- texto visível do link da licença alterado de `LICENSE.md` para `LICENSE`, mantendo o destino `LICENSE`.

Esses ajustes são editoriais e não alteram a baseline funcional do Documento Mestre.

---

# 6. Controle de alterações futuras

Depois da aprovação da v1.0, qualquer requisito novo deve ser tratado como **mudança posterior à baseline**, seguindo a seção 31 do Documento Mestre. Não deve ser apresentado como se estivesse faltando na baseline aprovada, salvo quando houver contradição comprovada, defeito documental ou decisão explícita do responsável para reabrir o tema.
