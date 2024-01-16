import reflex as rx
from enum import Enum
from .colors import Color as Color
from .colors import TextColor as TexColor
from .fonts import Font as Font, FontWeight

# Constans
MAX_WIDTH = "560px"


STYLESSHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"
]

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
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.BACKGROUND.value + "!important",
    rx.Heading:{
        "size" : "lg",
        "color": TexColor.HEADER.value,
        "font_family":Font.TITLE.value,
        "font_weight": FontWeight.MEDIUM.value,
    },
    rx.Button: {
        "width": "100%",
        "height": "100%",
        "padding": Size.MEDIUM.value,
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
    font_size=Size.LARGE.value,
    font_weight= FontWeight.LIGHT.value,
)

title_style = dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
)

button_title_style = dict(
    font_size=Size.DEFAULT.value,
    color=TexColor.HEADER.value,
    font_family=Font.TITLE.value,
    font_weight= FontWeight.MEDIUM.value,
)

button_body_style = dict(
    font_size=Size.MEDIUM.value,
    color=TexColor.BODY.value,
    font_weight= FontWeight.LIGHT.value,
)
