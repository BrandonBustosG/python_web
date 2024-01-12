import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TexColor

# Constans
MAX_WIDTH = "560px"


# Sizes
class Size(Enum):
    ZERO = "0px ! important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    BIG = "2em"


# Styles
BASE_STYLE = {
    "background_color": Color.BACKGROUND.value + "!important",
    rx.Button: {
        "width": "100%",
        "heigth": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TexColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "_hover": {
            "background_color": Color.SECONDARY.value,
        }
    },
    rx.Link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

title_style = dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
    color=TexColor.HEADER.value
)

button_title_style = dict(
    font_size=Size.DEFAULT.value,
    color=TexColor.HEADER.value
)

button_body_style = dict(
    font_size=Size.SMALL.value,
    color=TexColor.BODY.value
)
