import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, send_from_directory
from database import db
import dash_auth as da



SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}


# Make the actual sidebar

def create_sidebar():

    sidebar = html.Div(
        [
            html.H2("Links", className="display-4"),
            html.Hr(),
            html.P(
                "Coupon Response Analysis", className="lead"
            ),
            dbc.Nav(
                [
                    dbc.NavLink(
                        [
                            html.Div(page["name"], className="ms-2"),
                        ],
                        href=page["path"],
                        active="exact",
                    )
                    for page in dash.page_registry.values()
                ],
                vertical=True,
                pills=True,
            ),
        ],
        style=SIDEBAR_STYLE,
    )

    return sidebar
    #
    # layout = html.Div(
    #     [
    #         sidebar,
    #         html.Div(dash.page_container, style=CONTENT_STYLE)
    #     ]
    # )
