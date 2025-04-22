import dash
from dash import html
import pandas as pd

dash.register_page(__name__, path_template="/wheelset/<wheel_id>")

cond = pd.read_csv("data/wheelset_condition_sample.csv")
hist = pd.read_csv("data/maintenance_records_sample.csv")

def layout(wheel_id=None):
    info = cond[cond["Wheelset Serial Number"] == wheel_id]
    history = hist[hist["Wheelset Serial Number"] == wheel_id]

    if info.empty:
        return html.Div([html.H4(f"No info for {wheel_id}")])

    i = info.iloc[0]
    return html.Div([
        html.H3(f"Wheelset {wheel_id}"),
        html.P(f"Status: {i['Status']}"),
        html.P(f"Depot: {i['Depot']}"),
        html.P(f"Remarks: {i['Remarks']}"),
        html.H4("Maintenance History"),
        html.Ul([html.Li(f"{r['Date']} - {r['Maintenance Action']} - {r['Depot']}") for _, r in history.iterrows()])
    ])

