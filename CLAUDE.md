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

### Color Palette
| Color | Hex | Use |
|-------|-----|-----|
| Primary Red | #E44D26 | Flame, accents |
| Deep Red | #C41E3A | "ROJA" text |
| Brasa Gold | #D4A84B | Swirl, "BRASA" text |
| Accent Red | #B02D37 | Secondary elements |
| Light Neutral | #F6F0E6 | Cream backgrounds |
| Charcoal | #2D2D2D | Dark backgrounds |

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
├── Sign_Concepts/       # Restaurant signage
│   └── Round_Signs/     # Blade sign variations
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
