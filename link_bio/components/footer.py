import reflex as rx
import datetime


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="favicon.ico", 
            width="100px", 
            height="auto"
        ),
        rx.text(f"©️ {datetime.date.today().year} BRANDON BUSTOS V1. BUILDING SOFTWARE WITH ❤️ FROM COLOMBIA TO THE WORLD")
    )