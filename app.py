import dash
from dash import dcc, html, dash_table
import pandas as pd
import plotly.express as px

# Load data
wheelsets = pd.read_csv("wheelset_data.csv")
inspections = pd.read_csv("inspection_data.csv")
alerts = pd.read_csv("alerts.csv")
kpi = pd.read_csv("kpi_data.csv")

app = dash.Dash(__name__)
app.title = "Freight Wheelset Dashboard"

# Layout
app.layout = html.Div([
    html.H1("🚆 Freight Wagon Wheelset Dashboard", style={'textAlign': 'center', 'color': '#2c3e50'}),

    html.H3("📋 Wheelset Summary"),
    dash_table.DataTable(
        data=wheelsets.to_dict('records'),
        columns=[{"name": i, "id": i} for i in wheelsets.columns],
        style_table={'overflowX': 'auto'},
        page_size=5
    ),

    html.H3("🧪 Latest Inspection Logs"),
    dash_table.DataTable(
        data=inspections.to_dict('records'),
        columns=[{"name": i, "id": i} for i in inspections.columns],
        style_table={'overflowX': 'auto'},
        page_size=5
    ),

    html.H3("🚨 Condition Alerts"),
    dash_table.DataTable(
        data=alerts.to_dict('records'),
        columns=[{"name": i, "id": i} for i in alerts.columns],
        style_table={'overflowX': 'auto'},
        page_size=5
    ),

    html.H3("📊 Monthly KPIs"),
    dcc.Graph(
        figure=px.bar(kpi, x="Month", y=["Inspections", "Defects_Logged", "Wheelsets_Reprofiled"],
                      barmode="group", title="Monthly KPI Trends")
    )
])

server = app.server

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=10000)
