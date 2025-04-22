import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

server = app.server

app.layout = dbc.Container([
    html.H2("🛠️ Freight Wheelset Maintenance Dashboard", className="mt-4"),
    dash.page_container
], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=True)
