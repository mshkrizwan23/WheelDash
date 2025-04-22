import dash
from dash import html, dcc, Input, Output
import pandas as pd

# Sample internal dataset (this would usually be imported or generated)
data = pd.DataFrame({
    'Wheelset Serial': ['WS0001', 'WS0002', 'WS0003'],
    'Status': ['OK', 'Warning', 'Replace'],
    'Last Maintenance': ['2024-09-01', '2024-06-15', '2024-01-20'],
    'Depot': ['Hunslet', 'Bescot', 'Southampton'],
    'Remarks': ['Profile corrected', 'Minor wear', 'Excessive wear']
})

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1("🛠️ Freight Wheelset Maintenance Dashboard"),
    html.Div([
        html.Div([
            html.Div([
                html.H4(f"{row['Wheelset Serial']}"),
                html.P(f"Status: {row['Status']}"),
                html.P(f"Last Maintenance: {row['Last Maintenance']}"),
                html.P(f"Depot: {row['Depot']}"),
                html.P(f"Remarks: {row['Remarks']}"),
            ], style={
                'border': '1px solid #ccc',
                'padding': '10px',
                'margin': '10px',
                'border-radius': '8px',
                'box-shadow': '2px 2px 10px rgba(0,0,0,0.1)',
                'background': '#fff',
                'width': '200px',
                'display': 'inline-block',
                'vertical-align': 'top'
            }) for _, row in data.iterrows()
        ])
    ])
])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
