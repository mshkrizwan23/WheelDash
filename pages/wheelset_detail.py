import dash
from dash import html, dcc
import pandas as pd
import dash_bootstrap_components as dbc

dash.register_page(__name__, path_template="/wheelset/<wheelset_id>")

condition_df = pd.read_csv("data/wheelset_condition.csv")
history_df = pd.read_csv("data/wheelset_history.csv")
maint_df = pd.read_csv("data/dashboard_maintenance_records.csv")

def layout(wheelset_id=None):
    wheel_info = condition_df[condition_df["Wheelset Serial"] == wheelset_id]
    maintenance = maint_df[maint_df["Wheelset Serial"] == wheelset_id]
    history = history_df[history_df["Wheelset Serial"] == wheelset_id]

    if wheel_info.empty:
        return html.H4("Wheelset not found.")

    info = wheel_info.iloc[0]

    return dbc.Container([
        html.H3(f"Wheelset: {wheelset_id}"),
        html.Hr(),
        html.Div([
            html.P(f"Status: {info['Status']}"),
            html.P(f"Depot: {info['Depot']}"),
            html.P(f"Last Maintenance: {info['Last Maintenance Date']}"),
            html.P(f"Remarks: {info['Remarks']}"),
        ]),

        html.H4("🔧 Maintenance Records"),
        dbc.Table.from_dataframe(maintenance, striped=True, bordered=True, hover=True),

        html.H4("📈 Wear History"),
        dbc.Table.from_dataframe(history, striped=True, bordered=True, hover=True),
    ], fluid=True)
