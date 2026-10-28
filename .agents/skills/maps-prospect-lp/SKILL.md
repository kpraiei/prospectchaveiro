---
name: maps-prospect-lp
description: >-
  Gera automaticamente Landing Pages hiperlocais de alta conversão (estilo Cinematic + Morphix)
  a partir de um link do Google Maps ou JSON de scraper para prospecção ativa de negócios locais
  (Chaveiro 24h, Desentupidora, Encanador, Eletricista, Guincho, Climatização, etc.) e integra
  com a esteira de prospecção do SaaS kriar.digital.
---

# Skill: Gerador de Landing Pages Hiperlocais de Alta Conversão (Maps -> LP)

Esta skill automatiza a transformação de qualquer perfil de negócio local encontrado no Google Maps em uma **Landing Page completa, responsiva, cinematográfica e de ultra-conversão**, pronta para ser utilizada como demonstração de alto impacto na prospecção comercial via WhatsApp/SaaS.

---

## 1. Gatilhos de Ativação

A skill deve ser ativada sempre que:
- O usuário enviar um link do Google Maps (`https://maps.app.goo.gl/...`, `https://www.google.com/maps/place/...`);
- O usuário fornecer um JSON ou dados brutos de um scraper do Google Maps;
- O usuário solicitar: *"Crie uma LP de prospecção para este negócio"*.

---

## 2. Fluxo de Execução Passo a Passo

### Passo 1: Extração e Enriquecimento de Dados
A partir do link ou JSON, extraia e estruture os seguintes dados no dicionário `BUSINESS_DATA`:
- `nome`: Razão comercial ou nome fantasia divulgado no Maps.
- `telefone_display`: Telefone formatado para exibição (ex: `(11) 97435-9641`).
- `telefone_link`: Apenas dígitos com código do país (ex: `5511974359641`).
- `endereco`: Rua e número da base física.
- `bairro`: Bairro de origem.
- `cidade`: Cidade e UF.
- `cep`: CEP do local.
- `nota`: Média de avaliação no Google (ex: `4.9`).
- `total_avaliacoes`: Quantidade de reviews reais.
- `referencia`: Ponto de referência mais próximo (estações de metrô, shoppings, avenidas conhecidas).
- `regioes`: Lista de 5 bairros/regiões vizinhas num raio de 5 km, com tempo médio estimado de deslocamento (ex: `12 a 18 min`).
- `vias_locais`: Lista de 6 a 10 ruas, avenidas e praças conhecidas do bairro para compor a faixa de hiperlocalização.

---

### Passo 2: Seleção da Paleta e Identidade Cinematic do Nicho
Aplique a paleta correspondente ao nicho do negócio:

| Nicho | Cor de Fundo | Cor Primária / Glow | Acento de Ação | Efeito Atmosférico |
| :--- | :--- | :--- | :--- | :--- |
| **Chaveiro / Aberturas** | Midnight Obsidian (`#070A12`) | Âmbar Tungstênio (`#F59E0B`) | Verde WhatsApp (`#10B981`) | Luz de farol/lanterna noturna |
| **Desentupidora / Hidráulica** | Deep Slate (`#0B132B`) | Azul Ciano Limpo (`#06B6D4`) | Verde WhatsApp (`#10B981`) | Reflexos de água e tubulação |
| **Eletricista / Energia** | Grafite Carbono (`#111827`) | Amarelo Alta Tensão (`#EAB308`) | Verde WhatsApp (`#10B981`) | Faísca e contraste técnico |
| **Guincho / Auto Socorro** | Asfalto Escuro (`#0F172A`) | Laranja Segurança (`#F97316`) | Verde WhatsApp (`#10B981`) | Giroflex e reflexo de chuva |

---

### Passo 3: Geração de Ativos Visuais Cinematográficos
Sempre que possível, utilize o `generate_image` para gerar duas fotografias autênticas e não-genéricas:
1. **Hero Principal (16:9):** O profissional do nicho executando o serviço técnico com iluminação volumétrica, sombras densas e ambiente real.
2. **Macro de Ferramental (1:1):** Close no ferramental especializado do ofício (ex: decodificador Lishi, câmera de vídeo-inspeção, multímetro de precisão).

