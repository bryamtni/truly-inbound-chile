# Auditoría de verdad · artículo 02 «termitas subterráneas en Chile» (6-nov-2026)

(Informe del agente blog-auditor-verdad. Corrió en solo lectura, así que el orquestador guardó su contenido.)

## Veredicto: NO PUBLICABLE hasta aplicar 4 reescrituras; con ellas, PUBLICABLE

Fuentes que el agente abrió hoy en vivo:
- K2008: https://www.redalyc.org/pdf/485/48510203.pdf (PDF completo)
- TN-SERV: https://trulynolen.cl/trulynolen-servicios/
- TN-SUC: https://trulynolen.cl/sucursales-trulynolen-chile/
- BCN Región de Valparaíso: https://www.bcn.cl/siit/nuestropais/region5
- Commons: https://commons.wikimedia.org/wiki/File:Reticulitermes_flavipes_K8085-6.jpg
- Wikipedia, Kalotermitidae

Conteo: 45 afirmaciones verdaderas, 2 exageradas (#14 y #46), 1 falsa (#49) y 1 de grafía (#10).

## Reescrituras
1. **#49, falso.** En la foto, la cabeza de los soldados es ámbar y solo las mandíbulas son oscuras.
   `["og_alt_text","con la cabeza oscura, sobre un fondo azul","de cabeza ámbar y mandíbulas oscuras, entre otras termitas claras, sobre un fondo azul"]`
2. **#46, atribución exagerada.** K2008 dice «actualmente se afirma que se trataría…»: recoge lo que otros afirman, no lo afirma.
   `["faqs[2].a","dice que se trataría de Reticulitermes flavipes.","dice que, a la fecha, se afirmaba que se trataría de Reticulitermes flavipes."]`
3. **#14, impreciso.** La fuente cuenta los focos en la Quinta Región, no en la ciudad.
   `["content_md","## Los focos se contaron por decenas en Santiago y en Valparaíso","## Los focos se contaron por decenas en Santiago y en la Región de Valparaíso"]`
4. **#10, grafía.** El nombre válido es Kalotermitidae. La bibliografía del mismo PDF y la guía del sitio lo escriben así, y el artículo parafrasea, no cita.
   `["content_md","Kalotermidae y Termopsidae","Kalotermitidae y Termopsidae"]`

## Lo verificado sin cambios
- **Datos del estudio:** 80 focos en 29 comunas (1997-1998, INTEC-INFOR); de 30 a 56 focos en la V Región (2002-2004, INIA). La especie va en condicional en el cuerpo, la introducción ocurrió en los setenta (Camousseight 1998) y las colonias estudiadas son de San Bernardo y Santiago.
- **Datos de la oficina:** los dos grupos de termitas, los tratamientos distintos, «cuanto antes se controlen es mejor», la prevención y las 3 zonas coinciden con TN-SERV.
- **Sucursales:** las de San Felipe, Viña del Mar y San Antonio, y la casa matriz en Vitacura, coinciden con TN-SUC y `sucursales.json`.
- **Lo que no está:** el artículo no trae señales de infestación, SAG 1985, «millón», «sin costo», precios, plazos ni garantías.
- **Enlaces y portada:** los 3 enlaces internos existen. La portada es de dominio público (USDA ARS) y no tiene textos ni marcas.

## Notas fuera del artículo
- El primer párrafo tiene 4 oraciones según el contador.
- La guía `plagas/termita-subterranea/` atribuye a la oficina las «señales de infestación» y cita como fuente la noticia https://trulynolen.cl/termitas-subterraneas/. Conviene revisarla aparte.
