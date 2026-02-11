# -*- coding: utf-8 -*-
"""
Brasa Roja - 6 Views of the APPROVED Smart LED Sign (v4)
FIXES from v3 audit:
  - Sign shape MUST be SQUARE (1:1 ratio) in every view — v3 had some landscape rectangles
  - Stick as close as possible to the approved design
  - Every view must show the SAME square sign, only camera angle and lighting differ
"""

import sys
import os
import time
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not set. Check .env file.")

from google import genai
from google.genai import types

OUTPUT_DIR = Path(r"C:\Users\maxys\OneDrive\Imágenes\BrasaRoja\Sign_6Views_v4")
OUTPUT_DIR.mkdir(exist_ok=True)

APPROVED_SIGN = Path(r"G:\My Drive\Projects\Brasa Roja\Sign_Concepts\08_smart_led_ember_animation.png")
if not APPROVED_SIGN.exists():
    raise FileNotFoundError(f"Approved sign image not found: {APPROVED_SIGN}")

client = genai.Client(api_key=GEMINI_API_KEY)


def load_image(path: Path) -> types.Part:
    with open(path, 'rb') as f:
        data = f.read()
    return types.Part.from_bytes(data=data, mime_type='image/png')


# ============================================================
# SIGN IDENTITY — shared across ALL prompts for consistency
# The sign is SQUARE. This is non-negotiable.
# ============================================================

SIGN_LOCK = """This is a photograph of the APPROVED Brasa Roja restaurant sign. Generate the SAME EXACT sign from a different camera angle.

THE SIGN IS A PERFECT SQUARE. The width and height of the sign panel are EQUAL. Do NOT make the sign rectangular, landscape, or portrait. It is a 1:1 SQUARE.

SIGN DETAILS (DO NOT MODIFY ANY OF THESE):
- SQUARE smart LED panel sign (equal width and height, approximately 1.5m x 1.5m)
- Brushed aluminum/chrome frame with rounded corners wrapping all 4 sides equally
- The frame has 15-20cm depth
- Inside: SOLID BLACK LED screen background
- The Brasa Roja logo is centered on the black screen with equal padding on all 4 sides
- Logo layout (top to bottom): flame icon with golden orbital swirl and rising ember dots, then "BRASAROJA" text with "BRASA" in gold and "ROJA" in red, then "Tradicion Familiar" tagline in gold script
- All logo elements GLOW (LED-lit, not flat print)
- Warm amber LED accent light at the top edge illuminates downward
- Mounted on a CLEAN WHITE WALL (smooth white stucco/painted concrete, NO brick)
- Sign is mounted with metal standoffs creating a gap from the wall

CRITICAL: The sign is SQUARE. Keep the EXACT same proportions, logo layout, and colors as the reference image."""


