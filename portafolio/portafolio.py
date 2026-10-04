"""Portafolio de Valentin Galeano Peralta hecho con Reflex.

Todo el contenido está en la sección DATOS. El diseño vive en assets/estilo.css.
No usa rx.State ni eventos del servidor: así se exporta como sitio estático y se aloja en Vercel sin backend.
"""
from datetime import datetime

import reflex as rx

E = rx.el  # elementos HTML: E.div, E.section, E.a ...

# ===================== DATOS: edita aquí =====================
NOMBRE_COMPLETO = "Valentin Galeano Peralta"
EMAIL = "galeanov019@gmail.com"
GITHUB = "https://github.com/Valentin-gp"
LINKEDIN = "https://www.linkedin.com/in/valentin-galeano-peralta-89a2632a7"

TECNOLOGIAS = ["Python", "Flask", "React", "Docker", "Linux", "MySQL", "Fundamentos de redes",
               "Cisco Packet Tracer", "Ciberseguridad", "GitHub", "Claude Code"]

HABILIDADES = {
    "Desarrollo": ["Python", "Flask", "React"],
    "Datos e infraestructura": ["MySQL", "Docker", "Linux"],
    "Redes y seguridad": ["Fundamentos de redes", "Cisco Packet Tracer", "Ciberseguridad"],
    "Herramientas": ["GitHub", "Claude Code"],
}

CAPTURAS = [  # (archivo en assets/, texto alternativo, pie, pestaña, ancho, alto)
    ("sgeu-login.png", "Pantalla de inicio de sesión del SGEU con logotipo de la UPAP",
     "Inicio de sesión único para estudiante, docente y administrador.", "Login", "360", "408"),
    ("sgeu-registro.png", "Formulario para registrar una nueva actividad de extensión",
     "El docente registra una actividad y descarga los documentos oficiales.", "Registro", "1107", "632"),
    ("sgeu-metricas.png", "Gráfico de dona con la participación por carrera",
     "Métricas del docente: participación por carrera.", "Métricas", "1155", "530"),
    ("sgeu-estadisticas.png", "Gráfico de barras con estadísticas generales de estudiantes, docentes y graduados",
     "Panel del administrador: estadísticas generales de la plataforma.", "Estadísticas", "980", "541"),
]

PASOS = [
    ("El docente propone", "Registra la actividad y adjunta la propuesta con el formulario oficial."),
    ("El administrador aprueba", "Revisa la propuesta y la acepta o la rechaza."),
    ("Se inscribe y se registra asistencia", "El docente inscribe a los estudiantes y sube lista de asistencia y evidencias."),
    ("El sistema suma las horas", "Cada estudiante ve su historial y su avance hacia las 90 horas."),
]

ESTUDIOS = [
    ("Ingeniería Informática", "UPAP, Luque · Cuarto año · Actualidad"),
    ("Bachiller Técnico en Contabilidad",
     "Colegio Nacional Izidoro Zaracho · 2020–2022 · Mención de Mejor Egresado"),
]
CERTIFICACIONES = [
    ("CCNA 1: Introducción a las Redes", "Cisco Networking Academy · En curso"),
    ("Python Essentials 1", "Cisco Networking Academy"),
    ("Programación con Python", "SNPP · 2024"),
    ("Introducción a la Ciberseguridad", "Cisco Networking Academy"),
    ("Linux Unhatched", "Instituto Tecnológico de Luque / Cisco Networking Academy"),
]


# ===================== Piezas reutilizables =====================
# Reflex convierte cada <a> en un Link de React Router; sin esto, "/cv.pdf" se trata como una página (404)
ARCHIVO = {"reloadDocument": True}


def t(texto, clase):
    return E.span(texto, class_name=clase)


def chips(items):
    return E.ul(*[E.li(i) for i in items], class_name="chips")


