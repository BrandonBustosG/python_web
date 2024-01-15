import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TexColor
from .fonts import Font as Font

# Constans
MAX_WIDTH = "560px"


# Sizes
class Size(Enum):
    ZERO = "0px ! important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"


# Styles
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "background_color": Color.BACKGROUND.value + "!important",
    rx.Heading:{
        "size" : "lg",
        "color": TexColor.HEADER.value,
        "font_family":Font.TITLE.value
    },
    rx.Button: {
        "width": "100%",
        "heigth": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TexColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "white_space": "normal",
        "text_align": "start",
        "_hover": {
            "background_color": Color.SECONDARY.value,
        }
    },
    rx.Link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_size=Size.LARGE.value
)

title_style = dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
)

button_title_style = dict(
    font_size=Size.DEFAULT.value,
    color=TexColor.HEADER.value,
    font_family=Font.TITLE.value,
)

button_body_style = dict(
    font_size=Size.SMALL.value,
    color=TexColor.BODY.value,
)
