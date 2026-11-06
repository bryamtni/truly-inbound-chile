# Arma el sitio borrador de Truly Nolen Chile en sitio/ a partir del sitio de Venezuela ya armado (base de Roger,
# 5-nov-2026) y de nuestra investigación (docs/design/oficinas/chile). Pedido de Roger el 5-nov: «copia
# oficinas/venezuela como oficinas/chile y cámbiale todo con tu investigación». No hay generador ni candados: este
# script hace el reemplazo y se puede volver a correr cuando cambie un borrador.
#
# Uso (desde la raíz del repo):
#   python3 -I scripts/armar_sitio_chile.py
#
# Mientras no haya foto ni carro de Chile, la portada usa el video común del mundo; las plagas van sin foto; el contacto
# es la central de la casa matriz (WhatsApp, correo y horario no los publica la oficina). El blog sale de
# docs/design/oficinas/chile/blog/publicados/<slug>.json (método blog-verificado) y se publica en goteo: solo lo que
# tiene fecha de hoy o anterior, hora de Santiago (FECHA_HOY=AAAA-MM-DD para probar otra fecha).
import datetime, html, json, math, os, re, shutil, subprocess, sys
from zoneinfo import ZoneInfo
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
BASE = RAIZ / 'Roger/truly-inbound-base-sitio-2026-11-05'
DISENO = RAIZ / 'Roger/paquete-alumnos 2/capa-oficinas/scripts'
DOCS = RAIZ / 'docs/design/oficinas/chile'
OUT = RAIZ / 'sitio'
SITIO = 'https://bryamtni.github.io/truly-inbound-chile'  # GitHub Pages del repo; el sitio vive en una subcarpeta
VE, CL = '/oficinas/venezuela/', '/oficinas/chile/'

sys.path.insert(0, str(DISENO))
from diseno_oficina import _fin, _linea, _parrafos, _primera  # el mismo armado de tablas que usa el generador

e = lambda s: html.escape(s, quote=True)
ficha = json.loads((DOCS / 'ficha-chile-borrador.json').read_text(encoding='utf-8'))
TEL = ficha['oficina']['telefono']
TEL_URL = 'tel:' + re.sub(r'[^\d+]', '', TEL)
DIRECCION = ficha['oficina']['direccion']


# Nombre corto de cada plaga (menú, pie, tarjetas y «Otras plagas»); los títulos largos de los borradores no siguen una forma fija.
NOMBRES = {'raton-colilargo': 'Ratón colilargo', 'arana-de-rincon': 'Araña de rincón', 'termita-subterranea': 'Termita subterránea',
           'cucaracha-alemana': 'Cucaracha alemana', 'zancudo': 'Zancudo', 'paloma': 'Paloma'}


PLAGAS = []
for slug in ficha['paginas']['plagas']:
    d = json.loads((DOCS / f'borrador-paginas/plaga-{slug}.json').read_text(encoding='utf-8'))
    PLAGAS.append({'slug': slug, 'nombre': NOMBRES[slug], **d})
SERVICIOS = {s: json.loads((DOCS / f'borrador-paginas/servicio-{s}.json').read_text(encoding='utf-8'))
             for s in ficha['paginas']['servicios']}
NOMBRE_SERV = {'hogares': 'Hogares', 'comercios': 'Comercios', 'industria': 'Industria'}

# Blog: goteo por fecha, el más nuevo primero.
HOY = os.environ.get('FECHA_HOY') or datetime.datetime.now(ZoneInfo('America/Santiago')).date().isoformat()
BLOG = sorted((json.loads(p.read_text(encoding='utf-8')) for p in (DOCS / 'blog/publicados').glob('*.json')),
              key=lambda a: (a['fecha'], a['title']), reverse=True)
BLOG = [a for a in BLOG if a['fecha'] <= HOY]
MESES = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
def fecha_larga(f): a, m, d = map(int, f.split('-')); return f'{d} de {MESES[m - 1]} de {a}'


def descripcion(texto, n=158):
    """Meta descripción: frases enteras hasta n caracteres."""
    out = ''
    for f in re.findall(r'[^.!?]+[.!?]', texto):
        if len(out + f) > n: break
        out += f
    return (out or texto[:n]).strip()


# ---------------------------------------------------------------- 1. copiar la base
if OUT.exists(): shutil.rmtree(OUT)
OUT.mkdir()
for x in ['landing', 'machotes', 'oficinas/assets', 'tn-emblema.png']:
    (shutil.copytree if (BASE / x).is_dir() else shutil.copy2)(BASE / x, OUT / x)
for p in OUT.rglob('.DS_Store'): p.unlink()
CHILE = OUT / 'oficinas/chile'
(CHILE / 'assets').mkdir(parents=True)
# Diagrama de las tres zonas dibujado para Chile (scripts/dibujar_zonas_chile.py): reemplaza zonas-truly-oficial.jpg,
# porque en las oficinas no va ninguna imagen de Truly ni de globaltni (regla de Roger, 6-nov-2026).
shutil.copy2(DOCS / 'zonas-chile.svg', CHILE / 'assets/zonas-chile.svg')
(OUT / 'oficinas/assets/zonas-truly-oficial.jpg').unlink()

# Portada provisional: un cuadro del video común del mundo (sin país). Se cambia por el carro de Chile en el paso 5.
ffmpeg = subprocess.run([str(Path.home() / '.local/bin/uv'), 'run', '-q', '--python', '3.12', '--no-project', '--with', 'imageio-ffmpeg',
                         'python', '-c', 'import imageio_ffmpeg,sys;sys.stdout.write(imageio_ffmpeg.get_ffmpeg_exe())'],
                        capture_output=True, text=True, check=True).stdout
mundo = OUT / 'oficinas/assets/mundo-desktop.mp4'
subprocess.run([ffmpeg, '-loglevel', 'error', '-y', '-i', mundo, '-frames:v', '1', '-vf', 'scale=1920:-1', '-quality', '82',
                CHILE / 'assets/chile-desktop.webp'], check=True)
subprocess.run([ffmpeg, '-loglevel', 'error', '-y', '-i', mundo, '-frames:v', '1', '-vf', 'scale=1200:-1,crop=1200:630', '-q:v', '3',
                CHILE / 'assets/chile-social.jpg'], check=True)


# ---------------------------------------------------------------- 2. lo común a todas las páginas
def leer(rel): return (BASE / 'oficinas/venezuela' / rel / 'index.html').read_text(encoding='utf-8')


# Bajada de cada plaga en el menú (la base repetía «Información e identificación de la plaga.» en las seis). Cada una
# resume lo que trae su guía, sin datos que la guía no tenga.
BAJADAS = {'raton-colilargo': 'Hantavirus y lo que recomienda el MINSAL.', 'arana-de-rincon': 'Qué indica la guía del MINSAL de 2016.',
           'termita-subterranea': 'Dónde se ha detectado en Chile.', 'cucaracha-alemana': 'Registros en Chile y control de rastreros.',
           'zancudo': 'Aedes aegypti y lo que informa el MINSAL.', 'paloma': 'Truly Pigeons Away y la autorización del SAG.'}