Salve os arquivos na pasta `assets/img/`.

---

### Passo 4: Estrutura Obrigatória da Landing Page (Morphix + Humanização)

A página gerada (em `app.py` e compilada em `index.html`) **DEVE** conter obrigatoriamente:

1. **Top Bar Radar de Plantão:**
   - Indicador pulsante em tempo real com tempo médio de chegada no bairro e localização da base física.

2. **Hero Section Ultra-Visual:**
   - H1 humanizado com foco na dor imediata do cliente (sem clichês corporativos de IA).
   - Composição visual com as fotografias reais geradas e badges flutuantes em vidro fosco (*Morphix Glass*).
   - Botões de chamada imediata: WhatsApp e Ligação Direta 24h.

3. **Simulador de Atendimento & Orçamento Interativo:**
   - **Passo 1:** Urgência / Serviço desejado.
   - **Passo 2:** Bairro de localização (com as opções locais reais + a opção `📍 Outro bairro / endereço personalizado...`).
   - **Campo Dinâmico para Outro Endereço:** Se selecionado, exibe input de texto + **Aviso de Atendimento Imediato**:
     > *"Nossa central entrará em contato imediatamente pelo WhatsApp para confirmar a viatura mais próxima da sua rota e informar o valor fechado antes do deslocamento."*
   - **Passo 3:** Tipo de equipamento / fechadura / veículo.
   - **Botão WhatsApp Dinâmico:** Monta a URL do WhatsApp com a mensagem completa estruturada com base nas respostas do cliente.

4. **Faixa Hiperlocal Rua a Rua:**
   - Chips com os nomes reais de 6 a 10 ruas, avenidas e praças conhecidas do bairro.

5. **Seção de Serviços Técnicos:**
   - 3 cartões em vidro fumê com borda luminosa (Morphix Card), detalhando ferramental específico, marcas atendidas e diferenciais que comprovam conhecimento da profissão.

6. **Protocolo Anti-Golpe / Segurança:**
   - 4 pilares: Preço fechado antes por foto, exigência de documento no local, ferramentas não-destrutivas e base física oficial.

7. **Prova Social Realista do Google Maps:**
   - Selo Google Maps com nota real e total de reviews.
   - 3 depoimentos autênticos citando bairros/ruas vizinhas e serviços específicos.

8. **FAQ Sanfonado (Accordion Interativo):**
   - 5 perguntas cruciais respondidas com honestidade técnica.

9. **Base Física e Mapa Interativo:**
   - Endereço real, horário de funcionamento e iframe do Google Maps da base física.

10. **Barra Fixa Mobile:**
    - Botão fixo no rodapé para dispositivos móveis com Ligação de Emergência e WhatsApp.

---

### Passo 5: Deploy & Geração do Script de Prospecção

1. Gerar o `app.py` com Flask e compilar o `index.html`.
2. Publicar no GitHub Pages ou mover para a pasta de demos do SaaS `kriar.digital`.
3. Gerar a mensagem pronta de abordagem comercial para envio no WhatsApp do proprietário:

```text
Olá [Nome do Responsável], tudo bem?
Encontrei o perfil do [Nome da Empresa] no Google Maps aqui no [Nome do Bairro] e vi as excelentes avaliações de vocês ({{ nota }}★).

Notei que muitos moradores da região precisam de socorro rápido de emergência e hoje esperam conseguir orçamento e calcular o tempo de atendimento direto pelo celular.

Tomei a liberdade de criar uma demonstração exclusiva e funcional para o [Nome da Empresa], com simulador de rota e botão direto para o seu WhatsApp:
👉 [LINK_DA_DEMO]

Se fizer sentido para o seu negócio, podemos colocar no ar no seu domínio hoje mesmo. O que achou?
```
