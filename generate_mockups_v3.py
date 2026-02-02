# -*- coding: utf-8 -*-
"""
Brasa Roja Mockup Generator v3
Fixes: Ensure "Tradicion Familiar" tagline is on EVERY mockup
"""

from google import genai
from google.genai import types
from pathlib import Path
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

import os
from dotenv import load_dotenv
load_dotenv()
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set")
OUTPUT_DIR = Path(r"C:\Users\maxys\OneDrive\Imágenes\BrasaRoja\Mockups_v3")
OUTPUT_DIR.mkdir(exist_ok=True)

LOGO_FULL = Path(r"C:\Users\maxys\OneDrive\Imágenes\BrasaRoja\Assets\Logo_Full\Logo_Transparent.png")
LOGO_ICON = Path(r"C:\Users\maxys\OneDrive\Imágenes\BrasaRoja\Clean Files\BR Icon NBG.png")

client = genai.Client(api_key=GEMINI_API_KEY)

def load_image(path: Path) -> types.Part:
    with open(path, 'rb') as f:
        data = f.read()
    return types.Part.from_bytes(data=data, mime_type='image/png')

# FIXED: All mockups MUST include "Tradicion Familiar" tagline per brand guidelines
MOCKUPS = {
    "05_chef_formal_shirt": {
        "use_logo": "full",
        "prompt": """Create a professional product photography mockup featuring this EXACT logo on a formal chef coat.

CRITICAL REQUIREMENTS:
1. Use this EXACT logo image - do not modify or reinterpret it
2. The logo MUST include ALL elements: flame icon, orange swirl, rising embers
3. Text MUST read "BRASAROJA" with "BRASA" in gold and "ROJA" in red
4. MANDATORY: Include "Tradicion Familiar" tagline in gold script below the brand name - THIS IS REQUIRED BY BRAND GUIDELINES

Mockup details:
- Black formal chef coat/jacket with mandarin collar
- Double-breasted style with black buttons
- Complete logo embroidered on LEFT CHEST including:
  * Flame icon with swirl and embers
  * "BRASAROJA" text (gold BRASA, red ROJA)
  * "Tradicion Familiar" in gold script underneath - DO NOT OMIT THIS
- Chef coat displayed on professional mannequin
- Clean dark studio background
- Professional lighting
- 4K commercial uniform photography"""
    },

    "06_cup_sleeve": {
        "use_logo": "full",
        "prompt": """Create a professional product photography mockup featuring this EXACT logo on a coffee cup sleeve.

CRITICAL REQUIREMENTS:
1. Use this EXACT logo image - do not modify or reinterpret it
2. The logo MUST include ALL elements: flame icon, orange swirl, rising embers
3. Text MUST read "BRASAROJA" with "BRASA" in gold and "ROJA" in red
4. MANDATORY: Include "Tradicion Familiar" tagline in gold script below - THIS IS REQUIRED BY BRAND GUIDELINES

Mockup details:
- BLACK branded cup sleeve wrapped around white paper coffee cup
- Complete logo printed centered on sleeve:
  * Flame icon with swirl and rising embers
  * "BRASAROJA" text below
  * "Tradicion Familiar" in gold script underneath - DO NOT OMIT THIS
- Gold accent lines at top and bottom edges of sleeve
- Subtle repeating flame pattern in background
- Cup on white marble countertop
- Coffee beans scattered as props
- Steam rising from cup
- Warm morning cafe lighting
- 4K commercial product photography"""
    },
}

def generate_with_nano_banana(prompt: str, logo_path: Path, filename: str) -> str:
    """Generate using Nano Banana Pro with logo reference"""
    try:
        logo_part = load_image(logo_path)

        response = client.models.generate_content(
            model='nano-banana-pro-preview',
            contents=[logo_part, prompt],
            config=types.GenerateContentConfig(
                response_modalities=['IMAGE', 'TEXT'],
            )
        )

        for part in response.candidates[0].content.parts:
            if part.inline_data and part.inline_data.mime_type.startswith('image'):
                output_path = OUTPUT_DIR / f"{filename}.png"
                with open(output_path, 'wb') as f:
                    f.write(part.inline_data.data)
                print(f"[OK] {filename}.png")
                return str(output_path)

        print(f"[NO IMAGE] {filename}")
        return None
    except Exception as e:
        print(f"[ERROR] {filename}: {e}")
        return None

def main():
    print("=" * 60)
    print("BRASA ROJA MOCKUP GENERATOR v3")
    print("FIX: Adding 'Tradicion Familiar' to all mockups")
    print("=" * 60)
    print()

    results = []
    for name, config in MOCKUPS.items():
        print(f"Regenerating: {name}")
        logo_path = LOGO_ICON if config["use_logo"] == "icon" else LOGO_FULL
        result = generate_with_nano_banana(config["prompt"], logo_path, name)
        results.append((name, result))
        time.sleep(3)

    print("\n" + "=" * 60)
    print("COMPLETE")
    print("=" * 60)

    success = sum(1 for _, r in results if r)
    print(f"Success: {success}/{len(results)}")
    print(f"Output: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