def enlaces_plagas(m):
    """Las listas de plagas del menú y del pie, con las de Chile y en el mismo formato que traían."""
    bloque = m.group(0)
    if '<strong>' in bloque:
        return ''.join(f'<a href="{CL}plagas/{p["slug"]}/"><strong>{e(p["nombre"])}</strong><span>{BAJADAS[p["slug"]]}</span></a>' for p in PLAGAS)
    return ''.join(f'<a href="{CL}plagas/{p["slug"]}/">{e(p["nombre"])}</a>' for p in PLAGAS)


CONTEXTO = (f'Truly Nolen Chile public website. Truly Nolen Chile has a local office: casa matriz at {DIRECCION}, phone {TEL}, '
            'with branches listed on trulynolen.cl. Never invent schedules, WhatsApp numbers, emails, prices, coverage of a specific '
            'commune, availability or guarantees: for those, invite the visitor to call the casa matriz or leave their details so the '
            'office confirms. Help visitors describe their pest situation (homes, businesses or industry): what they see, where, '
            'since when, type of space, children or pets. Explain the general Truly Nolen approach (listen, evaluate, propose, follow up). '
            'My Truly opens the separate VIP portal; Inside Truly opens the internal portal. No access to customer account data. '
            f'Do not claim the chat stores no data. Language: {ficha["chatIdioma"]}.')

LLAMAR = f'<a class="text-link" href="{TEL_URL}">Llamar al {e(TEL)}</a>'
CIERRE_TXT = 'Todo empieza con contarnos qué vio. Escríbale a Truly AI aquí mismo o llame a nuestra casa matriz y le orientamos en el siguiente paso.'
CIERRE = (f'<section id="contacto" class="s-closing"><div class="wrap"><h2>Cuéntenos qué necesita proteger.</h2><p>{e(CIERRE_TXT)}</p>'
          f'<div class="s-closing-actions"><a class="button button-dark" href="#contacto" data-abrir-chat>Escribir en el chat</a>{LLAMAR}'
          f'<a class="text-link" href="{CL}#consulta">Consultar cobertura →</a></div></div></section>')


# Ajustes de las secciones que Chile agrega a la base: (1) la pregunta de «Lo que más nos preguntan» alineada con su
# respuesta (la base le da 18 px de sangría, pensada para Industria de Venezuela); (2) al saltar desde «En esta página»,
# el título de la sección queda bajo la cabecera fija y no pegado a ella.
AJUSTES = ('<style>html body.country-site[data-oficina] #contenido details.ux-answer>summary h3{padding-left:0!important}'
           'html body.country-site[data-oficina] #contenido .pest-copy{scroll-margin-top:128px}'
           # (4) legales en párrafos: una columna de lectura de unos 70 caracteres reales (660 px; 70ch daba ~90), como una página legal de globaltni.
           'html body.country-site[data-oficina] #contenido .s-legal p{max-width:660px}'
           # (3) en la portada, los saltos a cobertura, consulta y preguntas también dejan aire bajo la cabecera.
           'html body.country-site[data-oficina] #contenido :is(#cobertura,#consulta){display:block}'
           'html body.country-site[data-oficina] #contenido :is(#cobertura,#consulta,#preguntas){scroll-margin-top:128px}'
           # (5) en celular, el botón del chat en reposo (88×89 px) tapaba al abrir la página las pestañas «Cucaracha alemana» y
           # «Paloma» de las guías: se achica al 82 % desde la esquina, misma forma, y sigue sobre los 44 px para tocarlo.
           '@media(max-width:760px){html body.country-site[data-oficina] .machote-chat-host .tia:not(.tia--on) .tia-fab'
           '{transform:scale(.82);transform-origin:100% 100%}}'
           # (6) lo de adentro de «Formación, supervisión y respuesta» (TEPS) no ocupa lugar mientras está cerrado: Chrome le
           # dejaba caja y el gate-replica lo daba como tapado por el chat sin que se viera.
           'html body.country-site[data-oficina] .teps details.program-overview:not([open])>.program{display:none}'
           # (7) el punto de «Áreas verdes» va verde como el césped del diagrama de Chile (la base lo dejaba gris).
           'html body.country-site[data-oficina][data-machote] .g-zonas-lista li.g-z-verde::before{background:#3f9b4a!important}'
           # (8) migas de los artículos del blog como las de los servicios: centradas con las «/» y sin negrita
           # (en celular los enlaces de 44 px de alto quedaban desfasados de las barras).
           'html body.country-site[data-oficina] .s-intro nav[aria-label="Ruta"]{align-items:center}'
           'html body.country-site[data-oficina] .s-intro nav[aria-label="Ruta"] a{font-weight:400!important;align-items:center}'
           # (9) en computadora, el «+»/«–» de «En esta página» de las guías queda fuera del botón del chat al abrir la página
           # (en 1440×900 el chat caía justo encima).
           '@media(min-width:761px){html body.country-site[data-oficina] .pest-index>summary{padding-right:96px!important}}'
           # (10) foto de los artículos del blog: alineada con el título y a su tamaño (hasta 640 px), no una miniatura centrada.
           'html body.country-site[data-oficina] .s-intro>.s-figure{margin-left:0!important;margin-right:auto!important;width:auto!important;max-width:640px!important}'
           'html body.country-site[data-oficina] .s-intro>.s-figure img{width:auto!important;max-width:100%!important;height:auto!important}'
           # (11) «¿Quién se beneficia?» de Comercios en una columna en celular: en dos se cortaban palabras («Supermercado/s»).
           '@media(max-width:480px){html body.country-site[data-oficina] .ct-facilities ul{grid-template-columns:1fr!important}}'
           # (12) en celular, con la página arriba del todo, el chat espera (arriba está «Conversemos» del hero): al abrir una guía
           # caía sobre las pestañas de plagas o sobre «En esta página». Aparece al bajar 160 px (CHAT_ARRIBA).
           'html body.country-site[data-oficina] .machote-chat-host .tia-fab{transition:opacity .2s}'
           'html.chat-arriba body.country-site[data-oficina] .machote-chat-host .tia:not(.tia--on) .tia-fab{opacity:0;pointer-events:none}'
           # (13) en celular, las secciones que terminan en un control pegado abajo dejan 88 px de aire: el chat ocupa los
           # últimos ~75 px de la pantalla y, al final de la sección, tapaba el «+» del índice del blog, la flecha de los videos
           # de ayuda, el botón «Escribir en el chat» y la última fuente de la portada.
           '@media(max-width:760px){html body.country-site[data-oficina] :is(.s-index,.g-ayuda,.contact-band,#fuentes-corporativas)'
           '{padding-bottom:88px!important}}'
           # (14) el índice «En este artículo» del blog lleva «+»/«−» como las preguntas (no se notaba que se abre).
           'html body.country-site[data-oficina] .s-index details>summary{justify-content:space-between;gap:24px;list-style:none}'
           'html body.country-site[data-oficina] .s-index details>summary::-webkit-details-marker{display:none}'
           'html body.country-site[data-oficina] .s-index details>summary::after{content:"+";flex:0 0 auto;font-size:22px;font-weight:400;line-height:1}'
           'html body.country-site[data-oficina] .s-index details[open]>summary::after{content:"−"}'
           # (15) crédito de una foto CC BY en su propia línea bajo el pie.
           'html body.country-site[data-oficina] .s-credito{display:block;margin-top:6px;font-style:normal;font-size:13px}'
           'html body.country-site[data-oficina] .s-credito a{color:inherit}</style>')
