import reflex as rx
import datetime
from link_bio.styles.styles import Size as Size


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="favicon.ico",
        ),
        rx.link(
            f"©️ {datetime.date.today().year} BRANDON BUSTOS V1.",
            href="https://google.com",
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.text(
            "BUILDING SOFTWARE WITH ❤️ FROM COLOMBIA TO THE WORLD",
            font_size=Size.MEDIUM.value,
            margin_top="0px ! important"
        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,
        spacing=Size.DEFAULT.value,
    )
