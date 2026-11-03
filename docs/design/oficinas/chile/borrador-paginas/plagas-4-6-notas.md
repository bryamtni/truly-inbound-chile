# Plagas 4-6 (cucaracha alemana, zancudo, paloma) · notas del paso 10

Fecha: 2026-11-02. Archivos: plaga-cucaracha-alemana.json, plaga-zancudo.json, plaga-paloma.json. Correcciones de `auditoria-plagas-4-6.md` aplicadas el mismo día. Los datos que faltan van en `preguntas-para-la-oficina-plagas-4-6.md`.

## Fuentes abiertas
| Fuente | Resultado |
|---|---|
| N. Pérez 2015, Biodiversity and Natural History 1(2) | CONFIRMADO: 30 ejemplares (adultos y juveniles), oct-dic 2013, La Serena y Coquimbo; recolectados de noche en las afueras de restaurantes del centro; los contenedores de basura son donde la autora observó muchos ejemplares, no donde se recolectó cada uno. Cita a Moroni y Camousseight (Santiago, Isla de Pascua; «años 70») y a Faúndez y Carvajal 2011 (Magallanes y la cifra de 22 bacterias, 2 protistas, 20 helmintos y 3 virus: «puede llegar a portar y transmitir»). |
| MINSAL 20-nov-2019, dengue Isla de Pascua (reabierta hoy) | CONFIRMADO: caso DEN-2 «importado», hombre de 55 años que adquirió el virus de viaje en Tahití; el primero de ese serotipo en la isla; «En mayo de este año se decretó Alerta Sanitaria»; «34 casos de dengue DEN 1 en la isla»; control del vector en todas las viviendas del área de riesgo. Se puso en tarjeta, cifras, tabla y FAQ, sin sugerir transmisión local del DEN-2. |
| Res. Ex. SAG 718/2016 | CONFIRMADO: una empresa (GREEN PEST CONTROL SPA), solo inmuebles de la Región de Tarapacá, dos años, aviso con cinco días hábiles, carné de caza solo a quien use rifle de aire comprimido, sin tóxicos. |
| Ley 19.473 art. 7 | CONFIRMADO en el XML de la BCN (idNorma 30840, versión 06-sep-2023; abre con curl). Se reemplazó la copia de la UACh por el XML. Se agregó la competencia del SBAP en áreas protegidas. |
| MINSAL 29-ene-2026 y 18-abr-2016 | CONFIRMADO (ver auditoría). Se agregó que en las tres primeras semanas de 2026 solo había tres casos importados. La recomendación de 2016 se atribuye a la población de Arica. |
| DS 977/96 art. 48, DS 157/2005 arts. 85 y 101 | Corregidos según la auditoría: el art. 48 limita el tratamiento (no toda erradicación) a empresas autorizadas; el art. 85 es para plaguicidas de uso especializado. |

## Datos descartados
- «Hasta 100 %» de palomas, sucursales, años de trayectoria y cifras de clientes: no se usan.
- Zancudo: no se afirma «establecido» ni «erradicado»; no se usa «ausente desde 1960».
- Riesgos sanitarios de palomas: sin fuente chilena oficial, no se dan.

## Decisiones donde no se siguió al pie de la letra la auditoría
- Sin «pendiente de la oficina» ni notas internas en los JSON (decisión de estilo 1): no aparece «no publica» ni «no indica». Por eso: (a) se omitió «La oficina no publica un servicio de captura ni caza»; el texto solo dice que la autorización en área urbana corresponde al SAG; (b) se omitió «La oficina no indica que trate específicamente Aedes aegypti»; basta con no afirmarlo (el zancudo se presenta solo como parte de insectos voladores); (c) se omitió «no publica detalle para la cucaracha alemana». Las tres dudas están en el archivo de preguntas.
- Resolución 718/2016: se describe como «autoriza la captura y caza de palomas (Columba livia) con fines de control, dentro de inmuebles», que es el título de la resolución. No se escribió «capturar y sacrificar palomas y gorriones» (instrucción del dueño de la marca); la fila sobre gorriones y el método quedan fuera.
- «Cómo reconocerla» del zancudo: en vez de cambiar a «reconocerlo» se renombró «Qué nombre usa cada fuente», porque MINSAL no describe cómo reconocerlo. Tarjetas de paloma: «Nombre», «Ejemplo revisado», «Qué pidió la empresa»; zancudo: «Hallazgos en Chile», «Qué informó MINSAL».
- «Según la oficina» queda una sola vez (TRULY PIGEONS AWAY: sistema que repele sin químicos y sin comprometer la infraestructura). «Insectos rastreros» y «zancudos» son listado de servicios y se dicen con la voz de la oficina («atendemos», «nuestro servicio»).
- Se quitó «Consulte en su oficina regional» (el SAG) hasta citar la web del SAG; se quitó «presencial» (no está publicado).
- Cifra de patógenos atribuida a Faúndez y Carvajal (2011), vía Pérez.

## Pendiente (solo en el archivo de preguntas)
Ver `preguntas-para-la-oficina-plagas-4-6.md`. Además: foto real de Truly (`imagen` e `imagenOrigen` dicen «pendiente» en los tres JSON).
