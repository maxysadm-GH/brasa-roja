# Brasa Roja - Project Memory & Skills

## Project Overview
**Brand:** Brasa Roja - Family tradition Mexican restaurant
**Tagline:** "Tradición Familiar"
**Domain:** brasaroja.com
**Lovable Project:** https://lovable.dev/projects/7738bc22-270b-430e-a394-82d168fd8023

---

## Brand Guidelines Summary

### Logo Elements
1. **Flame** - Red flame with inner darker flame shape, 3 points (past, present, future)
2. **Golden Swirl** - Orange-to-gold gradient orbital swirl wrapping around flame base
3. **Rising Embers** - Small dots/particles rising upward from flame
4. **Typography** - "BRASA" (gold serif) + "ROJA" (red serif)
5. **Tagline** - "Tradición Familiar" in gold script (REQUIRED on all branded materials)

### Color Palette (AUTHORITATIVE - verified against brand guide + Pantone)
| Color | Hex | Pantone | Use |
|-------|-----|---------|-----|
| Primary Red | #E44D26 | - | Flame LED glow |
| Rojo Roja | #C63333 | PMS 1797 C | "ROJA" text |
| Oro Brasa | #C9882B | PMS 7564 C | "BRASA" text, swirl, embers |
| Brasa Profunda | #8B2500 | PMS 7622 C | Dark accents |
| Light Neutral | #F6F0E6 | - | Cream backgrounds |
| Charcoal | #2D2D2D | PMS Black 7 C | Dark backgrounds |

### Brand Rules
- Logo must include ALL elements (flame, swirl, embers, text)
- "Tradición Familiar" tagline REQUIRED on branded materials
- Packaging should be BLACK (not kraft/brown)
- Do not modify, stretch, or recolor the logo

---

## AI Image Generation Skill

### API Configuration
```python
# Google Gemini API (Nano Banana Pro)
from google import genai
from google.genai import types

client = genai.Client(api_key="YOUR_GEMINI_API_KEY")

# Available models for image generation:
# - nano-banana-pro-preview (best quality, supports image input)
# - gemini-2.0-flash-exp-image-generation
# - imagen-4.0-generate-001
```

### Image-to-Image Generation Pattern
For brand-accurate mockups, always use the actual logo as input:

```python
def load_image(path: Path) -> types.Part:
    with open(path, 'rb') as f:
        data = f.read()
    return types.Part.from_bytes(data=data, mime_type='image/png')

def generate_with_logo(prompt: str, logo_path: Path, filename: str):
    logo_part = load_image(logo_path)

    response = client.models.generate_content(
        model='nano-banana-pro-preview',
        contents=[logo_part, prompt],  # Logo + prompt
        config=types.GenerateContentConfig(
            response_modalities=['IMAGE', 'TEXT'],
        )
    )

    for part in response.candidates[0].content.parts:
        if part.inline_data and part.inline_data.mime_type.startswith('image'):
            with open(f"{filename}.png", 'wb') as f:
                f.write(part.inline_data.data)
            return True
    return False
```

### Prompt Engineering for Brand Accuracy

**Critical elements to include in prompts:**
1. "Use this EXACT logo image - do not modify or reinterpret"
2. Specify ALL logo elements: flame, swirl, embers, text colors
3. Explicitly state "Tradición Familiar" requirement
4. Define materials (matte black, brushed gold, etc.)
5. Specify lighting conditions and environment

**Example prompt structure:**
```
Create a professional [ITEM] mockup featuring this EXACT logo.

CRITICAL REQUIREMENTS:
1. Use this EXACT logo - do not modify
2. Logo MUST include: flame, orange swirl, rising embers
3. Text: "BRASAROJA" with "BRASA" gold, "ROJA" red
4. MANDATORY: Include "Tradición Familiar" tagline

Mockup details:
- [Item description]
- [Material/finish]
- [Placement]
- [Environment/setting]
- [Lighting]
- 4K [photography type]
```

---

## Generated Assets

### Vectors (SVG)
Location: `Vectors/`
- Logo variations (full, icon, gold mono, white mono)
- Patterns (dark tile, light tile)
- Apparel templates (t-shirt, apron, cap)
- Packaging templates (box, bag, cup sleeve, napkin)

### Mockups (PNG)
Location: `Mockups_v2/` and `Mockups_v3/`
- T-shirt (black)
- Takeout box (black)
- Paper bag (BLACK - per brand guidelines)
- Apron
- Chef formal shirt
- Cup sleeve

