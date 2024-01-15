import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size


def link_button(title: str, body: str, url: str, img: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=img,
                    width=Size.LARGE.value,
                    height=Size.LARGE.value,
                    margin=Size.MEDIUM.value,
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    spacing=Size.SMALL.value,
                    align_items="start",
                    padding_y=Size.SMALL.value,
                    padding_right=Size.SMALL.value
                ),
                width="100%",
                id="button_content"
            )
        ),
        href="https://reflex.dev",
        is_external=True,
        width="100%"
    )
