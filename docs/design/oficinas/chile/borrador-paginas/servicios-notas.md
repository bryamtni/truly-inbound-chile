# Notas de los 3 servicios (paso 10, borrador)

Archivos: `servicio-hogares.json`, `servicio-comercios.json`, `servicio-industria.json`. Estructura: `titulo`, `resumen`, `intro`, `imagen`, `bloques` {`tarjetas`, `tabla`, `cifras` (solo Hogares), `preguntas`, `fuentes`}.

## Pendiente de la oficina (detalle en `preguntas-para-la-oficina-servicios.md`)
- Precios, frecuencia de visitas, duración y plazos de cada servicio.
- Qué revisa el técnico paso a paso en la primera visita; productos usados.
- Condiciones del contrato anual (la oficina solo dice que vuelve sin costo adicional hasta controlar la plaga).
- Qué documentos entrega en cada servicio (diagnóstico, certificado) y en qué formato.
- Detalle de los 4 componentes de TEPS, indicadores del informe mensual, y qué parte de cada norma de inocuidad cubre.
- Datos de Chile para cucaracha y zancudo (la oficina los atiende, pero no hay fuente abierta verificada hoy; la nota de cucaracha de Pérez 2015 y la de dengue en Rapa Nui 2019 no se reabrieron).
- Foto real de Truly (`imagen`: «pendiente: foto real de Truly»).
- Alcance por sucursal / cobertura; WhatsApp, correo y horario.

## Afirmado que NO está en una fuente
Ninguna afirmación sin fuente en los textos públicos tras la auditoría del 2 de noviembre de 2026. Correcciones aplicadas: art. 85 (el certificado con el diagnóstico lo entrega la empresa al terminar, solo plaguicidas de uso especializado), art. 95 («autoridad sanitaria del territorio», sin nombrar SEREMI), art. 81 (personal capacitado), art. 11 del DS 594 («los lugares de trabajo», sin «empleador» ni «hoteles, tiendas y bodegas»), TEPS con la frase de la oficina («permite dar cumplimiento a todas las normativas existentes», atribuida a la oficina), rastreros vs voladores, «hasta el interior», «nebulización», «plantas y bodegas», «respaldo para las exigencias sanitarias» y «hoteles y tiendas» eliminados.
- Verificado: las páginas de la oficina (servicios, TEPS, por qué elegirnos, sucursales), la nota MINSAL de hantavirus, la guía MINSAL 2016 de la araña de rincón (copia alojada en la Universidad Mayor) y el XML consolidado de la BCN de los DS 157, 594 y 977 (DS 977 completo, 19,8 MB, versión 2026-06-19). Arts. 47 y 48 (DS 977), 81, 85, 95 y 101 (DS 157) y 11 (DS 594) coinciden con la paráfrasis; el art. 101 quedó verificado.
- Cucaracha: la oficina no nombra especies, solo «insectos rastreros». La viñeta de cucaracha de la tabla de hogares se quitó (no es del MINSAL ni la nombra la oficina); queda como pregunta para la oficina. Zancudo figura en los insectos voladores.
- No se usó: «hasta 100 %», 21/22/23 sucursales, 35 años, cifras de roedores/parásitos de la oficina, «millón de dólares» de termitas.
- Discrepancia anotada: la oficina escribe «Arica a Chaitén» en una página y «Arica a Chiloé» en otra; no se usa ninguna.
- Opción de la auditoría para TEPS: se eligió la variante fiel (a), con cita textual atribuida a la oficina.
- El FAQ sobre reemplazo de certificaciones ya no afirma que la certificación la otorga el organismo certificador (sin fuente); remite a la certificadora.
- Decisión de estilo: sin marcadores «pendiente» en el texto público; los datos faltantes están en `preguntas-para-la-oficina-servicios.md`. Solo `imagen` conserva «pendiente».

## URLs abiertas
- https://trulynolen.cl/trulynolen-servicios/
- https://trulynolen.cl/programa-teps/
- https://trulynolen.cl/truly-nolen-por-que-elegirnos/
- https://trulynolen.cl/termitas-subterraneas/
- https://www.minsal.cl/ministerio-de-salud-declara-alerta-sanitaria-por-hantavirus-desde-atacama-a-magallanes/
- https://postgrados.umayor.cl/wp-content/uploads/2020/02/Guía-para-el-Manejo-de-Mordedura-de-Araña-de-los-Rincones-Loxosceles-laeta.pdf
- https://www.bcn.cl/leychile/consulta/obtxml?opt=7&idNorma=262263 (DS 157, leído completo)
- https://www.bcn.cl/leychile/consulta/obtxml?opt=7&idNorma=167766 (DS 594, leído completo)
- https://www.bcn.cl/leychile/consulta/obtxml?opt=7&idNorma=71271 (DS 977, descargado completo y buscado con Python)

## 5-nov-2026 · tablas a prosa
La regla del paquete («nada de tablas en servicio, plaga o artículo: prosa como globaltni») pidió pasar a prosa las
tablas de los tres servicios. Se cambió `bloques.tabla` por `bloques.prosa` (secciones con título y párrafos) con los
mismos datos y las mismas citas; las notas «Fuente: trulynolen.cl…» salieron del texto (las fuentes siguen en la lista
de fuentes de cada página).