def boton(texto, href, principal=False, chico=False, descarga=False, fantasma=False):
    clase = "ghost" if fantasma else "btn" + ("" if principal else " alt") + (" sm" if chico else "")
    extra = {"download": True, "custom_attrs": ARCHIVO} if descarga else {}
    return E.a(texto, href=href, class_name=clase, **extra)


def linea_tiempo(items):
    return E.ul(*[E.li(E.b(a), E.small(b)) for a, b in items], class_name="tl")


def encabezado():
    return E.header(
        E.div(
            E.a("valentin", E.b("."), "dev", href="#inicio", class_name="logo"),
            E.nav(
                E.a("Proyecto", href="#proyecto"),
                E.a("Habilidades", href="#habilidades"),
                E.a("Formación", href="#formacion"),
                E.a("Contacto", href="#contacto"),
                class_name="links",
                custom_attrs={"aria-label": "Principal"},
            ),
            E.button("◐", class_name="tg", type="button", title="Modo claro/oscuro",
                     custom_attrs={"data-toggle-theme": "1", "aria-label": "Cambiar entre modo claro y oscuro"}),
            class_name="wrap",
        ),
        class_name="nav",
    )


def tarjeta_codigo():
    lineas = [
        [t("class ", "k"), t("Valentin", "f"), ":"],
        ["    rol   = ", t('"Estudiante de Ing. Informática"', "s")],
        ["    stack = [", t('"Python"', "s"), ", ", t('"Flask"', "s"), ", ", t('"React"', "s"), "]"],
        ["    infra = [", t('"Docker"', "s"), ", ", t('"Linux"', "s"), ", ", t('"MySQL"', "s"), "]"],
        ["    redes = ", t('"CCNA 1 (en curso)"', "s")],
        ["    idiomas = [", t('"es"', "s"), ", ", t('"gn"', "s"), ", ", t('"en básico"', "s"), "]"],
        ["    busca = ", t('"primera experiencia en equipo"', "s")],
        [""],
        ["    ", t("def ", "k"), t("contacto", "f"), "(self):"],
        ["        ", t("return ", "k"), t(f'"{EMAIL}"', "s"), E.span(class_name="cur")],
    ]
    cuerpo = []
    for ln in lineas:
        cuerpo.extend(ln)
        cuerpo.append("\n")
    return E.div(
        E.div(E.i(), E.i(), E.i(), E.span("perfil.py"), class_name="bar"),
        E.pre(*cuerpo),
        class_name="code",
        custom_attrs={"aria-label": "Resumen de perfil escrito como código Python"},
    )


def presentacion():
    return E.div(
        E.div(
            E.div(
                E.p(E.i(), " Luque, Paraguay · Cuarto año de Ingeniería Informática", class_name="pill"),
                E.h1("Valentin ", E.span("Galeano")),
                E.p("Desarrollo de software y redes", class_name="role"),
                E.p("Desarrollo aplicaciones web con Python, Flask y React, uso Docker y Linux, y me formo en "
                    "redes y ciberseguridad. Busco una primera experiencia profesional donde seguir "
                    "aprendiendo en equipo.", class_name="lead"),
                E.div(
                    boton("Ver mi proyecto", "#proyecto", principal=True),
                    boton("Descargar CV", "/cv.pdf", descarga=True),
                    E.span(boton("GitHub", GITHUB, fantasma=True), boton("LinkedIn", LINKEDIN, fantasma=True),
                           class_name="sub"),
                    class_name="actions",
                ),
                E.p("Correo: ", E.a(EMAIL, href=f"mailto:{EMAIL}"), class_name="mail-line"),
            ),
            tarjeta_codigo(),
            class_name="wrap",
        ),
        class_name="hero",
    )


def cinta():
    def fila(oculta=False):
        return [E.span(x, custom_attrs={"aria-hidden": "true"} if oculta else {}) for x in TECNOLOGIAS]
    return E.div(E.div(*fila(), *fila(True), class_name="track"), class_name="ticker", custom_attrs={"aria-hidden": "true"})


