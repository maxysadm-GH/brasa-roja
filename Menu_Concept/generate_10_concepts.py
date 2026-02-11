# -*- coding: utf-8 -*-
"""
Brasa Roja - Generate 10 Menu Concept HTML files
Each is a self-contained, print-ready visual concept with embedded logo.
"""
import sys, json
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

OUT = Path(r"G:\My Drive\Projects\Brasa Roja\Menu Concept")

# Load base64 assets
with open(OUT / "_assets.json") as f:
    assets = json.load(f)
LOGO_B64 = assets["logo"]
ICON_B64 = assets["icon"]

LOGO_SRC = f"data:image/png;base64,{LOGO_B64}"
ICON_SRC = f"data:image/png;base64,{ICON_B64}"

# ============================================================
# SHARED: Brand Config
# ============================================================
BRAND = {
    "gold": "#C9882B",
    "red": "#C63333",
    "deep": "#8B2500",
    "charcoal": "#2D2D2D",
    "cream": "#F5EFE0",
    "smoke": "#8B7355",
    "dark": "#1a1a1a",
}

FONTS = "https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700&family=Lora:ital,wght@0,400;0,500;0,600;1,400&family=Parisienne&display=swap"

LEGEND = """<div class="legend">
<span class="sym sym-v">V</span> Vegetariano &nbsp;
<span class="sym sym-vg">VG</span> Vegano &nbsp;
<span class="sym sym-sg">SG</span> Sin Gluten &nbsp;
<span class="sym sym-sl">SL</span> Sin Lactosa &nbsp;
<span class="sym sym-rec">★</span> Recomendado &nbsp;
<span class="sym sym-pic">🌶</span> Picante
<br><em>Informanos sobre alergias o restricciones alimentarias. Consultá a tu mozo.</em>
</div>"""

SYM_CSS = """
.sym { display:inline-block; padding:1px 5px; border-radius:8px; font-size:9px; font-weight:700; margin-right:2px; }
.sym-v { background:#2d6b2d; color:white; }
.sym-vg { background:#1a8a1a; color:white; }
.sym-sg { background:#C9882B; color:#1a1a1a; }
.sym-sl { background:#444; color:#C9882B; }
.sym-rec { background:#8B2500; color:white; }
.sym-pic { background:transparent; }
"""


# ============================================================
# MENU DATA (normalized, optimized flow)
# ============================================================

def sym(codes):
    """Generate symbol HTML from codes like 'v sg rec'"""
    m = {
        'v': '<span class="sym sym-v">V</span>',
        'vg': '<span class="sym sym-vg">VG</span>',
        'sg': '<span class="sym sym-sg">SG</span>',
        'sl': '<span class="sym sym-sl">SL</span>',
        'rec': '<span class="sym sym-rec">★</span>',
        'pic': '<span class="sym sym-pic">🌶</span>',
    }
    if not codes:
        return ""
    return " ".join(m.get(c, "") for c in codes.split())


MENU = {
    "combos": {
        "title": "COMBO DEPORTIVO",
        "icon": "⚡",
        "items": [
            ("Combo Milanesa", "Milanesa de pollo + guarnicion + agua | ~850 kcal", "25.000", ""),
            ("Combo Pasta", "Tallarines con salsa a eleccion + agua | ~650 kcal", "20.000", ""),
        ]
    },
    "sandwiches": {
        "title": "SANDWICHES Y HAMBURGUESAS",
        "icon": "🥪",
        "items": [
            ("Sandwich de Colita de Cuadril", "Colita a la parrilla en pan artesanal | ~620 kcal", "12.500", "sg rec"),
            ("Sandwich de Bondiola", "Bondiola braseada, pan artesanal | ~580 kcal", "11.500", ""),
            ("Sandwich de Milanesa de Pollo", "Milanesa casera de pollo en pan | ~550 kcal", "9.500", ""),
            ("Sandwich de J&Q (Arabe)", "Pan arabe, jamon cocido, queso | ~420 kcal", "9.000", ""),
            ("Sandwich de J&Q (Pebete)", "Pan pebete, jamon cocido, queso | ~400 kcal", "8.000", ""),
            ("Sandwich de J&Q (Frances)", "Pan frances tostado, jamon, queso | ~380 kcal", "7.500", ""),
            ("Choripan", "Chorizo criollo en pan frances, chimichurri | ~450 kcal", "7.500", "rec"),
            ("Hamburguesa Clasica", "Medallon de carne 200g en pan de papa | ~520 kcal", "6.500", ""),
        ]
    },
    "platos": {
        "title": "NUESTROS PLATOS",
        "icon": "🔥",
        "items": [
            ("Colita de Cuadril", "A la parrilla, corte premium | ~480 kcal", "22.000", "sg rec"),
            ("Bondiola", "Braseada lenta, tierna y jugosa | ~520 kcal", "22.000", "sg"),
            ("Milanesa Napolitana (Carne)", "Con salsa, jamon y queso gratinado | ~780 kcal", "22.000", ""),
            ("Milanesa Napolitana (Pollo)", "Suprema napo con salsa, jamon y queso | ~720 kcal", "22.000", ""),
            ("Milanesa de Carne", "Milanesa casera de nalga, empanada a mano | ~580 kcal", "18.000", ""),
            ("Milanesa de Pollo", "Suprema de pollo empanada casera | ~520 kcal", "18.000", ""),
            ("Pollo Grille", "Pechuga a la plancha con hierbas | ~350 kcal", "18.000", "sg"),
        ]
    },
    "pastas": {
        "title": "PASTAS CASERAS",
        "icon": "🍝",
        "items": [
            ("Sorrentinos de Jamon y Queso", "Masa casera rellena | ~620 kcal", "19.000", ""),
            ("Ravioles de Verdura", "Masa casera, verdura y ricota | ~480 kcal", "19.000", "v"),
            ("Noquis de Papa", "Noquis caseros de papa | ~420 kcal", "15.000", "v"),
            ("Tallarines al Huevo", "Tallarines caseros al huevo | ~450 kcal", "15.000", "v"),
        ],
        "note": "Salsas: Fileto 2.500 (+80 kcal) | Crema 3.000 (+150 kcal) | Mixta 5.000 (+120 kcal) | 4 Quesos 6.500 (+250 kcal) | Bolognesa 6.500 (+180 kcal)"
    },
    "ensaladas": {
        "title": "ENSALADAS",
        "icon": "🥗",
        "items": [
            ("Gourmet", "3 verduras, huevo, choclo, aderezo de la casa | ~320 kcal", "15.000", "v sg"),
            ("Mediterranea", "3 verduras, atun, aceitunas negras | ~280 kcal", "14.000", "sg"),
            ("Campestre", "Mix de 3 verduras de estacion con parmesano | ~250 kcal", "13.000", "v sg"),
            ("Rucula con Parmesano", "Rucula fresca, lascas de parmesano, oliva | ~220 kcal", "12.000", "v"),
        ]
    },
    "guarniciones": {
        "title": "GUARNICIONES",
        "icon": "🍟",
        "items": [
            ("Papas Fritas", "Porcion abundante | ~380 kcal", "7.000", "sg"),
            ("Pure de Papas", "Casero, cremoso | ~250 kcal", "6.000", "v sg"),
            ("Huevo Frito (c/u)", "A la plancha | ~90 kcal", "2.500", "v sg"),
        ]
    },
    "postres": {
        "title": "POSTRES",
        "icon": "🍮",
        "items": [
            ("Panqueques de Dulce de Leche", "Panqueques caseros, dulce de leche | ~420 kcal", "9.500", "v"),
            ("Queso y Dulce", "Queso fresco con dulce de batata o membrillo | ~350 kcal", "8.000", "v sg"),
            ("Postre Helado", "Bomba helada del dia | ~280 kcal", "8.000", "v"),
        ]
    },
    "sin_alcohol": {
        "title": "SIN ALCOHOL",
        "icon": "💧",
        "items": [
            ("Gatorade", "Deportiva, sabores varios | ~130 kcal", "3.500", ""),
            ("Gaseosa", "Coca-Cola, Sprite, Fanta | ~140 kcal", "3.000", ""),
            ("Agua Saborizada", "Levite / Villa del Sur | ~80 kcal", "3.000", ""),
            ("Agua Mineral", "Con o sin gas, 500ml | 0 kcal", "2.500", ""),
        ]
    },
    "cervezas_vinos": {
        "title": "CERVEZAS Y VINOS",
        "icon": "🍺",
        "items": [
            ("Vino de la Casa", "Tinto o blanco, botella | ~600 kcal (botella)", "20.000", ""),
            ("Cerveza Litro", "Botella 1L | ~430 kcal", "12.000", ""),
            ("Cerveza Lata", "Lata 473ml | ~200 kcal", "5.500", ""),
        ]
    },
    "tragos": {
        "title": "TRAGOS Y COCTELES",
        "icon": "🍸",
        "items": [
            ("La Brasa ★", "Gin, pomelo rosado, romero y tonica | ~180 kcal", "18.000", "rec"),
            ("El Tercer Tiempo ★", "Fernet Branca, Coca-Cola, twist de limon | ~220 kcal", "14.000", "rec"),
            ("Scrum Sour", "Whisky, limon, azucar, clara de huevo | ~190 kcal", "17.000", ""),
            ("Try Line Spritz", "Aperol, espumante, soda, naranja | ~160 kcal", "17.000", ""),
            ("Gin Tonic Clasico", "Gin, tonica premium, botanicos | ~170 kcal", "16.000", ""),
            ("Campari con Naranja", "Campari, jugo de naranja, hielo | ~150 kcal", "16.000", ""),
            ("Fernet con Coca", "Fernet Branca, Coca-Cola, hielo | ~220 kcal", "14.000", ""),
            ("Whisky", "Medida simple, hielo | ~105 kcal", "10.000", ""),
        ],
        "note": "★ Cocteles de la casa, creados para Brasa Roja"
    },
    "cafeteria": {
        "title": "CAFETERIA",
        "icon": "☕",
        "items": [
            ("Cafe Espresso", "Espresso simple | ~5 kcal", "4.000", ""),
            ("Cafe en Jarrito", "Cafe doble en jarrito de ceramica | ~10 kcal", "5.000", ""),
            ("Cafe Doble", "Doble shot de espresso | ~10 kcal", "5.000", ""),
            ("Te", "Seleccion de saquitos | ~2 kcal", "4.500", ""),
            ("Submarino", "Leche caliente con barra de chocolate | ~250 kcal", "5.000", "v"),
            ("Medialuna", "Medialuna de manteca | ~180 kcal", "1.500", "v"),
            ("Medialuna de Jamon y Queso", "Rellena, tostada | ~280 kcal", "3.500", ""),
        ]
    },
}

