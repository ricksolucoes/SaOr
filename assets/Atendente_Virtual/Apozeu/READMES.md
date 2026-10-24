# APOZEU — Character Reference & AI Animation Specification

> **Personagem:** Apozeu  
> **Função:** Atendente virtual oficial do **SaOr — Sales Order**  
> **Tipo de documento:** Character Bible / Model Sheet Specification / AI Animation Guide  
> **Status:** Referência canônica para geração, animação, fala e preservação de identidade

---

## 1. Objetivo

Este documento define como as pranchas canônicas do personagem **Apozeu** devem ser interpretadas por sistemas de IA, pipelines de animação 2D/2.5D/3D, geração de vídeo, facial animation, lip sync, motion retargeting e composição.

O objetivo principal é garantir que qualquer nova imagem, vídeo, fala, movimento corporal ou expressão facial represente **o mesmo ator humano fictício**, preservando a identidade visual de Apozeu entre frames, cenas, poses, ângulos e falas.

A regra de maior prioridade é:

> **APOZEU É UMA ÚNICA IDENTIDADE HUMANA CANÔNICA.**  
> Não gerar “versões parecidas”, variações faciais, irmãos, substitutos, rejuvenescimento, envelhecimento ou alterações arbitrárias de corpo, roupa ou aparência.

---

## 2. Terminologia técnica

As pranchas existentes compõem um conjunto de **Character Reference Sheets**, também conhecido em produção como:

- **Character Bible** — especificação geral e invariantes do personagem;
- **Model Sheet** — folha de referência visual usada para manter consistência;
- **Head Turnaround** — rotação controlada da cabeça;
- **Full-Body Turnaround** — rotação corporal completa;
- **Pose Sheet / Pose Library** — biblioteca de poses e gestos;
- **Expression Sheet** — biblioteca de expressões faciais;
- **Identity Reference / Identity Anchor** — referência visual usada para bloquear a identidade;
- **Pose Conditioning** — condicionamento da geração por pose;
- **Facial Animation** — animação de músculos e regiões faciais;
- **Lip Sync** — sincronização labial com áudio;
- **Phoneme-to-Viseme Mapping** — conversão de fonemas em formas visuais da boca;
- **Coarticulation** — transição natural entre visemas consecutivos;
- **Facial Rig** — sistema de controles usado para deformar a face;
- **Blendshapes / Morph Targets** — formas faciais parametrizadas;
- **FACS (Facial Action Coding System)** — representação de movimentos faciais por Action Units;
- **Facial Landmarks** — pontos de referência geométricos do rosto;
- **Head Pose Estimation** — estimação de yaw, pitch e roll;
- **Pose Estimation** — extração de esqueleto corporal;
- **Motion Retargeting** — transferência de movimento para outro rig/personagem;
- **Inverse Kinematics (IK)** — resolução de articulações a partir de posições-alvo;
- **Temporal Consistency** — estabilidade visual entre frames;
- **Identity Lock / Face-ID Conditioning** — condicionamento que mantém a mesma identidade durante a geração;
- **Chroma Key / Spill Suppression** — recorte por fundo verde e remoção de contaminação verde.

---

## 3. Manifesto de ativos canônicos

As quatro pranchas abaixo constituem o **Canonical Reference Set v1**.

| ID | Arquivo | Tipo técnico | Função principal |
|---|---|---|---|
| `APZ-REF-01` | `PRANCHA 1 — HEAD TURNAROUND.png` | **Head Turnaround / Identity Reference** | Geometria facial, perfil, crânio, orelhas, cabelo e consistência de identidade |
| `APZ-REF-02` | `PRANCHA 2 — FULL BODY TURNAROUND.png` | **Full-Body Turnaround** | Proporções corporais, roupa, silhueta e vistas corporais |
| `APZ-REF-03` | `PRANCHA 3 — VIRTUAL ASSISTANT POSES.png` | **Pose Sheet / Gesture Library** | Linguagem corporal, gestos de apresentação e poses de atendimento |
| `APZ-REF-04` | `PRANCHA 4 — FACIAL EXPRESSIONS.png` | **Facial Expression Sheet** | Estados expressivos do rosto mantendo a identidade |

### 3.1. Hierarquia de autoridade

