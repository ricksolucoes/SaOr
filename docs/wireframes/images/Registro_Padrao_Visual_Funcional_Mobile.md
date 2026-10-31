# SaOr — Registro de seleção do padrão visual funcional Mobile

## 1. Finalidade e autoridades

**Registro genérico de vigência visual funcional**: identifica qual perfil de UI está autorizado a orientar novas Telas Mobile; sua seleção não altera o template da Prancha, cuja vigência é exclusivamente governada por `docs/wireframes/images/Registro_Controle_Template_Oficial.md` (SPEC 2). Não é uma quarta SPEC.

**Regra permanente de seleção:** versão nova só passa a `VIGENTE` após evidência completa dos Gates de sua formalização, validação técnica e decisão aplicável; nomes `v02`, datas inscritas em PNGs, aparências ou conversas não substituem o registro final. As versões anteriores não são sobrescritas. Não herdar componentes particulares de T00.

## 2. Estado da seleção durante GV2-02

- **Perfil candidato à formalização:** `docs/wireframes/images/padroes-funcionais/Mobile-v02.md`.
- **Origem concreta:** Telas T00 Mobile white/black `v02`, com variantes Desconectada (ver arquivos e hashes no perfil).
- **Situação:** `PENDENTE DE VIGÊNCIA — GV2-06 NÃO CONCLUÍDO`.
- **Decisão de adoção da V2:** declarada pelo responsável no contexto da nova versão; **a vigência documental somente será ativada quando GV2-06 tiver evidências e encerramento**.
- **Padrão anterior:** a documentação funcional aprovada de T00 `v01` permanece histórica. Não inventar uma data original de seleção anterior se o registro não a apresentar.
- **Template de Prancha vigente:** Modelo C white C_v02 e black C_v01, **selecionado em registro independente**. Seu contrato concreto de utilização funcional está em `docs/wireframes/images/contratos/USO-TEMPLATE-C.md` (vinculado pelos seis hashes oficiais, não pelo número v02 do padrão visual funcional).

## 3. Evento de ativação — preencher em GV2-06, não antes

| Campo | Valor |
|---|---|
| Perfil escolhido | PENDENTE |
| Caminho de perfil e hash | PENDENTE |
| Referências white/black e hashes | PENDENTE (ver perfil candidato) |
| Decisão formal e alcance | PENDENTE DE REGISTRO NO GV2-06 |
| Evidência de GI-1/2/3/4 de T00 v02 | PENDENTE |
| Data de ativação | NÃO DEFINIDA |
| Versão histórica substituída | A REGISTRAR SEM SOBRESCRITA |

## 4. Como usar após formalização

A interface nova consulta primeiro a fonte funcional e a SPEC 3; localiza neste registro o perfil **efetivamente vigente**; confere caminho, SHA-256, tema e versionamento; abre o perfil e seus PNGs de referência; aplica somente padrões compatíveis com os requisitos próprios da interface. Se o registro não declarar um perfil vigente com hashes e decisão, o Gate GI-0 registra bloqueio para uso do novo perfil. A produção do MVP atual permanece exclusivamente Mobile, White e Black.


---

## 5. Evento posterior de vigência — GV2-06 (registro de 30/10/2026)

**Estado atual:** `VIGENTE — Mobile v02`, temas White e Black. Esta decisão posterior substitui exclusivamente o estado provisório da seção 2 e os campos `PENDENTE` da seção 3, preservados como histórico do GV2-02.

| Identificação | Referência aprovada |
|---|---|
| Perfil vigente | `docs/wireframes/images/padroes-funcionais/Mobile-v02.md` |
| SHA-256 do perfil | `88c9258e53c7a4416403b6f60f792d923b2234bd78e1fdb52b40a505f0781dea` |
| Tela funcional white v02 | `docs/wireframes/images/white/telas/design/01_Mobile_360x800/T00-01-01_v02.png` — SHA-256 `0442412875e3c45b85038d75d8b628f16c94c4ba06529d1c0c97a32d47761504` |
| Tela funcional black v02 | `docs/wireframes/images/black/telas/design/01_Mobile_360x800/T00-01-01_v02.png` — SHA-256 `0d4baf7b7d4e12a59db8646dc6317976a860b573abd14745def152ea64b34950` |
| Estados alternativos | White `0e4a2da069611f52064c9a3e60f27536ebef21fd787ee9829a70d635de750e90`; Black `d9d70702af9473bad1688faae215ca14fdd5e294c076e32a3c4526e3d33dbe77` — nomes com `_estado-` |
| Prancha funcional white v02 | `docs/wireframes/images/white/telas/pranchas/01_Mobile_360x800/T00-01-01_v02.png` — SHA-256 `310bbac69366d6f57279ca30f2858d0489ca17e370120819b0594c18c06a9fae` |
| Prancha funcional black v02 | `docs/wireframes/images/black/telas/pranchas/01_Mobile_360x800/T00-01-01_v02.png` — SHA-256 `564cddc9a492810298be96c811487e702ab8273ee1a6bfe8d153db6741354efd` |
| Evidência da decisão | Responsável declarou a V2 como nova referência visual aprovada. Aceitou expressamente o GI-2 dos dois TextFrames pelos hashes; GI-3 validado fisicamente; aprovação visual das Pranchas V2 anteriormente declarada, transcrita nos registros de composição, §7 |
| Data desta formalização | 30/10/2026 (não constitui comprovação da data original de aprovação das imagens) |
| Histórico substituído | A V1 de T00 permanece **aprovada historicamente**, sem sobrescrita e sem vigência para novas produções |
| Template oficial vigente | Modelo C White C_v02 / Black C_v01, sob autoridade independente da SPEC 2 e seu registro permanente |

**Evidências de passagem GV2-06:** controles `white/black/telas/controle/T00-01-01_v02.md` §§6–8; TextFrames V2 aprovados por SHA-256 `e590ef912f00902aad3beb1bd6885c26631528088c5a97dc3f5b81e2553a0cb0` e `9d550bf5cf2ee73fff2f495d20997d644f95f14c2e1cc22beb23c2f41b1d5dc9`; registros de composição `white/black/telas/pranchas/01_Mobile_360x800/wiframetext/T00-01-01_v02.md` §§6–7; registro sequencial GV2-04/05/06.

**Limite da vigência:** o perfil V2 fornece padrões técnicos reutilizáveis **somente quando aplicáveis**. Não herdar de T00 seus textos, componentes, estados, destinos ou exceções. Outra versão só poderá substituir a V2 com decisão e rastreabilidade próprias. Não se altera o template oficial congelado nem a baseline funcional.
