
import dash
from dash import html, Input, Output, State, callback, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

from components import choosecolumn
import time
import boto3
from io import BytesIO
import plotly.io as pio
from database import db, Image


s3 = boto3.client('s3',
                    aws_access_key_id='AKIA5YBQKQYJBKCQPKGE',
                    aws_secret_access_key='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',
                    region_name='us-west-2'
                  )



dash.register_page(__name__, name='Save Files')




df = pd.read_csv("coupons.csv")
fig = px.histogram(df, x = 'age')

layout = html.Div([

    dbc.Row([html.H1('Save Chart to Your Page')]),
    dbc.Row([choosecolumn.choose_column_dropdown('dropdown_save_image')]),
    dbc.Row([
             html.Div(
                 dcc.Graph(id='bar_graph_save_image',
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
                                   }
                              }
                           ),
                 style={'display': 'inline-block', 'width': '90%'}
             )
    ]),
    dbc.Row([html.Button('Save Chart', id='save-button')])
])


# -------------------------------------------------------------------------------------
# Save Image to File

@callback(
    Output('save-button', 'n_clicks'),
    Input('save-button', 'n_clicks'),
    State('bar_graph_save_image', 'figure'),
    State('dropdown_save_image', 'value'),

    prevent_initial_call=True
)

def save_image(n, figure,column):
    if n:
        current_user = 1111
        fig = go.Figure(figure)
        id_time = int(time.time())

        img_path = f'image_{current_user}_{column}_{int(time.time())}.png'

        # Convert the plotly figure to a PNG BytesIO object
        image_bytes = pio.to_image(fig, format='png')
        image_obj = BytesIO(image_bytes)

        # Upload the BytesIO object to S3
        s3.upload_fileobj(image_obj, 'coupondashboardhaasdatabase', img_path)

        img = Image( id=id_time, user_id=current_user, path=img_path)  # Create new image instance
        db.session.add(img)  # Add to session
        db.session.commit()  # Commit transaction
    return 0  # resetting the click count


# -------------------------------------------------------------------------------------
# Create Grouped Bar Based on the Choose Column

@callback(
         Output(component_id='bar_graph_save_image', component_property='figure'),
    [
         Input(component_id='dropdown_save_image', component_property='value'),
    ]
)

def create_grouped_bar(column_chosen2):
    dffBar = df

    accepted = dffBar[dffBar['Y'] == 1]
    acceptedDf = accepted.groupby(column_chosen2).size().reset_index().set_index(column_chosen2)
    acceptedDf.columns = ['Accepted']

    denied = dffBar[dffBar['Y'] == 0]
    deniedDf = denied.groupby(column_chosen2).size().reset_index().set_index(column_chosen2)
    deniedDf.columns = ['Denied']

    groupedDf = acceptedDf.merge(deniedDf, on=column_chosen2).reset_index()

    fig_bar = go.Figure()
    fig_bar.add_trace(go.Bar(x=groupedDf[column_chosen2], y=groupedDf['Accepted'], name='Accepted'))
    fig_bar.add_trace(go.Bar(x=groupedDf[column_chosen2], y=groupedDf['Denied'], name='Denied'))
    fig_bar.update_layout(barmode='group', xaxis_title=column_chosen2, yaxis_title='Count',
                          title='Coupon Response by ' + column_chosen2 + ' type', title_x=0.5, title_y=0.9)

    return fig_bar