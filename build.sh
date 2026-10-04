#!/bin/bash
# Compila el frontend de Reflex a archivos estáticos en /public (mismo enfoque que la plantilla de mouredev)
set -e
# En Vercel, apunta al propio dominio del sitio para que el navegador del visitante no intente conectarse a su "localhost".
if [ -n "$VERCEL_PROJECT_PRODUCTION_URL" ]; then export REFLEX_API_URL="https://$VERCEL_PROJECT_PRODUCTION_URL";
elif [ -n "$VERCEL_URL" ]; then export REFLEX_API_URL="https://$VERCEL_URL"; fi
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
rm -rf public
reflex export --frontend-only --no-zip
cp -r .web/build/client public
deactivate
