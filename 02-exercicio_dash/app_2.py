import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd


app = dash.Dash(__name__)


app.layout = html.Div([
    html.Label("Dropdown"),
    
    dcc.Dropdown(
        id="dp-1",
        )
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8080)