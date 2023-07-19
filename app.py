import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, send_from_directory
from database import db, User
import dash_auth as da
from components import navbar
import boto3
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, request, render_template, redirect, url_for
from components.LoginFiles import LoginForm, RegisterForm
#
# s3 = boto3.client('s3',
#                     aws_access_key_id='AKIA5YBQKQYJBKCQPKGE',
#                     aws_secret_access_key='fP5HyKydCmEct8RyTQSfuFeeKXkzm1/QohzRDvTT',
#                     region_name='us-west-2')


server = Flask(__name__)
server.config['SECRET_KEY'] = 'your-secret-key'
# ----------------------------------------
# Use the code below to leverage the Postgre dataset
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
server.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:Utila2020@localhost/test"
db = SQLAlchemy()
db.init_app(server)
# server.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"

# ----------------------------------------
# database setup
# db.init_app(app.server) # use this when we are using the local postgre server
 # db = SQLAlchemy(app.server) # use this for the heroku server/aws connection


# ----------------------------------------
# Login manager setup
login_manager = LoginManager()
# login_manager.init_app(app)
login_manager.login_view = 'login'



# Flask routes

@server.route('/')
def home():
    return redirect(url_for('login'))


@server.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect('/datadescription/')

        # If credentials are not correct, return an error

    return render_template('login.html', form=form)

@server.route('/templates/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ----------------------------------------
# for your live Heroku PostgreSQL database
# app.server.config["SQLALCHEMY_DATABASE_URI"] = "postgres://ntfhytpjxytbar:76e313ce534f461e2d422836883acbdd5618090\
# 72baea3a9a9429e0de3f8fcb5@ec2-44-213-228-107.compute-1.amazonaws.com:5432/d2v4mqm1etefkn"

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SPACELAB],
                server=server, suppress_callback_exceptions=True, url_base_pathname='/datadescription/'
                )

@app.server.route('/datadescription/')
@login_required
def serve_dash_app():
    print("serve_dash_app function called")
    return app.index()


# db.init_app(app.server) # use this when we are using the local postgre server
# ----------------------------------------
# Use this to apply some sort of authentication to your app
# auth = da.BasicAuth(
#     app,
#     {'admin': 'password',
#      'blake': 'password'}
# )


# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}



app.layout = html.Div(
    [
        navbar.create_sidebar(),
        html.Div(dash.page_container, style=CONTENT_STYLE)
    ]
)

if __name__ == "__main__":
    server.run(debug=False, port =5000)