def galeria():
    radios = [E.input(type="radio", name="g", id=f"g{i}", default_checked=(i == 1))
              for i in range(1, len(CAPTURAS) + 1)]
    imagenes = [E.img(src=f"/{c[0]}", alt=c[1], width=c[4], height=c[5], class_name=f"pic p{i}")
                for i, c in enumerate(CAPTURAS, 1)]
    pies = [E.p(c[2], class_name=f"cap c{i}") for i, c in enumerate(CAPTURAS, 1)]
    pestanas = [E.label(c[3], html_for=f"g{i}") for i, c in enumerate(CAPTURAS, 1)]
    return E.div(
        *radios,
        E.div(E.i(), E.i(), E.i(), class_name="top"),
        E.div(*imagenes, class_name="stage"),
        E.div(*pies, class_name="capw", custom_attrs={"aria-live": "polite"}),
        E.div(*pestanas, class_name="tabs"),
        class_name="viewer",
        custom_attrs={"role": "radiogroup", "aria-label": "Capturas del sistema"},
    )


def demostracion():
    """Ventana con el video del SGEU; la abre y cierra assets/interacciones.js."""
    return E.dialog(
        E.div(
            E.p("Demostración del SGEU", class_name="vt"),
            E.button("✕", type="button", class_name="vx",
                     custom_attrs={"data-close-dialog": "1", "aria-label": "Cerrar video"}),
            class_name="vh",
        ),
        E.video(
            E.source(src="/sgeu-demo.mp4", type="video/mp4"),
            "Tu navegador no puede reproducir este video.",
            controls=True, preload="none", plays_inline=True,
        ),
        id="demo",
        class_name="vdlg",
        custom_attrs={"aria-label": "Video de demostración del SGEU"},
    )


def proyecto():
    info = E.div(
        E.p("Plataforma web para la UPAP, Filial Luque, que reemplaza las planillas y carpetas en papel. "
            "Registra actividades de extensión, asistencia y horas, y calcula el avance de cada estudiante "
            "hacia el requisito de egreso."),
        E.div(
            *[E.div(E.b(n), E.span(d), class_name="stat") for n, d in [
                ("11", "estudiantes en el equipo"), ("4", "roles de usuario"),
                ("90 h", "de extensión calculadas por el sistema"), ("3", "documentos oficiales digitalizados")]],
            class_name="stats",
        ),
        E.p(E.b("Mi participación: "),
            "entrevista de relevamiento inicial, diagramas y diseño de la base de datos, backend, frontend y "
            "propuesta del reglamento de extensión.", class_name="mine"),
        chips(["React 19", "Flask", "MariaDB", "Docker", "JWT"]),
        E.p("Proyecto universitario · Cátedra Desarrollo de Sistemas III · 2026", class_name="meta"),
        E.p("El código pertenece al equipo y no es público, pero puedes ver el sistema funcionando.", class_name="priv"),
        E.button("▶ Ver demostración", type="button", class_name="btn sm",
                 custom_attrs={"data-open-dialog": "demo"}),
        demostracion(),
        class_name="info",
    )
    return E.section(
        E.div(
            E.p("Proyecto destacado", class_name="kicker rv"),
            E.h2("SGEU: Sistema de Gestión de Extensión Universitaria", class_name="rv"),
            E.div(galeria(), info, class_name="proj rv"),
            E.p("Cómo funciona", class_name="flow-t rv"),
            E.ol(*[E.li(E.b(a), E.span(b)) for a, b in PASOS], class_name="flow rv"),
            class_name="wrap",
        ),
        id="proyecto",
    )


def habilidades():
    return E.section(
        E.div(
            E.p("Stack", class_name="kicker rv"),
            E.h2("Habilidades", class_name="rv"),
            E.div(*[E.div(E.h3(g), chips(v), class_name="sk") for g, v in HABILIDADES.items()],
                  class_name="skills rv"),
            class_name="wrap",
        ),
        id="habilidades",
    )