# Archivo aparte: la CSP del sitio (script-src 'self') bloquea los scripts en línea.
CHAT_ARRIBA_JS = ('(()=>{const m=matchMedia("(max-width:760px)"),f=()=>document.documentElement.classList.toggle("chat-arriba",'
                  'm.matches&&scrollY<160);addEventListener("scroll",f,{passive:true});m.addEventListener("change",f);f()})()\n')
CHAT_ARRIBA = f'<script src="{CL}assets/chat-arriba.js"></script>'
(CHILE / 'assets/chat-arriba.js').write_text(CHAT_ARRIBA_JS, encoding='utf-8')


def comun(t):
    t = t.replace(VE, CL).replace('</head>', AJUSTES + '</head>', 1).replace('</body>', CHAT_ARRIBA + '</body>', 1)
    # La marca en el sitio del país es Truly Nolen (la base decía «TNI» en Hogares y Comercios).
    t = t.replace('posible, TNI ofrece', 'posible, Truly Nolen Chile ofrece').replace('Contactar a TNI', 'Contactar a Truly Nolen')
    t = t.replace('archivo de servicios de TNI', 'archivo de servicios de Truly Nolen')
    t = re.sub(r'<img(?=[^>]*zonas-truly-oficial\.jpg)[^>]*?(loading="\w+")[^>]*>', lambda m: f'<img src="{CL}assets/zonas-chile.svg" width="1019" height="680" '
               'alt="Diagrama de las tres zonas: el jardín en verde, el borde de la casa en amarillo y el interior en rojo" ' + m.group(1) + '/>', t)
    # Plagas de Chile en el menú y en el pie (grupos seguidos de enlaces a plagas de Venezuela).
    t = re.sub(r'(?:<a href="/oficinas/chile/plagas/[^"]+/"[^>]*>.*?</a>)+', enlaces_plagas, t, flags=re.S)
    # El enlace al blog solo mientras haya artículos publicados.
    if not BLOG: t = re.sub(r'<a href="/oficinas/chile/blog/">Blog</a>', '', t)
    # Contacto: central de la casa matriz en vez del WhatsApp de Truly AI (Chile sí tiene oficina).
    t = re.sub(r'<a class="tia-wa" href="https://wa\.me/\d+"[^>]*>.*?</a>', f'<a class="tia-wa" href="{TEL_URL}">Llamar a Truly Nolen Chile</a>', t, flags=re.S)
    t = re.sub(r'<a class="text-link" href="https://wa\.me/\d+"[^>]*>Escribir por WhatsApp</a>', LLAMAR, t)
    t = t.replace('Todo empieza con contarnos qué vio. Escríbale a Truly AI aquí mismo o por WhatsApp y le orienta en el siguiente paso.', e(CIERRE_TXT))
    t = re.sub(r'(<script id="tia-contexto" type="text/plain">).*?(</script>)', lambda m: m.group(1) + e(CONTEXTO) + m.group(2), t, flags=re.S)
    t = re.sub(r'"wa": "Seguir por WhatsApp"', '"wa": "Llamar a la oficina"', t)
    t = t.replace('Soy Truly AI, de Truly Nolen Venezuela.', 'Soy Truly AI, de Truly Nolen Chile.')
    t = t.replace('data-storage-scope="oficina-venezuela"', 'data-storage-scope="oficina-chile"')
    t = t.replace('data-machote="venezuela" data-oficina="venezuela"', 'data-machote="chile" data-oficina="chile"')
    t = t.replace('<small data-preview-office>Venezuela</small>', '<small data-preview-office>Chile</small>')
    t = t.replace('<summary>Truly Nolen Venezuela</summary>', '<summary>Truly Nolen Chile</summary>')
    t = t.replace('© Truly Nolen · Venezuela', '© Truly Nolen · Chile')
    t = t.replace('Por ejemplo: comercios o alacranes', 'Por ejemplo: comercios o termitas')
    if not BLOG: t = t.replace('Busque servicios, plagas o artículos', 'Busque servicios o plagas')  # sin blog no hay artículos
    t = re.sub(r'(<script type="application/json" id="gt-buscar-indice">).*?(</script>)', lambda m: m.group(1) + BUSCAR + m.group(2), t, flags=re.S)
    return t


BUSCAR = json.dumps({'items': [[NOMBRE_SERV[s], SERVICIOS[s].get('resumen', ''), f'{CL}servicios/{s}/', 'Servicios'] for s in SERVICIOS]
                     + [[p['nombre'], p.get('avance') or _primera(p['intro']), f'{CL}plagas/{p["slug"]}/', 'Guía de plagas'] for p in PLAGAS]
                     + [[a['title'], a['meta_description'], f'{CL}blog/{a["slug"]}/', 'Blog'] for a in BLOG]
                     + [[x, '', f'{CL}#{a}', 'Inicio'] for x, a in [('Sanitización', 'sanitizacion'), ('Sistema TEPS', 'teps'), ('Cobertura', 'cobertura'), ('Nosotros', 'nosotros'), ('Preguntas frecuentes', 'preguntas'), ('Contacto', 'contacto')]],
                     'textos': {'uno': '1 resultado', 'varios': '{n} resultados', 'cero': 'Sin resultados. Pruebe con otra palabra.'}}, ensure_ascii=False).replace('</', '<\\/')


