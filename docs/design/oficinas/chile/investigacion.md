# Chile · investigación (BORRADOR, sin repo)

Estado: paso 1 hecho en borrador el 2026-11-02. Pasos 2 en adelante pendientes. Sin el repo no se pudo mirar `franquicias.ts` ni correr `ruta-oficina.py`; el paso 1 NO está ✅ por la ruta.

## 1. Contacto y lo que el sitio nuevo tiene que hacer mejor

**Fuente:** https://trulynolen.cl (sitio de la oficina, leído el 2026-11-02). Texto guardado en `sitio-actual/`.

### Contacto (lo que la oficina pone AL FRENTE)
| Canal | Dato | Dirección |
|---|---|---|
| Central | +56 22 784 4400 («CASA MATRIZ CHILE») | cabecera y pie de todas las páginas |
| Dirección | Avenida Presidente Kennedy 8028, Vitacura, Santiago | /contacto-truly-nolen-chile/ |
| WhatsApp | NO lo publica | — |
| Correo | NO lo publica | — |
| Horario | NO lo publica | — |
| Sucursales | 23 ciudades, cada una con dirección y teléfono | /sucursales-trulynolen-chile/ |

Regla 2: no se inventa WhatsApp, correo ni horario. Si el dueño los consigue con la oficina, se agregan; mientras tanto la ficha lleva solo la central y la dirección, y el WhatsApp del chat es el de Truly AI.

### Legales
Solo existe **Políticas de privacidad** (https://trulynolen.cl/politica-privacidad/). No hay términos ni accesibilidad: el sitio nuevo tiene que redactarlos (la ficha pide las 3) y la oficina debe aprobarlos.

### Tipo de sitio
Chile tiene Casa Matriz y 23 sucursales. Por defecto (Anexo F): UN sitio del país con la central, y las sucursales nombradas en la cobertura. Falta que el dueño lo confirme.

### Lo que el sitio nuevo tiene que hacer mejor
- Los datos de contacto del sitio actual se contradicen: Los Ángeles repite la dirección de Concepción (Talcahuano); Curicó y Talca comparten dirección con dos grafías («Montucci» / «Montuca»); Casa Matriz aparece en un enlace con el teléfono de Arica (+56 58 225 1490); Valdivia sale como «XVI Región» (hoy es XIV, Los Ríos). Hay que confirmarlos con la oficina antes de publicar: hoy no sabemos cuál es el dato correcto.
- Cifras que no se pueden reusar sin fuente: «más de 21 oficinas» (la tabla lista 23 ciudades); «35 años en Chile» contra «en Chile desde 1990» (serían 36); «hasta 100 %» de las palomas; las cifras globales de la página «Nuestra empresa» (238 oficinas, 4.000 empleados) son de la red mundial.
- Noticias estancadas: 7 notas con fecha de 2025 pero de contenido de 2020.
- Sin formulario visible en la captura, sin garantías explícitas, sin cifras de plagas ni normas chilenas.
- Aprovechable (lo publica la oficina): las tres zonas de protección (verde, amarilla, roja), el programa TEPS y sus 4 componentes, la sanitización ambiental, los servicios por tipo de plaga, y las resoluciones sanitarias por sucursal.

### Nota sobre el catálogo
`chile` ya es uno de los 10 machotes del catálogo. El sitio de la oficina sería una ficha aparte (`chile.json`, `base: chile`) y el catálogo no se toca (regla 3).

## 2. Trato (cómo escribe LA OFICINA)
Pendiente. Primeras pistas del sitio actual: usa **tú** («¿Tienes un problema de plagas?», «Completa el formulario… contacto contigo»), con tono corporativo. Falta confirmarlo con más páginas.

## Decisiones del dueño (2026-11-02)
- **Trato: USTED en todo el sitio** (en Chile es lo más común al hablarle a otras empresas). `tratoVetado`: «tú», «Tú», «tu», «Tu», «tus», «Tus», «te», «Te», «puedes», «necesitas», «quieres», el voseo («podís», «tenís», «querís») y «vosotros/vuestro/vuestra/os». NO vetar «Indica», «Conoce», «Consulta». Pendiente al armar la ficha: las 8 frases del diseño de oficinas que vienen en tú (Anexo C) hay que pasarlas a usted en `textos`, y el chat en español viene en tú (límite conocido, Anexo J).
- **Plagas: las 6 propuestas** (ratón colilargo, araña de rincón, termita subterránea, cucaracha alemana, zancudo, paloma).
- **Portada: seguir buscando** (ninguna foto cumplió los tres criterios).
- **Uno o varios sitios:** sin decidir (se asume uno).

## 3 a 6 · Plagas, normas, negocios y territorio, lugares de portada
Ver `investigacion-paso2-agente.md` (entrega del agente, con cada dato y su fuente). Pendiente de decidir con el dueño: trato, plagas y lugar.

## Comprobación propia (2026-11-02)
Revisé contra la fuente, abriéndola yo:
- **Hantavirus (MINSAL, 28-jul-2026):** 2026, 46 contagios y 18 fallecidos (letalidad 39 %); 2025, 44 contagios y 8 fallecidos (18 %); alerta sanitaria vigente hasta el 31-jul-2027; regiones con casos de Valparaíso a Aysén. Coincide con la nota. El nombre científico del ratón colilargo no aparece en la nota: no se pone.
- **DS 157/2005 (texto de la BCN):** arts. 81, 85, 95 y 101 coinciden con lo que dice el agente.
- **DS 977/96:** arts. 47 y 48 coinciden (programa preventivo continuo; erradicación solo por empresas autorizadas).
- **DS 594:** art. 11 coincide.
- **Trato de la oficina:** coinciden las citas «Usted no tendrá que molestarse en llamarnos», «Consulte sobre los planes preventivos y curativos», «¿Tienes un problema de plagas?», «Contáctanos y únete a millones de clientes satisfechos» y «Más de 4.000 clientes». La oficina mezcla tú y usted.
- **Corrección al paso 1:** mi resumen de la página de contacto decía «35 años» y «21 oficinas»; la portada dice «más de 22 sucursales» y «más de 4.000 clientes». Hay tres cifras de sucursales (21, 22, 23): no se usa ninguna sin confirmar con la oficina.
No revisé aún (se quedan como no verificadas): guía MINSAL 2016 de la araña de rincón, Karsulovic 2008 (termitas), Pérez 2015 (cucaracha), nota ISP de dengue 2019, resolución SAG 718/2016, cifras de exportaciones 2025, y las fotos de portada (las miró solo el agente).
## Lo que no encontré
- WhatsApp, correo y horario de la oficina.
- Fuente interna (`franquicias.ts`, formulario de trulyinbound.ai): sin acceso al repo.
