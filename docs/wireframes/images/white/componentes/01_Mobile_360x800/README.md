# SaOr — Componentes reutilizáveis — white — Mobile 360×800

Controle da versão vigente (com hash) e do histórico de versões das imagens de componentes reutilizáveis do tema **white**. Escrito para o responsável humano, para o assistente de IA que gera ou usa as imagens e para qualquer LLM ou auditor que verifique o estado sem acesso a conversas. **Em caso de conflito com uma lembrança de conversa, vale este README.**

| Campo | Valor |
| --- | --- |
| Tema / resolução | white / Mobile 360 × 800 (única no escopo vigente do MVP) |
| Pasta | `docs/wireframes/images/white/componentes/01_Mobile_360x800/` |
| Catálogo de origem | `docs/Documento_Mestre.md`, seção 20 (C01–C44) |
| Tema equivalente | `../../../black/componentes/01_Mobile_360x800/` (mesmos IDs, versões equivalentes, mesmas caixas; só variam os tokens cromáticos) |
| Última atualização | 15/11/2026 |

---

## 1. Regras

1. Documentação em português do Brasil.
2. **Só existe o que está na seção 3.** Componente fora dela não tem imagem oficial: não presumir, não desenhar de memória, não inventar. Tela nova consulta esta pasta antes de desenhar e reutiliza a versão vigente; se faltar componente, registra a lacuna.
3. Componente sem tela aprovada que o defina fica como `Montar` e aguarda: não se cria por padrão visual.
4. **Toda versão criada é registrada** no histórico (seção 5), vigente ou não.
5. **Nunca sobrescrever** uma versão. Mudança gera `v02`, `v03`… e entra no histórico (seção 5).
6. **O hash é a identidade.** Conferir o SHA-256 (seção 4) antes de usar; hash diferente = arquivo não confiável.
7. **Aprovação não é presumida:** só vale `APROVADO` com data e hora registradas pelo responsável.
8. O que não puder ser medido ou comprovado fica `NÃO VALIDADO`; nunca afirmar.
9. Não herdar componentes particulares de T00 para outras telas sem decisão e registro próprios (`Registro_Padrao_Visual_Funcional_Mobile`). Estados genéricos (Default, Focus, Pressed, Disabled, Error) seguem a Prancha da T02, Item 11, e só viram imagem com tela aprovada que os mostre.
10. Quem gera os arquivos os entrega ao responsável; commit e publicação são decisão dele.

---

## 2. Convenção de nome

```text
COMP-[ID]-[NomeDoComponente]-[versão].png
```

- `[ID]`: ID do catálogo (`C01`…`C44`). **Variante:** `Cnn.m`, fora da numeração do catálogo (exemplo `C01.1`).
- `[NomeDoComponente]`: nome em PascalCase, sem espaços nem acentos.
- `[versão]`: `v` + 2 dígitos, como nas demais imagens do repositório.
- **Estado:** sufixo no final do nome, depois da versão, com `_` e o estado em PascalCase sem acentos, por exemplo `COMP-C13-Switch-v01_Ligado.png`. O arquivo sem sufixo é o estado base. Decisão do responsável (15/11/2026, 18:53). A regra anterior (sufixo antes da versão) fica substituída.
- Formato: PNG RGBA, tamanho exato do componente, escala 1:1, sem redimensionar. Nos botões (C03 a C05), no C06 e do C12 em diante, o fundo fora do componente é **transparente**, para a imagem funcionar sobre qualquer página.

---

## 3. Versão vigente (a ser utilizada)

| ID | Componente | Arquivo | Versão | Dimensões (px) | Aprovação do responsável |
| --- | --- | --- | --- | --- | --- |
| C01 | AppHeader | `COMP-C01-AppHeader-v01.png` | v01 | 360 × 56 | APROVADO (15/11/2026, 10:33) |
| C01.1 | AppHeaderBack (variante do C01) | `COMP-C01.1-AppHeaderBack-v01.png` | v01 | 360 × 57 | APROVADO (15/11/2026, 10:48) |
| C02 | BottomNavigation | `COMP-C02-BottomNavigation-v01.png` | v01 | 360 × 64 | APROVADO (15/11/2026, 10:33) |
| C03 | PrimaryButton | `COMP-C03-PrimaryButton-v01.png` | v01 | 336 × 56 | APROVADO (15/11/2026, 11:34) |
| C04 | SecondaryButton | `COMP-C04-SecondaryButton-v01.png` | v01 | 336 × 56 | APROVADO (15/11/2026, 11:34) |
| C05 | TextButton | `COMP-C05-TextButton-v01.png` | v01 | 124 × 56 | APROVADO (15/11/2026, 11:34) |
| C06 | TextInput | `COMP-C06-TextInput-v01.png` | v01 | 336 × 106 | APROVADO (15/11/2026, 11:34) |
| C06.1 | TextInputShort (variante do C06) | `COMP-C06.1-TextInputShort-v01.png` | v01 | 168 × 106 | APROVADO (15/11/2026, 20:16) |
| C06.2 | TextInputWithButton (variante do C06) | `COMP-C06.2-TextInputWithButton-v01.png` | v01 | 336 × 106 | APROVADO (15/11/2026, 20:16) |
| C07 | SearchInput | `COMP-C07-SearchInput-v01.png` | v01 | 336 × 56 | APROVADO (15/11/2026, 15:32) |
| C08 | SelectInput | `COMP-C08-SelectInput-v01.png` | v01 | 336 × 106 | APROVADO (15/11/2026, 15:32) |
| C09 | DateInput | `COMP-C09-DateInput-v01.png` | v01 | 336 × 106 | APROVADO (15/11/2026, 15:32) |
| C09.1 | DatePickerCalendar (variante do C09) | `COMP-C09.1-DatePickerCalendar-v01.png` | v01 | 336 × 464 | APROVADO (15/11/2026, 15:32) |
| C10 | TimeInput | `COMP-C10-TimeInput-v01.png` | v01 | 336 × 106 | APROVADO (15/11/2026, 15:32) |
| C11 | TextArea | `COMP-C11-TextArea-v01.png` | v01 | 336 × 170 | APROVADO (15/11/2026, 15:32) |
| C12 | Checkbox | `COMP-C12-Checkbox-v01.png` | v01 | 336 × 48 | APROVADO (15/11/2026, 12:08) |
| C13 | Switch | `COMP-C13-Switch-v01.png` | v01 | 336 × 56 | APROVADO (15/11/2026, 18:59) |
| C13 | Switch (estado) | `COMP-C13-Switch-v01_Ligado.png` | v01 | 336 × 56 | APROVADO (15/11/2026, 18:59) |
| C14 | StatusBadge | `COMP-C14-StatusBadge-v01.png` | v01 | 63 × 20 | APROVADO (15/11/2026, 14:23) |
| C15 | MetricCard | `COMP-C15-MetricCard-v01.png` | v01 | 164 × 88 | APROVADO (15/11/2026, 12:08) |
| C15.1 | MetricCardSubcaption (variante do C15) | `COMP-C15.1-MetricCardSubcaption-v01.png` | v01 | 164 × 88 | APROVADO (15/11/2026, 12:08) |
| C16 | ClientCard | `COMP-C16-ClientCard-v01.png` | v01 | 336 × 152 | APROVADO (15/11/2026, 19:29) |
| C16.1 | ClientCardSelectable (variante do C16) | `COMP-C16.1-ClientCardSelectable-v01.png` | v01 | 336 × 152 | APROVADO (15/11/2026, 19:29) |
| C16.1 | ClientCardSelectable (estado) | `COMP-C16.1-ClientCardSelectable-v01_Selecionado.png` | v01 | 336 × 152 | APROVADO (15/11/2026, 19:29) |
| C16.2 | ClientCardDisabled (variante do C16) | `COMP-C16.2-ClientCardDisabled-v01.png` | v01 | 336 × 152 | APROVADO (15/11/2026, 19:29) |
| C17 | ProspectCard | `COMP-C17-ProspectCard-v01.png` | v01 | 336 × 152 | APROVADO (15/11/2026, 19:39) |
| C17.1 | ProspectCardSelectable (variante do C17) | `COMP-C17.1-ProspectCardSelectable-v01.png` | v01 | 336 × 152 | APROVADO (15/11/2026, 19:39) |
| C17.1 | ProspectCardSelectable (estado) | `COMP-C17.1-ProspectCardSelectable-v01_Selecionado.png` | v01 | 336 × 152 | APROVADO (15/11/2026, 19:39) |
| C17.2 | ProspectCardDisabled (variante do C17) | `COMP-C17.2-ProspectCardDisabled-v01.png` | v01 | 336 × 152 | APROVADO (15/11/2026, 19:39) |
| C18 | ProductCard | `COMP-C18-ProductCard-v01.png` | v01 | 336 × 110 | APROVADO (15/11/2026, 19:46) |
| C18.1 | ProductCardUnavailable (variante do C18) | `COMP-C18.1-ProductCardUnavailable-v01.png` | v01 | 336 × 110 | APROVADO (15/11/2026, 19:46) |
| C18.2 | ProductOrderItem (variante do C18) | `COMP-C18.2-ProductOrderItem-v01.png` | v01 | 336 × 150 | APROVADO (15/11/2026, 19:51) |
| C18.3 | ProductOrderItemNoSku (variante do C18) | `COMP-C18.3-ProductOrderItemNoSku-v01.png` | v01 | 336 × 126 | APROVADO (15/11/2026, 19:51) |
| C19 | OrderCard | `COMP-C19-OrderCard-v01.png` | v01 | 336 × 64 | APROVADO (15/11/2026, 14:36) |
| C19.1 | OrderCardByClient (variante do C19) | `COMP-C19.1-OrderCardByClient-v01.png` | v01 | 336 × 110 | APROVADO (15/11/2026, 20:48) |
| C19.2 | OrderCardByCustomer (variante do C19) | `COMP-C19.2-OrderCardByCustomer-v01.png` | v01 | 336 × 110 | APROVADO (15/11/2026, 20:48) |
| C20 | VisitCard | `COMP-C20-VisitCard-v01.png` | v01 | 336 × 64 | APROVADO (15/11/2026, 14:36) |
| C20.1 | VisitHistoryItem (variante do C20) | `COMP-C20.1-VisitHistoryItem-v01.png` | v01 | 336 × 88 | APROVADO (15/11/2026, 20:48) |
| C21 | QuantitySelector | `COMP-C21-QuantitySelector-v01.png` | v01 | 336 × 48 | APROVADO (15/11/2026, 18:59) |
| C21 | QuantitySelector (estado) | `COMP-C21-QuantitySelector-v01_Minimo.png` | v01 | 336 × 48 | APROVADO (15/11/2026, 18:59) |
| C22 | FilterChip | `COMP-C22-FilterChip-v01.png` | v01 | 58 × 32 | APROVADO (15/11/2026, 18:59) |
| C22 | FilterChip (estado) | `COMP-C22-FilterChip-v01_Selecionado.png` | v01 | 80 × 32 | APROVADO (15/11/2026, 18:59) |
| C23 | Stepper | `COMP-C23-Stepper-v01.png` | v01 | 336 × 56 | APROVADO (15/11/2026, 18:59) |
| C23 | Stepper (estado) | `COMP-C23-Stepper-v01_Etapa1.png` | v01 | 336 × 56 | APROVADO (15/11/2026, 18:59) |
| C23 | Stepper (estado) | `COMP-C23-Stepper-v01_Etapa4.png` | v01 | 336 × 56 | APROVADO (15/11/2026, 18:59) |
| C24 | StatusTimeline | `COMP-C24-StatusTimeline-v01.png` | v01 | 336 × 184 | APROVADO (15/11/2026, 19:10) |
| C24 | StatusTimeline (estado) | `COMP-C24-StatusTimeline-v01_Etapa1.png` | v01 | 336 × 184 | APROVADO (15/11/2026, 19:10) |
| C24 | StatusTimeline (estado) | `COMP-C24-StatusTimeline-v01_Etapa5.png` | v01 | 336 × 184 | APROVADO (15/11/2026, 19:10) |
| C25 | Dialog | `COMP-C25-Dialog-v01.png` | v01 | 312 × 308 | APROVADO (15/11/2026, 12:08) |
| C26 | BottomSheet | `COMP-C26-BottomSheet-v01.png` | v01 | 360 × 280 | APROVADO (15/11/2026, 19:10) |
| C27 | EmptyState | `COMP-C27-EmptyState-v01.png` | v01 | 336 × 64 | APROVADO (15/11/2026, 14:10) |
| C28 | ErrorState | `COMP-C28-ErrorState-v01.png` | v01 | 336 × 188 | APROVADO (15/11/2026, 14:10) |
| C29 | LoadingState | `COMP-C29-LoadingState-v01.png` | v01 | 336 × 128 | APROVADO (15/11/2026, 14:10) |
| C29.1 | LoadingStateCard (variante do C29) | `COMP-C29.1-LoadingStateCard-v01.png` | v01 | 164 × 88 | APROVADO (15/11/2026, 14:10) |
| C30 | SyncStatus | `COMP-C30-SyncStatus-v01.png` | v01 | 336 × 67 | APROVADO (15/11/2026, 12:08) |
| C30.1 | SyncStatusDetail (variante do C30) | `COMP-C30.1-SyncStatusDetail-v01.png` | v01 | 336 × 67 | APROVADO (15/11/2026, 12:08) |
| C31 | MoneyDisplay | `COMP-C31-MoneyDisplay-v01.png` | v01 | 76 × 24 | APROVADO (15/11/2026, 14:36) |
| C31.1 | MoneyDisplayInline (variante do C31) | `COMP-C31.1-MoneyDisplayInline-v01.png` | v01 | 52 × 20 | APROVADO (15/11/2026, 14:36) |
| C32 | SectionHeader | `COMP-C32-SectionHeader-v01.png` | v01 | 336 × 30 | APROVADO (15/11/2026, 12:08) |
| C32.1 | SectionHeaderIcon (variante do C32) | `COMP-C32.1-SectionHeaderIcon-v01.png` | v01 | 336 × 30 | APROVADO (15/11/2026, 12:08) |
| C33 | AddressCard | `COMP-C33-AddressCard-v01.png` | v01 | 336 × 130 | APROVADO (15/11/2026, 20:16) |
| C33 | AddressCard (estado) | `COMP-C33-AddressCard-v01_Selecionado.png` | v01 | 336 × 130 | APROVADO (15/11/2026, 20:16) |
| C33.1 | AddressCardSummary (variante do C33) | `COMP-C33.1-AddressCardSummary-v01.png` | v01 | 336 × 92 | APROVADO (15/11/2026, 20:16) |
| C33.2 | AddressCardDetail (variante do C33) | `COMP-C33.2-AddressCardDetail-v01.png` | v01 | 336 × 232 | APROVADO (15/11/2026, 20:16) |
| C33.3 | AddressMap (variante do C33) | `COMP-C33.3-AddressMap-v01.png` | v01 | 336 × 200 | APROVADO (15/11/2026, 20:16) |
| C34 | ContactCard | `COMP-C34-ContactCard-v01.png` | v01 | 336 × 112 | PENDENTE |
| C34.1 | ContactCardDetail (variante do C34) | `COMP-C34.1-ContactCardDetail-v01.png` | v01 | 336 × 176 | PENDENTE |
| C34.2 | ProfileHeader (variante do C34) | `COMP-C34.2-ProfileHeader-v01.png` | v01 | 336 × 136 | PENDENTE |
| C35 | ThemeSelector | `COMP-C35-ThemeSelector-v01.png` | v01 | 336 × 56 | APROVADO (15/11/2026, 13:41) |
| C36 | ThemePreview | `COMP-C36-ThemePreview-v01.png` | v01 | 336 × 290 | APROVADO (15/11/2026, 13:41) |
| C37 | ConnectionStatus | `COMP-C37-ConnectionStatus-v01.png` | v01 | 336 × 56 | APROVADO (15/11/2026, 13:41) |
| C38 | ApiConfigurationForm | `COMP-C38-ApiConfigurationForm-v01.png` | v01 | 336 × 464 | APROVADO (15/11/2026, 13:41) |
| C39 | SecretInput | `COMP-C39-SecretInput-v01.png` | v01 | 336 × 106 | APROVADO (15/11/2026, 13:41) |
| C40 | ConnectionTest | `COMP-C40-ConnectionTest-v01.png` | v01 | 336 × 56 | APROVADO (15/11/2026, 14:18) |
| C41 | DiagnosticsItem | `COMP-C41-DiagnosticsItem-v01.png` | v01 | 336 × 72 | APROVADO (15/11/2026, 13:41) |
| C42 | SettingsGroup | `COMP-C42-SettingsGroup-v01.png` | v01 | 336 × 104 | APROVADO (15/11/2026, 13:41) |
| C43 | SettingsItem | `COMP-C43-SettingsItem-v01.png` | v01 | 336 × 72 | APROVADO (15/11/2026, 13:41) |
| C43.1 | SettingsItemBadge (variante do C43) | `COMP-C43.1-SettingsItemBadge-v01.png` | v01 | 336 × 80 | APROVADO (15/11/2026, 13:41) |
| C43.2 | SettingsItemDestructive (variante do C43) | `COMP-C43.2-SettingsItemDestructive-v01.png` | v01 | 336 × 56 | APROVADO (15/11/2026, 13:41) |
| C44 | ConnectionBadge | `COMP-C44-ConnectionBadge-v01.png` | v01 | 77 × 24 | APROVADO (15/11/2026, 13:41) |