Quando houver conflito entre referências, aplicar esta prioridade:

1. **Identidade facial:** `APZ-REF-01`
2. **Proporção corporal e roupa:** `APZ-REF-02`
3. **Gestos e poses:** `APZ-REF-03`
4. **Expressão facial:** `APZ-REF-04`

Uma pose ou expressão **nunca pode substituir ou reinterpretar a identidade** definida pelo Head Turnaround.

---

## 4. Identity Lock — invariantes do personagem

Um sistema de geração deve tratar as características abaixo como **identity invariants**.

### 4.1. Identidade facial

Preservar:

- geometria do crânio;
- formato e proporção do rosto;
- distância e formato dos olhos;
- sobrancelhas;
- ponte, largura e ponta do nariz;
- formato dos lábios;
- mandíbula;
- queixo;
- posição e formato das orelhas;
- linha frontal do cabelo;
- densidade e comprimento do cabelo;
- idade aparente;
- tom e subtom da pele.

### 4.2. Identidade corporal

Preservar:

- altura visual aproximada;
- relação cabeça/tronco/pernas;
- largura dos ombros;
- volume do tórax;
- comprimento dos braços;
- proporções das mãos;
- comprimento e volume das pernas;
- constituição média, saudável, moderadamente atlética e levemente robusta.

### 4.3. Guarda-roupa canônico

Manter:

- blazer moderno azul-marinho escuro;
- camisa social branca ou azul extremamente claro;
- primeiro botão aberto;
- sem gravata;
- calça grafite escuro;
- calçado corporativo minimalista;
- nenhuma peça verde.

A roupa deve ser considerada parte da **canonical appearance** e não deve variar entre cenas, salvo nova versão formalmente aprovada do personagem.

---

## 5. Representação espacial e Head Pose

A prancha `APZ-REF-01` deve ser usada como referência de **Head Pose Estimation**.

Convenção recomendada:

- **Yaw** — rotação esquerda/direita;
- **Pitch** — inclinação para cima/baixo;
- **Roll** — inclinação lateral.

Referências disponíveis:

- frontal: `yaw ≈ 0°`;
- direita: `+15°`, `+30°`, `+45°`, `+60°`, `+90°`;
- esquerda: `-15°`, `-30°`, `-45°`, `-60°`, `-90°`;
- traseira: aproximadamente `180°`.

Para ângulos intermediários, realizar **interpolação de pose**, preservando a geometria facial observada nas vistas canônicas.

Nunca redesenhar o rosto de maneira independente a cada ângulo.

---

## 6. Pose Conditioning e animação corporal

A prancha `APZ-REF-03` deve funcionar como **Pose Library**.

Em pipelines baseados em esqueleto, recomenda-se extrair ou representar a pose por landmarks compatíveis com padrões como:

- COCO Keypoints;
- OpenPose;
- MediaPipe / BlazePose;
- skeleton rigs equivalentes.

### 6.1. Procedimento recomendado

1. selecionar a pose canônica ou pose-alvo;
2. extrair o esqueleto corporal;
3. aplicar **Pose Conditioning**;
4. preservar o **Identity Anchor** do rosto;
5. preservar o guarda-roupa canônico;
6. aplicar **Inverse Kinematics (IK)** quando necessário;
7. realizar **Motion Retargeting** para sequências animadas;
8. interpolar movimentos com curvas suaves;
9. validar mãos, dedos, braços e silhueta;
10. verificar **Temporal Consistency** entre frames.

### 6.2. Movimento corporal

Apozeu deve utilizar movimentos:

- profissionais;
- moderados;
- naturais;
- controlados;
- sem gesticulação exagerada;
- compatíveis com um atendente virtual corporativo.

Evitar:

- movimentos caricatos;
- bouncing excessivo;
- movimentos muito rápidos sem finalidade;
- gestos agressivos;
- poses teatrais incompatíveis com atendimento profissional.

---

## 7. Facial Animation

A prancha `APZ-REF-04` é a referência para **Facial Animation**.

Os estados disponíveis são:

1. Neutral Professional
2. Light Smile
3. Cordial Smile
4. Attention
5. Concentration
6. Thinking
7. Explanation
8. Confirmation
9. Satisfaction
10. Moderate Concern
11. Moderate Positive Surprise
12. Empathy

