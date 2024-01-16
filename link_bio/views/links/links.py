import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size


def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button(
            "Youtube",
            "canal principal, videos de programacion",
            "https://reflex.dev",
            "icons/youtube.svg"
        ),
        link_button(
            "Instagram",
            "informacion de proyectos y contenido",
            "https://reflex.dev",
            "icons/youtube.svg"
        ),
        link_button(
            "Discord",
            "chat de la comunidad",
            "https://reflex.dev",
            "icons/youtube.svg"
        ),
        link_button(
            "Telegram",
            "Compartir contenido",
            "https://reflex.dev",
            "icons/youtube.svg"
        ),
        title("Recursos"),
        link_button(
            "Youtube",
            "canal principal",
            "https://reflex.dev",
            "icons/youtube.svg"
        ),
        title("Contactos"),
        link_button(
            "Youtube",
            "canal principal",
            "https://reflex.dev",
            "icons/youtube.svg"
        ),
        width="100%",
        spacing=Size.MEDIUM.value
    )
