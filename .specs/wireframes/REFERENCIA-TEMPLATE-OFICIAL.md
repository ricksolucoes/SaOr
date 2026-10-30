# SaOr — SPEC 2: Prancha de Modelo (Template) — referência oficial selecionada

## 1. Responsabilidade e limites

Esta SPEC define **como identificar, comprovar a integridade e preservar a prancha de modelo selecionada como referência oficial vigente**, em `white` e `black`. **Não** define como construir uma prancha do zero (SPEC 1), o conteúdo das interfaces funcionais ou seu processo de produção (SPEC 3). A referência oficial é um resultado aprovado, não um segundo processo de desenho.

A autoridade permanente de definição técnica e construção de pranchas de template é [`PROCESSO-PRANCHA.md`](PROCESSO-PRANCHA.md), complementada por [`WIREFRAME-TEXT.md`](WIREFRAME-TEXT.md), [`MONTAGEM-IMAGEM.md`](MONTAGEM-IMAGEM.md) e [`REGRAS-TECNICAS.md`](REGRAS-TECNICAS.md). Esta SPEC **não reexecuta** os Gates de uma referência já aprovada.

## 2. Fonte única da seleção vigente

O registro canônico e genérico [`docs/wireframes/images/Registro_Controle_Template_Oficial.md`](../../docs/wireframes/images/Registro_Controle_Template_Oficial.md) é a **única fonte para modelo vigente, temas, versões aprovadas, hashes, origem, histórico de decisões e data de ativação**. Nenhum nome de arquivo, comentário, versão mais alta, imagem histórica, README ou memória de conversa pode selecionar implicitamente um modelo.

**Estado registrado na criação desta SPEC:** Modelo C, white `WF-TEMPLATE-C_v02` e black `WF-TEMPLATE-C_v01`, aprovado em 28/10/2026. Isso descreve a vigência atual; não torna o modelo imutável para sempre. Se o registro mudar formalmente, esta SPEC permanece válida sem renomeação.

## 3. Contrato obrigatório da referência oficial

Para cada tema, o registro deve identificar de forma inequívoca:

1. identificador do modelo, versão, tema e estado de vigência;
2. PNG da prancha, Wireframe Text de sua aprovação e PNG do ViewPort demonstrativo, com **caminhos completos relativos à raiz**;
3. origem preservada e SHA-256 de cada arquivo e sua cópia oficial;
4. dimensões do canvas, ViewPort, escala, posição de inserção conforme **o Wireframe Text e o PNG efetivamente aprovados**;
5. data e decisão explícita de aprovação/ativação, histórico de substituições e justificativa;
6. regras de integridade e relação entre as versões `white`/`black`.

Os arquivos em `references/` preservam referências históricas e origens. Os diretórios `white/template/` e `black/template/` guardam o conjunto oficial de cada tema. O bitmap de ViewPort contém **demonstração**, não constitui uma Tela funcional pronta.

## 4. Verificação antes de utilizar a referência

1. Abrir o registro genérico e identificar o modelo **vigente no momento da criação da saída**, para ambos os temas; não adivinhar pelo nome do arquivo.
2. Abrir os seis artefatos correspondentes registrados, conferir existência, tipo, dimensão física e SHA-256. Comparar a identidade binária das cópias com as origens quando estiverem presentes.
3. Ler o Wireframe Text aprovado para comprovar **geometria e identidade estrutural fixa**. O uso funcional exige um **contrato técnico versionado de aplicação**, associado explicitamente ao modelo, versões white/black e hashes vigentes, conforme a SPEC 3, seção 6.1. Os campos de conteúdo variável e suas coordenadas pertencem a esse contrato concreto; não são definidos por esta SPEC 2 nem por um mapeamento universal da SPEC 3. **Não inferir** novas regiões variáveis pela aparência ou transferir o contrato a eventual modelo futuro.
4. Conferir o PNG e o ViewPort fisicamente. Falha de hash, ausência de contrato técnico **explícito, íntegro e aplicável à versão vigente**, incompatibilidade entre variações ou ausência de informação necessária é **BLOQUEIO**, não autorização para editar o modelo. O contrato técnico concreto precisa preservar a autorização documentada de substituição dos conteúdos demonstrativos sem editar o Wireframe Text original congelado.
5. Registrar na saída dependente o identificador **exato da versão usada** e os hashes, preservando o vínculo mesmo se outro modelo passar a vigorar depois.

A leitura desta SPEC não equivale a autorização para modificar o conjunto oficial. Sua utilização nas interfaces funcionais é regida somente pela SPEC 3.

## 5. Aprovação, congelamento e substituição

- `APROVADO E CONGELADO` qualifica uma **versão física específica**. Uma versão substituída permanece aprovada historicamente e não pode ser sobrescrita.
- `VIGENTE` identifica qual versão aprovada está autorizada para **novas** saídas. Vigência não se deduz de timestamp ou da maior versão numérica.
- Uma mudança exige necessidade concreta e verificável, análise do impacto sobre white/black e saídas dependentes, comparação com manter a versão atual, proposta delimitada, autorização explícita, nova versão aprovada e registro de ativação.
- A definição e validação técnica de uma **nova** prancha-modelo obedecem à SPEC 1 e seus contratos auxiliares. A simples troca de vigência não autoriza editar arquivos congelados nem descartar o histórico.
- A seleção de novo modelo não modifica retroativamente interfaces aprovadas. Cada saída histórica conserva sua versão e hash de referência. Se for necessária migração, ela é uma alteração específica, analisada e aprovada.
- Qualquer mudança documental ou de arquivo segue [`.specs/PROCESSO-ALTERACAO-ASSISTIDA.md`](../PROCESSO-ALTERACAO-ASSISTIDA.md).

## 6. Critérios objetivos de aceite

A referência pode ser consumida somente quando: existe decisão explícita vigente por tema; versões e caminhos resolvem; hashes correspondem; imagens e dimensões físicas são válidas; geometrias essenciais estão no Wireframe Text aprovado; cada artefato histórico anterior permanece preservado. A ausência de um item impede declarar a referência tecnicamente verificada.

**Saída desta SPEC:** identidade verificável da referência aprovada e vigente (tema, modelo, versões, arquivos, hashes e decisão), disponibilizada à SPEC 3. **Nenhuma Tela ou Prancha de Implementação é produzida aqui.**
