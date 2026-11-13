# CONTROLE DE EVOLUÇÃO VISUAL

Cada interface deverá ter seu estágio acompanhado durante o projeto.

Estados permitidos para cada etapa:

```text
PENDENTE
EM VALIDAÇÃO
AJUSTES NECESSÁRIOS
APROVADO
```

**Última atualização:** 13/11/2026 — Wireframe aprovado e congelado (GI-4, Mobile `360 × 800`, temas Claro e Escuro) até a T02 v01, conforme a decisão D-22 do Controle da T02 (seis Pranchas, white e black, páginas 01/03 a 03/03). A contagem do Wireframe foi corrigida de 16/55 para 18/53: a matriz da seção 15 de `docs/wireframes/images/README.md` já tinha 17 interfaces aprovadas (T00 a E01.5), e a T02 passa a ser a 18ª.

Resumo do avanço (71 interfaces):

| Etapa | Aprovado | Pendente |
|---|---:|---:|
| Textframe | 71 | 0 |
| Wireframe | 18 | 53 |
| Design | 0 | 71 |
| Figma | 0 | 71 |
| Protótipo | 0 | 71 |
| HTML | 0 | 71 |

Fonte do estado do Wireframe: matriz da seção 15 de `docs/wireframes/images/README.md` e os registros de controle por tela em `docs/wireframes/images/<tema>/telas/`. Uma interface só consta como **Aprovado** no Wireframe quando as variações Claro e Escuro e o conjunto passaram pelo Gate GI-4. Para as interfaces com mais de uma versão (T00, T00.1 e T00.2), o estado refere-se à versão vigente.

Modelo resumido de acompanhamento:

| ID | Interface | Textframe | Wireframe | Design | Figma | Protótipo | HTML |
|---|---|---|---|---|---|---|---|
| T00 | Configuração da aplicação | Aprovado | Aprovado | Pendente | Pendente | Pendente | Pendente |
| T00.1 | Configuração da API | Aprovado | Aprovado | Pendente | Pendente | Pendente | Pendente |
| T00.2 | Aparência / Tema | Aprovado | Aprovado | Pendente | Pendente | Pendente | Pendente |
| T00.3 | Diagnóstico de conexão | Aprovado | Aprovado | Pendente | Pendente | Pendente | Pendente |
| M00.4 | Confirmar alteração da API | Aprovado | Aprovado | Pendente | Pendente | Pendente | Pendente |
| M00.5 | Restaurar configuração | Aprovado | Aprovado | Pendente | Pendente | Pendente | Pendente |
| E00.6 | Testando conexão | Aprovado | Aprovado | Pendente | Pendente | Pendente | Pendente |
| E00.7 | Conexão realizada | Aprovado | Aprovado | Pendente | Pendente | Pendente | Pendente |
| E00.8 | Falha de conexão | Aprovado | Aprovado | Pendente | Pendente | Pendente | Pendente |
| E00.9 | API não configurada | Aprovado | Aprovado | Pendente | Pendente | Pendente | Pendente |
| E00.10 | API indisponível no login | Aprovado | Aprovado | Pendente | Pendente | Pendente | Pendente |
| T01 | Login | Aprovado | Aprovado | Pendente | Pendente | Pendente | Pendente |
| T01.1 | Recuperar senha | Aprovado | Aprovado | Pendente | Pendente | Pendente | Pendente |
| E01.2 | Login inválido | Aprovado | Aprovado | Pendente | Pendente | Pendente | Pendente |
| E01.3 | Sem conexão | Aprovado | Aprovado | Pendente | Pendente | Pendente | Pendente |
| E01.4 | Recuperação solicitada | Aprovado | Aprovado | Pendente | Pendente | Pendente | Pendente |
| E01.5 | Falha ao solicitar recuperação | Aprovado | Aprovado | Pendente | Pendente | Pendente | Pendente |
| T02 | Início / Dashboard | Aprovado | Aprovado | Pendente | Pendente | Pendente | Pendente |
| T02.1 | Notificações | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T03 | Clientes e Prospects | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| M03.1 | Filtros de clientes | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| E03.2 | Busca sem resultado | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T04 | Cliente — Resumo | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T04.1 | Cliente — Pedidos | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T04.2 | Cliente — Visitas | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T04.3 | Cliente — Financeiro | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T04.4 | Cliente — Endereço | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T04.5 | Cliente — Dados cadastrais | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T05 | Novo Prospect — Dados básicos | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T05.1 | Novo Prospect — Endereço | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T05.2 | Novo Prospect — Informações comerciais | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T05.3 | Prospect — Resumo | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T05.4 | Prospect — Histórico de visitas | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T06 | Registrar visita | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| M06.1 | Finalizar visita | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T06.2 | Detalhes da visita | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| E06.3 | Falha ao finalizar visita | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T07 | Catálogo de produtos | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| M07.1 | Filtros de produtos | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| E07.2 | Produto não encontrado | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T08 | Detalhes do produto | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T09 | Pedido — Cliente | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| M09.1 | Selecionar cliente | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T09.2 | Selecionar endereço | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| M09.3 | Selecionar tabela de preço | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T10 | Pedido — Itens | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| M10.1 | Editar item | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T11 | Pedido — Condições comerciais | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T12 | Pedido — Revisão | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| M12.1 | Confirmar pedido | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T13 | Pedido confirmado | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T14 | Pedidos | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| M14.1 | Filtros de pedidos | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T15 | Detalhes do pedido | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T15.1 | Condições do pedido | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T15.2 | Endereço de entrega | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T16 | Agenda | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T16.1 | Agendar visita | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T16.2 | Compromisso / Visita | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| M16.3 | Confirmar cancelamento da visita | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| E16.4 | Falha ao cancelar visita | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T17 | Mais | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T17.1 | Meu perfil | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T17.2 | Sincronização | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T17.3 | Configurações | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T17.4 | Ajuda | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| T17.5 | Sobre | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| M17.6 | Confirmar saída | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| E17.7 | Sincronização em andamento | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| E17.8 | Sincronização concluída | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |
| E17.9 | Falha na sincronização | Aprovado | Pendente | Pendente | Pendente | Pendente | Pendente |

A matriz completa deverá ser atualizada conforme os wireframes, designs, frames no Figma, protótipos e páginas HTML forem concluídos.

Uma etapa somente poderá assumir **APROVADO** depois de sua validação obrigatória.

A aprovação de uma etapa libera a execução da etapa imediatamente seguinte. Estados **PENDENTE**, **EM VALIDAÇÃO** ou **AJUSTES NECESSÁRIOS** não liberam avanço.

Nenhuma tela já documentada será removida desse controle sem uma decisão explícita registrada neste Documento Mestre.