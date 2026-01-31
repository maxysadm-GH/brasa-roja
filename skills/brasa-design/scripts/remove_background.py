#!/usr/bin/env python3
"""
Brasa Roja - Script de Remoción de Fondos
Usa Remove.bg API para limpiar logos y crear variantes transparentes.

Uso:
    python remove_background.py

Requiere:
    - REMOVEBG_API_KEY en archivo .env o variable de entorno
    - pip install requests python-dotenv Pillow
"""

import os
import sys
import requests
from pathlib import Path

# Intentar cargar dotenv si está disponible
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Configuración
API_KEY = os.getenv('REMOVEBG_API_KEY')
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
        'input': PROJECT_ROOT / 'BR_LOGO_1.png',
        'output': OUTPUT_DIR / 'Logo_Premium_Transparente.png',
        'description': 'Logo premium sin fondo'
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
    {
        'input': PROJECT_ROOT / 'brasa_primary_dark.png',
        'output': OUTPUT_DIR / 'Logo_Dark_Transparente.png',
        'description': 'Logo oscuro sin fondo'
    }
]


def remove_background(input_path: Path, output_path: Path) -> bool:
    """
    Remueve el fondo de una imagen usando Remove.bg API.

    Args:
        input_path: Ruta al archivo de entrada
        output_path: Ruta donde guardar el resultado

    Returns:
        True si fue exitoso, False si falló
    """
    if not API_KEY:
        print("ERROR: REMOVEBG_API_KEY no configurada")
        print("Agregá tu API key al archivo .env:")
        print("  REMOVEBG_API_KEY=tu_api_key_aqui")
        return False

    if not input_path.exists():
        print(f"  SALTANDO: {input_path.name} no existe")
        return False

    # Crear directorio de salida si no existe
    output_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"  Procesando: {input_path.name}...")

    try:
        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': open(input_path, 'rb')},
            data={'size': 'auto'},
            headers={'X-Api-Key': API_KEY},
            timeout=60
        )

        if response.status_code == 200:
            with open(output_path, 'wb') as out:
                out.write(response.content)
            print(f"  ✅ Guardado: {output_path.name}")
            return True
        else:
            error = response.json().get('errors', [{}])[0]
            print(f"  ❌ Error: {error.get('title', 'Unknown error')}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"  ❌ Error de conexión: {e}")
        return False


def create_color_variants(transparent_logo: Path, colors: dict) -> None:
    """
    Crea variantes del logo con diferentes fondos de color.
    Requiere Pillow instalado.
    """
    try:
        from PIL import Image
    except ImportError:
        print("  NOTA: Instalar Pillow para crear variantes de color")
        print("        pip install Pillow")
        return

    if not transparent_logo.exists():
        return

    variants_dir = transparent_logo.parent / 'Variantes_Color'
    variants_dir.mkdir(exist_ok=True)

    # Abrir imagen con transparencia
    img = Image.open(transparent_logo).convert('RGBA')

    for color_name, hex_color in colors.items():
        # Crear fondo del color especificado
        r = int(hex_color[1:3], 16)
        g = int(hex_color[3:5], 16)
        b = int(hex_color[5:7], 16)

        background = Image.new('RGBA', img.size, (r, g, b, 255))
        # Componer logo sobre fondo
        combined = Image.alpha_composite(background, img)

        output_name = f"Logo_Fondo_{color_name}.png"
        combined.save(variants_dir / output_name)
        print(f"  ✅ Variante: {output_name}")


def main():
    print("=" * 50)
    print("BRASA ROJA - Limpieza de Logos")
    print("=" * 50)
    print()

    if not API_KEY:
        print("⚠️  REMOVEBG_API_KEY no encontrada")
        print()
        print("Para usar este script:")
        print("1. Obtené tu API key gratis en: https://www.remove.bg/api")
        print("2. Creá un archivo .env en la raíz del proyecto:")
        print("   REMOVEBG_API_KEY=tu_api_key_aqui")
        print("3. Ejecutá este script de nuevo")
        print()
        sys.exit(1)

    print(f"✅ API Key configurada")
    print(f"📁 Salida logos: {OUTPUT_DIR}")
    print(f"📁 Salida iconos: {ICON_OUTPUT_DIR}")
    print()

    # Crear directorios
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ICON_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Procesar cada logo
    success_count = 0
    for item in LOGOS_TO_PROCESS:
        print(f"\n📷 {item['description']}")
        if remove_background(item['input'], item['output']):
            success_count += 1

    print()
    print("=" * 50)
    print(f"Completado: {success_count}/{len(LOGOS_TO_PROCESS)} archivos procesados")
    print("=" * 50)

    # Crear variantes de color si hay logos procesados
    if success_count > 0:
        print()
        print("Creando variantes de color para stickers...")

        brand_colors = {
            'Blanco': '#FFFFFF',
            'Negro': '#000000',
            'Crema': '#F5EFE0',
            'Rojo': '#C63333',
            'Dorado': '#C9882B',
            'Charcoal': '#2D2D2D'
        }

        main_logo = OUTPUT_DIR / 'Logo_Transparente_Limpio.png'
        if main_logo.exists():
            create_color_variants(main_logo, brand_colors)

    print()
    print("¡Listo! Los archivos limpios están en Brand_Assets/")


if __name__ == '__main__':
    main()
