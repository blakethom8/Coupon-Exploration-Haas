import dash
from dash import html
from dash import dcc, html, Output, Input, callback
import plotly.express as px
import plotly.graph_objects as go
import plotly
import dash_bootstrap_components as dbc
import pandas as pd
from components.column_dictionary import column_names, column_list


dash.register_page(__name__, name="Home Page", path='/')

df = pd.read_csv("coupons.csv")

df_columns = df[column_list]


def accordion_item(column_name, column_data):
    return dbc.AccordionItem(
       html.Ul([html.Li(value) for value in column_data.unique()]),
       title=column_names.get(column_name, column_name),
    )

accordion = dbc.Accordion(
    [
        accordion_item(column_name, df[column_name]) for column_name in df_columns.columns
    ],
    always_open = True,
    flush=True,
    id ="accordion-always-open",
)

layout = html.Div(
    [
        html.H1("Explored Variable", style={'textAlign': 'center'}),
        html.H4("Below are a list of options found on the surveys", style={'textAlign': 'center'}),
        html.Hr(),
        html.Br(),
        html.Div(accordion)
    ]
)

@callback(
    Output("accordion-contents-open-ids", "children"),
    [Input("accordion-always-open", "active_item")],
)
def change_item(item):
    print(item)
    return f"Item(s) selected: {item}"