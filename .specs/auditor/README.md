# SaOr — Auditoria: índice canônico e limites de aplicação

## Finalidade desta área

A pasta `.specs/auditor/` organiza as normas de **auditoria de conformidade e integridade**. Seu núcleo é genérico e reutilizável: audita o resultado de qualquer etapa do SaOr com base nas **autoridades existentes** do domínio, sem inventar requisitos, alterar Gates ou depender de conversas anteriores.

A criação de uma norma nesta pasta **não significa** que já existe uma Skill instalada, um executor automatizado, integração por evento, contrato especializado publicado ou aprovação de encerramento. A existência e o estado desses recursos precisam ser verificados fisicamente em cada base.

## Autoridade principal

- [**`PROCESSO-AUDITORIA.md` — Processo genérico de auditoria**](PROCESSO-AUDITORIA.md): define o método obrigatório para identificar a fonte, selecionar normas, conferir integridade, estrutura, semântica, referências, hashes, versões, Gates, ocorrências, correções autorizadas, reauditoria e encerramento. Inclui contrato de entrada/saída, estados, critérios de evidência e matriz de cobertura da implantação.
- [**`../PROCESSO-ALTERACAO-ASSISTIDA.md` — Processo global de alteração**](../PROCESSO-ALTERACAO-ASSISTIDA.md): permanece superior para leitura contextual, autorização anterior a qualquer escrita, execução local, preservação, auditoria pós-alteração e entrega. A auditoria não concede autorização própria.
- [**`../README.md` — Índice das autoridades do projeto**](../README.md): fonte de navegação das SPECs existentes e de suas responsabilidades. Cada requisito técnico, funcional, editorial ou de Gate continua sob a norma do assunto.

Uma regra deve ter **uma autoridade normativa principal**. Este README é índice; não redefine o conteúdo da SPEC genérica, dos contratos dos domínios ou de qualquer Skill.

## Organização por domínio

```text
.specs/
└── auditor/
    ├── README.md
    ├── PROCESSO-AUDITORIA.md
    └── <dominio>/                 [somente quando formalmente criado]
        └── <contrato-especializado>.md
```

Os contratos especializados **não** devem copiar regras das SPECs responsáveis; devem indicar sua autoridade, condições de aplicação, método de coleta, evidência e teste. Uma auditoria de outro assunto usa o mesmo processo genérico e somente os contratos desse assunto que realmente estiverem aprovados. Não criar pastas vazias nem normas particulares para cada objeto.

**Verificação obrigatória da instalação:** antes de invocar um contrato de domínio, uma Skill ou um validador, confirmar sua existência física, versão, integridade e aprovação na base examinada. Contratos e ferramentas apenas planejados não são considerados instalados. A implantação pode ocorrer por Gates diferentes, sem antecipar requisitos ou declarar concluída uma etapa futura.

## Quando usar

| Momento | Procedimento |
|---|---|
| `SOB_DEMANDA` | Pode ser iniciado em qualquer estágio; audita obrigações já exigíveis, registra etapas futuras como pendentes e não presume fechamento |
| `ENCERRAMENTO` | Deve integrar, após autorização de alteração do processo responsável, o fechamento de cada SPEC/atividade concluída; somente termina com todas as condições de fechamento efetivamente comprovadas |
| Após ajuste autorizado | Reexecuta controles impactados e a auditoria pós-alteração, antes de qualquer entrega |

A auditoria não substitui os Gates do processo responsável nem antecipa aprovações humanas. Um arquivo contendo a SPEC não aciona automaticamente código: eventual integração e Skill operacional deverão ser implementadas e validadas nos Gates próprios.

## Política de identidade e preservação

- Ajustes autorizados nos bytes de uma **mesma versão formal** não criam uma nova versão nem um histórico artificial de hashes intermediários. As referências correntes passam a identificar os bytes finais depois da autorização e da reauditoria.
- Identidades necessárias para **comprovar submissões, decisões ou origens** mantêm sua função de evidência, sem serem classificadas automaticamente como versões históricas.
- Uma **transição formal de versão** exige a preservação da versão anterior e dos registros aplicáveis, conforme o contrato competente.
- Mudança de hash não autoriza reabrir nem ignorar Gate automaticamente. Objetos congelados exigem verificação de impacto e decisão conforme a norma responsável.
- `assets/` e materiais LEGADOS normativamente excluídos permanecem protegidos; GitHub é estritamente somente leitura.

Os critérios detalhados e suas exceções estão em [`PROCESSO-AUDITORIA.md`](PROCESSO-AUDITORIA.md), especialmente §§2, 5, 8, 9 e 11. O índice não constitui regra paralela.

## Condições de adoção

A produção normativa está sujeita a Gates bloqueantes: GVA-0 (inventário), **GVA-1 (SPEC genérica)**, GVA-2 (contrato de domínio), GVA-3 (Skill e integração), GVA-4 (executor), GVA-5 (testes), GVA-6 (consistência cruzada), GVA-7 (segunda auditoria) e GVA-8 (entrega/incorporação). A aprovação de um Gate **não autoriza** os seguintes.

Para aplicar a auditoria, identificar primeiro o ZIP/clone real, ler o processo global e as fontes competentes, selecionar o modo, produzir a matriz de requisitos e verificar evidências. Se a Skill de Auditoria ainda não estiver instalada, executar apenas as verificações comprovadamente disponíveis e registrar a limitação; nunca afirmar automação inexistente.

A criação, alteração ou implantação de normas, Skills e validadores exige escopo e autorização próprios. Nenhum Gate de construção dispensa a conferência da base física, a segunda auditoria, as preservações e o aceite humano correspondente.
