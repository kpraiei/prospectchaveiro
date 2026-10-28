import re
from datetime import datetime

NICHE_CONFIGS = {
    "chaveiro": {
        "tag": "Socorro 24 Horas",
        "bg_color": "#070A12",
        "glow_color": "#F59E0B",
        "glow_class": "text-amber-500",
        "accent_name": "Âmbar Tungstênio",
        "headline": "Ficou trancado para fora? Chegamos em 20 minutos sem arrombar sua porta.",
        "subheadline": "Atendimento técnico de urgência residencial, comercial e automotivo. Orçamento passado por foto no WhatsApp antes da viatura sair da base.",
        "icon": "fa-key",
        "action_icon": "fa-phone-volume",
        "services": [
            {
                "title": "Aberturas & Troca de Segredo",
                "desc": "Abertura de portas simples, tetra e blindadas. Troca de miolo com chaves lacradas no local.",
                "bullets": ["Chaves Yale, Tetra e Multiponto", "Extração de chave quebrada no miolo", "Unificação de segredos"]
            },
            {
                "title": "Socorro Automotivo Lishi",
                "desc": "Abertura técnica pelo miolo da maçaneta sem entortar a coluna nem riscar a lataria do veículo.",
                "bullets": ["Nacionais e importados", "Chaves canivete e presença", "Reparo de ignição"]
            },
            {
                "title": "Fechaduras Digitais & Biometria",
                "desc": "Instalação com gabarito de fábrica para portas de madeira, ferro ou vidro.",
                "bullets": ["Intelbras, Yale, Papaiz e Samsung", "Configuração de senhas e tags", "Instalação limpa com aspirador"]
            }
        ],
        "garantias": [
            {"title": "Preço Fechado Antes", "desc": "Você manda foto pelo WhatsApp e passamos o valor exato antes de sair."},
            {"title": "Conferência de Documento", "desc": "Exigimos documento no local para total proteção do condomínio e imóvel."},
            {"title": "Ferramentas Não-Destrutivas", "desc": "Mais de 95% das portas abertas sem dano ao miolo ou fechadura."},
            {"title": "Base Física Estabelecida", "desc": "Técnicos uniformizados e ponto físico oficial na região."}
        ]
    },
    "barbearia": {
        "tag": "Arte com Estilo & Visagismo",
        "bg_color": "#0A0A0C",
        "glow_color": "#C9A86A",
        "glow_class": "text-amber-300",
        "accent_name": "Ouro Vintage",
        "headline": "Corte na régua e visagismo masculino sem fila com hora marcada.",
        "subheadline": "Consultoria estética para harmonizar o corte com seu formato de rosto. Navalha afiada, toalha quente e cerveja gelada inclusa.",
        "icon": "fa-scissors",
        "action_icon": "fa-calendar-check",
        "services": [
            {
                "title": "Corte Fade & Visagismo",
                "desc": "Degradê milimétrico (Skin Fade, Taper ou Clássico na tesoura) planejado para o seu rosto.",
                "bullets": ["Pezinho a laser", "Lavagem e finalização matte", "Bebida cortesia inclusa"]
            },
            {
                "title": "Barboterapia Tradicional",
                "desc": "Ritual relaxante com toalha aquecida aromatizada, óleos emolientes e navalhete descartável.",
                "bullets": ["Abertura dos poros", "Alinhamento simétrico", "Pós-barba sem ardência"]
            },
            {
                "title": "Planos Mensais de Assinatura",
                "desc": "Mantenha o cabelo e barba impecáveis o mês todo pagando uma mensalidade econômica fixa.",
                "bullets": ["Opções a partir de R$ 80/mês", "Prioridade na agenda", "Sem fidelidade abusiva"]
            }
        ],
        "garantias": [
            {"title": "Pontualidade Britânica", "desc": "Atendimento rigoroso no horário agendado, sem horas de espera na recepção."},
            {"title": "Lâminas 100% Descartáveis", "desc": "Abertura de lacre na sua frente e toalhas higienizadas esterilizadas."},
            {"title": "Bebida Cortesia", "desc": "Deguste cerveja estupidamente gelada ou café expresso durante o corte."},
            {"title": "Ambiente Climatizado", "desc": "Espaço moderno com boa música, ar-condicionado e Wi-Fi de alta velocidade."}
        ]
    },
    "desentupidora": {
        "tag": "Plantão Hidráulico 24h",
        "bg_color": "#07111E",
        "glow_color": "#06B6D4",
        "glow_class": "text-cyan-400",
        "accent_name": "Ciano Técnico",
        "headline": "Ralo, vaso ou pia entupidos? Desentupimento sem quebrar pisos ou paredes.",
        "subheadline": "Equipamentos de hidrojateamento de alta pressão e sondas rotativas Roto-Rooter K-500. Orçamento gratuito no local em até 30 minutos.",
        "icon": "fa-faucet-drip",
        "action_icon": "fa-truck-fast",
        "services": [
            {
                "title": "Desentupimento de Esgoto & Pias",
                "desc": "Desobstrução completa de ramais de gordura, ralos de banheiro e pias de cozinha.",
                "bullets": ["Sem quebrar azulejos", "Limpeza preventiva de ramais", "Garantia por escrito"]
            },
            {
                "title": "Hidrojateamento de Alta Pressão",
                "desc": "Limpeza técnica profunda com jato de água de alta pressão para redes prediais e comerciais.",
                "bullets": ["Remoção de raízes e crostas", "Caminhão equipado", "Laudo técnico para condomínios"]
            },
            {
                "title": "Vídeo-Inspeção Robotizada",
                "desc": "Câmera de fibra óptica com micro-sonda que filma o interior da tubulação e aponta a rachadura exata.",
                "bullets": ["Localização precisa do ponto", "Relatório fotográfico", "Economia em reformas"]
            }
        ],
        "garantias": [
            {"title": "Chegada em 30 Minutos", "desc": "Equipes volantes de moto e furgão estrategicamente distribuídas na região."},
            {"title": "Visita Técnica Gratuita", "desc": "Avaliamos no local sem custo de visita para passar o valor fechado."},
            {"title": "Garantia de 90 Dias", "desc": "Certificado de garantia por escrito após a conclusão da desobstrução."},
            {"title": "Limpeza Pós-Serviço", "desc": "Deixamos o ambiente higienizado e limpo, sem mau cheiro."}
        ]
    }
}