### 3.1. Especificação

**C01 — AppHeader**

| Item | Valor |
| --- | --- |
| Conteúdo | logo SaOr horizontal; ícones de notificações e de conta |
| Dimensões | 360 × 56 px; alvo de toque mínimo 48 × 48 |
| Uso | telas com usuário logado |

**C01.1 — AppHeaderBack (variante do C01)**

O sistema tem **duas AppBars**: C01 e C01.1.

| Item | Valor |
| --- | --- |
| Conteúdo | `chevron_left` e título; divisor de 1 px na base. "Título da tela" é **placeholder**: cada tela coloca o seu título. |
| Dimensões | 360 × 57 px (faixa de 56 + divisor de 1 px); título em Inter SemiBold 20 px |
| Uso | telas **sem usuário logado** e qualquer tela, mesmo logada, que precise de retorno |

**C02 — BottomNavigation**

| Item | Valor |
| --- | --- |
| Conteúdo | 5 itens: Início, Clientes, botão central `+`, Pedidos, Mais |
| Dimensões | 360 × 64 px; botão central 48 × 48 |
| Item ativo | **muda conforme a tela selecionada** (Início, Clientes, Pedidos ou Mais). A v01 mostra só "Início ativo"; os demais estados serão acrescentados como arquivos próprios. |

**C03 — PrimaryButton**

| Item | Valor |
| --- | --- |
| Conteúdo | rótulo em caixa alta ("RÓTULO" é **placeholder**) sobre fundo Primary |
| Dimensões | 336 × 56 px (largura útil), raio 12 px |
| Uso | ação principal |
| Estados | a v01 mostra só o estado padrão; carregando, desabilitado e variante de erro serão arquivos próprios |

**C04 — SecondaryButton**

| Item | Valor |
| --- | --- |
| Conteúdo | rótulo em caixa alta na cor Primary ("RÓTULO" é **placeholder**), contorno de 1 px, sem preenchimento; ícone opcional à esquerda do rótulo (não incluído na imagem genérica) |
| Dimensões | 336 × 56 px (largura útil), raio 12 px |
| Uso | ação secundária |

**C05 — TextButton**

| Item | Valor |
| --- | --- |
| Conteúdo | rótulo em caixa alta na cor Primary ("RÓTULO" é **placeholder**), sem contorno nem preenchimento |
| Dimensões | 124 × 56 px de referência; a largura acompanha o rótulo, com alvo de toque mínimo de 48 × 48 |
| Uso | ação de menor destaque |

**C06 — TextInput**

| Item | Valor |
| --- | --- |
| Conteúdo | rótulo acima, campo e texto de apoio abaixo. "Rótulo", "Texto de exemplo" e "Texto de apoio." são **placeholders** |
| Dimensões | 336 × 106 px; campo 336 × 56, raio 12 px, borda de 1 px |
| Estados | a v01 mostra só o estado padrão; foco, erro e bloqueado serão arquivos próprios |

**C06.1 — TextInputShort (variante do C06)**

| Item | Valor |
| --- | --- |
| Conteúdo | o mesmo conteúdo do C06 (rótulo, campo e texto de apoio) com o campo de largura parcial ("Rótulo", "Texto de exemplo" e "Texto de apoio." são **placeholders**) |
| Dimensões | 168 × 106 px; campo 168 × 56, raio 12 px, borda de 1 px; derivado do arquivo aprovado do C06, sem redesenhar os textos |
| Uso | campo curto, como o Número da T05.1 (L2276–2278) |
| Não validado | largura de 168 px (o textframe só mostra `[__________]`); estados iguais aos do C06 (só o padrão) |

**C06.2 — TextInputWithButton (variante do C06)**

| Item | Valor |
| --- | --- |
| Conteúdo | rótulo acima; na mesma linha, o campo do C06 (224 px) e o botão `BUSCAR` (104 × 56 px, raio 12, contorno de 1 px em BORDER-CONTROL, rótulo em caixa alta Inter Medium 15 px, espaçamento 0,6, na cor Primary, mesmo estilo do C04); texto de apoio abaixo ("Rótulo", "Texto de exemplo" e "Texto de apoio." são **placeholders**) |
| Dimensões | 336 × 106 px; campo 224 × 56 com intervalo de 8 px até o botão; o botão alinha com o campo |
| Uso | campo CEP com `BUSCAR` na T05.1 (L2270–2271) |
| Não validado | larguras de 224 e 104 px e o intervalo de 8 px (o textframe só mostra `[___________] [ BUSCAR ]`); botão no estilo do C04; estados iguais aos do C06 (só o padrão) |

**C07 — SearchInput**

| Item | Valor |
| --- | --- |
| Conteúdo | campo com ícone `search` de 24 px à esquerda e texto de dica em Inter Regular 16 px, TEXT-2, sem rótulo e sem texto de apoio ("Buscar" é **placeholder**) |
| Dimensões | 336 × 56 px, raio 12 px, borda de 1 px em BORDER-CONTROL `#868686`, fundo SURFACE; ícone a 16 px da borda e texto a 52 px |
| Estados | a v01 mostra o campo vazio; com texto aparece o botão de limpar (`close`); foco, erro e bloqueado serão arquivos próprios |
| Não validado | cor TEXT-2 da dica e ícone em ACTION `#333333`; decisão do responsável |

**C08 — SelectInput**

| Item | Valor |
| --- | --- |
| Conteúdo | rótulo acima, campo com o valor selecionado e `arrow_drop_down` de 24 px à direita, e texto de apoio abaixo ("Rótulo", "Opção selecionada" e "Texto de apoio." são **placeholders**) |
| Dimensões | 336 × 106 px; campo 336 × 56, raio 12 px, borda de 1 px, ícone a 16 px da borda direita |
| Estados | a v01 mostra o estado fechado; o menu de opções aberto, foco, erro e bloqueado serão arquivos próprios |

**C09 — DateInput**

| Item | Valor |
| --- | --- |
| Conteúdo | rótulo acima, campo com a máscara de data em TEXT-2 e `calendar_today` de 24 px à direita, e texto de apoio abaixo ("Rótulo", "DD/MM/AAAA" e "Texto de apoio." são **placeholders**) |
| Dimensões | 336 × 106 px; campo 336 × 56, raio 12 px, borda de 1 px |
| Estados | a v01 mostra o campo vazio; com valor, foco, erro e bloqueado serão arquivos próprios. O ícone abre o calendário (C09.1) |
| Não validado | formato DD/MM/AAAA; o Documento Mestre não define o formato de data; decisão do responsável |

**C09.1 — DatePickerCalendar (variante do C09)**

