import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
from flask_login import current_user
from flask import request
from components.navbar import create_sidebar
from flask_login import current_user



# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}



# Create Dash app function
def create_dash_app(flask_app):

    dash_app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SPACELAB],
                         server = flask_app,
                         url_base_pathname='/dash/',
                         assets_url_path='/dash/assets',
                         assets_folder='/dash/assets',
                         )

    # Define Dash layout
    dash_app.layout = html.Div([
        # ... your other layout components ...
        create_sidebar(),
        html.Div(dash.page_container, id='page-content', style=CONTENT_STYLE),
        # dcc.Location to access the URL pathname
        dcc.Location(id='url', refresh=False)
    ])

    @dash_app.callback(Output('page-content', 'children'),
                       [Input('url', 'pathname')])
    def display_page(pathname):
        # Check if the user is authenticated
        print("User authentication:", current_user.is_authenticated)

        if not current_user.is_authenticated:
            # Redirect to the login page if the user is not authenticated
            print("User is not authenticated. Redirecting to login page.")
            return dcc.Location(pathname='/login', id='redirect-login')

        # Depending on the URL pathname, return the corresponding layout
        if pathname == '/dash/':
            print("Rendering Dash App.")
            return html.Div([
                html.H1('Dash App'),
                # ... your Dash app content ...
            ])
        elif pathname == '/homepage/':
            print("Rendering Other Page.")
            return []
                # ... your other page content ...

        else:
            print("Page Not Found.")
            return html.Div([
                html.H1('Page Not Found'),
                # ... handle the case of a page not found ...
            ])

    # ... other Dash routes ...

    return dash_app