import dash
from dash import dcc, html

import pandas as pd
from components.column_dictionary import column_dict2
from components import accordionitems

dash.register_page(__name__, name='Sandbox')

# Tell Accordion which data to pull from
df = pd.read_csv("coupons.csv")
number_variables = len(column_dict2)

# Create histogram accordion
accordion = accordionitems.accordion_hist_plots(column_dict2, df)

layout = html.Div(
    [
    html.Div(html.H1(f"Hello World {number_variables}"), style={'textAlign': 'center'}),
        accordion
    ]
)

