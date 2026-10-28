from flask import Flask, render_template_string

app = Flask(__name__)

# Dados reais extraídos do perfil da empresa
BUSINESS_DATA = {
    "nome": "Chaveiro 24 Horas Tatuapé",
    "telefone_display": "(11) 97435-9641",
    "telefone_link": "5511974359641",
    "endereco": "Rua Domingos Agostim, 128 - Cidade Mãe do Céu, Tatuapé",
    "cep": "03306-010",
    "cidade": "São Paulo - SP",
    "nota": "4.8",
    "total_avaliacoes": "142",
    "tempo_medio": "15 a 25 min",
    "regioes": ["Tatuapé", "Jardim Anália Franco", "Vila Gomes Cardim", "Carrão", "Mooca", "Belém"]
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ data.nome }} | Socorro Rápido Residencial e Automotivo</title>
    <meta name="description" content="Trancado para fora? Perdeu a chave do carro? Chaveiro 24h no Tatuapé com chegada em até 25 minutos. Abertura sem danos, fechaduras digitais e chaves codificadas.">
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Google Fonts: Inter e Plus Jakarta Sans para leitura limpa e comercial -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@700;800&display=swap" rel="stylesheet">
    
    <!-- FontAwesome para ícones sóbrios e diretos -->
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
                        brand: {
                            dark: '#0F172A',      /* Azul ardósia escuro profundo */
                            navy: '#1E293B',      /* Azul marinho técnico */
                            yellow: '#F59E0B',    /* Amarelo atenção/emergência comercial */
                            yellowHover: '#D97706',
                            whatsapp: '#16A34A',  /* Verde sólido de conversão */
                            light: '#F8FAFC'
                        }
                    }
                }
            }
        }
    </script>
    <style>
        /* Textura sutil de fundo técnico */
        .bg-grid-pattern {
            background-image: radial-gradient(rgba(255, 255, 255, 0.07) 1px, transparent 1px);
            background-size: 24px 24px;
        }
        /* Sombra dura comercial para destacar cards sem parecer flutuação genérica */
        .commercial-card {
            border: 1px solid #E2E8F0;
            transition: all 0.2s ease-in-out;
        }
        .commercial-card:hover {
            border-color: #CBD5E1;
            transform: translateY(-2px);
            box-shadow: 0 12px 24px -10px rgba(15, 23, 42, 0.12);
        }
    </style>
