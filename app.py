import dash
from dash import dcc, html, Input, Output, State, dash_table
import pandas as pd
import base64
import io

app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server

app.layout = html.Div([
    html.H1("🚆 Freight Wheelset Maintenance Dashboard", style={'textAlign': 'center'}),

    dcc.Tabs(id="tabs", value='tab-condition', children=[
        dcc.Tab(label='Wheelset Condition Data', value='tab-condition'),
        dcc.Tab(label='Maintenance Records', value='tab-maintenance'),
    ]),
    html.Div(id='tabs-content')
])

@app.callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))
def render_content(tab):
    if tab == 'tab-condition':
        return html.Div([
            html.H3("Upload Wheelset Condition Data"),
            dcc.Upload(
                id='upload-condition',
                children=html.Div(['📂 Drag and Drop or ', html.A('Select wheelset_condition_sample.csv')]),
                style={'width': '60%', 'height': '60px', 'lineHeight': '60px',
                       'borderWidth': '1px', 'borderStyle': 'dashed',
                       'borderRadius': '5px', 'textAlign': 'center', 'margin': '10px'}
            ),
            html.Div(id='output-condition')
        ])
    elif tab == 'tab-maintenance':
        return html.Div([
            html.H3("Upload Maintenance Records"),
            dcc.Upload(
                id='upload-maintenance',
                children=html.Div(['📂 Drag and Drop or ', html.A('Select maintenance_records_sample.csv')]),
                style={'width': '60%', 'height': '60px', 'lineHeight': '60px',
                       'borderWidth': '1px', 'borderStyle': 'dashed',
                       'borderRadius': '5px', 'textAlign': 'center', 'margin': '10px'}
            ),
            html.Div(id='output-maintenance')
        ])

def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
            return dash_table.DataTable(
                data=df.to_dict('records'),
                columns=[{'name': i, 'id': i} for i in df.columns],
                style_table={'overflowX': 'auto'},
                style_cell={'textAlign': 'left'},
                page_size=10
            )
    except Exception as e:
        return html.Div(['There was an error processing this file.'])

@app.callback(Output('output-condition', 'children'),
              Input('upload-condition', 'contents'),
              State('upload-condition', 'filename'))
def update_condition(contents, filename):
    if contents:
        return parse_contents(contents, filename)

@app.callback(Output('output-maintenance', 'children'),
              Input('upload-maintenance', 'contents'),
              State('upload-maintenance', 'filename'))
def update_maintenance(contents, filename):
    if contents:
        return parse_contents(contents, filename)

if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0", port=10000)