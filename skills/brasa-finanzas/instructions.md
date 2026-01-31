# Skill: Brasa Finanzas
## Gestión Financiera y Facturación

---

## Descripción

Este skill gestiona toda la operación financiera del restaurante, incluyendo facturación electrónica AFIP, control de caja, reportes de ventas y análisis de rentabilidad.

---

## Facturación Electrónica Argentina

### Tipos de Comprobante

| Tipo | Emisor | Receptor | Uso |
|------|--------|----------|-----|
| **Factura A** | Resp. Inscripto | Resp. Inscripto | Empresas |
| **Factura B** | Resp. Inscripto | Consumidor Final / Monotributista | Particulares |
| **Factura C** | Monotributista | Cualquiera | Si aplica |
| **Ticket** | Con controlador fiscal | Consumidor Final | Consumos menores |

### Datos Requeridos

**Para Factura A:**
- Razón Social
- CUIT
- Domicilio fiscal
- Condición IVA

**Para Factura B:**
- Nombre (opcional para montos bajos)
- DNI/CUIL (opcional)

### IVA Aplicable

| Concepto | Alícuota |
|----------|----------|
| Alimentos y bebidas | 21% |
| Servicio de mesa | 21% |
| Propina | No aplica IVA |

---

## Control de Caja

### Apertura de Caja
```
APERTURA DE CAJA - BRASA ROJA
Fecha: [FECHA]
Turno: [ALMUERZO/CENA]
Responsable: [NOMBRE]

Fondo de caja inicial: $[MONTO]

Verificación:
- Billetes: $[DETALLE]
- Monedas: $[DETALLE]
- Total verificado: $[TOTAL]

Firma apertura: ________________
Hora: [HH:MM]
```

### Cierre de Caja
```
CIERRE DE CAJA - BRASA ROJA
Fecha: [FECHA]
Turno: [ALMUERZO/CENA]
Responsable: [NOMBRE]

INGRESOS:
| Medio | Monto |
|-------|-------|
| Efectivo | $[X] |
| Tarjeta Débito | $[X] |
| Tarjeta Crédito | $[X] |
| MercadoPago | $[X] |
| Transferencia | $[X] |
| **TOTAL** | **$[X]** |

EGRESOS:
| Concepto | Monto |
|----------|-------|
| Proveedores | $[X] |
| Gastos menores | $[X] |
| **TOTAL** | **$[X]** |

ARQUEO:
- Efectivo en caja: $[X]
- Diferencia: $[X]

Firma cierre: ________________
Hora: [HH:MM]
```

---

## Medios de Pago

### Configuración

| Medio | Comisión | Acreditación |
|-------|----------|--------------|
| Efectivo | 0% | Inmediato |
| Débito | 1.2% | 48h |
| Crédito 1 cuota | 3% | 18 días |
| Crédito 3 cuotas | 7% | 18 días |
| MercadoPago QR | 2.99% | 24h |
| Transferencia | 0% | Inmediato |

### Integración MercadoPago
```json
{
  "merchant_id": "[ID]",
  "pos_id": "[POS]",
  "qr_enabled": true,
  "link_pago": true,
  "cuotas_habilitadas": [1, 3, 6]
}
```

---

## Reportes de Ventas

### Reporte Diario
```
VENTAS DEL DÍA - [FECHA]

Turno Almuerzo:
- Mesas atendidas: [X]
- Comensales: [X]
- Venta total: $[X]
- Ticket promedio: $[X]

Turno Cena:
- Mesas atendidas: [X]
- Comensales: [X]
- Venta total: $[X]
- Ticket promedio: $[X]

TOTAL DÍA: $[X]
Comensales totales: [X]
Ticket promedio: $[X]
```

### Ventas por Categoría
```
VENTAS POR CATEGORÍA - [PERÍODO]

| Categoría | Cantidad | Monto | % Total |
|-----------|----------|-------|---------|
| Parrilla | [X] | $[X] | [X]% |
| Entradas | [X] | $[X] | [X]% |
| Acompañamientos | [X] | $[X] | [X]% |
| Postres | [X] | $[X] | [X]% |
| Bebidas | [X] | $[X] | [X]% |
| **TOTAL** | **[X]** | **$[X]** | **100%** |
```

### Top 10 Platos
```
PLATOS MÁS VENDIDOS - [PERÍODO]

1. Bife de chorizo - [X] unidades - $[X]
2. Asado de tira - [X] unidades - $[X]
3. Parrillada completa - [X] unidades - $[X]
...
```

---

## Análisis de Rentabilidad

### Por Plato
```
RENTABILIDAD POR PLATO

| Plato | Costo | Precio | Margen | Margen % |
|-------|-------|--------|--------|----------|
| Bife de chorizo | $7.740 | $14.500 | $6.760 | 47% |
| Vacío | $6.200 | $11.800 | $5.600 | 47% |
| Provoleta | $1.800 | $5.800 | $4.000 | 69% |
| Empanadas x3 | $1.200 | $4.500 | $3.300 | 73% |
```

### Métricas Clave

| Métrica | Objetivo | Actual |
|---------|----------|--------|
| Food Cost | <35% | [X]% |
| Margen Bruto | >60% | [X]% |
| Ticket Promedio | >$15.000 | $[X] |
| Mesas/Turno | >20 | [X] |

---

## Gestión de Propinas

### Política
- Propinas voluntarias (no incluidas en factura)
- Distribución: 70% mozos, 20% cocina, 10% limpieza
- Registro diario obligatorio

### Registro
```
PROPINAS DEL DÍA - [FECHA]

| Mozo | Efectivo | Digital | Total |
|------|----------|---------|-------|
| [Nombre 1] | $[X] | $[X] | $[X] |
| [Nombre 2] | $[X] | $[X] | $[X] |
| TOTAL | $[X] | $[X] | $[X] |

Distribución:
- Mozos (70%): $[X]
- Cocina (20%): $[X]
- Limpieza (10%): $[X]
```

---

## Obligaciones Fiscales

### Mensuales
- [ ] DDJJ IVA (vto: día 20)
- [ ] Ingresos Brutos (vto: día 15)
- [ ] SUSS/Cargas Sociales (vto: día 10)

### Anuales
- [ ] Ganancias (vto: junio)
- [ ] Bienes Personales (vto: junio)

### Controlador Fiscal
- Marca: [MARCA]
- Modelo: [MODELO]
- Número: [NÚMERO]
- Homologación AFIP: [CÓDIGO]

---

## Indicadores de Gestión

### Dashboard Financiero

```
═══════════════════════════════════════════
       BRASA ROJA - DASHBOARD FINANCIERO
               [MES/AÑO]
═══════════════════════════════════════════

VENTAS
├── Total mes: $[X]
├── vs mes anterior: [+/-X]%
└── Proyección: $[X]

COSTOS
├── Insumos: $[X] ([X]%)
├── Personal: $[X] ([X]%)
├── Servicios: $[X] ([X]%)
└── Otros: $[X] ([X]%)

RESULTADO
├── Margen bruto: $[X] ([X]%)
├── EBITDA: $[X] ([X]%)
└── Resultado neto: $[X] ([X]%)

═══════════════════════════════════════════
```

---

## Alertas Financieras

### Configuración
- Venta diaria < $[X] → Alerta amarilla
- Costo insumos > 40% → Alerta amarilla
- Diferencia caja > $5.000 → Alerta roja
- Ticket promedio < $10.000 → Alerta amarilla

---

*Skill desarrollado para Brasa Roja - Tradición Familiar*
*Cumplimiento normativa AFIP Argentina*
