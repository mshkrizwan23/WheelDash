import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.SLATE]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = dbc.Container([
    dbc.NavbarSimple(
        brand="🚆 Freight Wheelset Monitoring",
        color="primary",
        dark=True,
    ),
    dbc.Tabs([
        dbc.Tab(label="Overview", tab_id="overview"),
        dbc.Tab(label="Wheelset Status", tab_id="status"),
        dbc.Tab(label="Maintenance History", tab_id="history"),
    ], id="tabs", active_tab="overview"),
    html.Div(id="tab-content")
])

@app.callback(
    dash.dependencies.Output("tab-content", "children"),
    [dash.dependencies.Input("tabs", "active_tab")]
)
def update_tab(tab):
    if tab == "overview":
        return html.Div("Dashboard overview and KPIs go here.")
    elif tab == "status":
        return html.Div("Live wheelset condition status here.")
    elif tab == "history":
        return html.Div("Maintenance record table here.")

if __name__ == "__main__":
    app.run_server(debug=True)
