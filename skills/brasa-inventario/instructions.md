# Skill: Brasa Inventario
## Control de Stock e Insumos

---

## Descripción

Este skill gestiona el inventario completo del restaurante, incluyendo carnes, bebidas, verduras y todos los insumos necesarios para la operación.

---

## Categorías de Inventario

### 1. CARNES (Frescos - Cadena de Frío)

| Producto | Stock Mínimo | Stock Óptimo | Unidad | Proveedor |
|----------|--------------|--------------|--------|-----------|
| Asado de tira | 15 kg | 40 kg | kg | Frigorífico [X] |
| Vacío | 12 kg | 30 kg | kg | Frigorífico [X] |
| Entraña | 8 kg | 20 kg | kg | Frigorífico [X] |
| Bife de chorizo | 10 kg | 25 kg | kg | Frigorífico [X] |
| Ojo de bife | 8 kg | 20 kg | kg | Frigorífico [X] |
| Lomo | 6 kg | 15 kg | kg | Frigorífico [X] |
| Chorizo | 10 kg | 25 kg | kg | Frigorífico [X] |
| Morcilla | 5 kg | 12 kg | kg | Frigorífico [X] |
| Pollo | 8 kg | 20 kg | kg | Avícola [Y] |
| Bondiola cerdo | 6 kg | 15 kg | kg | Frigorífico [X] |

### 2. LÁCTEOS

| Producto | Stock Mínimo | Stock Óptimo | Unidad | Vencimiento |
|----------|--------------|--------------|--------|-------------|
| Provolone | 5 kg | 12 kg | kg | 15 días |
| Crema | 3 L | 8 L | litros | 7 días |
| Manteca | 2 kg | 5 kg | kg | 30 días |
| Queso rallado | 2 kg | 5 kg | kg | 30 días |

### 3. VERDURAS Y HORTALIZAS

| Producto | Stock Mínimo | Stock Óptimo | Unidad | Frecuencia |
|----------|--------------|--------------|--------|------------|
| Papa | 20 kg | 50 kg | kg | 2x semana |
| Lechuga | 3 kg | 8 kg | kg | 3x semana |
| Tomate | 5 kg | 15 kg | kg | 3x semana |
| Cebolla | 5 kg | 15 kg | kg | 1x semana |
| Morrón | 3 kg | 8 kg | kg | 2x semana |
| Limón | 2 kg | 5 kg | kg | 2x semana |
| Zapallo | 3 kg | 8 kg | kg | 1x semana |
| Berenjena | 2 kg | 5 kg | kg | 2x semana |

### 4. BEBIDAS

| Producto | Stock Mínimo | Stock Óptimo | Unidad |
|----------|--------------|--------------|--------|
| Vino Malbec (botellas) | 24 | 60 | unid |
| Vino Cabernet (botellas) | 12 | 30 | unid |
| Vino Torrontés (botellas) | 12 | 24 | unid |
| Cerveza Quilmes | 48 | 120 | unid |
| Cerveza artesanal | 24 | 60 | unid |
| Coca-Cola (1.5L) | 24 | 60 | unid |
| Agua mineral (500ml) | 48 | 120 | unid |
| Fernet | 6 | 12 | unid |

### 5. CONDIMENTOS Y ESPECIAS

| Producto | Stock Mínimo | Stock Óptimo | Unidad |
|----------|--------------|--------------|--------|
| Sal gruesa | 5 kg | 15 kg | kg |
| Pimienta | 500 g | 1.5 kg | g |
| Orégano | 300 g | 1 kg | g |
| Chimichurri (preparado) | 3 L | 8 L | litros |
| Aceite de oliva | 5 L | 15 L | litros |
| Vinagre | 2 L | 5 L | litros |
| Ajo | 1 kg | 3 kg | kg |
| Perejil | 500 g | 1.5 kg | g |

### 6. DESCARTABLES

| Producto | Stock Mínimo | Stock Óptimo | Unidad |
|----------|--------------|--------------|--------|
| Servilletas (paquetes) | 20 | 50 | paq |
| Bolsas take-away | 50 | 150 | unid |
| Contenedores aluminio | 50 | 150 | unid |
| Rollos cocina | 12 | 30 | unid |
| Bolsas residuos | 30 | 80 | unid |

---

## Alertas Automáticas

### Alerta de Stock Bajo
```
⚠️ ALERTA DE STOCK BAJO

Producto: [NOMBRE]
Stock actual: [CANTIDAD] [UNIDAD]
Stock mínimo: [MÍNIMO] [UNIDAD]
Proveedor: [NOMBRE]

Acción recomendada: Realizar pedido de [CANTIDAD SUGERIDA]

¿Generamos la orden de compra?
```

### Alerta de Vencimiento
```
⚠️ PRODUCTO POR VENCER

Producto: [NOMBRE]
Cantidad: [CANTIDAD]
Vencimiento: [FECHA] ([X] días)

Sugerencia: Priorizar uso en menú del día
```

---

## Cálculo de Costos por Plato

### Ejemplo: Bife de Chorizo

| Ingrediente | Cantidad | Costo/Unidad | Subtotal |
|-------------|----------|--------------|----------|
| Bife de chorizo | 400 g | $18.000/kg | $7.200 |
| Papas fritas | 150 g | $2.000/kg | $300 |
| Ensalada | 100 g | $1.500/kg | $150 |
| Chimichurri | 30 ml | $3.000/L | $90 |
| **COSTO TOTAL** | | | **$7.740** |
| Precio venta | | | $14.500 |
| **Margen bruto** | | | **47%** |

---

## Gestión de Proveedores

### Proveedores Registrados

| Proveedor | Categoría | Contacto | Días de entrega |
|-----------|-----------|----------|-----------------|
| Frigorífico [X] | Carnes | [Tel] | Lun, Mié, Vie |
| Avícola [Y] | Pollo | [Tel] | Mar, Jue |
| Verdulería [Z] | Verduras | [Tel] | Diario |
| Distribuidora [W] | Bebidas | [Tel] | Mar, Vie |
| Especias [V] | Condimentos | [Tel] | Mié |

### Template de Pedido
```
ORDEN DE COMPRA - BRASA ROJA
Fecha: [FECHA]
Proveedor: [NOMBRE]

| Producto | Cantidad | Precio Est. |
|----------|----------|-------------|
| [...]    | [...]    | [...]       |

Total estimado: $[TOTAL]
Fecha entrega: [FECHA]
Contacto: [NOMBRE] - [TELÉFONO]

Firma: ________________
```

---

## Reportes Disponibles

1. **Stock actual:** Estado de todo el inventario
2. **Consumo semanal:** Productos más usados
3. **Costos del mes:** Total gastado en insumos
4. **Rotación:** Velocidad de salida por producto
5. **Merma:** Productos vencidos o desperdiciados
6. **Comparativo:** Mes actual vs. anterior

---

## Checklist Diario

### Apertura
- [ ] Verificar temperaturas de heladera/freezer
- [ ] Revisar productos por vencer hoy
- [ ] Confirmar entregas del día
- [ ] Descongelar carnes necesarias

### Cierre
- [ ] Registrar consumo del día
- [ ] Guardar productos correctamente
- [ ] Preparar lista de pedidos para mañana
- [ ] Limpiar y organizar depósito

---

*Skill desarrollado para Brasa Roja - Tradición Familiar*
