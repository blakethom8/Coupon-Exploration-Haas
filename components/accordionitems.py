import dash_bootstrap_components as dbc
import pandas as pd
from dash import html, dcc
import plotly.express as px

from components.column_dictionary import column_names

def accordion_item_list(column_name, column_data):
    return dbc.AccordionItem(
        html.Ul([html.Li(value) for value in column_data.unique()]),
        title=column_names.get(column_name, column_name),
    )

def create_accordion_list(df, columns):
    return dbc.Accordion(
        [
            accordion_item_list(column_name, df[column_name]) for column_name in columns
        ],
        always_open = True,
        flush=True,
        id ="accordion-always-open",
    )


def accordion_hist_plots(dictionary, df):
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