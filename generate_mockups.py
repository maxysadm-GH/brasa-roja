# -*- coding: utf-8 -*-
"""
Brasa Roja Mockup Generator
Uses Google Gemini API (Nano Banana Pro / Imagen 4) for image generation
"""

from google import genai
from google.genai import types
from pathlib import Path
import time
import sys
import base64

# Fix Windows console encoding
sys.stdout.reconfigure(encoding='utf-8')

import os
from dotenv import load_dotenv
load_dotenv()
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set")

# Output directory
OUTPUT_DIR = Path(r"C:\Users\maxys\OneDrive\Imágenes\BrasaRoja\Mockups")
OUTPUT_DIR.mkdir(exist_ok=True)

# Initialize client
client = genai.Client(api_key=GEMINI_API_KEY)

# Mockup prompts - prioritized for cost effectiveness
MOCKUPS = {
    "01_tshirt_black": """Professional product photography of a black crew neck t-shirt laying flat on a dark slate surface. The t-shirt features embroidered branding: a stylized flame icon in red-orange gradient with a golden orbital swirl around its base, positioned on the left chest. Below the flame icon reads "BRASAROJA" in serif font where "BRASA" is gold and "ROJA" is crimson red. Underneath in elegant script reads "Tradicion Familiar" in gold. Studio lighting with soft shadows, 4K resolution, commercial product photography style, clean minimalist background.""",

    "02_takeout_box": """Overhead product photography of premium black takeout container with gold foil accents. Box features the Brasa Roja flame logo centered with embossed golden swirl, brand name "BRASAROJA" in gold and red below with "Tradicion Familiar" tagline. Box is slightly open revealing kraft paper lining. Styled on dark wooden table with scattered fresh herbs and a folded cream napkin. Warm restaurant lighting, 4K food packaging photography.""",

    "03_paper_bag": """Commercial photography of kraft paper shopping bag with twisted rope handles standing upright. Bag features full-color printed Brasa Roja logo: flame icon with red-orange gradient, golden orbital swirl wrapping around base, rising golden ember sparks. "BRASAROJA" text with gold "BRASA" and red "ROJA" split, elegant script tagline "Tradicion Familiar" below. Black decorative band at bottom with gold stripe accent. Clean white background with soft natural shadow, professional packaging mockup, 4K resolution.""",

    "04_apron_chef": """Professional product photography of a black chef bib apron displayed on rustic wooden hanger against exposed brick wall. The apron features premium embroidered branding on chest area: a stylized flame icon with red-orange gradient, golden swirl orbit around base, and golden ember sparks rising above. Text reads "BRASAROJA" with "BRASA" in metallic gold thread and "ROJA" in crimson. Script tagline "Tradicion Familiar" embroidered below. Warm tungsten lighting creating authentic restaurant ambiance, 4K resolution, commercial hospitality photography.""",

    "05_cup_sleeve": """Product photography of black branded coffee cup sleeve wrapped around white paper cup. Sleeve features the Brasa Roja flame logo repeated pattern with gold accent lines at top and bottom edges. Central logo placement with flame, golden swirl, and "BRASAROJA" branding clearly visible. Styled on white marble countertop with scattered coffee beans and steam wisps. Warm morning light from side window, commercial coffee shop aesthetic, 4K product photography.""",
}

def generate_with_imagen(prompt: str, filename: str) -> str:
    """Generate image using Imagen 4.0"""
    try:
        response = client.models.generate_images(
            model='imagen-4.0-generate-001',
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
                output_options=types.OutputOptions(
                    mime_type='image/png',
                ),
            )
        )

        if response.generated_images:
            output_path = OUTPUT_DIR / f"{filename}.png"
            image = response.generated_images[0]
            image.image.save(str(output_path))
            print(f"[OK] Saved: {filename}.png (Imagen 4)")
            return str(output_path)
        return None
    except Exception as e:
        print(f"[Imagen Error] {e}")
        return None

def generate_with_gemini_flash(prompt: str, filename: str) -> str:
    """Generate image using Gemini 2.0 Flash Image Generation"""
    try:
        response = client.models.generate_content(
            model='gemini-2.0-flash-exp-image-generation',
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=['IMAGE', 'TEXT'],
            )
        )

        # Extract image from response
        for part in response.candidates[0].content.parts:
            if part.inline_data and part.inline_data.mime_type.startswith('image'):
                output_path = OUTPUT_DIR / f"{filename}.png"
                with open(output_path, 'wb') as f:
                    f.write(part.inline_data.data)
                print(f"[OK] Saved: {filename}.png (Gemini Flash)")
                return str(output_path)
        return None
    except Exception as e:
        print(f"[Gemini Flash Error] {e}")
        return None

def generate_with_nano_banana(prompt: str, filename: str) -> str:
    """Generate image using Nano Banana Pro Preview"""
    try:
        response = client.models.generate_content(
            model='nano-banana-pro-preview',
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=['IMAGE', 'TEXT'],
            )
        )

        # Extract image from response
        for part in response.candidates[0].content.parts:
            if part.inline_data and part.inline_data.mime_type.startswith('image'):
                output_path = OUTPUT_DIR / f"{filename}.png"
                with open(output_path, 'wb') as f:
                    f.write(part.inline_data.data)
                print(f"[OK] Saved: {filename}.png (Nano Banana Pro)")
                return str(output_path)
        return None
    except Exception as e:
        print(f"[Nano Banana Error] {e}")
        return None

def generate_image(prompt: str, filename: str) -> str:
    """Try multiple methods to generate image"""
    # Try Imagen 4 first (best quality)
    result = generate_with_imagen(prompt, filename)
    if result:
        return result

    # Fallback to Nano Banana Pro
    result = generate_with_nano_banana(prompt, filename)
    if result:
        return result

    # Fallback to Gemini Flash
    result = generate_with_gemini_flash(prompt, filename)
    if result:
        return result

    print(f"[FAIL] Could not generate {filename}")
    return None

def main():
    print("=" * 60)
    print("BRASA ROJA MOCKUP GENERATOR")
    print("Using Google AI: Imagen 4 / Nano Banana Pro")
    print("=" * 60)
    print()

    results = []

    for name, prompt in MOCKUPS.items():
        print(f"\nGenerating: {name}")
        result = generate_image(prompt, name)
        results.append((name, result))
        time.sleep(3)  # Rate limiting

    print("\n" + "=" * 60)
    print("GENERATION COMPLETE")
    print("=" * 60)

    success = sum(1 for _, r in results if r)
    print(f"\nSuccess: {success}/{len(results)}")
    print(f"Output folder: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
