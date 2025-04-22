import dash
from dash import html
import dash_bootstrap_components as dbc

# Initialize app
app = dash.Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

server = app.server

# Main layout
app.layout = dbc.Container([
    html.H2("🛠️ Freight Wheelset Maintenance Dashboard", className="mt-4"),
    dash.page_container
], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=True)