A expressão deve ser aplicada **sobre a identidade**, e nunca recriar uma nova face.

### 7.1. Representações técnicas compatíveis

A expressão pode ser convertida para:

- **FACS Action Units**;
- **Blendshapes / Morph Targets**;
- rigs faciais proprietários;
- ARKit-style facial blendshapes;
- facial landmark deformation;
- neural facial animation.

A correspondência com FACS ou blendshapes deve ser usada como **controle de animação**, não como substituição da referência visual.

---

## 8. Lip Sync — fala e movimento da boca

As pranchas atuais não possuem uma **Viseme Sheet** dedicada. Portanto, o movimento labial deve ser sintetizado por um pipeline de **Audio-Driven Facial Animation** ou **Phoneme-to-Viseme Lip Sync**, usando a identidade facial canônica como restrição.

### 8.1. Pipeline recomendado

```text
Texto
  ↓
TTS / voz gravada
  ↓
Áudio
  ↓
Forced Alignment / Speech Alignment
  ↓
Timeline de fonemas
  ↓
Phoneme-to-Viseme Mapping
  ↓
Coarticulation
  ↓
Blendshapes / Facial Rig / Neural Face Animation
  ↓
Identity Constraint + Temporal Consistency
  ↓
Render final
```

### 8.2. Forced Alignment

O sistema deve obter uma linha do tempo aproximada contendo:

```text
fonema + início + fim + intensidade/confiança
```

Exemplo conceitual:

```text
0.000–0.090  /b/
0.090–0.180  /o/
0.180–0.260  /m/
0.260–0.400  /d/
0.400–0.540  /i/
0.540–0.700  /a/
```

O objetivo é sincronizar cada configuração da boca com o áudio real.

---

## 9. Visemas recomendados para Português do Brasil

Para fala em **pt-BR**, usar grupos de visemas em vez de criar uma forma diferente para cada fonema.

| Visema | Fonemas aproximados | Configuração visual |
|---|---|---|
| `REST` | pausa / silêncio | boca neutra |
| `MBP` | /m/, /b/, /p/ | lábios completamente fechados |
| `FV` | /f/, /v/ | dentes superiores tocando o lábio inferior |
| `TDNL` | /t/, /d/, /n/, /l/ | abertura leve, língua/alvéolos sugeridos |
| `KG` | /k/, /g/ | abertura moderada, articulação posterior |
| `SZ` | /s/, /z/ | lábios estreitos, dentes próximos |
| `SHZH` | /ʃ/, /ʒ/ | leve protrusão/arredondamento |
| `CHJ` | /tʃ/, /dʒ/ | protrusão moderada com abertura curta |
| `R` | variações de /r/ | abertura e tensão compatíveis com contexto |
| `A` | /a/, /ɐ/ | abertura vertical ampla/moderada |
| `E` | /e/, /ɛ/ | abertura média, lábios mais horizontais |
| `I` | /i/ | abertura pequena, lábios lateralizados |
| `O` | /o/, /ɔ/ | boca arredondada |
| `U` | /u/ | protrusão e arredondamento mais acentuados |

Esta tabela é um **viseme map operacional**, não uma substituição de análise fonética contextual.

---

## 10. Coarticulation

Lip sync realista exige **coarticulation**.

A boca não deve saltar abruptamente entre formas.

Aplicar:

- antecipação parcial do próximo visema;
- sobreposição entre visemas;
- easing temporal;
- redução de amplitude em fala rápida;
- maior abertura em sílabas tônicas quando compatível;
- retorno suave para `REST`.

### 10.1. Interpolação

Uma implementação típica pode usar:

- spline interpolation;
- cubic Bézier;
- critically damped smoothing;
- temporal low-pass filtering;
- blendshape interpolation.

Mudanças bruscas de mouth shape devem ser evitadas.

---

## 11. Controles faciais mínimos para fala

Caso o motor utilize blendshapes, os seguintes controles são recomendados:

```text
jawOpen
mouthClose
mouthFunnel
mouthPucker
mouthSmileLeft
mouthSmileRight
mouthFrownLeft
mouthFrownRight
mouthStretchLeft
mouthStretchRight
mouthPressLeft
mouthPressRight
mouthUpperUpLeft
mouthUpperUpRight
mouthLowerDownLeft
mouthLowerDownRight
cheekSquintLeft
cheekSquintRight
eyeBlinkLeft
eyeBlinkRight
eyeLookUp / Down / In / Out
browInnerUp
browDownLeft
browDownRight
```

