import dash
from dash import dcc, html
from dash.dependencies import Output, Input, ALL, State, MATCH, ALLSMALLER
import plotly.express as px
import plotly.graph_objects as go
import plotly
import dash_bootstrap_components as dbc
import pandas as pd


dash.register_page(__name__, name='Sandbox')

df = pd.read_csv("coupons.csv")
histogram1 = px.histogram(df, x = 'weather' ,
                          title = '# of Weather Coupons by Weather')
histogram1 = dcc.Graph(figure=histogram1, style = {'width':'800px', 'height':'400px'})
histogram2 = px.histogram(df, x = 'income',
                          title = '# of Income Customers by Income')
histogram2 = dcc.Graph(figure=histogram2, style = {'width':'800px', 'height':'400px'})

# def create_histgram_plot(dictionary):
#     return px.histogram(df, x = dictionary['id'],
#                         title = dictionary['label'])
# accordion2 = dbc.Accordion(
#     [
#         accordion_item(column_name, df[column_name]) for id in df_columns.columns
#     ],
#     always_open = True,
#     flush=True,
#     id ="accordion-always-open",
#
layout = html.Div(
    [
        dbc.Accordion(
            [
            dbc.AccordionItem(html.Div([
                                        histogram1,
                                        html.H1("Check")
                ]),
                title="Weather"),
            dbc.AccordionItem(histogram2, title="Income"),
        ]
        )
    ]
)