import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.styles.styles import Size as Size
from link_bio.components.info_text import info_text


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(name="Brandon Bustos", size="xl"),
            rx.vstack(
                rx.text(
                    "Brandon Bustos",
                    size="lg"
                ),
                rx.text(
                    "@lineasdecodigo",
                    margin_top="0px ! important"
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
        rx.text("""
                Soy tecnologo en sistemas y desarrolladore de software desde hace 3 años, Trabajo con lenguajes de 
                programacion como C#, Python y Java.
                Bienvenid@!!
                """),
        spacing=Size.BIG.value,
        align_items="start"
    )