def cabeza(t, ruta, titulo, desc):
    """Título, descripción y direcciones de la página (canónica y redes en GitHub Pages, sin indexar)."""
    url = f'{SITIO}{CL}{ruta}'
    social = f'{SITIO}{CL}assets/chile-social.jpg'
    t = re.sub(r'<title>.*?</title>', f'<title>{e(titulo)}</title>', t, count=1)
    t = re.sub(r'(<meta (?:name="description"|property="og:description"|name="twitter:description") content=")[^"]*', lambda m: m.group(1) + e(desc), t)
    t = re.sub(r'(<meta (?:property="og:title"|name="twitter:title") content=")[^"]*', lambda m: m.group(1) + e(titulo), t)
    t = re.sub(r'(<link rel="canonical" href=")[^"]*', lambda m: m.group(1) + url, t)
    t = re.sub(r'(<meta property="og:url" content=")[^"]*', lambda m: m.group(1) + url, t)
    t = re.sub(r'(<meta (?:property="og:image"|name="twitter:image") content=")[^"]*', lambda m: m.group(1) + social, t)
    t = re.sub(r'(<meta property="og:image:alt" content=")[^"]*', lambda m: m.group(1) + 'Truly Nolen Chile', t)
    t = t.replace('content="Truly Nolen Venezuela"', 'content="Truly Nolen Chile"').replace('content="es_VE"', 'content="es_CL"')
    org = {'@context': 'https://schema.org', '@type': 'Organization', 'name': 'Truly Nolen Chile', 'url': f'{SITIO}{CL}',
           'logo': f'{SITIO}/tn-emblema.png', 'image': social, 'telephone': TEL,
           'address': {'@type': 'PostalAddress', 'streetAddress': 'Avenida Presidente Kennedy 8028', 'addressLocality': 'Vitacura',
                       'addressRegion': 'Región Metropolitana', 'addressCountry': 'CL'},
           'areaServed': {'@type': 'Country', 'name': 'Chile'}}
    web = {'@context': 'https://schema.org', '@type': 'WebSite', 'name': 'Truly Nolen Chile', 'url': f'{SITIO}{CL}', 'inLanguage': 'es'}
    lds = iter([org, web])
    t = re.sub(r'(<script type="application/ld\+json">)(.*?)(</script>)',
               lambda m: m.group(1) + json.dumps(next(lds, json.loads(m.group(2))), ensure_ascii=False) + m.group(3), t, flags=re.S)
    return t


def main(t, contenido):
    return re.sub(r'<main id="contenido">.*?</main>', lambda _: '<main id="contenido">' + contenido + '</main>', t, count=1, flags=re.S)


def guardar(rel, t):
    f = CHILE / rel / 'index.html'
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(t, encoding='utf-8')


# ---------------------------------------------------------------- 3. bloques de los borradores → HTML
def cifra(c):
    if 'valor' in c:
        cab, cuerpo = c['valor'], c['texto']
    else:
        cab, cuerpo = c['dato'], c.get('texto', '')
    fuente = c['fuente'] + (f' · Período: {c["anio"]}' if c.get('anio') else '')
    cab = cab if re.fullmatch(r'[\d.,%+ ]+', cab) else _fin(cab)
    return f'<p><strong>{e(cab)}</strong> {e(cuerpo)} <small class="s-fuente">{e(fuente)}</small></p>'


def tabla(b):
    # El mismo armado del generador: una cita repetida en filas seguidas se dice una sola vez para el grupo.
    return ''.join(_parrafos({}, {'tipo': 'tabla', 'filas': b['filas'], 'columnas': b.get('columnas') or []}, None))


def relacionadas(items):
    por_nombre = {p['nombre']: p for p in PLAGAS}
    li = ''.join(f'<li><a href="{CL}plagas/{por_nombre[x]["slug"]}/">{e(x)}</a></li>' for x in items if x in por_nombre)
    falta = [x for x in items if x not in por_nombre]
    if falta: print('  aviso: relacionadas sin página:', falta)
    return f'<ul class="s-enlaces">{li}</ul>' if li else ''


def preguntas(qs):
    if not qs: return ''
    qs = [(q['pregunta'], q['respuesta']) if isinstance(q, dict) else tuple(q) for q in qs]  # los borradores traen las dos formas
    det = ''.join(f'<details class="ux-answer"{" open" if i == 0 else ""}><summary><h3>{e(q)}</h3></summary><article><p>{e(a)}</p></article></details>'
                  for i, (q, a) in enumerate(qs))
    return f'<section class="wrap s-section s-preguntas"><h2>Lo que más nos preguntan.</h2><div class="s-prose">{det}</div></section>'


def fuentes(fs):
    if not fs: return ''
    li = ''.join(f'<li><a href="{e(u)}" target="_blank" rel="noopener noreferrer">{e(n)}</a></li>' for n, u in fs)
    return ('<section class="wrap s-section s-fuentes"><h2>De dónde sale esta información.</h2>'
            f'<p class="s-note">Cada dato de esta página viene de una fuente pública que puede revisar.</p><ol>{li}</ol></section>')


# ---------------------------------------------------------------- 4. plagas
# comun() va antes de poner el contenido: sus listas de plagas no deben tocar las del cuerpo.
# En celular las 6 pestañas de Chile (nombres más largos que los de Venezuela) se partían en filas desparejas: dos columnas parejas.
PESTANAS = ('<style>@media(max-width:760px){html body.country-site[data-oficina] .pest-families{display:grid!important;'
            'grid-template-columns:1fr 1fr;gap:0 18px!important}html body.country-site[data-oficina] .pest-families a{padding:12px 0 11px;justify-self:start}}</style>')
# (justify-self: cada pestaña mide lo que su texto, y el subrayado de la activa no llega hasta el botón del chat.)
PLANTILLA_PLAGA = comun(leer('plagas/zancudos')).replace('</head>', PESTANAS + '</head>', 1)
for i, p in enumerate(PLAGAS):
    secs, idx = [], []
    for n, b in enumerate(p['bloques'], 1):
        tipo = b['tipo']
        if tipo == 'tarjetas':
            tt = b.get('titulo') or 'Lo que hay que saber.'
            cuerpo = ''.join(f'<h3>{e(x["titulo"])}</h3><p>{e(x["texto"])}</p>' for x in b['items'])
        elif tipo == 'cifras':
            tt = b.get('titulo') or 'Lo que dicen las cifras.'
            cuerpo = ''.join(cifra(c) for c in b['items'])
        elif tipo == 'tabla':
            tt, cuerpo = b['titulo'], tabla(b)
        elif tipo == 'prosa':  # lo que no es «norma → qué pide» va en párrafos (receta, vuelta 5 d)
            tt, cuerpo = b['titulo'], ''.join(f'<p>{e(x)}</p>' for x in b['parrafos'])
        elif tipo == 'relacionadas':
            tt, cuerpo = b.get('titulo') or 'Otras plagas.', relacionadas(b['items'])
        else:
            raise SystemExit(f'bloque desconocido {tipo} en {p["slug"]}')
        if not cuerpo: continue
        tt = _fin(_linea(tt))
        secs.append(f'<section class="pest-copy" id="guia-{n}"><h2 id="guia-{n}-title">{e(tt)}</h2>{cuerpo}</section>')
        idx.append(f'<li><a href="#guia-{n}">{e(tt)}</a></li>')
    fam = ''.join(f'<a href="{CL}plagas/{q["slug"]}/"' + (' aria-current="page"' if q is p else '') + f'>{e(q["nombre"])}</a>' for q in PLAGAS)
    contenido = (f'<div class="wrap pest-wrap"><nav class="pest-breadcrumb" aria-label="Ruta"><a href="{CL}">Inicio</a><span aria-hidden="true">/</span><span>Guía de plagas</span><span aria-hidden="true">/</span><span>{e(p["nombre"])}</span></nav>'
                 f'<header class="pest-masthead"><div><p class="pest-eyebrow">Guía de plagas</p><h1>{e(p["nombre"])}</h1><p class="pest-lead">{e(p["intro"])}</p>'
                 f'<div class="pest-hero-actions"><a class="button" href="#contacto">Conversemos →</a><a class="text-link" href="#guia-1">Explorar esta guía ↓</a></div></div></header>'
                 f'<nav class="pest-families" aria-label="Guía de plagas">{fam}</nav>'
                 f'<div class="pest-layout"><aside class="pest-sidebar"><details class="pest-index" id="reading-index"><summary>En esta página <span>−</span></summary><ol>{"".join(idx)}</ol></details></aside>'
                 f'<div class="pest-content">{"".join(secs)}</div></div></div>'
                 + preguntas(p.get('preguntas')) + fuentes(p.get('fuentes')) + CIERRE)
    t = cabeza(main(PLANTILLA_PLAGA, contenido), f'plagas/{p["slug"]}/', f'{p["nombre"]} · Truly Nolen Chile', descripcion(p['intro']))
    guardar(f'plagas/{p["slug"]}', t)