def formacion():
    return E.section(
        E.div(
            E.div(
                E.div(E.p("Estudios", class_name="kicker"), E.h2("Formación"),
                      linea_tiempo(ESTUDIOS), class_name="rv"),
                E.div(E.p("Cursos", class_name="kicker"), E.h2("Certificaciones"),
                      linea_tiempo(CERTIFICACIONES),
                      E.p("Lista completa en mi ", E.a("CV", href="/cv.pdf", custom_attrs=ARCHIVO), ".", class_name="note"),
                      class_name="rv"),
                class_name="two",
            ),
            class_name="wrap",
        ),
        id="formacion",
    )


def sobre_mi():
    return E.section(
        E.div(
            E.div(
                E.p("Sobre mí", class_name="kicker"),
                E.h2("Aprendo construyendo"),
                E.p("En la universidad participé en el desarrollo completo de una plataforma web para gestionar "
                    "la extensión universitaria, y fuera de ella complemento mi formación con cursos de "
                    "programación, redes, Linux e inteligencia artificial."),
                E.p("Valoro el trabajo en equipo, la organización y la comunicación clara."),
                class_name="rv",
            ),
            E.div(E.h3("Idiomas"), chips(["Castellano", "Guaraní", "Inglés básico"]), class_name="box rv"),
            class_name="wrap about",
        ),
        id="sobre-mi",
    )


def contacto():
    return E.section(
        E.div(
            E.div(
                E.h2("Hablemos"),
                E.p("Estoy buscando mi primera experiencia profesional. Escríbeme y respondo pronto."),
                E.a(EMAIL, href=f"mailto:{EMAIL}", class_name="mail"),
                E.div(
                    E.button("Copiar correo", type="button", class_name="btn", custom_attrs={"data-copy": EMAIL}),
                    boton("GitHub", GITHUB), boton("LinkedIn", LINKEDIN),
                    boton("CV", "/cv.pdf", descarga=True),
                    class_name="actions",
                ),
                class_name="cta rv",
            ),
            class_name="wrap",
        ),
        id="contacto",
    )


def index() -> rx.Component:
    return rx.fragment(
        E.a("Saltar al contenido", href="#inicio", class_name="skip"),
        encabezado(),
        E.main(
            presentacion(), cinta(), proyecto(), habilidades(), formacion(), sobre_mi(), contacto(),
            id="inicio",
        ),
        E.footer(E.div(f"© {datetime.now().year} {NOMBRE_COMPLETO}", class_name="wrap")),
    )


app = rx.App(
    html_lang="es",
    enable_state=False,  # sin backend: evita que el navegador intente abrir el WebSocket /_event cada segundo
    head_components=[rx.script(src="/interacciones.js")],
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@500;700;800&family=JetBrains+Mono:wght@400;600&display=swap",
        "/estilo.css",
    ],
)
app.add_page(
    index,
    route="/",
    title=f"{NOMBRE_COMPLETO} · Ingeniería Informática",
    description="Portafolio de Valentin Galeano Peralta, estudiante de Ingeniería Informática en Luque, "
    "Paraguay. Python, Flask, React, Docker y redes.",
    meta=[
        {"name": "theme-color", "content": "#f5f8f7", "media": "(prefers-color-scheme: light)"},
        {"name": "theme-color", "content": "#0a1016", "media": "(prefers-color-scheme: dark)"},
        {"property": "og:type", "content": "website"},
        {"property": "og:locale", "content": "es_PY"},
        {"property": "og:title", "content": f"{NOMBRE_COMPLETO} · Ingeniería Informática"},
        {"property": "og:description", "content": "Python, Flask, React, Docker y redes. Proyecto SGEU para la UPAP."},
    ],
)
