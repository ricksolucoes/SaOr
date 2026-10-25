# Wireframes — Regras técnicas canônicas

## 1. Escopo

Esta spec define as regras técnicas invariantes da representação de wireframes.

Ela não define a composição específica de uma prancha-modelo.

## 2. Canvas

```text
Canvas: 1280 × 1920 px
Orientação: retrato
Margem horizontal estrutural: 12 px
```

## 3. Viewport

```text
Viewport lógico: 360 × 800 px
Orientação: retrato
Escala na prancha: 1:1
```

Regras obrigatórias:

- o viewport deve medir fisicamente `360 × 800 px`;
- não redimensionar, esticar, comprimir ou reproporcionar;
- não criar área funcional fora dos `800 px`;
- não desenhar moldura física de aparelho;
- não criar versão específica para iOS ou Android;
- uma legenda de dimensão não substitui a verificação física.

### 3.1 Referência de demonstração

Para pranchas-modelo neutras:

```text
docs/wireframes/images/templates/references/WF-VIEWPORT-360x800-clean.png
```

Pode ser inserido diretamente em `100%` e deve permanecer `360 × 800 px`.

### 3.2 Cotas

Referência:

```text
docs/wireframes/images/templates/references/Especificação Técnica do Viewport Mobile.png
```

Cotas vigentes:

```text
largura total:             360 px
largura útil:              336 px
margem lateral esquerda:    12 px
margem lateral direita:     12 px
altura total:              800 px

12 + 336 + 12 = 360
```

### 3.3 Safe area

Não existe reserva fixa de faixa superior ou inferior de safe area nesta etapa.

Não reservar automaticamente `24 px` no topo ou `32 px` na base.

## 4. Grid e spacing

```text
Base: 4 px
Escala: 4 / 8 / 12 / 16 / 24 / 32 px
Padding-base horizontal: 16 px
Padding-base vertical: 12 px
```

Espaçamento fora dessa escala exige necessidade objetiva registrada no Wireframe Text específico.

## 5. Tipografia técnica

```text
Família: Inter
```

| Token | Peso | Tamanho | Line-height |
|---|---:|---:|---:|
| `WF-TITLE` | 600 | 20 px | 28 px |
| `WF-SECTION` | 600 | 14 px | 20 px |
| `WF-BODY` | 400 | 16 px | 24 px |
| `WF-LABEL` | 500 | 14 px | 20 px |
| `WF-ACTION-TEXT` | 500 | 16 px | 24 px |
| `WF-CAPTION` | 400 | 12 px | 16 px |

Inter é tipografia técnica e não substitui a tipografia oficial da marca.

## 6. Tokens técnicos

### Claro

| Token | HEX |
|---|---|
| `WF-W-BG` | `#F4F4F4` |
| `WF-W-SURFACE` | `#FFFFFF` |
| `WF-W-SURFACE-ALT` | `#EAEAEA` |
| `WF-W-BORDER` | `#B5B5B5` |
| `WF-W-TEXT` | `#1A1A1A` |
| `WF-W-TEXT-2` | `#565656` |
| `WF-W-ACTION` | `#333333` |
| `WF-W-DISABLED` | `#9A9A9A` |
| `WF-W-FOCUS` | `#4A4A4A` |
| `WF-W-STATUS` | `#626262` |

### Escuro

| Token | HEX |
|---|---|
| `WF-B-BG` | `#121212` |
| `WF-B-SURFACE` | `#1E1E1E` |
| `WF-B-SURFACE-ALT` | `#2A2A2A` |
| `WF-B-BORDER` | `#5E5E5E` |
| `WF-B-TEXT` | `#F2F2F2` |
| `WF-B-TEXT-2` | `#C2C2C2` |
| `WF-B-ACTION` | `#E0E0E0` |
| `WF-B-DISABLED` | `#777777` |
| `WF-B-FOCUS` | `#D0D0D0` |
| `WF-B-STATUS` | `#A8A8A8` |

Cor nunca pode ser o único indicador de estado.

## 7. Componentes técnicos

| Elemento | Especificação |
|---|---|
| App Bar | `56 px` |
| Touch target | mínimo `48 × 48 px` |
| Campo Outlined | `56 px`, radius `12 px`, borda `1 px` quando aplicável |
| Botão textual | altura mínima `48 px`, radius `12 px` |
| Icon Button | touch target mínimo `48 × 48 px` |
| Item simples | mínimo `56 px` |
| Item com secundário/status | mínimo `64 px` |
| Card | radius `16 px`, borda `1 px` quando necessária |
| Modal/Dialog | margem lateral `24 px`, radius `16 px` |
| Bottom Navigation | `64 px` quando prevista na baseline |

## 8. Bordas, radius e elevação

```text
Bordas: 1 px quando necessárias
Divisores: 1 px
Campos/botões: radius 12 px
Cards/modais: radius 16 px
```

Elevação:

```text
WF-ELEVATION-0: 0 / 0 / 0 / 0%
WF-ELEVATION-1: 0 / 1 / 2 / 12%
WF-ELEVATION-2: 0 / 2 / 6 / 16%
WF-ELEVATION-3: 0 / 4 / 12 / 20%
```

Ordem:

```text
offset-x / offset-y / blur / opacidade
```

## 9. Iconografia

```text
Referência: Material Icons Outlined
Auxiliar: 20 px
Ação/navegação: 24 px
Touch target: mínimo 48 × 48 px
```

## 10. Estados

```text
default
focus
pressed / selected
disabled
error
hover
```

`hover` é documentado, mas não é obrigatório em prancha mobile sem necessidade específica.

## 11. Acessibilidade estrutural

A composição deve preservar:

- cor nunca como único indicador;
- touch target mínimo;
- ordem de leitura clara;
- campos com rótulos;
- erro próximo ao contexto;
- foco e seleção distinguíveis;
- hierarquia tipográfica consistente;
- ausência de compactação prejudicial.
