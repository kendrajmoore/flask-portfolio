import os
from app import app
from app import db
from flask import render_template, request
from app.models import UserModel
from werkzeug.security import check_password_hash, generate_password_hash
from app.forms import RegistrationForm
from app.forms import LoginForm


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
        # elif UserModel.query.filter_by(username=username).first() is not None:
        #     error = f"User {username} is already registered."

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
