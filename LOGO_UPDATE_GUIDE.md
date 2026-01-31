# Brasa Roja - Actualización de Logos Limpios
## Lista Completa de Archivos a Actualizar

---

## ARCHIVOS DE LOGO LIMPIO (Fuente)

Usar estos archivos limpios (fondo transparente) en todos los deliverables:

```
Brand_Assets/Logo_Limpio/
├── Logo_Transparente_Limpio.png      # Logo principal - USAR ESTE
├── Logo_Alt_Transparente.png         # Alternativa
└── Variantes_Stickers/
    ├── Sticker_Fondo_Blanco.png
    ├── Sticker_Fondo_Negro.png
    ├── Sticker_Fondo_Crema.png
    ├── Sticker_Fondo_Rojo.png
    ├── Sticker_Fondo_Dorado.png
    └── Sticker_Fondo_Charcoal.png

Brand_Assets/Icono_Limpio/
├── Icono_Transparente_Limpio.png     # Icono principal - USAR ESTE
└── Variantes_Stickers/
    └── [mismas variantes de color]
```

---

## ARCHIVOS A ACTUALIZAR

### 1. Brand Guidelines (3 archivos)

| Archivo | Ruta | Cambios Necesarios |
|---------|------|-------------------|
| `BRASA_ROJA_Brand_Guidelines.md` | `/home/user/brasa-roja/` | Actualizar rutas de logo, agregar sección Logo Limpio |
| `BRASA_ROJA_Brand_Guidelines.html` | `/home/user/brasa-roja/` | Reemplazar imágenes con versiones limpias |
| `BrasaRoja_Brand_Guidelines.html` | `/home/user/brasa-roja/` | Reemplazar imágenes con versiones limpias |

### 2. Brand Package - Templates (7 archivos)

| Archivo | Ruta | Cambios |
|---------|------|---------|
| `00_README_Brand_Package_Index.html` | `Brand_Package/` | Actualizar índice con nuevos logos |
| `01_Business_Cards.html` | `Brand_Package/` | Reemplazar logo en tarjetas |
| `02_Email_Signature.html` | `Brand_Package/` | Reemplazar logo en firma |
| `03_Social_Media_Guidelines.html` | `Brand_Package/` | Actualizar guías con logos limpios |
| `04_Menu_Template_Print.html` | `Brand_Package/` | Reemplazar logo en menú |
| `05_TV_Digital_Menu_Board.html` | `Brand_Package/` | Reemplazar logo en pantalla TV |
| `06_Instagram_Templates.html` | `Brand_Package/` | Actualizar templates con logos limpios |

### 3. Otros Archivos (3 archivos)

| Archivo | Ruta | Cambios |
|---------|------|---------|
| `MASTER_INDEX.html` | `/home/user/brasa-roja/` | Agregar Logo_Limpio e Icono_Limpio al índice |
| `Website_Setup_Checklist.html` | `Deliverables/` | Actualizar rutas de favicon/logo |
| `README.md` | `/home/user/brasa-roja/` | Actualizar estructura y referencias |

---

## CAMBIOS ESPECÍFICOS POR ARCHIVO

### Business Cards (01_Business_Cards.html)
```html
<!-- ANTES -->
<img src="../Logo_MAIN_1.png" ...>

<!-- DESPUÉS -->
<img src="../Brand_Assets/Logo_Limpio/Logo_Transparente_Limpio.png" ...>
```

### Email Signature (02_Email_Signature.html)
```html
<!-- ANTES -->
<img src="Logo_MAIN_1.png" width="150" ...>

<!-- DESPUÉS -->
<img src="Brand_Assets/Logo_Limpio/Logo_Transparente_Limpio.png" width="150" ...>
```

### Menu Template (04_Menu_Template_Print.html)
```html
<!-- Header logo -->
<img src="../Brand_Assets/Logo_Limpio/Logo_Transparente_Limpio.png" class="logo">

<!-- Para fondo oscuro usar -->
<img src="../Brand_Assets/Logo_Limpio/Variantes_Stickers/Sticker_Fondo_Charcoal.png">
```

### TV Digital Menu (05_TV_Digital_Menu_Board.html)
```html
<!-- Logo principal en header -->
<img src="../Brand_Assets/Logo_Limpio/Logo_Transparente_Limpio.png" class="tv-logo">

<!-- Icono decorativo -->
<img src="../Brand_Assets/Icono_Limpio/Icono_Transparente_Limpio.png" class="flame-icon">
```

