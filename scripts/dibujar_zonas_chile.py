# Dibuja el diagrama de las tres zonas de Chile (docs/design/oficinas/chile/zonas-chile.svg; armar_sitio_chile.py lo copia).
# Regla del 6-nov-2026: en las oficinas no va ninguna imagen de Truly ni de globaltni. Este dibujo es propio: toma del
# diagrama de Truly solo el estilo (vista isométrica de una casa en corte, de noche, con las zonas verde, amarilla y roja)
# y no copia su casa, su planta ni sus muebles. Uso: python3 -I scripts/dibujar_zonas_chile.py
import math
from pathlib import Path

SAL = Path(__file__).resolve().parent.parent / 'docs/design/oficinas/chile/zonas-chile.svg'
S, C, N = 22, math.cos(math.radians(30)), math.sin(math.radians(30))

def iso(x, y, z=0):
    return ((x - y) * C * S, (x + y) * N * S - z * S)

def poli(pts, fill, op=1, stroke=None, sw=0, extra=''):
    p = ' '.join(f'{a:.1f},{b:.1f}' for a, b in (iso(*q) for q in pts))
    st = f' stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"' if stroke else ''
    o = f' fill-opacity="{op}"' if op != 1 else ''
    return f'<polygon points="{p}" fill="{fill}"{o}{st}{extra}/>'

def caja(x0, y0, x1, y1, z0, z1, arriba, lado_x, lado_y):
    # Caras visibles desde el espectador: la de arriba, la que mira a +x y la que mira a +y.
    return [poli([(x1, y0, z0), (x1, y1, z0), (x1, y1, z1), (x1, y0, z1)], lado_x),
            poli([(x0, y1, z0), (x1, y1, z0), (x1, y1, z1), (x0, y1, z1)], lado_y),
            poli([(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)], arriba)]

def anillo(ext, inn):
    # Banda entre dos contornos (regla evenodd): la zona amarilla y la verde rodean a la casa sin taparla.
    f = lambda pts: 'M' + ' L'.join(f'{a:.1f},{b:.1f}' for a, b in (iso(*q) for q in pts)) + ' Z'
    return f(ext), f(inn)

L = []
# Terreno, cerco y senderos ------------------------------------------------------------------------------------------
LOTE = [(0, 0), (28, 0), (28, 24), (0, 24)]
L.append(poli([(x, y, 0) for x, y in LOTE], '#1f3a22'))
for i in range(0, 28, 2):  # franjas de pasto
    L.append(poli([(i, 0, 0), (i + 1, 0, 0), (i + 1, 24, 0), (i, 24, 0)], '#24432a', .55))
L.append(poli([(2, 16, 0), (6.5, 16, 0), (6.5, 24, 0), (2, 24, 0)], '#5f675e'))       # entrada de autos
L.append(poli([(9.5, 19.5, 0), (11.5, 19.5, 0), (11.5, 24, 0), (9.5, 24, 0)], '#727a70'))  # sendero a la puerta
L.append(poli([(21, 3, 0), (26, 3, 0), (26, 9, 0), (21, 9, 0)], '#6f776d'))           # terraza de baldosas
for i in range(1, 5):
    L.append(poli([(21 + i, 3, 0.01), (21.08 + i, 3, 0.01), (21.08 + i, 9, 0.01), (21 + i, 9, 0.01)], '#5a6158'))

# Casa: planta en L (unidades en metros) ---------------------------------------------------------------------------
CASA = [(7, 4), (19, 4), (19, 12), (15, 12), (15, 19), (7, 19)]
AMARILLA = [(5.4, 2.4), (20.6, 2.4), (20.6, 13.6), (16.6, 13.6), (16.6, 20.6), (5.4, 20.6)]
VERDE = [(0.8, 0.8), (27.2, 0.8), (27.2, 23.2), (0.8, 23.2)]
pv, pa = anillo([(x, y, 0) for x, y in VERDE], [(x, y, 0) for x, y in AMARILLA])
L.append(f'<path d="{pv} {pa}" fill="#4cff7a" fill-opacity=".20" fill-rule="evenodd" stroke="#7dff9c" stroke-opacity=".55" stroke-width="1.5"/>')
pa2, pc = anillo([(x, y, 0) for x, y in AMARILLA], [(x, y, 0) for x, y in CASA])
L.append(f'<path d="{pa2} {pc}" fill="#ffd800" fill-opacity=".62" fill-rule="evenodd" stroke="#ffe85c" stroke-opacity=".8" stroke-width="1.5"/>')