| Item | Valor |
| --- | --- |
| Conteúdo | painel de seleção de data: cabeçalho com "Selecionar data" (Inter Regular 12, TEXT-2) e a data escolhida (Inter Regular 24, TEXT); divisor de 1 px em BORDER `#B5B5B5`; mês e ano em Inter Medium 14 com `arrow_drop_down`, e `chevron_left` e `chevron_right`; dias da semana D S T Q Q S S (Inter Medium 12, TEXT-2); grade de 7 colunas por 48 px; ações CANCELAR e CONFIRMAR em Primary (estilo do C05). Textos, mês e datas são **placeholders** |
| Dimensões | 336 × 464 px, raio 16 px, fundo SURFACE; células de 48 × 48 px, que atendem o toque mínimo |
| Estados da célula | dia selecionado: círculo de 40 px preenchido em Primary `#004A99`, texto ON Primary `#FFFFFF`; dia atual: círculo de 40 px com contorno de 1 px em Primary e texto Primary; demais dias em TEXT; dias fora do mês ficam vazios |
| Não validado | largura de 336 px, em vez dos 312 px de modal da regra 7 de `REGRAS-TECNICAS.md` (7 colunas de 48 px exigem 336 px); catálogo sem item de seletor de data e variante sem tela aprovada de origem; ausência do ícone de alternar para teclado; textos "Selecionar data", "CANCELAR" e "CONFIRMAR". Decisão do responsável |
| Estados futuros | dias desabilitados, seletor de ano aberto e versão White serão arquivos próprios |

**C10 — TimeInput**

| Item | Valor |
| --- | --- |
| Conteúdo | rótulo acima, campo com a máscara de hora em TEXT-2 e `schedule` de 24 px à direita, e texto de apoio abaixo ("Rótulo", "HH:MM" e "Texto de apoio." são **placeholders**) |
| Dimensões | 336 × 106 px; campo 336 × 56, raio 12 px, borda de 1 px |
| Estados | a v01 mostra o campo vazio; com valor, foco, erro e bloqueado serão arquivos próprios |
| Não validado | formato de 24 horas (HH:MM); o Documento Mestre não define o formato de hora; decisão do responsável |

**C11 — TextArea**

| Item | Valor |
| --- | --- |
| Conteúdo | rótulo acima, campo de várias linhas com o texto no topo, texto de apoio à esquerda e contador de caracteres à direita ("Rótulo", "Texto de exemplo", "Texto de apoio." e "0/500" são **placeholders**) |
| Dimensões | 336 × 170 px; campo 336 × 120 (cerca de 4 linhas), raio 12 px, borda de 1 px |
| Estados | a v01 mostra o campo vazio; foco, erro e bloqueado serão arquivos próprios |
| Não validado | altura de 120 px e limite de 500 caracteres do contador; decisão do responsável |

**C12 — Checkbox**

| Item | Valor |
| --- | --- |
| Conteúdo | caixa de seleção de 24 px e rótulo ("Rótulo" é **placeholder**) |
| Dimensões | 336 × 48 px |
| Estados | a v01 mostra só o estado desmarcado; marcado e demais estados serão arquivos próprios |

**C13 — Switch**

| Item | Valor |
| --- | --- |
| Conteúdo | rótulo à esquerda e interruptor à direita ("Rótulo" é **placeholder**) |
| Dimensões | 336 × 56 px; trilho de 52 × 32 px (raio 16) alinhado à direita, a 12 px do topo |
| Estados | a v01 mostra o estado **desligado**: trilho SURFACE-ALT com borda de 2 px BORDER-CONTROL e polegar de 16 px BORDER-CONTROL. Estado **ligado** (`COMP-C13-Switch-v01_Ligado.png`): trilho Primary, polegar de 24 px ON Primary à direita. Desabilitado, foco e pressionado serão arquivos próprios |
| Referência | Material Design 3 (trilho 52 × 32, polegar 16/24 px, alvo de toque mínimo de 48 × 48; sem texto ON/OFF no interruptor) |
| Não validado | posição (rótulo à esquerda, interruptor à direita, como em listas de configuração); borda de 2 px; uso do Primary para o estado ligado |

**C14 — StatusBadge**

| Item | Valor |
| --- | --- |
| Conteúdo | ícone de estado de 16 px e texto de status em Inter Regular 14 px, na cor TEXT, lado a lado, com 4 px entre eles, sem contorno nem preenchimento próprios ("Status" e o ícone tracejado são **placeholders**) |
| Dimensões | 63 × 20 px; a largura acompanha o texto; fundo SURFACE-ALT, o fundo em que o selo aparece nas linhas de lista |
| Estados | o ícone, o texto e a cor mudam conforme o status do registro; a v01 usa cor neutra (ícone placeholder ACTION `#333333` e texto TEXT) e cada status será arquivo próprio |
| Diferença para o C44 | o C44 (ConnectionBadge) é um selo com contorno de 1 px para o estado da conexão; o C14 é o status de pedidos e registros, em linha com o texto da lista, sem contorno |

**C15 — MetricCard**

O MetricCard tem **duas versões**: sem sublegenda (C15) e com sublegenda (C15.1).

| Item | Valor |
| --- | --- |
| Conteúdo | valor em destaque e legenda ("Valor" e "Legenda" são **placeholders**) |
| Dimensões | 164 × 88 px, raio 16 px |

**C15.1 — MetricCardSubcaption (variante do C15)**

| Item | Valor |
| --- | --- |
| Conteúdo | valor em destaque, legenda e sublegenda ("Valor", "Legenda" e "Sublegenda" são **placeholders**) |
| Dimensões | 164 × 88 px, raio 16 px |

**C16 — ClientCard**

| Item | Valor |
| --- | --- |
| Conteúdo | título em Inter Medium 16 px (TEXT) com `chevron_right` à direita; abaixo, em Regular 14 px TEXT-2, o código e a cidade com UF; o selo de status (C14); e duas linhas de mensagem em Regular 14 px TEXT-2 ("Título", "#000000", "Cidade - UF", "Mensagem 1" e "Mensagem 2" são **placeholders**; o selo "Status" é o arquivo do C14) |
| Dimensões | 336 × 152 px, raio 16 px, fundo SURFACE-ALT; cartão avulso, que funciona isolado em qualquer janela; texto a 16 px da borda esquerda, linhas a cada 22 px |
| Uso | o cartão inteiro é a área de toque e abre o Cliente (T03 → T04). As mensagens são preenchidas por cada tela, por exemplo "Última compra: 10/10/2026" na T03. O selo muda de ícone, texto e cor conforme a situação (ver C14) |
| Referência | T03 do Doc. Mestre (nome, código, cidade, situação, última compra); Aetna e Glance (cartão inteiro tocável com indicador de ação); Material 3 (listas de duas e três linhas) |
| Variantes | `C16.1` (com seletor no lugar da seta) e `C16.2` (desabilitado, sem controle) |
| Não validado | altura de 152 px e passo de 22 px; chevron alinhado à linha do título; comportamento com texto mais longo que a linha (truncamento ou quebra); não há tela aprovada que defina o cartão |

**C16.1 — ClientCardSelectable (variante do C16)**

| Item | Valor |
| --- | --- |
| Conteúdo | o mesmo conteúdo do C16, com um seletor (botão de rádio de 24 px) no lugar da seta ("Mensagem 1" e "Mensagem 2" são **placeholders**) |
| Dimensões | 336 × 152 px, as mesmas do C16; seletor a 16 px da borda direita, alinhado à linha do título |
| Estados | a v01 mostra o seletor **vazio** (ícone `radio_button_unchecked` em BORDER-CONTROL); `COMP-C16.1-ClientCardSelectable-v01_Selecionado.png` mostra o seletor **marcado** (`radio_button_checked` em Primary) |
| Uso | seleção de um Cliente numa lista, como no seletor da M09.1; só um Cliente é marcado por vez |
| Não validado | escolha do botão de rádio (a M09.1 mostra só `( )`); posição do seletor na linha do título |

**C16.2 — ClientCardDisabled (variante do C16)**

| Item | Valor |
| --- | --- |
| Conteúdo | o mesmo conteúdo do C16, sem seta e sem seletor ("Mensagem 1" e "Mensagem 2" são **placeholders**) |
| Dimensões | 336 × 152 px, as mesmas do C16 |
| Uso | Cliente que não pode ser aberto nem selecionado; a mensagem explica o motivo (por exemplo, "Não pode emitir pedido" na M09.1), pois o texto e o ícone do selo devem informar além da cor |
| Não validado | interpretação de "desabilitado": o controle da direita é ocultado e o texto fica com a mesma cor; decisão do responsável |


**C17 — ProspectCard**

| Item | Valor |
| --- | --- |
| Conteúdo | título em Inter Medium 16 px (TEXT) com `chevron_right` à direita; abaixo, em Regular 14 px TEXT-2, a cidade com UF e o nome do contato; o selo de status (C14); e duas linhas de mensagem em Regular 14 px TEXT-2 ("Título", "Cidade - UF", "Contato", "Mensagem 1" e "Mensagem 2" são **placeholders**; o selo "Status" é o arquivo do C14) |
| Dimensões | 336 × 152 px, raio 16 px, fundo SURFACE-ALT; cartão avulso, que funciona isolado em qualquer janela; texto a 16 px da borda esquerda, linhas a cada 22 px; mesma estrutura do C16, sem o código `#` |
| Uso | o cartão inteiro é a área de toque e abre o Prospect (T03, aba Prospects → T05.3). As mensagens são preenchidas por cada tela. O Prospect existe só como `PROSPECT + BLOQUEADO` (Doc. Mestre, seção 4.1), por isso o selo mostra essa situação e uma mensagem explica o motivo, por exemplo "Cadastro ainda não aprovado" |
| Referência | T03 e T05.3 do Doc. Mestre; mesmas referências do C16 (Aetna, Glance, Material 3) |
| Variantes | `C17.1` (com seletor no lugar da seta) e `C17.2` (desabilitado, sem controle) |
| Não validado | a T03 não desenha o item de Prospect, então o cartão é inferido; a linha de contato (o documento a traz na T05.3, não na lista); ausência de código; altura de 152 px; comportamento com texto mais longo que a linha (truncamento ou quebra) |

**C17.1 — ProspectCardSelectable (variante do C17)**

| Item | Valor |
| --- | --- |
| Conteúdo | o mesmo conteúdo do C17, com um seletor (botão de rádio de 24 px) no lugar da seta ("Mensagem 1" e "Mensagem 2" são **placeholders**) |
| Dimensões | 336 × 152 px, as mesmas do C17; seletor a 16 px da borda direita, alinhado à linha do título |
| Estados | a v01 mostra o seletor **vazio** (ícone `radio_button_unchecked` em BORDER-CONTROL); `COMP-C17.1-ProspectCardSelectable-v01_Selecionado.png` mostra o seletor **marcado** (`radio_button_checked` em Primary) |
| Uso | escolha de um Prospect nos campos "Cliente/Prospect" da T06 e da T16.1; o Doc. Mestre não desenha essa lista |
| Não validado | existência e layout da lista de seleção (sem textframe); escolha do botão de rádio |

**C17.2 — ProspectCardDisabled (variante do C17)**

| Item | Valor |
| --- | --- |
| Conteúdo | o mesmo conteúdo do C17, sem seta e sem seletor ("Mensagem 1" e "Mensagem 2" são **placeholders**) |
| Dimensões | 336 × 152 px, as mesmas do C17 |
| Uso | Prospect que não pode ser aberto nem selecionado; a mensagem explica o motivo |
| Não validado | o Doc. Mestre não prevê uso: o Prospect não é listado no seletor de pedido (M09.1) e a T06 não o desabilita; mantida por simetria com o C16.2; decisão do responsável |

**C18 — ProductCard**

| Item | Valor |
| --- | --- |
| Conteúdo | imagem placeholder de 72 × 72 px (raio 12, SURFACE) à esquerda; título em Inter Medium 16 px (TEXT) com `chevron_right` à direita; SKU em Inter Regular 14 px (TEXT-2); preço e unidade em Inter Medium 14 px (TEXT); selo de status (C14); botão `[ + ]` de 48 × 48 px (raio 12, borda BORDER-CONTROL, ícone `add` 24 px) ("Título", "SKU 000000", "R$ 0,00 / UN" e o selo "Status" são **placeholders**) |
| Dimensões | 336 × 110 px, raio 16 px, fundo SURFACE-ALT; textos a 96 px da borda esquerda |
| Ações | duas ações separadas, sem elementos interativos aninhados: a área de informações (imagem, texto e seta) abre o detalhe (T08) e o botão `[ + ]` adiciona o item ao pedido em edição (T07) |
| Variante | `C18.1` (indisponível): o `[ + ]` aparece desabilitado (ícone e borda em DISABLED `#9A9A9A`) |
| Uso | item do catálogo da T07 |
| Não validado | tamanho da imagem (72 px) e altura do cartão; preço em Medium 14 (o C31.1 é Regular 14 em TEXT-2); existência e comportamento da variante indisponível (o Doc. Mestre só define "Disponível"); indicadores de promoção e favorito (filtros existem na M07.1, mas o item não os desenha); truncamento de textos longos; item do pedido da T10 (sem imagem, com quantidade e total) não coberto por este componente |