FOOD_SECTIONS = ["combos", "sandwiches", "platos", "pastas", "ensaladas", "guarniciones"]
DRINK_SECTIONS = ["tragos", "cervezas_vinos", "sin_alcohol"]
DESSERT_SECTIONS = ["postres"]
CAFE_SECTIONS = ["cafeteria"]
ALL_FOOD = FOOD_SECTIONS + DESSERT_SECTIONS
ALL_DRINK = DRINK_SECTIONS + CAFE_SECTIONS


# ============================================================
# HTML HELPERS
# ============================================================

def html_head(title, extra_css=""):
    return f"""<!DOCTYPE html>
<html lang="es-AR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link href="{FONTS}" rel="stylesheet">
<style>
:root {{
    --gold: {BRAND['gold']};
    --red: {BRAND['red']};
    --deep: {BRAND['deep']};
    --charcoal: {BRAND['charcoal']};
    --cream: {BRAND['cream']};
    --smoke: {BRAND['smoke']};
    --dark: {BRAND['dark']};
}}
* {{ margin:0; padding:0; box-sizing:border-box; }}
{SYM_CSS}
{FOOTER_CSS}
.page-divider {{ display: block; }}
@media print {{ .page-divider {{ display: none; }} }}
{extra_css}
</style>
</head>
<body>
"""

def html_foot():
    return "</body>\n</html>"


def divider(label="✂ DA VUELTA ✂"):
    return f"""
<div class="page-divider" style="
    width:100%; max-width:11in; margin:0 auto; padding:20px 0; text-align:center; position:relative;
">
    <div style="position:absolute;top:50%;left:0;right:0;height:0;
        border-top:3px dashed #C9882B;"></div>
    <span style="
        position:relative; display:inline-block; background:#e0e0e0; padding:6px 30px;
        font-family:'Cinzel',serif; font-size:13px; letter-spacing:5px;
        color:#C9882B; font-weight:700; border:2px solid #C9882B; border-radius:4px;
    ">{label}</span>
</div>
"""


# ============================================================
# SHARED: Footer with locations, socials, phone, QR
# ============================================================
FOOTER_CSS = """
.footer-info { margin-top:10px; padding-top:8px; border-top:2px solid var(--gold); font-size:9px; text-align:center; line-height:1.6; }
.footer-info-light { color: var(--charcoal); }
.footer-info-dark { color: var(--cream); }
.fi-locations { display:flex; justify-content:center; gap:30px; margin-bottom:4px; flex-wrap:wrap; }
.fi-loc { font-size:8.5px; }
.fi-contact { margin-bottom:4px; font-size:9px; }
.fi-social { margin-bottom:6px; font-size:8px; letter-spacing:0.5px; }
.fi-social span { margin:0 4px; }
.fi-events { display:flex; align-items:center; justify-content:center; gap:10px; margin-top:4px; }
.fi-qr { width:52px; height:52px; background:white; border:1px solid #ccc; border-radius:6px; display:flex; align-items:center; justify-content:center; font-size:7px; color:#555; font-family:monospace; }
.fi-qr-text { text-align:left; font-size:9px; font-weight:600; }
.fi-qr-text small { font-size:7.5px; font-weight:400; }
"""