def clean_phone(phone_str: str) -> str:
    digits = re.sub(r"\D", "", phone_str)
    if len(digits) == 10 or len(digits) == 11:
        return "55" + digits
    return digits

def generate_slug(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[àáâãä]", "a", text)
    text = re.sub(r"[èéêë]", "e", text)
    text = re.sub(r"[ìíîï]", "i", text)
    text = re.sub(r"[òóôõö]", "o", text)
    text = re.sub(r"[ùúûü]", "u", text)
    text = re.sub(r"[ç]", "c", text)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")

def generate_landing_page(data: dict) -> tuple[str, str, str]:
    """
    Recebe os dados do prospect extraídos do Google Maps / Scraper do kriar.digital
    e gera:
    1. slug (identificador único da demo)
    2. HTML completo da Landing Page (Cinematic + Morphix)
    3. Mensagem de abordagem personalizada para o WhatsApp do proprietário
    """
    nome = data.get("business_name") or data.get("nome") or "Negócio Local"
    category = (data.get("category") or data.get("nicho") or "chaveiro").lower()
    phone_raw = data.get("phone") or data.get("telefone") or "(11) 99999-9999"
    phone_clean = clean_phone(phone_raw)
    address = data.get("address") or data.get("endereco") or "Endereço comercial"
    neighborhood = data.get("neighborhood") or data.get("bairro") or "Bairro central"
    city = data.get("city") or data.get("cidade") or "São Paulo"
    state = data.get("state") or data.get("uf") or "SP"
    rating = str(data.get("rating") or data.get("nota") or "4.9")
    reviews_count = str(data.get("reviews_count") or data.get("total_avaliacoes") or "120")
    
    slug = generate_slug(f"{nome}-{neighborhood}")

    # Determina configuração de nicho
    niche = "chaveiro"
    if "barbe" in category or "cabel" in category:
        niche = "barbearia"
    elif "desentup" in category or "hidraul" in category or "encan" in category:
        niche = "desentupidora"

    config = NICHE_CONFIGS.get(niche, NICHE_CONFIGS["chaveiro"])

    # Fotos temáticas padrão (geradas ou curadas de alta definição)
    if niche == "barbearia":
        img_hero = "/assets/img/barbearia_hero.jpg"
        img_macro = "/assets/img/barba_macro.jpg"
    elif niche == "desentupidora":
        img_hero = "https://images.unsplash.com/photo-1581578731548-c64695cc6952?auto=format&fit=crop&w=900&q=80"
        img_macro = "https://images.unsplash.com/photo-1621905251918-48416bd8575a?auto=format&fit=crop&w=600&q=80"
    else:
        img_hero = "/assets/img/hero_chaveiro.jpg"
        img_macro = "/assets/img/auto_chaveiro.jpg"

    html = f"""<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{nome} | {config['tag']} em {neighborhood}, {city}</title>
    <meta name="description" content="{nome} - {config['subheadline']} Localizado em {neighborhood}, {city}.">
    <meta name="theme-color" content="{config['bg_color']}">

    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

    <style>
        body {{
            background-color: {config['bg_color']};
            background-image: 
                radial-gradient(circle at 15% 15%, rgba(245, 158, 11, 0.08) 0%, transparent 40%),
                radial-gradient(circle at 85% 30%, rgba(30, 43, 72, 0.35) 0%, transparent 50%),
                linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
            background-size: 100% 100%, 100% 100%, 36px 36px, 36px 36px;
        }}
        .morphix-panel {{
            background: linear-gradient(135deg, rgba(19, 27, 46, 0.88) 0%, rgba(13, 19, 34, 0.95) 100%);
            backdrop-filter: blur(18px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 24px 48px -12px rgba(0, 0, 0, 0.8), inset 0 1px 0 rgba(255, 255, 255, 0.1);
        }}
        .morphix-card {{
            background: linear-gradient(145deg, #131B2E 0%, #0D1322 100%);
            border: 1px solid rgba(255, 255, 255, 0.06);
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }}
        .morphix-card:hover {{
            transform: translateY(-4px);
            border-color: rgba(245, 158, 11, 0.35);
            box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.85);
        }}
    </style>
</head>
<body class="text-slate-200 antialiased font-sans">

    <!-- Top Bar Radar -->
    <aside class="bg-black/90 border-b border-white/10 py-2.5 px-4 text-xs sticky top-0 z-50 backdrop-blur-md">
        <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3">
            <div class="flex items-center gap-2.5">
                <span class="relative flex h-3 w-3 items-center justify-center">
                    <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-500 opacity-75"></span>
                    <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
                </span>
                <span class="font-bold text-white uppercase text-[11px] sm:text-xs">
                    Plantão Ativo: <span class="text-amber-400 font-semibold normal-case">{neighborhood} & Região</span>
                </span>
            </div>
            <div class="flex items-center gap-4 text-slate-400 text-xs">
                <span><i class="fa-solid fa-location-dot text-amber-400 mr-1"></i> {address}</span>
                <span class="text-emerald-400 font-semibold"><i class="fa-solid fa-star text-xs"></i> {rating} ({reviews_count} avaliações)</span>
            </div>
        </div>
    </aside>

    <!-- Header -->
    <header class="border-b border-white/5 py-4 px-4 sm:px-8 bg-black/50 backdrop-blur-xl relative z-40">
        <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
            <a href="#" class="flex items-center gap-3">
                <div class="w-11 h-11 rounded-xl bg-amber-500/20 border border-amber-500/40 flex items-center justify-center text-amber-400 text-xl font-bold">
                    <i class="fa-solid {config['icon']}"></i>
                </div>
                <div>
                    <span class="font-extrabold text-lg sm:text-xl text-white tracking-tight block leading-none">{nome.upper()}</span>
                    <span class="text-xs text-amber-400/90 font-medium block mt-1">{config['tag']}</span>
                </div>
            </a>
            <div class="flex items-center gap-3">
                <a href="tel:+{phone_clean}" class="hidden sm:inline-flex items-center gap-2 px-4 py-2.5 rounded-xl bg-slate-900 border border-slate-700 text-white text-sm font-semibold hover:border-amber-400/50 transition">
                    <i class="fa-solid {config['action_icon']} text-amber-400"></i>
                    <span>{phone_raw}</span>
                </a>
                <a href="https://wa.me/{phone_clean}?text=Ol%C3%A1!%20Vi%20o%20site%20da%20{nome}%20e%20gostaria%20de%20atendimento." target="_blank" class="px-5 py-2.5 rounded-xl bg-gradient-to-r from-emerald-500 to-emerald-600 text-white font-bold text-sm shadow-lg hover:brightness-110 transition flex items-center gap-2">
                    <i class="fa-brands fa-whatsapp text-lg"></i>
                    <span>Chamar no WhatsApp</span>
                </a>
            </div>
        </div>
    </header>

    <!-- Hero Section -->
    <main class="relative pt-8 pb-16 px-4 sm:px-8 max-w-7xl mx-auto">
        <div class="max-w-3xl mb-8 space-y-4">
            <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-slate-800/80 border border-slate-700 text-xs text-slate-300">
                <span class="text-amber-400 flex"><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i></span>
                <span class="font-bold text-white">{rating} de 5 no Google Maps</span>
                <span class="text-slate-500">•</span>
                <span>Referência em {neighborhood}</span>
            </div>
            <h1 class="text-3xl sm:text-5xl lg:text-6xl font-extrabold text-white tracking-tight leading-[1.12]">
                {config['headline']}
            </h1>
            <p class="text-slate-300 text-base sm:text-lg leading-relaxed">
                {config['subheadline']}
            </p>
            <div class="flex flex-wrap gap-3 pt-2">
                <a href="https://wa.me/{phone_clean}?text=Ol%C3%A1!%20Preciso%20de%20atendimento%20urgente%20em%20{neighborhood}." target="_blank" class="px-7 py-3.5 rounded-xl bg-gradient-to-r from-emerald-500 to-emerald-600 text-white font-extrabold text-sm sm:text-base flex items-center gap-2.5 shadow-lg hover:brightness-110 transition">
                    <i class="fa-brands fa-whatsapp text-xl"></i>
                    <span>SOLICITAR ORÇAMENTO NO WHATSAPP</span>
                </a>
                <a href="tel:+{phone_clean}" class="px-5 py-3.5 rounded-xl bg-slate-900 border border-slate-700 text-white font-bold text-sm flex items-center gap-2 transition hover:border-amber-400/50">
                    <i class="fa-solid fa-phone text-amber-400"></i>
                    <span>LIGAR DIRETO</span>
                </a>
            </div>
        </div>

        <!-- Grid Visual & Simulador -->
        <div class="grid lg:grid-cols-12 gap-8 items-stretch">
            
            <!-- Imagens Hero -->
            <div class="lg:col-span-6 flex flex-col justify-between gap-4">
                <div class="relative rounded-2xl overflow-hidden border border-slate-800 shadow-2xl min-h-[320px] group flex-1">
                    <img src="{img_hero}" alt="{nome}" class="w-full h-full object-cover group-hover:scale-105 transition duration-700">
                    <div class="absolute inset-0 bg-gradient-to-t from-black via-black/30 to-transparent"></div>
                    <div class="absolute bottom-4 left-4 right-4 bg-slate-900/95 backdrop-blur-md p-4 rounded-xl border border-slate-800">
                        <p class="text-xs font-bold uppercase tracking-wider text-amber-400">{config['tag']}</p>
                        <p class="text-sm font-semibold text-white mt-0.5">Atendimento rápido com garantia em {city}</p>
                    </div>
                </div>
                <div class="morphix-panel p-4 rounded-2xl flex items-center gap-4">
                    <div class="w-20 h-20 rounded-xl overflow-hidden shrink-0 border border-slate-800">
                        <img src="{img_macro}" alt="Ferramental" class="w-full h-full object-cover">
                    </div>
                    <div class="flex-1">
                        <span class="text-xs font-bold text-amber-400 uppercase">Ferramental Técnico Especializado</span>
                        <h4 class="font-bold text-sm text-white mt-0.5">Equipamentos de alta precisão</h4>
                        <p class="text-xs text-slate-400">Trabalho limpo, seguro e com laudo técnico quando solicitado.</p>
                    </div>
                </div>
            </div>

            <!-- Simulador Morphix com suporte a Outro Endereço -->
            <div class="lg:col-span-6">
                <div class="morphix-panel p-6 sm:p-7 rounded-2xl relative h-full flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between pb-4 border-b border-slate-800">
                            <div>
                                <span class="text-amber-400 font-bold text-[11px] uppercase tracking-wider flex items-center gap-1.5">
                                    <span class="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span>
                                    Simulador Imediato
                                </span>
                                <h3 class="font-extrabold text-xl text-white mt-1">Calcular Tempo & Preço Fechado</h3>
                            </div>
                            <div class="w-10 h-10 rounded-xl bg-slate-800 border border-slate-700 flex items-center justify-center text-amber-400">
                                <i class="fa-solid fa-sliders"></i>
                            </div>
                        </div>

                        <div class="mt-4 space-y-4">
                            <div>
                                <label class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1.5">1. O que você precisa?</label>
                                <select id="sel-servico" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-sm text-white focus:outline-none focus:border-amber-400 transition" onchange="calcSimulador()">
                                    <option value="{config['services'][0]['title']}">{config['services'][0]['title']}</option>
                                    <option value="{config['services'][1]['title']}">{config['services'][1]['title']}</option>
                                    <option value="{config['services'][2]['title']}">{config['services'][2]['title']}</option>
                                </select>
                            </div>

                            <div>
                                <label class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1.5">2. Sua Localização:</label>
                                <select id="sel-local" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-sm text-white focus:outline-none focus:border-amber-400 transition" onchange="calcSimulador()">
                                    <option value="{neighborhood} (Miolo / Central)" data-tempo="10 a 18 min" data-dist="1.2 km">📍 {neighborhood} (Região Central)</option>
                                    <option value="Bairros Adjacentes / Vizinhança" data-tempo="15 a 25 min" data-dist="2.8 km">📍 Bairros Vizinhos de {city}</option>
                                    <option value="OUTRO_ENDERECO" data-tempo="A confirmar" data-dist="Sob consulta">📍 Outro bairro / endereço personalizado...</option>
                                </select>
                            </div>

                            <!-- Campo Outro Endereço Dinâmico -->
                            <div id="box-outro-endereco" class="hidden space-y-2 p-3.5 rounded-xl bg-slate-800/80 border border-amber-500/30">
                                <label class="block text-xs font-semibold text-amber-400 uppercase tracking-wider">
                                    <i class="fa-solid fa-map-location-dot mr-1"></i> Digite sua rua ou bairro:
                                </label>
                                <input type="text" id="input-outro" oninput="calcSimulador()" placeholder="Ex: Rua das Flores, Centro..." class="w-full bg-slate-900 border border-slate-700 rounded-lg px-3.5 py-2.5 text-sm text-white focus:outline-none focus:border-amber-400 transition">
                                <div class="p-2.5 rounded-lg bg-amber-500/10 border border-amber-500/20 text-amber-200 text-xs flex items-start gap-2.5">
                                    <i class="fa-solid fa-headset text-amber-400 text-sm mt-0.5 shrink-0"></i>
                                    <span><strong>Aviso de Atendimento:</strong> Nossa central entrará em contato imediatamente pelo WhatsApp para confirmar a viatura/técnico mais próximo da sua rota!</span>
                                </div>
                            </div>

                            <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-3.5">
                                <div class="flex items-center justify-between text-xs pb-2 border-b border-slate-800">
                                    <span class="text-slate-400">Previsão estimada:</span>
                                    <span id="disp-tempo" class="font-extrabold text-amber-400 text-sm">10 a 18 min</span>
                                </div>
                                <div class="flex items-center justify-between text-xs pt-2">
                                    <span class="text-slate-400">Base física de saída:</span>
                                    <span id="disp-dist" class="font-semibold text-slate-200 text-xs">~1.2 km ({address})</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="mt-5 space-y-2">
                        <a id="btn-whats" href="https://wa.me/{phone_clean}" target="_blank" class="w-full py-4 rounded-xl bg-gradient-to-r from-emerald-500 to-emerald-600 text-white font-bold text-base flex items-center justify-center gap-2.5 shadow-lg hover:brightness-110 transition">
                            <i class="fa-brands fa-whatsapp text-xl"></i>
                            <span>SOLICITAR ATENDIMENTO AGORA</span>
                        </a>
                        <p class="text-[11px] text-center text-slate-400">
                            <i class="fa-solid fa-lock text-amber-400 mr-1"></i> Preço fechado antes de sair • Sem taxas ocultas
                        </p>
                    </div>
                </div>
            </div>

        </div>

        <!-- Seção de Serviços -->
        <section class="py-16">
            <div class="max-w-2xl mb-10">
                <span class="text-amber-400 font-bold text-xs uppercase tracking-widest">{config['tag']}</span>
                <h2 class="text-3xl font-extrabold text-white mt-1">Serviços Especializados em {city}</h2>
            </div>
            <div class="grid md:grid-cols-3 gap-6">
                <div class="morphix-card p-6 rounded-2xl">
                    <h3 class="font-extrabold text-lg text-white">{config['services'][0]['title']}</h3>
                    <p class="text-slate-400 text-xs mt-2 leading-relaxed">{config['services'][0]['desc']}</p>
                </div>
                <div class="morphix-card p-6 rounded-2xl">
                    <h3 class="font-extrabold text-lg text-white">{config['services'][1]['title']}</h3>
                    <p class="text-slate-400 text-xs mt-2 leading-relaxed">{config['services'][1]['desc']}</p>
                </div>
                <div class="morphix-card p-6 rounded-2xl">
                    <h3 class="font-extrabold text-lg text-white">{config['services'][2]['title']}</h3>
                    <p class="text-slate-400 text-xs mt-2 leading-relaxed">{config['services'][2]['desc']}</p>
                </div>
            </div>
        </section>

        <!-- Base Física e Contato -->
        <section class="py-12 border-t border-slate-800">
            <div class="grid md:grid-cols-2 gap-8 items-center">
                <div>
                    <span class="text-amber-400 font-bold text-xs uppercase tracking-widest">Base Física Oficial</span>
                    <h3 class="text-2xl font-bold text-white mt-1">{nome}</h3>
                    <p class="text-slate-400 text-sm mt-2">{address} - {neighborhood}, {city} - {state}</p>
                    <p class="text-emerald-400 text-sm font-semibold mt-1">Telefone / WhatsApp: {phone_raw}</p>
                </div>
                <div class="text-right">
                    <a href="https://wa.me/{phone_clean}" target="_blank" class="inline-flex items-center gap-2 px-6 py-3.5 rounded-xl bg-gradient-to-r from-emerald-500 to-emerald-600 text-white font-bold text-sm shadow-lg">
                        <i class="fa-brands fa-whatsapp text-lg"></i>
                        <span>Falar no WhatsApp Oficial</span>
                    </a>
                </div>
            </div>
        </section>
    </main>

    <footer class="border-t border-slate-800 py-8 text-center text-xs text-slate-500">
        <p>© {datetime.now().year} {nome}. Todos os direitos reservados • {city} - {state}</p>
    </footer>

    <!-- Barra Fixa Mobile -->
    <div class="fixed bottom-0 left-0 right-0 z-50 sm:hidden bg-black/95 border-t border-slate-800 p-2.5 grid grid-cols-2 gap-2 backdrop-blur-lg">
        <a href="tel:+{phone_clean}" class="bg-slate-800 text-white font-bold py-3 rounded-xl flex items-center justify-center gap-2 text-xs">
            <i class="fa-solid fa-phone text-amber-400"></i> LIGAR
        </a>
        <a href="https://wa.me/{phone_clean}" target="_blank" class="bg-gradient-to-r from-emerald-500 to-emerald-600 text-white font-bold py-3 rounded-xl flex items-center justify-center gap-2 text-xs">
            <i class="fa-brands fa-whatsapp text-base"></i> WHATSAPP
        </a>
    </div>

    <script>
        function calcSimulador() {{
            const selServ = document.getElementById('sel-servico');
            const selLoc = document.getElementById('sel-local');
            const boxOutro = document.getElementById('box-outro-endereco');
            const inputOutro = document.getElementById('input-outro');

            const isOutro = (selLoc.value === 'OUTRO_ENDERECO');
            let tempo = selLoc.options[selLoc.selectedIndex].getAttribute('data-tempo') || '15 a 20 min';
            let dist = selLoc.options[selLoc.selectedIndex].getAttribute('data-dist') || '1.0 km';
            let locText = selLoc.value;

            if (isOutro) {{
                boxOutro.classList.remove('hidden');
                locText = inputOutro.value.trim() ? inputOutro.value.trim() : 'Endereço a confirmar';
                tempo = 'A confirmar imediatamente via WhatsApp';
                dist = 'Sob consulta';
            }} else {{
                boxOutro.classList.add('hidden');
            }}

            document.getElementById('disp-tempo').textContent = tempo;
            document.getElementById('disp-dist').textContent = dist.startsWith('~') ? dist : (dist === 'Sob consulta' ? dist : '~' + dist + ' ({address})');

            const msg = `Olá! Gostaria de orçamento na {nome}:\\n\\n` +
                        `🚨 *Serviço:* ${{selServ.value}}\\n` +
                        `📍 *Localização:* ${{locText}}\\n\\n` +
                        `Poderiam me informar a previsão de atendimento e o valor fechado?`;
            
            document.getElementById('btn-whats').href = `https://wa.me/{phone_clean}?text=${{encodeURIComponent(msg)}}`;
        }}
        document.addEventListener('DOMContentLoaded', calcSimulador);
    </script>
</body>
</html>"""

    pitch = (
        f"Olá, tudo bem?\n"
        f"Encontrei o perfil do *{nome}* no Google Maps aqui em *{neighborhood}* e vi a excelente avaliação de vocês ({rating}★).\n\n"
        f"Notei que quando clientes precisam de atendimento rápido pelo celular, eles preferem ter um simulador interativo com cálculo de tempo e botão direto para o seu WhatsApp.\n\n"
        f"Tomei a liberdade de montar uma demonstração ao vivo e exclusiva para o *{nome}*:\n"
        f"👉 [LINK_DA_DEMO]\n\n"
        f"Se fizer sentido para o seu negócio receber mais clientes prontos para fechar no WhatsApp, podemos ativar essa página para você hoje. O que achou do modelo?"
    )

    return slug, html, pitch
