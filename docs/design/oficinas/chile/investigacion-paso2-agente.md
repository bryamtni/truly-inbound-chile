# Chile · investigación paso 2 (entrega del agente, para revisar e integrar)

Fecha de lectura: 2026-11-02. No toca `investigacion.md` ni `sitio-actual/`.
Cómo se leyó: el sitio de la oficina con `curl` (texto literal de la página, no resumen); los decretos desde el XML oficial de la BCN (`bcn.cl/leychile/consulta/obtxml?opt=7&idNorma=…`), que trae el texto consolidado y el campo `derogado`; las fotos se descargaron y se miraron una por una. Lo que solo vi en un resumen de búsqueda lo marco **(no verificado)**.

---

## 2. Trato · cómo escribe LA OFICINA (trulynolen.cl)

**Hallazgo principal: la oficina mezcla «tú» y «usted».** «Tú» en lo que habla al hogar y al formulario; «usted» en lo institucional y de empresa. No hay voseo ni «vosotros» en texto propio.

| # | Cita corta (literal) | Trato | Página |
|---|---|---|---|
| 1 | «¿Tienes un problema de plagas?» / «…se pondrá en contacto contigo» | tú | https://trulynolen.cl/contacto-truly-nolen-chile/ |
| 2 | «¡Contáctanos y únete a millones de clientes satisfechos!» | tú (imperativo) | https://trulynolen.cl/ |
| 3 | «¡COTIZA AQUÍ EL MEJOR SERVICIO DEL MERCADO!» | tú (imperativo) | https://trulynolen.cl/programa-teps/ |
| 4 | «Usted no tendrá que molestarse en llamarnos.» | usted | https://trulynolen.cl/truly-nolen-por-que-elegirnos/ |
| 5 | «Consulte sobre los planes preventivos y curativos» | usted | https://trulynolen.cl/trulynolen-servicios/ |
| 6 | «…que le llevará la gestión en prevención y control de plagas de su negocio…» | usted | https://trulynolen.cl/ |

