import os

from dotenv import load_dotenv, find_dotenv
from flask import Flask
from config import Config
from flask_assets import Environment, Bundle
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask import render_template, request
from app import app
from werkzeug.security import check_password_hash, generate_password_hash
from app.forms import RegistrationForm
from app.forms import LoginForm


load_dotenv(find_dotenv())

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{table}'.format(
    user=os.getenv('POSTGRES_USER'),
    passwd=os.getenv('POSTGRES_PASSWORD'),
    host=os.getenv('POSTGRES_HOST'),
    port=5432,
    table=os.getenv('POSTGRES_DB'))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

assets = Environment()
assets.init_app(app)


css = Bundle('src/css/*.css', filters='postcss', output='dist/css/main.css')
assets.register('css', css)

class UserModel(db.Model):
    __tablename__ = 'users'

    username = db.Column(db.String(), primary_key=True)
    password = db.Column(db.String())

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<User {self.username}>"

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv('URL'))


@app.route('/health')
def health():
    return "Works"


@app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif UserModel.query.filter_by(username=username).first() is not None:
            error = f"User {username} is already registered."

        if error is None:
            new_user = UserModel(username, generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            return f"User {username} created successfully"
        else:
            return error, 418

    # TODO: Return a restister page
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        error = None
        user = UserModel.query.filter_by(username=username).first()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user.password, password):
            error = 'Incorrect password.'

        if error is None:
            return "Login Successful", 200
        else:
            return error, 418

    # TODO: Return a login page
    return render_template('login.html', title='Login', form=form)


# from app import models

# from data.load_data import load_projects, load_profiles

# from dotenv import load_dotenv

# load_dotenv()

# if not os.environ.get("PRODUCTION"):
#     from dotenv import load_dotenv

#     load_dotenv()


# assets = Environment()
# assets.init_app(app)


# css = Bundle('src/css/*.css', filters='postcss', output='dist/css/main.css')
# assets.register('css', css)
# base_url = os.getenv("URL")
# projects_base_url = base_url + "/projects/"
# profiles_base_url = base_url + "/profiles/"

# projects = load_projects()
# profiles = load_profiles()

# @app.route('/')
# def index():
#     return "Hello, World"


# @app.route('/')
# def index():
#     return render_template('index.html', profiles=profiles, projects=projects, title="Team Kenargi's portfolio",
#                            url=base_url)


# @app.route('/projects/<name>')
# def get_project(name):
#     if name not in projects:
#         return abort(404)
#     return render_template('project.html', item=projects[name], title=name, url=projects_base_url + name)


# @app.route('/profiles/<name>')
# def get_profile(name):
#     if name not in profiles:
#         return abort(404)
#     title = name + "'s Profile"
#     return render_template('profile.html', item=profiles[name], title=title, url=profiles_base_url + name)


# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html', title="Page not found"), 404