**C18.2 — ProductOrderItem (variante do C18)**

| Item | Valor |
| --- | --- |
| Conteúdo | título em Inter Medium 16 px (TEXT); SKU em Inter Regular 14 px (TEXT-2); linha `quantidade UN × preço` em Inter Regular 14 px (TEXT-2) com o total em Inter Medium 16 px (TEXT) alinhado à direita; abaixo, `[ − ] quantidade [ + ]` (botões de 48 × 48 px, raio 12, borda BORDER-CONTROL, ícones `remove` e `add` de 24 px) à esquerda e o botão `Editar` (88 × 48 px, raio 12, borda BORDER-CONTROL, Inter Medium 14 px) à direita ("Título", "SKU 000000", "00 UN × R$ 0,00", "R$ 0,00" e "00" são **placeholders**) |
| Dimensões | 336 × 150 px, raio 16 px, fundo SURFACE-ALT; cartão avulso, sem imagem |
| Ações | `[ − ]` e `[ + ]` alteram a quantidade; `Editar` abre o M10.1 |
| Variante | `C18.3` (sem a linha de SKU), 336 × 126 px |
| Uso | item do pedido na T10 (L3236–3250) |
| Não validado | tamanhos dos botões de 48 px e de `Editar` (88 × 48), alturas de 126 e 150 px e total em Medium 16 (o documento só traz o textframe); stepper compacto independente do C21; divisor de 1 px entre itens (T10 e T07) não virou componente, como no C19; comportamento com textos longos |

**C19 — OrderCard**

| Item | Valor |
| --- | --- |
| Conteúdo | título em Inter Medium 16 px, TEXT; abaixo, o valor monetário (C31.1), o separador `•` e o selo de status (C14); `chevron_right` à direita ("Título", "R$ 0,00" e o selo "Status" são **placeholders**) |
| Dimensões | 336 × 64 px, raio 16 px, fundo SURFACE-ALT; cartão avulso, que funciona isolado em qualquer janela |
| Composição | o valor e o selo são os mesmos arquivos do C31.1 e do C14, a 5 px do fim do separador; o selo muda de ícone, texto e cor conforme o status do pedido (ver C14) |
| Em lista | na T02 as linhas ficam num contêiner único (raio 16 px, SURFACE-ALT) com divisor de 1 px em BORDER `#B5B5B5` entre elas. O contêiner de lista não é componente do catálogo e não foi isolado aqui |
| Não validado | comportamento com título ou valor mais longos que a linha (truncamento ou quebra), pois as telas aprovadas só trazem textos curtos; decisão do responsável |

**C19.1 — OrderCardByClient (variante do C19)**

| Item | Valor |
| --- | --- |
| Conteúdo | título em Inter Medium 16 px (TEXT) com `chevron_right` à direita; abaixo, em linhas separadas, a data em Inter Regular 14 px (TEXT-2), o valor monetário (estilo do C31.1) e o selo de status (C14) ("#000000", "00/00/0000", "R$ 0,00" e o selo "Status" são **placeholders**) |
| Dimensões | 336 × 110 px, raio 16 px, fundo SURFACE-ALT; cartão avulso; texto a 16 px da borda esquerda, linhas a cada 22 px |
| Uso | lista de pedidos do Cliente na T04.1 (L1870–1888) |
| Não validado | variante criada por decisão do responsável (15/11/2026, 20:45); o catálogo (seção 20) só define o C19; valor e selo em linhas separadas, como no textframe, em vez da linha única do C19; as telas mostram linhas com divisor, sem cartão; altura de 110 px; truncamento de textos longos |

**C19.2 — OrderCardByCustomer (variante do C19)**

| Item | Valor |
| --- | --- |
| Conteúdo | igual ao C19.1, com o nome do cliente no lugar da data ("#000000", "Cliente", "R$ 0,00" e o selo "Status" são **placeholders**) |
| Dimensões | 336 × 110 px, as mesmas do C19.1 |
| Uso | lista de pedidos da T14 (L3574–3604) |
| Não validado | os mesmos do C19.1; a geometria é idêntica à do C19.1 e só muda a segunda linha |

**C20 — VisitCard**

| Item | Valor |
| --- | --- |
| Conteúdo | horário em Inter Medium 14 px na cor Primary `#004A99`, à esquerda; título em Inter Medium 16 px (TEXT) e subtítulo em Inter Regular 14 px (TEXT-2), alinhados a 72 px da borda esquerda; `chevron_right` à direita ("00:00", "Título" e "Subtítulo" são **placeholders**) |
| Dimensões | 336 × 64 px, raio 16 px, fundo SURFACE-ALT; cartão avulso, que funciona isolado em qualquer janela |
| Em lista | igual ao C19: na T02 as linhas ficam num contêiner único com divisor de 1 px em BORDER `#B5B5B5`; o contêiner não foi isolado aqui |
| Não validado | comportamento com título ou subtítulo mais longos que a linha; decisão do responsável |

**C20.1 — VisitHistoryItem (variante do C20)**

| Item | Valor |
| --- | --- |
| Conteúdo | data em Inter Medium 16 px (TEXT) com `chevron_right` à direita; abaixo, o tipo e o resultado da visita em Inter Regular 14 px (TEXT-2) ("00 MMM 0000", "Tipo" e "Resultado" são **placeholders**) |
| Dimensões | 336 × 88 px, raio 16 px, fundo SURFACE-ALT; cartão avulso; texto a 16 px da borda esquerda |
| Uso | histórico de visitas do Cliente na T04.2 (L1921–1939) e do Prospect na T05.4 (L2517) |
| Não validado | variante criada por decisão do responsável (15/11/2026, 20:45); o catálogo só define o C20; o formato do mês abreviado em caixa alta ("15 OUT 2026") é o do textframe; as telas mostram linhas com divisor, sem cartão; altura de 88 px; truncamento de textos longos |

**C21 — QuantitySelector**

| Item | Valor |
| --- | --- |
| Conteúdo | botão −, valor numérico centralizado e botão + ("10" é **placeholder**) |
| Dimensões | 336 × 48 px; botões 48 × 48 px (raio 12, borda de 1 px, fundo SURFACE) nas extremidades; ícones `remove` e `add` de 24 px em ACTION; valor Inter Medium 20 em TEXT |
| Estados | a v01 mostra os dois botões ativos. **No mínimo** (`COMP-C21-QuantitySelector-v01_Minimo.png`): botão − com borda e ícone na cor DISABLED. No máximo, o botão + segue a mesma regra. Foco e pressionado serão arquivos próprios |
| Referência | NN/g e Baymard (botões − e + em volta do valor); alvo de toque de 48 px do projeto (acima do mínimo de 44 px do WCAG); layout de T08 e T10 do Doc. Mestre |
| Não validado | tamanho do valor (Medium 20); campo editável pelo teclado; limite máximo |

**C22 — FilterChip**

| Item | Valor |
| --- | --- |
| Conteúdo | chip com texto ("Filtro" é **placeholder**) |
| Dimensões | 58 × 32 px (largura segue o texto, com 12 px de margem lateral); raio 8; borda de 1 px; texto Inter Medium 14 |
| Estados | a v01 mostra o estado **não selecionado**: fundo SURFACE, borda BORDER-CONTROL e texto TEXT. Estado **selecionado** (`COMP-C22-FilterChip-v01_Selecionado.png`, 80 × 32 px): fundo SURFACE-ALT, borda Primary, ✓ (`check`, 18 px) em Primary à esquerda, margens de 8 px, texto TEXT. Desabilitado, foco e pressionado serão arquivos próprios |
| Referência | Material Design 3 (altura 32, raio 8, ✓ ao selecionar) |
| Não validado | altura de 32 px abaixo do alvo de toque de 48 px (a área de toque deve se estender fora do desenho); cores do estado selecionado |

**C23 — Stepper**

| Item | Valor |
| --- | --- |
| Conteúdo | indicador de 4 etapas com círculos, conectores e rótulos ("Etapa" é **placeholder**) |
| Dimensões | 336 × 56 px; círculos de 24 px com centros a cada 84 px; conectores de 2 px; rótulo Inter 12 abaixo do círculo |
| Estados | a v01 mostra a **etapa 2 como atual**. Concluída: círculo Primary com ✓ ON Primary e conector Primary. Atual: fundo SURFACE-ALT, borda de 2 px e número em Primary, rótulo Medium em TEXT. Futura: fundo SURFACE-ALT, borda de 1 px, número e rótulo em TEXT-2. Outras posições: etapa 1 atual (`COMP-C23-Stepper-v01_Etapa1.png`) e etapa 4 atual (`COMP-C23-Stepper-v01_Etapa4.png`) |
| Referência | design systems Toyota, eBay, Red Hat e Genesys (concluída, atual e futura; cor nunca é o único sinal; conector decorativo); até 4 etapas em mobile; wizard de pedido do Doc. Mestre (Cliente, Itens, Condições, Revisão) |
| Não validado | uso do Primary para progresso; número e posição das etapas; tamanho de 24 px |

**C24 — StatusTimeline**

| Item | Valor |
| --- | --- |
| Conteúdo | lista vertical de 5 etapas com marcador, trilho e rótulo ("Etapa" é **placeholder**), como o "Andamento" da T15 |
| Dimensões | 336 × 184 px; marcadores de 24 px a cada 40 px; trilho de 2 px; rótulo Inter 14 a 48 px da borda esquerda |
| Estados | a v01 mostra 2 etapas **concluídas** (círculo Primary com ✓ ON Primary), a etapa 3 **em andamento** (anel Primary de 2 px com ponto Primary, rótulo Medium em TEXT) e 2 **pendentes** (círculo SURFACE-ALT com borda de 1 px BORDER-CONTROL, rótulo em TEXT-2). O trilho é contínuo em Primary antes da etapa em andamento e tracejado em BORDER abaixo dela. Variações: `COMP-C24-StatusTimeline-v01_Etapa1.png` (etapa 1 em andamento) e `COMP-C24-StatusTimeline-v01_Etapa5.png` (etapa 5 em andamento) |
| Referência | Maersk Design System, UX4G e Customer.io Pluma (lista ordenada, uma só etapa atual, cor nunca é o único sinal); T15 do Doc. Mestre |
| Não validado | marcador da etapa em andamento (a T15 mostra só ✓ e ○); tamanho de 24 px e passo de 40 px; ausência de data e hora nas etapas; número de etapas (5) |

**C25 — Dialog**

| Item | Valor |
| --- | --- |
| Conteúdo | círculo de ícone (48 px; o ícone varia por situação, por isso a imagem genérica traz o círculo vazio), título, descrição centralizada em até três linhas e botão primário de largura total do diálogo. Textos são **placeholders**. |
| Dimensões | 312 × 308 px, raio 16 px; botão 264 × 48; a altura varia com o conteúdo |

**C26 — BottomSheet**

| Item | Valor |
| --- | --- |
| Conteúdo | folha modal com alça, título com botão de fechar, divisor e três linhas de conteúdo ("Título" e "Opção" são **placeholders**, e o ícone das linhas é o ícone placeholder) |
| Dimensões | 360 × 280 px, de lado a lado e colada na base, com raio de 16 px só nos cantos superiores; a altura varia com o conteúdo. Alça de 32 × 4 px em BORDER-CONTROL, numa área de 48 px; título Inter SemiBold 18 em TEXT; botão de fechar com ícone `close` de 24 px em ACTION e alvo de 48 px; divisor de 1 px em BORDER; linhas de 56 px com margem lateral de 12 px |
| Estados | a v01 mostra a folha aberta, sem o escurecimento do fundo (scrim), que pertence à tela. Foco e rolagem do conteúdo não estão desenhados |
| Referência | Material Design 3 (alça de 32 × 4, alvo de toque de 48), OVO e Koder Design (controle de fechar visível, foco preso, Esc fecha, foco volta ao gatilho) |
| Não validado | raio de 16 px (o M3 usa 28; vale a regra de modal do projeto); título SemiBold 18; margem lateral de 12 px; conteúdo real, definido por cada tela (como o filtro M03.1) |

