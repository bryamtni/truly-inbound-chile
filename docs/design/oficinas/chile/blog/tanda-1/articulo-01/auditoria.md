# Auditoría de verdad · artículo 01 «hantavirus ratón colilargo» (6-nov-2026)

(Informe del agente blog-auditor-verdad. Corrió en solo lectura; el orquestador guardó su contenido.)

## Veredicto: NO PUBLICABLE (10 frases a corregir + portada)

Fuentes abiertas en vivo:
- NOTA: https://www.minsal.cl/ministerio-de-salud-declara-alerta-sanitaria-por-hantavirus-desde-atacama-a-magallanes/ (28/07/2026)
- DIPRECE: https://diprece.minsal.cl/temas-de-salud/orden-alfabetico/hanta/
- TN-SERV: https://trulynolen.cl/trulynolen-servicios/
- TN-SUC: https://trulynolen.cl/sucursales-trulynolen-chile/

Conteo: 36 verdaderos, 4 falsos (filas 19, 40, 44, 46), 4 exagerados (7, 24, 27, 39), 2 de grafía (18, 26), 2 no publicables (portada).

## Hallazgos y reescrituras
- **R1 (exagerado):** la frase de las recomendaciones quita las condiciones de la NOTA («si han estado cerradas», «espacios sin uso»), y el «Por eso» es deducción propia.
  `["content_md","Por eso sus recomendaciones apuntan a ventilar antes de entrar, limpiar con agua y cloro y tapar la basura y resguardar los alimentos.","Sus recomendaciones incluyen ventilar la casa antes de entrar si estuvo cerrada, limpiar con agua y cloro los espacios sin uso, tapar la basura y resguardar los alimentos."]`
- **R2 (falso en la atribución, y grafía):** «no es un virus exclusivamente del verano» es de la subsecretaria Alejandra Pizarro, no de «el MINSAL». Además va «semirrurales».
  `["content_md","que habita las zonas rurales y semirurales de casi todo el país. La misma autoridad advierte que el hanta","que habita las zonas rurales y semirrurales de casi todo el país. La subsecretaria de Salud Pública, Alejandra Pizarro, advierte que el hanta"]`
- **R3 (exagerado):** según DIPRECE, sellar y ordenar casas, galpones, leñeras y bodegas va solo para quienes viven en áreas silvestres, rurales o semirrurales.
  `["content_md","A las casas, galpones, leñeras y bodegas, la autoridad les pide sellarlos y mantenerlos en orden.","A quienes viven en áreas silvestres, rurales o semirrurales, la autoridad les pide sellar y mantener en orden casas, galpones, leñeras y bodegas."]`
- **R4 (grafía):**
  `["content_md","Para quienes viven en áreas silvestres, rurales o semirurales, su página de hanta agrega","Para quienes viven en áreas silvestres, rurales o semirrurales, su página de hanta agrega"]`
- **R5 (exagerado):** las medidas de mascarilla, guantes, recipientes herméticos y exteriores limpios van solo para ese mismo público.
  `["content_md","Esa página también recomienda usar mascarilla y guantes al limpiar o desinfectar.","A ese mismo público, esa página le recomienda usar mascarilla y guantes al limpiar o desinfectar."]`
- **R6 (falso en la atribución, cita incompleta y grafía):** la cita es de Pizarro y sigue con «…para que puedan considerar el diagnóstico de hantavirus oportunamente».
  `["content_md","Si alguien los presenta y estuvo en zonas rurales o semirurales donde pudo haber ratones de cola larga, la indicación es «acudir de inmediato a un centro de salud e informarlo al personal médico».","Si alguien los presenta y estuvo en zonas rurales o semirrurales donde pudo haber ratones de cola larga, la subsecretaria Alejandra Pizarro indica que «debe acudir de inmediato a un centro de salud e informarlo al personal médico para que puedan considerar el diagnóstico de hantavirus oportunamente»."]`
- **R7 (exagerado):** TN-SERV habla de «defensa perimetral», no de que el plan «empiece» por el perímetro.
  `["content_md","un plan que empieza por el perímetro y busca mantener a los roedores fuera","un plan con una defensa perimetral que busca mantener a los roedores fuera"]`
- **R8 (falso):** varias sucursales comparten resolución (0227 para Arica, Iquique y la casa matriz; 1760 para Chillán, Concepción y Los Ángeles), y Curicó, Talca y Los Ángeles salen sin resolución. Es la misma frase que hoy está en «Términos» de la ficha.
  `["content_md","Cada sucursal opera con su propia resolución sanitaria, publicada con su número y fecha en la sección de cobertura del sitio.","Nuestras sucursales cumplen las resoluciones sanitarias de cada región, según publicamos en la sección de cobertura del sitio."]`
- **R9 (falso en la atribución):**
  `["faqs[0].a","Sí. El MINSAL, en la nota que publicó el 28 de julio de 2026, afirma que el hanta","Sí. En la nota que el MINSAL publicó el 28 de julio de 2026, la subsecretaria de Salud Pública, Alejandra Pizarro, afirma que el hanta"]`
- **R10 (atribución, condición recortada y grafía):** la condición de la fuente son los síntomas.
  `["faqs[2].a","Para quien estuvo en zonas rurales o semirurales donde pudo haber ratones de cola larga, el MINSAL pide «acudir de inmediato","Para quien estuvo en zonas rurales o semirrurales donde pudo haber ratones de cola larga y presenta fiebre, dolor muscular intenso y dificultad respiratoria, la subsecretaria de Salud Pública, Alejandra Pizarro, pide «acudir de inmediato"]`
- **R11:**
  `["faqs[2].a","Lo dice en la nota que publicó el 28 de julio de 2026.","Lo dijo en la nota que el MINSAL publicó el 28 de julio de 2026."]`
- **Portada (no publicable):** `cl-blog-hantavirus-raton-colilargo.webp` no existe todavía. Hay que elegirla, abrirla, pasarla por el veto y revisar `og_alt_text` contra la imagen.

## Lo verificado sin cambios
- **Cifras:** 46 contagios y 18 fallecidos (39 %), y 44 y 8 en 2025 (18 %), con fecha de corte. La alerta va de Atacama a Magallanes y rige hasta el 31-jul-2027. Coinciden las 10 regiones.
- **Vías de contagio y síntomas:** coinciden con DIPRECE.
- **Campaña:** «desratizar recintos» es de la campaña de DIPRECE y está bien atribuido.
- **Datos de la oficina:** los cebos, la casa matriz, Truly AI y las 3 zonas coinciden con TN-SERV y la ficha.
- **Enlaces:** los 3 enlaces internos existen.
