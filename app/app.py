# import os
# import sqlite3
# from flask import Flask, render_template, request, redirect, url_for, flash
# from flask_bcrypt import Bcrypt
# from flask_login import LoginManager, login_user, login_required, logout_user, current_user
# from forms import RegistrationForm, LoginForm, UpdateAccountForm, UpdatePersonalForm, UpdateProfilePic, UpdatePasswordForm 
# from datetime import timedelta, datetime

# app = Flask(__name__)
# app.config["SECRET_KEY"] = "dev"





# bcrypt = Bcrypt(app)
# login_manager = LoginManager(app)

# db = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app.db")



# @login_manager.user_loader
# def load_user(user_id):
#     ...
    
    
# @login_manager.unauthorized_handler
# def unauthorized():
#     return redirect(url_for('login'))








# @ app.route("/login", methods=['GET', 'POST'])
# def login():
#     form = LoginForm()

#     if request.method == 'POST':
#         if form.validate_on_submit():
#             user = load_user(form.email.data)
#             with sqlite3.connect(DB) as conn:
#                 cursor = conn.cursor()
#                 cursor.execute("SELECT email,password FROM users WHERE email= ?", [
#                     form.email.data])
#                 query_result = cursor.fetchone()
#                 if not query_result:
#                     flash("User not registered", 'warning')
#                     return redirect(url_for('login'))
#                 if bcrypt.check_password_hash(query_result[1], form.password.data) and form.email.data == query_result[0]:
#                     login_user(user, remember=form.remember.data,
#                                duration=timedelta(minutes=30), force=False, fresh=True)
#                     return redirect(url_for('trip'))
#                 else:
#                     flash(
#                         'Login Unsuccessful. Please check email and password!', 'danger')
#                     return redirect(url_for('login'))

#     return render_template('login.html', title='Login', form=form)


# @app.route('/')
# def index():
#     return render_template('index.html',title='Test')


# if __name__ == '__main__':
#     app.run(port=8080,debug=True)