def footer_info(dark=True):
    cls = "footer-info-dark" if dark else "footer-info-light"
    smoke = "var(--smoke)" if dark else "var(--smoke)"
    return f"""<div class="footer-info {cls}">
<div class="fi-locations">
    <div class="fi-loc">📍 <strong>SEDE 1:</strong> [Direccion Sede 1, Ciudad]</div>
    <div class="fi-loc">📍 <strong>SEDE 2:</strong> [Direccion Sede 2, Ciudad]</div>
</div>
<div class="fi-contact">📞 <strong>[Telefono Principal]</strong></div>
<div class="fi-social" style="color:{smoke}">
    <span>📸 @brasaroja</span> · <span>📘 /brasaroja</span> · <span>𝕏 @brasaroja</span> · <span>🎵 @brasaroja</span>
</div>
<div class="fi-events">
    <div class="fi-qr">[QR]</div>
    <div class="fi-qr-text">Explora nuestros EVENTOS<br><small style="color:{smoke}">Cumpleanos · Casamientos · Corporativos</small></div>
</div>
</div>"""


def render_items_dark(sec_key, show_desc=True, show_icon=True):
    """Render a section's items for dark background menus"""
    sec = MENU[sec_key]
    icon = sec["icon"] + " " if show_icon else ""
    html = f'<div class="menu-section">\n'
    html += f'<h3 class="sec-title">{icon}{sec["title"]}</h3>\n'
    for name, desc, price, syms in sec["items"]:
        s = sym(syms)
        html += f'<div class="item"><div class="item-left"><span class="item-name">{name}</span>{" " + s if s else ""}'
        if show_desc:
            html += f'<span class="item-desc">{desc}</span>'
        html += f'</div><span class="item-price">{price}</span></div>\n'
    if "note" in sec:
        html += f'<div class="item-note">{sec["note"]}</div>\n'
    html += '</div>\n'
    return html


def render_items_light(sec_key, show_desc=True, show_icon=True):
    """Render a section's items for light/cream background menus"""
    sec = MENU[sec_key]
    icon = sec["icon"] + " " if show_icon else ""
    html = f'<div class="menu-section">\n'
    html += f'<h3 class="sec-title">{icon}{sec["title"]}</h3>\n'
    for name, desc, price, syms in sec["items"]:
        s = sym(syms)
        html += f'<div class="item"><div class="item-left"><span class="item-name">{name}</span>{" " + s if s else ""}'
        if show_desc:
            html += f'<span class="item-desc">{desc}</span>'
        html += f'</div><span class="item-price">{price}</span></div>\n'
    if "note" in sec:
        html += f'<div class="item-note">{sec["note"]}</div>\n'
    html += '</div>\n'
    return html


# ============================================================
# CONCEPT 01: EL CLASICO
# One page, single side, all food. Black bg. Logo on back.
# ============================================================
def concept_01():
    css = """
@page { size: 8.5in 11in; margin: 0; }
body { font-family: 'Lora', Georgia, serif; background: #e0e0e0; }
.page { width: 8.5in; min-height: 11in; margin: 10px auto; position: relative; overflow: hidden; }
.page-front { background: var(--charcoal); color: var(--cream); padding: 0.35in; }
.page-back { background: var(--dark); display: flex; align-items: center; justify-content: center; }
.header { text-align: center; padding: 8px 0 6px; border-bottom: 2px solid var(--gold); margin-bottom: 8px; }
.header img { height: 80px; }
.columns { display: grid; grid-template-columns: 1fr 1fr; gap: 0 24px; }
.sec-title { font-family:'Cinzel',serif; color: var(--gold); font-size: 12px; letter-spacing: 2px; margin: 8px 0 4px; padding-bottom: 3px; border-bottom: 1px solid #444; }
.item { display: flex; justify-content: space-between; align-items: baseline; padding: 2px 0; }
.item-left { display: flex; flex-direction: column; flex: 1; }
.item-name { font-size: 11.5px; color: var(--cream); font-weight: 600; }
.item-desc { font-size: 9px; color: var(--smoke); font-style: italic; margin-top: 0; }
.item-price { font-size: 11px; color: var(--gold); font-weight: 600; margin-left: 8px; white-space: nowrap; }
.item-note { font-size: 8.5px; color: var(--smoke); font-style: italic; margin-top: 3px; padding: 3px 6px; background: rgba(255,255,255,0.03); border-radius: 3px; }
.menu-section { margin-bottom: 3px; }
.drinks-bar { margin-top: 5px; padding-top: 5px; border-top: 2px solid var(--gold); display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 0 16px; }
.legend { margin-top: 5px; padding-top: 4px; border-top: 1px solid #444; font-size: 8px; color: var(--smoke); text-align: center; }
.legend em { font-size: 7px; color: #666; }
.back-logo { width: 320px; filter: drop-shadow(0 0 40px rgba(201,136,43,0.3)); }
.back-tagline { font-family:'Parisienne',cursive; color: var(--gold); font-size: 24px; margin-top: 12px; text-align: center; }
.combo-box { background: rgba(201,136,43,0.08); border: 1px solid var(--gold); border-radius: 6px; padding: 6px 10px; margin-bottom: 5px; }
.combo-box .sec-title { margin-top: 2px; border-bottom: none; }
@media print { body{background:white;} .page{margin:0;box-shadow:none;} .page-back{page-break-before:always;} }
"""
    front = f"""<div class="page page-front">
<div class="header">
    <img src="{LOGO_SRC}" alt="Brasa Roja">
</div>
<div class="combo-box">
{render_items_dark("combos", show_desc=True)}
</div>
<div class="columns">
<div class="col-left">
{render_items_dark("sandwiches")}
{render_items_dark("platos")}
</div>
<div class="col-right">
{render_items_dark("pastas")}
{render_items_dark("ensaladas")}
{render_items_dark("guarniciones")}
{render_items_dark("postres")}
</div>
</div>
<div class="drinks-bar">
{render_items_dark("tragos")}
{render_items_dark("cervezas_vinos")}
{render_items_dark("sin_alcohol")}
</div>
{LEGEND}
{footer_info(dark=True)}
</div>"""

    back = f"""<div class="page page-back">
<div style="text-align:center">
    <img class="back-logo" src="{LOGO_SRC}" alt="Brasa Roja">
    <div class="back-tagline">Tradición Familiar</div>
</div>
</div>"""

    return html_head("Brasa Roja - Concepto 01: El Clasico", css) + front + divider("DA VUELTA — REVERSO") + back + html_foot()


