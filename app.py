from flask import Flask, render_template_string

app = Flask(__name__, static_url_path='/assets', static_folder='assets')

# Dados estruturados da empresa com hiperlocalização no Tatuapé
BUSINESS_DATA = {
    "nome": "Chaveiro 24 Horas Tatuapé",
    "telefone_display": "(11) 97435-9641",
    "telefone_link": "5511974359641",
    "endereco": "Rua Domingos Agostim, 128",
    "bairro": "Cidade Mãe do Céu, Tatuapé",
    "cep": "03306-010",
    "cidade": "São Paulo - SP",
    "referencia": "A 200m do Metrô Tatuapé e Shopping Boulevard",
    "nota": "4.9",
    "total_avaliacoes": "184",
    "tempo_medio": "15 a 20 min",
    "regioes": [
        {"nome": "Tatuapé (Centro / Miolo)", "tempo": "12-18 min", "desc": "Rua Tuiuti, Itapura, Serra de Bragança e arredores"},
        {"nome": "Jardim Anália Franco", "tempo": "15-22 min", "desc": "Shopping Anália Franco, Av. Regente Feijó, Ceret"},
        {"nome": "Vila Gomes Cardim", "tempo": "12-18 min", "desc": "Rua Azevedo Soares, Emília Marengo e imediações"},
        {"nome": "Vila Carrão / Penha", "tempo": "18-25 min", "desc": "Conselheiro Carrão, Radial Leste"},
        {"nome": "Mooca / Belém / Água Rasa", "tempo": "18-25 min", "desc": "Salim Farah Maluf, Paes de Barros, Alcântara"}
    ]
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ data.nome }} | Socorro Emergencial 24h Residencial e Automotivo</title>
    <meta name="description" content="Trancado para fora no Tatuapé ou Anália Franco? Chegamos em até 20 minutos. Abertura técnica sem danificar fechaduras ou lataria de carros. Orçamento fechado por WhatsApp.">
    <meta name="theme-color" content="#070A12">

    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Google Fonts: Plus Jakarta Sans (Headings) e Inter (Body) -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@600;700;800;900&display=swap" rel="stylesheet">
    
    <!-- FontAwesome 6 Pro-style icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        heading: ['Plus Jakarta Sans', 'sans-serif'],
                    },
                    colors: {
                        void: '#070A12',
                        surface: {
                            base: '#0D1322',
                            card: '#131B2E',
                            border: '#1E2B48',
                            light: '#253556'
                        },
                        amberGlow: {
                            DEFAULT: '#F59E0B',
                            light: '#FBBF24',
                            dark: '#D97706',
                            deep: '#78350F'
                        },
                        techGreen: {
                            DEFAULT: '#10B981',
                            dark: '#059669',
                            glow: '#34D399'
                        }
                    },
                    boxShadow: {
                        'glow-amber': '0 0 35px -8px rgba(245, 158, 11, 0.35)',
                        'glow-green': '0 0 35px -8px rgba(16, 185, 129, 0.45)',
                        'morphix': '0 20px 40px -15px rgba(0, 0, 0, 0.7), inset 0 1px 0 0 rgba(255, 255, 255, 0.08)',
                        'morphix-inset': 'inset 0 2px 4px 0 rgba(0, 0, 0, 0.6), 0 1px 0 0 rgba(255, 255, 255, 0.05)',
                    }
                }
            }
        }
    </script>

    <style>
        /* Ambient Cinematic Lighting */
        .cinematic-bg {
            background-color: #070A12;
            background-image: 
                radial-gradient(circle at 15% 15%, rgba(245, 158, 11, 0.08) 0%, transparent 40%),
                radial-gradient(circle at 85% 30%, rgba(30, 43, 72, 0.35) 0%, transparent 50%),
                radial-gradient(circle at 50% 80%, rgba(16, 185, 129, 0.05) 0%, transparent 45%),
                linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
            background-size: 100% 100%, 100% 100%, 100% 100%, 36px 36px, 36px 36px;
        }

        /* Glassmorphism Morphix Panel */
        .morphix-panel {
            background: linear-gradient(135deg, rgba(19, 27, 46, 0.88) 0%, rgba(13, 19, 34, 0.95) 100%);
            backdrop-filter: blur(18px);
            -webkit-backdrop-filter: blur(18px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 24px 48px -12px rgba(0, 0, 0, 0.7), inset 0 1px 0 rgba(255, 255, 255, 0.1);
        }

        .morphix-panel:hover {
            border-color: rgba(245, 158, 11, 0.25);
        }

        /* Interactive Card Spotlight */
        .morphix-card {
            background: linear-gradient(145deg, #131B2E 0%, #0D1322 100%);
            border: 1px solid rgba(255, 255, 255, 0.06);
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .morphix-card:hover {
            transform: translateY(-4px);
            border-color: rgba(245, 158, 11, 0.3);
            box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.8), 0 0 25px -8px rgba(245, 158, 11, 0.15);
        }

        /* Micro-Animations & Radar */
        @keyframes radar-sweep {
            0% { transform: scale(0.95); opacity: 0.8; }
            50% { transform: scale(1.6); opacity: 0; }
            100% { transform: scale(0.95); opacity: 0; }
        }

        .radar-pulse {
            animation: radar-sweep 2.2s infinite ease-out;
        }

        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #070A12;
        }
        ::-webkit-scrollbar-thumb {
            background: #1E2B48;
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #F59E0B;
        }
    </style>
</head>
<body class="cinematic-bg text-slate-200 antialiased selection:bg-amberGlow selection:text-void font-sans">

    <!-- 1. TOP BAR RADAR DE PLANTÃO (Urgência Real & Posicionamento GPS) -->
    <aside aria-label="Status do Plantão" class="bg-void/90 border-b border-surface-border/60 py-2.5 px-4 text-xs sticky top-0 z-50 backdrop-blur-md">
        <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3">
            
            <!-- Radar Blip -->
            <div class="flex items-center gap-2.5">
                <span class="relative flex h-3 w-3 items-center justify-center">
                    <span class="radar-pulse absolute inline-flex h-full w-full rounded-full bg-techGreen opacity-75"></span>
                    <span class="relative inline-flex rounded-full h-2 w-2 bg-techGreen"></span>
                </span>
                <span class="font-bold text-white tracking-wide uppercase text-[11px] sm:text-xs">
                    Plantão Móvel Ativo: <span class="text-amberGlow font-semibold normal-case">Tatuapé & Anália Franco</span>
                </span>
                <span class="hidden md:inline-flex items-center gap-1.5 text-slate-400 border-l border-slate-700 pl-3">
                    <i class="fa-solid fa-stopwatch text-amberGlow"></i> Chegada estimada agora: <strong class="text-white">{{ data.tempo_medio }}</strong>
                </span>
            </div>

            <!-- Base Física Real -->
            <div class="flex items-center gap-4 text-slate-400 text-[11px] sm:text-xs">
                <span class="hidden sm:inline">
                    <i class="fa-solid fa-location-dot text-amberGlow mr-1"></i> Base física: <strong class="text-slate-200">{{ data.endereco }}</strong> (Metrô Tatuapé)
                </span>
                <span class="inline-flex items-center gap-1 text-techGreen font-semibold">
                    <i class="fa-solid fa-bolt text-xs"></i> Socorro Rápido
                </span>
            </div>

        </div>
    </aside>

    <!-- 2. NAVBAR COM GLASSMORPHISM & BOTÕES TÁTEIS -->
    <header class="border-b border-white/5 py-4 px-4 sm:px-8 bg-surface-base/80 backdrop-blur-xl relative z-40">
        <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
            
            <!-- Marca com Identidade Artesanal e Sólida -->
            <a href="#" class="flex items-center gap-3.5 group">
                <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-amberGlow to-amberGlow-dark p-[1px] shadow-glow-amber transition transform group-hover:scale-105">
                    <div class="w-full h-full bg-void rounded-[11px] flex items-center justify-center text-amberGlow">
                        <i class="fa-solid fa-key text-xl"></i>
                    </div>
                </div>
                <div>
                    <div class="flex items-center gap-2">
                        <span class="font-heading font-extrabold text-lg sm:text-xl text-white tracking-tight leading-none">CHAVEIRO TATUAPÉ</span>
                        <span class="bg-amberGlow/10 border border-amberGlow/30 text-amberGlow text-[10px] font-bold px-2 py-0.5 rounded-full uppercase tracking-wider hidden sm:inline">24 Horas</span>
                    </div>
                    <span class="text-xs text-slate-400 font-medium block mt-1">Especialistas em Aberturas Sem Danos</span>
                </div>
            </a>

            <!-- Navegação Desktop -->
            <nav class="hidden lg:flex items-center gap-8 text-sm font-medium text-slate-300">
                <a href="#simulador" class="hover:text-amberGlow transition flex items-center gap-1.5"><i class="fa-solid fa-calculator text-xs text-amberGlow"></i> Orçamento Rápido</a>
                <a href="#servicos" class="hover:text-amberGlow transition">Serviços Técnicos</a>
                <a href="#seguranca" class="hover:text-amberGlow transition">Protocolo Anti-Golpe</a>
                <a href="#avaliacoes" class="hover:text-amberGlow transition flex items-center gap-1">Avaliações <span class="text-amberGlow text-xs">({{ data.nota }}★)</span></a>
                <a href="#base-fisica" class="hover:text-amberGlow transition">Localização</a>
            </nav>

            <!-- Ações Diretas no Topo -->
            <div class="flex items-center gap-3">
                <a href="tel:+{{ data.telefone_link }}" 
                   class="hidden sm:inline-flex items-center gap-2.5 px-4 py-2.5 rounded-xl bg-surface-card border border-surface-border text-slate-200 hover:text-white hover:border-amberGlow/50 transition text-sm font-semibold shadow-morphix-inset">
                    <i class="fa-solid fa-phone text-amberGlow animate-pulse"></i>
                    <span>{{ data.telefone_display }}</span>
                </a>

                <a href="https://wa.me/{{ data.telefone_link }}?text=Ol%C3%A1,%20estou%20no%20Tatuap%C3%A9%20e%20preciso%20de%20um%20chaveiro%20com%20urg%C3%AAncia."
                   target="_blank"
                   class="inline-flex items-center gap-2 px-4 sm:px-5 py-2.5 rounded-xl bg-gradient-to-r from-techGreen to-techGreen-dark text-white font-heading font-bold text-sm shadow-glow-green hover:brightness-110 active:scale-95 transition">
                    <i class="fa-brands fa-whatsapp text-lg"></i>
                    <span class="hidden sm:inline">Chamar no WhatsApp</span>
                    <span class="sm:hidden">WhatsApp</span>
                </a>
            </div>

        </div>
    </header>

    <!-- 3. HERO CINEMÁTICO: ULTRA-VISUAL COM IMAGENS REAIS E SIMULADOR INTEGRADO -->
    <main>
    <section class="relative pt-8 pb-16 px-4 sm:px-8 overflow-hidden">
        <!-- Glows de Iluminação Volumétrica Noturna -->
        <div class="absolute top-1/4 -left-32 w-96 h-96 bg-amberGlow/10 rounded-full blur-[120px] pointer-events-none"></div>
        <div class="absolute bottom-10 right-0 w-[500px] h-[500px] bg-surface-border/30 rounded-full blur-[150px] pointer-events-none"></div>

        <div class="max-w-7xl mx-auto relative z-10">
            
            <!-- Linha 1 do Hero: Proposta de Valor e Apresentação -->
            <div class="max-w-3xl mb-8 space-y-4">
                <div class="inline-flex items-center gap-2.5 px-3.5 py-1.5 rounded-full bg-surface-card/80 border border-surface-border text-xs text-slate-300 shadow-morphix-inset">
                    <span class="flex text-amber-400 text-xs">
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                    </span>
                    <span class="font-bold text-white">{{ data.nota }}/5.0 no Google Maps</span>
                    <span class="text-slate-500">•</span>
                    <span class="text-slate-400 font-medium">+10 anos no Tatuapé</span>
                </div>

                <h1 class="font-heading text-3xl sm:text-5xl lg:text-6xl font-extrabold text-white tracking-tight leading-[1.12]">
                    Ficou trancado para fora no Tatuapé? <br>
                    <span class="bg-gradient-to-r from-amberGlow via-amber-300 to-amberGlow-dark bg-clip-text text-transparent">
                        Chegamos em 20 minutos sem arrombar sua porta.
                    </span>
                </h1>

                <p class="text-slate-300 text-base sm:text-lg leading-relaxed max-w-2xl font-normal">
                    Você na calçada às 2h da manhã não pode esperar ninguém inventar preço. Atendimento técnico de urgência no <strong class="text-white">Tatuapé, Jardim Anália Franco e região</strong>. Valor fechado passado por foto antes da moto sair da base.
                </p>

                <!-- Botões de Ação Rápida de Topo -->
                <div class="flex flex-wrap items-center gap-3 pt-1">
                    <a href="https://wa.me/{{ data.telefone_link }}?text=Ol%C3%A1!%20Fiquei%20trancado%20para%20fora%20aqui%20no%20Tatuap%C3%A9%20e%20preciso%20de%20socorro%20urgente."
                       target="_blank"
                       class="px-7 py-3.5 rounded-xl bg-gradient-to-r from-techGreen to-techGreen-dark text-white font-heading font-extrabold text-sm sm:text-base flex items-center justify-center gap-2.5 shadow-glow-green hover:brightness-110 active:scale-95 transition">
                        <i class="fa-brands fa-whatsapp text-xl"></i>
                        <span>CHAMAR SOCORRO NO WHATSAPP</span>
                    </a>

                    <a href="tel:+{{ data.telefone_link }}"
                       class="px-5 py-3.5 rounded-xl bg-surface-card border border-surface-border hover:border-amberGlow/50 text-white font-heading font-bold text-sm flex items-center justify-center gap-2 transition shadow-morphix-inset">
                        <i class="fa-solid fa-phone-volume text-amberGlow"></i>
                        <span>LIGAR DIRETO (24H)</span>
                    </a>
                </div>
            </div>

            <!-- Linha 2 do Hero: Grid Duplo (Showcase Visual Fotográfico + Calculadora Interativa) -->
            <div class="grid lg:grid-cols-12 gap-8 items-stretch">
                
                <!-- COLUNA VISUAL COM IMAGENS CINEMATOGRÁFICAS REAIS (6 colunas) -->
                <div class="lg:col-span-6 flex flex-col justify-between gap-4">
                    
                    <!-- Imagem Principal 1: Técnico em Ação com Lanterna Noturna -->
                    <div class="relative rounded-2xl overflow-hidden border border-surface-border shadow-2xl group flex-1 min-h-[320px]">
                        <img src="assets/img/hero_chaveiro.jpg" 
                             alt="Técnico Chaveiro realizando abertura técnica noturna no Tatuapé com iluminação focada" 
                             class="w-full h-full object-cover object-center brightness-95 group-hover:scale-105 transition duration-700">
                        <div class="absolute inset-0 bg-gradient-to-t from-void via-void/30 to-transparent"></div>

                        <!-- Badge Flutuante no Topo da Foto -->
                        <div class="absolute top-4 left-4 right-4 flex items-center justify-between gap-2">
                            <span class="inline-flex items-center gap-2 bg-void/90 backdrop-blur-md border border-white/10 px-3.5 py-1.5 rounded-xl text-xs font-bold text-white shadow-lg">
                                <span class="w-2 h-2 rounded-full bg-techGreen animate-pulse"></span>
                                Viatura 02 em Plantão Noturno
                            </span>
                            <span class="bg-amberGlow text-void font-heading font-black text-[11px] px-2.5 py-1 rounded-lg uppercase tracking-wider shadow">
                                24 Horas
                            </span>
                        </div>

                        <!-- Card Flutuante Inferior com Detalhes da Foto -->
                        <div class="absolute bottom-4 left-4 right-4 bg-surface-base/95 backdrop-blur-md p-4 rounded-xl border border-surface-border shadow-xl">
                            <div class="flex items-center justify-between gap-3">
                                <div>
                                    <p class="text-xs font-bold uppercase tracking-wider text-amberGlow flex items-center gap-1.5">
                                        <i class="fa-solid fa-shield-halved"></i> Ferramental de Precisão Alemã
                                    </p>
                                    <p class="text-sm font-semibold text-white mt-0.5">Abertura técnica sem danificar miolo nem fechadura</p>
                                    <p class="text-[11px] text-slate-400 mt-0.5">Atendimentos residenciais em prédios e casas da Zona Leste</p>
                                </div>
                                <div class="w-10 h-10 rounded-xl bg-amberGlow/10 text-amberGlow flex items-center justify-center shrink-0 border border-amberGlow/20">
                                    <i class="fa-solid fa-key text-lg"></i>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Imagem Secundária 2: Banner Automotivo Lishi (Picture-in-Picture Bar) -->
                    <div class="morphix-panel p-4 rounded-2xl flex items-center gap-4">
                        <div class="w-20 h-20 rounded-xl overflow-hidden shrink-0 border border-surface-border relative">
                            <img src="assets/img/auto_chaveiro.jpg" 
                                 alt="Decodificador Lishi em fechadura automotiva" 
                                 class="w-full h-full object-cover">
                            <div class="absolute inset-0 bg-amberGlow/10"></div>
                        </div>
                        <div class="flex-1 min-w-0">
                            <div class="flex items-center gap-2">
                                <span class="text-xs font-bold text-amberGlow uppercase tracking-wider">Socorro Automotivo Lishi</span>
                                <span class="text-[10px] bg-techGreen/20 text-techGreen px-2 py-0.5 rounded font-semibold">Sem Riscos</span>
                            </div>
                            <h4 class="font-heading font-bold text-sm text-white mt-0.5 truncate">Chave trancada dentro do carro?</h4>
                            <p class="text-xs text-slate-400 mt-0.5">Abrimos pelo cilindro sem entortar a coluna e sem estragar a borracha da porta.</p>
                        </div>
                    </div>

                </div>

                <!-- COLUNA DO SIMULADOR MORPHIX COM OPÇÃO DE OUTRO ENDEREÇO (6 colunas) -->
                <div class="lg:col-span-6" id="simulador">
                    <div class="morphix-panel p-6 sm:p-7 rounded-2xl relative h-full flex flex-col justify-between">
                        
                        <!-- Header do Simulador -->
                        <div>
                            <div class="flex items-center justify-between pb-4 border-b border-surface-border">
                                <div>
                                    <span class="text-amberGlow font-bold text-[11px] uppercase tracking-wider flex items-center gap-1.5">
                                        <span class="w-2 h-2 rounded-full bg-techGreen animate-ping"></span>
                                        Calculadora de Deslocamento
                                    </span>
                                    <h3 class="font-heading font-extrabold text-xl text-white mt-1">
                                        Simular Socorro e Tempo de Chegada
                                    </h3>
                                </div>
                                <div class="w-10 h-10 rounded-xl bg-surface-card border border-surface-border flex items-center justify-center text-amberGlow">
                                    <i class="fa-solid fa-sliders"></i>
                                </div>
                            </div>

                            <!-- Formulário Interativo -->
                            <div class="mt-4 space-y-4">
                                
                                <!-- Passo 1: O que aconteceu? -->
                                <div>
                                    <label for="select-problema" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1.5">
                                        1. Qual é a sua urgência?
                                    </label>
                                    <select id="select-problema" onchange="atualizarSimulador()" 
                                            class="w-full bg-surface-base border border-surface-border rounded-xl px-4 py-3 text-sm text-white font-medium focus:outline-none focus:border-amberGlow transition cursor-pointer">
                                        <option value="Trancado fora de casa (porta fechada)">🚪 Trancado(a) para fora de casa/apto</option>
                                        <option value="Chave trancada dentro do carro">🚗 Chave trancada dentro do veículo</option>
                                        <option value="Chave quebrada dentro da fechadura">🗝️ Chave quebrou dentro do miolo</option>
                                        <option value="Troca de segredo / cilindro urgente">🔒 Perdi a chave / Trocar segredo agora</option>
                                        <option value="Instalação ou conserto de fechadura digital">📱 Fechadura digital (instalação/reparo)</option>
                                    </select>
                                </div>

                                <!-- Passo 2: Onde você está? (Com opção de outro endereço) -->
                                <div>
                                    <label for="select-bairro" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1.5">
                                        2. Onde você está localizado(a)?
                                    </label>
                                    <select id="select-bairro" onchange="atualizarSimulador()" 
                                            class="w-full bg-surface-base border border-surface-border rounded-xl px-4 py-3 text-sm text-white font-medium focus:outline-none focus:border-amberGlow transition cursor-pointer">
                                        <option value="Tatuapé (Centro / Miolo)" data-tempo="12 a 18 min" data-dist="0.8 km">📍 Tatuapé (R. Tuiuti, Itapura, Serra de Bragança)</option>
                                        <option value="Jardim Anália Franco" data-tempo="15 a 20 min" data-dist="1.9 km">📍 Jardim Anália Franco (Próx. Shopping / Ceret)</option>
                                        <option value="Vila Gomes Cardim" data-tempo="12 a 18 min" data-dist="1.2 km">📍 Vila Gomes Cardim (Azevedo Soares / Emília Marengo)</option>
                                        <option value="Vila Carrão" data-tempo="18 a 22 min" data-dist="2.8 km">📍 Vila Carrão / Conselheiro Carrão</option>
                                        <option value="Mooca ou Belém" data-tempo="18 a 25 min" data-dist="3.4 km">📍 Mooca / Belém / Salim Farah Maluf</option>
                                        <option value="OUTRO_ENDERECO" data-tempo="A confirmar" data-dist="Sob consulta">📍 Outro bairro / endereço personalizado...</option>
                                    </select>
                                </div>

                                <!-- CAMPO DINÂMICO PARA OUTRO ENDEREÇO (Aparece ao selecionar a opção) -->
                                <div id="container-outro-endereco" class="hidden space-y-2 p-3.5 rounded-xl bg-surface-card border border-amberGlow/30 animate-fadeIn">
                                    <label for="input-outro-endereco" class="block text-xs font-semibold text-amberGlow uppercase tracking-wider">
                                        <i class="fa-solid fa-map-location-dot mr-1"></i> Digite seu bairro ou endereço:
                                    </label>
                                    <input type="text" 
                                           id="input-outro-endereco" 
                                           oninput="atualizarSimulador()"
                                           placeholder="Ex: Av. Celso Garcia, Brás, Penha, Vila Matilde..." 
                                           class="w-full bg-surface-base border border-surface-border rounded-lg px-3.5 py-2.5 text-sm text-white focus:outline-none focus:border-amberGlow transition">
                                    
                                    <!-- AVISO DE CONTATO IMEDIATO DO PROFISSIONAL -->
                                    <div class="p-2.5 rounded-lg bg-amberGlow/10 border border-amberGlow/20 text-amber-200 text-xs flex items-start gap-2.5 leading-relaxed">
                                        <i class="fa-solid fa-headset text-amberGlow text-sm mt-0.5 shrink-0"></i>
                                        <span>
                                            <strong>Aviso de Atendimento:</strong> Nossa central entrará em contato imediatamente pelo WhatsApp para confirmar a viatura mais próxima da sua rota e informar o valor fechado antes do deslocamento.
                                        </span>
                                    </div>
                                </div>

                                <!-- Passo 3: Tipo da Porta/Carro -->
                                <div>
                                    <label for="select-tipo" class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1.5">
                                        3. Tipo de Fechadura / Veículo:
                                    </label>
                                    <select id="select-tipo" onchange="atualizarSimulador()" 
                                            class="w-full bg-surface-base border border-surface-border rounded-xl px-4 py-3 text-sm text-white font-medium focus:outline-none focus:border-amberGlow transition cursor-pointer">
                                        <option value="Porta Comum (Chave Yale simples)">Porta comum de madeira / Chave simples</option>
                                        <option value="Fechadura Tetra ou Multiponto">Fechadura Tetra / Chave Multiponto</option>
                                        <option value="Porta Blindada ou Pivotante">Porta Blindada / Fechadura de alta segurança</option>
                                        <option value="Carro Nacional">Veículo Nacional (Abertura pelo cilindro)</option>
                                        <option value="Carro Importado / Blindado">Veículo Importado / Sistema pantográfico</option>
                                    </select>
                                </div>

                                <!-- Painel Dinâmico de Estimativa Morphix -->
                                <div class="bg-surface-base/90 border border-surface-border rounded-xl p-3.5">
                                    <div class="flex items-center justify-between text-xs pb-2 border-b border-surface-border/50">
                                        <span class="text-slate-400">Tempo estimado da viatura:</span>
                                        <span id="display-tempo" class="font-heading font-extrabold text-amberGlow text-sm">12 a 18 min</span>
                                    </div>
                                    <div class="flex items-center justify-between text-xs pt-2">
                                        <span class="text-slate-400">Distância da base fixa:</span>
                                        <span id="display-dist" class="font-semibold text-slate-200 text-xs">~0.8 km (R. Domingos Agostim)</span>
                                    </div>
                                </div>

                            </div>
                        </div>

                        <!-- Botão Dinâmico de WhatsApp com Link Pré-formatado -->
                        <div class="mt-5 space-y-2">
                            <a id="btn-whatsapp-simulador" 
                               href="https://wa.me/{{ data.telefone_link }}?text=Ol%C3%A1,%20estou%20no%20Tatuap%C3%A9%20e%20preciso%20de%20chaveiro%20urgente." 
                               target="_blank"
                               class="w-full py-4 rounded-xl bg-gradient-to-r from-techGreen to-techGreen-dark text-white font-heading font-bold text-base flex items-center justify-center gap-2.5 shadow-glow-green hover:brightness-110 active:scale-95 transition">
                                <i class="fa-brands fa-whatsapp text-xl"></i>
                                <span>SOLICITAR ATENDIMENTO AGORA</span>
                            </a>

                            <p class="text-[11px] text-center text-slate-400">
                                <i class="fa-solid fa-lock text-amberGlow mr-1"></i> Preço fechado antes de sair • Sem cobranças surpresa
                            </p>
                        </div>

                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- 4. RUA A RUA: HIPERLOCALIZAÇÃO REAL DO TATUAPÉ -->
    <section class="border-y border-surface-border/80 bg-surface-base/60 py-6 px-4">
        <div class="max-w-7xl mx-auto">
            <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
                
                <div class="flex items-center gap-2 text-xs font-bold text-amberGlow uppercase tracking-wider shrink-0">
                    <i class="fa-solid fa-route text-base"></i>
                    <span>Deslocamento Imediato no Bairro:</span>
                </div>

                <div class="flex flex-wrap items-center gap-2 text-xs font-medium text-slate-300">
                    <span class="bg-surface-card px-3 py-1.5 rounded-lg border border-surface-border">Praça Silvio Romero</span>
                    <span class="bg-surface-card px-3 py-1.5 rounded-lg border border-surface-border">Rua Tuiuti</span>
                    <span class="bg-surface-card px-3 py-1.5 rounded-lg border border-surface-border">Rua Serra de Bragança</span>
                    <span class="bg-surface-card px-3 py-1.5 rounded-lg border border-surface-border">Rua Itapura</span>
                    <span class="bg-surface-card px-3 py-1.5 rounded-lg border border-surface-border">Rua Azevedo Soares</span>
                    <span class="bg-surface-card px-3 py-1.5 rounded-lg border border-surface-border">Shopping Anália Franco</span>
                    <span class="bg-surface-card px-3 py-1.5 rounded-lg border border-surface-border">Rua Emília Marengo</span>
                    <span class="bg-surface-card px-3 py-1.5 rounded-lg border border-surface-border">Radial Leste / Metrô</span>
                </div>

            </div>
        </div>
    </section>

    <!-- 5. SERVIÇOS TÉCNICOS COM DETALHAMENTO DE PROFISSÃO -->
    <section id="servicos" class="py-20 px-4 sm:px-8 max-w-7xl mx-auto">
        <div class="max-w-3xl mb-14">
            <span class="text-amberGlow font-bold text-xs uppercase tracking-widest flex items-center gap-2">
                <i class="fa-solid fa-wrench"></i> Ferramental Profissional Especializado
            </span>
            <h2 class="font-heading text-3xl sm:text-4xl font-extrabold text-white mt-2">
                Serviços de Chaveiro sem Danificar Portas ou Pinturas
            </h2>
            <p class="text-slate-400 mt-3 text-base leading-relaxed">
                Não usamos furadeira nem métodos destrutivos sem real necessidade. Trabalhamos com gazuas pantográficas, michas automotivas Lishi e decodificadores que abrem pelo segredo mecânico original.
            </p>
        </div>

        <div class="grid md:grid-cols-3 gap-8">
            
            <!-- Card 1: Residencial & Fechaduras -->
            <div class="morphix-card rounded-2xl overflow-hidden flex flex-col justify-between">
                <div>
                    <div class="h-56 relative overflow-hidden bg-void">
                        <img src="assets/img/hero_chaveiro.jpg" 
                             alt="Fechadura residencial com chave de alta segurança" 
                             class="w-full h-full object-cover opacity-85 hover:scale-105 transition duration-700">
                        <div class="absolute inset-0 bg-gradient-to-t from-surface-card via-transparent to-transparent"></div>
                        <span class="absolute top-4 left-4 bg-void/90 border border-white/10 text-amberGlow text-xs font-bold px-3 py-1.5 rounded-lg backdrop-blur-md">
                            <i class="fa-solid fa-house-chimney mr-1"></i> Residencial
                        </span>
                    </div>

                    <div class="p-6">
                        <h3 class="font-heading font-extrabold text-xl text-white">Aberturas & Troca de Segredo</h3>
                        <p class="text-slate-400 text-sm mt-2 leading-relaxed">
                            Abertura técnica de portas comuns, tetra e blindadas. Em caso de perda, furto de chaves ou mudança de imóvel, trocamos o cilindro na hora com chaves novas lacradas.
                        </p>

                        <div class="mt-5 pt-5 border-t border-surface-border space-y-2.5 text-xs text-slate-300 font-medium">
                            <div class="flex items-center gap-2">
                                <i class="fa-solid fa-circle-check text-techGreen"></i>
                                <span>Chaves Yale, Tetra, Multiponto e Gorges</span>
                            </div>
                            <div class="flex items-center gap-2">
                                <i class="fa-solid fa-circle-check text-techGreen"></i>
                                <span>Extração de chave quebrada no miolo</span>
                            </div>
                            <div class="flex items-center gap-2">
                                <i class="fa-solid fa-circle-check text-techGreen"></i>
                                <span>Unificação de segredos (1 chave para portão e porta)</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="p-6 pt-0">
                    <a href="https://wa.me/{{ data.telefone_link }}?text=Ol%C3%A1,%20preciso%20de%20atendimento%20residencial%20no%20Tatuap%C3%A9."
                       target="_blank"
                       class="w-full py-3 px-4 rounded-xl bg-surface-base border border-surface-border hover:border-amberGlow/50 text-white font-semibold text-sm flex items-center justify-center gap-2 transition">
                        <i class="fa-brands fa-whatsapp text-techGreen"></i> Orçar Abertura Residencial
                    </a>
                </div>
            </div>

            <!-- Card 2: Automotivo de Precisão (Com Foto Real Lishi) -->
            <div class="morphix-card rounded-2xl overflow-hidden flex flex-col justify-between">
                <div>
                    <div class="h-56 relative overflow-hidden bg-void">
                        <img src="assets/img/auto_chaveiro.jpg" 
                             alt="Chave automotiva canivete e codificação Lishi" 
                             class="w-full h-full object-cover opacity-85 hover:scale-105 transition duration-700">
                        <div class="absolute inset-0 bg-gradient-to-t from-surface-card via-transparent to-transparent"></div>
                        <span class="absolute top-4 left-4 bg-void/90 border border-white/10 text-amberGlow text-xs font-bold px-3 py-1.5 rounded-lg backdrop-blur-md">
                            <i class="fa-solid fa-car mr-1"></i> Automotivo 24h
                        </span>
                    </div>

                    <div class="p-6">
                        <h3 class="font-heading font-extrabold text-xl text-white">Carros Trancados & Chave Codificada</h3>
                        <p class="text-slate-400 text-sm mt-2 leading-relaxed">
                            Chave ficou trancada no contato ou no porta-malas? Abrimos carros nacionais e importados pelo miolo da maçaneta com gazuas Lishi, sem forçar borrachas nem arranhar.
                        </p>

                        <div class="mt-5 pt-5 border-t border-surface-border space-y-2.5 text-xs text-slate-300 font-medium">
                            <div class="flex items-center gap-2">
                                <i class="fa-solid fa-circle-check text-techGreen"></i>
                                <span>Abertura técnica sem entortar a quina da porta</span>
                            </div>
                            <div class="flex items-center gap-2">
                                <i class="fa-solid fa-circle-check text-techGreen"></i>
                                <span>Cópia de chaves canivete e chave de presença</span>
                            </div>
                            <div class="flex items-center gap-2">
                                <i class="fa-solid fa-circle-check text-techGreen"></i>
                                <span>Conserto de miolo de ignição e telecomandos</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="p-6 pt-0">
                    <a href="https://wa.me/{{ data.telefone_link }}?text=Ol%C3%A1,%20preciso%20de%20socorro%20automotivo%20no%20Tatuap%C3%A9."
                       target="_blank"
                       class="w-full py-3 px-4 rounded-xl bg-surface-base border border-surface-border hover:border-amberGlow/50 text-white font-semibold text-sm flex items-center justify-center gap-2 transition">
                        <i class="fa-brands fa-whatsapp text-techGreen"></i> Destrancar Meu Veículo
                    </a>
                </div>
            </div>

            <!-- Card 3: Fechaduras Digitais -->
            <div id="fechaduras-digitais" class="morphix-card rounded-2xl overflow-hidden flex flex-col justify-between">
                <div>
                    <div class="h-56 relative overflow-hidden bg-void">
                        <img src="https://images.unsplash.com/photo-1563013544-824ae1b704d3?auto=format&fit=crop&w=800&q=80" 
                             alt="Fechadura digital biométrica com leitor de senha" 
                             class="w-full h-full object-cover opacity-80 hover:scale-105 transition duration-700">
                        <div class="absolute inset-0 bg-gradient-to-t from-surface-card via-transparent to-transparent"></div>
                        <span class="absolute top-4 left-4 bg-void/90 border border-white/10 text-amberGlow text-xs font-bold px-3 py-1.5 rounded-lg backdrop-blur-md">
                            <i class="fa-solid fa-fingerprint mr-1"></i> Biometria & Digital
                        </span>
                    </div>

                    <div class="p-6">
                        <h3 class="font-heading font-extrabold text-xl text-white">Fechaduras Digitais & Eletrônicas</h3>
                        <p class="text-slate-400 text-sm mt-2 leading-relaxed">
                            Instalação com gabarito de fábrica para portas de madeira maciça, ferro, vidro ou alumínio. Configuração de senhas, biometrias e tags no local com orientação completa.
                        </p>

                        <div class="mt-5 pt-5 border-t border-surface-border space-y-2.5 text-xs text-slate-300 font-medium">
                            <div class="flex items-center gap-2">
                                <i class="fa-solid fa-circle-check text-techGreen"></i>
                                <span>Intelbras, Samsung, Yale, Papaiz, Elsys e Pado</span>
                            </div>
                            <div class="flex items-center gap-2">
                                <i class="fa-solid fa-circle-check text-techGreen"></i>
                                <span>Modelos de embutir com maçaneta ou sobrepor</span>
                            </div>
                            <div class="flex items-center gap-2">
                                <i class="fa-solid fa-circle-check text-techGreen"></i>
                                <span>Instalação limpa com aspirador e acabamento</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="p-6 pt-0">
                    <a href="https://wa.me/{{ data.telefone_link }}?text=Ol%C3%A1,%20gostaria%20de%20or%C3%A7ar%20a%20instala%C3%A7%C3%A3o%20de%20uma%20fechadura%20digital."
                       target="_blank"
                       class="w-full py-3 px-4 rounded-xl bg-surface-base border border-surface-border hover:border-amberGlow/50 text-white font-semibold text-sm flex items-center justify-center gap-2 transition">
                        <i class="fa-brands fa-whatsapp text-techGreen"></i> Agendar Instalação
                    </a>
                </div>
            </div>

        </div>
    </section>

    <!-- 6. PROTOCOLO DE SEGURANÇA & TRANSPARÊNCIA (ANTI-GOLPE) -->
    <section id="seguranca" class="py-16 px-4 sm:px-8 border-y border-surface-border bg-surface-card/40">
        <div class="max-w-7xl mx-auto">
            <div class="grid lg:grid-cols-12 gap-10 items-center">
                
                <div class="lg:col-span-5 space-y-4">
                    <span class="text-amberGlow font-bold text-xs uppercase tracking-widest flex items-center gap-2">
                        <i class="fa-solid fa-shield-halved"></i> Segurança do Cliente & Condomínio
                    </span>
                    <h2 class="font-heading text-2xl sm:text-3xl font-extrabold text-white">
                        Por que moradores e síndicos do Tatuapé confiam no nosso trabalho?
                    </h2>
                    <p class="text-slate-300 text-sm leading-relaxed">
                        No desespero de estar trancado para fora, muitos contratam chaveiros clandestinos que quebram a fechadura para forçar a compra de peças caras ou cobram valores abusivos no local. Aqui temos um protocolo rígido:
                    </p>
                </div>

                <div class="lg:col-span-7 grid sm:grid-cols-2 gap-5">
                    
                    <div class="morphix-panel p-5 rounded-xl">
                        <div class="text-amberGlow text-2xl mb-2 font-heading font-black">01.</div>
                        <h4 class="font-heading font-bold text-base text-white">Preço Combinado Antes</h4>
                        <p class="text-slate-400 text-xs mt-1 leading-relaxed">
                            Você nos envia a foto da fechadura pelo WhatsApp e passamos o valor exato. Sem "taxa de chegada" surpresa ou pegadinha.
                        </p>
                    </div>

                    <div class="morphix-panel p-5 rounded-xl">
                        <div class="text-amberGlow text-2xl mb-2 font-heading font-black">02.</div>
                        <h4 class="font-heading font-bold text-base text-white">Conferência de Documento</h4>
                        <p class="text-slate-400 text-xs mt-1 leading-relaxed">
                            Para abrir residências ou carros, solicitamos comprovante ou documento no local. Proteção garantida para você e sua família.
                        </p>
                    </div>

                    <div class="morphix-panel p-5 rounded-xl">
                        <div class="text-amberGlow text-2xl mb-2 font-heading font-black">03.</div>
                        <h4 class="font-heading font-bold text-base text-white">Ferramentas Não-Destrutivas</h4>
                        <p class="text-slate-400 text-xs mt-1 leading-relaxed">
                            Mais de 95% das portas são abertas mantendo o mesmo miolo e fechadura funcionando perfeitamente sem dano estético.
                        </p>
                    </div>

                    <div class="morphix-panel p-5 rounded-xl">
                        <div class="text-amberGlow text-2xl mb-2 font-heading font-black">04.</div>
                        <h4 class="font-heading font-bold text-base text-white">Base Física Estabelecida</h4>
                        <p class="text-slate-400 text-xs mt-1 leading-relaxed">
                            Não somos intermediários virtuais. Temos loja fixa na Rua Domingos Agostim, 128 (ao lado do Metrô Tatuapé).
                        </p>
                    </div>

                </div>

            </div>
        </div>
    </section>

    <!-- 7. PROVA SOCIAL AUTÊNTICA (GOOGLE MAPS REALISTA COM BAIRROS DO TATUAPÉ) -->
    <section id="avaliacoes" class="py-20 px-4 sm:px-8 max-w-7xl mx-auto">
        <div class="flex flex-col md:flex-row md:items-end justify-between mb-12 gap-6">
            <div>
                <div class="flex items-center gap-2 mb-2">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/c/c1/Google_%22G%22_logo.svg" alt="Google" class="w-5 h-5">
                    <span class="text-xs font-bold uppercase tracking-wider text-slate-400">Avaliações Verificadas no Google Maps</span>
                </div>
                <h2 class="font-heading text-3xl sm:text-4xl font-extrabold text-white">
                    Histórias reais de quem precisou de socorro
                </h2>
            </div>

            <!-- Box Nota Google -->
            <div class="bg-surface-card border border-surface-border p-4 rounded-xl flex items-center gap-4 shrink-0 shadow-morphix-inset">
                <div class="text-3xl font-heading font-black text-white">{{ data.nota }}</div>
                <div>
                    <div class="flex text-amber-400 text-sm">
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                    </div>
                    <span class="text-xs text-slate-400 font-medium">Mais de {{ data.total_avaliacoes }} clientes atendidos</span>
                </div>
            </div>
        </div>

        <div class="grid md:grid-cols-3 gap-6">
            
            <!-- Avaliação 1 -->
            <div class="morphix-card p-6 rounded-2xl flex flex-col justify-between">
                <div>
                    <div class="flex items-center justify-between mb-4">
                        <div class="flex items-center gap-3">
                            <div class="w-11 h-11 rounded-full bg-blue-600/30 border border-blue-500/40 text-blue-400 font-bold flex items-center justify-center text-sm font-heading">
                                MS
                            </div>
                            <div>
                                <h4 class="font-bold text-sm text-white">Dr. Marcos Silveira</h4>
                                <p class="text-xs text-slate-400">Rua Itapura • Tatuapé</p>
                            </div>
                        </div>
                        <i class="fa-brands fa-google text-slate-500 text-lg"></i>
                    </div>

                    <div class="flex text-amber-400 text-xs mb-3">
                        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                    </div>

                    <p class="text-slate-300 text-sm leading-relaxed">
                        "Fiquei trancado para fora do condomínio às 01h20 da madrugada voltando de plantão. O chaveiro chegou de moto em 15 minutos na Rua Itapura. Abriu a fechadura multiponto alemã sem fazer um risco sequer. Preço justo e profissional educado."
                    </p>
                </div>

                <div class="mt-4 pt-4 border-t border-surface-border flex items-center justify-between text-[11px] text-slate-500">
                    <span>Atendimento de Emergência Madrugada</span>
                    <span class="text-techGreen font-semibold">✓ Verificado</span>
                </div>
            </div>

            <!-- Avaliação 2 -->
            <div class="morphix-card p-6 rounded-2xl flex flex-col justify-between">
                <div>
                    <div class="flex items-center justify-between mb-4">
                        <div class="flex items-center gap-3">
                            <div class="w-11 h-11 rounded-full bg-emerald-600/30 border border-emerald-500/40 text-emerald-400 font-bold flex items-center justify-center text-sm font-heading">
                                BC
                            </div>
                            <div>
                                <h4 class="font-bold text-sm text-white">Beatriz Cavalcanti</h4>
                                <p class="text-xs text-slate-400">Rua Emília Marengo • Anália Franco</p>
                            </div>
                        </div>
                        <i class="fa-brands fa-google text-slate-500 text-lg"></i>
                    </div>

                    <div class="flex text-amber-400 text-xs mb-3">
                        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                    </div>

                    <p class="text-slate-300 text-sm leading-relaxed">
                        "Comprei uma fechadura digital Intelbras IFR 7000 e precisava de instalação em porta de madeira pivotante maciça. Fizeram a furação com gabarito sem lascar a madeira, aspiraram a serragem e me ensinaram a cadastrar as biometrias. Serviço impecável."
                    </p>
                </div>

                <div class="mt-4 pt-4 border-t border-surface-border flex items-center justify-between text-[11px] text-slate-500">
                    <span>Instalação Fechadura Digital</span>
                    <span class="text-techGreen font-semibold">✓ Verificado</span>
                </div>
            </div>

            <!-- Avaliação 3 -->
            <div class="morphix-card p-6 rounded-2xl flex flex-col justify-between">
                <div>
                    <div class="flex items-center justify-between mb-4">
                        <div class="flex items-center gap-3">
                            <div class="w-11 h-11 rounded-full bg-amber-600/30 border border-amber-500/40 text-amber-400 font-bold flex items-center justify-center text-sm font-heading">
                                RQ
                            </div>
                            <div>
                                <h4 class="font-bold text-sm text-white">Renato Queiroz</h4>
                                <p class="text-xs text-slate-400">Próx. Praça Silvio Romero</p>
                            </div>
                        </div>
                        <i class="fa-brands fa-google text-slate-500 text-lg"></i>
                    </div>

                    <div class="flex text-amber-400 text-xs mb-3">
                        <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                    </div>

                    <p class="text-slate-300 text-sm leading-relaxed">
                        "Coloquei as compras no porta-malas do carro com a chave dentro e a porta travou sozinha. O técnico usou micha pantográfica pelo miolo e abriu em menos de 5 minutos, sem almofada de ar e sem forçar lataria. Salvou meu dia!"
                    </p>
                </div>

                <div class="mt-4 pt-4 border-t border-surface-border flex items-center justify-between text-[11px] text-slate-500">
                    <span>Socorro Automotivo Lishi</span>
                    <span class="text-techGreen font-semibold">✓ Verificado</span>
                </div>
            </div>

        </div>
    </section>

    <!-- 8. FAQ INTERATIVO SANFONADO (ACCORDION PURO SEM DEPENDÊNCIAS) -->
    <section class="py-16 px-4 sm:px-8 border-t border-surface-border bg-surface-base/50">
        <div class="max-w-4xl mx-auto">
            
            <div class="text-center mb-12">
                <span class="text-amberGlow font-bold text-xs uppercase tracking-widest">Dúvidas Frequentes</span>
                <h2 class="font-heading text-3xl font-extrabold text-white mt-1">
                    Perguntas Frequentes sobre o Atendimento
                </h2>
                <p class="text-slate-400 text-sm mt-2">Transparência total antes de solicitar o seu atendimento.</p>
            </div>

            <div class="space-y-3.5" id="faq-container">
                
                <!-- FAQ 1 -->
                <div class="morphix-card rounded-xl border border-surface-border overflow-hidden">
                    <button type="button" onclick="toggleFaq(this)" class="w-full p-5 text-left font-heading font-bold text-white flex justify-between items-center gap-4 hover:text-amberGlow transition">
                        <span>Vocês vão quebrar ou estragar a minha porta para abrir?</span>
                        <i class="fa-solid fa-chevron-down text-xs text-amberGlow transition-transform duration-300"></i>
                    </button>
                    <div class="px-5 pb-5 text-slate-300 text-sm hidden border-t border-surface-border/50 pt-3">
                        Não! Nós somos especialistas em aberturas técnicas com gazuas, decodificadores e michas de precisão. Em mais de 95% dos casos, a abertura é realizada pelo próprio segredo do cilindro sem causar nenhum dano à madeira, lataria do carro ou pintura.
                    </div>
                </div>

                <!-- FAQ 2 -->
                <div class="morphix-card rounded-xl border border-surface-border overflow-hidden">
                    <button type="button" onclick="toggleFaq(this)" class="w-full p-5 text-left font-heading font-bold text-white flex justify-between items-center gap-4 hover:text-amberGlow transition">
                        <span>Quanto custa o serviço e como é passado o valor?</span>
                        <i class="fa-solid fa-chevron-down text-xs text-amberGlow transition-transform duration-300"></i>
                    </button>
                    <div class="px-5 pb-5 text-slate-300 text-sm hidden border-t border-surface-border/50 pt-3">
                        Para total honestidade e transparência, você nos envia uma foto da fechadura pelo WhatsApp (ou o modelo e ano do seu carro). Informamos o valor total fechado antes de qualquer deslocamento. O valor informado é o valor que você pagará, sem taxas ocultas.
                    </div>
                </div>

                <!-- FAQ 3 -->
                <div class="morphix-card rounded-xl border border-surface-border overflow-hidden">
                    <button type="button" onclick="toggleFaq(this)" class="w-full p-5 text-left font-heading font-bold text-white flex justify-between items-center gap-4 hover:text-amberGlow transition">
                        <span>Quais são as formas de pagamento aceitas no local?</span>
                        <i class="fa-solid fa-chevron-down text-xs text-amberGlow transition-transform duration-300"></i>
                    </button>
                    <div class="px-5 pb-5 text-slate-300 text-sm hidden border-t border-surface-border/50 pt-3">
                        O técnico leva a maquininha móvel sem fio no local. Aceitamos Pix, Cartão de Débito e Cartão de Crédito (com opção de parcelamento para fechaduras digitais ou trocas completas). Também emitimos recibo e nota para reembolso de seguro residencial.
                    </div>
                </div>

                <!-- FAQ 4 -->
                <div class="morphix-card rounded-xl border border-surface-border overflow-hidden">
                    <button type="button" onclick="toggleFaq(this)" class="w-full p-5 text-left font-heading font-bold text-white flex justify-between items-center gap-4 hover:text-amberGlow transition">
                        <span>Qualquer pessoa pode pedir para abrir uma porta ou carro?</span>
                        <i class="fa-solid fa-chevron-down text-xs text-amberGlow transition-transform duration-300"></i>
                    </button>
                    <div class="px-5 pb-5 text-slate-300 text-sm hidden border-t border-surface-border/50 pt-3">
                        Não. Por protocolo rigoroso de segurança e para proteção dos moradores do bairro, exigimos a presença de um responsável com documento que comprove residência (ou porte do documento do veículo). Não realizamos aberturas sob suspeita de invasão.
                    </div>
                </div>

                <!-- FAQ 5 -->
                <div class="morphix-card rounded-xl border border-surface-border overflow-hidden">
                    <button type="button" onclick="toggleFaq(this)" class="w-full p-5 text-left font-heading font-bold text-white flex justify-between items-center gap-4 hover:text-amberGlow transition">
                        <span>Vocês atendem de madrugada, domingos e feriados?</span>
                        <i class="fa-solid fa-chevron-down text-xs text-amberGlow transition-transform duration-300"></i>
                    </button>
                    <div class="px-5 pb-5 text-slate-300 text-sm hidden border-t border-surface-border/50 pt-3">
                        Sim! Nosso plantão é 24 horas ininterrupto, 365 dias por ano. Temos técnicos de moto escalados para a madrugada prontos para socorrer emergências no Tatuapé e bairros vizinhos em minutos.
                    </div>
                </div>

            </div>

        </div>
    </section>

    <!-- 9. SEÇÃO DE LOCALIZAÇÃO FÍSICA COM GOOGLE MAPS EMBED -->
    <section id="base-fisica" class="py-20 px-4 sm:px-8 max-w-7xl mx-auto">
        <div class="grid lg:grid-cols-12 gap-10 items-center">
            
            <div class="lg:col-span-5 space-y-6">
                <div>
                    <span class="text-amberGlow font-bold text-xs uppercase tracking-widest">Base Física Estabelecida</span>
                    <h2 class="font-heading text-3xl font-extrabold text-white mt-1">
                        Ponto de apoio real no coração do Tatuapé
                    </h2>
                </div>

                <p class="text-slate-300 text-sm leading-relaxed">
                    Nossa oficina central fica a poucos metros da Estação Metrô Tatuapé, o que nos dá acesso estratégico e imediato à Radial Leste, Salim Farah Maluf, Av. Celso Garcia e às principais vias da Zona Leste.
                </p>

                <div class="space-y-4 pt-2 text-sm">
                    <div class="flex items-start gap-3.5">
                        <div class="w-9 h-9 rounded-lg bg-surface-card border border-surface-border flex items-center justify-center text-amberGlow shrink-0 mt-0.5">
                            <i class="fa-solid fa-map-pin"></i>
                        </div>
                        <div>
                            <strong class="text-white block font-heading">Endereço da Base:</strong>
                            <span class="text-slate-400">{{ data.endereco }} - {{ data.bairro }}</span>
                            <span class="text-xs text-slate-500 block mt-0.5">{{ data.referencia }}</span>
                        </div>
                    </div>

                    <div class="flex items-start gap-3.5">
                        <div class="w-9 h-9 rounded-lg bg-surface-card border border-surface-border flex items-center justify-center text-techGreen shrink-0 mt-0.5">
                            <i class="fa-solid fa-clock"></i>
                        </div>
                        <div>
                            <strong class="text-white block font-heading">Disponibilidade:</strong>
                            <span class="text-techGreen font-semibold">Plantão 24 Horas Direto (Inclusive Domingos e Feriados)</span>
                        </div>
                    </div>

                    <div class="flex items-start gap-3.5">
                        <div class="w-9 h-9 rounded-lg bg-surface-card border border-surface-border flex items-center justify-center text-amberGlow shrink-0 mt-0.5">
                            <i class="fa-solid fa-phone"></i>
                        </div>
                        <div>
                            <strong class="text-white block font-heading">Linha Direta de Emergência:</strong>
                            <a href="tel:+{{ data.telefone_link }}" class="text-white hover:text-amberGlow font-bold text-base transition">
                                {{ data.telefone_display }}
                            </a>
                        </div>
                    </div>
                </div>

                <div class="pt-2">
                    <a href="https://www.google.com/maps/place/Chaveiro+24+horas+Tatuap%C3%A9/@-23.5421701,-46.5758179,17z" 
                       target="_blank"
                       class="inline-flex items-center gap-2.5 px-5 py-3 rounded-xl bg-surface-card border border-surface-border text-white text-sm font-semibold hover:border-amberGlow/50 transition">
                        <i class="fa-solid fa-diamond-turn-right text-amberGlow"></i>
                        <span>Abrir Rota no Google Maps</span>
                    </a>
                </div>
            </div>

            <!-- Mapa Real Incorporado -->
            <div class="lg:col-span-7">
                <div class="rounded-2xl overflow-hidden border border-surface-border shadow-2xl h-[400px] bg-surface-card relative">
                    <iframe 
                        title="Mapa de Localização Chaveiro 24h Tatuapé"
                        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3657.766213651811!2d-46.5758179!3d-23.5421701!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94ce5f983c96ce09%3A0x3af69aa663ef0b5a!2sChaveiro%24%20horas%20Tatuap%C3%A9!5e0!3m2!1spt-BR!2sbr!4v1700000000000!5m2!1spt-BR!2sbr" 
                        width="100%" 
                        height="100%" 
                        style="border:0; filter: contrast(105%) brightness(95%);" 
                        allowfullscreen="" 
                        loading="lazy" 
                        referrerpolicy="no-referrer-when-downgrade">
                    </iframe>
                </div>
            </div>

        </div>
    </section>
    </main>

    <!-- 10. FOOTER CINEMÁTICO & SOBRE -->
    <footer class="border-t border-surface-border bg-void py-12 px-4 sm:px-8 pb-28 sm:pb-12 text-xs text-slate-400">
        <div class="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-6">
            
            <div class="text-center md:text-left space-y-1">
                <p class="font-heading font-extrabold text-sm text-white">{{ data.nome }}</p>
                <p>{{ data.endereco }} - {{ data.bairro }} • CEP {{ data.cep }}</p>
                <p class="text-slate-500 text-[11px]">CNPJ regularizado • Técnicos uniformizados e identificados</p>
            </div>

            <div class="flex items-center gap-6 text-sm font-medium">
                <a href="#simulador" class="hover:text-amberGlow transition">Simulador</a>
                <a href="#servicos" class="hover:text-amberGlow transition">Serviços</a>
                <a href="#seguranca" class="hover:text-amberGlow transition">Segurança</a>
                <a href="#base-fisica" class="hover:text-amberGlow transition">Onde Estamos</a>
            </div>

            <div class="text-center md:text-right">
                <p>© 2026 Todos os direitos reservados.</p>
                <p class="text-slate-500 text-[11px] mt-0.5">Atendimento móvel de urgência 24 Horas em toda a Zona Leste - SP.</p>
            </div>

        </div>
    </footer>

    <!-- 11. BARRA FIXA MOBILE DE EMERGÊNCIA (ULTRA-CONVERSÃO) -->
    <div class="fixed bottom-0 left-0 right-0 z-50 sm:hidden bg-void/95 border-t border-surface-border p-3 grid grid-cols-2 gap-2.5 backdrop-blur-xl shadow-2xl">
        <a href="tel:+{{ data.telefone_link }}" 
           class="bg-surface-card border border-surface-border text-white font-heading font-extrabold py-3.5 rounded-xl flex items-center justify-center gap-2 text-xs shadow-morphix-inset active:scale-95 transition">
            <i class="fa-solid fa-phone-volume text-amberGlow"></i> LIGAR AGORA
        </a>
        <a href="https://wa.me/{{ data.telefone_link }}?text=Ol%C3%A1!%20Fiquei%20trancado(a)%20para%20fora%20no%20Tatuap%C3%A9%20e%20preciso%20de%20socorro%20urgente." 
           target="_blank"
           class="bg-gradient-to-r from-techGreen to-techGreen-dark text-white font-heading font-extrabold py-3.5 rounded-xl flex items-center justify-center gap-2 text-xs shadow-glow-green active:scale-95 transition">
            <i class="fa-brands fa-whatsapp text-lg"></i> WHATSAPP 24H
        </a>
    </div>

    <!-- 12. BOTÃO FLUTUANTE WHATSAPP DESKTOP (MORPHIX GLOW) -->
    <a href="https://wa.me/{{ data.telefone_link }}?text=Ol%C3%A1!%20Preciso%20de%20um%20chaveiro%20com%20urg%C3%AAncia%20aqui%20no%20Tatuap%C3%A9." 
       target="_blank"
       title="Plantão WhatsApp 24h Chaveiro Tatuapé"
       class="hidden sm:flex fixed bottom-6 right-6 z-50 bg-gradient-to-r from-techGreen to-techGreen-dark text-white px-5 py-3.5 rounded-full items-center gap-3 shadow-glow-green hover:scale-105 active:scale-95 transition font-heading font-bold text-sm">
        <i class="fa-brands fa-whatsapp text-2xl"></i>
        <span>Plantão WhatsApp 24h</span>
    </a>

    <!-- JAVASCRIPT DINÂMICO PARA INTERAÇÕES FRONTEND -->
    <script>
        // Simulador de Socorro Imediato com Suporte a Outro Endereço
        function atualizarSimulador() {
            const selectProblema = document.getElementById('select-problema');
            const selectBairro = document.getElementById('select-bairro');
            const selectTipo = document.getElementById('select-tipo');
            const containerOutro = document.getElementById('container-outro-endereco');
            const inputOutro = document.getElementById('input-outro-endereco');
            
            const selectedBairroOpt = selectBairro.options[selectBairro.selectedIndex];
            const isOutroEndereco = (selectBairro.value === 'OUTRO_ENDERECO');

            let tempo = selectedBairroOpt.getAttribute('data-tempo') || '15 a 20 min';
            let dist = selectedBairroOpt.getAttribute('data-dist') || '1.0 km';
            let bairroDescricao = selectBairro.value;

            // Se for outro endereço, mostra campo de digitação e alerta
            if (isOutroEndereco) {
                containerOutro.classList.remove('hidden');
                const enderecoDigitado = inputOutro.value.trim();
                bairroDescricao = enderecoDigitado ? `Endereço: ${enderecoDigitado}` : 'Endereço a confirmar';
                tempo = 'A confirmar pela central (Viatura mais próxima)';
                dist = 'Sob consulta imediata';
            } else {
                containerOutro.classList.add('hidden');
            }

            // Atualiza tempo e distância na tela
            document.getElementById('display-tempo').textContent = tempo;
            document.getElementById('display-dist').textContent = dist.startsWith('~') ? dist : (dist === 'Sob consulta imediata' ? dist : '~' + dist + ' (R. Domingos Agostim)');

            // Formata mensagem personalizada para o WhatsApp
            const problema = selectProblema.value;
            const tipo = selectTipo.value;

            let mensagem = '';
            if (isOutroEndereco) {
                const endFinal = inputOutro.value.trim() || 'A informar no chat';
                mensagem = `Olá! Preciso de socorro de chaveiro em um endereço fora do miolo central:\n\n` +
                           `🚨 *Problema:* ${problema}\n` +
                           `📍 *Endereço / Bairro:* ${endFinal}\n` +
                           `🔑 *Tipo:* ${tipo}\n\n` +
                           `Poderiam me informar a viatura mais próxima, previsão de chegada e o valor fechado?`;
            } else {
                mensagem = `Olá! Preciso de socorro urgente de chaveiro no Tatuapé:\n\n` +
                           `🚨 *Problema:* ${problema}\n` +
                           `📍 *Localização:* ${bairroDescricao}\n` +
                           `🔑 *Tipo:* ${tipo}\n\n` +
                           `Por favor, me informe o valor fechado e a previsão de chegada da moto.`;
            }

            const linkWhatsApp = `https://wa.me/{{ data.telefone_link }}?text=${encodeURIComponent(mensagem)}`;
            document.getElementById('btn-whatsapp-simulador').href = linkWhatsApp;
        }

        // Accordion FAQ Interativo
        function toggleFaq(btn) {
            const content = btn.nextElementSibling;
            const icon = btn.querySelector('i');
            const isOpen = !content.classList.contains('hidden');

            // Fecha todos os outros FAQs para manter o visual limpo
            document.querySelectorAll('#faq-container > div > div').forEach(el => el.classList.add('hidden'));
            document.querySelectorAll('#faq-container button i').forEach(ic => ic.classList.remove('rotate-180'));

            if (!isOpen) {
                content.classList.remove('hidden');
                icon.classList.add('rotate-180');
            }
        }

        // Inicializa o simulador na carga
        document.addEventListener('DOMContentLoaded', () => {
            atualizarSimulador();
        });
    </script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE, data=BUSINESS_DATA)

@app.route("/papicarte")
def papicarte():
    with open("papicarte.html", "r", encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)