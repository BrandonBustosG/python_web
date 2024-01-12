import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TexColor


def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.span(
                "brandon",
                color=Color.PRIMARY.value
            ),
            rx.span(
                "bustos",
                color=Color.SECONDARY.value
            )
        ),
        rx.text(
            "Lineas de codigo",
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        z_index="999",
        top="0"
    )
