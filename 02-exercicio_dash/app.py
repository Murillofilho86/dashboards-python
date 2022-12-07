import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

external_css = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_css)

df = pd.DataFrame({
    "Fruit": ["Maçã", "Morango", "Laranja", "Banana"],
    "Amount": [4, 1, 3, 5],
    "City": ["SP", "RJ", "MG", "ES"]
})

fig = px.bar(df, x ="Fruit", y="Amount", color="City")

app.layout = html.Div(id="div1",
    children=[
        html.H1("Hello dash", id="h1"),
        html.Div("Dash: para web python"),
        dcc.Graph(figure=fig, id="graph")   
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True, port=8080)