# ---------------------------------------------------------------- 5. servicios
def secciones_servicio(s):
    b = s['bloques']
    out = ''
    if b.get('tarjetas'):
        ps = ''.join(f'<p><strong>{e(_fin(x["titulo"]))}</strong> {e(x["texto"])}</p>' for x in b['tarjetas'])
        out += f'<section class="wrap s-section s-flow"><h2>Cómo trabajamos en Chile.</h2><article class="s-prose">{ps}</article></section>'
    # Prosa como globaltni (regla del paquete: nada de tablas en servicios).
    for x in b.get('prosa', []):
        ps = ''.join(f'<p>{e(p)}</p>' for p in x['parrafos'])
        out += f'<section class="wrap s-section s-flow"><h2>{e(_fin(_linea(x["titulo"])))}</h2><article class="s-prose">{ps}</article></section>'
    if b.get('tabla'): raise SystemExit(f'{s["titulo"]}: los servicios van en prosa, no en tabla')
    if b.get('cifras'):
        out += f'<section class="wrap s-section s-flow"><h2>Lo que dicen las cifras.</h2><article class="s-prose">{"".join(cifra(c) for c in b["cifras"])}</article></section>'
    return out + preguntas(b.get('preguntas')) + fuentes(b.get('fuentes'))


def entrada_chile(s):
    return (f'<section class="wrap s-section s-flow" id="chile"><h2>{e(_fin(s["titulo"]))}</h2><article class="s-prose"><p>{e(s["intro"])}</p></article></section>')


FOTO_INDUSTRIA = '/oficinas/assets/sector-industria-planta.webp'
for slug, s in SERVICIOS.items():
    t = comun(leer(f'servicios/{slug}'))
    m = re.search(r'<main id="contenido">(.*?)</main>', t, re.S).group(1)
    if slug in ('hogares', 'comercios'):
        # La copia de globaltni se queda (es el plato); debajo va lo de Chile con sus fuentes, y el cierre nuevo.
        copia = re.sub(r'<section id="contacto" class="s-closing">.*$', '', m, flags=re.S)
        copia = re.sub(r'<section class="ct-contact">.*?</div></div></section>', '', copia, count=1, flags=re.S)  # un solo cierre: el nuestro
        contenido = copia + entrada_chile(s) + secciones_servicio(s) + CIERRE
    else:
        lead = (f'<section class="wrap s-intro"><nav aria-label="Ruta"><a href="{CL}">Inicio</a><span aria-hidden="true">/</span>Servicios<span aria-hidden="true">/</span>Servicio industrial</nav><h1>Servicio industrial</h1></section>'
                f'<section class="wrap s-section s-lead-pair"><article class="s-prose"><h2>{e(_fin(s["titulo"]))}</h2></article>'
                f'<article class="s-prose"><p>{e(s["intro"])}</p></article>'
                f'<figure class="s-figure"><img src="{FOTO_INDUSTRIA}" alt="Planta industrial"/></figure><a class="button s-service-action" href="#contacto">Conversemos →</a></section>')
        contenido = lead + secciones_servicio(s) + CIERRE
    titulo = {'hogares': 'Servicios residenciales', 'comercios': 'Servicios comerciales', 'industria': 'Industria'}[slug]
    guardar(f'servicios/{slug}', cabeza(main(t, contenido), f'servicios/{slug}/', f'{titulo} · Truly Nolen Chile', descripcion(s['resumen'])))


# ---------------------------------------------------------------- 6. legales
NOMBRES_LEGALES = {'privacidad': 'Privacidad', 'terminos': 'Términos de uso', 'accesibilidad': 'Accesibilidad'}
for slug, nombre in NOMBRES_LEGALES.items():
    t = comun(leer(slug))
    contenido = (f'<section class="wrap s-intro"><nav aria-label="Ruta"><a href="{CL}">Inicio</a><span aria-hidden="true">/</span>{e(nombre)}</nav><h1>{e(nombre)}</h1></section>'
                 '<section class="wrap s-section s-prose s-legal">' + ''.join(f'<p>{e(p).replace(TEL, TEL.replace(" ", "\u00a0"))}</p>' for p in ficha['legales'][slug].split('\n\n'))
                 + '</section>' + CIERRE)  # en los legales el teléfono va con espacios que no se parten
    guardar(slug, cabeza(main(t, contenido), f'{slug}/', f'{nombre} · Truly Nolen Chile', ficha['seo']['descripciones'][f'{slug}/']))


# ---------------------------------------------------------------- 7. portada

# Cobertura (pedido de Roger, 4-nov: casa matriz al frente y las sucursales en la cobertura), con los datos verificados
# en sucursales.json. Lo que no cuadra en el sitio de la oficina va solo con la ciudad.
SUC = json.loads((DOCS / 'sucursales.json').read_text(encoding='utf-8'))
def tel_url(x): return 'tel:' + re.sub(r'[^\d+]', '', x)
def sucursal(x, cls=''):
    return (f'<li{cls}><strong>{e(x["ciudad"])}</strong>' + (f'<span>{e(x["direccion"])}</span>' if x.get('direccion') else '')
            + (f'<a href="{tel_url(x["telefono"])}">{e(x["telefono"])}</a>' if x.get('telefono') else '')
            + (f'<small>Resolución sanitaria {e(x["resolucion"])}</small>' if x.get('resolucion') else '') + '</li>')
