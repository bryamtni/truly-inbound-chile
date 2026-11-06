# Revisión SXO · artículo 01 · «hantavirus ratón colilargo»

Limitaciones: la SERP se aproximó con WebSearch agregando «Chile» (3 búsquedas de las 8 permitidas). No es la SERP real de Google Chile: no hay posiciones exactas, ni PAA, ni AI Overview, ni features visibles. No se renderizó la página con el script del skill (el encargo era solo leer el JSON). El puntaje SXO Gap Score completo de 7 dimensiones no se calculó, porque es un borrador sin URL publicada. Lo que sigue es una lectura cualitativa.

## Qué muestra Google (aproximación)

Resultados vistos para la búsqueda y variantes: 24horas.cl (alerta sanitaria, características del ratón), La Tercera (síntomas y prevención), Emol (ratón cola larga), U. de Chile (transmisión cepa Andes), ISL, MINSAL/Seremi, Rentokil Chile (página comercial «Ratón Colilargo · Principal vector del Hantavirus en Chile»), además de medios extranjeros.

- Tipo dominante: guía o nota informativa de medio o institución, cerca de 8 de 10 (confianza media, por ser aproximación). Un resultado comercial (Rentokil), que mezcla información y servicio de desratización.
- Intención: informacional de salud con ángulo de actualidad (alerta sanitaria, letalidad 39 %). Subintenciones: qué es el ratón y dónde vive, cómo se contagia, síntomas y cuándo consultar, qué hacer en casa.
- Tipo de la página: guía informativa con cierre comercial suave. Desajuste: ALINEADO. No hay hallazgo crítico.

## Historias de usuario (con la señal que las origina)

1. Persona con casa o bodega cerrada en zona rural: «¿cómo limpio y entro sin riesgo?». Señal: resultados de prevención de La Tercera, 24horas y Rentokil. La página responde (H2 3).
2. Persona preocupada por la alerta: «¿es grave, hay epidemia?». Señal: títulos sobre alerta sanitaria y letalidad. La página responde (H2 1, con la aclaración de que no hay epidemia en curso).
3. Persona con síntomas: «¿qué síntomas son y cuándo voy al médico?». Señal: La Tercera y U. de Chile. La página responde, pero el H2 es largo y no dice «síntomas del hantavirus» de forma directa.
4. Persona que ya vio un ratón: «¿puedo contratar a alguien?». Señal: Rentokil. La página responde (H2 5 y cierre).

## Personas (0 a 25 por relevancia, claridad, confianza y acción)

| Persona | Rel | Cla | Conf | Acc | Total | Mejora |
|---|---|---|---|---|---|---|
| Propietario rural con bodega o leñera | 23 | 20 | 22 | 20 | 85 | Ya cubierto. |
| Lector preocupado por la alerta | 24 | 22 | 24 | 17 | 87 | Sin dato nuevo posible. |
| Persona con síntomas | 20 | 16 | 23 | 18 | 77 | H2 de síntomas más directo (cambio 1). |
| Lector que busca «cómo se contagia» | 21 | 17 | 23 | 18 | 79 | H2 con la pregunta literal (cambio 2). |
| Cliente que quiere control de roedores | 22 | 20 | 18 | 21 | 81 | La confianza depende de datos de la oficina aún sin confirmar. |

Los más débiles son el lector de síntomas y el de contagio, y ambos se resuelven con títulos, sin datos nuevos.

## Brechas frente a la SERP que NO se pueden cerrar (sin respaldo en fuentes.md)

No se proponen porque no están en fuentes.md y serían datos nuevos: periodo de incubación, transmisión entre personas, cómo limpiar paso a paso (humedecer, no barrer en seco), trampas o cebos para uso doméstico, hábitat (quila, cerca del agua), cifras actualizadas posteriores al 28-jul. Si se quiere competir en ellas, hay que abrir y registrar primero la fuente (MINSAL/ISL) en fuentes.md. Frescura: las cifras son de julio y la SERP ya habla de agosto, así que conviene revisar la actualización de cifras en una pasada futura (duda 6 del auditor).

## Lo que ya funciona y no se toca

Palabra clave en título, entrada y H2 1 y 2. Entrada con respuesta directa. Frases aprobadas de la ficha. Aclaración «no implica epidemia». Cierre con teléfono y Truly AI. Enlaces internos sin enlaces externos.

## Tabla final de cambios

| campo | texto viejo (literal, aparece una sola vez) | texto nuevo | por qué | respaldo en fuentes.md |
|---|---|---|---|---|
| content_md (H2 4) | Con fiebre, dolor muscular intenso y dificultad respiratoria tras estar en zonas rurales, el MINSAL pide consulta inmediata | Síntomas del hantavirus y cuándo consultar: fiebre, dolor muscular intenso y dificultad respiratoria | El H2 actual tiene 19 palabras y no nombra «síntomas», que es la subintención más buscada. El nuevo es más corto, usa el término de búsqueda y sigue anunciando lo que dice el párrafo. | Filas 17 y 18 (síntomas y acudir de inmediato) |
| content_md (H2 3) | El contagio se concentra en lugares cerrados donde hubo ratones | Cómo se contagia el hantavirus: en lugares cerrados donde hubo ratones | Replica la pregunta «cómo se contagia», presente en los resultados de prevención, y mantiene el contenido del apartado. | Fila 2 (contagio en lugares cerrados con presencia reciente de ratones) y fila 12 |
