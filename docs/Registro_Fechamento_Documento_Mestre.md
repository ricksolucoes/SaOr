# SaOr - Sales Order
## Registro Permanente de Fechamento da Documentação Mestre

**Finalidade:** manter um registro canônico dos problemas já identificados, decisões já fechadas, correções realizadas e critérios de promoção da Documentação Mestre, evitando reabrir decisões concluídas ou introduzir requisitos sem base documental.

**Documento canônico:** `docs/Documento_Mestre.md`  
**Branch de referência:** `main`  
**Versão atual em validação:** `0.7 — Candidata final à aprovação`

> Antes de propor qualquer alteração funcional futura, este registro deve ser consultado. Um item marcado como **RESOLVIDO** somente deve ser reaberto por decisão explícita do responsável do projeto ou por nova contradição comprovada no Documento Mestre canônico.

---

# 1. Regras permanentes para evitar regressões

1. Não inventar telas, fluxos, permissões, tecnologias ou regras de negócio sem base no Documento Mestre ou decisão explícita do responsável.
2. Não remover telas, módulos ou regras já documentadas sem decisão explícita registrada.
3. Toda ação visível deve possuir destino ou comportamento documentado.
4. Toda interface T/M/E deve manter Ficha funcional de aceite com os 12 critérios definidos na seção 28.
5. Prospect e Cliente continuam classificações do mesmo Cadastro Comercial.
6. Somente `CLIENTE + ATIVO` pode iniciar, avançar ou confirmar Pedido de Venda.
7. Cliente Bloqueado ou Inativo continua sendo Cliente.
8. `PROSPECT + ATIVO` não é combinação prevista na baseline atual.
9. Aprovação cadastral é externa ao fluxo funcional do vendedor nesta baseline; o SaOr recebe o resultado e aplica a transição definida.
10. Suporte oficial da interface é por WhatsApp, com fallback web e mensagem textual de indisponibilidade.
11. WCAG 2.2 AA é o mínimo obrigatório; AAA é o alvo quando viável; cor nunca é o único indicador.
12. Tecnologias definitivas pertencem ao Documento Técnico de Arquitetura, não à Documentação Mestre.
13. GitHub permanece somente para leitura por esta assistência; nenhuma alteração deve ser feita diretamente no repositório.
14. O Documento Mestre só passa para v1.0 após aprovação explícita do responsável.
15. O arquivo `docs/Documento_Mestre.md` é a referência canônica. Nomes temporários de arquivos de revisão, cópias locais ou sufixos de rodada não devem ser tratados como fontes oficiais.
16. O processo de evolução descrito no README deve permanecer alinhado ao processo oficial do Documento Mestre, inclusive a etapa de Slides de Navegação / Apresentação e suas validações.

---

# 2. Problemas históricos — situação atual no Documento Mestre canônico

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

# 3. Auditoria estrutural do Documento Mestre canônico

Na auditoria realizada sobre `docs/Documento_Mestre.md`:

- **71** interfaces T/M/E foram encontradas.
- **71** IDs são únicos.
- **0** referências T/M/E apontam para interface inexistente.
- **71/71** interfaces possuem Ficha funcional de aceite.
- **0** Fichas estão sem qualquer um dos 12 critérios estruturais.
- **0** ocorrências dos nomes antigos do projeto.
- **0** referências às versões 0.5 ou 0.6.
- **0** ocorrências de `React`, `ThemeProvider` ou `C45`.
- **0** fórmulas genéricas remanescentes de obrigatoriedade do tipo “a obrigatoriedade é indicada...” nas Fichas revisadas.
- A matriz de evolução possui **71** linhas.
- Os Textframes permanecem **Em validação** enquanto a aprovação humana não for declarada.
- Wireframe, Design, Figma, Protótipo e HTML permanecem **Pendente**.

---

# 4. Situação atual para fechar a Documentação Mestre

Não existe, nesta auditoria, bloqueador funcional conhecido que exija nova tela ou nova regra de negócio antes da aprovação humana.

O fechamento formal exige:

1. revisar o Documento Mestre canônico `docs/Documento_Mestre.md`;
2. registrar eventuais correções encontradas pelo responsável;
3. declarar explicitamente a aprovação da baseline funcional;
4. promover o Documento Mestre para `v1.0 — APROVADO / BASELINE FUNCIONAL`;
5. alterar as 71 linhas de Textframe de `Em validação` para `Aprovado`;
6. manter Wireframe, Design, Figma, Protótipo e HTML como `Pendente`;
7. atualizar este Registro Permanente para apontar a v1.0 como baseline oficial;
8. atualizar o README para refletir a aprovação da Documentação Mestre e a próxima etapa;
9. somente então iniciar a etapa de Wireframe.

---

# 5. README

O README deve permanecer sincronizado com o Documento Mestre.

Na revisão de consistência realizada antes da aprovação:

- a frase editorial temporária foi removida;
- o link visível da licença está alinhado ao arquivo `LICENSE`;
- o fluxo do projeto foi alinhado ao processo oficial do Documento Mestre, incluindo **Slides de Navegação / Apresentação** e as validações obrigatórias;
- foi incluído link para este `Registro_Fechamento_Documento_Mestre.md`;
- o status permanece **Em definição** enquanto a baseline funcional não estiver formalmente aprovada.

Após a aprovação da v1.0, o README deverá ser atualizado novamente para indicar que a Documentação Mestre foi aprovada e que a etapa seguinte está pendente/iniciando.

---

# 6. Controle de alterações futuras

Depois da aprovação da v1.0, qualquer requisito novo deve ser tratado como **mudança posterior à baseline**, seguindo a seção 31 do Documento Mestre. Não deve ser apresentado como se estivesse faltando na baseline aprovada, salvo quando houver contradição comprovada, defeito documental ou decisão explícita do responsável para reabrir o tema.

Toda proposta de alteração futura deve verificar primeiro:

1. o Documento Mestre canônico;
2. este Registro Permanente;
3. a existência de decisão já registrada sobre o tema;
4. se a mudança é correção de contradição, evolução posterior à baseline ou nova decisão de negócio.

Isso evita regressões documentais e a reinvenção de requisitos já decididos.
