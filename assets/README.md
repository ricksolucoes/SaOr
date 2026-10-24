# SaOr - Sales Order
## Índice e governança de ativos

**Diretório:** `assets/`  
**Finalidade:** centralizar ativos visuais, tipográficos, audiovisuais e referências canônicas utilizadas pelo projeto.

---

## 1. Estrutura atual

```text
assets/
├── README.md
├── logo/
│   └── README.md
├── fonts/
│   └── logo/
│       └── README.md
├── video/
│   └── intro/
│       └── README.md
└── Atendente_Virtual/
    └── Apozeu/
        └── README.md
```

Os arquivos binários existentes permanecem nos respectivos diretórios e não são duplicados neste índice.

---

## 2. Catálogo dos conjuntos

| Diretório | Conteúdo | Documento de referência |
|---|---|---|
| `logo/` | ícone mestre, variantes de ícone e logo para fundos claros/escuros e modelos de referência | [`logo/README.md`](logo/README.md) |
| `fonts/logo/` | pacote das famílias tipográficas associadas à identidade da marca | [`fonts/logo/README.md`](fonts/logo/README.md) |
| `video/intro/` | vídeos de introdução em formatos horizontal e vertical | [`video/intro/README.md`](video/intro/README.md) |
| `Atendente_Virtual/Apozeu/` | pranchas canônicas e Character Bible do atendente virtual Apozeu | [`Atendente_Virtual/Apozeu/README.md`](Atendente_Virtual/Apozeu/README.md) |

---

## 3. Regra de autoridade

Cada conjunto possui documentação local responsável por suas regras específicas.

Este `assets/README.md` funciona somente como índice e camada de governança. Em caso de dúvida:

1. consultar o documento específico do conjunto;
2. preservar o arquivo canônico indicado nesse documento;
3. não inferir novas variantes, regras ou finalidades apenas pelo nome de um arquivo;
4. não substituir silenciosamente um ativo aprovado;
5. registrar formalmente qualquer mudança que altere identidade, finalidade ou referência canônica.

---

## 4. Separação entre ativo e Design System

A presença de um ativo em `assets/` não o transforma automaticamente em token, componente ou regra do futuro Design System.

Exemplos:

- as cores presentes na logo pertencem à identidade da marca e não definem sozinhas a paleta completa da interface;
- as fontes da logo não definem automaticamente a tipografia dos wireframes ou do produto;
- os vídeos de introdução são ativos audiovisuais, não especificações de navegação;
- as pranchas de Apozeu definem a identidade do personagem, não autorizam sua inserção em qualquer interface sem necessidade documentada.

---

## 5. Preservação e versionamento

Ativos canônicos devem ser preservados.

Ao adicionar um novo conjunto relevante de ativos:

- criar documentação local quando houver regras próprias de uso;
- adicionar o conjunto a este índice;
- atualizar o `README.md` principal quando a nova categoria tiver relevância para descoberta do projeto;
- evitar documentação duplicada entre níveis;
- manter nomes de diretórios e arquivos estáveis após passarem a ser referenciados por documentação ou código.

Alterações puramente internas de um conjunto não exigem replicação de detalhes no README principal.