regiones = {}
for x in SUC['sucursales']: regiones.setdefault(x['region'], []).append(x)
m = SUC['casaMatriz']
COBERTURA = ('<style>#cobertura .cob-matriz{display:grid;gap:4px;margin:36px 0 44px;padding:28px 32px;background:#ffd800;list-style:none}'
             '#cobertura .cob-matriz strong{font-size:22px}#cobertura .cob-matriz :is(span,small){color:#010007}#cobertura .cob-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:36px 28px}'
             '#cobertura .cob-region h3{margin:0 0 12px;padding-top:14px;border-top:1px solid #dedede;font-size:14px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:#5e5e5e}'
             '#cobertura ul{margin:0;padding:0;list-style:none}#cobertura .cob-region li{margin:0 0 18px}'
             '#cobertura li strong{display:block;font-size:18px;color:#010007}#cobertura li span{display:block;font-size:15px;line-height:1.5;color:#5e5e5e}'
             '#cobertura li a{display:inline-block;margin-top:2px;font-size:15px;font-weight:600;color:#010007}#cobertura li small{display:block;font-size:13px;color:#5e5e5e}'
             '@media(max-width:1100px){#cobertura .cob-grid{grid-template-columns:repeat(3,minmax(0,1fr))}}'
             '@media(max-width:760px){#cobertura .cob-grid{grid-template-columns:repeat(2,minmax(0,1fr));gap:28px 18px}#cobertura .cob-matriz{padding:22px 20px}}'
             '</style>'
             '<section id="cobertura" class="section g g-cobertura"><span id="consulta"></span><header class="g-cab"><p class="g-ey">Cobertura</p>'
             '<h2>Casa matriz en Santiago.<br/>Sucursales de Arica a Chiloé.</h2>'
             '<p class="g-intro">Truly Nolen Chile informa cobertura de Arica a Chaitén, con sucursales que cumplen las resoluciones sanitarias de cada región. '
             'Llame a la casa matriz o a la sucursal más cercana para confirmar si atendemos su comuna.</p></header>'
             f'<ul class="cob-matriz"><li><strong>Casa matriz · {e(m["ciudad"])}</strong><span>{e(m["direccion"])}</span>'
             f'<a href="{tel_url(m["telefono"])}">{e(m["telefono"])}</a><small>Resolución sanitaria {e(m["resolucion"])}</small></li></ul>'
             '<div class="cob-grid">' + ''.join(f'<div class="cob-region"><h3>{e(r)}</h3><ul>{"".join(sucursal(x) for x in xs)}</ul></div>' for r, xs in regiones.items())
             + '</div></section>')
t = leer('')
t = re.sub(r'<source media="\(max-width:760px\)" srcset="[^"]*"/><img src="[^"]*"',
           f'<source media="(max-width:760px)" srcset="{CL}assets/chile-desktop.webp"/><img src="{CL}assets/chile-desktop.webp"', t, count=1)
t = re.sub(r'data-src-movil="[^"]*"', 'data-src-movil="/oficinas/assets/mundo-movil.mp4"', t, count=1)
t = re.sub(r'(<video[^>]*?) data-src="[^"]*"', r'\1 data-src="/oficinas/assets/mundo-desktop.mp4"', t, count=1)
t = t.replace('Truly Nolen · Venezuela', 'Truly Nolen · Chile')
t = t.replace('<span data-preview-office>Venezuela</span>', '<span data-preview-office>Chile</span>')
t = re.sub(r'/oficinas/venezuela/assets/ve-operacion-[^"]*', '/oficinas/assets/sector-alimentos-supermercado.webp', t)
# Plagas de Chile, sin foto mientras no haya fotos propias.
def resumen(intro):
    """Primera frase de la entrada; si es muy corta («convive con las personas»), también la segunda."""
    uno = _primera(intro)
    return uno if len(uno) >= 70 else _primera(intro) + ' ' + _primera(intro[len(uno):])


GRUPO = {'raton-colilargo': 'roedores', 'arana-de-rincon': 'arañas', 'termita-subterranea': 'termitas', 'cucaracha-alemana': 'cucarachas',
         'zancudo': 'zancudos', 'paloma': 'aves urbanas'}
tarjetas = ''.join(f'<article style="display:flex;flex-direction:column"><h3>{e(p["nombre"])}</h3><p class="g-pl-sub">Guía de {GRUPO[p["slug"]]}</p><p>{e(p.get("avance") or resumen(p["intro"]))}</p>'
                   f'<a class="g-mas" href="{CL}plagas/{p["slug"]}/">Ver la guía<span aria-hidden="true">→</span></a></article>' for p in PLAGAS)
t = re.sub(r'<div class="g-plagas-grid" style="--n:6">.*?</div></section>', f'<div class="g-plagas-grid" style="--n:{len(PLAGAS)}">{tarjetas}</div></section>', t, count=1, flags=re.S)
t = t.replace('Las que más vemos en Venezuela. Cada guía explica las señales y qué hacer, con fuentes.',
              'Seis plagas con presencia documentada en Chile. Cada guía explica qué dicen las fuentes del país y qué hacer.')
if BLOG:
    # El último artículo en el bloque de ayuda, como en Venezuela.
    a = BLOG[0]
    url = f'{CL}blog/{a["slug"]}/'
    img = f'<img src="{CL}assets/{a["cover_url"]}" alt="" loading="lazy"/>' if (DOCS / 'blog/fotos' / a['cover_url']).exists() else ''
    tarjeta = (f'<article class="g-blog"><div class="g-blog-top">{img}<p class="g-ey">Del blog · {fecha_larga(a["fecha"])}</p></div>'
               f'<h3><a href="{url}">{e(a["title"])}</a></h3><p>{e(a["excerpt"])}</p>'
               f'<a class="g-link" href="{url}">Leer el artículo<span aria-hidden="true">→</span></a>'
               f'<a class="g-link g-link-2" href="{CL}blog/">Ver todo el blog<span aria-hidden="true">→</span></a></article>')
    t = re.sub(r'<article class="g-blog">.*?</article>', lambda _: tarjeta, t, count=1, flags=re.S)
else:
    # Sin blog: queda solo el bloque de preguntas.
    t = re.sub(r'<article class="g-blog">.*?</article>', '', t, count=1, flags=re.S)
    t = re.sub(r'(<section class="section g g-ayuda">)(<header class="g-cab">.*?</header>)(<div class="g-ayuda-grid">)', r'\1\3\2', t, count=1, flags=re.S)
    t = t.replace('<p class="g-intro">Consejos para prevenir plagas y cómo trabajamos.</p>', '<p class="g-intro">Cómo empieza el servicio y qué conviene preparar.</p>')
t = t.replace('Indique su estado, municipio y el tipo de espacio.', 'Indique su región, su comuna y el tipo de espacio.')
t = t.replace('<div class="contact-actions"><a class="button button-dark" href="#contacto" data-abrir-chat>Escribir en el chat</a>',
              f'<div class="contact-actions"><a class="button button-dark" href="#contacto" data-abrir-chat>Escribir en el chat</a>')
# La cobertura va antes de las fuentes; sus anclas (#cobertura, #consulta) salen del bloque de contacto.
t = t.replace('<span id="consulta"></span><span id="cobertura"></span>', '', 1)
assert '<section class="wrap s-section s-fuentes" id="fuentes-corporativas"><h2>Fuentes</h2><ol>' in t
t = t.replace('<section class="wrap s-section s-fuentes" id="fuentes-corporativas"><h2>Fuentes</h2><ol>',
              COBERTURA + '<section class="wrap s-section s-fuentes" id="fuentes-corporativas"><h2>Fuentes</h2><ol>'
              '<li><a href="https://trulynolen.cl/sucursales-trulynolen-chile/" target="_blank" rel="noopener noreferrer">Truly Nolen Chile · Sucursales (leída el 5 de noviembre de 2026)</a></li>', 1)
