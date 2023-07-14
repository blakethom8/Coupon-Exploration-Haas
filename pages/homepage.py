import dash
from dash import dcc, html
from dash.dependencies import Output, Input, ALL, State, MATCH, ALLSMALLER
import plotly.express as px
import plotly.graph_objects as go
import plotly
import dash_bootstrap_components as dbc
import pandas as pd


dash.register_page(__name__, name='Home')

layout = html.Div(['home page'])