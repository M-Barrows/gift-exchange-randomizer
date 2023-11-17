import dash
from dash import html
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO
from theme.config import (LIGHT_THEME_TEMPLATE, LIGHT_THEME_URL, DARK_THEME_TEMPLATE, DARK_THEME_URL)

def make_navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("Settings", header=True),
                    dbc.Col(ThemeSwitchAIO(aio_id="theme", themes=[LIGHT_THEME_URL, DARK_THEME_URL],icons={"left" :"fa fa-moon", "right" :"fa fa-sun"}),class_name='ms-3'),
                    dbc.DropdownMenuItem("Made With ❤️ By:", header=True),
                    dbc.DropdownMenuItem("🧑‍💻Code|Coffee☕", href="https://codecoffee.org"),
                ],
                nav=True,
                in_navbar=True,
                label="More",
            ),
        ],
        brand="Secret Gift Pairing Generator",
        brand_href="/",
        color="primary",
        dark=True,
        class_name='mb-3'
    )
    return navbar