# ============================================================
# CONCEPT 02: EL DOBLE
# Double sided A4. Front: food (cream bg). Back: drinks+desserts (dark bg).
# ============================================================
def concept_02():
    css = """
@page { size: 8.5in 11in; margin: 0; }
body { font-family: 'Lora', Georgia, serif; background: #e0e0e0; }
.page { width: 8.5in; min-height: 11in; margin: 10px auto; position: relative; overflow: hidden; }
.page-a { background: var(--cream); color: var(--charcoal); padding: 0.5in 0.6in; }
.page-b { background: var(--charcoal); color: var(--cream); padding: 0.5in 0.6in; }
.header-a { text-align: center; margin-bottom: 14px; padding-bottom: 10px; border-bottom: 2px solid var(--gold); }
.header-a img { height: 90px; }
.header-b { text-align: center; margin-bottom: 14px; }
.header-b img { height: 55px; }
.header-b h2 { font-family:'Cinzel',serif; color: var(--gold); font-size: 17px; letter-spacing: 4px; margin-top: 8px; }
.sec-title { font-family:'Cinzel',serif; color: var(--gold); font-size: 13px; letter-spacing: 2.5px; margin: 14px 0 5px; padding-bottom: 4px; border-bottom: 1px solid var(--gold); }
.page-b .sec-title { border-bottom-color: #555; }
.columns { display: grid; grid-template-columns: 1fr 1fr; gap: 0 30px; }
.item { display: flex; justify-content: space-between; align-items: baseline; padding: 3px 0; }
.item-left { display: flex; flex-direction: column; flex: 1; }
.item-name { font-size: 13px; font-weight: 600; }
.page-a .item-name { color: var(--charcoal); }
.page-b .item-name { color: var(--cream); }
.item-desc { font-size: 10px; color: var(--smoke); font-style: italic; }
.item-price { font-size: 12px; color: var(--gold); font-weight: 600; margin-left: 10px; white-space: nowrap; }
.item-note { font-size: 8.5px; color: var(--smoke); font-style: italic; margin-top: 4px; }
.menu-section { margin-bottom: 2px; }
.combo-box { background: rgba(201,136,43,0.08); border: 1.5px solid var(--gold); border-radius: 8px; padding: 10px 16px; margin-bottom: 8px; }
.combo-box .sec-title { margin-top: 2px; }
.legend { margin-top: 10px; padding-top: 8px; border-top: 1px solid #ddd; font-size: 8.5px; color: var(--smoke); text-align: center; }
.page-b .legend { border-top-color: #444; }
.legend em { font-size: 7.5px; }
.footer { text-align: center; font-family:'Parisienne',cursive; color: var(--gold); font-size: 14px; margin-top: 14px; }
.drink-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 0 30px; }
@media print { body{background:white;} .page{margin:0;box-shadow:none;} .page-b{page-break-before:always;} }
"""
    page_a = f"""<div class="page page-a">
<div class="header-a"><img src="{LOGO_SRC}" alt="Brasa Roja"></div>
<div class="combo-box">
{render_items_light("combos")}
</div>
<div class="columns">
<div>
{render_items_light("sandwiches")}
{render_items_light("platos")}
</div>
<div>
{render_items_light("pastas")}
{render_items_light("ensaladas")}
{render_items_light("guarniciones")}
</div>
</div>
{LEGEND}
{footer_info(dark=False)}
</div>"""

    page_b = f"""<div class="page page-b">
<div class="header-b">
    <img src="{ICON_SRC}" alt="BR" style="height:50px">
    <h2>BEBIDAS Y POSTRES</h2>
</div>
<div class="drink-grid">
<div>
{render_items_dark("tragos")}
{render_items_dark("cervezas_vinos")}
{render_items_dark("sin_alcohol")}
</div>
<div>
{render_items_dark("postres")}
{render_items_dark("cafeteria")}
</div>
</div>
{LEGEND}
{footer_info(dark=True)}
</div>"""

    return html_head("Brasa Roja - Concepto 02: El Doble", css) + page_a + divider("✂ DA VUELTA — LADO B: BEBIDAS Y POSTRES ✂") + page_b + html_foot()


# ============================================================
# CONCEPT 03: EL TRIPTICO
# Tri-fold. 3 panels inner = food. Outer panels = drinks + cover.
# ============================================================
def concept_03():
    css = """
@page { size: 11in 8.5in; margin: 0; }
body { font-family: 'Lora', Georgia, serif; background: #e0e0e0; }
.spread { width: 11in; height: 8.5in; margin: 10px auto; display: grid; grid-template-columns: 1fr 1fr 1fr; position: relative; }
.spread-inner { background: var(--cream); color: var(--charcoal); }
.spread-outer { background: var(--charcoal); color: var(--cream); }
.panel { padding: 0.35in; overflow: hidden; border-right: 2px dashed rgba(201,136,43,0.4); }
.panel:last-child { border-right: none; }
.panel-cover { display: flex; flex-direction: column; align-items: center; justify-content: center; background: var(--dark); text-align: center; }
.panel-cover img { width: 200px; filter: drop-shadow(0 0 20px rgba(201,136,43,0.3)); }
.panel-cover .tagline { font-family:'Parisienne',cursive; color: var(--gold); font-size: 18px; margin-top: 10px; }
.panel-cover .sub { color: var(--smoke); font-size: 10px; margin-top: 20px; letter-spacing: 2px; font-family:'Cinzel',serif; }
.sec-title { font-family:'Cinzel',serif; color: var(--gold); font-size: 11px; letter-spacing: 2px; margin: 10px 0 4px; padding-bottom: 3px; border-bottom: 1px solid var(--gold); }
.spread-outer .sec-title { border-bottom-color: #555; }
.item { display: flex; justify-content: space-between; align-items: baseline; padding: 2px 0; }
.item-left { display: flex; flex-direction: column; flex: 1; }
.item-name { font-size: 11px; font-weight: 600; }
.item-desc { font-size: 9px; color: var(--smoke); font-style: italic; }
.item-price { font-size: 10.5px; color: var(--gold); font-weight: 600; margin-left: 6px; white-space: nowrap; }
.item-note { font-size: 7.5px; color: var(--smoke); font-style: italic; margin-top: 2px; }
.menu-section { margin-bottom: 2px; }
.legend { margin-top: 6px; padding-top: 4px; border-top: 1px solid #ddd; font-size: 7px; color: var(--smoke); text-align: center; }
.spread-outer .legend { border-top-color: #444; }
.legend em { font-size: 6.5px; }
.combo-box { background: rgba(201,136,43,0.08); border: 1px solid var(--gold); border-radius: 6px; padding: 5px 8px; margin-bottom: 4px; }
.combo-box .sec-title { margin-top: 0; }
@media print { body{background:white;} .spread{margin:0;} }
"""

    inner = f"""<div class="spread spread-inner">
<div class="panel">
<div class="combo-box">
{render_items_light("combos", show_desc=True)}
</div>
{render_items_light("sandwiches")}
</div>
<div class="panel">
{render_items_light("platos")}
{render_items_light("pastas")}
</div>
<div class="panel">
{render_items_light("ensaladas")}
{render_items_light("guarniciones")}
{render_items_light("postres")}
{LEGEND}
</div>
</div>"""

    outer = f"""<div class="spread spread-outer">
<div class="panel">
{render_items_dark("tragos")}
{render_items_dark("cervezas_vinos")}
{render_items_dark("sin_alcohol")}
{render_items_dark("cafeteria")}
</div>
<div class="panel" style="display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;background:var(--dark);">
    <img src="{ICON_SRC}" alt="BR" style="width:80px;opacity:0.15;">
    <p style="font-family:'Parisienne',cursive;color:var(--gold);font-size:14px;margin-top:10px;">Bienvenidos a</p>
    <p style="font-family:'Cinzel',serif;color:var(--cream);font-size:18px;letter-spacing:4px;margin-top:4px;">BRASA<span style='color:var(--red)'>ROJA</span></p>
    <p style="font-family:'Parisienne',cursive;color:var(--gold);font-size:14px;margin-top:4px;">Tradición Familiar</p>
</div>
<div class="panel panel-cover">
    <img src="{LOGO_SRC}" alt="Brasa Roja">
    <div class="tagline">Tradición Familiar</div>
    <div class="sub">NUESTRO MENÚ</div>
{footer_info(dark=True)}
</div>
</div>"""

    return html_head("Brasa Roja - Concepto 03: El Triptico", css) + inner + divider("✂ DA VUELTA — EXTERIOR DEL TRIPTICO ✂") + outer + html_foot()


