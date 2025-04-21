
import dash
from dash import Dash, dcc, html, Input, Output, dash_table
import pandas as pd
import dash_bootstrap_components as dbc
import os

app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Load wheelset history data
history_df = pd.read_csv("wheelset_history.csv")

app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    html.Div(id="page-content")
])

@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def render_page_content(pathname):
    if pathname.startswith("/asset/"):
        serial = pathname.split("/")[-1]
        record = history_df[history_df["Wheelset Serial Number"] == serial]

        if record.empty:
            return html.H3("❌ No data found for serial number: " + serial)

        record_dict = record.iloc[0].to_dict()
        info = [html.P(f"{k}: {v}") for k, v in record_dict.items()]

        qr_path = f"/qrcodes/{serial}.png"

        return dbc.Container([
            html.H2(f"Wheelset Asset Viewer: {serial}"),
            html.Img(src=qr_path, style={"width": "150px"}),
            html.Hr(),
            html.Div(info)
        ])

    # Default page content
    return dbc.Container([
        html.H2("📊 Freight Wheelset Maintenance Dashboard"),
        html.P("Use the dashboard to upload wheelset data or navigate to an asset."),
        html.Hr(),
        html.H4("Available Assets:"),
        dash_table.DataTable(
            data=history_df.to_dict("records"),
            columns=[{"name": i, "id": i} for i in history_df.columns],
            page_size=10,
            style_table={"overflowX": "auto"}
        )
    ])

if __name__ == "__main__":
    app.run(debug=True)