**C27 — EmptyState**

| Item | Valor |
| --- | --- |
| Conteúdo | mensagem centralizada em Inter Regular 14 px, na cor TEXT-2 ("Texto de estado vazio" é **placeholder**) |
| Dimensões | 336 × 64 px, raio 16 px, fundo SURFACE-ALT |
| Opacidade | fundo do bloco com opacidade 0.8 (alpha 204 de 255), por decisão do responsável em 15/11/2026, 14:05; `REGRAS-TECNICAS.md` não define opacidade. Texto, logomarca, ícone e botão ficam 100% opacos; os cantos arredondados são transparentes |

**C28 — ErrorState**

| Item | Valor |
| --- | --- |
| Conteúdo | ícone centralizado de 36 px (o tracejado é **placeholder**), mensagem centralizada em Inter Regular 16 px e botão primário de 304 × 48 px, raio 12 px, com rótulo ("Mensagem de erro" e "RÓTULO" são **placeholders**) |
| Dimensões | 336 × 188 px, raio 16 px, fundo SURFACE-ALT |
| Estados | o ícone e a cor do ícone mudam conforme o tipo de erro; a v01 usa placeholder neutro (ACTION `#333333`). Para erro de carregamento de dados, o ícone é de alerta no token Error `#991B1B`. |

**C29 — LoadingState**

O LoadingState tem **duas versões**: bloco de lista (C29) e bloco de cartão (C29.1).

| Item | Valor |
| --- | --- |
| Conteúdo | bloco que ocupa o lugar do elemento enquanto os dados carregam, com a logomarca SaOr centralizada (variante para fundos claros, 64 px de altura, proporção original) e, abaixo dela, o texto fixo `Aguarde...` (Inter Regular 14 px, TEXT-2, espaçamento de 8 px); o conjunto é centralizado verticalmente |
| Dimensões | 336 × 128 px, raio 16 px, fundo SURFACE-ALT; largura e altura acompanham o elemento que o bloco substitui |
| Logomarca | arquivo oficial `saor-logo-SSO-para_fundos_claros.png` (SHA-256 `dd4082946acfce2d25ccf2b154949ec3df8c1d36fe2a8cfa406e4054949cf419`), variante de aplicação para fundos claros; sem inversão de cores nem filtros |
| Não validado | altura da logomarca (64 px), espaçamento e tamanho do texto; o catálogo de identidade visual não define tamanho mínimo nem área de proteção; decisão do responsável |

**C29.1 — LoadingStateCard (variante do C29)**

| Item | Valor |
| --- | --- |
| Conteúdo | bloco no lugar de um cartão de métrica, com a logomarca SaOr centralizada (mesmo arquivo do C29, 36 px de altura) e, abaixo dela, o texto fixo `Aguarde...` (Inter Regular 12 px, TEXT-2, espaçamento de 6 px); o conjunto é centralizado verticalmente |
| Dimensões | 164 × 88 px, raio 16 px, fundo SURFACE-ALT |
| Não validado | altura da logomarca (36 px), espaçamento e tamanho do texto; decisão do responsável |

**C30 — SyncStatus**

O SyncStatus tem **duas versões**: só com texto de status (C30) e com título e subtítulo (C30.1).

| Item | Valor |
| --- | --- |
| Conteúdo | texto de status à esquerda ("Texto de status" é **placeholder**, na cor do estado) e chip de 40 × 40 com o ícone do estado à direita |
| Dimensões | 336 × 67 px |
| Estados | cor e ícone mudam conforme o estado (tabela "Variação por estado"); a v01 mostra "sincronizado" e cada demais estado será arquivo próprio |

**C30.1 — SyncStatusDetail (variante do C30)**

| Item | Valor |
| --- | --- |
| Conteúdo | título, subtítulo e texto de status à esquerda ("Título", "Subtítulo" e "Texto de status" são **placeholders**) e chip de 40 × 40 à direita |
| Dimensões | 336 × 67 px |
| Estados | iguais aos do C30 (tabela "Variação por estado"); título e subtítulo não mudam com o estado |

**Variação por estado (C30 e C30.1)**

Cor e ícone do SyncStatus dependem do estado de sincronização. O texto de status e o ícone do chip usam o mesmo token de status; o fundo do chip permanece SURFACE-ALT em todos os estados.

| Estado | Token de status (texto e ícone) | Ícone do chip |
| --- | --- | --- |
| Sincronizado | Success `#166534` | confirmação |
| Sincronizando | Info `#004A99` | sincronização |
| Carregando | Info `#004A99` | progresso circular |
| Falha na sincronização | Warning (texto/ícone) `#AC4F01` | alerta |
| Offline | Warning (texto/ícone) `#AC4F01` | sem conexão |
| Erro | Error `#991B1B` | erro |

Não validado: correspondência dos ícones com os nomes da família Material Icons Outlined (seção 9 de `REGRAS-TECNICAS.md`); decisão do responsável.

Warning (White): decisão do responsável em 15/11/2026, 14:15: usar o valor da tabela 6.5 de `REGRAS-TECNICAS.md`, `#AC4F01`, em vez do `#7C4A03` do Documento Mestre §20.1.

**C31 — MoneyDisplay**

O MoneyDisplay tem **duas versões**: em destaque (C31) e em linha (C31.1).

| Item | Valor |
| --- | --- |
| Conteúdo | valor monetário em destaque, Inter SemiBold 20 px, TEXT, como no MetricCard ("R$ 0,00" é **placeholder**) |
| Dimensões | 76 × 24 px; a largura acompanha o texto; fundo SURFACE-ALT, o fundo em que o valor aparece nos cartões |
| Formato | prefixo `R$` e espaço, milhar com ponto, decimal com vírgula e duas casas, conforme as telas aprovadas (`R$ 8.450,00`, `R$ 980,00`, `R$ 0,00`); o formato é o do componente e o número é variável |

**C31.1 — MoneyDisplayInline (variante do C31)**

| Item | Valor |
| --- | --- |
| Conteúdo | o mesmo valor em linha com outro texto, Inter Regular 14 px, TEXT-2, como na linha de pedido ("R$ 0,00" é **placeholder**) |
| Dimensões | 52 × 20 px; a largura acompanha o texto; fundo SURFACE-ALT; mesma altura e linha de base do C14, para que os dois fiquem alinhados na mesma linha |
| Formato | igual ao do C31 |

**C32 — SectionHeader**

A SectionHeader tem **duas versões**: sem ícone (C32) e com ícone (C32.1).

| Item | Valor |
| --- | --- |
| Conteúdo | título de seção ("Título da seção" é **placeholder**), Inter SemiBold 14 px |
| Dimensões | 336 × 30 px |

**C32.1 — SectionHeaderIcon (variante do C32)**

| Item | Valor |
| --- | --- |
| Conteúdo | ícone de 24 px à esquerda (o tracejado é **placeholder**: cada seção usa o seu ícone) e título de seção |
| Dimensões | 336 × 30 px; título a 32 px da borda esquerda |
| Não validado | tamanho do ícone e espaçamento até o título |

**C33 — AddressCard**

| Item | Valor |
| --- | --- |
| Conteúdo | seletor de rádio de 24 px à esquerda (`radio_button_unchecked` em BORDER-CONTROL); título em Inter Medium 16 px (TEXT) ao lado do seletor; abaixo, a 48 px da borda esquerda, logradouro, bairro, cidade-UF e CEP em Inter Regular 14 px (TEXT-2) ("Título", "Logradouro, 000", "Bairro", "Cidade - UF" e "CEP 00000-000" são **placeholders**) |
| Dimensões | 336 × 130 px, raio 16 px, fundo SURFACE-ALT; cartão avulso |
| Estados | a v01 mostra o seletor **vazio**; `COMP-C33-AddressCard-v01_Selecionado.png` mostra o seletor **marcado** (`radio_button_checked` em Primary) |
| Variantes | `C33.1` (resumo, com seta), `C33.2` (detalhe, somente leitura) e `C33.3` (caixa de mapa) |
| Uso | escolha do endereço de entrega na T09.2 (L3109–3164) |
| Não validado | seletor à esquerda, conforme o textframe (no C16.1 e no C17.1 fica à direita) e linhas alinhadas ao título (decisão minha); altura de 130 px e espaçamento de 22 px entre linhas; o tipo do endereço (Principal, Entrega, Filial, Depósito) é só exemplo, por isso o título é placeholder; não há variante desabilitada, pois o documento não a prevê; truncamento de textos longos |

**C33.1 — AddressCardSummary (variante do C33)**

| Item | Valor |
| --- | --- |
| Conteúdo | título em Inter Medium 16 px (TEXT), logradouro e cidade-UF em Inter Regular 14 px (TEXT-2) e `chevron_right` à direita ("Título", "Logradouro, 000" e "Cidade - UF" são **placeholders**) |
| Dimensões | 336 × 92 px, raio 16 px, fundo SURFACE-ALT |
| Uso | linha de resumo do endereço, com destino à T09.2, T15.2 ou T04.4: T09 (L3024), T12 (L3413), T15 (L3700), T04 (L1841), T05 (L2475) e T16 (L3970) |
| Não validado | duas linhas apenas (a T12 mostra só a rua); o rótulo em maiúsculas da T12 ("ENTREGA") entra como o título; se o resumo é componente ou só linha de campo; altura de 92 px |

**C33.2 — AddressCardDetail (variante do C33)**

| Item | Valor |
| --- | --- |
| Conteúdo | rótulo `CEP` (Inter Regular 14 px, TEXT-2) e valor (Inter Regular 16 px, TEXT); abaixo, logradouro, complemento, bairro e cidade-UF em Inter Regular 16 px (TEXT); rótulo `Referência` e texto de referência ("00000-000", "Logradouro, 000", "Complemento", "Bairro", "Cidade - UF" e "Texto de referência" são **placeholders**) |
| Dimensões | 336 × 232 px, raio 16 px, fundo SURFACE-ALT; somente leitura |
| Uso | consulta de endereço na T04.4 (L2037–2060) e na T15.2 (L3788–3805) |
| Não validado | a caixa `MAPA` está no `C33.3` e o botão `ABRIR NO MAPA` não foi desenhado (seria o C03 ou o C04); o item "localização" da lista de informações da T04.4 (L2031) não aparece no textframe, e presume-se que seja o mapa (inferência); altura de 232 px e espaçamento entre linhas; nomes e numeração C33.1 e C33.2 |

**C33.3 — AddressMap (variante do C33)**

| Item | Valor |
| --- | --- |
| Conteúdo | caixa de mapa com o marcador `location_on` de 40 px em Primary, centralizado |
| Dimensões | 336 × 200 px, raio 16 px, fundo SURFACE-ALT |
| Uso | espaço do mapa na T04.4 (L2054–2058) e na T15.2 (L3802–3806), acima do botão `ABRIR NO MAPA` (C03 ou C04) |
| Não validado | o documento só traz o desenho `MAPA` com `●`; altura de 200 px e o marcador `location_on` são decisão minha; o mapa real vem de serviço externo, então a imagem é placeholder; o botão `ABRIR NO MAPA` não está na imagem |

**C34 — ContactCard**

O ContactCard tem **três versões**: resumo com ícones (C34), detalhe com rótulos (C34.1) e cabeçalho de perfil (C34.2).

| Item | Valor |
| --- | --- |
| Conteúdo | três linhas, cada uma com ícone de 24 px em ACTION `#333333` à esquerda e texto em Inter Regular 16 px (TEXT) a 56 px da borda: `place` + cidade-UF, `call` + telefone, `person` + nome do contato ("Cidade - UF", "(00) 00000-0000" e "Contato principal" são **placeholders**) |
| Dimensões | 336 × 112 px, raio 16 px, fundo SURFACE-ALT; cartão avulso; linhas a cada 32 px |
| Uso | bloco de contato no resumo do Cliente (T04, L1826–1828) e do Prospect (T05.3, L2460–2462) |
| Não validado | o fundo de cartão (o textframe mostra só as três linhas, sem cartão); nenhuma ação ao tocar (ligar, abrir WhatsApp), pois o documento não define; nomes dos ícones `place`, `call` e `person` (correspondência com a família Material Icons Outlined não verificada); altura de 112 px e passo de 32 px; truncamento de textos longos |

