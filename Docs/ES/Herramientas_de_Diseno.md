# Guía de Configuración de Herramientas de Diseño y Mockups

## Servidores MCP para Trabajo de Diseño

### Servidor MCP de Figma (Recomendado)
Conectá Claude Code directamente a Figma para diseño asistido por IA.

**Configuración para Claude Desktop:**
Agregá a tu `claude_desktop_config.json`:
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

**Para Claude Code CLI:**
```bash
claude mcp add --transport http figma https://mcp.figma.com/mcp
```

**Capacidades:**
- Extraer tokens de diseño desde Figma
- Generar código que coincida con mockups de Figma
- Crear componentes de UI mediante lenguaje natural

### Servidor MCP de Canva Dev
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

## Generadores de Mockups Gratuitos

### 1. Mockey.ai (Mejor Opción Gratuita)
- **URL:** https://mockey.ai/
- **Plantillas:** 15.000+ en 45 categorías
- **Costo:** GRATIS, sin marcas de agua
- **Exportación:** JPG/PNG, 3 descargas/día gratis
- **Categorías:** Ropa, empaque, tazas, bolsas, tecnología

### 2. Recraft AI
- **URL:** https://www.recraft.ai/mockup-generator
- **Costo:** 30 generaciones gratis/día
- **Características:** Impulsado por IA, prompts de texto, exportación en alta resolución
- **API:** Disponible para automatización

### 3. Mediamodifier
- **URL:** https://mediamodifier.com/mockups/all
- **Costo:** 100 llamadas API gratuitas
- **Plantillas:** Miles disponibles
- **Documentación API:** https://mediamodifier.com/mockup-api

### 4. Dynamic Mockups (Enfocado en API)
- **URL:** https://dynamicmockups.com/
- **Ideal para:** Generación masiva, integración con Shopify/Etsy
- **Clave API:** Gratis para empezar

---

## Recursos de Vectores Gratuitos

### Mockups de Restaurante/Comida
| Fuente | URL | Licencia |
|--------|-----|----------|
| Freepik | freepik.com/free-photos-vectors/mockup-restaurant | Gratis con atribución |
| Vecteezy | vecteezy.com/free-vector/restaurant-mockup | Libre de regalías |
| Vexels | vexels.com/free-vectors/restaurant/ | Licencia comercial |

### Plantillas de Menú
- Vecteezy: 18.000+ vectores de mockup de menú
- Vexels: Vectores de menú en AI, SVG, JPG, PNG

---

## Flujo de Trabajo Recomendado

### Para Mockups Rápidos:
1. Andá a **mockey.ai**
2. Subí `Assets/Logo_Full/Logo_Transparent.png`
3. Buscá el tipo de producto (taza, remera, bolsa, etc.)
4. Descargá el mockup en alta resolución

### Para Branding Profesional:
1. Configurá el **Servidor MCP de Figma**
2. Creá diseños en Figma
3. Usá Claude Code para generar assets de producción
4. Exportá a la carpeta Assets/

### Para Generación Masiva:
1. Usá **Dynamic Mockups API** o **Mediamodifier API**
2. Automatizá la creación de mockups para catálogo
3. Integrá con plataforma de e-commerce

---

## Archivos de Logo para Mockups

Usá estos archivos cuando generes mockups:

| Uso | Ruta del Archivo |
|-----|------------------|
| Branding completo | `Assets/Logo_Full/Logo_Transparent.png` |
| Ícono/avatar | `Assets/Logo_Icon/Icon_Transparent.png` |
| Sobre fondos oscuros | `Assets/Logo_Full/Logo_Transparent.png` |
| Para bordado | `Assets/Apparel/Light_Garment/Logo_3.5in.png` |
| Para empaque | `Assets/Packaging/Logo_CMYK_300dpi.png` |

---

## Próximos Pasos

1. **Probá Mockey.ai** - Subí el logo, generá 3 mockups gratis hoy
2. **Configurá Figma MCP** - Para trabajo de diseño continuo
3. **Descargá vectores** - De Freepik/Vecteezy para plantillas
4. **Explorá opciones de API** - Si necesitás generación masiva de mockups
