import reflex as rx


def link_icon(url: str) -> rx.Component:
    return rx.link(
        rx.icon(
            tag="link"
        ),
        href=url,
        button=True,
        is_external=True,
    )
