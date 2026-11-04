# Ficha de Chile: notas del borrador (2026-11-04)

Archivo: `ficha-chile-borrador.json`. Va contra el Anexo C de la receta `truly-inbound`. Sin repo, no pasó por el generador ni por `gate-oficinas`.

## Qué quedó lleno y de dónde sale
| Campo | Valor | Fuente |
|---|---|---|
| `id`, `base`, `title` | `chile`, `chile`, «Chile» | `chile` ya es machote del catálogo (investigacion.md) |
| `chatIdioma`, `tratoVetado` | usted siempre | Decisión del dueño, 2-nov-2026 |
| `textos` | las 8 frases del diseño de oficinas pasadas a usted | Anexo C |
| `oficina.telefono`, `direccion` | +56 22 784 4400; Av. Presidente Kennedy 8028, Vitacura | trulynolen.cl, leído el 2-nov-2026 |
| `paginas` | 3 servicios y 6 plagas | borrador-paginas/ |
| `blog.porDia` | 2 | Anexo C |

## Qué falta (null) y quién lo da
| Campo | Qué falta | De quién depende |
|---|---|---|
| `oficina.whatsapp`, `correo`, `horario` | No los publica la oficina | Oficina (preguntas 1 en `preguntas-para-la-oficina.md`) |
| `legales.privacidad` | Existe en trulynolen.cl/politica-privacidad/; falta redactar la versión del sitio nuevo | Nosotros, la oficina aprueba |
| `legales.terminos`, `accesibilidad` | No existen; hay que redactarlos | Nosotros, la oficina aprueba |
| `landmark`, `localArea` | Dependen de la portada | Decisión de la portada |
| `headline`, `intro`, `chapter`, `focus`, `contacto` | Texto de portada y voz | Se generan contra `voz-humana/voz-card.md`, con medidor y juez (paso 12) |
| `pelicula`, `footer`, imágenes, `casaZonas`, `ruta.aprobado` | Video del carro, fotos y aprobaciones | Portada, creador visual, dueño |

## Para revisar a mano
- **Textos con «Conozca», «Elija», «Reconozca», «Entienda».** El Anexo C dice que «Conoce», «Reconoce», «Entiende» y «para ti» no los ve el candado. Yo los pasé a usted de todos modos («Conozca…», «para usted»). Se confirman mirando la portada.
- **`paginas.plagas`:** los slugs son los nombres de los archivos del borrador. Si el generador pide otros, se ajustan.
- **Un sitio o varios:** sin decidir. Esta ficha asume un solo sitio para el país, con la casa matriz.
- **Datos de contacto contradictorios** del sitio actual (Los Ángeles, Curicó/Talca, Casa Matriz, Valdivia): ver `investigacion.md`. Confirmar con la oficina antes de publicar sucursales.
- **Chat en español viene en tú** (límite conocido, Anexo J).
