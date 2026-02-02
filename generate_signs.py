# -*- coding: utf-8 -*-
"""
Brasa Roja Restaurant Sign Concepts
8 different illumination/design concepts
"""

from google import genai
from google.genai import types
from pathlib import Path
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

GEMINI_API_KEY = "AIzaSyAu9WSLO7DKlCSl_SFdzlw8X7Bx0XQx1PI"
OUTPUT_DIR = Path(r"C:\Users\maxys\OneDrive\Imágenes\BrasaRoja\Sign_Concepts")
OUTPUT_DIR.mkdir(exist_ok=True)

LOGO_FULL = Path(r"C:\Users\maxys\OneDrive\Imágenes\BrasaRoja\Assets\Logo_Full\Logo_Transparent.png")

client = genai.Client(api_key=GEMINI_API_KEY)

def load_image(path: Path) -> types.Part:
    with open(path, 'rb') as f:
        data = f.read()
    return types.Part.from_bytes(data=data, mime_type='image/png')

# 8 Sign Concepts with different illumination styles
SIGN_CONCEPTS = {
    "01_flame_only_lit": {
        "prompt": """Create a photorealistic restaurant exterior sign mockup based on this logo.

CONCEPT: FLAME-ONLY ILLUMINATED
- The flame icon is the ONLY illuminated element - glowing bright red-orange LED from within
- "BRASA" text in brushed gold metal (NOT lit, catches ambient light)
- "ROJA" text in dark red powder-coated metal (NOT lit)
- Rising ember dots are small LED points that glow softly
- Sign mounted on dark charcoal/black metal backing plate
- Wall-mounted on brick exterior

Show TWO views: DAYTIME (flame still visible, metallic text gleams) and DUSK/NIGHT (flame dramatically glows, creates warm ambient light)
Professional architectural signage photography, 4K"""
    },

    "02_roja_and_flame_lit": {
        "prompt": """Create a photorealistic restaurant exterior sign mockup based on this logo.

CONCEPT: "ROJA" + FLAME ILLUMINATED (specific request)
- Flame icon illuminated with internal red-orange LED, glowing intensely
- "BRASA" text in NON-LIT brushed gold/brass metal
- "ROJA" text is ILLUMINATED - deep red LED channel letters glowing
- The contrast between lit ROJA and unlit BRASA creates visual drama
- Gold swirl element has subtle gold LED edge lighting
- Mounted on matte black metal plate on dark brick wall

Show at NIGHT TIME - the lit ROJA and flame pop dramatically while BRASA remains elegant but dark
Professional architectural photography, dramatic lighting, 4K"""
    },

    "03_full_neon_outline": {
        "prompt": """Create a photorealistic restaurant exterior sign mockup based on this logo.

CONCEPT: FULL NEON OUTLINE SIGN
- Entire logo rendered in LED neon flex tubing
- Flame outlined in gradient neon: red at base, orange-yellow at tips
- Golden swirl in warm amber neon
- "BRASA" in gold/amber neon tubes
- "ROJA" in red neon tubes
- Rising embers as small neon dots
- Mounted on clear acrylic backing with standoffs on dark wall
- Classic neon sign aesthetic with modern LED neon durability

Show at NIGHT - full neon glow effect, vibrant colors
Urban restaurant district setting, 4K"""
    },

    "04_halo_backlit_channel": {
        "prompt": """Create a photorealistic restaurant exterior sign mockup based on this logo.

CONCEPT: HALO-LIT / BACKLIT CHANNEL LETTERS
- 3D dimensional channel letters with REVERSE/HALO lighting
- Letters and flame are raised brushed metal on front
- LED lighting behind each element creates glowing halo effect on wall
- Flame has warm orange-red halo glow
- "BRASA" has warm gold halo glow
- "ROJA" has deep red halo glow
- Creates sophisticated, upscale restaurant appearance
- Mounted on light stucco or cream-colored wall

Show at TWILIGHT - the halo effect visible, elegant and premium feel
High-end restaurant exterior, 4K architectural photography"""
    },

    "05_blade_projecting_sign": {
        "prompt": """Create a photorealistic restaurant blade sign (projecting sign) mockup based on this logo.

CONCEPT: CIRCULAR BLADE/PROJECTING SIGN (inspired by classic cafe signs)
- Double-sided circular sign projecting from wall on ornate iron bracket
- Black circular frame with the Brasa Roja logo centered
- Flame icon dimensional and internally lit with red-orange LED
- "BRASAROJA" text in gold and red on black background
- Iron bracket has decorative scrollwork matching brand aesthetic
- Sign hangs perpendicular to building for visibility from street

Show from STREET ANGLE - visible to pedestrians walking by
Day and night visibility, classic European cafe style, 4K"""
    },

    "06_dimensional_fire_effect": {
        "prompt": """Create a photorealistic restaurant exterior sign mockup based on this logo.

CONCEPT: 3D DIMENSIONAL FLAME WITH ANIMATED EFFECT
- Flame is HIGHLY DIMENSIONAL - multiple layered acrylic pieces
- Each flame layer has separate LED lighting creating depth
- Flame appears to flicker/dance with layered lighting effect
- Rising embers are fiber optic points that twinkle
- "BRASA" in raised brushed brass letters
- "ROJA" in raised deep red metallic letters
- Gold swirl is edge-lit acrylic with golden glow
- Mounted on weathered steel/corten backdrop

Show at NIGHT - the dimensional flame creates stunning 3D fire illusion
Modern industrial restaurant exterior, 4K"""
    },

    "07_vintage_marquee_bulbs": {
        "prompt": """Create a photorealistic restaurant exterior sign mockup based on this logo.

CONCEPT: VINTAGE MARQUEE WITH EXPOSED EDISON BULBS
- Retro/vintage aesthetic with modern twist
- Large dimensional letters "BRASAROJA" with exposed warm Edison bulbs outlining each letter
- Flame icon rendered as metal cutout with bulbs tracing the flame shape
- Bulbs are warm amber 2700K color temperature
- Sign mounted on reclaimed wood or rusted metal backing
- Industrial restaurant/gastropub aesthetic
- Combines nostalgia with the fire/warmth of the brand

Show at DUSK - warm bulbs glowing, inviting atmosphere
Rustic-industrial restaurant facade, 4K"""
    },

    "08_smart_led_ember_animation": {
        "prompt": """Create a photorealistic restaurant exterior sign mockup based on this logo.

CONCEPT: SMART LED WITH ANIMATED RISING EMBERS
- Modern programmable LED sign panel
- Flame icon is static lit element (red-orange glow)
- "BRASA" in gold LED channel letters
- "ROJA" in red LED channel letters
- SPECIAL FEATURE: The rising ember dots are individually addressable LEDs
- Embers animate - slowly rising and fading like real sparks from fire
- Creates mesmerizing, eye-catching motion that draws attention
- Sleek modern aluminum frame, minimal design

Show at NIGHT - capture the ember animation mid-rise
Contemporary urban restaurant, 4K"""
    },
}

def generate_sign(prompt: str, logo_path: Path, filename: str) -> str:
    """Generate sign concept using Nano Banana Pro"""
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
    print("BRASA ROJA SIGN CONCEPTS GENERATOR")
    print("8 Different Illumination Designs")
    print("=" * 60)
    print()
    print("Concepts:")
    print("  1. Flame-Only Illuminated")
    print("  2. ROJA + Flame Illuminated (requested)")
    print("  3. Full Neon Outline")
    print("  4. Halo-Lit/Backlit Channel Letters")
    print("  5. Blade/Projecting Sign (cafe style)")
    print("  6. 3D Dimensional Fire Effect")
    print("  7. Vintage Marquee Edison Bulbs")
    print("  8. Smart LED with Animated Embers")
    print()

    results = []
    for name, config in SIGN_CONCEPTS.items():
        print(f"Generating: {name}")
        result = generate_sign(config["prompt"], LOGO_FULL, name)
        results.append((name, result))
        time.sleep(4)  # Rate limiting

    print("\n" + "=" * 60)
    print("COMPLETE")
    print("=" * 60)

    success = sum(1 for _, r in results if r)
    print(f"Success: {success}/{len(results)}")
    print(f"Output: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
