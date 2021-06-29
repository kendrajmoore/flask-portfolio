import os

from dotenv import load_dotenv, find_dotenv
from flask import Flask
from config import Config
from flask_assets import Environment, Bundle
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config


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


from app import routes, models

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