# ============================================================
# CONCEPT 04: EL RAPIDO
# A5 laminated card. Both sides. No descriptions. Big type.
# ============================================================
def concept_04():
    css = """
@page { size: 5.83in 8.27in; margin: 0; }
body { font-family: 'Lora', Georgia, serif; background: #e0e0e0; }
.card { width: 5.83in; min-height: 8.27in; margin: 10px auto; position: relative; }
.card-a { background: var(--charcoal); color: var(--cream); padding: 0.3in; }
.card-b { background: var(--dark); color: var(--cream); padding: 0.3in; }
.header { text-align: center; margin-bottom: 8px; }
.header img { height: 65px; }
.sec-title { font-family:'Cinzel',serif; color: var(--gold); font-size: 12px; letter-spacing: 2.5px; margin: 12px 0 5px; padding-bottom: 3px; border-bottom: 2px solid var(--gold); }
.item { display: flex; justify-content: space-between; align-items: center; padding: 4px 0; }
.item-left { flex: 1; }
.item-name { font-size: 14px; font-weight: 600; color: var(--cream); }
.item-desc { font-size: 10px; color: var(--smoke); font-style: italic; }
.item-price { font-size: 14px; color: var(--gold); font-weight: 700; margin-left: 10px; }
.item-note { font-size: 8px; color: var(--smoke); font-style: italic; margin-top: 2px; }
.menu-section { margin-bottom: 4px; }
.combo-box { background: rgba(201,136,43,0.12); border: 2px solid var(--gold); border-radius: 8px; padding: 8px 12px; margin-bottom: 8px; }
.combo-box .sec-title { margin-top: 2px; border-bottom: none; }
.combo-box .item-name { color: var(--gold); }
.legend { margin-top: 8px; padding-top: 6px; border-top: 1px solid #444; font-size: 7.5px; color: var(--smoke); text-align: center; }
.legend em { font-size: 7px; }
.lam-badge { position:absolute; top:8px; right:8px; background:var(--gold); color:var(--dark); font-size:7px; padding:2px 8px; border-radius:10px; font-family:'Cinzel',serif; letter-spacing:1px; }
@media print { body{background:white;} .card{margin:0;} .card-b{page-break-before:always;} }
"""
    card_a = f"""<div class="card card-a">
<div class="lam-badge">LAMINADO</div>
<div class="header"><img src="{LOGO_SRC}" alt="Brasa Roja"></div>
<div class="combo-box">
{render_items_dark("combos", show_desc=True)}
</div>
{render_items_dark("sandwiches", show_desc=True)}
{render_items_dark("platos", show_desc=True)}
{render_items_dark("pastas", show_desc=True)}
{LEGEND}
</div>"""

    card_b = f"""<div class="card card-b">
<div class="header"><img src="{ICON_SRC}" alt="BR" style="height:40px"></div>
{render_items_dark("ensaladas", show_desc=True)}
{render_items_dark("guarniciones", show_desc=True)}
{render_items_dark("postres", show_desc=True)}
<div style="margin-top:10px;padding-top:8px;border-top:2px solid var(--gold)">
{render_items_dark("tragos", show_desc=True)}
{render_items_dark("cervezas_vinos", show_desc=True)}
{render_items_dark("sin_alcohol", show_desc=True)}
</div>
{LEGEND}
{footer_info(dark=True)}
</div>"""

    return html_head("Brasa Roja - Concepto 04: El Rapido", css) + card_a + divider("✂ DA VUELTA — LADO B ✂") + card_b + html_foot()


# ============================================================
# CONCEPT 05: LA PIZARRA
# Chalkboard aesthetic. Single page. Hand-drawn feel.
# ============================================================
def concept_05():
    css = """
@page { size: 8.5in 11in; margin: 0; }
body { font-family: 'Lora', Georgia, serif; background: #e0e0e0; }
.page { width: 8.5in; min-height: 11in; margin: 10px auto; background: #1e1e1e; color: #e8e0d4; padding: 0.45in; position: relative; background-image: repeating-linear-gradient(0deg, transparent, transparent 40px, rgba(255,255,255,0.01) 40px, rgba(255,255,255,0.01) 41px); }
.chalk-border { border: 2px solid rgba(255,255,255,0.15); border-radius: 4px; padding: 0.3in; min-height: calc(11in - 1.1in); }
.header { text-align: center; margin-bottom: 12px; }
.header img { height: 85px; filter: brightness(1.1); }
.header .line { width: 60%; height: 1px; background: rgba(201,136,43,0.4); margin: 8px auto; }
.columns { display: grid; grid-template-columns: 1fr 1fr; gap: 0 28px; }
.sec-title { font-family:'Cinzel',serif; color: var(--gold); font-size: 13px; letter-spacing: 3px; margin: 14px 0 6px; text-align: center; }
.sec-title::before, .sec-title::after { content: ' ~ '; color: rgba(201,136,43,0.5); }
.item { display: flex; justify-content: space-between; align-items: baseline; padding: 2.5px 0; }
.item-left { display: flex; flex-direction: column; flex: 1; }
.item-name { font-size: 12px; color: rgba(255,255,255,0.9); font-weight: 400; }
.item-desc { font-size: 9.5px; color: rgba(255,255,255,0.4); font-style: italic; }
.item-price { font-size: 11.5px; color: var(--gold); font-weight: 600; margin-left: 8px; white-space: nowrap; }
.item-note { font-size: 8px; color: rgba(255,255,255,0.35); font-style: italic; margin-top: 2px; }
.menu-section { margin-bottom: 4px; }
.combo-box { border: 1px dashed rgba(201,136,43,0.4); border-radius: 6px; padding: 6px 10px; margin-bottom: 6px; }
.combo-box .sec-title { margin-top: 2px; }
.drinks-strip { margin-top: 8px; padding-top: 8px; border-top: 1px dashed rgba(255,255,255,0.15); display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 0 16px; }
.legend { margin-top: 8px; padding-top: 6px; border-top: 1px dashed rgba(255,255,255,0.1); font-size: 8px; color: rgba(255,255,255,0.35); text-align: center; }
.legend em { font-size: 7px; }
@media print { body{background:white;} .page{margin:0;} }
"""
    page = f"""<div class="page">
<div class="chalk-border">
<div class="header">
    <img src="{LOGO_SRC}" alt="Brasa Roja">
    <div class="line"></div>
</div>
<div class="combo-box">
{render_items_dark("combos")}
</div>
<div class="columns">
<div>
{render_items_dark("sandwiches")}
{render_items_dark("platos")}
</div>
<div>
{render_items_dark("pastas")}
{render_items_dark("ensaladas")}
{render_items_dark("guarniciones")}
{render_items_dark("postres")}
</div>
</div>
<div class="drinks-strip">
{render_items_dark("tragos", show_desc=True)}
{render_items_dark("cervezas_vinos", show_desc=True)}
{render_items_dark("sin_alcohol", show_desc=True)}
</div>
{LEGEND}
{footer_info(dark=True)}
</div>
</div>"""

    return html_head("Brasa Roja - Concepto 05: La Pizarra", css) + page + html_foot()


