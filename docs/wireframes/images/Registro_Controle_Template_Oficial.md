# SaOr — Registro Permanente de Controle do Template Oficial

**Natureza:** controle permanente de seleção vigente, decisões históricas e integridade dos artefatos de template.  
**Data de formalização:** 28/10/2026.  
**Decisão vigente registrada:** **Modelo C selecionado em `white` e `black` em 28/10/2026.**  
**Estado:** versões físicas `APROVADO E CONGELADO`; seleção do Modelo C **VIGENTE até revisão formal**, sem prazo presumido.  
**Baseline funcional relacionada:** `v1.0 — APROVADO / BASELINE FUNCIONAL`, sem mudança de requisitos.  
**Etapa funcional seguinte:** produção das interfaces T/M/E, ainda pendentes.

---

## 1. Vigência atual e histórico de decisões

**Este registro é permanente e independente do nome do modelo selecionado.** A seleção vigente é uma decisão **revisável mediante necessidade comprovada**; os arquivos de cada versão aprovada continuam congelados. As regras normativas de identificação da referência pertencem à SPEC 2: [`.specs/wireframes/REFERENCIA-TEMPLATE-OFICIAL.md`](../../../.specs/wireframes/REFERENCIA-TEMPLATE-OFICIAL.md).

### 1.1 Entrada histórica de aprovação — 28/10/2026

**Decisão:** Modelo C selecionado como template oficial para as duas variações, sem modificar a baseline funcional `v1.0`.

- `white`: `WF-TEMPLATE-C_v02` — **APROVADO E CONGELADO; VIGENTE**.
- `black`: `WF-TEMPLATE-C_v01` — **APROVADO E CONGELADO; VIGENTE**.
- Data da formalização: **28/10/2026**.
- Justificativa registrada: encerramento da seleção entre os modelos A/B/C para uso funcional ordinário, com integridade das referências white/black e preservação dos modelos históricos.
- Versões anteriores A/B e C permanecem como referências e histórico; sua existência não equivale a vigência.
- Ativação: decisão expressa de oficialização em 28/10/2026. **Nenhuma substituição posterior foi registrada nesta revisão documental.**

### 1.2 Registro de eventos futuros

Cada substituição ou revisão deve ser **acrescentada ao histórico**, sem apagar esta entrada: identificador do evento; data; modelo/tema/versão anterior e nova; defeito ou necessidade demonstrada; comparação de alternativas; impacto nas interfaces existentes; autorização explícita; hashes e caminhos de todos os artefatos; evidências de Gates/validações aplicáveis; data de ativação; versão que deixou de estar vigente. Um modelo não pode ser registrado como novo vigente até que a aprovação esteja concluída.

---

## 2. Inventário da versão vigente — artefatos imutáveis e origem

Todos os caminhos da tabela são relativos à raiz do repositório. As quatro cópias oficiais de Prancha C/Wireframe Text e as duas cópias de Viewport técnico foram criadas **sem qualquer alteração de bytes** em relação às suas origens. Os arquivos de Viewport passam a integrar o conjunto oficial congelado, **sem reabrir** a aprovação original das pranchas ou constituir uma Tela funcional.

| Tema | Cópia oficial congelada | Origem preservada | SHA-256 (ambos) |
|---|---|---|---|
| `white` | `docs/wireframes/images/white/template/WF-TEMPLATE-C_v02.png` | `docs/wireframes/images/references/templates/white/WF-TEMPLATE-C_v02.png` | `558d108e3b0fec923e478482749c678f4b50d8b09055441ee52a9392b0f4929d` |
| `white` | `docs/wireframes/images/white/template/WF-TEMPLATE-C_v02.md` | `docs/wireframes/images/references/templates/white/wiframetext/WF-TEMPLATE-C_v02.md` | `89154c5c1dda6f1aa1a16ac85a641a3ddc3101da8011f727eaec2c68141980c7` |
| `black` | `docs/wireframes/images/black/template/WF-TEMPLATE-C_v01.png` | `docs/wireframes/images/references/templates/black/WF-TEMPLATE-C_v01.png` | `a1c6816cd14e0ea74f1bfb02842581dd7f3fa400c190087cbfa33e93f3b3cb63` |
| `black` | `docs/wireframes/images/black/template/WF-TEMPLATE-C_v01.md` | `docs/wireframes/images/references/templates/black/wiframetext/WF-TEMPLATE-C_v01.md` | `60e1a8f476fc36233033d3c99f1588f21ee560967c31d6a31f6fb13e43b1892b` |
| `white` | `docs/wireframes/images/white/template/WF-VIEWPORT-360x800.png` | `docs/wireframes/images/references/white/WF-VIEWPORT-360x800.png` | `7de6522e31df89c8925093691442726ef7f72724bcde5905fb3380e4c5c5687c` |
| `black` | `docs/wireframes/images/black/template/WF-VIEWPORT-360x800.png` | `docs/wireframes/images/references/black/WF-VIEWPORT-360x800.png` | `fde139557c36375f5ce569f4884822d4fd7c8344da1ce777b72873e1885a73fd` |

