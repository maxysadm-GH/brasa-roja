# Design & Mockup Tools Setup Guide

## MCP Servers for Design Work

### Figma MCP Server (Recommended)
Connect Claude Code directly to Figma for AI-assisted design.

**Setup for Claude Desktop:**
Add to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "figma": {
      "command": "npx",
      "args": ["-y", "@anthropic/figma-mcp-server"]
    }
  }
}
```

**For Claude Code CLI:**
```bash
claude mcp add --transport http figma https://mcp.figma.com/mcp
```

**Capabilities:**
- Pull design tokens from Figma
- Generate code matching Figma mockups
- Create UI components via natural language

### Canva Dev MCP Server
```json
{
  "mcpServers": {
    "canva": {
      "command": "npx",
      "args": ["-y", "@canva/mcp-server"]
    }
  }
}
```

---

## Free Mockup Generators

### 1. Mockey.ai (Best Free Option)
- **URL:** https://mockey.ai/
- **Templates:** 15,000+ across 45 categories
- **Cost:** FREE, no watermarks
- **Export:** JPG/PNG, 3 downloads/day free
- **Categories:** Apparel, packaging, mugs, bags, tech

### 2. Recraft AI
- **URL:** https://www.recraft.ai/mockup-generator
- **Cost:** 30 free generations/day
- **Features:** AI-powered, text prompts, hi-res export
- **API:** Available for automation

### 3. Mediamodifier
- **URL:** https://mediamodifier.com/mockups/all
- **Cost:** 100 free API calls
- **Templates:** Thousands available
- **API Docs:** https://mediamodifier.com/mockup-api

### 4. Dynamic Mockups (API-First)
- **URL:** https://dynamicmockups.com/
- **Best for:** Bulk generation, Shopify/Etsy integration
- **API Key:** Free to start

---

## Free Vector Resources

### Restaurant/Food Mockups
| Source | URL | License |
|--------|-----|---------|
| Freepik | freepik.com/free-photos-vectors/mockup-restaurant | Free with attribution |
| Vecteezy | vecteezy.com/free-vector/restaurant-mockup | Royalty-free |
| Vexels | vexels.com/free-vectors/restaurant/ | Commercial license |

### Menu Templates
- Vecteezy: 18,000+ menu mockup vectors
- Vexels: Menu vectors in AI, SVG, JPG, PNG

---

## Recommended Workflow

### For Quick Mockups:
1. Go to **mockey.ai**
2. Upload `Assets/Logo_Full/Logo_Transparent.png`
3. Search for product type (mug, t-shirt, bag, etc.)
4. Download high-res mockup

### For Professional Branding:
1. Set up **Figma MCP Server**
2. Create designs in Figma
3. Use Claude Code to generate production assets
4. Export to Assets/ folder

### For Bulk Generation:
1. Use **Dynamic Mockups API** or **Mediamodifier API**
2. Automate mockup creation for catalog
3. Integrate with e-commerce platform

---

## Logo Files for Mockups

Use these files when generating mockups:

| Use Case | File Path |
|----------|-----------|
| Full branding | `Assets/Logo_Full/Logo_Transparent.png` |
| Icon/avatar | `Assets/Logo_Icon/Icon_Transparent.png` |
| On dark backgrounds | `Assets/Logo_Full/Logo_Transparent.png` |
| For embroidery | `Assets/Apparel/Light_Garment/Logo_3.5in.png` |
| For packaging | `Assets/Packaging/Logo_CMYK_300dpi.png` |

---

## Next Steps

1. **Try Mockey.ai** - Upload logo, generate 3 free mockups today
2. **Set up Figma MCP** - For ongoing design work
3. **Download vectors** - From Freepik/Vecteezy for templates
4. **Explore API options** - If you need bulk mockup generation
