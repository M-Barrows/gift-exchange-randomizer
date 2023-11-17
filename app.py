# app.py
# This is the main file for the Dash app

# Import the necessary modules
import dash
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from components.navbar import make_navbar
from theme.config import (LIGHT_THEME_TEMPLATE, LIGHT_THEME_URL, DARK_THEME_TEMPLATE, DARK_THEME_URL)

load_figure_template(['minty','solar'])

dbc_css = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.1/dbc.min.css"
)


app = dash.Dash(__name__, external_stylesheets=[LIGHT_THEME_URL,dbc_css], use_pages=True,url_base_pathname="/apps/secret-gift-pairing-generator/")
app.title = 'Secret Gift Pairing Generator'

app.layout = dbc.Container([
    make_navbar(),
    dash.page_container
],className='dbc dbc-ag-grid',fluid=True)


# Run the app on port 8080
if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8080, debug=False)
