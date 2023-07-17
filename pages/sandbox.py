import dash
from dash import dcc, html
from dash.dependencies import Output, Input, ALL, State, MATCH, ALLSMALLER
import plotly.express as px
import plotly.graph_objects as go
import plotly
import dash_bootstrap_components as dbc
import pandas as pd
from components.column_dictionary import column_dict2

dash.register_page(__name__, name='Sandbox')

df = pd.read_csv("coupons.csv")

number_variables = len(column_dict2)
def accordion_hist_plots(dictionary):
    accordion_items = []
    for idx, item in enumerate(dictionary):
        label =item['label']
        x_value = item['id']

        histogram_plot = px.histogram(df, x = x_value)
        title = label
        histogram_plot = dcc.Graph(figure=histogram_plot, style = {'width':'400px', 'height':'200px'})
        accordion_item = dbc.AccordionItem(
                histogram_plot, title=title,
        )
        accordion_items.append(accordion_item)
    return dbc.Accordion(accordion_items)

accordion = accordion_hist_plots(column_dict2)

layout = html.Div(
    [
    html.Div(html.H1(f"Hello World {number_variables}"), style={'textAlign': 'center'}),
        accordion
    ]
)

