# Revisión GEO · artículo 01 · «hantavirus ratón colilargo»

Alcance: solo `articulo.json`. Sin llms.txt ni robots. Sin datos nuevos, sin filas ni viñetas nuevas, sin enlaces externos, palabra clave intacta.

## Diagnóstico

- Respuesta directa en las primeras 60 palabras: cumple. Fuente nombrada (MINSAL) en cada pasaje clave.
- Estructura: H2 que afirman, párrafos cortos, FAQ con pregunta y respuesta. Bien para Google AIO y Perplexity.
- Problema principal: varios pasajes dependen del párrafo o H2 anterior. Ejemplos: «esa nota», «la misma nota», «Abarca…», «No implica…», «La transmite…», «Esa misma página», «A ese mismo público», «Pide guardar…», «Menciona además…», «Lo hacemos…», «Nuestros técnicos», «la roja», «Lo dijo…». Un motor que extrae un solo párrafo no sabría de qué entidad habla (hantavirus, MINSAL, Truly Nolen Chile).
- Pasajes de 134-167 palabras: el artículo tiene secciones de 60-110 palabras. No se alargan, porque eso exigiría datos nuevos. La mejora es nombrar la entidad en cada pasaje.
- Se respetan máximo 3 oraciones por párrafo, sin punto y coma, y las frases atribuidas siguen separadas de las propias.

## Puntajes (estimados, antes de los cambios)

| Dimensión | Puntaje |
|---|---|
| Citabilidad | 68 |
| Legibilidad estructural | 82 |
| Multimodal | 45 (una portada con alt; sin tabla, video ni infografía; no se pueden añadir) |
| Autoridad y marca | 80 (fuentes oficiales con fecha; autor de marca sin firma individual) |
| Accesibilidad técnica | no evaluada (borrador noindex, fuera de alcance) |

Por plataforma, con los cambios aplicados: Google AIO 78, Perplexity 80, ChatGPT 72, Copilot 70.

## Tabla final de cambios

Todos los cambios son sobre `content_md` salvo los marcados `faqs[n]`.