# Piso interior en rojo y piezas
L.append(poli([(x, y, 0) for x, y in CASA], '#9e2a22'))
L.append(poli([(x, y, 0) for x, y in CASA], '#ff4b3a', .35))
for x0, y0, x1, y1, col in [(8, 5, 12.5, 10.5, '#b5463a'), (13.5, 5, 18, 11, '#a83a30'), (8, 11.5, 14, 18, '#b84a3c')]:
    L.append(poli([(x0, y0, 0.02), (x1, y0, 0.02), (x1, y1, 0.02), (x0, y1, 0.02)], col, .55))   # alfombras / pisos

# Muebles (cajas bajas), de atrás hacia adelante
muebles = [
    (8.6, 5.6, 11.4, 7.6, 0, .55, '#e8d9c8', '#bfae9a', '#a8977f'),     # cama
    (8.6, 5.6, 11.4, 6.0, 0, .9, '#6b3b2b', '#4f2a1e', '#43231a'),      # respaldo
    (14.2, 5.6, 17.4, 6.6, 0, .9, '#d9d2c8', '#b0a89c', '#9a9286'),     # cocina
    (15, 8, 17, 10, 0, .75, '#7a4a33', '#5c3626', '#4d2d20'),           # mesa
    (8.7, 13, 9.7, 16.8, 0, .7, '#e5dccf', '#bcb2a3', '#a39a8b'),       # sofá
    (10.8, 14.2, 12.4, 15.6, 0, .4, '#5a3a2c', '#45291f', '#3a221a'),   # mesa de centro
]
for m in sorted(muebles, key=lambda m: m[2] + m[3]):
    L += caja(*m)

# Muros cortados (bajos, como maqueta): exteriores e interiores, ordenados por profundidad
H, T = 1.6, .3
muros = [
    (7, 4, 19, 4 + T), (7, 4, 7 + T, 19),                        # fondo
    (12.5, 4, 12.5 + T, 11), (7, 11, 15, 11 + T), (13.2, 11, 13.2 + T, 12),
    (19 - T, 4, 19, 12), (15, 12 - T, 19, 12), (15 - T, 12, 15, 19), (7, 19 - T, 15, 19),  # frente
]
for x0, y0, x1, y1 in sorted(muros, key=lambda w: (w[2] + w[3])):
    L += caja(x0, y0, x1, y1, 0, H, '#3b1410', '#c9b8a4', '#ddd0bf')

# Árboles y luces del jardín ---------------------------------------------------------------------------------------
for x, y in [(2.5, 3), (3, 10.5), (24.5, 14), (25.5, 20.5), (20, 22)]:
    cx, cy = iso(x, y, 0)
    L.append(f'<ellipse cx="{cx:.1f}" cy="{cy + 4:.1f}" rx="18" ry="9" fill="#0d1a10" opacity=".55"/>')
    L.append(f'<circle cx="{cx:.1f}" cy="{cy - 22:.1f}" r="19" fill="#2f6b37"/><circle cx="{cx - 6:.1f}" cy="{cy - 28:.1f}" r="11" fill="#3f8546"/>')
for x, y in [(1.5, 15), (1.5, 20), (8, 21.5), (13, 21.5), (21.5, 16), (27, 11), (17.5, 1.5), (9, 1.5)]:
    cx, cy = iso(x, y, 0)
    L.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="9" fill="url(#luz)"/><circle cx="{cx:.1f}" cy="{cy:.1f}" r="2" fill="#fff6d0"/>')
# Cerco
for i in range(0, 29, 2):
    for a, b in [((i, 0), (i, 0)), ((0, i), (0, i))]:
        if (a[0] <= 28 and a[1] <= 24):
            L += caja(a[0] - .15, a[1] - .15, a[0] + .15, a[1] + .15, 0, 1.2, '#cfd6cc', '#9aa597', '#b5beb1')

xs, ys = [], []
for x, y in [(0, 0), (28, 0), (28, 24), (0, 24)]:
    for z in (0, 2):
        a, b = iso(x, y, z); xs.append(a); ys.append(b)
pad = 14
vb = (min(xs) - pad, min(ys) - 50, max(xs) - min(xs) + 2 * pad, max(ys) - min(ys) + 50 + pad)
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb[0]:.0f} {vb[1]:.0f} {vb[2]:.0f} {vb[3]:.0f}" role="img" '
       'aria-labelledby="t"><title id="t">Una casa vista desde arriba con tres zonas: el jardín en verde, el borde de la casa en amarillo y el interior en rojo</title>'
       '<defs><radialGradient id="luz"><stop offset="0" stop-color="#fff3b0" stop-opacity=".9"/><stop offset="1" stop-color="#fff3b0" stop-opacity="0"/></radialGradient></defs>'
       f'<rect x="{vb[0]:.0f}" y="{vb[1]:.0f}" width="{vb[2]:.0f}" height="{vb[3]:.0f}" fill="#0e110e"/>' + ''.join(L) + '</svg>')
SAL.write_text(svg, encoding='utf-8')
print(SAL, len(svg), 'bytes; viewBox', [round(v) for v in vb])
