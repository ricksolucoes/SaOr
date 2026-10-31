# SaOr — Perfil técnico do padrão visual funcional Mobile v02 (T00 como referência)

## 1. Fronteira e estado

**Natureza:** perfil **concreto**, derivado das Telas Mobile de T00 v02 fornecidas para os temas white e black. **Não é SPEC 1, 2 ou 3; não é novo template de prancha.**

**Situação vigente após GV2-06:** `PERFIL VISUAL FUNCIONAL MOBILE v02 — VIGENTE`, por ato formal de seleção em `docs/wireframes/images/Registro_Padrao_Visual_Funcional_Mobile.md`, seção 5. A presente descrição técnica não seleciona uma versão por conta própria; seus PNGs, suas características e seu alcance permanecem os mesmos. Os GI-1/GI-2/GI-3/GI-4 de T00 V2 estão comprovados nos controles e registros específicos.

**Imagens que limitam o alcance de suas observações:**

| Tema | Tela v02 principal | SHA-256 | Estado alternativo | SHA-256 |
|---|---|---|---|---|
| white | `docs/wireframes/images/white/telas/design/01_Mobile_360x800/T00-01-01_v02.png` | `0442412875e3c45b85038d75d8b628f16c94c4ba06529d1c0c97a32d47761504` | `T00-01-01_v02_estado-desconectada.png` no mesmo diretório | `0e4a2da069611f52064c9a3e60f27536ebef21fd787ee9829a70d635de750e90` |
| black | `docs/wireframes/images/black/telas/design/01_Mobile_360x800/T00-01-01_v02.png` | `0d4baf7b7d4e12a59db8646dc6317976a860b573abd14745def152ea64b34950` | `T00-01-01_v02_estado-desconectada.png` no mesmo diretório | `d9d70702af9473bad1688faae215ca14fdd5e294c076e32a3c4526e3d33dbe77` |

Ambas as Telas são `360 × 800 px`. A compatibilidade com `.specs/wireframes/REGRAS-TECNICAS.md` é uma obrigação, não uma autorização para inferir o design de qualquer interface futura a partir da presença de um exemplo.

## 2. Elementos reutilizáveis — somente quando aplicáveis

| Propriedade verificável | Referência concreta e limite de reutilização |
|---|---|
| Estrutura Mobile | ViewPort 360×800, AppBar superior, margens laterais de 12 px e largura útil 336 px **quando aplicável**, conforme REGRAS-TECNICAS §§3–4 |
| Tipografia técnica | Família Inter e tokens WF-TITLE, WF-SECTION, WF-BODY, WF-LABEL, WF-ACTION-TEXT e WF-CAPTION, conforme §5; a identidade tipográfica da marca é independente |
| Superfícies | Cartões e fundo utilizam separação tonal por tema, conforme tabelas 6.5/6.6 e observação física dos PNGs V2; não importar contornos ou sombras da V1 por hábito |
| Agrupamentos | Seções de conteúdo e cartões são separados por ritmo vertical; o número de seções, seus textos e a ordem dos cartões pertencem à Tela individual |
| Itens de ação | Quando o requisito exigir navegação, usar estrutura de item com título, possível ícone e indicador direcional **se efetivamente documentado**; subtítulo só quando o requisito individual o determinar |
| Estados | Variantes de um componente mantêm a geometria das partes invariáveis da Tela; ícone e texto devem explicitar o estado, com cor semântica aplicável do tema |
| Ação destrutiva | Um destaque vermelho contextual somente é aplicado a uma ação comprovadamente destrutiva, com destino/fluxo documentado; não transforma todas as ações em vermelhas |
| Iconografia | Família técnica prevista em REGRAS-TECNICAS §9. **Os identificadores específicos de cada ícone pertencem ao TextFrame da interface**, e não são transferidos automaticamente desta amostra |
| Valores cromáticos | Nunca inventar HEX: obter os tokens canônicos de REGRAS-TECNICAS §§6.5/6.6 e conferir as cores visíveis do PNG em cada versão de Tela |

Este documento registra a **linguagem visual funcional selecionada**; a equivalência entre um valor rasterizado e uma propriedade editável de origem (por exemplo, família exata de glyph, sombra e raio antialias) não é afirmada quando não for tecnicamente demonstrável. Um novo componente sem padrão suficiente bloqueia o Gate correspondente até definição própria, em vez de receber parâmetros inventados.

## 3. Conteúdos exclusivos de T00 — proibida herança automática

Não são padrões universais nem requisitos de outras interfaces:

- `Configurações`, `CONEXÃO`, `APARÊNCIA`, `SISTEMA`, `API de acesso`, `Tema`, `Diagnóstico`, `Restaurar configuração`, `Versão 1.0.0`.
- Valor `Claro` no white e `Escuro` no black; `Verificar integridade do app`; localização inferior do texto de versão.
- Número e ordem dos cartões, ícones de conexão/rede/tema/diagnóstico/restauração, estados Conectada/Desconectada e destinos T00.1, T00.2, T00.3, M00.5.
- A exceção visual de T00 v01 (ocultar `Claro / Escuro`) é histórica; a V2 contém informação contextual de tema e deve ter decisão/versionamento próprios.

## 4. Aplicação futura, sem substituir os requisitos

Para uma nova interface: (1) abrir sua ficha no Documento Mestre; (2) consultar a seleção vigente no registro genérico; (3) abrir este perfil **somente se efetivamente selecionado** e conferir seus hashes; (4) listar os padrões aplicáveis; (5) definir componentes/estados individuais apenas pelas fontes funcionais e pela aprovação de sua Tela; (6) registrar por que algo da referência foi ou não usado; (7) executar GI-0 a GI-4 da SPEC 3.

Para `T00.1`, por exemplo, URL, credenciais condicionais, testes de conexão e estados de erro devem vir de sua própria ficha. Este perfil não transfere para ela os cartões, textos ou destinos de T00. A simples existência de PNGs de T00.1 no repositório **não representa aprovação GI-0/GI-1 nem liberação da produção pela GV2-08**.

## 5. Preservação e revisões

A V1 permanece histórica. A V2 passou a `VIGENTE` mediante o registro de seleção GV2-06 em `Registro_Padrao_Visual_Funcional_Mobile.md`, sem alterar o Modelo C. Mudança futura de perfil exigirá nova identidade, versão, evidências e histórico; as SPECs permanentes e os templates oficiais não são reescritos para refletir cada mudança visual.
