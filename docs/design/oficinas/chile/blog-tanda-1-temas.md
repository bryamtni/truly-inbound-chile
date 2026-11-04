# Blog de Chile · temas para la tanda 1 (borrador, 2026-11-04)

Para el paso 11 y el Anexo E de `truly-inbound`. Todavía no se escribió ningún artículo: falta la receta `blog-verificado` (escritor, juez de voz, auditor de verdad, revisión final, `lt.py`), la ficha de marca `truly-chile.{json,md}` y la carpeta de la tanda. Esta lista solo deja los temas listos, cada uno atado a una fuente que ya se leyó y se auditó para las páginas de plagas.

Reglas que valen para todos: usted en todo; nada de «hasta 100 %», sucursales (21/22/23), «35 años» ni cifras de clientes; nada que diga que la oficina hace algo que no publica (ver `preguntas-para-la-oficina.md`); sin «presencial» ni «caza de palomas» como servicio de la oficina; la portada, una foto REAL de la plaga (primero Truly; si no, Commons solo en dominio público o CC0), nunca generada.

## Formato de `tanda-1.txt` (`NN|palabra clave|nota`)

```
01|hantavirus ratón colilargo Chile|MINSAL 28-jul-2026: 2026 46 contagios y 18 fallecidos (39 %); 2025 44 y 8 (18 %); alerta hasta 31-jul-2027. Prevención y síntomas según la nota. Sin nombre científico del ratón.
02|araña de rincón mordedura Chile|Guía MINSAL 2016 (Loxosceles laeta; dentro de casas urbanas y rurales). Atribuir cuadros al género. Qué hacer ante una mordedura según la guía. Es arácnido, no insecto.
```

## Los 2 primeros (los que salen a goteo, 2 por día)
| # | Tema | Por qué primero | Fuente ya leída | Cuidado |
|---|---|---|---|---|
| 01 | Hantavirus y ratón colilargo: qué dice el MINSAL | Alerta sanitaria vigente hasta el 31-jul-2027; es lo que más busca la gente | MINSAL, nota 28-jul-2026 (reabierta) | Cifras tal cual, con fecha de corte; sin nombre científico; «acudir de inmediato a un centro de salud e informarlo al personal médico» es cita del MINSAL |
| 02 | Araña de rincón: cómo reconocerla y qué hacer ante una mordedura | Vive dentro de casas; la guía del MINSAL es clara y abierta | Guía MINSAL 2016 (copia alojada en la Universidad Mayor) | Atribuir al género *Loxosceles* mientras no se determine la especie; letalidad 1-3 % del loxoscelismo y 20-25 % en el cuadro cutáneo visceral |

## De reserva (tanda 2)
| # | Tema | Fuente ya leída | Cuidado |
|---|---|---|---|
| 03 | Termitas subterráneas en Santiago y Valparaíso: qué se sabe | Karsulovic et al. 2008: 80 focos en 29 comunas (1997-1998); V Región de 30 a 56 focos (2002-2004) | Cifras de INTEC-INFOR e INIA vía el artículo; la especie «se trataría» de *Reticulitermes flavipes* (condicional); no usar el dato del SAG de 1985 |
| 04 | Cucaracha alemana en La Serena y Coquimbo: el primer registro formal | Pérez 2015: 30 ejemplares (adultos y juveniles), oct-dic 2013 | Los contenedores son donde se observó, no donde se recolectó cada ejemplar; la cifra de patógenos es de Faúndez y Carvajal (2011), «puede llegar a portar y transmitir» |
| 05 | Programa preventivo de plagas: qué exigen el DS 977/96 y el DS 594 | DS 977/96 arts. 47 y 48; DS 594 art. 11; DS 157/2005 arts. 85 y 101 | Reabrir la BCN antes de publicar para fijar la versión consolidada; el art. 48 limita el tratamiento, no toda erradicación; el art. 85 es para plaguicidas de uso especializado |
| 06 | Dengue en Isla de Pascua: lo que informó el MINSAL | MINSAL 20-nov-2019 y 29-ene-2026 | Caso DEN-2 importado, no transmisión local; no decir «establecido» ni «erradicado» |

## Lo que no se usa como tema
- Palomas: la nota de la Res. SAG 718/2016 es de un caso particular (una empresa, solo Tarapacá); no da para artículo general. Riesgos sanitarios de palomas: sin fuente chilena oficial.
- Cualquier artículo que obligue a afirmar un servicio de la oficina sin respuesta (araña de rincón, Aedes aegypti, captura de palomas) queda a la espera de `preguntas-para-la-oficina.md`.

## Qué hace falta para escribirlos
1. La receta `blog-verificado` (la pide el dueño).
2. Ficha de marca `truly-chile.{json,md}` (copiar la de Nicaragua y cambiar todo; la voz sale de `voz-humana/voz-card.md`).
3. Carpeta `~/proyectos/blogs/truly-chile/tanda-1/` con `tanda-1.txt`, `blog-settings.json` y `posts-existentes.json`.
4. Foto real de portada para cada tema (Truly primero; si no, Commons PD o CC0).
5. El repo, para montar `blog/<slug>.json` y pasar `gate-oficinas`.
