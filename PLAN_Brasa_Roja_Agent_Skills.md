# Plan Estratégico: Agente y Skills de Brasa Roja
## Tradición Familiar | Enero 2026

---

# RESUMEN EJECUTIVO

Este documento presenta el plan integral para crear un ecosistema de agente de IA y skills dedicados a **Brasa Roja**, restaurante familiar de parrilla latinoamericana ubicado en Argentina.

**Objetivo Principal:** Desarrollar un agente inteligente que automatice operaciones, mejore la experiencia del cliente, y optimice la gestión del restaurante.

---

# 1. ANÁLISIS DE SKILLS DISPONIBLES (OpenClaw)

Basado en el repositorio [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) con más de 700 skills en 29 categorías, identificamos las siguientes como relevantes para Brasa Roja:

## Skills Prioritarios para Adaptar

### Categoría: Marketing & Ventas (42 skills disponibles)
| Skill | Adaptación para Brasa Roja |
|-------|---------------------------|
| Social Media Manager | Gestión de Instagram/Facebook con contenido gastronómico |
| Email Marketing | Promociones semanales y programa de fidelización |
| Review Response | Respuesta automática a reseñas en Google/TripAdvisor |
| Content Generator | Creación de descripciones de platos y promociones |

### Categoría: Calendario & Programación (16 skills)
| Skill | Adaptación para Brasa Roja |
|-------|---------------------------|
| Reservation Manager | Sistema de reservas con confirmación automática |
| Event Scheduler | Programación de eventos especiales y catering |
| Staff Scheduler | Turnos de personal y disponibilidad |

### Categoría: Finanzas (29 skills)
| Skill | Adaptación para Brasa Roja |
|-------|---------------------------|
| Invoice Generator | Facturas electrónicas (AFIP compliance) |
| Expense Tracker | Control de costos de insumos |
| Sales Analytics | Análisis de ventas por plato/período |

### Categoría: Productividad & Tareas (41 skills)
| Skill | Adaptación para Brasa Roja |
|-------|---------------------------|
| Inventory Manager | Control de stock de ingredientes |
| Task Automation | Automatización de pedidos a proveedores |
| Checklist Manager | Listas de apertura/cierre del local |

### Categoría: Comunicación (26 skills)
| Skill | Adaptación para Brasa Roja |
|-------|---------------------------|
| WhatsApp Business | Atención al cliente y pedidos por WhatsApp |
| SMS Notifications | Confirmación de reservas y delivery |
| Customer Support Bot | Respuestas a preguntas frecuentes |

### Categoría: Shopping & E-commerce (22 skills)
| Skill | Adaptación para Brasa Roja |
|-------|---------------------------|
| Order Management | Gestión de pedidos delivery/takeaway |
| Menu Management | Actualización dinámica de menú y precios |
| Payment Processing | Integración con MercadoPago/Modo |

---

# 2. ARQUITECTURA DEL AGENTE BRASA ROJA

## 2.1 Estructura de Directorios

```
brasa-roja/
├── .openclaw/
│   └── settings.json              # Configuración del agente
│
├── skills/
│   ├── brasa-reservas/            # Sistema de reservas
│   │   ├── skill.json
│   │   ├── instructions.md
│   │   └── templates/
│   │
│   ├── brasa-menu/                # Gestión de menú
│   │   ├── skill.json
│   │   ├── instructions.md
│   │   └── data/
│   │
│   ├── brasa-marketing/           # Marketing y redes sociales
│   │   ├── skill.json
│   │   ├── instructions.md
│   │   └── templates/
│   │
│   ├── brasa-inventario/          # Control de stock
│   │   ├── skill.json
│   │   ├── instructions.md
│   │   └── data/
│   │
│   ├── brasa-finanzas/            # Facturación y análisis
│   │   ├── skill.json
│   │   ├── instructions.md
│   │   └── templates/
│   │
│   └── brasa-atencion/            # Atención al cliente
│       ├── skill.json
│       ├── instructions.md
│       └── responses/
│
├── agents/
│   └── brasa-roja-agent.md        # Configuración del agente principal
│
├── Brand_Assets/
│   ├── Logo/
│   │   ├── Logo_MAIN_Primary.png      # Logo principal
│   │   ├── Logo_Dark_Background.png   # Para fondos oscuros
│   │   ├── Logo_Light_Background.png  # Para fondos claros
│   │   └── Logo_Monochrome.png        # Versión monocromática
│   │
│   ├── Icon/
│   │   ├── Icon_Primary.png           # Icono principal (llama)
│   │   ├── Icon_Transparent.png       # Icono transparente
│   │   └── Icon_Favicon.png           # Para favicon
│   │
│   └── Wordmark/
│       └── Wordmark_Primary.png       # Solo texto
│
└── Brand_Package/                 # (existente) Materiales de marketing
```