### Sign Concepts (PNG)
Location: `Sign_Concepts/`
- 8 main concepts (flame-lit, ROJA+flame, neon, halo, blade, 3D, marquee, LED)
- 5 round blade signs in `Round_Signs/`
- **APPROVED DESIGN:** `08_smart_led_ember_animation.png` (Smart LED square panel)

### Sign 6 Views (v4) - APPROVED SIGN MOCKUPS
Location: `Sign_6Views/`
- `01_frontal_noche.png` - Frontal straight-on, night (LEDs on)
- `02_frontal_dia.png` - Frontal straight-on, daytime
- `03_angulo_izq_noche.png` - 45 degrees from left, night
- `04_angulo_der_dia.png` - 45 degrees from right, daytime
- `05_perfil_lateral.png` - Side profile (edge-on), daytime
- `06_contrapicado_noche.png` - Low angle looking up, night
- Generated with `generate_sign_6views_v4.py` using approved sign as reference input
- All views: SQUARE sign, WHITE wall, consistent logo layout

---

## Vendor Folders (Google Drive)

Three self-contained vendor folders at `G:\My Drive\Projects\Brasa Roja\`:

### Vendor_Letreros/ (Sign Maker)
- 6 mockup views of the approved sign
- ESPECIFICACIONES_LETRERO.md (full tech specs in Spanish/Argentina)
- GUIA_INSTALACION_MANTENIMIENTO.md
- Logos (PNG) + Vectors (SVG/PDF)

### Vendor_Packaging/ (Packaging/Print)
- CMYK 300dpi logos for print
- Vectors: SVG, PDF, EPS (all variants)
- Stickers (2" and 3", multiple backgrounds)
- GUIA_COLORES_PACKAGING.md

### Vendor_Ropa/ (Embroidery/Uniforms)
- Embroidery-ready logos (light/dark garments, simplified)
- Thread specs (Madeira Polyneon codes + Isacord alternatives)
- ESPECIFICACIONES_BORDADO.md (per-garment placement, sizes, thread colors)
- Vectors (SVG/PDF)

---

## Lessons Learned

### 1. AI Image Generation Limitations
- AI creates "interpretations" of logos, not exact reproductions
- Solution: Use image-to-image with actual logo file as input
- Always provide the source logo to maintain brand accuracy

### 2. Brand Compliance Checklist
Before finalizing any mockup, verify:
- [ ] Logo shape matches exactly (flame, swirl, embers)
- [ ] "BRASA" is gold, "ROJA" is red
- [ ] "Tradición Familiar" tagline present
- [ ] Correct color palette used
- [ ] BLACK packaging (not kraft/brown)

### 3. Effective Prompting
- Be explicit about what NOT to change
- List ALL required elements
- Specify "MANDATORY" for critical items
- Describe day AND night appearance for signage

### 4. Cost-Effective API Usage
- Nano Banana Pro: Best for complex, brand-accurate work
- Gemini Flash: Good fallback, faster
- Always include rate limiting (3-4 sec between calls)

### 5. Sign Generation Consistency (v4 lessons)
- Use a SHARED text block (SIGN_LOCK) injected into every prompt for consistency
- Explicitly state the sign SHAPE (square/rectangle) multiple times - AI varies it otherwise
- Specify wall color explicitly ("CLEAN WHITE WALL") - AI defaults to brick
- For multiple angles: use LEFT vs RIGHT, describe which frame edge is closer to camera
- Always use the APPROVED sign image as image input, not the raw logo

---

## File Structure
```
BrasaRoja/
├── Assets/              # Official brand assets
│   ├── Logo_Full/
│   ├── Logo_Icon/
│   ├── Digital/
│   ├── Packaging/
│   ├── Apparel/
│   └── Stickers/
├── Clean Files/         # Clean logo versions
├── Vectors/             # SVG files
├── Mockups_v2/          # Product mockups
├── Mockups_v3/          # Fixed mockups
├── Sign_Concepts/       # Restaurant signage concepts
│   └── Round_Signs/     # Blade sign variations
├── Sign_6Views/         # 6 approved sign mockups (v4)
├── _Source/             # Reference images
├── BrasaRoja_Brand_Guidelines.pdf
├── CLAUDE.md            # This file
└── generate_*.py        # Generation scripts
```

---

## Quick Commands

### Generate new mockups:
```bash
python generate_mockups_v2.py
```

### Generate sign concepts:
```bash
python generate_signs.py
python generate_round_signs.py
```

---

*Last updated: February 2026*
