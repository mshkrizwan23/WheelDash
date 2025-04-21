import dash
from dash import dcc, html, dash_table, Input, Output
import pandas as pd

app = dash.Dash(__name__)
server = app.server

# Load data
condition_df = pd.read_csv("dashboard_wheelset_condition.csv")
maintenance_df = pd.read_csv("dashboard_maintenance_records.csv")

# App layout
app.layout = html.Div([
    html.H2("🚆 Wheelset Condition & Maintenance Dashboard"),

    dcc.Input(id='input-wheelset', type='text', placeholder='Enter or scan Wheelset Serial', debounce=True),
    html.Div(id='output-details')
])

@app.callback(
    Output('output-details', 'children'),
    Input('input-wheelset', 'value')
)
def display_wheelset_info(serial):
    if not serial:
        return "🔍 Awaiting input..."
    filtered = condition_df[condition_df["Wheelset Serial"] == serial]
    history = maintenance_df[maintenance_df["Wheelset Serial"] == serial]
    if filtered.empty:
        return html.Div(f"❌ No data found for wheelset: {serial}")
    return html.Div([
        html.H4("Current Condition:"),
        dash_table.DataTable(
            data=filtered.to_dict('records'),
            columns=[{"name": i, "id": i} for i in filtered.columns],
            style_table={"overflowX": "auto"},
            style_cell={"textAlign": "left"}
        ),
        html.H4("Maintenance History:"),
        dash_table.DataTable(
            data=history.to_dict('records'),
            columns=[{"name": i, "id": i} for i in history.columns],
            style_table={"overflowX": "auto"},
            style_cell={"textAlign": "left"}
        )
    ])

if __name__ == "__main__":
    app.run_server(debug=True, port=10000)