- **Giros chilenos que usa la oficina:** «zancudos» (servicios, insectos voladores), «polillas», «sanitización», «colaboradores», «cotiza aquí», «de Arica a Chiloé».
- **Aviso de lectura:** en la portada hay testimonios con «vuestros clientes» y «vuestra empresa» (vosotros peninsular). Son cartas de clientes, no la voz de la oficina. No copiarlos como trato.
- **Voseo chileno («podís», «tenís», «sabís»):** ninguna aparición en las 8 páginas leídas (portada, contacto, servicios, por qué elegirnos, TEPS, protección ambiental, nuestra empresa, noticias).
- **Corrección a una lectura anterior:** la frase «Protección Total para tu empresa y hogar» que devolvió un resumen automático NO está en el HTML de la portada. No usarla.
- **Cifra nueva que se contradice con el paso 1:** la portada dice «Más de 4.000 clientes» y «Más de 22 sucursales» (https://trulynolen.cl/); «Nuestra empresa» dice «más de 21 oficinas» y la tabla lista 23. Hay tres cifras distintas.
- **Propuesta `tratoVetado` (decisión del dueño):**
  - Vetar: «vos», voseo verbal («podís», «tenís», «querís»), «vosotros/vuestro/vuestra», «os», y mezclar «tú» y «usted» dentro de una misma pieza.
  - Decisión pendiente: la oficina hace «tú» para hogar y formulario, «usted» para empresas. Si el sitio nuevo es de un solo trato, lo más cercano a lo que ya dice la oficina es **«tú» en portada, formulario y hogar, y «usted» en las páginas de empresa/TEPS**; si se quiere uno solo, hay que elegirlo con la oficina.

---

## 3. Plagas con nombre local y fuente

Orden: las que más importan al cliente de la oficina. Solo cifras que leí en la fuente.

| Plaga (nombre local) | Especie | Dónde pesa | Dato (año) | Fuente |
|---|---|---|---|---|
| **Ratón colilargo** (roedor silvestre, reservorio de hantavirus; también rural y semirural) | El MINSAL no da el nombre científico en la nota (Oligoryzomys longicaudatus no confirmado) | «Casi todo el país»; casos 2026 en Valparaíso, Metropolitana, O'Higgins, Maule, Ñuble, Biobío, La Araucanía, Los Ríos, Los Lagos y Aysén | 2025: 44 contagios y 8 fallecidos (letalidad 18 %). 2026 hasta la semana previa al 28-jul-2026: 46 contagios y 18 fallecidos (39 %). Alerta sanitaria «desde Atacama hasta Magallanes», «vigente hasta el 31 de julio de 2027» | MINSAL, 28-jul-2026: https://www.minsal.cl/ministerio-de-salud-declara-alerta-sanitaria-por-hantavirus-desde-atacama-a-magallanes/ |
| **Araña de rincón** (araña de los rincones) | *Loxosceles laeta* | «Principalmente desde la primera a la octava región», con casos en todo el país; 86,6 % de los casos de Santiago 1955-88 ocurrió dentro de la casa | Letalidad 1-3 % del total y 20-25 % en el cuadro cutáneo-visceral; guía 2016 | MINSAL, Depto. Enfermedades Transmisibles, «Guía para el Manejo de Mordedura de Araña de los Rincones», 2016 (copia alojada en https://postgrados.umayor.cl/wp-content/uploads/2020/02/Guía-para-el-Manejo-de-Mordedura-de-Araña-de-los-Rincones-Loxosceles-laeta.pdf). Casos Santiago: Schenone et al., 1989, https://revistas.usp.br/rimtsp/article/view/28696 |
| **Termita subterránea** | *Reticulitermes* (especie discutida: *R. hesperus* en reportes antiguos; *R. flavipes* según el artículo de 2008; un estudio de la U. de Talca no pudo asignar la especie, **no verificado**) | Región Metropolitana y V Región | 80 focos en 29 comunas de Santiago (prospección 1997-1998). V Región: de 30 a 56 focos entre 2002 y 2004 | Karsulovic et al., *Maderas. Ciencia y Tecnología* 10(2), 2008 (U. de Chile; cita INTEC-INFOR 1997 e INIA 2004): https://www.redalyc.org/pdf/485/48510203.pdf |
| **Cucaracha alemana** (en la literatura chilena también «barata») | *Blattella germanica* | Citada para Santiago, Isla de Pascua y Magallanes; primer registro formal en Coquimbo y La Serena (muestras oct-dic 2013, junto a restaurantes y contenedores de basura) | 30 ejemplares colectados en 2013; sin cifras de prevalencia | N. Pérez, *Biodiversity and Natural History* 1(2), 2015: http://www.biodiversnathist.com/index.php/bnh/article/download/14/19 |
| **Zancudo / mosquito** (*Aedes aegypti*) | *Aedes aegypti* | Isla de Pascua (Rapa Nui) | 20-nov-2019: el ISP confirma un caso de dengue DEN-2, el primero de ese serotipo en la isla; control del vector en todas las viviendas del área de riesgo | MINSAL: https://www.minsal.cl/isp-confirma-caso-de-dengue-en-isla-de-pascua/ (la nota dice «mosquito»; «zancudo» lo usa la oficina, sin fuente oficial aquí) |
| **Paloma** (paloma doméstica) | *Columba livia* (la resolución escribe «Columbia livia») | Zonas urbanas; el ejemplo es Tarapacá | La captura o caza en área urbana la autoriza el SAG, no la empresa: Res. Ex. 718/2016, Iquique, 05-jul-2016, vigencia 2 años, aviso previo de 5 días hábiles, carné de caza vigente | SAG: https://www.sag.cl/sites/default/files/718_2016_t.pdf (cita la Ley 19.473 art. 7; no la abrí en leychile) |
| **Hormiga argentina** | *Linepithema humile* | Chile central (estudio precordillerano) | Sin cifra | Solo fuente comercial y un estudio de 2010 visto en resumen: **débil, no usar sin segunda fuente** |

- **Araña del trigo no es la araña de rincón.** El pedido las unía. La araña del trigo es *Latrodectus* (INIA nombra *L. mactans*; otra fuente, *L. thoracicus*), de campos de cultivo, con letalidad 0-6 % según ARS Medica (https://arsmedica.cl/index.php/MED/article/view/1003; **no verificado**, solo resumen de búsqueda). Para clientes agroexportadores puede importar; la oficina no la menciona.
- **Chinche de cama:** solo hay una nota de prensa (El Desconcierto, 23-mar-2025, https://eldesconcierto.cl/2025/03/23/chinches-de-cama-plaga-que-afecto-a-cathy-barriga-resurge-y-es-dura-de-matar-por-resistencia-a-quimicos/) que habla de «resurgimiento»; sin cifra oficial. No la pongo en la tabla.
- **Termita y la oficina:** su página dice que el SAG detectó la especie en 1985 (https://trulynolen.cl/termitas-subterraneas/). Es afirmación de la oficina; no la encontré en ninguna fuente chilena independiente. Una fuente de la propia oficina no sustenta la cifra.
- **Termitas nativas:** el artículo de 2008 dice que antes solo había dos familias en Chile (Kalotermitidae y Termopsidae) y que la subterránea (Rhinotermitidae) llegó después. Sirve para la sección «termitas de madera seca vs subterráneas» de la oficina.

---

## 4. Normas (texto leído hoy en la BCN)

Todas figuran **«no derogado»** en el XML oficial leído el 2026-11-02.

| Norma | Dato y vigencia | Artículo y numeral (lo que dice) | Fuente |
|---|---|---|---|
| **DS 157/2005 MINSAL**, «Reglamento de pesticidas de uso sanitario y doméstico» | Promulgado 22-jul-2005, publicado 30-jun-2007; idNorma 262263; versión única, no derogado | Art. 1: regula registro, fabricación, importación, venta, aplicación y eliminación. Art. 4: el ISP registra y las SEREMI emiten certificados. Art. 81: los plaguicidas de venta especializada solo los aplican empresas autorizadas por la autoridad sanitaria. Art. 83: avisar a la autoridad con 5 días hábiles en lugares de uso público, superficies mayores de 5.000 m², cuarta aplicación del año o más, y (solo con aviso previo) en establecimientos de salud, educacionales, salas cuna, jardines infantiles, hogares de ancianos y de menores. Art. 84: fumigantes con 3 días hábiles de aviso. Art. 85: diagnóstico antes de cada aplicación, con certificado. Art. 95: autorización sanitaria de la SEREMI, dura 3 años y se renueva sola. Art. 96: antecedentes (plano, equipos de protección, nómina con capacitación vigente). Art. 100: registros. Art. 101: certificado al cliente al terminar. Art. 104: responsable técnico con título profesional de 8 semestres. Art. 107: fiscalizan las SEREMI y el ISP (Libro Décimo del Código Sanitario). Art. 108: deroga el DS 105/1998 | https://www.leychile.cl/navegar?idNorma=262263 |
| **DS 977/96 MINSAL**, Reglamento Sanitario de los Alimentos | Publicado 13-may-1997; idNorma 71271; versión consolidada 2026-06-19 | Art. 40: impedir el acceso de plagas a los desechos. Art. 47: «programa preventivo eficaz y continuo de lucha contra las plagas», con inspección periódica del establecimiento y su entorno. Art. 48: la erradicación con agentes químicos, físicos o biológicos solo «por empresas autorizadas» por la autoridad sanitaria. Art. 49: plaguicidas solo si otras medidas no bastan. Art. 50: prohíbe mantener plaguicidas en zonas de producción, envase y almacenamiento | https://www.leychile.cl/navegar?idNorma=71271 |
| **DS 594 MINSAL**, condiciones sanitarias en lugares de trabajo | Publicado 29-abr-2000; idNorma 167766; versión 2026-01-16 | Art. 11: tomar «medidas efectivas para evitar la entrada o eliminar la presencia de insectos, roedores y otras plagas de interés sanitario». Art. 22: el empleador mantiene los baños protegidos de vectores. Art. 122: lo mismo en baños, cocinas, comedores y dormitorios | https://www.leychile.cl/navegar?idNorma=167766 |
| **Ley 19.473 (Caza), art. 7** | Citada por la Res. Ex. SAG 718/2016: la captura en área urbana la puede autorizar el SAG para controlar animales que dañan | Sin abrir en leychile | https://www.sag.cl/sites/default/files/718_2016_t.pdf |

- **Para la oficina:** el art. 85 y el art. 101 del DS 157 (diagnóstico y certificado) y el art. 48 del DS 977 (empresa autorizada) son los que el cliente puede exigir; la oficina ya publica «resoluciones sanitarias por sucursal» (paso 1).
- **DS 6/2009 (residuos):** es el reglamento de residuos de **establecimientos de atención de salud** (promulgado 23-feb-2009, publicado 04-dic-2009, según la BCN). No aplica a una empresa de plagas; no cito numeral. El de residuos peligrosos es el DS 148/2003 (no lo abrí).
- **Distinto del DS 157:** el DS 158 es de plaguicidas agrícolas (no lo abrí).
- **SAG:** la nota de palomas es de fauna (Ley de Caza), no de plaguicidas; no atribuir al SAG nada sobre roedores o insectos.

---

## 5. Negocios típicos y división territorial

**División oficial** (BCN): 16 regiones, 56 provincias, 346 comunas. Fuente: https://www.bcn.cl/siit/nuestropais/div_pol-adm.htm (la página no trae fecha). Nombres tal como los lista la BCN, de norte a sur: Arica y Parinacota, Tarapacá, Antofagasta, Atacama, Coquimbo, Valparaíso, Libertador B. O'Higgins (nombre abreviado en la BCN: confirmar el nombre completo antes de escribirlo), Maule, Ñuble, Biobío, La Araucanía, Los Ríos, Los Lagos, Aysén, Magallanes y Antártica Chilena, Metropolitana de Santiago.

| Tema | Qué decir | Fuente |
|---|---|---|
| Cómo nombrarlas | «Región de X» (con «de»); «Región Metropolitana»; «comuna», no «municipio»; ciudades por comuna | BCN, ver arriba |
| Cifras que ya no sirven | Statoids da 57 provincias y un metadato del INE de 2016 da 54: ambas viejas **(no verificado)** | resumen de búsqueda |
| Números romanos | **No** los verifiqué en esta pasada; la oficina escribe «XVI Región» para Valdivia (error del paso 1). Antes de usar romanos hay que confirmar con la BCN | — |
| Código postal | Existe: 7 dígitos por vivienda, lo administra CorreosChile, se consulta con comuna, calle y número | ChileAtiende ficha 892: https://www.chileatiende.gob.cl/fichas/892-codigo-postal |
| ¿Útil para el sitio? | No para «cobertura» (es por vivienda, no por comuna). Solo serviría en la dirección de la oficina; la oficina no lo publica | — |

**Negocios típicos.** Cifras de exportaciones de 2025 (Banco Central, vía prensa; no encontré el cuadro oficial):

| Sector | Dato 2025 | Fuente |
|---|---|---|
| Total exportado | US$ 107.004 millones (+7,9 % sobre 2024); el artículo cita al Banco Central | El Dínamo, 07-ene-2026: https://www.eldinamo.cl/economia/negocios-economia/2026/01/07/cobre-y-cerezas-impulsan-exportaciones-chilenas-y-logran-ano-record-en-2025/ |
| Minería | US$ 63.253 millones (59,1 % de los bienes) | idem (el artículo no nombra la fuente de esta cifra) |
| Fruta | US$ 8.630 millones; cerezas US$ 3.380 millones | idem (sin fuente propia) |
| Alimentos | US$ 13.610 millones | idem (sin fuente propia) |
| Salmón (SalmonChile) US$ 6.549 millones; vino embotellado US$ 1.298 millones (-3,7 %) | **(no verificado)**, solo en resumen de búsqueda | nota de prensa sin abrir |

- Para plagas, el vínculo con la norma es el DS 977 (alimentos, agroexportación, salmonicultura, vitivinícola, retail de alimentos) y el DS 594 (cualquier lugar de trabajo, incluidas faenas mineras; la oficina cita un testimonio de un campamento minero).
- **No encontré:** cifras oficiales de hotelería y retail; y el cuadro anual del Banco Central.

---

## 6. Lugares para la portada

**Resultado honesto: ninguna foto que vi cumple los tres criterios a la vez.** Las miré una por una (descargadas de Pexels). Licencia de Pexels: gratuita, uso comercial permitido, sin atribución obligatoria; prohíbe vender copias sin modificar, redistribuir como stock y sugerir respaldo de personas o marcas (https://www.pexels.com/license/). En Wikimedia Commons no hallé ninguna foto CC0 ni de dominio público con el volcán y una carretera (todo lo que apareció era CC BY-SA). Unsplash no se pudo leer.

Leyenda: C1 = ícono que se ve y el chileno reconoce; C2 = asfalto despejado, sin tierra, vallas, tráfico ni barrios humildes; C3 = calle en diagonal de abajo-izquierda a arriba-derecha, monumento a un lado del fondo, no al final.

| Lugar (zona) | Por qué el chileno lo reconoce | Foto (página, autor, fecha, licencia) | C1 | C2 | C3 |
|---|---|---|---|---|---|
| **Volcán Osorno, Ruta 5 (Los Lagos, sur)** | Es el volcán de postal del sur; la página nombra «Osorno Volcano» | **A.** https://www.pexels.com/photo/road-leading-towards-a-snowcapped-volcano-mountain-osorno-15191378/ · Rodrigo Araya · tomada 23-dic-2022 · Pexels | **Sí** | **Sí** (asfalto limpio, sin vallas ni tráfico; bermas de pasto) | **No**: recta y vertical, volcán justo al final |
| idem | idem | **B.** https://www.pexels.com/photo/gray-asphalt-road-in-between-brown-trees-14925850/ · Alexis Leandro Jeria Bocca · tomada 06-nov-2018 · Pexels | **Sí** (el volcán domina el cuadro) | **Parcial**: asfalto limpio, pero se ven postes, veredas, cartel y un auto estacionado al fondo | **No**: recta, volcán al fondo y al final |
| idem | idem | **C.** https://www.pexels.com/photo/scenic-landscape-with-a-view-of-a-volcano-15085895/ · Alexis Leandro Jeria Bocca · tomada 21-feb-2022 · Pexels | **Incierto**: la página dice «Ensenada» pero no nombra el volcán; yo no puedo confirmar cuál es | **Parcial**: asfalto con parches y una berma de tierra a la derecha (falla «sin tierra») | **Parcial, la más cercana**: el camino sube desde abajo-izquierda hacia la derecha y el volcán queda al lado, no al final; cielo nublado |
| **Valle de la Luna / San Pedro de Atacama (norte)** | Es el paisaje del norte grande | https://www.pexels.com/photo/asphalt-road-between-mountains-13531656/ y https://www.pexels.com/photo/gray-asphalt-road-beside-brown-rocky-mountain-13531655/ (autor y fecha: no abrí las páginas) | **No**: no se ve ningún ícono; solo cerros rojizos. La página dice «San Pedro de Atacama», no nombra Valle de la Luna | **Sí** (asfalto despejado y sin tierra; en 13531656 hay señales) | **Parcial**: la calzada curva desde abajo-izquierda hacia el fondo-centro; sin monumento |
| idem | idem | https://www.pexels.com/photo/gray-asphalt-road-under-blue-sky-13544657/ | **No** | **Sí** | **No**: recta al horizonte |
| **Santiago: Gran Torre Costanera (centro)** | El edificio más alto de Sudamérica; lo reconoce todo chileno | https://www.pexels.com/photo/gran-torre-santiago-skyscraper-in-chile-s-capital-29032777/ · página no abierta (autor sin confirmar; la búsqueda dio «Willian Justen de Vasconcellos», no verificado) | **Sí** (Gran Torre con la cordillera) | **No aplica**: no hay carretera ni calle | **No**: no hay calle |
| Santiago: camino a la cordillera | — | https://www.pexels.com/photo/scenic-road-with-andes-mountains-in-santiago-chile-34004183/ · DΛVΞ GΛRCIΛ · 22-sep-2025 · Pexels | **No** (cordillera sin ícono) | **No** (vallas y postes a los lados) | **No** (recta al final) |
| **Costa Viña del Mar / Concón (centro)** | Costa de la V Región, muy reconocible | https://www.pexels.com/photo/road-on-sea-coast-15203397/ (página no abierta; la búsqueda la titula como Viña del Mar) | **Débil**: se ve una duna y la costa; no puedo confirmar el lugar | **Sí** (camino costero limpio) | **No**: toma aérea y la calzada corre de abajo-derecha a arriba-izquierda (al revés) |
| **Torres del Paine (sur)** | Ícono de la Patagonia | https://www.pexels.com/photo/scenic-view-of-the-torres-del-paine-massif-in-patagonia-chile-25067987/ (sin carretera) | **Sí** | **No aplica** | **No aplica** |
| idem | idem | https://www.pexels.com/photo/empty-road-in-countryside-in-argentina-17370375/ | **No**: el título dice «Argentina» y no se ven las torres | **No** (camino de gravilla, con señales y alambrado) | **No** |
| **Carretera Austral** | Ruta emblema del sur austral | https://www.pexels.com/photo/straight-road-near-trees-13557956/ (la búsqueda la ubicó en Puerto Varas, no en la Austral) | **No** | **Sí** (asfalto limpio) | **No** (recta al final) |

- **No encontré:** una foto de la Carretera Austral comprobada ni de Valparaíso (el icono sería la costanera o los cerros); tampoco una de Villarrica con carretera (las 14 que hay no traen camino).
- **Lo que haría falta:** una foto de ruta con el Osorno o el Villarrica al costado y la calzada en diagonal, con asfalto limpio. No existe en lo que revisé. Opciones: probar otras búsquedas en Pexels/Unsplash, o fotografiarla (la receta pide fotos propias).

---

## Lo que no encontré
- Un nombre local comprobado para *Rattus norvegicus* y *Rattus rattus* («guarén» u otro); ninguna cifra oficial de ratas urbanas. Hay un estudio (Rubio y Villaseñor, 2023, centro de Chile) que solo vi por título.
- Cifras de casos de loxoscelismo posteriores a 2016 (MINSAL/DEIS) y datos del ISP sobre arañas.
- Datos oficiales de chinche de cama, hormiga, mosca, pulga y garrapata para Chile.
- Datos de Aedes aegypti en Arica con fuente oficial (solo prensa 2024, sin abrir).
- Texto de la Ley 19.473 art. 7 en leychile.
- Números romanos de las regiones y el nombre completo de la región de O'Higgins.
- El cuadro oficial del Banco Central y cifras de hotelería y retail.
- WhatsApp, correo y horario de la oficina (sigue pendiente del paso 1).

---

## Resumen para decidir (10 líneas)
1. **Trato:** la oficina usa «tú» (hogar, formulario) y «usted» (empresa, institucional); sin voseo. Decidir si el sitio nuevo parte de «tú» con «usted» solo en empresas.
2. **Vetar:** voseo («podís»), «vosotros/vuestro» y mezclar tú/usted en una misma pieza.
3. **Plagas del menú corto:** ratón colilargo (hanta, MINSAL 2026), araña de rincón (guía MINSAL 2016), termita subterránea (80 focos Santiago 1997-98), cucaracha alemana, zancudo (Rapa Nui, 2019), paloma (autoriza el SAG).
4. **Cuidado:** la «araña del trigo» no es la de rincón; la oficina dice «SAG detectó termitas en 1985» sin fuente independiente.
5. **Normas que sirven al cliente:** DS 157 arts. 85, 95, 101 (diagnóstico, autorización, certificado) y DS 977 art. 47-48 (programa de plagas, empresa autorizada); todas vigentes hoy en la BCN.
6. **Territorio:** 16 regiones, 56 provincias, 346 comunas (BCN); el código postal es por vivienda y no sirve para cobertura.
7. **Negocios:** minería, fruta y alimentos pesan más en 2025; salmón y vino sin verificar.
8. **Portada, mejor candidato:** Osorno con Ruta 5 (foto A, `15191378`): cumple C1 y C2, falla C3.
9. **Más cerca de C3:** `15085895` (diagonal, volcán al lado), pero no confirma el volcán y tiene tierra en la berma.
10. **Ninguna foto cumple los tres criterios** (ni hay CC0 en Commons): decidir si se acepta la que cumple dos, se busca otra, o se toma una foto propia.

Archivo: `/Users/bvasquez/Developer/TNI/Proyectos/Truly Inbound/truly-inbound-chile/docs/design/oficinas/chile/investigacion-paso2-agente.md`
