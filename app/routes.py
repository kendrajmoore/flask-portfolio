import os
from app import app
from app import db
from flask import render_template, request
from app.models import UserModel
from werkzeug.security import check_password_hash, generate_password_hash
from app.forms import RegistrationForm
from app.forms import LoginForm


@app.route("/")
def index():
    return render_template("index.html", title="Welcome", url=os.getenv("URL")), 200


@app.route("/health")
def health():
    return "Works"


@app.route("/about")
def about():
    return render_template("about.html", title="About Me", url=os.getenv("URL")), 200


@app.route("/blog")
def blog():
    return render_template("blog.html", title="Blogs", url=os.getenv("URL")), 200


@app.route("/project")
def project():
    return render_template("project.html", title="Projects", url=os.getenv("URL")), 200


@app.route("/register", methods=("GET", "POST"))
def register():
    form = RegistrationForm()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."

        if error is None:
            new_user = UserModel(username, generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            return render_template("index.html", title="Registered", url=os.getenv("URL")), 200
        else:
            return error, 418

    # TODO: Return a restister page
    return render_template("register.html", title="Register", form=form), 200


@app.route("/login", methods=("GET", "POST"))
def login():
    form = LoginForm()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        error = None
        user = UserModel.query.filter_by(username=username).first()

        if user is None:
            error = "Incorrect username."
        elif not check_password_hash(user.password, password):
            error = "Incorrect password."

        if error is None:
            return render_template("index.html", title="Logged In", url=os.getenv("URL")), 200
        else:
            return error, 418

    # TODO: Return a login page
    return render_template("login.html", title="Login", form=form), 200


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", title="Login"), 404