### Instagram Templates (06_Instagram_Templates.html)
```html
<!-- Feed posts (1080x1080) -->
<img src="../Brand_Assets/Logo_Limpio/Logo_Transparente_Limpio.png" class="ig-logo">

<!-- Stories (1080x1920) -->
<img src="../Brand_Assets/Icono_Limpio/Icono_Transparente_Limpio.png" class="story-icon">

<!-- Para fondos de color -->
Blanco: Sticker_Fondo_Blanco.png
Negro: Sticker_Fondo_Negro.png
Rojo marca: Sticker_Fondo_Rojo.png
```

### Social Media Guidelines (03_Social_Media_Guidelines.html)
```html
<!-- Agregar sección de assets -->
<h3>Logos para Redes Sociales</h3>
<ul>
  <li>Logo transparente: Logo_Limpio/Logo_Transparente_Limpio.png</li>
  <li>Icono para avatar: Icono_Limpio/Icono_Transparente_Limpio.png</li>
  <li>Stickers con fondo: Logo_Limpio/Variantes_Stickers/</li>
</ul>
```

---

## BRAND GUIDELINES - SECCIÓN A AGREGAR

```markdown
## Logos Limpios (Fondo Transparente)

### Para Impresión y Merchandising

| Uso | Archivo | Ubicación |
|-----|---------|-----------|
| Ropa (serigrafía) | Logo_Transparente_Limpio.png | Brand_Assets/Logo_Limpio/ |
| Bordado | Icono_Transparente_Limpio.png | Brand_Assets/Icono_Limpio/ |
| Stickers blancos | Sticker_Fondo_Blanco.png | Logo_Limpio/Variantes_Stickers/ |
| Stickers negros | Sticker_Fondo_Negro.png | Logo_Limpio/Variantes_Stickers/ |
| Papel kraft | Sticker_Fondo_Crema.png | Logo_Limpio/Variantes_Stickers/ |

### Especificaciones de Impresión

- **Serigrafía:** Usar Logo_Transparente_Limpio.png, separar colores
- **Vinilo:** Usar versión de 1 color (dorado o rojo)
- **Bordado:** Usar Icono simplificado, máx 3 colores
- **Transfer:** Usar Sticker_Fondo_Blanco.png sobre telas oscuras
```

---

## COLORES DE MARCA (Referencia)

| Color | Hex | Uso |
|-------|-----|-----|
| Brasa Gold | #C9882B | Texto "BRASA", swirl |
| Roja Red | #C63333 | Llama, texto "ROJA" |
| Deep Ember | #8B2500 | Profundidad |
| Charcoal | #2D2D2D | Fondos oscuros |
| Crema | #F5EFE0 | Fondos claros |

---

## CHECKLIST DE ACTUALIZACIÓN

- [ ] Brand_Assets/Logo_Limpio/ - Agregar archivos limpios
- [ ] Brand_Assets/Icono_Limpio/ - Agregar iconos limpios
- [ ] BRASA_ROJA_Brand_Guidelines.md - Actualizar
- [ ] BRASA_ROJA_Brand_Guidelines.html - Actualizar
- [ ] BrasaRoja_Brand_Guidelines.html - Actualizar
- [ ] 01_Business_Cards.html - Reemplazar logo
- [ ] 02_Email_Signature.html - Reemplazar logo
- [ ] 03_Social_Media_Guidelines.html - Agregar sección logos limpios
- [ ] 04_Menu_Template_Print.html - Reemplazar logo
- [ ] 05_TV_Digital_Menu_Board.html - Reemplazar logo e icono
- [ ] 06_Instagram_Templates.html - Actualizar todos los templates
- [ ] MASTER_INDEX.html - Agregar nuevas carpetas al índice
- [ ] Website_Setup_Checklist.html - Actualizar rutas
- [ ] README.md - Actualizar estructura

---

## RUTAS COMPLETAS DE ARCHIVOS

```
/home/user/brasa-roja/
├── BRASA_ROJA_Brand_Guidelines.md
├── BRASA_ROJA_Brand_Guidelines.html
├── BrasaRoja_Brand_Guidelines.html
├── MASTER_INDEX.html
├── README.md
│
├── Brand_Assets/
│   ├── Logo_Limpio/                    ← NUEVO
│   │   ├── Logo_Transparente_Limpio.png
│   │   └── Variantes_Stickers/
│   ├── Icono_Limpio/                   ← NUEVO
│   │   └── Icono_Transparente_Limpio.png
│   └── [carpetas existentes...]
│
├── Brand_Package/
│   ├── 00_README_Brand_Package_Index.html
│   ├── 01_Business_Cards.html
│   ├── 02_Email_Signature.html
│   ├── 03_Social_Media_Guidelines.html
│   ├── 04_Menu_Template_Print.html
│   ├── 05_TV_Digital_Menu_Board.html
│   └── 06_Instagram_Templates.html
│
└── Deliverables/
    └── Website_Setup_Checklist.html
```

---

*Documento generado para Brasa Roja - Enero 2026*
