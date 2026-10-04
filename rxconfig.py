import reflex as rx

config = rx.Config(
    app_name="portafolio",
    plugins=[
        rx.plugins.RadixThemesPlugin(
            theme=rx.theme(appearance="inherit", accent_color="blue", radius="medium"),
        ),
        rx.plugins.SitemapPlugin(),
    ],
)