| campo | texto viejo | texto nuevo | por qué |
|---|---|---|---|
| content_md | `Abarca desde la Región de Atacama hasta la de Magallanes y rige hasta` | `La alerta abarca desde la Región de Atacama hasta la de Magallanes y rige hasta` | Sujeto omitido: el pasaje no nombra qué abarca. |
| content_md | `explicó que la medida se tomó porque este año aumentó la letalidad del virus` | `explicó que la alerta se declaró porque en 2026 aumentó la letalidad del hantavirus` | Nombra la entidad y fija el año en lugar de «la medida» y «este año». |
| content_md | `Hasta la semana anterior a esa nota se registraban 46 contagios y 18 fallecidos, una letalidad del 39 %.` | `Hasta la semana anterior a la nota del MINSAL del 28 de julio de 2026 se registraban 46 contagios y 18 fallecidos por hantavirus, una letalidad del 39 %.` | «Esa nota» no se entiende solo. Se agrega fuente, fecha y enfermedad (todo ya en fuentes.md, filas 4 y 6). |
| content_md | `En 2025 hubo 44 contagios y ocho fallecidos, con una letalidad de 18 %.` | `En 2025 hubo 44 contagios y ocho fallecidos por hantavirus, con una letalidad de 18 %.` | La cifra citada sola debe nombrar la enfermedad. |
| content_md | `Según la misma nota, en lo que iba de 2026 hubo casos en Valparaíso` | `Según la nota del MINSAL del 28 de julio de 2026, en lo que iba de 2026 hubo casos de hantavirus en Valparaíso` | «La misma nota» depende del párrafo anterior. |
| content_md | `No implica que exista una epidemia en curso.` | `La alerta sanitaria no implica que exista una epidemia en curso.` | Frase sin sujeto: el motor no sabría a qué se refiere. |
| content_md | `La transmite el ratón de cola larga, que habita las zonas rurales y semirrurales de casi todo el país.` | `El ratón de cola larga, que habita las zonas rurales y semirrurales de casi todo el país, transmite el hantavirus.` | «La» solo se entiende con la oración anterior. |
| content_md | `La subsecretaria Pizarro advierte` | `La subsecretaria de Salud Pública, Alejandra Pizarro, advierte` | Nombre y cargo completos dentro del pasaje. |
| content_md | `La más importante es respirar gotas` | `La vía más importante del hantavirus es respirar gotas` | «La más importante» no dice más importante de qué. |
| content_md | `Otras vías son tocar objetos` | `Otras vías de contagio son tocar objetos` | Autocontenido, sin cambiar el sentido. |
| content_md | `Esa misma página indica que no existe evidencia de transmisión del virus por` | `La página de hanta del MINSAL indica que no existe evidencia de transmisión del hantavirus por` | «Esa misma página» exige el párrafo de arriba. Este dato suele extraerse solo. |
| content_md | `## El contagio se concentra en lugares cerrados donde hubo ratones` | `## El contagio de hantavirus se concentra en lugares cerrados donde hubo ratones` | El H2 es el ancla del pasaje y debe nombrar la enfermedad. |
| content_md | `Por eso la transmisión es poco frecuente` | `Por eso la transmisión del hantavirus es poco frecuente` | Nombra la entidad en la frase que se cita. |
| content_md | `la autoridad les pide sellar` | `el MINSAL les pide sellar` | «La autoridad» es vago. El MINSAL es la fuente de la fila 14. |
| content_md | `En su nota de julio, el MINSAL` | `En su nota del 28 de julio de 2026, el MINSAL` | Fecha completa, ya verificada. |
| content_md | `su página de hanta agrega ventilar por al menos 30 minutos` | `la página de hanta del MINSAL agrega ventilar por al menos 30 minutos` | «Su» depende de la oración anterior. |
| content_md | `A ese mismo público, esa página le recomienda usar mascarilla y guantes` | `A quienes viven en áreas silvestres, rurales o semirurales, la página de hanta del MINSAL les recomienda usar mascarilla y guantes` | Elimina «ese/esa». La condición ya estaba en el párrafo anterior y en la duda 3 de fuentes.md. |
| content_md | `Pide guardar alimentos y agua en recipientes herméticos y mantener los exteriores libres de basura y maleza.` | `La página del MINSAL también pide a quienes viven en esas áreas guardar alimentos y agua en recipientes herméticos y mantener los exteriores libres de basura y maleza.` | Frase sin sujeto. Se le da sujeto y condición de la fila 16. |
| content_md | `Si alguien los presenta y estuvo en zonas rurales` | `Si alguien presenta fiebre, dolor muscular intenso y dificultad respiratoria y estuvo en zonas rurales` | «Los» depende de la oración anterior. Es el pasaje más citable de salud y debe valer solo. |
| content_md | `Su página de hanta describe el síndrome pulmonar por hantavirus` | `La página de hanta del MINSAL describe el síndrome pulmonar por hantavirus` | «Su» no tiene antecedente dentro del pasaje. |
| content_md | `Menciona además calofríos,` | `La página del MINSAL menciona además calofríos,` | Frase sin sujeto. |
| content_md | `Lo hacemos con cebos rodenticidas de última generación` | `Truly Nolen Chile hace el control de roedores con cebos rodenticidas de última generación` | Nombra la marca y el servicio. Es lo que debe citar un motor ante «control de roedores Chile». |
| content_md | `Nuestros técnicos saben que las plagas buscan` | `Los técnicos de Truly Nolen Chile saben que las plagas buscan` | «Nuestros» no nombra a la marca. |
| content_md | `Por eso todo servicio parte con el plan de protección de las 3 zonas.` | `Por eso todo servicio de Truly Nolen Chile parte con el plan de protección de las 3 zonas.` | Marca dentro de la oración extraíble. |
| content_md | `la amarilla es la defensa final con el exterior para mantener las plagas fuera y la roja es la zona crítica` | `la zona amarilla es la defensa final con el exterior para mantener las plagas fuera y la zona roja es la zona crítica` | «La amarilla» y «la roja» no se entienden solas. |
| content_md | `Nuestras sucursales cumplen las resoluciones sanitarias de cada región` | `Las sucursales de Truly Nolen Chile cumplen las resoluciones sanitarias de cada región` | Marca nombrada. |
| faqs[2].q | `¿Qué hacer si aparecen síntomas después de estar en una zona rural?` | `¿Qué hacer si aparecen síntomas de hantavirus después de estar en una zona rural?` | La pregunta sola no dice de qué enfermedad. |
| faqs[2].a | `Lo dijo en la nota que el MINSAL publicó el 28 de julio de 2026.` | `La subsecretaria Pizarro lo dijo en la nota que el MINSAL publicó el 28 de julio de 2026.` | «Lo dijo» no tiene sujeto. |
| faqs[1].a | `También se contagia al ingerir agua o alimentos contaminados` | `La página de hanta del MINSAL agrega que el hantavirus también se contagia al ingerir agua o alimentos contaminados` | Sujeto y fuente dentro de la respuesta. |
| faqs[3].a | `Sí. Según su página de servicios en trulynolen.cl, el control de roedores es uno de sus servicios principales y se hace` | `Sí, Truly Nolen Chile hace control de roedores. Según la página de servicios de Truly Nolen Chile en trulynolen.cl, el control de roedores es uno de los servicios principales y se hace` | Respuesta directa con la marca en la primera oración. Quedan 3 oraciones. |

## Notas

- No se tocó la apertura (ya responde en menos de 60 palabras y lleva la palabra clave), ni H2 1, 2, 4 y 5, ni el cierre, ni la FAQ 1. FAQ 1 ya es autocontenida.
- No se tocaron las frases aprobadas de la ficha ni se cambió ninguna lista atribuida.
- Los cambios aumentan unas 90 palabras de repetición de entidad. Todos los datos ya están en fuentes.md (filas 4, 6, 7, 8, 9, 10, 12, 13, 14, 16, 18, 21 a 25).
- Riesgo a vigilar: las cifras del MINSAL son del 28 de julio de 2026 y pueden estar desactualizadas (duda 6 de fuentes.md). La fecha ahora está dentro del pasaje, lo que ayuda a que el motor las cite con su corte.