</head>
<body class="bg-brand-light text-slate-800 antialiased selection:bg-brand-yellow selection:text-slate-900">

    <!-- TOP BAR DE PLANTÃO (Gatilho de Urgência Imediata) -->
    <div class="bg-brand-dark text-white text-xs sm:text-sm py-2.5 px-4 border-b border-slate-800">
        <div class="max-w-6xl mx-auto flex flex-wrap justify-between items-center gap-2">
            <div class="flex items-center gap-2">
                <span class="relative flex h-2.5 w-2.5">
                    <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"></span>
                    <span class="relative inline-flex rounded-full h-2.5 w-2.5 bg-green-500"></span>
                </span>
                <span class="font-medium text-slate-200">Unidade Móvel em Plantão Agora no Tatuapé</span>
                <span class="hidden md:inline text-slate-400">| Chegada estimada: <strong class="text-brand-yellow">{{ data.tempo_medio }}</strong></span>
            </div>
            <div class="flex items-center gap-4 ml-auto sm:ml-0">
                <span class="hidden sm:inline text-slate-300"><i class="fa-solid fa-location-dot text-brand-yellow mr-1"></i> Próx. ao Metrô Tatuapé</span>
            </div>
        </div>
    </div>

    <!-- HEADER / NAVBAR -->
    <header class="bg-white sticky top-0 z-40 border-b border-slate-200 shadow-sm">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 py-4 flex justify-between items-center">
            <!-- Logo Tipográfico Sóbrio -->
            <a href="#" class="flex items-center gap-3">
                <div class="bg-brand-dark text-brand-yellow w-11 h-11 rounded-lg flex items-center justify-center font-bold text-xl shadow-inner">
                    <i class="fa-solid fa-key"></i>
                </div>
                <div>
                    <span class="font-heading font-extrabold text-lg sm:text-xl text-slate-900 tracking-tight block leading-none">CHAVEIRO TATUAPÉ</span>
                    <span class="text-xs font-semibold uppercase tracking-widest text-amber-600 block mt-1">Plantão 24 Horas</span>
                </div>
            </a>

            <!-- Links Desktop -->
            <nav class="hidden md:flex items-center gap-7 text-sm font-semibold text-slate-600">
                <a href="#servicos" class="hover:text-slate-900 transition">Serviços</a>
                <a href="#fechaduras-digitais" class="hover:text-slate-900 transition">Fechaduras Digitais</a>
                <a href="#avaliacoes" class="hover:text-slate-900 transition">Avaliações ({{ data.nota }}★)</a>
                <a href="#localizacao" class="hover:text-slate-900 transition">Base Física</a>
            </nav>

            <!-- Botão de Ligação Direta no Header -->
            <div class="flex items-center gap-2.5">
                <a href="tel:+{{ data.telefone_link }}" 
                   class="bg-slate-900 hover:bg-slate-800 text-white font-semibold px-4 py-2.5 rounded-lg text-sm flex items-center gap-2 transition shadow-sm">
                    <i class="fa-solid fa-phone-volume text-brand-yellow animate-pulse"></i>
                    <span>{{ data.telefone_display }}</span>
                </a>
            </div>
        </div>
    </header>

    <!-- HERO SECTION (Foco em Conversão de Emergência + Foto Real do Nicho) -->
    <section class="relative bg-brand-dark text-white bg-grid-pattern overflow-hidden">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 py-12 md:py-20 relative z-10">
            <div class="grid md:grid-cols-12 gap-10 items-center">
                
                <!-- Coluna de Copy (7 colunas) -->
                <div class="md:col-span-7 space-y-6">
                    <!-- Selo de Confiança Google -->
                    <div class="inline-flex items-center gap-2.5 bg-slate-800/90 border border-slate-700 px-3.5 py-1.5 rounded-full text-xs sm:text-sm">
                        <div class="flex text-amber-400 text-xs">
                            <i class="fa-solid fa-star"></i>
                            <i class="fa-solid fa-star"></i>
                            <i class="fa-solid fa-star"></i>
                            <i class="fa-solid fa-star"></i>
                            <i class="fa-solid fa-star"></i>
                        </div>
                        <span class="font-semibold text-white">{{ data.nota }} de 5 no Google</span>
                        <span class="text-slate-400">• Referência na Zona Leste</span>
                    </div>

                    <h1 class="font-heading text-3xl sm:text-5xl font-extrabold tracking-tight leading-[1.15] text-white">
                        Ficou trancado para fora ou perdeu a chave? <span class="text-brand-yellow underline decoration-amber-500/30 underline-offset-8">Chegamos em 20 minutos.</span>
                    </h1>

                    <p class="text-slate-300 text-base sm:text-lg leading-relaxed max-w-xl">
                        Atendimento técnico imediato no <strong class="text-white">Tatuapé, Anália Franco e região</strong>. Abertura técnica sem danificar sua porta ou veículo, dia, noite, domingos e feriados.
                    </p>

                    <!-- Dupla de CTAs de Resposta Direta -->
                    <div class="pt-2 flex flex-col sm:flex-row gap-3.5">
                        <a href="https://wa.me/{{ data.telefone_link }}?text=Ol%C3%A1!%20Preciso%20de%20um%20chaveiro%20com%20urg%C3%AAncia%20aqui%20na%20regi%C3%A3o%20do%20Tatuap%C3%A9." 
                           target="_blank"
                           class="bg-brand-whatsapp hover:bg-green-700 text-white font-heading font-bold text-base sm:text-lg px-7 py-4 rounded-xl flex items-center justify-center gap-3 shadow-lg shadow-green-900/30 transition transform active:scale-95">
                            <i class="fa-brands fa-whatsapp text-2xl"></i>
                            <span>CHAMAR NO WHATSAPP AGORA</span>
                        </a>
                        
                        <a href="tel:+{{ data.telefone_link }}" 
                           class="bg-brand-yellow hover:bg-brand-yellowHover text-slate-950 font-heading font-bold text-base sm:text-lg px-7 py-4 rounded-xl flex items-center justify-center gap-3 shadow-lg transition">
                            <i class="fa-solid fa-phone text-xl"></i>
                            <span>LIGAR DE EMERGÊNCIA</span>
                        </a>
                    </div>

                    <!-- Micro-garantias técnicas -->
                    <div class="pt-4 grid grid-cols-3 gap-4 border-t border-slate-800 text-xs sm:text-sm text-slate-300">
                        <div class="flex items-center gap-2">
                            <i class="fa-solid fa-shield-halved text-brand-yellow"></i>
                            <span>Abertura sem avarias</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <i class="fa-solid fa-motorcycle text-brand-yellow"></i>
                            <span>Socorro móvel ágil</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <i class="fa-regular fa-credit-card text-brand-yellow"></i>
                            <span>Pix e Cartão no local</span>
                        </div>
                    </div>
                </div>

                <!-- Coluna de Imagem Fotográfica Real do Nicho (5 colunas) -->
                <div class="md:col-span-5 relative">
                    <div class="relative rounded-2xl overflow-hidden border-2 border-slate-700 shadow-2xl bg-slate-800">
                        <!-- Foto real de cilindro/chave e mão de técnico (sem aspecto gerado por IA) -->
                        <img src="https://images.unsplash.com/photo-1582139329536-e7284fece509?auto=format&fit=crop&w=900&q=85" 
                             alt="Técnico chaveiro realizando manutenção e abertura de fechadura" 
                             class="w-full h-[380px] sm:h-[440px] object-cover object-center brightness-95">
                        
                        <!-- Card Flutuante de Base Física -->
                        <div class="absolute bottom-4 left-4 right-4 bg-slate-900/95 backdrop-blur-md p-4 rounded-xl border border-slate-700">
                            <div class="flex items-start gap-3">
                                <div class="bg-brand-yellow/20 text-brand-yellow p-2.5 rounded-lg mt-0.5">
                                    <i class="fa-solid fa-store text-lg"></i>
                                </div>
                                <div>
                                    <p class="text-xs font-semibold uppercase tracking-wider text-brand-yellow">Base Fixa no Tatuapé</p>
                                    <p class="text-sm font-medium text-white mt-0.5">{{ data.endereco }}</p>
                                    <p class="text-xs text-slate-400 mt-0.5">Profissionais credenciados e identificados</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- FAIXA DE BAIRROS ATENDIDOS -->
    <div class="bg-slate-200/70 border-b border-slate-300 py-3.5 px-4">
        <div class="max-w-6xl mx-auto flex flex-wrap items-center justify-center sm:justify-between gap-2 text-xs sm:text-sm text-slate-700">
            <span class="font-bold text-slate-900 uppercase tracking-wider"><i class="fa-solid fa-route text-amber-600 mr-1.5"></i> Deslocamento Rápido:</span>
            <div class="flex flex-wrap justify-center gap-x-4 gap-y-1 font-medium">
                {% for regiao in data.regioes %}
                <span class="flex items-center gap-1.5">
                    <i class="fa-solid fa-check text-green-600 text-xs"></i> {{ regiao }}
                </span>
                {% endfor %}
            </div>
        </div>
    </div>

    <!-- SEÇÃO DE SERVIÇOS COM FOTOS ESPECÍFICAS DA PROFISSÃO -->
    <section id="servicos" class="py-16 sm:py-24 max-w-6xl mx-auto px-4 sm:px-6">
        <div class="max-w-2xl mb-12">
            <span class="text-amber-600 font-bold text-xs uppercase tracking-widest">Soluções Completas 24h</span>
            <h2 class="font-heading text-2xl sm:text-4xl font-extrabold text-slate-900 mt-1">
                Serviços de Chaveiro Residencial, Automotivo e Comercial
            </h2>
            <p class="text-slate-600 mt-3 text-base">
                Trabalhamos com ferramental de precisão (michas pantográficas e decodificadores) para resolver o seu problema na hora, sem quebrar portas ou danificar a pintura do seu veículo.
            </p>
        </div>

        <div class="grid md:grid-cols-3 gap-7">
            
            <!-- Card 1: Residencial -->
            <div class="bg-white rounded-xl overflow-hidden commercial-card flex flex-col justify-between">
                <div>
                    <div class="h-52 overflow-hidden relative bg-slate-900">
                        <img src="https://images.unsplash.com/photo-1558002038-1055907df827?auto=format&fit=crop&w=700&q=80" 
                             alt="Fechadura residencial e jogo de chaves" 
                             class="w-full h-full object-cover opacity-90 hover:scale-105 transition duration-500">
                        <span class="absolute top-3 left-3 bg-slate-900/90 text-white text-xs font-bold px-3 py-1 rounded">
                            Urgência Residencial
                        </span>
                    </div>
                    <div class="p-6">
                        <h3 class="font-heading font-bold text-xl text-slate-900">Abertura e Troca de Segredo</h3>
                        <p class="text-slate-600 text-sm mt-2 leading-relaxed">
                            Abertura de portas trancadas (simples, tetra, multiponto e blindadas). Troca de cilindro imediata em casos de perda ou roubo de chaves.
                        </p>
                        <ul class="mt-4 space-y-2 text-xs sm:text-sm text-slate-700 font-medium border-t border-slate-100 pt-4">
                            <li><i class="fa-solid fa-angle-right text-amber-600 mr-1.5"></i> Chaves Yale, Tetra e Multiponto</li>
                            <li><i class="fa-solid fa-angle-right text-amber-600 mr-1.5"></i> Extração de chave quebrada no miolo</li>
                            <li><i class="fa-solid fa-angle-right text-amber-600 mr-1.5"></i> Unificação de segredos (1 chave p/ tudo)</li>
                        </ul>
                    </div>
                </div>
                <div class="px-6 pb-6">
                    <a href="https://wa.me/{{ data.telefone_link }}?text=Ol%C3%A1,%20preciso%20de%20atendimento%20residencial%20no%20Tatuap%C3%A9." 
                       target="_blank"
                       class="w-full bg-slate-900 hover:bg-slate-800 text-white font-semibold py-3 px-4 rounded-lg text-sm flex items-center justify-center gap-2 transition">
                        <i class="fa-brands fa-whatsapp text-green-400 text-base"></i> Solicitar Orçamento Rápido
                    </a>
                </div>
            </div>

            <!-- Card 2: Automotivo -->
            <div class="bg-white rounded-xl overflow-hidden commercial-card flex flex-col justify-between">
                <div>
                    <div class="h-52 overflow-hidden relative bg-slate-900">
                        <img src="https://images.unsplash.com/photo-1617788138017-80ad40651399?auto=format&fit=crop&w=700&q=80" 
                             alt="Chave automotiva codificada e telecomando" 
                             class="w-full h-full object-cover opacity-90 hover:scale-105 transition duration-500">
                        <span class="absolute top-3 left-3 bg-amber-500 text-slate-950 text-xs font-bold px-3 py-1 rounded">
                            Socorro Automotivo
                        </span>
                    </div>
                    <div class="p-6">
                        <h3 class="font-heading font-bold text-xl text-slate-900">Abertura de Carros e Codificação</h3>
                        <p class="text-slate-600 text-sm mt-2 leading-relaxed">
                            Chave trancada dentro do carro ou no porta-malas? Abrimos veículos nacionais e importados com almofadas pneumáticas e michas específicas, sem arranhar.
                        </p>
                        <ul class="mt-4 space-y-2 text-xs sm:text-sm text-slate-700 font-medium border-t border-slate-100 pt-4">
                            <li><i class="fa-solid fa-angle-right text-amber-600 mr-1.5"></i> Abertura técnica pelo cilindro da porta</li>
                            <li><i class="fa-solid fa-angle-right text-amber-600 mr-1.5"></i> Cópia de chaves canivete e presença</li>
                            <li><i class="fa-solid fa-angle-right text-amber-600 mr-1.5"></i> Reparo de ignição e troca de carcaça</li>
                        </ul>
                    </div>
                </div>
                <div class="px-6 pb-6">
                    <a href="https://wa.me/{{ data.telefone_link }}?text=Ol%C3%A1,%20preciso%20de%20socorro%20automotivo%20no%20Tatuap%C3%A9." 
                       target="_blank"
                       class="w-full bg-slate-900 hover:bg-slate-800 text-white font-semibold py-3 px-4 rounded-lg text-sm flex items-center justify-center gap-2 transition">
                        <i class="fa-brands fa-whatsapp text-green-400 text-base"></i> Destrancar Meu Veículo
                    </a>
                </div>
            </div>

            <!-- Card 3: Fechaduras Digitais -->
            <div id="fechaduras-digitais" class="bg-white rounded-xl overflow-hidden commercial-card flex flex-col justify-between">
                <div>
                    <div class="h-52 overflow-hidden relative bg-slate-900">
                        <img src="https://images.unsplash.com/photo-1563013544-824ae1b704d3?auto=format&fit=crop&w=700&q=80" 
                             alt="Instalação de fechadura eletrônica e segurança comercial" 
                             class="w-full h-full object-cover opacity-90 hover:scale-105 transition duration-500">
                        <span class="absolute top-3 left-3 bg-slate-900/90 text-white text-xs font-bold px-3 py-1 rounded">
                            Instalação Especializada
                        </span>
                    </div>
                    <div class="p-6">
                        <h3 class="font-heading font-bold text-xl text-slate-900">Fechaduras Digitais e Biométricas</h3>
                        <p class="text-slate-600 text-sm mt-2 leading-relaxed">
                            Instalação limpa com gabarito de furação para portas de madeira, ferro ou vidro. Configuração completa de senhas e biometria no ato.
                        </p>
                        <ul class="mt-4 space-y-2 text-xs sm:text-sm text-slate-700 font-medium border-t border-slate-100 pt-4">
                            <li><i class="fa-solid fa-angle-right text-amber-600 mr-1.5"></i> Intelbras, Samsung, Elsys, Papaiz e Pado</li>
                            <li><i class="fa-solid fa-angle-right text-amber-600 mr-1.5"></i> Modelos de embutir e sobrepor</li>
                            <li><i class="fa-solid fa-angle-right text-amber-600 mr-1.5"></i> Manutenção em travas de condomínios</li>
                        </ul>
                    </div>
                </div>
                <div class="px-6 pb-6">
                    <a href="https://wa.me/{{ data.telefone_link }}?text=Ol%C3%A1,%20gostaria%20de%20or%C3%A7ar%20a%20instala%C3%A7%C3%A3o%20de%20uma%20fechadura%20digital." 
                       target="_blank"
                       class="w-full bg-slate-900 hover:bg-slate-800 text-white font-semibold py-3 px-4 rounded-lg text-sm flex items-center justify-center gap-2 transition">
                        <i class="fa-brands fa-whatsapp text-green-400 text-base"></i> Agendar Instalação
                    </a>
                </div>
            </div>

        </div>
    </section>

    <!-- BANNER DE COMO FUNCIONA O ATENDIMENTO DE EMERGÊNCIA -->
    <section class="bg-slate-900 text-white py-14 px-4 sm:px-6 border-y border-slate-800">
        <div class="max-w-6xl mx-auto">
            <div class="grid md:grid-cols-4 gap-8 items-center">
                <div class="md:col-span-1">
                    <span class="text-brand-yellow text-xs font-bold uppercase tracking-widest">Transparência Total</span>
                    <h3 class="font-heading text-2xl font-extrabold mt-1">Sem surpresas no valor final.</h3>
                    <p class="text-slate-400 text-sm mt-2">Nosso orçamento é passado antes do deslocamento mediante foto da fechadura no WhatsApp.</p>
                </div>
                <div class="md:col-span-3 grid sm:grid-cols-3 gap-6">
                    <div class="bg-slate-800/70 border border-slate-700 p-5 rounded-xl">
                        <span class="text-brand-yellow font-heading font-extrabold text-2xl">01.</span>
                        <h4 class="font-bold text-base mt-2">Envie uma Foto</h4>
                        <p class="text-slate-300 text-xs sm:text-sm mt-1">Mande foto da fechadura ou informe o modelo do carro pelo WhatsApp.</p>
                    </div>
                    <div class="bg-slate-800/70 border border-slate-700 p-5 rounded-xl">
                        <span class="text-brand-yellow font-heading font-extrabold text-2xl">02.</span>
                        <h4 class="font-bold text-base mt-2">Preço Fechado</h4>
                        <p class="text-slate-300 text-xs sm:text-sm mt-1">Informamos o valor exato do serviço e o tempo real de chegada até você.</p>
                    </div>
                    <div class="bg-slate-800/70 border border-slate-700 p-5 rounded-xl">
                        <span class="text-brand-yellow font-heading font-extrabold text-2xl">03.</span>
                        <h4 class="font-bold text-base mt-2">Resolução no Local</h4>
                        <p class="text-slate-300 text-xs sm:text-sm mt-1">Nosso técnico realiza o serviço rapidamente e você paga via Pix ou Cartão.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- PROVA SOCIAL (ESTILO GOOGLE MEU NEGÓCIO REAL) -->
    <section id="avaliacoes" class="py-16 sm:py-20 max-w-6xl mx-auto px-4 sm:px-6">
        <div class="flex flex-col md:flex-row md:items-end justify-between mb-10 gap-4">
            <div>
                <div class="flex items-center gap-2">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/c/c1/Google_%22G%22_logo.svg" alt="Google" class="w-5 h-5">
                    <span class="text-xs font-bold uppercase tracking-wider text-slate-500">Avaliações Verificadas no Google Maps</span>
                </div>
                <h2 class="font-heading text-2xl sm:text-3xl font-extrabold text-slate-900 mt-1">
                    O que dizem os moradores do Tatuapé
                </h2>
            </div>
            <div class="bg-white border border-slate-200 px-4 py-3 rounded-xl flex items-center gap-4 shadow-sm">
                <div class="text-3xl font-heading font-extrabold text-slate-900">{{ data.nota }}</div>
                <div>
                    <div class="flex text-amber-400 text-sm">
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                        <i class="fa-solid fa-star"></i>
                    </div>
                    <p class="text-xs text-slate-500 mt-0.5">Média de excelência na região</p>
                </div>
            </div>
        </div>

        <div class="grid md:grid-cols-3 gap-6">
            <!-- Review 1 -->
            <div class="bg-white p-6 rounded-xl commercial-card">
                <div class="flex items-center justify-between mb-3">
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 rounded-full bg-blue-600 text-white font-bold flex items-center justify-center text-sm">RM</div>
                        <div>
                            <h4 class="font-bold text-sm text-slate-900">Rodrigo Mendes</h4>
                            <p class="text-xs text-slate-400">Morador do Tatuapé</p>
                        </div>
                    </div>
                    <i class="fa-brands fa-google text-slate-300"></i>
                </div>
                <div class="flex text-amber-400 text-xs mb-2">
                    <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                </div>
                <p class="text-slate-600 text-sm leading-relaxed">
                    "Fiquei trancado para fora do apartamento às 23h30 num domingo. Liguei e o rapaz chegou de moto em menos de 20 minutos. Abriu a fechadura multiponto sem estragar nada. Recomendo demais!"
                </p>
            </div>

            <!-- Review 2 -->
            <div class="bg-white p-6 rounded-xl commercial-card">
                <div class="flex items-center justify-between mb-3">
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 rounded-full bg-emerald-600 text-white font-bold flex items-center justify-center text-sm">CA</div>
                        <div>
                            <h4 class="font-bold text-sm text-slate-900">Camila Andrade</h4>
                            <p class="text-xs text-slate-400">Jardim Anália Franco</p>
                        </div>
                    </div>
                    <i class="fa-brands fa-google text-slate-300"></i>
                </div>
                <div class="flex text-amber-400 text-xs mb-2">
                    <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                </div>
                <p class="text-slate-600 text-sm leading-relaxed">
                    "Fizeram a instalação da minha fechadura digital Intelbras na porta de madeira. Muito caprichosos, limparam tudo depois de furar a porta e me ensinaram a cadastrar as senhas."
                </p>
            </div>

            <!-- Review 3 -->
            <div class="bg-white p-6 rounded-xl commercial-card">
                <div class="flex items-center justify-between mb-3">
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 rounded-full bg-amber-600 text-white font-bold flex items-center justify-center text-sm">LF</div>
                        <div>
                            <h4 class="font-bold text-sm text-slate-900">Lucas Ferreira</h4>
                            <p class="text-xs text-slate-400">Próx. Shopping Metrô Tatuapé</p>
                        </div>
                    </div>
                    <i class="fa-brands fa-google text-slate-300"></i>
                </div>
                <div class="flex text-amber-400 text-xs mb-2">
                    <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                </div>
                <p class="text-slate-600 text-sm leading-relaxed">
                    "Tranquei a chave dentro do porta-malas do carro. Atendimento super rápido aqui na Rua Domingos Agostim, preço justo combinado antes pelo WhatsApp e serviço nota 10."
                </p>
            </div>
        </div>
    </section>

    <!-- SEÇÃO DE LOCALIZAÇÃO E CONTATO DIRETO -->
    <section id="localizacao" class="py-14 bg-white border-t border-slate-200">
        <div class="max-w-6xl mx-auto px-4 sm:px-6">
            <div class="grid md:grid-cols-12 gap-8 items-center">
                
                <div class="md:col-span-5 space-y-5">
                    <span class="text-amber-600 font-bold text-xs uppercase tracking-widest">Onde Estamos</span>
                    <h2 class="font-heading text-2xl sm:text-3xl font-extrabold text-slate-900">
                        Base física no coração do Tatuapé
                    </h2>
                    <p class="text-slate-600 text-sm leading-relaxed">
                        Contamos com ponto de apoio fixo na Cidade Mãe do Céu (ao lado do Metrô Tatuapé) e técnicos volantes estrategicamente posicionados para atender emergências em minutos.
                    </p>

                    <div class="space-y-3 pt-2 text-sm">
                        <div class="flex items-start gap-3">
                            <i class="fa-solid fa-location-dot text-amber-600 text-lg mt-0.5"></i>
                            <div>
                                <strong class="text-slate-900 block">Endereço:</strong>
                                <span class="text-slate-600">{{ data.endereco }} - {{ data.cidade }}</span>
                            </div>
                        </div>
                        <div class="flex items-start gap-3">
                            <i class="fa-solid fa-clock text-amber-600 text-lg mt-0.5"></i>
                            <div>
                                <strong class="text-slate-900 block">Horário de Funcionamento:</strong>
                                <span class="text-green-700 font-semibold">Aberto 24 Horas (Incluindo Domingos e Feriados)</span>
                            </div>
                        </div>
                        <div class="flex items-start gap-3">
                            <i class="fa-solid fa-phone text-amber-600 text-lg mt-0.5"></i>
                            <div>
                                <strong class="text-slate-900 block">Central de Atendimento Direto:</strong>
                                <span class="text-slate-800 font-bold text-base">{{ data.telefone_display }}</span>
                            </div>
                        </div>
                    </div>

                    <div class="pt-3">
                        <a href="https://www.google.com/maps/place/Chaveiro+24+horas+Tatuap%C3%A9/@-23.5421701,-46.5758179,17z" 
                           target="_blank"
                           class="inline-flex items-center gap-2 text-sm font-bold text-slate-900 hover:text-amber-600 underline underline-offset-4">
                            <i class="fa-solid fa-map-location-dot"></i> Abrir rota no Google Maps
                        </a>
                    </div>
                </div>

                <!-- Mapa Real Incorporado (Rua Domingos Agostim, 128 - Tatuapé) -->
                <div class="md:col-span-7">
                    <div class="rounded-xl overflow-hidden border border-slate-300 shadow-md h-[340px] bg-slate-100">
                        <iframe 
                            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3657.766213651811!2d-46.5758179!3d-23.5421701!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94ce5f983c96ce09%3A0x3af69aa663ef0b5a!2sChaveiro%24%20horas%20Tatuap%C3%A9!5e0!3m2!1spt-BR!2sbr!4v1700000000000!5m2!1spt-BR!2sbr" 
                            width="100%" 
                            height="100%" 
                            style="border:0;" 
                            allowfullscreen="" 
                            loading="lazy" 
                            referrerpolicy="no-referrer-when-downgrade">
                        </iframe>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- FOOTER SÓBRIO -->
    <footer class="bg-brand-dark text-slate-400 py-10 px-4 border-t border-slate-800 pb-24 sm:pb-10">
        <div class="max-w-6xl mx-auto flex flex-col sm:flex-row justify-between items-center gap-4 text-xs sm:text-sm">
            <div>
                <p class="font-bold text-white">{{ data.nome }}</p>
                <p class="mt-0.5">{{ data.endereco }} • CEP {{ data.cep }}</p>
            </div>
            <div class="text-center sm:text-right">
                <p>© 2026 Todos os direitos reservados.</p>
                <p class="text-slate-500 text-xs mt-0.5">Atendimento técnico rápido em toda a Zona Leste - SP.</p>
            </div>
        </div>
    </footer>

    <!-- BARRA FIXA MOBILE (Essencial para LP de Chaveiro 24h) -->
    <div class="fixed bottom-0 left-0 right-0 z-50 sm:hidden bg-white border-t border-slate-300 p-2.5 grid grid-cols-2 gap-2 shadow-[0_-4px_12px_rgba(0,0,0,0.12)]">
        <a href="tel:+{{ data.telefone_link }}" 
           class="bg-brand-yellow text-slate-950 font-heading font-extrabold py-3 rounded-lg flex items-center justify-center gap-2 text-sm shadow">
            <i class="fa-solid fa-phone-volume"></i> LIGAR AGORA
        </a>
        <a href="https://wa.me/{{ data.telefone_link }}?text=Ol%C3%A1!%20Preciso%20de%20um%20chaveiro%2024h%20no%20Tatuap%C3%A9." 
           target="_blank"
           class="bg-brand-whatsapp text-white font-heading font-extrabold py-3 rounded-lg flex items-center justify-center gap-2 text-sm shadow">
            <i class="fa-brands fa-whatsapp text-lg"></i> WHATSAPP
        </a>
    </div>

    <!-- BOTÃO WHATSAPP FLUTUANTE DESKTOP -->
    <a href="https://wa.me/{{ data.telefone_link }}?text=Ol%C3%A1!%20Preciso%20de%20um%20chaveiro%20no%20Tatuap%C3%A9." 
       target="_blank"
       title="Chamar Chaveiro no WhatsApp"
       class="hidden sm:flex fixed bottom-6 right-6 z-50 bg-brand-whatsapp hover:bg-green-700 text-white px-5 py-3.5 rounded-full items-center gap-2.5 shadow-xl transition transform hover:scale-105 font-bold text-sm">
        <i class="fa-brands fa-whatsapp text-2xl"></i>
        <span>Plantão WhatsApp 24h</span>
    </a>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE, data=BUSINESS_DATA)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)