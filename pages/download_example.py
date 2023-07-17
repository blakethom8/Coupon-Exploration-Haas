import base64
import io
import dash
from dash import html, Input, Output, State, callback, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import os
from plotly.io import write_image
import time




dash.register_page(__name__, name='Save Files')

df = pd.read_csv("coupons.csv")
fig = px.histogram(df, x = 'age')

layout = html.Div([
        dbc.Row([
        dcc.Graph(figure = fig, id = 'my-graph',
                  config={
                      'modeBarButtonsToRemove': ['zoom2d', 'pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d',
                                                 'autoScale2d', 'resetScale2d', 'hoverClosestCartesian',
                                                 'hoverCompareCartesian'],
                      'toImageButtonOptions': {
                          'format': 'png',  # one of png, svg, jpeg, webp
                          'filename': 'custom_image',  # default is 'plot'
                          'height': 500,
                          'width': 700,
                          'scale': 9  # Multiply title/legend/axis/canvas sizes by this factor
                      }}),
    ]),
    html.Button('Save Chart', id='save-button'),
])


@callback(
    Output('save-button', 'n_clicks'),
    Input('save-button', 'n_clicks'),
    State('bar_graph', 'figure'),
    prevent_initial_call=True
)
def save_image(n, figure):
    if n:
        fig = go.Figure(figure)
        if not os.path.exists('saved_images'):
            os.mkdir('saved_images')
        img_path = f'saved_images/image_{n}.png'
        write_image(fig, img_path)  # save image
    return 0  # resetting the click count