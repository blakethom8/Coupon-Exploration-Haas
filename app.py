import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from database import db
import dash_auth as da

server = Flask(__name__)
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
server.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:Utila2020@localhost/test"


# for your live Heroku PostgreSQL database
# app.server.config["SQLALCHEMY_DATABASE_URI"] = "postgres://ntfhytpjxytbar:76e313ce534f461e2d422836883acbdd5618090\
# 72baea3a9a9429e0de3f8fcb5@ec2-44-213-228-107.compute-1.amazonaws.com:5432/d2v4mqm1etefkn"
app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SPACELAB],
                server=server, suppress_callback_exceptions=True
                )

# for your home PostgreSQL test table
# auth = da.BasicAuth(
#     app,
#     {'admin': 'password',
#      'blake': 'password'}
# )

db.init_app(app.server)

# db = SQLAlchemy(app.server)

#-------------------------------------------------------------------------------------
# Create Sidebar

# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

# Make the actual sidebar
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

app.layout = html.Div(
    [
        sidebar,
        html.Div(dash.page_container, style=CONTENT_STYLE)
    ]
)


if __name__ == "__main__":
    app.run(debug=False, port =5000)