# ============================================================
# CONCEPT 06: EL PREMIUM
# Tabloid 11x17. Single side. Luxury. 3 columns.
# ============================================================
def concept_06():
    css = """
@page { size: 17in 11in; margin: 0; }
body { font-family: 'Lora', Georgia, serif; background: #ccc; }
.page { width: 17in; min-height: 11in; margin: 10px auto; background: var(--dark); color: var(--cream); padding: 0.6in 0.8in; position: relative; overflow: hidden; }
.gold-line-top { position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, transparent 5%, var(--gold) 50%, transparent 95%); }
.gold-line-bot { position: absolute; bottom: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, transparent 5%, var(--gold) 50%, transparent 95%); }
.header { text-align: center; margin-bottom: 16px; }
.header img { height: 110px; filter: drop-shadow(0 0 20px rgba(201,136,43,0.2)); }
.header .divider { width: 40%; height: 1px; background: var(--gold); margin: 10px auto; }
.columns { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 0 40px; }
.sec-title { font-family:'Cinzel',serif; color: var(--gold); font-size: 13px; letter-spacing: 3px; margin: 16px 0 6px; padding-bottom: 4px; border-bottom: 1px solid rgba(201,136,43,0.3); }
.item { display: flex; justify-content: space-between; align-items: baseline; padding: 3px 0; }
.item-left { display: flex; flex-direction: column; flex: 1; }
.item-name { font-size: 13px; color: var(--cream); font-weight: 600; }
.item-desc { font-size: 10px; color: var(--smoke); font-style: italic; }
.item-price { font-size: 12px; color: var(--gold); font-weight: 600; margin-left: 10px; white-space: nowrap; }
.item-note { font-size: 8px; color: var(--smoke); font-style: italic; margin-top: 3px; }
.menu-section { margin-bottom: 4px; }
.combo-box { background: rgba(201,136,43,0.06); border: 1px solid rgba(201,136,43,0.3); border-radius: 8px; padding: 8px 14px; margin-bottom: 8px; }
.combo-box .sec-title { margin-top: 2px; }
.legend { margin-top: 12px; padding-top: 8px; border-top: 1px solid rgba(201,136,43,0.2); font-size: 8.5px; color: var(--smoke); text-align: center; }
.legend em { font-size: 7.5px; }
.footer { text-align:center; margin-top:10px; font-family:'Parisienne',cursive; color:var(--gold); font-size:16px; }
@media print { body{background:white;} .page{margin:0;} }
"""
    page = f"""<div class="page">
<div class="gold-line-top"></div>
<div class="gold-line-bot"></div>
<div class="header">
    <img src="{LOGO_SRC}" alt="Brasa Roja">
    <div class="divider"></div>
</div>
<div class="combo-box">
{render_items_dark("combos")}
</div>
<div class="columns">
<div>
{render_items_dark("sandwiches")}
{render_items_dark("platos")}
</div>
<div>
{render_items_dark("pastas")}
{render_items_dark("ensaladas")}
{render_items_dark("guarniciones")}
{render_items_dark("postres")}
</div>
<div>
{render_items_dark("tragos")}
{render_items_dark("cervezas_vinos")}
{render_items_dark("sin_alcohol")}
{render_items_dark("cafeteria")}
</div>
</div>
{LEGEND}
{footer_info(dark=True)}
</div>"""

    return html_head("Brasa Roja - Concepto 06: El Premium", css) + page + html_foot()


# ============================================================
# CONCEPT 07: EL HIBRIDO QR
# Small card 4x6. Top 5 items + QR code.
# ============================================================
def concept_07():
    css = """
@page { size: 4in 6in; margin: 0; }
body { font-family: 'Lora', Georgia, serif; background: #e0e0e0; }
.card { width: 4in; min-height: 6in; margin: 10px auto; background: var(--dark); color: var(--cream); padding: 0.3in; text-align: center; position: relative; overflow: hidden; }
.gold-frame { border: 1px solid rgba(201,136,43,0.3); border-radius: 8px; padding: 0.25in; min-height: calc(6in - 0.7in); display: flex; flex-direction: column; }
.header img { height: 70px; margin-bottom: 6px; }
.header .sub { font-family:'Cinzel',serif; color: var(--gold); font-size: 9px; letter-spacing: 2px; margin-bottom: 10px; }
.top-title { font-family:'Cinzel',serif; color: var(--gold); font-size: 10px; letter-spacing: 2px; margin-bottom: 8px; }
.top-item { display: flex; justify-content: space-between; padding: 4px 0; border-bottom: 1px solid rgba(255,255,255,0.06); text-align: left; }
.top-item .name { font-size: 11px; color: var(--cream); }
.top-item .price { font-size: 11px; color: var(--gold); font-weight: 600; }
.qr-section { margin-top: auto; padding-top: 12px; }
.qr-box { width: 100px; height: 100px; background: white; border-radius: 8px; margin: 0 auto 8px; display: flex; align-items: center; justify-content: center; }
.qr-box span { font-size: 10px; color: #333; font-family: monospace; }
.qr-label { font-size: 10px; color: var(--gold); font-family:'Cinzel',serif; letter-spacing: 1px; }
.qr-sub { font-size: 8px; color: var(--smoke); margin-top: 2px; }
.footer { font-family:'Parisienne',cursive; color: var(--gold); font-size: 13px; margin-top: 10px; }
@media print { body{background:white;} .card{margin:0;} }
"""
    card = f"""<div class="card">
<div class="gold-frame">
<div class="header">
    <img src="{LOGO_SRC}" alt="Brasa Roja">
    <div class="sub">NUESTRO MENÚ</div>
</div>
<div class="top-title">★ LOS MAS PEDIDOS ★</div>
<div class="top-item"><span class="name">Combo Milanesa + Guarnicion + Agua <small style="color:var(--smoke);font-size:9px">(~850 kcal)</small></span><span class="price">25.000</span></div>
<div class="top-item"><span class="name">Choripan con Chimichurri <small style="color:var(--smoke);font-size:9px">(~450 kcal)</small></span><span class="price">7.500</span></div>
<div class="top-item"><span class="name">Colita de Cuadril a la Parrilla <small style="color:var(--smoke);font-size:9px">(~480 kcal)</small></span><span class="price">22.000</span></div>
<div class="top-item"><span class="name">Milanesa Napolitana <small style="color:var(--smoke);font-size:9px">(~780 kcal)</small></span><span class="price">22.000</span></div>
<div class="top-item"><span class="name">Fernet con Coca <small style="color:var(--smoke);font-size:9px">(~220 kcal)</small></span><span class="price">14.000</span></div>
<div class="qr-section">
    <div class="qr-box"><span>[QR CODE]</span></div>
    <div class="qr-label">ESCANEA PARA VER TODO EL MENU</div>
    <div class="qr-sub">Bebidas, Pastas, Ensaladas, Postres y mas</div>
</div>
{footer_info(dark=True)}
</div>
</div>"""

    return html_head("Brasa Roja - Concepto 07: El Hibrido QR", css) + card + html_foot()


