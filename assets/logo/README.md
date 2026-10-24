# SaOr - Sales Order
## Catálogo de identidade visual — Logo e ícone

**Diretório oficial:** `assets/logo`  
**Status:** referência visual catalogada  
**Arquivo vetorial mestre do ícone:** `saor-icon-master.svg`

---

# 1. Finalidade

Este documento cataloga os artefatos de logo e ícone do **SaOr - Sales Order** existentes no repositório.

Seu objetivo é impedir uso ambíguo, alteração acidental ou escolha incorreta de variantes durante as etapas de Wireframe, Design Visual, Figma, apresentações e implementação.

Este catálogo não substitui um futuro manual completo de identidade visual. Regras que ainda não foram formalmente definidas — como área mínima de proteção, tamanho mínimo de reprodução ou tipografia oficial da marca — não devem ser inventadas nesta etapa.

---

# 2. Arquivo mestre

## `saor-icon-master.svg`

Arquivo vetorial mestre atualmente disponível para o ícone do SaOr.

Características comprovadas diretamente no SVG:

```text
viewBox: 0 0 833 748
cor estrutural escura: #0F172A
cor de destaque:       #2563EB
```

O SVG contém o monograma geométrico do SaOr com acento gráfico direcional.

Regras:

- preservar a geometria original;
- preservar a proporção;
- não redesenhar o símbolo a partir de PNG;
- não substituir o SVG mestre por uma rasterização;
- não alterar cores, formas ou proporções sem decisão explícita na etapa apropriada;
- quando for necessário derivar novos tamanhos ou formatos, usar o arquivo mestre como origem sempre que tecnicamente possível.

---

# 3. Arquivos catalogados

| Arquivo | Categoria | Uso catalogado |
|---|---|---|
| `saor-icon-master.svg` | Ícone / mestre vetorial | Fonte vetorial mestre do ícone |
| `saor-icon-para_fundos_claros.png` | Ícone | Variante preparada para aplicação sobre fundos claros |
| `saor-icon-para_fundos_escuros.png` | Ícone | Variante preparada para aplicação sobre fundos escuros |
| `saor-icon-modelo-com_fundos_claro.png` | Referência visual | Modelo de visualização do ícone em contexto de fundo claro |
| `saor-icon-modelo-com_fundos_escuros.png` | Referência visual | Modelo de visualização do ícone em contexto de fundo escuro |
| `saor-logo-para_fundos_claros.png` | Logo completa | Variante preparada para aplicação sobre fundos claros |
| `saor-logo-para_fundos_escuros.png` | Logo completa | Variante preparada para aplicação sobre fundos escuros |
| `saor-logo-modelo-com_fundos_claro.png` | Referência visual | Modelo de visualização da logo em contexto de fundo claro |
| `saor-logo-modelo-com_fundos_escuros.png` | Referência visual | Modelo de visualização da logo em contexto de fundo escuro |

Os arquivos classificados como **modelo de visualização** servem como referência de aplicação. Para inserção direta em uma interface, deve-se preferir a variante indicada como **para fundos claros** ou **para fundos escuros**, conforme o contexto.

---

# 4. Cores comprovadas do ícone mestre

As seguintes cores estão codificadas no arquivo `saor-icon-master.svg`:

| Referência | HEX | Origem |
|---|---|---|
| Estrutura principal | `#0F172A` | `fill` do caminho estrutural do SVG mestre |
| Destaque | `#2563EB` | `fill` do caminho de destaque do SVG mestre |

Estas cores são registradas porque estão objetivamente presentes no arquivo mestre.

Este registro não deve ser interpretado, por si só, como definição completa da paleta do produto ou do Design System. A paleta de interface possui processo próprio de definição e validação.

---

# 5. Uso em fundos claros e escuros

Quando uma interface utilizar a identidade do SaOr:

- em fundo claro, utilizar a variante explicitamente preparada para **fundos claros**;
- em fundo escuro, utilizar a variante explicitamente preparada para **fundos escuros**;
- não inverter cores manualmente;
- não aplicar filtros automáticos;
- não gerar uma nova variante quando já existir um arquivo correspondente;
- não utilizar o arquivo de modelo como substituto automático da variante de aplicação.

A escolha entre **ícone** e **logo completa** deve decorrer da necessidade real da interface e da documentação correspondente. A presença da identidade visual não autoriza inserir branding em telas que não o exijam.

---

# 6. Tipografia da marca

A tipografia oficial da marca **está definida neste catálogo**.

Não deve ser inferida a partir dos arquivos PNG ou reconstruída visualmente por aproximação.

A tipografia oficial da identidade está definida conforme:

```text
Família:
- Google Sans
- Quicksand

Peso(s):
- Google Sans: Bold 700
- Quicksand: Regular 400

Estilo(s):
- Normal

Uso:
- SaOr: Google Sans Bold 700
- SALES ORDER: Quicksand Regular 400, uppercase, tracking ampliado

Licenciamento:
- Google Sans: fonte proprietária do Google, sujeita aos termos de licenciamento e uso da família tipográfica.
- Quicksand: SIL Open Font License 1.1 (OFL)

Fonte oficial do arquivo:
- Google Sans: Google / arquivo oficial autorizado da família tipográfica
- Quicksand: Google Fonts / repositório oficial google/fonts
```

Qualquer tipografia usada nos wireframes pertence exclusivamente à especificação técnica de wireframe e não deve ser considerada tipografia oficial da marca, salvo quando expressamente especificada neste catálogo.

---

# 7. Preservação

Os arquivos de identidade existentes devem ser tratados como artefatos oficiais do projeto.

Qualquer mudança de:

- geometria;
- proporção;
- cores;
- composição;
- nomenclatura;
- variante de fundo;
- tipografia da marca;

deve ser uma decisão explícita e documentada.

Nenhum wireframe ou etapa posterior deve sobrescrever silenciosamente os arquivos originais da identidade.