t = re.sub(r'(<div class="contact-intro"><h2 id="contact-title">.*?</h2><p>.*?</p>)', lambda m: m.group(1) + f'<p>Casa matriz: {e(DIRECCION)}.</p>', t, count=1, flags=re.S)
t = cabeza(comun(t), '', 'Truly Nolen Chile | Control de plagas',
           'Control de plagas en Chile para hogares, comercios e industrias. Escríbale a Truly AI o llame a la casa matriz en Vitacura.')
guardar('', t)


# ---------------------------------------------------------------- 7b. blog
def md_a_html(md):
    """Markdown de blog-verificado a HTML: se escapa todo y solo pasan ##/###, párrafos, listas, negrita, cursiva y enlaces."""
    def linea(x):
        x = e(x)
        x = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', x)
        x = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', x)
        return re.sub(r'(?<![\w*])[*_](?!\s)(.+?)(?<!\s)[*_](?![\w*])', r'<em>\1</em>', x)
    out, lista, n = [], None, 0
    def cerrar():
        nonlocal lista
        if lista: out.append(f'</{lista}>'); lista = None
    for bloque in re.split(r'\n\s*\n', md.strip()):
        for l in bloque.split('\n'):
            l = l.rstrip()
            if not l: continue
            if l.startswith('## '):
                cerrar(); n += 1; out.append(f'<h2 id="art-{n}">{linea(l[3:])}</h2>')
            elif l.startswith('### '):
                cerrar(); out.append(f'<h3>{linea(l[4:])}</h3>')
            elif re.match(r'[-*] ', l) or re.match(r'\d+\. ', l):
                tipo = 'ol' if re.match(r'\d+\. ', l) else 'ul'
                if lista != tipo: cerrar(); out.append(f'<{tipo}>'); lista = tipo
                out.append(f'<li>{linea(re.sub(r"^([-*]|\d+\.) ", "", l))}</li>')
            else:
                cerrar(); out.append(f'<p>{linea(l)}</p>')
        cerrar()
    return ''.join(out)


LD = re.compile(r'<script type="application/ld\+json">.*?</script>', re.S)
def ld(*objs): return ''.join(f'<script type="application/ld+json">{json.dumps(o, ensure_ascii=False)}</script>' for o in objs)
ORG = {'@context': 'https://schema.org', '@type': 'Organization', 'name': 'Truly Nolen Chile', 'url': f'{SITIO}{CL}',
       'logo': f'{SITIO}/tn-emblema.png', 'telephone': TEL, 'areaServed': {'@type': 'Country', 'name': 'Chile'}}
if BLOG:
    for p in (DOCS / 'blog/fotos').glob('*'):
        if any(a['cover_url'] == p.name for a in BLOG): shutil.copy2(p, CHILE / 'assets' / p.name)
    PLANTILLA_ART = comun(leer('blog/como-eliminar-el-comejen'))
    for i, a in enumerate(BLOG):
        url = f'{CL}blog/{a["slug"]}/'
        cuerpo = md_a_html(a['content_md'])
        idx = ''.join(f'<li><a href="#art-{k}">{h}</a></li>' for k, h in enumerate(re.findall(r'<h2 id="art-\d+">(.*?)</h2>', cuerpo), 1))
        faqs = ''.join(f'<details class="ux-answer"{" open" if k == 0 else ""}><summary><h3>{e(q["q"])}</h3></summary><article><p>{e(q["a"])}</p></article></details>'
                       for k, q in enumerate(a['faqs']))
        if faqs: cuerpo += f'<h2 class="sin-num">Preguntas frecuentes</h2><div class="s-prose">{faqs}</div>'
        hay_foto = (DOCS / 'blog/fotos' / a['cover_url']).exists()
        if not hay_foto: print(f'  aviso: {a["slug"]} sin portada ({a["cover_url"]})')
        cred = (f' <small class="s-credito"><a href="{a["credito"][1]}" rel="license noopener" target="_blank">{e(a["credito"][0])}</a></small>'
                if a.get('credito') else '')
        fig = (f'<figure class="s-figure"><img src="{CL}assets/{a["cover_url"]}" alt="{e(a["og_alt_text"])}"/><figcaption>{e(a["og_alt_text"])}{cred}</figcaption></figure>') if hay_foto else ''
        # Sin créditos visibles (receta, Anexo E): la licencia va en portadaOrigen. Excepción: una foto CC BY lleva su crédito
        # en el pie, porque la licencia lo exige (campo «credito»: [texto, enlace a la licencia]).
        minutos = max(1, math.ceil(len(a['content_md'].split()) / 200))
        otros = [b for b in BLOG if b is not a]
        sig = (f'<section class="wrap closeout-blog-next"><div><p class="closeout-blog-eyebrow">Seguir leyendo</p><h2>{e(otros[0]["title"])}</h2>'
               f'<a class="text-link" href="{CL}blog/{otros[0]["slug"]}/">Leer el artículo →</a></div><a class="text-link" href="{CL}blog/">Ver todos los artículos →</a></section>') if otros else ''
        contenido = (f'<section class="wrap s-intro"><nav aria-label="Ruta"><a href="{CL}">Inicio</a><span aria-hidden="true">/</span><a href="{CL}blog/">Blog</a><span aria-hidden="true">/</span>{e(a["tema"])}</nav><h1>{e(a["title"])}</h1>{fig}</section>'
                     f'<section class="wrap s-section s-prose"><p class="s-note">Truly Nolen Chile · {fecha_larga(a["fecha"])} · {minutos} min de lectura</p><p class="s-entrada">{e(a["excerpt"])}</p></section>'
                     f'<nav class="wrap s-index ux-index" aria-label="En este artículo"><details><summary>En este artículo</summary><ul>{idx}</ul></details></nav>'
                     f'<section class="wrap s-section s-article"><div class="article-body">{cuerpo}</div></section>'
                     + fuentes(a['fuentes']) + sig + CIERRE)
        t = cabeza(LD.sub('', main(PLANTILLA_ART, contenido)), f'blog/{a["slug"]}/', f'{a["title"]} · Truly Nolen Chile', a['meta_description'])
        if hay_foto:
            t = re.sub(r'(<meta (?:property="og:image"|name="twitter:image") content=")[^"]*', lambda m: m.group(1) + f'{SITIO}{CL}assets/{a["cover_url"]}', t)
            t = re.sub(r'(<meta property="og:image:alt" content=")[^"]*', lambda m: m.group(1) + e(a['og_alt_text']), t)
            t = re.sub(r'<meta property="og:image:(?:width|height)" content="[^"]*"/>', '', t)
        t = t.replace('</head>', ld(ORG,
            {'@context': 'https://schema.org', '@type': 'BlogPosting', 'headline': a['title'], 'description': a['meta_description'],
             'datePublished': a['fecha'], 'inLanguage': 'es', **({'image': f'{SITIO}{CL}assets/{a["cover_url"]}'} if hay_foto else {}),
             'author': {'@type': 'Organization', 'name': 'Truly Nolen Chile'}, 'publisher': {'@type': 'Organization', 'name': 'Truly Nolen'}},
            {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q['q'], 'acceptedAnswer': {'@type': 'Answer', 'text': q['a']}} for q in a['faqs']]},
            {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
                {'@type': 'ListItem', 'position': 1, 'name': 'Inicio', 'item': f'{SITIO}{CL}'},
                {'@type': 'ListItem', 'position': 2, 'name': 'Blog', 'item': f'{SITIO}{CL}blog/'},
                {'@type': 'ListItem', 'position': 3, 'name': a['title'], 'item': f'{SITIO}{url}'}]}) + '</head>', 1)
        guardar(f'blog/{a["slug"]}', t)
    # Índice del blog
    historias = ''.join(
        f'<article class="journal-story"><div class="story-edition"><span>{k:02d}</span><time datetime="{a["fecha"]}">{fecha_larga(a["fecha"])}</time><span class="story-topic">{e(a["tema"])}</span></div>'
        f'<div class="story-copy"><h2><a href="{CL}blog/{a["slug"]}/">{e(a["title"])}</a></h2><p>{e(a["excerpt"])}</p><a class="text-link" href="{CL}blog/{a["slug"]}/">Leer el artículo <span aria-hidden="true">→</span></a></div>'
        + (f'<a class="story-image-link" href="{CL}blog/{a["slug"]}/" tabindex="-1" aria-hidden="true"><figure class="story-image"><img src="{CL}assets/{a["cover_url"]}" alt="" loading="lazy"/></figure></a>' if (DOCS / 'blog/fotos' / a['cover_url']).exists() else '')
        + '</article>' for k, a in enumerate(BLOG, 1))
    contenido = (f'<section class="wrap journal-wrap"><nav aria-label="Ruta"><a href="{CL}">Inicio</a><span aria-hidden="true">/</span>Blog de control de plagas</nav>'
                 '<header class="journal-heading"><h1>Blog de control de plagas</h1><p class="s-prose">Guías sobre las plagas de Chile, con cada dato respaldado por su fuente.</p></header></section>'
                 f'<section class="wrap journal-wrap"><div class="journal-stories">{historias}</div></section>' + CIERRE)
    t = cabeza(LD.sub('', main(comun(leer('blog')), contenido)), 'blog/', 'Blog de control de plagas · Truly Nolen Chile',
               'Guías sobre las plagas de Chile, con cada dato respaldado por su fuente.')
    guardar('blog', t.replace('</head>', ld(ORG) + '</head>', 1))

