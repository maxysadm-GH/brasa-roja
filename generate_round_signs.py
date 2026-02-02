# -*- coding: utf-8 -*-
"""
Brasa Roja Round/Blade Sign Concepts
5 variations of circular projecting signs
"""

from google import genai
from google.genai import types
from pathlib import Path
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

import os
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set")
OUTPUT_DIR = Path(r"C:\Users\maxys\OneDrive\Imágenes\BrasaRoja\Sign_Concepts\Round_Signs")
OUTPUT_DIR.mkdir(exist_ok=True)

LOGO_FULL = Path(r"C:\Users\maxys\OneDrive\Imágenes\BrasaRoja\Assets\Logo_Full\Logo_Transparent.png")

client = genai.Client(api_key=GEMINI_API_KEY)

def load_image(path: Path) -> types.Part:
    with open(path, 'rb') as f:
        data = f.read()
    return types.Part.from_bytes(data=data, mime_type='image/png')

# 5 Round/Blade Sign Variations
ROUND_SIGNS = {
    "round_01_neon_edge": {
        "prompt": """Create a photorealistic circular blade/projecting restaurant sign mockup based on this logo.

CONCEPT: ROUND SIGN WITH NEON EDGE LIGHTING
- Double-sided CIRCULAR sign projecting perpendicular from wall
- Black matte circular face with the Brasa Roja logo centered
- THE ENTIRE CIRCULAR EDGE is outlined with RED LED NEON creating a glowing ring
- Flame icon illuminated from within (red-orange glow)
- "BRASAROJA" text - BRASA in gold, ROJA in red
- Ornate black wrought iron bracket with decorative scrollwork
- Mounted on classic brick building exterior

Show at NIGHT - the neon ring edge glows dramatically, flame illuminated
European street setting, pedestrian view, 4K architectural photography"""
    },

    "round_02_backlit_halo": {
        "prompt": """Create a photorealistic circular blade/projecting restaurant sign mockup based on this logo.

CONCEPT: ROUND SIGN WITH BACKLIT HALO GLOW
- Double-sided CIRCULAR sign on decorative iron bracket
- Sign face is brushed copper/bronze metal
- Logo elements are CUT OUT - light shines THROUGH the cutouts
- Warm amber LED backlighting creates glowing halo effect around entire sign
- Flame cutout glows warm orange
- Text cutouts glow golden
- Creates ethereal, premium appearance
- Vintage-style curved iron mounting bracket

Show at DUSK - warm backlit glow visible, sophisticated ambiance
Upscale neighborhood restaurant exterior, 4K"""
    },

    "round_03_double_ring": {
        "prompt": """Create a photorealistic circular blade/projecting restaurant sign mockup based on this logo.

CONCEPT: DOUBLE RING CIRCULAR SIGN
- Double-sided CIRCULAR projecting sign
- TWO concentric circular rings - outer ring gold, inner ring red
- Both rings are illuminated LED channel
- Black center with Brasa Roja logo
- Flame icon has internal red-orange LED illumination
- "BRASAROJA" in dimensional letters - gold and red
- Minimalist modern black metal bracket (clean lines, not ornate)
- Mounted on contemporary gray stucco wall

Show at NIGHT - double illuminated rings create striking visual
Modern urban restaurant district, 4K"""
    },

    "round_04_rustic_wood": {
        "prompt": """Create a photorealistic circular blade/projecting restaurant sign mockup based on this logo.

CONCEPT: RUSTIC WOOD ROUND SIGN
- Double-sided CIRCULAR sign made of dark reclaimed WOOD
- Circular wooden frame with metal ring edge
- Logo laser-cut into wood, backed with warm LED lighting shining through
- Flame portion is metal cutout with orange LED behind
- "BRASAROJA" wood-burned or raised copper letters
- Rustic wrought iron bracket with farm/hacienda style curves
- Mounted on adobe or terracotta colored stucco wall

Show at TWILIGHT - warm light glowing through wood cutouts
Rustic Mexican/Spanish restaurant exterior, warm inviting feel, 4K"""
    },

    "round_05_glass_illuminated": {
        "prompt": """Create a photorealistic circular blade/projecting restaurant sign mockup based on this logo.

CONCEPT: ILLUMINATED GLASS ROUND SIGN
- Double-sided CIRCULAR sign with GLASS faces
- Thick black metal circular frame
- Interior is edge-lit glass panel with logo printed/etched
- Entire sign face glows evenly when lit (like a lightbox)
- Flame appears to glow from within the glass
- "BRASAROJA" clearly visible, sharp graphics
- Classic ornate iron bracket with spiral details
- Gold accent ring around the glass edge

Show at NIGHT - entire circular face glows like a beacon
Classic European street corner, highly visible, 4K"""
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
    print("BRASA ROJA ROUND SIGN CONCEPTS")
    print("5 Circular Blade/Projecting Sign Variations")
    print("=" * 60)
    print()

    results = []
    for name, config in ROUND_SIGNS.items():
        print(f"Generating: {name}")
        result = generate_sign(config["prompt"], LOGO_FULL, name)
        results.append((name, result))
        time.sleep(4)

    print("\n" + "=" * 60)
    print("COMPLETE")
    print("=" * 60)

    success = sum(1 for _, r in results if r)
    print(f"Success: {success}/{len(results)}")
    print(f"Output: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
