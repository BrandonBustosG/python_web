import reflex as rx

from link_bio.components.info_text import info_text
from link_bio.components.link_icon import link_icon
from link_bio.styles.colors import TextColor as TexColor
from link_bio.styles.colors import Color as Color
from link_bio.styles.styles import Size as Size


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Brandon Bustos",
                size="xl",
                src="",
                color=TexColor.BODY.value,
                bg=Color.CONTENT.value,
                padding="2px",
                border="4px",
                border_color=Color.PRIMARY.value
            ),
            rx.vstack(
                rx.heading("Brandon Bustos"),
                rx.text(
                    "@lineasdecodigo",
                    margin_top=Size.ZERO.value,
                    color=TexColor.BODY.value
                ),
                rx.hstack(
                    link_icon("https://x.com/brandonbustos"),
                    link_icon("https://x.com/brandonbustos"),
                    link_icon("https://x.com/brandonbustos"),
                ),
                align_items="start"
            ),
            spacing=Size.DEFAULT.value,
        ),
        rx.flex(
            info_text("+2", "años de experiencia"),
            rx.spacer(),
            info_text("+2", "años de experiencia"),
            rx.spacer(),
            info_text("+2", "años de experiencia"),
            width="100%"
        ),
        rx.text(
            """
            Soy tecnologo en sistemas y desarrolladore de software desde hace 3 años, Trabajo con lenguajes de 
            programacion como C#, Python y Java.
            Bienvenid@!!
            """,
            color=TexColor.BODY.value,
            font_size=Size.DEFAULT.value
        ),
        spacing=Size.BIG.value,
        align_items="start"
    )
