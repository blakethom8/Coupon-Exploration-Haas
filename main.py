from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
import time
# from app import app as dash_app
from app2 import create_dash_app


# Remove the separate Flask app initiliation
app = Flask(__name__)
# bcrypt = Bcrypt(app)

# Flask setup using Dash server
# app = dash_app.server
bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqldatabase.db'
app.config['SECRET_KEY'] = 'mysecretkey'

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return UserLogin.query.get(int(user_id))

# Create Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=time.time())

    # create string
    def __repr__(self):
        return '<Name %r>' % self.name

class UserLogin(db.Model, UserMixin):
    __tablename__ = 'UserLogin'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

    # create a string
    def __repr__(self):
       return '<Username %r>' % self.username

class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = UserLogin.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    login_error = None
    if form.validate_on_submit():
        user = UserLogin.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect('/dash/')
            else:
                login_error = "Incorrect Password. Please try again"
        else:
            login_error = "Username not found"
    return render_template('login.html', form=form, login_error=login_error)


# @app.route('/dashboard', methods=['GET', 'POST'])
# @login_required
# def dashboard():
#     return render_template('dashboard.html')

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@ app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = UserLogin(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


# Protect Dash routes
dash_app = create_dash_app(app)

if __name__ == "__main__":
   # DB is already created
   #  with app.app_context():
   #      db.create_all()
    app.run(debug=True, port = 4000)