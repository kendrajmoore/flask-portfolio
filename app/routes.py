# from flask import render_template, request
# from app import app
# from werkzeug.security import check_password_hash, generate_password_hash
# from app.forms import RegistrationForm
# from app.forms import LoginForm

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/register', methods=('GET', 'POST'))
# def register():
#     form = RegistrationForm()
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#         db = get_db()
#         error = None

#         if not username:
#             error = 'Username is required.'
#         elif not password:
#             error = 'Password is required.'
#         elif db.execute(
#             'SELECT id FROM user WHERE username = ?', (username,)
#         ).fetchone() is not None:
#             error = f"User {username} is already registered."

#         if error is None:
#             db.execute(
#                 'INSERT INTO user (username, password) VALUES (?, ?)',
#                 (username, generate_password_hash(password))
#             )
#             db.commit()
#             return f"User {username} created successfully"
#         else:
#             return error, 418

#     ## TODO: Return a restister page
#     return render_template('register.html', title='Register', form=form)

# @app.route('/login', methods=('GET', 'POST'))
# def login():
#     form = LoginForm()
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#         db = get_db()
#         error = None
#         user = db.execute(
#             'SELECT * FROM user WHERE username = ?', (username,)
#         ).fetchone()

#         if user is None:
#             error = 'Incorrect username.'
#         elif not check_password_hash(user['password'], password):
#             error = 'Incorrect password.'

#         if error is None:
#             return "Login Successful", 200 
#         else:
#             return error, 418
    
#     ## TODO: Return a login page
#     return render_template('login.html', title='Login', form=form)



# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html', title="Page not found"), 404