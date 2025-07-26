from app.extensions import db, login_manager
from app.forms import LoginForm
from app.models import User, AccountInfo, users
from flask_login import login_required, login_user, logout_user
from flask import Blueprint, render_template, redirect, url_for, flash
from werkzeug.security import check_password_hash

main = Blueprint("main", __name__)

@login_manager.user_loader
def load_user(username):
    if username in users:
        return User(username)

@main.route("/", methods=["GET", "POST"])
def login():
    print("OK")
    forms = LoginForm()
    if forms.validate_on_submit():
        username = forms.username.data
        password = forms.password.data

        if username in users and check_password_hash(users[username]["password"], password):
            user = User(username)
            login_user(user)
            return redirect(url_for("main.record"))
        else:
            flash("ユーザー名、またはパスワードが違います")
    
    return render_template("login.html", forms=forms)

@login_required
@main.route("/record")
def record():
    print("record.htmlを開く")
    return render_template("record.html")

@login_required
@main.route("/logout", methods=["POST"])
def logout():
    logout_user()
    flash("ログアウトしました。")
    return redirect(url_for("main.login"))