Os arquivos `.md` oficiais são **cópias integrais** dos Wireframe Text já aprovados, incluindo sua documentação original de caminhos, histórico, aprovações e diferenças entre temas. As referências internas a `references/templates/` e `references/white|black/` correspondem à origem/documentação dos ativos e **não** autorizam reconstruir ou alterar as cópias oficiais.

Os dois PNGs aprovados das **Pranchas** medem `1280 × 1920 px`; os dois **Viewports** oficiais medem `360 × 800 px`, conforme as specs vigentes. Os originais dos Viewports continuam em `docs/wireframes/images/references/{white,black}/` e não foram movidos; as cópias oficiais estão nas pastas `white/template/` e `black/template/`. Os Viewports contêm conteúdo demonstrativo e não são Telas funcionais novas nem precisam de Wireframe Text independente.

## 3. Regra de congelamento — proteção equivalente à baseline funcional

As **seis cópias da versão atualmente vigente** (Prancha PNG + Wireframe Text + Viewport PNG por tema) e suas **seis origens preservadas** constituem o conjunto de referência congelado. Em substituições futuras, cada inventário aprovado permanece neste histórico e o registro indica separadamente qual versão está vigente. Não é permitido:

1. editar, recortar, redimensionar, recalcular, recolorir, reexportar ou substituir os PNGs;
2. editar o conteúdo dos Wireframe Text congelados, inclusive ajustes editoriais silenciosos;
3. sobrescrever ou reutilizar os nomes oficiais para conteúdo diferente;
4. selecionar outro modelo ou versão sem nova decisão expressa e registro de vigência;
5. reinterpretar a aprovação de uma variação como aprovação automática de outra;
6. modificar a baseline funcional `v1.0` para acomodar o template;
7. usar o bitmap de Viewport demonstrativo como Tela funcional aprovada ou alterar as cópias de Viewport.

**Qualquer futura mudança exige necessidade concreta e documentada**, não apenas preferência visual, conveniência de montagem ou otimização genérica. Não há revisão automática ou periódica presumida.

### 3.1 Procedimento obrigatório para solicitar revisão ou substituir a referência

1. identificar o defeito comprovado, novo requisito ou incompatibilidade concreta, citando fontes técnicas e/ou arquivos afetados;
2. verificar se o problema pode ser resolvido na **interface específica** sem alterar o template; comparar formalmente as alternativas de manter, revisar ou selecionar outro modelo;
3. avaliar impactos em white/black, PNGs, Wireframe Text, ViewPorts, versões aprovadas e saídas funcionais que dependem do modelo atual;
4. registrar proposta, diferença prevista, justificativa, plano de validação, risco e preservação do histórico;
5. obter aprovação **humana explícita**, antes de executar qualquer alteração; silêncio não é aprovação;
6. construir e aprovar a **nova versão** pela SPEC 1 e seus contratos técnicos, se houver novo artefato, sem sobrescrever versões anteriores;
7. registrar evidências de integridade, tema, caminho, SHA-256, aprovação humana, vínculo com anterior e data de ativação;
8. atualizar a **vigência** somente após aprovação completa, mantendo a decisão anterior neste registro como evento histórico;
9. analisar explicitamente a eventual migração das interfaces dependentes; não convertê-las automaticamente.

Uma revisão de decisão não autoriza editar arquivos físicos aprovados. Aplicam-se também `.specs/PROCESSO-ALTERACAO-ASSISTIDA.md` e a SPEC 2.

## 4. Fronteira documental

**Este registro não define o processo de produção das interfaces.** A sequência de Wireframe Text da Tela, Tela de Referência e Prancha de Implementação pertence exclusivamente à SPEC 3 [`.specs/wireframes/PROCESSO-TELA-PRANCHA.md`](../../../.specs/wireframes/PROCESSO-TELA-PRANCHA.md). Sua consulta aqui restringe-se à referência oficialmente **vigente na data da produção**. As saídas já aprovadas conservam vínculo com o modelo e a versão exatos empregados em cada uma.

A SPEC 1 governa somente a definição técnica de uma **nova Prancha do Template**; a SPEC 2 governa a seleção, validação e preservação da referência; a SPEC 3 governa o uso funcional. Nenhum processo de implementação modifica os hashes registrados nas seções anteriores.

## 5. Continuidade e auditoria

- `docs/Documento_Mestre.md`: fonte funcional aprovada, sem mudanças decorrentes desta seleção.
- `.specs/wireframes/PROCESSO-PRANCHA.md`: SPEC 1, construção e Gates do template.
- `.specs/wireframes/REFERENCIA-TEMPLATE-OFICIAL.md`: SPEC 2, autoridade de consulta da referência selecionada.
- `.specs/wireframes/PROCESSO-TELA-PRANCHA.md`: SPEC 3, produção das Telas e Pranchas de Implementação.
- `docs/wireframes/images/README.md`: inventário e status operacional das interfaces; **não** decide qual versão está vigente.
- Este documento: **única fonte do evento histórico, identidade e vigência da versão selecionada**, com inventário de integridade da seção 2.

**Próxima atividade funcional:** elaborar e aprovar o Wireframe Text individual da primeira interface autorizada, conforme a SPEC 3. Isso não altera as decisões de 28/10/2026 e não aprova nenhuma interface automaticamente.