SIGN_VIEWS = {
    "01_frontal_noche": {
        "name": "01 - Frontal Straight-On, Night",
        "prompt": f"""{SIGN_LOCK}

CAMERA: STRAIGHT-ON FRONTAL (perpendicular, 0 degrees, centered)
Camera directly in front, at sign center height. Sign perfectly centered in frame. No perspective distortion.

LIGHTING: NIGHTTIME
- Dark sky, sign is primary light source
- LED panel brilliantly illuminated, logo glowing vividly
- Warm amber accent light washes golden light down onto white wall
- Aluminum frame reflects subtle LED glow
- White wall partially lit by sign's warm light

Professional architectural night photography, symmetrical, sharp, 4K."""
    },

    "02_frontal_dia": {
        "name": "02 - Frontal Straight-On, Daytime",
        "prompt": f"""{SIGN_LOCK}

CAMERA: STRAIGHT-ON FRONTAL (perpendicular, 0 degrees, centered)
Camera directly in front, at sign center height. Sign perfectly centered in frame. No perspective distortion.

LIGHTING: BRIGHT MIDDAY SUN
- Clear blue sky, direct overhead sunlight
- LED panel still ON, logo readable against daylight
- Aluminum frame gleams with sun reflections
- White wall brightly lit, clean
- Sign casts subtle shadow on white wall
- Construction quality visible in natural light

Professional architectural daytime documentation, symmetrical, 4K."""
    },

    "03_angulo_izq_noche": {
        "name": "03 - 45 Degrees from LEFT, Night",
        "prompt": f"""{SIGN_LOCK}

CAMERA: 45 DEGREES FROM THE LEFT
Camera to the left of the sign, looking at it from 45-degree angle. Left edge of frame closer to camera showing depth/thickness. Right side recedes with perspective. Camera at sign center height.

LIGHTING: NIGHTTIME
- Dark scene, sign is primary light source
- LED panel glowing, logo clearly visible at this angle
- Amber accent light washes warm light down white wall
- Left edge of aluminum frame catches strong LED reflections
- City bokeh in distant background

Professional nighttime architectural photography, 45-degree left perspective, 4K."""
    },

    "04_angulo_der_dia": {
        "name": "04 - 45 Degrees from RIGHT, Daytime",
        "prompt": f"""{SIGN_LOCK}

CAMERA: 45 DEGREES FROM THE RIGHT
Camera to the right of the sign, looking at it from 45-degree angle. Right edge of frame closer to camera showing depth/thickness. Left side recedes with perspective. Camera at sign center height.

LIGHTING: AFTERNOON SUN
- Warm afternoon sunlight from the right
- Right edge of aluminum frame catches bright sunlight highlight
- LED panel ON, logo visible in daylight
- Sign casts directional shadow on white wall to the left
- Blue sky with some clouds

Professional daytime architectural photography, 45-degree right perspective, 4K."""
    },

    "05_perfil_lateral": {
        "name": "05 - Side Profile (edge-on), Daytime",
        "prompt": f"""{SIGN_LOCK}

CAMERA: SIDE PROFILE VIEW (approximately 80-85 degrees from front)
Camera almost directly to the side. Sees primarily the EDGE/THICKNESS of the SQUARE sign panel. Full 15-20cm depth of aluminum frame visible. Gap between sign back and white wall visible. Mounting standoffs/brackets visible. A sliver of the LED face wrapping around. Top accent light visible from side.

LIGHTING: BRIGHT DAYTIME
- Clear natural light showing materials and construction
- Aluminum frame edge well-lit, brushed metal texture visible
- White wall extends behind, bright and clean
- Shadows reveal depth and standoff distance
- Technical/engineering documentation photo

Professional technical photography showing construction depth, daytime, 4K."""
    },

    "06_contrapicado_noche": {
        "name": "06 - Low Angle Looking Up, Night",
        "prompt": f"""{SIGN_LOCK}

CAMERA: LOW ANGLE LOOKING UPWARD (contrapicado, ~30 degrees up)
Camera below the sign, looking up. Bottom edge of frame closest to camera. Sign appears imposing from below. White wall extends upward behind sign.

LIGHTING: NIGHTTIME - DRAMATIC
- Dark night sky above the sign
- LED panel glows brilliantly from this dramatic low angle
- Amber accent light creates warm halo on white wall above
- Underside of sign catches warm ambient LED light
- Bottom aluminum frame edge highlighted by glow
- Powerful, dramatic, heroic presentation

Professional nighttime architectural photography, dramatic low angle, 4K."""
    },
}


def generate_view(prompt: str, reference_image_path: Path, filename: str) -> str:
    """Generate a single view using the approved sign as reference input."""
    try:
        sign_ref = load_image(reference_image_path)

        response = client.models.generate_content(
            model='gemini-2.0-flash-exp-image-generation',
            contents=[sign_ref, prompt],
            config=types.GenerateContentConfig(
                response_modalities=['IMAGE', 'TEXT'],
            )
        )

        for part in response.candidates[0].content.parts:
            if part.inline_data and part.inline_data.mime_type.startswith('image'):
                output_path = OUTPUT_DIR / f"{filename}.png"
                with open(output_path, 'wb') as f:
                    f.write(part.inline_data.data)
                print(f"  [OK] Saved: {output_path.name}")
                return str(output_path)
            elif part.text:
                print(f"  [TEXT] {part.text[:200]}")

        print(f"  [NO IMAGE] No image returned for {filename}")
        return None

    except Exception as e:
        print(f"  [ERROR] {filename}: {e}")
        return None


def main():
    print("=" * 65)
    print("  BRASA ROJA - 6 VIEWS v4 (SQUARE SHAPE FIX)")
    print("  Fix: sign must be SQUARE in every view")
    print("=" * 65)
    print()
    print(f"  Reference: {APPROVED_SIGN}")
    print(f"  Output:    {OUTPUT_DIR}")
    print(f"  Model:     gemini-2.0-flash-exp-image-generation")
    print()
    print("  Views:")
    for i, (key, view) in enumerate(SIGN_VIEWS.items(), 1):
        print(f"    {i}. {view['name']}")
    print()
    print("-" * 65)

    results = []
    total = len(SIGN_VIEWS)

    for i, (key, view) in enumerate(SIGN_VIEWS.items(), 1):
        print(f"\n[{i}/{total}] Generating: {view['name']}")
        result = generate_view(view["prompt"], APPROVED_SIGN, key)
        results.append((view["name"], result))

        if i < total:
            print("  Waiting 5s (rate limit)...")
            time.sleep(5)

    print("\n" + "=" * 65)
    print("  GENERATION COMPLETE")
    print("=" * 65)

    success = sum(1 for _, r in results if r)
    print(f"\n  Results: {success}/{total} images generated")
    print(f"  Output:  {OUTPUT_DIR}")
    print()

    for name, result in results:
        status = "OK" if result else "FAILED"
        print(f"  [{status}] {name}")


if __name__ == "__main__":
    main()