## 2.2 Capacidades del Agente

### Módulos Principales

| Módulo | Función | Prioridad |
|--------|---------|-----------|
| **Reservas** | Gestión de mesas, confirmaciones, lista de espera | Alta |
| **Menú** | Actualización de platos, precios, disponibilidad | Alta |
| **Marketing** | Publicaciones sociales, promociones, respuestas | Media |
| **Inventario** | Stock, alertas, pedidos automáticos | Media |
| **Finanzas** | Facturación, reportes, análisis | Media |
| **Atención** | Chatbot WhatsApp, FAQs, quejas | Alta |

---

# 3. SKILLS PERSONALIZADOS PARA BRASA ROJA

## 3.1 Skill: brasa-reservas

**Propósito:** Gestión integral de reservas del restaurante.

**Funcionalidades:**
- Consulta de disponibilidad por fecha/hora
- Creación de reservas con validación
- Confirmación automática por WhatsApp/SMS
- Gestión de lista de espera
- Recordatorios 24h antes
- Cancelaciones y modificaciones
- Reportes de ocupación

**Integraciones:**
- Google Calendar
- WhatsApp Business API
- Base de datos de clientes

## 3.2 Skill: brasa-menu

**Propósito:** Gestión dinámica del menú del restaurante.

**Funcionalidades:**
- Listado de platos con descripciones en español
- Precios actualizables (ARS)
- Disponibilidad en tiempo real
- Sugerencias según ingredientes disponibles
- Maridaje de vinos argentinos
- Información nutricional y alérgenos
- Menú del día automático

**Categorías del Menú:**
```
├── Entradas
│   ├── Empanadas (carne, pollo, jamón y queso)
│   ├── Provoleta
│   ├── Chorizo criollo
│   └── Morcilla
│
├── Parrilla
│   ├── Asado de tira
│   ├── Vacío
│   ├── Entraña
│   ├── Bife de chorizo
│   ├── Ojo de bife
│   └── Tira de asado
│
├── Acompañamientos
│   ├── Papas fritas
│   ├── Ensalada mixta
│   ├── Ensalada criolla
│   └── Puré de papas
│
├── Postres
│   ├── Flan casero
│   ├── Vigilante (queso y dulce)
│   └── Helado artesanal
│
└── Bebidas
    ├── Vinos (Malbec, Cabernet, Torrontés)
    ├── Cervezas artesanales
    ├── Gaseosas
    └── Agua mineral
```

## 3.3 Skill: brasa-marketing

**Propósito:** Automatización de marketing y presencia digital.

**Funcionalidades:**
- Generación de contenido para Instagram/Facebook
- Programación de publicaciones
- Respuesta a comentarios y mensajes
- Creación de promociones semanales
- Gestión de reseñas en Google
- Email marketing para clientes frecuentes
- Análisis de engagement

