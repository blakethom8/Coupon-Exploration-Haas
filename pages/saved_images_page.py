import dash
from dash import Input, Output, State, callback, dcc, html, dash_table
import os

dash.register_page(__name__, name='Saved Graphs')

image_path = "saved_images/image_1.png"

layout = html.Div([
    html.Button('Refresh Images', id='refresh-button'),
    html.Div(id='saved-images'),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Div(
        children = [
            html.Img(src = image_path, alt='Image'),
            ]
    )
])

@callback(
    Output('saved-images', 'children'),
    Input('refresh-button', 'n_clicks')
)
def update_images(n):
    # Assuming you have saved your images in a directory named 'saved_images'
    saved_images = os.listdir('saved_images')
    return [html.Img(src=f'/saved_images/{img}') for img in saved_images]
