import reflex as rx
from link_bio.components.link_button import link_button

def links() -> rx.Component :
    return rx.vstack(
        link_button("Youtube","https://reflex.dev"),
        link_button("Instagram","https://reflex.dev"),
        link_button("Discord","https://reflex.dev"),
        link_button("Telegram","https://reflex.dev")
    )