# Portafolio de Valentin Galeano (Reflex)

Portafolio hecho con [Reflex](https://reflex.dev). El contenido está al inicio de `portafolio/portafolio.py`
y el diseño en `assets/estilo.css`.

## Probar en local
```bash
python -m venv .venv
.venv\Scripts\activate        # Windows  (Mac/Linux: source .venv/bin/activate)
pip install -r requirements.txt
reflex run                    # http://localhost:3000
```

## Probar la versión estática (la que se publica)
```bash
reflex export --frontend-only --no-zip
python -m http.server 8000 --directory .web/build/client     # http://localhost:8000
```

## Publicar en Vercel
Ver la guía paso a paso. Resumen: sube el repo a GitHub, impórtalo en Vercel y despliega.
`build.sh` exporta el frontend a `public` y `vercel.json` lo sirve como sitio estático.

## Importante
- El sitio no usa `rx.State`: modo oscuro, galería y botón de copiar funcionan con CSS y
  `assets/interacciones.js`. Los botones o formularios de Reflex que dependan del servidor no funcionarán.
- `assets/estilo.css` oculta el contenedor de avisos de Reflex ("Cannot connect to server").
- Todo lo que dice "Tu..." o enlaces a revisar está en `portafolio/portafolio.py` (sección DATOS).
