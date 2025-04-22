import dash
from dash import html, dcc
import pandas as pd
import dash_bootstrap_components as dbc

dash.register_page(__name__, path_template="/wheelset/<wheelset_id>")

condition_df = pd.read_csv("data/wheelset_condition.csv")
history_df = pd.read_csv("data/wheelset_history.csv")
maint_df = pd.read_csv("data/dashboard_maintenance_records.csv")

def layout(wheelset_id=None):
    if wheelset_id is None:
        return html.H4("⚠️ No Wheelset ID provided.")

    # Strip and standardise the ID
    wheelset_id = wheelset_id.strip()

    # Debug print — will show up in Render logs
    print("Requested Wheelset ID:", wheelset_id)
    print("Available:", condition_df["Wheelset Serial"].unique())

# Search for latest history
wheel_history = history_df[history_df["Wheelset Serial Number"] == wheelset_id]
latest_history = wheel_history.sort_values(by="Date", ascending=False).head(1)

if latest_history.empty:
    return html.H4(f"⚠️ No historical data found for {wheelset_id}.")

info = latest_history.iloc[0]

return dbc.Container([
    html.H3(f"Wheelset: {wheelset_id}"),
    html.Hr(),
    html.Div([
        html.P(f"Date: {info['Date']}"),
        html.P(f"Maintenance Action: {info['Maintenance Action']}"),
        html.P(f"Depot: {info['Depot']}"),
        html.P(f"Remarks: {info['Remarks']}"),
    ]),


        html.H4("🔧 Maintenance Records"),
        dbc.Table.from_dataframe(maintenance, striped=True, bordered=True, hover=True),

        html.H4("📈 Wear History"),
        dbc.Table.from_dataframe(history, striped=True, bordered=True, hover=True),
    ], fluid=True)