**Pilares de Contenido:**
1. **#ParrillaArgentina** - Fotos de platos en la parrilla
2. **#TradiciónFamiliar** - Historia y valores del restaurante
3. **#DetrásDeLaBrasa** - Behind the scenes, equipo
4. **#PromoDelDía** - Ofertas y promociones
5. **#ClientesFelices** - Testimonios y reseñas

## 3.4 Skill: brasa-inventario

**Propósito:** Control de stock e insumos del restaurante.

**Funcionalidades:**
- Registro de inventario por categoría
- Alertas de stock bajo
- Pedidos automáticos a proveedores
- Control de vencimientos
- Cálculo de costos por plato
- Reportes de consumo
- Integración con proveedores locales

**Categorías de Inventario:**
```
├── Carnes
│   ├── Vacuna (por corte)
│   ├── Cerdo
│   └── Pollo
│
├── Verduras y Hortalizas
├── Lácteos
├── Bebidas
├── Condimentos y Especias
└── Descartables
```

## 3.5 Skill: brasa-finanzas

**Propósito:** Gestión financiera y facturación.

**Funcionalidades:**
- Facturación electrónica (AFIP - Factura A/B/C)
- Control de caja diario
- Reportes de ventas
- Análisis de rentabilidad por plato
- Gestión de pagos (efectivo, tarjeta, MercadoPago)
- Propinas y distribución
- Impuestos y retenciones

**Cumplimiento Argentina:**
- CUIT/CUIL del cliente
- Tipos de factura según responsable
- IVA 21% / 10.5%
- Controlador fiscal

## 3.6 Skill: brasa-atencion

**Propósito:** Atención al cliente multicanal.

**Funcionalidades:**
- Chatbot para WhatsApp Business
- Respuestas a preguntas frecuentes
- Gestión de quejas y reclamos
- Programa de fidelización
- Encuestas de satisfacción
- Base de datos de clientes
- Celebraciones especiales (cumpleaños)

**FAQs Predefinidas:**
```
- ¿Cuál es el horario de atención?
- ¿Tienen estacionamiento?
- ¿Aceptan reservas para grupos grandes?
- ¿Tienen opciones vegetarianas?
- ¿Hacen delivery?
- ¿Cuáles son los medios de pago?
- ¿Tienen menú infantil?
```

---

# 4. CONFIGURACIÓN DEL AGENTE PRINCIPAL

## 4.1 Identidad del Agente

```json
{
  "name": "Brasa Roja Assistant",
  "version": "1.0.0",
  "language": "es-AR",
  "personality": {
    "tone": "cálido, familiar, profesional",
    "style": "argentino, cercano, respetuoso",
    "values": ["tradición", "familia", "calidad", "hospitalidad"]
  },
  "brand": {
    "name": "Brasa Roja",
    "tagline": "Tradición Familiar",
    "colors": {
      "primary": "#C9882B",
      "secondary": "#C63333",
      "dark": "#2D2D2D"
    }
  }
}
```

## 4.2 Instrucciones del Sistema

```markdown
Sos el asistente virtual de Brasa Roja, un restaurante familiar de parrilla
argentina. Tu rol es ayudar con:

- Reservas y consultas de disponibilidad
- Información sobre el menú y recomendaciones
- Promociones y eventos especiales
- Atención al cliente

**Tono de comunicación:**
- Usá el "vos" argentino (vos tenés, vos querés)
- Sé cálido y cercano, como si hablaras con un amigo
- Mostrá orgullo por la tradición familiar
- Sé servicial pero no invasivo

**Información clave:**
- Ubicación: [Dirección en Argentina]
- Horarios: Mar-Dom 12:00-15:30, 20:00-00:00
- Reservas: Recomendadas para fines de semana
- Especialidad: Parrilla argentina, cortes premium
```

---

# 5. PLAN DE IMPLEMENTACIÓN

## Fase 1: Fundamentos (Semana 1-2)