# ============================================================
# CONCEPT 08: EL MODULAR
# Folder-style with 2 insert pages. Cover + 2 inner pages.
# ============================================================
def concept_08():
    css = """
@page { size: 8.5in 11in; margin: 0; }
body { font-family: 'Lora', Georgia, serif; background: #e0e0e0; }
.page { width: 8.5in; min-height: 11in; margin: 10px auto; position: relative; }
.cover { background: var(--dark); display: flex; align-items: center; justify-content: center; flex-direction: column; }
.cover img { width: 260px; filter: drop-shadow(0 0 30px rgba(201,136,43,0.3)); }
.cover .tagline { font-family:'Parisienne',cursive; color: var(--gold); font-size: 22px; margin-top: 12px; }
.cover .badge { font-family:'Cinzel',serif; color: var(--smoke); font-size: 10px; letter-spacing: 3px; margin-top: 30px; padding: 6px 20px; border: 1px solid var(--smoke); border-radius: 20px; }
.insert { background: var(--cream); color: var(--charcoal); padding: 0.5in 0.6in; }
.insert-dark { background: var(--charcoal); color: var(--cream); padding: 0.5in 0.6in; }
.insert-header { display: flex; align-items: center; gap: 12px; margin-bottom: 14px; padding-bottom: 10px; border-bottom: 2px solid var(--gold); }
.insert-header img { height: 40px; }
.insert-header h2 { font-family:'Cinzel',serif; color: var(--gold); font-size: 15px; letter-spacing: 3px; }
.columns { display: grid; grid-template-columns: 1fr 1fr; gap: 0 28px; }
.sec-title { font-family:'Cinzel',serif; color: var(--gold); font-size: 12px; letter-spacing: 2px; margin: 14px 0 5px; padding-bottom: 3px; border-bottom: 1px solid var(--gold); }
.insert-dark .sec-title { border-bottom-color: #555; }
.item { display: flex; justify-content: space-between; align-items: baseline; padding: 3px 0; }
.item-left { display: flex; flex-direction: column; flex: 1; }
.item-name { font-size: 12.5px; font-weight: 600; }
.item-desc { font-size: 10px; color: var(--smoke); font-style: italic; }
.item-price { font-size: 11.5px; color: var(--gold); font-weight: 600; margin-left: 8px; white-space: nowrap; }
.item-note { font-size: 8px; color: var(--smoke); font-style: italic; margin-top: 3px; }
.menu-section { margin-bottom: 3px; }
.combo-box { background: rgba(201,136,43,0.08); border: 1.5px solid var(--gold); border-radius: 8px; padding: 8px 14px; margin-bottom: 8px; }
.combo-box .sec-title { margin-top: 2px; }
.legend { margin-top: 10px; padding-top: 6px; border-top: 1px solid #ddd; font-size: 8px; color: var(--smoke); text-align: center; }
.insert-dark .legend { border-top-color: #444; }
.legend em { font-size: 7px; }
.page-label { position:absolute; top:12px; right:16px; font-family:'Cinzel',serif; font-size:8px; color:var(--smoke); letter-spacing:2px; }
@media print { body{background:white;} .page{margin:0;page-break-after:always;} }
"""
    cover = f"""<div class="page cover">
    <img src="{LOGO_SRC}" alt="Brasa Roja">
    <div class="tagline">Tradición Familiar</div>
    <div class="badge">NUESTRO MENÚ</div>
</div>"""

    insert1 = f"""<div class="page insert">
<div class="page-label">HOJA 1 — COMIDAS</div>
<div class="insert-header">
    <img src="{ICON_SRC}" alt="BR">
    <h2>COMIDAS</h2>
</div>
<div class="combo-box">
{render_items_light("combos")}
</div>
<div class="columns">
<div>
{render_items_light("sandwiches")}
{render_items_light("platos")}
</div>
<div>
{render_items_light("pastas")}
{render_items_light("ensaladas")}
{render_items_light("guarniciones")}
</div>
</div>
{LEGEND}
{footer_info(dark=False)}
</div>"""

    insert2 = f"""<div class="page insert-dark">
<div class="page-label" style="color:#666">HOJA 2 — BEBIDAS Y POSTRES</div>
<div class="insert-header">
    <img src="{ICON_SRC}" alt="BR">
    <h2>BEBIDAS Y POSTRES</h2>
</div>
<div class="columns">
<div>
{render_items_dark("tragos")}
{render_items_dark("cervezas_vinos")}
{render_items_dark("sin_alcohol")}
</div>
<div>
{render_items_dark("postres")}
{render_items_dark("cafeteria")}
</div>
</div>
{LEGEND}
{footer_info(dark=True)}
</div>"""

    return html_head("Brasa Roja - Concepto 08: El Modular", css) + cover + divider("✂ HOJA 1 — COMIDAS ✂") + insert1 + divider("✂ HOJA 2 — BEBIDAS Y POSTRES ✂") + insert2 + html_foot()