Os nomes acima seguem convenções amplamente usadas em rigs modernos e são compatíveis conceitualmente com pipelines do tipo **ARKit Blendshape**.

O sistema pode usar nomenclatura diferente, desde que preserve comportamento equivalente.

---

## 12. Fala natural — comportamento além da boca

Para evitar aparência de “cabeça falando”, a animação deve combinar lip sync com microanimações.

### 12.1. Eye Animation

Adicionar:

- blinking natural;
- micro-saccades;
- pequenas mudanças de foco;
- eye contact predominante com a câmera durante atendimento.

Evitar olhar fixo artificial por longos períodos.

### 12.2. Head Motion

Adicionar pequenas variações de:

- yaw;
- pitch;
- roll.

Movimento deve ser discreto e sem comprometer o enquadramento.

### 12.3. Facial Micro-Expressions

Combinar a fala com:

- pequenos movimentos de sobrancelha;
- leve alteração de bochechas;
- microexpressões compatíveis com intenção;
- mudanças sutis na região periocular.

### 12.4. Gesture Synchronization

Gestos corporais devem estar semanticamente sincronizados com a fala.

Exemplos:

- apresentar informação → mão aberta;
- confirmar → gesto positivo discreto;
- indicar interface → apontar lateralmente;
- escutar → postura atenta;
- explicar → movimentos moderados das mãos.

---

## 13. Emotion / Expression State Machine

Para sistemas conversacionais, recomenda-se representar o estado expressivo como uma máquina de estados simples.

Exemplo:

```yaml
expression_state:
  default: neutral_professional

  states:
    neutral_professional:
      reference: APZ-REF-04-01

    light_smile:
      reference: APZ-REF-04-02

    cordial_smile:
      reference: APZ-REF-04-03

    attention:
      reference: APZ-REF-04-04

    concentration:
      reference: APZ-REF-04-05

    thinking:
      reference: APZ-REF-04-06

    explanation:
      reference: APZ-REF-04-07

    confirmation:
      reference: APZ-REF-04-08

    satisfaction:
      reference: APZ-REF-04-09

    moderate_concern:
      reference: APZ-REF-04-10

    positive_surprise:
      reference: APZ-REF-04-11

    empathy:
      reference: APZ-REF-04-12
```

As transições devem ser interpoladas. Nunca realizar corte instantâneo entre expressões muito diferentes.

---

## 14. Arquitetura de geração recomendada

Um pipeline de animação pode ser representado assim:

```text
                         ┌─────────────────────┐
                         │ Canonical Identity  │
                         │     APZ-REF-01      │
                         └──────────┬──────────┘
                                    │
                   ┌────────────────┼────────────────┐
                   │                │                │
                   ▼                ▼                ▼
            Head Pose          Face Identity   Facial Geometry
                   │                │                │
                   └────────────────┼────────────────┘
                                    │
                            Identity Constraint
                                    │
           ┌────────────────────────┼────────────────────────┐
           │                        │                        │
           ▼                        ▼                        ▼
    Body Pose / Gesture        Expression State        Speech Audio
       APZ-REF-03               APZ-REF-04                 │
           │                        │                       ▼
           │                        │              Forced Alignment
           │                        │                       │
           │                        │                       ▼
           │                        │                Phoneme Timeline
           │                        │                       │
           │                        │                       ▼
           │                        │                Viseme Sequence
           │                        │                       │
           └──────────────┬─────────┴───────────────┬──────┘
                          │                         │
                          ▼                         ▼
                   Motion Synthesis          Facial Rig / Lip Sync
                          │                         │
                          └────────────┬────────────┘
                                       ▼
                              Temporal Consistency
                                       │
                                       ▼
                                   Rendering
                                       │
                                       ▼
                              Chroma Key Composite
```

---

## 15. Temporal Consistency

Para vídeo, cada frame não deve ser tratado como uma imagem independente.

Aplicar mecanismos de:

- identity embedding persistente;
- face landmark tracking;
- pose tracking;
- optical flow ou equivalente;
- temporal attention;
- temporal latent consistency;
- motion-aware generation;
- seed/state persistence quando disponível.

### 15.1. Erros proibidos

Não permitir:

- mudança de nariz entre frames;
- mudança de olhos;
- mudança do formato da cabeça;
- oscilação da linha do cabelo;
- flutuação de idade;
- mudança de tom de pele;
- mudança de roupa;
- alteração súbita de largura corporal;
- “face flicker”;
- “identity drift”;
- dedos surgindo ou desaparecendo;
- mandíbula mudando de tamanho durante fala.

---

## 16. Chroma Key e composição

Todas as referências utilizam:

```text
HEX: #00FF00
RGB: 0, 255, 0
```

O pipeline final deve suportar:

- **Chroma Key Extraction**;
- **Alpha Matte Generation**;
- **Edge Refinement**;
- **Despill / Spill Suppression**;
- **Hair Matte Refinement**;
- **Premultiplied Alpha** quando aplicável.

### 16.1. Regras

O verde não deve contaminar:

- pele;
- cabelo;
- orelhas;
- camisa;
- blazer;
- mãos;
- dedos;
- sapatos.

O recorte deve preservar detalhes finos, principalmente cabelo, orelhas e dedos.

---

## 17. Prompt técnico base para sistemas generativos

O seguinte bloco pode ser usado como especificação de alto nível para um modelo de geração de imagem/vídeo:

```text
Use APOZEU canonical character references as identity-locked conditioning.

Primary identity anchor:
APZ-REF-01 Head Turnaround.

Body and wardrobe anchor:
APZ-REF-02 Full-Body Turnaround.

Pose conditioning:
APZ-REF-03 Pose Sheet.

Facial expression conditioning:
APZ-REF-04 Facial Expression Sheet.

This is one single human actor.
Maintain strict Face-ID consistency, facial geometry, skull geometry,
hairline, skin tone, apparent age, body proportions and wardrobe.

For speech animation, preserve identity while driving only the mouth,
jaw and related facial regions using phoneme-to-viseme lip sync,
coarticulation and temporally smooth facial animation.

Use subtle eye blinks, micro-saccades, head motion and context-appropriate
micro-expressions.

Do not regenerate a new face per frame.
Do not alter ethnicity appearance, skin tone, age, hairstyle, body type,
height or clothing.

Maintain temporal consistency and photorealistic human anatomy.
Background must remain pure chroma key green #00FF00 with no green spill.
```

---

## 18. Negative constraints

```text
different person,
multiple identities,
face variation,
identity drift,
face flicker,
facial geometry drift,
different skull,
different eyes,
different nose,
different jaw,
different ears,
different lips,
different hairline,
different age,
different skin tone,
different body proportions,
different height,
different wardrobe,
green clothing,
green spill,
plastic skin,
beauty filter,
cartoon,
anime,
illustration,
CGI appearance,
malformed hands,
extra fingers,
missing fingers,
duplicated limbs,
asymmetrical eyes,
mouth deformation unrelated to phonemes,
jaw size drift,
temporal instability,
background scenery,
office environment,
furniture,
uneven green screen,
background shadows.
```

---

## 19. Machine-readable character profile

```yaml
character:
  id: APOZEU
  role: virtual_sales_assistant
  product: SaOr - Sales Order
  identity_policy: strict_locked_identity

appearance:
  sex_presentation: male
  apparent_age: 45
  visual_height_m: 1.80
  visual_weight_kg: 82
  build: medium_moderately_athletic_slightly_robust
  skin:
    tone: medium_brown
    undertone: warm_subtle_golden
  hair:
    color: very_dark_brown_almost_black
    length_mm: 1-3
    temples: slightly_receded
  facial_hair: clean_shaven_with_very_subtle_shadow
  eyes: dark_brown
  glasses: false

wardrobe:
  blazer: dark_navy
  shirt: white_or_extremely_light_blue
  shirt_first_button_open: true
  tie: false
  trousers: dark_graphite
  shoes: minimal_corporate
  green_clothing: forbidden

rendering:
  style: ultra_photorealistic_human_photography
  lighting_kelvin: 5500
  background:
    type: chroma_key
    hex: "#00FF00"
    rgb: [0, 255, 0]
  green_spill: forbidden

animation:
  face_identity_lock: required
  temporal_consistency: required
  head_pose_tracking: required
  pose_conditioning: supported
  facial_animation: supported
  lip_sync:
    method: phoneme_to_viseme
    coarticulation: required
    forced_alignment: recommended
    language_primary: pt-BR
  eye_animation:
    blinking: natural
    micro_saccades: subtle
  motion_style:
    professional: true
    restrained: true
    exaggerated_gestures: false

canonical_references:
  head_turnaround: APZ-REF-01
  full_body_turnaround: APZ-REF-02
  pose_sheet: APZ-REF-03
  expression_sheet: APZ-REF-04
```

