import dash
from dash import dcc, html, Output, Input, callback
import dash_bootstrap_components as dbc
import pandas as pd
from components.column_dictionary import column_names, column_list
from components import accordionitems

dash.register_page(__name__, name="Home Page", path='/datadescription')

df = pd.read_csv("coupons.csv")

df_columns = df[column_list]

accordion = accordionitems.create_accordion_list(df, df_columns.columns)

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