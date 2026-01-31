#!/usr/bin/env python3
"""
Brasa Roja - Remoción de Fondos con OpenAI
Usa DALL-E/GPT-4 Vision para limpiar logos.

Uso:
    python remove_bg_openai.py

Requiere:
    - OPENAI_API_KEY en archivo .env
    - pip install openai python-dotenv Pillow
"""

import os
import sys
import base64
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

try:
    from openai import OpenAI
except ImportError:
    print("Instalar: pip install openai")
    sys.exit(1)

try:
    from PIL import Image
    import io
except ImportError:
    print("Instalar: pip install Pillow")
    sys.exit(1)

# Configuración
API_KEY = os.getenv('OPENAI_API_KEY')
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent
OUTPUT_DIR = PROJECT_ROOT / 'Brand_Assets' / 'Logo_Limpio'
ICON_OUTPUT_DIR = PROJECT_ROOT / 'Brand_Assets' / 'Icono_Limpio'

# Archivos a procesar
LOGOS_TO_PROCESS = [
    {
        'input': PROJECT_ROOT / 'Logo_MAIN_1.png',
        'output': OUTPUT_DIR / 'Logo_Transparente_Limpio.png',
        'description': 'Logo principal sin fondo'
    },
    {
        'input': PROJECT_ROOT / 'ICON.png',
        'output': ICON_OUTPUT_DIR / 'Icono_Transparente_Limpio.png',
        'description': 'Icono de llama sin fondo'
    },
]


def encode_image(image_path: Path) -> str:
    """Codifica imagen a base64."""
    with open(image_path, "rb") as f:
        return base64.standard_b64encode(f.read()).decode("utf-8")


def remove_background_openai(input_path: Path, output_path: Path, client: OpenAI) -> bool:
    """
    Usa OpenAI para analizar y procesar la imagen.
    Nota: OpenAI no tiene remoción directa de fondos, pero puede guiar el proceso.
    """
    if not input_path.exists():
        print(f"  SALTANDO: {input_path.name} no existe")
        return False

    output_path.parent.mkdir(parents=True, exist_ok=True)
    print(f"  Analizando: {input_path.name}...")

    try:
        # Usar GPT-4 Vision para analizar la imagen
        base64_image = encode_image(input_path)

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": """Analiza este logo y dame:
1. Los colores exactos del fondo (en hex)
2. Los colores del logo/elementos principales (en hex)
3. ¿El fondo es sólido o tiene gradiente?
4. ¿Hay transparencia actual?

Responde en formato JSON."""
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=500
        )

        analysis = response.choices[0].message.content
        print(f"  📊 Análisis:\n{analysis}")

        # Por ahora, copiar el archivo original y marcar para procesamiento manual
        # OpenAI no tiene API de edición de imágenes para remover fondos directamente
        import shutil
        shutil.copy(input_path, output_path)
        print(f"  ⚠️  Copiado para procesamiento manual con Canva Pro")

        return True

    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False


def main():
    print("=" * 50)
    print("BRASA ROJA - Análisis de Logos con OpenAI")
    print("=" * 50)
    print()

    if not API_KEY:
        print("⚠️  OPENAI_API_KEY no encontrada")
        print()
        print("Agregá tu API key al archivo .env:")
        print("  OPENAI_API_KEY=sk-...")
        print()
        sys.exit(1)

    client = OpenAI(api_key=API_KEY)
    print(f"✅ OpenAI API configurada")
    print()

    # Crear directorios
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ICON_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Procesar cada logo
    for item in LOGOS_TO_PROCESS:
        print(f"\n📷 {item['description']}")
        remove_background_openai(item['input'], item['output'], client)

    print()
    print("=" * 50)
    print("RECOMENDACIÓN:")
    print("Para remoción de fondos, usá una de estas opciones:")
    print("1. Canva Pro (tenés acceso) - Background Remover integrado")
    print("2. Remove.bg API (50 gratis/mes) - Automático")
    print("3. Photopea.com (gratis) - Manual pero preciso")
    print("=" * 50)


if __name__ == '__main__':
    main()
