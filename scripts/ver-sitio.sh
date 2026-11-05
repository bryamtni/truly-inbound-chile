#!/bin/bash
# Levanta el sitio de Chile en local y lo abre en el navegador. Se detiene con Ctrl+C.
# Uso (desde la raíz del repo):  bash scripts/ver-sitio.sh            (puerto 8000)
#                                bash scripts/ver-sitio.sh 8123       (otro puerto)
# Si cambió un borrador, antes:  python3 -I scripts/armar_sitio_chile.py
cd "$(dirname "$0")/../sitio" || exit 1
PUERTO="${1:-8000}"
URL="http://127.0.0.1:$PUERTO/oficinas/chile/"
echo "Sitio de Chile en $URL  (Ctrl+C para detener)"
(sleep 1 && open "$URL") &
# Python de uv (el mismo de la receta) si está; si no, el python3 del sistema.
if [ -x "$HOME/.local/bin/uv" ]; then
  exec "$HOME/.local/bin/uv" run -q --python 3.12 --no-project python -m http.server "$PUERTO" --bind 127.0.0.1
fi
exec python3 -m http.server "$PUERTO" --bind 127.0.0.1
