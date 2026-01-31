#!/usr/bin/env python3
"""
Brasa Roja - Remoción de Fondos con Gemini 2.5 Flash Image
Usa Google Gemini API (Nano Banana) para limpiar logos.

Uso:
    python remove_bg_gemini.py

Requiere:
    - GEMINI_API_KEY en archivo .env
    - pip install google-generativeai python-dotenv Pillow

Costo: ~$0.04 USD por imagen
"""

import os
import sys
import base64
from pathlib import Path
from io import BytesIO

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

try:
    import google.generativeai as genai
    from google.generativeai import types
except ImportError:
    print("ERROR: Instalar Google Generative AI SDK")
    print("  pip install google-generativeai")
    sys.exit(1)

try:
    from PIL import Image
except ImportError:
    print("ERROR: Instalar Pillow")
    print("  pip install Pillow")
    sys.exit(1)

# Configuración
API_KEY = os.getenv('GEMINI_API_KEY') or os.getenv('GOOGLE_API_KEY')
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
        'input': PROJECT_ROOT / 'BR_Main_1.png',
        'output': OUTPUT_DIR / 'Logo_Alt_Transparente.png',
        'description': 'Logo alternativo sin fondo'
    },
    {
        'input': PROJECT_ROOT / 'ICON.png',
        'output': ICON_OUTPUT_DIR / 'Icono_Transparente_Limpio.png',
        'description': 'Icono de llama sin fondo'
    },
    {
        'input': PROJECT_ROOT / 'ICON_2.png',
        'output': ICON_OUTPUT_DIR / 'Icono_Variante_Transparente.png',
        'description': 'Icono variante sin fondo'
    },
]


def remove_background_gemini(input_path: Path, output_path: Path) -> bool:
    """
    Remueve el fondo de una imagen usando Gemini 2.5 Flash Image.

    Args:
        input_path: Ruta al archivo de entrada
        output_path: Ruta donde guardar el resultado

    Returns:
        True si fue exitoso, False si falló
    """
    if not input_path.exists():
        print(f"  SALTANDO: {input_path.name} no existe")
        return False

    output_path.parent.mkdir(parents=True, exist_ok=True)
    print(f"  Procesando: {input_path.name}...")

    try:
        # Cargar imagen
        img = Image.open(input_path)

        # Configurar el modelo
        model = genai.GenerativeModel('gemini-2.0-flash-exp-image-generation')

        # Prompt para remover fondo
        prompt = """Remove the background from this logo image completely.
Keep only the logo elements (the flame, the text "BRASA ROJA", the golden swirl, and the sparks).
Make the background fully transparent.
Maintain the exact colors and quality of the original logo elements.
Output as PNG with transparency."""

        # Generar imagen editada
        response = model.generate_content(
            [prompt, img],
            generation_config=types.GenerationConfig(
                response_mime_type='image/png'
            )
        )

        # Guardar resultado
        if response.candidates and response.candidates[0].content.parts:
            for part in response.candidates[0].content.parts:
                if hasattr(part, 'inline_data') and part.inline_data:
                    image_data = base64.b64decode(part.inline_data.data)
                    result_img = Image.open(BytesIO(image_data))
                    result_img.save(output_path, 'PNG')
                    print(f"  ✅ Guardado: {output_path.name}")
                    return True

        print(f"  ⚠️  No se pudo procesar la imagen")
        return False

    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False


def create_color_variants(transparent_logo: Path, colors: dict) -> None:
    """
    Crea variantes del logo con diferentes fondos de color para stickers.
    """
    if not transparent_logo.exists():
        return

    variants_dir = transparent_logo.parent / 'Variantes_Stickers'
    variants_dir.mkdir(exist_ok=True)

    try:
        img = Image.open(transparent_logo).convert('RGBA')
    except Exception as e:
        print(f"  Error abriendo imagen: {e}")
        return

    for color_name, hex_color in colors.items():
        r = int(hex_color[1:3], 16)
        g = int(hex_color[3:5], 16)
        b = int(hex_color[5:7], 16)

        background = Image.new('RGBA', img.size, (r, g, b, 255))
        combined = Image.alpha_composite(background, img)

        output_name = f"Sticker_Fondo_{color_name}.png"
        combined.save(variants_dir / output_name, 'PNG')
        print(f"  ✅ Sticker: {output_name}")


def main():
    print("=" * 60)
    print("BRASA ROJA - Limpieza de Logos con Gemini 2.5 Flash Image")
    print("=" * 60)
    print()

    if not API_KEY:
        print("⚠️  GEMINI_API_KEY no encontrada")
        print()
        print("Agregá tu API key al archivo .env:")
        print("  GEMINI_API_KEY=tu_api_key_aqui")
        print()
        print("Obtener en: https://aistudio.google.com/apikey")
        print()
        sys.exit(1)

    # Configurar API
    genai.configure(api_key=API_KEY)

    print(f"✅ Gemini API configurada")
    print(f"📁 Salida logos: {OUTPUT_DIR}")
    print(f"📁 Salida iconos: {ICON_OUTPUT_DIR}")
    print(f"💰 Costo estimado: ~${len(LOGOS_TO_PROCESS) * 0.04:.2f} USD")
    print()

    # Crear directorios
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ICON_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Procesar cada logo
    success_count = 0
    for item in LOGOS_TO_PROCESS:
        print(f"\n📷 {item['description']}")
        if remove_background_gemini(item['input'], item['output']):
            success_count += 1

    print()
    print("=" * 60)
    print(f"Completado: {success_count}/{len(LOGOS_TO_PROCESS)} archivos procesados")
    print("=" * 60)

    # Crear variantes de color para stickers
    if success_count > 0:
        print()
        print("Creando variantes para stickers...")

        brand_colors = {
            'Blanco': '#FFFFFF',
            'Negro': '#000000',
            'Crema': '#F5EFE0',
            'Rojo_Brasa': '#C63333',
            'Dorado': '#C9882B',
            'Charcoal': '#2D2D2D',
            'Azul_Noche': '#1A237E',
            'Verde_Oliva': '#556B2F'
        }

        main_logo = OUTPUT_DIR / 'Logo_Transparente_Limpio.png'
        if main_logo.exists():
            create_color_variants(main_logo, brand_colors)

        main_icon = ICON_OUTPUT_DIR / 'Icono_Transparente_Limpio.png'
        if main_icon.exists():
            create_color_variants(main_icon, brand_colors)

    print()
    print("✅ ¡Listo! Los archivos limpios están en Brand_Assets/")
    print()
    print("Estructura creada:")
    print("  Brand_Assets/Logo_Limpio/")
    print("    ├── Logo_Transparente_Limpio.png")
    print("    ├── Logo_Alt_Transparente.png")
    print("    └── Variantes_Stickers/")
    print("        ├── Sticker_Fondo_Blanco.png")
    print("        ├── Sticker_Fondo_Negro.png")
    print("        └── ...")
    print("  Brand_Assets/Icono_Limpio/")
    print("    ├── Icono_Transparente_Limpio.png")
    print("    └── Variantes_Stickers/")


if __name__ == '__main__':
    main()
