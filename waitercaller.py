from flask import Flask, render_template, request
from flask_login import LoginManager, login_required, login_user, logout_user
# from mockdbhelper import MockDBHelper
from mockdbhelper import MockDBHelper as DBHelper
from passwordhelper import PasswordHelper
from user import User

PH = PasswordHelper()
DB = DBHelper()

app = Flask(__name__)
app.secret_key = 'gwJtFlFZBCmd7OoPlK6IOrmgk5VnynDMJ2bkfiwHh1sXIiYm4Wi+xjZ5BTmAS4tCmXVPbGRYIQNI1EK9/SZuficO1cH9Nj7qKoG'  # Required for Flask-Login

# Initialize LoginManager
login_manager = LoginManager(app)

@app.route("/")
def home():
    return render_template("home.html")

@login_manager.user_loader
def load_user(user_id):
    if DB.get_user(user_id):  # Check if the user exists in the mock database
        return User(user_id)  # Return a User object for Flask-Login
    return None  # Flask-Login treats None as not logged in

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    stored_user = DB.get_user(email)
    if stored_user and PH.validate_password(password,
                                            store_user['salt'], stored_user['hashed']):
        user = User(email)
        login_user(user, remember=True)
        return redirect(url_for('account'))
    return home()



@app.route("/account")
@login_required
def account():
    return "You are logged in"

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(port=5000, debug=True)