**C34.1 — ContactCardDetail (variante do C34)**

| Item | Valor |
| --- | --- |
| Conteúdo | pares de rótulo e valor empilhados: rótulo em Inter Regular 14 px (TEXT-2) e valor em Inter Regular 16 px (TEXT), três pares ("Contato principal" / "Nome do contato", "Telefone" / "(00) 00000-0000", "E-mail" / "email@exemplo.com"; os valores são **placeholders**) |
| Dimensões | 336 × 176 px, raio 16 px, fundo SURFACE-ALT; somente leitura; um par a cada 56 px, texto a 16 px da borda |
| Uso | contato nos dados cadastrais do Cliente (T04.5, L2105–2113); o bloco "E-mail" e "Telefone" do perfil (T17.1, L4151–4156) usa o mesmo desenho, com os pares que a tela traz |
| Não validado | cobertura da T17.1 (a imagem traz três pares; a T17.1 mostra só E-mail e Telefone); fundo de cartão; altura de 176 px e passo de 56 px; truncamento de textos longos |

**C34.2 — ProfileHeader (variante do C34)**

| Item | Valor |
| --- | --- |
| Conteúdo | avatar circular de 72 px (fundo SURFACE-ALT, ícone `person` de 40 px em ACTION) centralizado; abaixo, o nome em Inter SemiBold 18 px (TEXT) e o cargo em Inter Regular 14 px (TEXT-2), centralizados ("Nome do usuário" e "Cargo" são **placeholders**; o avatar é o espaço da `[ FOTO ]`) |
| Dimensões | 336 × 136 px, sobre o fundo da tela (BG `#F4F4F4`), sem cartão; PNG com fundo transparente |
| Uso | cabeçalho com foto, nome e cargo do vendedor na T17 (L4087–4090) e na T17.1 |
| Não validado | tamanho do avatar (72 px) e das fontes do nome e do cargo; ícone no lugar da foto real (o documento só traz `[ FOTO ]`); ausência de cartão; altura de 136 px; truncamento de textos longos |

**C35 — ThemeSelector**

| Item | Valor |
| --- | --- |
| Conteúdo | seletor segmentado com duas opções, "Claro" e "Escuro", cada uma com ícone |
| Dimensões | 336 × 56 px, raio 12 px |
| Opção ativa | **muda conforme o tema selecionado**. A v01 mostra "Claro" ativo; "Escuro" ativo será arquivo próprio. |

**C36 — ThemePreview**

| Item | Valor |
| --- | --- |
| Conteúdo | cartão de pré-visualização do tema: logo SaOr, saudação, dois cartões de métrica e botão primário com ícone. Os textos e valores são de exemplo. |
| Dimensões | 336 × 290 px, raio 16 px, borda de 1 px |
| Tema | a v01 mostra a pré-visualização do tema white |

**C37 — ConnectionStatus**

| Item | Valor |
| --- | --- |
| Conteúdo | rótulo "Status", ConnectionBadge (C44) e texto de apoio em até duas linhas ("Status" e o ícone tracejado do selo e "Texto de apoio em até duas linhas." são **placeholders**) |
| Dimensões | 336 × 56 px |
| Estados | o ícone e a cor mudam conforme o estado; a v01 usa cor neutra (contorno BORDER-CONTROL e texto TEXT) e cada estado será arquivo próprio |

**C38 — ApiConfigurationForm**

| Item | Valor |
| --- | --- |
| Conteúdo | formulário completo: campo "URL da API" com ícone de validação e texto de apoio, SecretInput (C39), ConnectionTest (C40), ConnectionStatus (C37) e botão primário "SALVAR". O endereço e o texto do último teste são valores de exemplo. |
| Dimensões | 336 × 464 px |
| Estados | a v01 mostra só "conectado"; demais estados serão arquivos próprios |

**C39 — SecretInput**

| Item | Valor |
| --- | --- |
| Conteúdo | TextInput (C06) com valor mascarado e dois ícones à direita (mostrar/ocultar e colar). "Rótulo" e "Texto de apoio." são **placeholders** |
| Dimensões | 336 × 106 px; campo 336 × 56, raio 12 px, borda de 1 px |
| Estados | a v01 mostra o valor oculto; valor visível e demais estados serão arquivos próprios |

**C40 — ConnectionTest**

| Item | Valor |
| --- | --- |
| Conteúdo | botão secundário com ícone e rótulo "TESTAR CONEXÃO", contorno de 1 px, sem preenchimento |
| Dimensões | 336 × 56 px, raio 12 px (altura padrão dos botões C03 a C05); conteúdo centralizado verticalmente |
| Estados | a v01 mostra só o estado padrão; testando e demais estados serão arquivos próprios |

**C41 — DiagnosticsItem**

| Item | Valor |
| --- | --- |
| Conteúdo | ícone de 24 px à esquerda (o tracejado é **placeholder**), rótulo e, à direita, ícone de estado com texto de status ("Rótulo", "Status" e o ícone tracejado de estado são **placeholders**) |
| Dimensões | 336 × 72 px, raio 16 px |
| Estados | o ícone e a cor mudam conforme o estado; a v01 usa cor neutra (contorno BORDER-CONTROL e texto TEXT) e cada estado será arquivo próprio |

**C42 — SettingsGroup**

| Item | Valor |
| --- | --- |
| Conteúdo | título do grupo em caixa alta ("TÍTULO DO GRUPO" é **placeholder**) e, abaixo, SettingsItem (C43) |
| Dimensões | 336 × 104 px; título do grupo a 16 px da borda esquerda |

**C43 — SettingsItem**

O SettingsItem tem **três versões**: padrão (C43), com ConnectionBadge (C43.1) e de ação destrutiva (C43.2).

| Item | Valor |
| --- | --- |
| Conteúdo | ícone de 24 px à esquerda (o tracejado é **placeholder**), título, subtítulo e `chevron_right` à direita ("Título" e "Subtítulo" são **placeholders**) |
| Dimensões | 336 × 72 px, raio 16 px |

**C43.1 — SettingsItemBadge (variante do C43)**

| Item | Valor |
| --- | --- |
| Conteúdo | ícone, título e selo de status abaixo do título, no lugar do subtítulo; `chevron_right` à direita ("Título", "Status" e o ícone tracejado do selo são **placeholders**) |
| Dimensões | 336 × 80 px, raio 16 px |
| Selo | ícone de 18 px, maior que o do C44 (16 px); largura acompanha o texto |
| Estados | o ícone e a cor mudam conforme o estado; a v01 usa cor neutra (contorno BORDER-CONTROL e texto TEXT) e cada estado será arquivo próprio |

**C43.2 — SettingsItemDestructive (variante do C43)**

| Item | Valor |
| --- | --- |
| Conteúdo | ícone, título e `chevron_right` na cor Error, sem subtítulo |
| Dimensões | 336 × 56 px, raio 16 px |

**C44 — ConnectionBadge**

| Item | Valor |
| --- | --- |
| Conteúdo | selo com contorno de 1 px, ícone de estado de 16 px e texto de status ("Status" e o ícone tracejado são **placeholders**) |
| Dimensões | 77 × 24 px; a largura acompanha o texto |
| Estados | o ícone e a cor mudam conforme o estado; a v01 usa cor neutra (contorno BORDER-CONTROL e texto TEXT) e cada estado será arquivo próprio |

---

## 4. Integridade (SHA-256)

Os hashes ficam na tabela de histórico (seção 5). O arquivo `SHA256SUMS`, nesta pasta, traz os hashes das versões **vigentes** no formato do `sha256sum`. Em divergência, vale a tabela da seção 5.

Conferir, a partir desta pasta:

```text
sha256sum -c SHA256SUMS
```

Regenerar o `SHA256SUMS` a partir da tabela (após qualquer mudança na seção 5):