# ---------------------------------------------------------------- 8. sitemap, raíz y rutas relativas
paginas = sorted(p.parent.relative_to(CHILE).as_posix() for p in CHILE.rglob('index.html'))
(CHILE / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                                   + ''.join(f'<url><loc>{SITIO}{CL}{"" if r == "." else r + "/"}</loc></url>\n' for r in paginas) + '</urlset>\n', encoding='utf-8')
(OUT / 'index.html').write_text('<!doctype html><html lang="es"><head><meta charset="utf-8"/><meta name="robots" content="noindex,nofollow"/>'
                                '<meta http-equiv="refresh" content="0; url=oficinas/chile/"/><title>Truly Nolen Chile</title></head>'
                                '<body><a href="oficinas/chile/">Truly Nolen Chile</a></body></html>\n', encoding='utf-8')
(OUT / '.nojekyll').write_text('')

# GitHub Pages sirve el sitio en /truly-inbound-chile/: toda ruta que empieza con / se vuelve relativa a la página.
LOCAL = re.compile(r'(?<=["\'(])/(oficinas|machotes|landing|tn-emblema\.png)')
for f in OUT.rglob('*.html'):
    prof = len(f.parent.relative_to(OUT).parts)
    pre = '../' * prof if prof else './'
    t = f.read_text(encoding='utf-8')
    t = LOCAL.sub(lambda m: pre + m.group(1), t)
    f.write_text(t, encoding='utf-8')

# ---------------------------------------------------------------- 9. que no quede nada de Venezuela
resto = []
for f in OUT.rglob('*.html'):
    for m in re.finditer(r'(?i)venezuel\w*|caracas|chiripa|bachaco|comej[eé]n|alacr[aá]n|pipote|tobos?\b|wa\.me', f.read_text(encoding='utf-8')):
        resto.append(f'{f.relative_to(OUT)}: {m.group(0)}')
# Receta, vuelta 5 b: ninguna frase de 8 palabras o más sale dos veces en la misma página. Se mira el texto propio
# del contenido: fuera quedan el menú y el pie, el índice «En esta página» y las migas (repiten títulos a propósito),
# las citas de fuente, y la copia heredada de globaltni (que ya se repite sola en Venezuela; sí se avisa si nuestro
# texto repite una frase de esa copia).
def texto(t):
    t = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', t, flags=re.S)
    return re.findall(r'[\wáéíóúüñÁÉÍÓÚÜÑ]+', html.unescape(re.sub(r'<[^>]+>', ' ', t)).lower())
def ochos(pal): return [' '.join(pal[i:i + 8]) for i in range(len(pal) - 7)]
repetidas = []
for f in sorted(CHILE.rglob('index.html')):
    m = re.search(r'<main id="contenido">(.*?)</main>', f.read_text(encoding='utf-8'), re.S).group(1)
    copia = ''.join(re.findall(r'<div class="(?:gt-copia|ct-commercial)">.*?(?=<section class="wrap s-section s-flow" id="chile">)', m, re.S))
    propio = m.replace(copia, ' ') if copia else m
    propio = re.sub(r'<(nav|details class="pest-index")[^>]*>.*?</(nav|details)>|<small class="s-fuente">.*?</small>|<section class="wrap s-section s-fuentes">.*?</section>|<section id="cobertura".*?</section>', ' ', propio, flags=re.S)  # la lista de sucursales repite teléfonos y resoluciones: son datos
    de_copia, vistas, dobles = set(ochos(texto(copia))), set(), set()
    for g in ochos(texto(propio)):
        if g in vistas or g in de_copia: dobles.add(g)
        vistas.add(g)
    if dobles: repetidas.append(f'{f.relative_to(OUT)}: {len(dobles)} · ' + ' | '.join(sorted(dobles)[:4]))
print(f'{len(paginas)} páginas en {CHILE.relative_to(RAIZ)}')
if repetidas: print('Frases de 8+ palabras repetidas en la misma página:'); print('\n'.join(repetidas))
if resto:
    print('QUEDA de Venezuela:'); print('\n'.join(sorted(set(resto))))
    sys.exit(1)
print('sin restos de Venezuela')