# ============================================================
# CONCEPT 09: EL DEPORTIVO
# Rugby-themed sections. Warm-up, 1st half, 2nd half, 3rd time.
# ============================================================
def concept_09():
    css = """
@page { size: 8.5in 11in; margin: 0; }
body { font-family: 'Lora', Georgia, serif; background: #e0e0e0; }
.page { width: 8.5in; min-height: 11in; margin: 10px auto; position: relative; overflow: hidden; }
.page-a { background: var(--charcoal); color: var(--cream); padding: 0.4in 0.5in; }
.page-b { background: var(--dark); color: var(--cream); padding: 0.4in 0.5in; }
.header { text-align: center; margin-bottom: 10px; }
.header img { height: 80px; }
.header .divider { width: 50%; height: 2px; background: linear-gradient(90deg, transparent, var(--gold), transparent); margin: 8px auto; }
.time-title { font-family:'Cinzel',serif; font-size: 14px; letter-spacing: 4px; margin: 16px 0 4px; padding: 8px 16px; text-align: center; border-radius: 4px; }
.time-sub { text-align: center; font-size: 9px; color: var(--smoke); font-style: italic; margin-bottom: 8px; }
.warmup { background: rgba(201,136,43,0.12); color: var(--gold); border: 1px solid rgba(201,136,43,0.3); }
.first-half { background: rgba(198,51,51,0.1); color: var(--red); border: 1px solid rgba(198,51,51,0.2); }
.second-half { background: rgba(139,37,0,0.1); color: var(--cream); border: 1px solid rgba(139,37,0,0.3); }
.third-time { background: rgba(201,136,43,0.15); color: var(--gold); border: 2px solid var(--gold); }
.columns { display: grid; grid-template-columns: 1fr 1fr; gap: 0 24px; }
.sec-title { font-family:'Cinzel',serif; color: var(--gold); font-size: 11px; letter-spacing: 2px; margin: 10px 0 4px; padding-bottom: 3px; border-bottom: 1px solid #444; }
.item { display: flex; justify-content: space-between; align-items: baseline; padding: 2.5px 0; }
.item-left { display: flex; flex-direction: column; flex: 1; }
.item-name { font-size: 12px; color: var(--cream); font-weight: 600; }
.item-desc { font-size: 9.5px; color: var(--smoke); font-style: italic; }
.item-price { font-size: 11px; color: var(--gold); font-weight: 600; margin-left: 8px; white-space: nowrap; }
.item-note { font-size: 8px; color: var(--smoke); font-style: italic; margin-top: 2px; }
.menu-section { margin-bottom: 3px; }
.legend { margin-top: 8px; padding-top: 6px; border-top: 1px solid #444; font-size: 8px; color: var(--smoke); text-align: center; }
.legend em { font-size: 7px; }
.footer { text-align:center; font-family:'Parisienne',cursive; color:var(--gold); font-size:13px; margin-top:8px; }
.field-line { height:1px; background:rgba(255,255,255,0.05); margin:4px 0; }
@media print { body{background:white;} .page{margin:0;} .page-b{page-break-before:always;} }
"""
    page_a = f"""<div class="page page-a">
<div class="header">
    <img src="{LOGO_SRC}" alt="Brasa Roja">
    <div class="divider"></div>
</div>

<div class="time-title warmup">⚡ ENTRADA EN CALOR</div>
<div class="time-sub">Para arrancar rapido. Combos y sandwiches.</div>
{render_items_dark("combos")}
{render_items_dark("sandwiches")}

<div class="field-line"></div>

<div class="time-title first-half">🔥 PRIMER TIEMPO</div>
<div class="time-sub">Los platos fuertes. Milanesas, carnes, pastas.</div>
<div class="columns">
<div>
{render_items_dark("platos")}
</div>
<div>
{render_items_dark("pastas")}
</div>
</div>

{LEGEND}
</div>"""

    page_b = f"""<div class="page page-b">
<div class="header">
    <img src="{ICON_SRC}" alt="BR" style="height:45px">
</div>

<div class="time-title second-half">🥗 SEGUNDO TIEMPO</div>
<div class="time-sub">Ensaladas, guarniciones y lo que acompana.</div>
<div class="columns">
<div>
{render_items_dark("ensaladas")}
</div>
<div>
{render_items_dark("guarniciones")}
</div>
</div>

<div class="field-line"></div>

<div class="time-title third-time">🍸 TERCER TIEMPO</div>
<div class="time-sub">Postres, tragos y lo que viene despues del partido.</div>
<div class="columns">
<div>
{render_items_dark("postres")}
{render_items_dark("cafeteria")}
</div>
<div>
{render_items_dark("tragos")}
{render_items_dark("cervezas_vinos")}
{render_items_dark("sin_alcohol")}
</div>
</div>

{LEGEND}
{footer_info(dark=True)}
</div>"""

    return html_head("Brasa Roja - Concepto 09: El Deportivo", css) + page_a + divider("✂ DA VUELTA — SEGUNDO Y TERCER TIEMPO ✂") + page_b + html_foot()


# ============================================================
# CONCEPT 10: EL MINIMALISTA
# Half-letter. Cream paper. Minimal. Whisky bar feel.
# ============================================================
def concept_10():
    css = """
@page { size: 5.5in 8.5in; margin: 0; }
body { font-family: 'Lora', Georgia, serif; background: #e0e0e0; }
.card { width: 5.5in; min-height: 8.5in; margin: 10px auto; background: var(--cream); color: var(--charcoal); padding: 0.5in 0.45in; position: relative; }
.header { text-align: center; margin-bottom: 16px; }
.header img { height: 90px; }
.header .line { width: 30%; height: 1px; background: var(--gold); margin: 6px auto; }
.sec-title { font-family:'Cinzel',serif; color: var(--gold); font-size: 11px; letter-spacing: 3px; margin: 18px 0 6px; text-align: center; }
.item { display: flex; justify-content: space-between; align-items: center; padding: 4px 0; }
.item-name { font-size: 12.5px; color: var(--charcoal); }
.item-desc { font-size: 10px; color: var(--smoke); font-style: italic; }
.item-left { flex: 1; }
.item-price { font-size: 12px; color: var(--gold); font-weight: 600; margin-left: 8px; }
.item-note { font-size: 8px; color: var(--smoke); font-style: italic; text-align: center; margin-top: 2px; }
.menu-section { margin-bottom: 2px; }
.divider { width: 20%; height: 1px; background: var(--gold); margin: 12px auto; opacity: 0.4; }
.legend { margin-top: 14px; padding-top: 8px; border-top: 1px solid rgba(201,136,43,0.2); font-size: 7.5px; color: var(--smoke); text-align: center; }
.legend em { font-size: 7px; }
.footer { text-align: center; font-family:'Parisienne',cursive; color: var(--gold); font-size: 14px; margin-top: 12px; }
@media print { body{background:white;} .card{margin:0;box-shadow:none;} }
"""
    card = f"""<div class="card">
<div class="header">
    <img src="{LOGO_SRC}" alt="Brasa Roja">
    <div class="line"></div>
</div>
{render_items_light("combos", show_desc=True, show_icon=False)}
<div class="divider"></div>
{render_items_light("sandwiches", show_desc=True, show_icon=False)}
<div class="divider"></div>
{render_items_light("platos", show_desc=True, show_icon=False)}
<div class="divider"></div>
{render_items_light("pastas", show_desc=True, show_icon=False)}
<div class="divider"></div>
{render_items_light("ensaladas", show_desc=True, show_icon=False)}
{render_items_light("guarniciones", show_desc=True, show_icon=False)}
<div class="divider"></div>
{render_items_light("tragos", show_desc=True, show_icon=False)}
{render_items_light("cervezas_vinos", show_desc=True, show_icon=False)}
<div class="divider"></div>
{render_items_light("postres", show_desc=True, show_icon=False)}
{LEGEND}
{footer_info(dark=False)}
</div>"""

    return html_head("Brasa Roja - Concepto 10: El Minimalista", css) + card + html_foot()


# ============================================================
# GENERATE ALL
# ============================================================
def main():
    concepts = [
        ("Concepto_01_El_Clasico.html", concept_01),
        ("Concepto_02_El_Doble.html", concept_02),
        ("Concepto_03_El_Triptico.html", concept_03),
        ("Concepto_04_El_Rapido.html", concept_04),
        ("Concepto_05_La_Pizarra.html", concept_05),
        ("Concepto_06_El_Premium.html", concept_06),
        ("Concepto_07_El_Hibrido_QR.html", concept_07),
        ("Concepto_08_El_Modular.html", concept_08),
        ("Concepto_09_El_Deportivo.html", concept_09),
        ("Concepto_10_El_Minimalista.html", concept_10),
    ]

    print("=" * 55)
    print("  BRASA ROJA - Generating 10 Menu Concepts")
    print("=" * 55)
    print()

    for filename, gen_func in concepts:
        html = gen_func()
        path = OUT / filename
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        size_kb = len(html.encode("utf-8")) / 1024
        print(f"  [OK] {filename} ({size_kb:.0f} KB)")

    print()
    print(f"  All 10 concepts generated in: {OUT}")
    print("=" * 55)


if __name__ == "__main__":
    main()