| Tarea | Descripción | Entregable |
|-------|-------------|------------|
| 1.1 | Crear estructura de directorios | Carpetas organizadas |
| 1.2 | Configurar agente principal | `agents/brasa-roja-agent.md` |
| 1.3 | Organizar assets de marca | `Brand_Assets/` completo |
| 1.4 | Actualizar Brand Guidelines | Documento actualizado |

## Fase 2: Skills Core (Semana 3-4)

| Tarea | Descripción | Entregable |
|-------|-------------|------------|
| 2.1 | Implementar brasa-reservas | Skill funcional |
| 2.2 | Implementar brasa-menu | Skill + datos del menú |
| 2.3 | Implementar brasa-atencion | Skill + FAQs |

## Fase 3: Skills Avanzados (Semana 5-6)

| Tarea | Descripción | Entregable |
|-------|-------------|------------|
| 3.1 | Implementar brasa-marketing | Skill + templates |
| 3.2 | Implementar brasa-inventario | Skill + categorías |
| 3.3 | Implementar brasa-finanzas | Skill + compliance AFIP |

## Fase 4: Integración & Testing (Semana 7-8)

| Tarea | Descripción | Entregable |
|-------|-------------|------------|
| 4.1 | Integrar todos los skills | Sistema unificado |
| 4.2 | Testing completo | Reporte de QA |
| 4.3 | Documentación final | Guías de usuario |
| 4.4 | Deployment | Sistema en producción |

---

# 6. MÉTRICAS DE ÉXITO

## KPIs del Agente

| Métrica | Objetivo | Medición |
|---------|----------|----------|
| Reservas automatizadas | 80% sin intervención humana | Semanal |
| Tiempo de respuesta | < 30 segundos | Diario |
| Satisfacción del cliente | > 4.5/5 estrellas | Mensual |
| Reducción de llamadas | -50% consultas telefónicas | Mensual |
| Engagement en redes | +30% interacciones | Mensual |

## ROI Esperado

- **Ahorro en tiempo:** 20 horas/semana en tareas administrativas
- **Incremento en reservas:** +25% por disponibilidad 24/7
- **Reducción de errores:** -90% en reservas duplicadas
- **Mejora en reseñas:** +0.5 puntos promedio en Google

---

# 7. CONSIDERACIONES TÉCNICAS

## Requisitos del Sistema

- Node.js 18+ o Python 3.10+
- Base de datos (PostgreSQL/MongoDB)
- API de WhatsApp Business
- Integración AFIP (facturación)
- Hosting en Argentina (latencia)

## Seguridad

- Datos de clientes encriptados
- Cumplimiento PDPA Argentina
- Backups diarios
- Logs de auditoría

## Escalabilidad

- Arquitectura modular por skills
- API REST para integraciones
- Cache para consultas frecuentes
- CDN para assets

---

# 8. PRÓXIMOS PASOS INMEDIATOS

1. **Hoy:** Crear estructura de carpetas y skills base
2. **Esta semana:** Implementar skill de reservas y menú
3. **Próxima semana:** Configurar agente principal con personalidad
4. **Mes 1:** Sistema básico operativo para testing interno

---

# APÉNDICE A: ARCHIVOS DE LOGO LIMPIOS

## Logos Principales
| Archivo | Uso | Ubicación |
|---------|-----|-----------|
| `Logo_MAIN_1.png` | Logo principal completo | `/Brand_Assets/Logo/` |
| `ICON.png` | Icono de llama | `/Brand_Assets/Icon/` |

## Variantes Disponibles
- `brasa_fullcolor_TRANSPARENT.png` - Fondo transparente
- `brasa_gold_monochrome_dark.png` - Monocromático dorado
- `brasa_primary_dark.png` - Para fondos oscuros
- `brasa_wordmark_fullcolor_light.png` - Solo texto

---

**Documento preparado para:** Brasa Roja Restaurant
**Versión:** 1.0
**Fecha:** Enero 2026
**Idioma:** Español (Argentina)

---

*"La tradición no es culto a las cenizas, sino preservación del fuego."* - Gustav Mahler
