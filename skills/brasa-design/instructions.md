# Skill: Brasa Design
## Procesamiento de Assets de Marca

---

## Descripción

Este skill maneja todo el procesamiento de imágenes y assets visuales de Brasa Roja:
- Remoción de fondos para logos e iconos
- Creación de variantes de color
- Preparación para impresión (ropa, stickers, merchandising)
- Gestión de assets de marca

---

## Configuración Rápida

### 1. Obtener API Key de Remove.bg (Gratis)

1. Ir a: https://www.remove.bg/api
2. Crear cuenta gratuita
3. Copiar tu API Key

### 2. Configurar API Key

Crear archivo `.env` en la raíz del proyecto:

```bash
REMOVEBG_API_KEY=tu_api_key_aqui
```

### 3. Instalar Dependencias

```bash
pip install requests python-dotenv Pillow
```

### 4. Ejecutar Script

```bash
cd /home/user/brasa-roja
python skills/brasa-design/scripts/remove_background.py
```

---

## Archivos que se Procesan

| Archivo Original | Resultado | Uso |
|------------------|-----------|-----|
| `Logo_MAIN_1.png` | `Logo_Transparente_Limpio.png` | Impresión general |
| `BR_Main_1.png` | `Logo_Alt_Transparente.png` | Alternativa |
| `BR_LOGO_1.png` | `Logo_Premium_Transparente.png` | Uso premium |
| `ICON.png` | `Icono_Transparente_Limpio.png` | Favicon, apps |
| `ICON_2.png` | `Icono_Variante_Transparente.png` | Variante |
| `brasa_primary_dark.png` | `Logo_Dark_Transparente.png` | Fondos claros |

---

## Estructura de Salida

Después de ejecutar el script:

```
Brand_Assets/
├── Logo_Limpio/
│   ├── Logo_Transparente_Limpio.png      # ⭐ Principal
│   ├── Logo_Alt_Transparente.png
│   ├── Logo_Premium_Transparente.png
│   ├── Logo_Dark_Transparente.png
│   └── Variantes_Color/
│       ├── Logo_Fondo_Blanco.png         # Para impresión
│       ├── Logo_Fondo_Negro.png          # Stickers oscuros
│       ├── Logo_Fondo_Crema.png          # Papel kraft
│       ├── Logo_Fondo_Rojo.png           # Merchandising
│       ├── Logo_Fondo_Dorado.png         # Premium
│       └── Logo_Fondo_Charcoal.png       # Elegante
│
└── Icono_Limpio/
    ├── Icono_Transparente_Limpio.png     # ⭐ Principal
    └── Icono_Variante_Transparente.png
```

---

## Uso de Logos Limpios

### Para Ropa (Serigrafía/Bordado)
- Usar: `Logo_Transparente_Limpio.png`
- Formato: PNG con transparencia
- Resolución: Original (alta calidad)

### Para Stickers
- Fondo blanco: `Variantes_Color/Logo_Fondo_Blanco.png`
- Fondo transparente: `Logo_Transparente_Limpio.png`
- Con borde: Agregar contorno en software de diseño

### Para Merchandising
- Tazas claras: `Logo_Transparente_Limpio.png`
- Tazas oscuras: `Logo_Fondo_Blanco.png` o logo en colores claros

### Para Web/Digital
- Favicon: `Icono_Transparente_Limpio.png` (redimensionar a 32x32, 180x180)
- Avatar redes: `Icono_Transparente_Limpio.png`

---

## API Remove.bg - Información

### Límites del Plan Gratuito
- 50 llamadas/mes
- Resolución estándar (0.25 megapixels)
- Suficiente para procesar todos los logos

### Planes Pagos (si necesitás más)
- $9/mes: 40 créditos HD
- $39/mes: 200 créditos HD
- Enterprise: Volumen ilimitado

### Documentación
- API Docs: https://www.remove.bg/api
- Ejemplos: https://www.remove.bg/api#sample-code

---

## Colores de Marca para Variantes

| Color | Hex | RGB | Uso |
|-------|-----|-----|-----|
| Blanco | `#FFFFFF` | 255, 255, 255 | Impresión general |
| Negro | `#000000` | 0, 0, 0 | Stickers premium |
| Crema | `#F5EFE0` | 245, 239, 224 | Papel kraft, eco |
| Rojo (Roja) | `#C63333` | 198, 51, 51 | Merchandising destacado |
| Dorado (Brasa) | `#C9882B` | 201, 136, 43 | Premium, elegante |
| Charcoal | `#2D2D2D` | 45, 45, 45 | Fondos oscuros |

---

## Troubleshooting

### "REMOVEBG_API_KEY no encontrada"
```bash
# Verificar que .env existe
cat .env

# Verificar que tiene la key
grep REMOVEBG .env
```

### "Error: Could not remove background"
- Verificar que la imagen tiene suficiente contraste
- Probar con imagen de mayor resolución

### "Error 402: Insufficient credits"
- Se acabaron los 50 créditos gratuitos
- Opciones: esperar al próximo mes o comprar créditos

---

## Integración con Otros Skills

### brasa-marketing
Usa los logos limpios para crear contenido de redes sociales.

### brasa-menu
Usa el icono para headers y decoración del menú.

### brasa-atencion
Usa el logo para firmas de email y respuestas automáticas.

---

*Skill desarrollado para Brasa Roja - Tradición Familiar*
