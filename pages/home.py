import dash
from dash import html
import pandas as pd
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/', name='Dashboard')

df = pd.read_csv("data/wheelset_condition_sample.csv")

def create_card(row):
    return dbc.Card([
        dbc.CardBody([
            html.H5(row["Wheelset Serial Number"], className="card-title"),
            html.P(f"Status: {row['Status']}"),
            html.P(f"Depot: {row['Depot']}"),
            html.P(f"Remarks: {row['Remarks']}"),
            dbc.Button("View Details", href=f"/wheelset/{row['Wheelset Serial Number']}", color="primary")
        ])
    ], style={"width": "18rem", "margin": "10px"})

layout = dbc.Row([dbc.Col(create_card(row), width="auto") for _, row in df.iterrows()])