---

## 20. Quality Assurance — validação automática ou manual

Antes de aprovar um frame ou vídeo, validar:

### Identidade

- [ ] é inequivocamente o mesmo Apozeu;
- [ ] rosto compatível com `APZ-REF-01`;
- [ ] linha do cabelo preservada;
- [ ] idade aparente preservada;
- [ ] olhos, nariz, mandíbula, boca e orelhas preservados;
- [ ] tom de pele consistente.

### Corpo e roupa

- [ ] proporção corporal compatível com `APZ-REF-02`;
- [ ] roupa canônica preservada;
- [ ] nenhuma peça verde;
- [ ] anatomia correta;
- [ ] mãos e dedos corretos.

### Animação

- [ ] pose coerente;
- [ ] expressão coerente;
- [ ] movimento contínuo;
- [ ] sem identity drift;
- [ ] sem face flicker;
- [ ] sem alterações abruptas de proporção;
- [ ] piscadas naturais;
- [ ] olhar coerente;
- [ ] gestos compatíveis com a fala.

### Lip Sync

- [ ] fonemas alinhados ao áudio;
- [ ] visemas coerentes;
- [ ] fechamento labial correto para `/m b p/`;
- [ ] articulação labiodental para `/f v/`;
- [ ] vogais visualmente diferenciadas;
- [ ] coarticulation suave;
- [ ] mandíbula não deforma a identidade;
- [ ] nenhuma alteração estrutural do rosto durante fala.

### Chroma Key

- [ ] fundo uniforme `#00FF00`;
- [ ] sem cenário;
- [ ] sem sombra no fundo;
- [ ] sem green spill;
- [ ] bordas limpas;
- [ ] cabelo preservado no matte.

---

## 21. Ativos complementares recomendados

As quatro pranchas atuais são suficientes para estabelecer identidade, corpo, poses e expressões. Para aumentar a precisão de animação em produção, podem ser criados futuramente, mediante aprovação:

### `APZ-REF-05` — Viseme Sheet

Prancha frontal dedicada às formas de boca:

```text
REST
MBP
FV
TDNL
KG
SZ
SHZH
CHJ
R
A
E
I
O
U
```

Essa prancha reduziria a necessidade de o sistema inferir a forma da boca.

### `APZ-REF-06` — Eye & Gaze Sheet

Referências para:

- gaze left/right/up/down;
- blink;
- half blink;
- squint;
- attentive gaze.

### `APZ-REF-07` — Hand Gesture Sheet

Close-ups para:

- pointing;
- open palm;
- presenting;
- confirmation;
- neutral hands;
- device/interface pointing.

Esses ativos são **recomendações futuras** e não fazem parte do conjunto canônico atual.

---

## 22. Regra final para qualquer IA

> Use as pranchas como referências condicionantes de uma única identidade persistente.  
> Movimento, fala, expressão e pose são variáveis.  
> **Identidade, anatomia-base, idade, pele, cabelo, roupa e proporções são invariantes.**

Uma implementação correta deve fazer Apozeu parecer **um único ator humano real sendo filmado continuamente**, e não imagens independentes de homens semelhantes.

---

## 23. Versionamento

Convenção sugerida:

```text
APOZEU_CHARACTER_SPEC_v1.0
APZ-REF-01_v1
APZ-REF-02_v1
APZ-REF-03_v1
APZ-REF-04_v1
```

Mudanças de identidade visual, corpo ou guarda-roupa exigem nova revisão formal da especificação.

Alterações apenas de documentação, metadados ou pipeline podem incrementar versão secundária sem redefinir o personagem.
