import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd

dash.register_page(__name__, path="/")

df = pd.read_csv("data/wheelset_history.csv")

def generate_card(row):
    return dbc.Col(
        dbc.Card(
            dbc.CardBody([
                html.H5(row["Wheelset Serial Number"]),
                html.P(f"Date: {row['Date']}"),
                html.P(f"Maintenance Action: {row['Maintenance Action']}"),
                html.P(f"Depot: {row['Depot']}"),
                html.P(f"Remarks: {row['Remarks']}"),
                dcc.Link("🔍 View Details", href=f"/wheelset/{row['Wheelset Serial']}")
            ]),
            className="mb-4", style={"height": "100%"}
        ),
        width=4
    )

layout = dbc.Container([
    dbc.Row([
        generate_card(row) for _, row in df.iterrows()
    ])
], fluid=True)
