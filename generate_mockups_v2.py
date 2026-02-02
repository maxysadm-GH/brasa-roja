# -*- coding: utf-8 -*-
"""
Brasa Roja Mockup Generator v2
Uses actual logo image for accurate brand representation
"""

from google import genai
from google.genai import types
from pathlib import Path
import time
import sys
import base64

sys.stdout.reconfigure(encoding='utf-8')

GEMINI_API_KEY = "AIzaSyAu9WSLO7DKlCSl_SFdzlw8X7Bx0XQx1PI"
OUTPUT_DIR = Path(r"C:\Users\maxys\OneDrive\Imágenes\BrasaRoja\Mockups_v2")
OUTPUT_DIR.mkdir(exist_ok=True)

# Actual logo files
LOGO_FULL = Path(r"C:\Users\maxys\OneDrive\Imágenes\BrasaRoja\Assets\Logo_Full\Logo_Transparent.png")
LOGO_ICON = Path(r"C:\Users\maxys\OneDrive\Imágenes\BrasaRoja\Clean Files\BR Icon NBG.png")

client = genai.Client(api_key=GEMINI_API_KEY)

def load_image(path: Path) -> types.Part:
    """Load image file as Part for API"""
    with open(path, 'rb') as f:
        data = f.read()
    return types.Part.from_bytes(data=data, mime_type='image/png')

# Updated mockups with corrections
MOCKUPS = {
    "01_tshirt_black": {
        "use_logo": "icon",
        "prompt": """Create a professional product photography mockup of this EXACT logo on a black crew neck t-shirt.

CRITICAL: Use this EXACT logo image provided - do not modify, redesign, or reinterpret it. The logo must appear EXACTLY as shown.

Mockup details:
- Black crew neck t-shirt laying flat on dark slate surface
- Logo embroidered on LEFT CHEST area (small, approximately 3 inches wide)
- Below the flame icon, add text "BRASAROJA" where "BRASA" is metallic gold and "ROJA" is deep red
- Below that in small gold script: "Tradicion Familiar"
- Studio lighting with soft shadows
- 4K commercial product photography
- Clean minimalist background"""
    },

    "02_takeout_box": {
        "use_logo": "full",
        "prompt": """Create a professional product photography mockup featuring this EXACT logo on premium packaging.

CRITICAL: Use this EXACT logo image provided - do not modify, redesign, or reinterpret it. The logo must appear EXACTLY as shown with the flame, orange swirl, rising embers, and text.

Mockup details:
- Premium BLACK matte takeout container/box
- Logo printed centered on the lid
- Gold foil accent line around the edge of the box
- Box slightly open showing kraft paper lining inside
- Styled on dark walnut wooden table
- Fresh rosemary and thyme sprigs as props
- Cream colored linen napkin folded nearby
- Warm restaurant tungsten lighting
- 4K food packaging photography"""
    },

    "03_paper_bag_black": {
        "use_logo": "full",
        "prompt": """Create a professional product photography mockup featuring this EXACT logo on a shopping bag.

CRITICAL: Use this EXACT logo image provided - do not modify, redesign, or reinterpret it. The logo must appear EXACTLY as shown.

Mockup details:
- BLACK matte paper shopping bag with twisted rope handles (NOT kraft/brown - must be BLACK)
- Logo printed large and centered on the bag
- Subtle gold foil stripe accent near the bottom
- Bag standing upright at 3/4 angle
- Clean white/light gray studio background
- Soft natural shadow beneath
- Professional packaging mockup style
- 4K commercial photography"""
    },

    "04_apron_chef": {
        "use_logo": "full",
        "prompt": """Create a professional product photography mockup featuring this EXACT logo on a chef's apron.

CRITICAL: Use this EXACT logo image provided - do not modify, redesign, or reinterpret it. The logo must appear EXACTLY as shown.

Mockup details:
- Black chef's bib apron on rustic wooden hanger
- Logo embroidered/printed large on chest area
- Apron displayed against exposed red brick wall
- Warm Edison bulb pendant lights visible
- Copper pots hanging in background
- Rustic kitchen/restaurant ambiance
- Warm tungsten lighting
- 4K commercial hospitality photography"""
    },

    "05_chef_formal_shirt": {
        "use_logo": "icon",
        "prompt": """Create a professional product photography mockup featuring this EXACT logo on a formal chef coat.

CRITICAL: Use this EXACT logo image provided - do not modify or reinterpret it. The logo must appear EXACTLY as shown.

Mockup details:
- Black formal chef coat/jacket with mandarin collar
- Double-breasted style with black buttons
- Logo embroidered small on LEFT CHEST (about 2.5 inches)
- Below logo: "BRASAROJA" text with "BRASA" in gold thread, "ROJA" in red thread
- Chef coat displayed on professional mannequin or laid flat
- Clean dark background
- Professional studio lighting
- 4K commercial uniform photography"""
    },

    "06_cup_sleeve": {
        "use_logo": "icon",
        "prompt": """Create a professional product photography mockup featuring this EXACT logo on a coffee cup sleeve.

CRITICAL: Use this EXACT logo image provided - do not modify or reinterpret it. The logo must appear EXACTLY as shown.

Mockup details:
- BLACK branded cup sleeve wrapped around white paper coffee cup
- Logo printed centered on the sleeve
- "BRASAROJA" text below logo
- Gold accent lines at top and bottom of sleeve
- Small repeating flame pattern in background of sleeve design
- Cup on white marble countertop
- Scattered coffee beans as props
- Steam rising from cup
- Warm morning cafe lighting from window
- 4K commercial product photography"""
    },
}

def generate_with_logo(prompt: str, logo_path: Path, filename: str) -> str:
    """Generate mockup using actual logo image as reference"""
    try:
        logo_part = load_image(logo_path)

        response = client.models.generate_content(
            model='gemini-2.0-flash-exp-image-generation',
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
                print(f"[OK] {filename}.png (Gemini Flash)")
                return str(output_path)

        print(f"[NO IMAGE] {filename}")
        return None
    except Exception as e:
        print(f"[ERROR] {filename}: {e}")
        return None

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
                print(f"[OK] {filename}.png (Nano Banana Pro)")
                return str(output_path)

        print(f"[NO IMAGE] {filename}")
        return None
    except Exception as e:
        print(f"[ERROR] {filename}: {e}")
        return None

def generate_mockup(name: str, config: dict) -> str:
    """Generate a single mockup with fallback"""
    logo_path = LOGO_ICON if config["use_logo"] == "icon" else LOGO_FULL
    prompt = config["prompt"]

    # Try Nano Banana Pro first (better quality)
    result = generate_with_nano_banana(prompt, logo_path, name)
    if result:
        return result

    # Fallback to Gemini Flash
    result = generate_with_logo(prompt, logo_path, name)
    return result

def main():
    print("=" * 60)
    print("BRASA ROJA MOCKUP GENERATOR v2")
    print("Using ACTUAL logo for brand accuracy")
    print("=" * 60)
    print()
    print("Corrections applied:")
    print("  - Using exact approved logo (not AI interpretation)")
    print("  - Paper bag changed to BLACK")
    print("  - Added Chef Formal Shirt")
    print()

    results = []
    for name, config in MOCKUPS.items():
        print(f"Generating: {name}")
        result = generate_mockup(name, config)
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