```text
grep -E '^\| [0-9/]+ \|.*\| VIGENTE \|' README.md | sed -E 's/.*`(COMP-[^`]+)`.*`([0-9a-f]{64})`.*/\2  \1/' > SHA256SUMS
```

Esperado na conferência: tudo `OK`. Qualquer `FAILED` bloqueia o uso até decisão do responsável.

---

## 5. Histórico de versões

Registra **todas as versões criadas**, vigentes ou não. A versão em uso é a de situação `VIGENTE` (e é a da seção 3). Os arquivos de versões antigas permanecem na pasta.

| Data | ID | Versão | Arquivo | SHA-256 | Situação | Motivo |
| --- | --- | --- | --- | --- | --- | --- |
| 15/11/2026 | C01 | v01 | `COMP-C01-AppHeader-v01.png` | `b7c010834f2394644709c828ecc47c780e8169c6aeed5e546a88cfea2222f76f` | VIGENTE | Versão inicial |
| 15/11/2026 | C01.1 | v01 | `COMP-C01.1-AppHeaderBack-v01.png` | `a62ac164c36c5f86ca2a9692f3290af63ca906d066a90325abff767915184986` | VIGENTE | Versão inicial |
| 15/11/2026 | C02 | v01 | `COMP-C02-BottomNavigation-v01.png` | `98fe8d8e01f2a1ce97df244bd36c60b716f813e89688f7dbdd03dc5bbe414c90` | VIGENTE | Versão inicial |
| 15/11/2026 | C03 | v01 | `COMP-C03-PrimaryButton-v01.png` | `b7bbf00fedb1763c7939e563823c5429d782c0c2cf958dc35eaf80e1938c0f4f` | VIGENTE | Versão inicial |
| 15/11/2026 | C04 | v01 | `COMP-C04-SecondaryButton-v01.png` | `27384c75eb6b6901dd5edf5b47737457bb95949535ddfa3953ae0f155cc9af40` | VIGENTE | Versão inicial |
| 15/11/2026 | C05 | v01 | `COMP-C05-TextButton-v01.png` | `f373aaee7858089724b2de3ee315edbff6b3453d03501bca49efda74993fbe60` | VIGENTE | Versão inicial |
| 15/11/2026 | C06 | v01 | `COMP-C06-TextInput-v01.png` | `02f8f6980ff9347f9fa3d2b284ed07a4d252250010a03e31aebfc467c269c8e5` | VIGENTE | Versão inicial |
| 15/11/2026 | C06.1 | v01 | `COMP-C06.1-TextInputShort-v01.png` | `b732d66a42e6d2ceeb308690244a3189925b8e702a58bb5f558386bf46b93171` | VIGENTE | Versão inicial |
| 15/11/2026 | C06.2 | v01 | `COMP-C06.2-TextInputWithButton-v01.png` | `1280e32523a799f3832d87e5c07b5d92dcda4e283fc4dd610c7933a712f5c98a` | VIGENTE | Versão inicial |
| 15/11/2026 | C07 | v01 | `COMP-C07-SearchInput-v01.png` | `1f6118dade03fc9d388619367b28f533bbfb5f068d45e1d4a9295cc22964f3d4` | VIGENTE | Versão inicial |
| 15/11/2026 | C08 | v01 | `COMP-C08-SelectInput-v01.png` | `e6d85e0ba6e45b27e1cf718bec5726e27b8b40f573f716d326dab1a1d8df7d2b` | VIGENTE | Versão inicial |
| 15/11/2026 | C09 | v01 | `COMP-C09-DateInput-v01.png` | `18d6c092c965d5cb2a7c0fcd91c01369f725bf04de9c535f129464ff25e37e9e` | VIGENTE | Versão inicial |
| 15/11/2026 | C09.1 | v01 | `COMP-C09.1-DatePickerCalendar-v01.png` | `64c9d011a423eb8767ee646ec8e83886228f4ea729c06e60bb4a6357045773ff` | VIGENTE | Versão inicial |
| 15/11/2026 | C10 | v01 | `COMP-C10-TimeInput-v01.png` | `3d9db3a47fd9d71eb99e77f0aaa70ad1cc31ce11bc7425c08f35ed062b4c7d20` | VIGENTE | Versão inicial |
| 15/11/2026 | C11 | v01 | `COMP-C11-TextArea-v01.png` | `576aea91f46efe25bc3e61ab3fd77d1d122b9a36f9ed1e0223a036aadaeddbf5` | VIGENTE | Versão inicial |
| 15/11/2026 | C12 | v01 | `COMP-C12-Checkbox-v01.png` | `90458c5e742414e0162bcd2a15af7a8e74f328583da7cbb1d361288ed80f002c` | VIGENTE | Versão inicial |
| 15/11/2026 | C13 | v01 | `COMP-C13-Switch-v01.png` | `c1e9654bd1052a45b6c21980b21e668e1bce0965dce9713fc30a76716f9347d0` | VIGENTE | Versão inicial |
| 15/11/2026 | C13 | v01 | `COMP-C13-Switch-v01_Ligado.png` | `4e2b1cb768f2f9c15791ece6af1269cddf2ea91f5387db41d912afe7d0a127e3` | VIGENTE | Estado do C13 para mostrar o comportamento |
| 15/11/2026 | C14 | v01 | `COMP-C14-StatusBadge-v01.png` | `4e4d012a5bd39f77f56fe54bf92b90743f1e0fbd1e258ed8b74f8526e477fb14` | VIGENTE | Versão inicial |
| 15/11/2026 | C15 | v01 | `COMP-C15-MetricCard-v01.png` | `23e2f03fe0a4840b837daf3cbe7e0351ac2f921f7b3c0aec5847be90ead404d9` | VIGENTE | Versão inicial |
| 15/11/2026 | C15.1 | v01 | `COMP-C15.1-MetricCardSubcaption-v01.png` | `5959d5fb49a3f4d57c9b0c74d443c3dca7bb2e316fbc11062e7d61d634662fb6` | VIGENTE | Versão inicial |
| 15/11/2026 | C16 | v01 | `COMP-C16-ClientCard-v01.png` | `d5b9d00f231961cdf1fe63b91307fb6f97f261c12dd4e48d935cfe2cc0744f18` | VIGENTE | Versão inicial |
| 15/11/2026 | C16.1 | v01 | `COMP-C16.1-ClientCardSelectable-v01.png` | `91ee51bb3e29a3ade4b0c551ba1270f95d27c35bac4d6a0393f24f101aec6801` | VIGENTE | Versão inicial |
| 15/11/2026 | C16.1 | v01 | `COMP-C16.1-ClientCardSelectable-v01_Selecionado.png` | `05025ee6d8ee8dd09c267324107ce63b6fd50cd02bb9e50c5f7ca7051f906d1a` | VIGENTE | Estado do C16.1 para mostrar o comportamento |
| 15/11/2026 | C16.2 | v01 | `COMP-C16.2-ClientCardDisabled-v01.png` | `2ce5562bb956c7ac1262c8e39387197f553bfe8c99acc58bfa9de6efa55647c3` | VIGENTE | Versão inicial |
| 15/11/2026 | C17 | v01 | `COMP-C17-ProspectCard-v01.png` | `f023ecc3f6b8e448d51b2aa2ee0ef832a4c005423b319190cd2734f2c44dc3f9` | VIGENTE | Versão inicial |
| 15/11/2026 | C17.1 | v01 | `COMP-C17.1-ProspectCardSelectable-v01.png` | `f822bc40c9869cb45e2f9e03de9f5279bc0ea1f1ec376f53f2895ed6e758a584` | VIGENTE | Versão inicial |
| 15/11/2026 | C17.1 | v01 | `COMP-C17.1-ProspectCardSelectable-v01_Selecionado.png` | `8f6d172349506e212ca4c1af92e3eadf7c20301073d92e7f521a1d614912722c` | VIGENTE | Estado do C17.1 para mostrar o comportamento |
| 15/11/2026 | C17.2 | v01 | `COMP-C17.2-ProspectCardDisabled-v01.png` | `759cb89393059e32fdfc4694740677c70b7355a56eb44d0223879c77d5a09777` | VIGENTE | Versão inicial |
| 15/11/2026 | C18 | v01 | `COMP-C18-ProductCard-v01.png` | `790b62c62d3210ade7e69228cd724e0a7c53b4fb0cc347a77ecbe5a6901fcbe8` | VIGENTE | Versão inicial |
| 15/11/2026 | C18.1 | v01 | `COMP-C18.1-ProductCardUnavailable-v01.png` | `bbe292b94f1aa016cda5d62c7ac77f683eef7e60300c8112ebc4f0915375628a` | VIGENTE | Versão inicial |
| 15/11/2026 | C18.2 | v01 | `COMP-C18.2-ProductOrderItem-v01.png` | `2c0a12789e1b10d8e4b413bd2941d9ec665febc45b967720b1801ce29c194b02` | VIGENTE | Versão inicial |
| 15/11/2026 | C18.3 | v01 | `COMP-C18.3-ProductOrderItemNoSku-v01.png` | `06ca2e3af4d80899a1e051493cd4a7a35781500ec5e84956a74ceefa950e5e9c` | VIGENTE | Versão inicial |
| 15/11/2026 | C19 | v01 | `COMP-C19-OrderCard-v01.png` | `905022ac661bc85aba3432d8fb508e6f81a871561db6186fbefb193dc019d7c2` | VIGENTE | Versão inicial |
| 15/11/2026 | C20 | v01 | `COMP-C20-VisitCard-v01.png` | `34899eb7d5a77b3a0776541e96d4b83e0f809ee194c6c129154f986272ca07c4` | VIGENTE | Versão inicial |
| 15/11/2026 | C21 | v01 | `COMP-C21-QuantitySelector-v01.png` | `5c15da09ede940ea0aaf01c0eced6c1b553818ec187f5d984d67d325e82c190d` | VIGENTE | Versão inicial |
| 15/11/2026 | C21 | v01 | `COMP-C21-QuantitySelector-v01_Minimo.png` | `6371c83bb3899df9c9043aa41c29ad53ca548202bdbb6fde64bab8291267f3e4` | VIGENTE | Estado do C21 para mostrar o comportamento |
| 15/11/2026 | C22 | v01 | `COMP-C22-FilterChip-v01.png` | `477a0fc684a4cf866fa91b35e3f7ad6626a2d9c7881637ceeeb502c7530ccc4c` | VIGENTE | Versão inicial |
| 15/11/2026 | C22 | v01 | `COMP-C22-FilterChip-v01_Selecionado.png` | `dcb66aac4ebafe086c7ea405b6ec3a397eff16ccddf1c9e59332cc3038d45305` | VIGENTE | Estado do C22 para mostrar o comportamento |
| 15/11/2026 | C23 | v01 | `COMP-C23-Stepper-v01.png` | `87df617426969c7251482a4a923c23bc4c4a77ac8610e621927c99af6c6f3e83` | VIGENTE | Versão inicial |
| 15/11/2026 | C23 | v01 | `COMP-C23-Stepper-v01_Etapa1.png` | `1e94d760d9a27a3e015845d821afdf3c17103b35c15196118fe35e6168811330` | VIGENTE | Estado do C23 para mostrar o comportamento |
| 15/11/2026 | C23 | v01 | `COMP-C23-Stepper-v01_Etapa4.png` | `c87e9612b85ed68913b1e40f792ad528228df60178a3f1ba25fc08f8be3c292c` | VIGENTE | Estado do C23 para mostrar o comportamento |
| 15/11/2026 | C24 | v01 | `COMP-C24-StatusTimeline-v01.png` | `e38fb8b984debc4887de7298978fdd4849e9599da5305ef7d06c15e8313eccac` | VIGENTE | Versão inicial |
| 15/11/2026 | C24 | v01 | `COMP-C24-StatusTimeline-v01_Etapa1.png` | `08fd178b7abfd1011774e462b2858467da320d337bfdeb51f54db96ddea5cd9b` | VIGENTE | Estado do C24 para mostrar o comportamento |
| 15/11/2026 | C24 | v01 | `COMP-C24-StatusTimeline-v01_Etapa5.png` | `cd1b8ece9864aaa344dff78f181efe72a3d746b6451db36dbf69607b8da3a553` | VIGENTE | Estado do C24 para mostrar o comportamento |
| 15/11/2026 | C25 | v01 | `COMP-C25-Dialog-v01.png` | `bb8901fe46b29e5ae8d37a2594132078c4fdbd376f3b21a150b4d7eaae9d17df` | VIGENTE | Versão inicial |
| 15/11/2026 | C26 | v01 | `COMP-C26-BottomSheet-v01.png` | `b47c99c3934d3acdcf3293665546b119d1b3f348c3a8f451d265aadeca8d052a` | VIGENTE | Versão inicial |
| 15/11/2026 | C30 | v01 | `COMP-C30-SyncStatus-v01.png` | `a2ddfe3116d7b59e3f0296a8746e8ee0fbd6fb6dd1786e3087716e568413000c` | VIGENTE | Versão inicial |
| 15/11/2026 | C30.1 | v01 | `COMP-C30.1-SyncStatusDetail-v01.png` | `5e2884d805018245ba4f940f73507d18f79beac1a9906d8398590dd96ad5643c` | VIGENTE | Versão inicial |
| 15/11/2026 | C31 | v01 | `COMP-C31-MoneyDisplay-v01.png` | `9c1316fcc4d8b5fcc2c8286a15d4f1145a49864b9963be953cd8654aa944a70d` | VIGENTE | Versão inicial |
| 15/11/2026 | C31.1 | v01 | `COMP-C31.1-MoneyDisplayInline-v01.png` | `d8df508642def0d8ff6955f521577e7560675fcd79627926d5cad23928519bc4` | VIGENTE | Versão inicial |
| 15/11/2026 | C32 | v01 | `COMP-C32-SectionHeader-v01.png` | `52fc2e8a1a0164fca68922a9909a96a7504938c638dfd4e23090f75a74fc076f` | VIGENTE | Versão inicial |
| 15/11/2026 | C32.1 | v01 | `COMP-C32.1-SectionHeaderIcon-v01.png` | `7d51275960e17423179825f93bb0e31f97e47ae91ca1a052232a87fe99c0a4a8` | VIGENTE | Versão inicial |
| 15/11/2026 | C33 | v01 | `COMP-C33-AddressCard-v01.png` | `6c79ee2c705853e0716bd06e92c53318a269fe71c9c1f91b7c1600ac9e5a0686` | VIGENTE | Versão inicial |
| 15/11/2026 | C33 | v01 | `COMP-C33-AddressCard-v01_Selecionado.png` | `2361c541759aca46e48d5e9ee6de440c319301af2f7475309adf4d1d2873e648` | VIGENTE | Estado do C33 para mostrar o comportamento |
| 15/11/2026 | C33.1 | v01 | `COMP-C33.1-AddressCardSummary-v01.png` | `a93bbd05939c8434cf1b3d3e6c792e5ed4427ae7c830f1b2e08785e03fa34bdf` | VIGENTE | Versão inicial |
| 15/11/2026 | C33.2 | v01 | `COMP-C33.2-AddressCardDetail-v01.png` | `7ffa1b6590f5b701eacd77c1e2378a0d30f467a7356b6e08170e6ed800f773d9` | VIGENTE | Versão inicial |
| 15/11/2026 | C33.3 | v01 | `COMP-C33.3-AddressMap-v01.png` | `440cf5e8fddfd0df1fdfd056be0bd16b7ce8b08e39bd4d833f45cccb70c082ad` | VIGENTE | Versão inicial |
| 15/11/2026 | C35 | v01 | `COMP-C35-ThemeSelector-v01.png` | `8c000809c6d60288e60bfaa6929c2e7bf5beb629a5b294862931fa4efc8ab314` | VIGENTE | Versão inicial |
| 15/11/2026 | C36 | v01 | `COMP-C36-ThemePreview-v01.png` | `e40bf20e3974dc6f7b61779c49eb5ef863a26708649c0557c191be1c30f45f82` | VIGENTE | Versão inicial |
| 15/11/2026 | C37 | v01 | `COMP-C37-ConnectionStatus-v01.png` | `d2464f3b998064acfb1a5450b8eea1b0b0dc00ff49157f7f244ae523fc263c4d` | VIGENTE | Versão inicial |
| 15/11/2026 | C38 | v01 | `COMP-C38-ApiConfigurationForm-v01.png` | `fa9d389ca3c07b281f83825296576a9a698c5d0801e359bc714cad98fc1f9b0f` | VIGENTE | Versão inicial |
| 15/11/2026 | C39 | v01 | `COMP-C39-SecretInput-v01.png` | `c8ed761aae89406b55c1d3ea1856d6c5559c605356ae7dd4c66a09eba9cde377` | VIGENTE | Versão inicial |
| 15/11/2026 | C40 | v01 | `COMP-C40-ConnectionTest-v01.png` | `2aa8b11bfd742aa245d54155fea756f4fd30ff465ffea89898e78bde3ea0f6b9` | VIGENTE | Versão inicial |
| 15/11/2026 | C41 | v01 | `COMP-C41-DiagnosticsItem-v01.png` | `4b72d479d380f637de63dc6d413644a2a29c8ef0c78a0ce7ceaa6b5cf7479a85` | VIGENTE | Versão inicial |
| 15/11/2026 | C42 | v01 | `COMP-C42-SettingsGroup-v01.png` | `e064f094dfb9346d9e074d30af6d24e9e7a6baca4949db3a6eb03a2193e6bbcc` | VIGENTE | Versão inicial |
| 15/11/2026 | C43 | v01 | `COMP-C43-SettingsItem-v01.png` | `594cb0ed7e9c94b6c509ffbdb6b26223faf2d42a3cd57b1c050f404eda0ca374` | VIGENTE | Versão inicial |
| 15/11/2026 | C43.1 | v01 | `COMP-C43.1-SettingsItemBadge-v01.png` | `06c6f3f56ea0ff1c736c84be86c802ae5cc185594e2749b5d76094642e7121bd` | VIGENTE | Versão inicial |
| 15/11/2026 | C43.2 | v01 | `COMP-C43.2-SettingsItemDestructive-v01.png` | `309f7182e431288ad026bd1c5195f1dc7f4c5d4ab5efa1f77c556c72226e263d` | VIGENTE | Versão inicial |
| 15/11/2026 | C44 | v01 | `COMP-C44-ConnectionBadge-v01.png` | `d724b68dd3f6980ca15c261a039d32aa506572f248846cf766d0127cc168c283` | VIGENTE | Versão inicial |
| 15/11/2026 | C27 | v01 | `COMP-C27-EmptyState-v01.png` | `40075176de8274da45cdeeef6dd6716c4b724ae9cf259e402ef0e651849f1518` | VIGENTE | Versão inicial |
| 15/11/2026 | C28 | v01 | `COMP-C28-ErrorState-v01.png` | `be8a07d69454f233d310fc54ea729b3ea082a8083d35354550d3e836a45597b6` | VIGENTE | Versão inicial |
| 15/11/2026 | C29 | v01 | `COMP-C29-LoadingState-v01.png` | `2d5262c5927c98dcfdc18270e2b23c9b45ddf6f76de1a4b0665fd315db0b132a` | VIGENTE | Versão inicial |
| 15/11/2026 | C29.1 | v01 | `COMP-C29.1-LoadingStateCard-v01.png` | `1e0dbb48dc0a88f89f8fae4267eaee18fb4178dcb04471c64c3f458ff1bdee08` | VIGENTE | Versão inicial |
| 15/11/2026 | C34 | v01 | `COMP-C34-ContactCard-v01.png` | `8137c337d3d40ac16277a12d6e63f27d99118e450ceff1679e2c98139b4bb9e7` | VIGENTE | Versão inicial |
| 15/11/2026 | C34.1 | v01 | `COMP-C34.1-ContactCardDetail-v01.png` | `1246c60336c136b1c6eef1cc0fdbd2923d1f7e4a77809a789c53bab5d980e56e` | VIGENTE | Versão inicial |
| 15/11/2026 | C34.2 | v01 | `COMP-C34.2-ProfileHeader-v01.png` | `e1e03c6311292e0e6dd438a7e793d968fbbcfccd269eb2e2c7ddc7debff76aa5` | VIGENTE | Versão inicial |
| 15/11/2026 | C19.1 | v01 | `COMP-C19.1-OrderCardByClient-v01.png` | `9d61a31bea3b788548f23661dadfacdb7d005220140d09d2fa5f76fc9c6890aa` | VIGENTE | Versão inicial |
| 15/11/2026 | C19.2 | v01 | `COMP-C19.2-OrderCardByCustomer-v01.png` | `66bae8d1f03ed87b93b93cf6e9860af6da03d652ed3c4842af18cbb03f9cf55c` | VIGENTE | Versão inicial |
| 15/11/2026 | C20.1 | v01 | `COMP-C20.1-VisitHistoryItem-v01.png` | `94f72bb421d079477256b1318b3e333d0a2a6ec31174271635fc1b560e0e91fd` | VIGENTE | Versão inicial |

Situação: `VIGENTE`, `SUBSTITUÍDA por vNN` ou `RETIRADA (motivo)`.

---

## 6. Procedimentos

**Registrar um componente novo**
1. Conferir na seção 7 que ele é do catálogo e ainda não existe. Se for `Montar`, parar.
2. Gerar o arquivo com o nome da seção 2, no tamanho exato do componente, escala 1:1.
3. Abrir a imagem e inspecionar: nada cortado, nada de elemento vizinho.
4. Calcular o SHA-256 e regenerar o `SHA256SUMS` (seção 4).
5. Registrar: seção 3 (arquivo, versão, dimensões, aprovação `PENDENTE`), seção 3.1 (especificação), seção 5 (linha `VIGENTE` com data, hash e motivo) e seção 7 (situação `Existe` e Feito ✅).
6. Entregar ao responsável. A aprovação só muda para `APROVADO` com a data e a hora da decisão dele.

**Mudar a versão:** gerar a versão seguinte sem sobrescrever a anterior; na seção 5, mudar a linha antiga para `SUBSTITUÍDA por vNN` e acrescentar a nova como `VIGENTE`, com data, hash e motivo; atualizar as seções 3 e 3.1; registrar a nova aprovação.

**Retirar:** na seção 5, marcar a linha como `RETIRADA (motivo)` e remover da seção 3.

---

## 7. Catálogo e situação

- **Feito** (✅): a imagem vigente já foi criada nesta pasta (situação `Existe`); ⬜ = ainda não feita.
- **Existe**: há imagem vigente aqui · **Extraível**: aparece em tela aprovada, sem imagem aqui · **Parcial**: existe só dentro de uma tela, precisa ser isolado e verificado · **Montar**: sem tela aprovada que o defina; **não criar** até a tela ser aprovada.
- A classificação veio das telas aprovadas; confirmar na imagem antes de produzir.

| ID | Componente | Situação | Feito |
| --- | --- | --- | --- |
| C01 | AppHeader | Existe | ✅ |
| C01.1 | AppHeaderBack (variante do C01) | Existe | ✅ |
| C02 | BottomNavigation | Existe | ✅ |
| C03 | PrimaryButton | Existe | ✅ |
| C04 | SecondaryButton | Existe | ✅ |
| C05 | TextButton | Existe | ✅ |
| C06 | TextInput | Existe | ✅ |
| C06.1 | TextInputShort (variante do C06) | Existe | ✅ |
| C06.2 | TextInputWithButton (variante do C06) | Existe | ✅ |
| C07 | SearchInput | Existe | ✅ |
| C08 | SelectInput | Existe | ✅ |
| C09 | DateInput | Existe | ✅ |
| C09.1 | DatePickerCalendar (variante do C09) | Existe | ✅ |
| C10 | TimeInput | Existe | ✅ |
| C11 | TextArea | Existe | ✅ |
| C12 | Checkbox | Existe | ✅ |
| C13 | Switch | Existe | ✅ |
| C14 | StatusBadge | Existe | ✅ |
| C15 | MetricCard | Existe | ✅ |
| C15.1 | MetricCardSubcaption (variante do C15) | Existe | ✅ |
| C16 | ClientCard | Existe | ✅ |
| C16.1 | ClientCardSelectable (variante do C16) | Existe | ✅ |
| C16.2 | ClientCardDisabled (variante do C16) | Existe | ✅ |
| C17 | ProspectCard | Existe | ✅ |
| C17.1 | ProspectCardSelectable (variante do C17) | Existe | ✅ |
| C17.2 | ProspectCardDisabled (variante do C17) | Existe | ✅ |
| C18 | ProductCard | Existe | ✅ |
| C18.1 | ProductCardUnavailable (variante do C18) | Existe | ✅ |
| C18.2 | ProductOrderItem (variante do C18) | Existe | ✅ |
| C18.3 | ProductOrderItemNoSku (variante do C18) | Existe | ✅ |
| C19 | OrderCard | Existe | ✅ |
| C19.1 | OrderCardByClient (variante do C19) | Existe | ✅ |
| C19.2 | OrderCardByCustomer (variante do C19) | Existe | ✅ |
| C20 | VisitCard | Existe | ✅ |
| C20.1 | VisitHistoryItem (variante do C20) | Existe | ✅ |
| C21 | QuantitySelector | Existe | ✅ |
| C22 | FilterChip | Existe | ✅ |
| C23 | Stepper | Existe | ✅ |
| C24 | StatusTimeline | Existe | ✅ |
| C25 | Dialog | Existe | ✅ |
| C26 | BottomSheet | Existe | ✅ |
| C27 | EmptyState | Existe | ✅ |
| C28 | ErrorState | Existe | ✅ |
| C29 | LoadingState | Existe | ✅ |
| C29.1 | LoadingStateCard (variante do C29) | Existe | ✅ |
| C30 | SyncStatus | Existe | ✅ |
| C30.1 | SyncStatusDetail (variante do C30) | Existe | ✅ |
| C31 | MoneyDisplay | Existe | ✅ |
| C31.1 | MoneyDisplayInline (variante do C31) | Existe | ✅ |
| C32 | SectionHeader | Existe | ✅ |
| C32.1 | SectionHeaderIcon (variante do C32) | Existe | ✅ |
| C33 | AddressCard | Existe | ✅ |
| C33.1 | AddressCardSummary (variante do C33) | Existe | ✅ |
| C33.2 | AddressCardDetail (variante do C33) | Existe | ✅ |
| C33.3 | AddressMap (variante do C33) | Existe | ✅ |
| C34 | ContactCard | Existe | ✅ |
| C34.1 | ContactCardDetail (variante do C34) | Existe | ✅ |
| C34.2 | ProfileHeader (variante do C34) | Existe | ✅ |
| C35 | ThemeSelector | Existe | ✅ |
| C36 | ThemePreview | Existe | ✅ |
| C37 | ConnectionStatus | Existe | ✅ |
| C38 | ApiConfigurationForm | Existe | ✅ |
| C39 | SecretInput | Existe | ✅ |
| C40 | ConnectionTest | Existe | ✅ |
| C41 | DiagnosticsItem | Existe | ✅ |
| C42 | SettingsGroup | Existe | ✅ |
| C43 | SettingsItem | Existe | ✅ |
| C43.1 | SettingsItemBadge (variante do C43) | Existe | ✅ |
| C43.2 | SettingsItemDestructive (variante do C43) | Existe | ✅ |
| C44 | ConnectionBadge | Existe | ✅ |

Catálogo C01–C44: **44 Existe · 0 Extraível · 0 Parcial · 0 Montar** (as variantes não entram na contagem).

---

## 8. Documentos relacionados

| Documento | Para quê |
| --- | --- |
| `docs/Documento_Mestre.md` §20 | catálogo oficial C01–C44 |
| `.specs/wireframes/PROCESSO-TELA-PRANCHA.md` | pastas, nomes e Gates das telas |
| `.specs/wireframes/REGRAS-TECNICAS.md` | tokens, componentes técnicos, acessibilidade |
| `docs/wireframes/images/Registro_Padrao_Visual_Funcional_Mobile.md` | perfil visual funcional vigente (Mobile v02) |

**Pendência estrutural:** a pasta `componentes/` ainda não consta na SPEC 3 nem em `docs/wireframes/images/README.md`; registrar ali é etapa posterior, a decidir pelo responsável, para o auditor não tratá-la como fora do padrão.
