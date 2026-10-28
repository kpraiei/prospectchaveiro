import urllib.request
import json
import sys

# Garante suporte a UTF-8 no terminal Windows
if sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

WEBHOOK_URL = "http://localhost:5000/api/webhook/prospect"

lead_exemplo = {
    "business_name": "Eletricista Rápido Mooca",
    "category": "eletricista",
    "phone": "(11) 97711-2233",
    "address": "Rua da Mooca, 1420",
    "neighborhood": "Mooca",
    "city": "São Paulo",
    "state": "SP",
    "rating": 4.9,
    "reviews_count": 98
}

print(f"[OK] Disparando Webhook para {WEBHOOK_URL}...")
req = urllib.request.Request(
    WEBHOOK_URL,
    data=json.dumps(lead_exemplo).encode("utf-8"),
    headers={"Content-Type": "application/json"}
)

try:
    with urllib.request.urlopen(req) as response:
        status_code = response.getcode()
        body = json.loads(response.read().decode("utf-8"))
        print(f"Status HTTP: {status_code}")
        print("[OK] Sucesso! Landing Page gerada pelo motor:")
        print(f"-> Slug: {body['slug']}")
        print(f"-> Demo URL Local: {body['demo_url']}")
        print(f"-> Demo GitHub Pages: {body['github_pages_url']}")
        print(f"-> WhatsApp Proprietário: {body['owner_phone']}")
        print("\n--- Script de Abordagem Personalizado para WhatsApp ---")
        print(body["whatsapp_pitch"])
        print("-" * 55)
except Exception as e:
    print(f"[ERRO]: {e}")
