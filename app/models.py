from flask_login import UserMixin
from app.extensions import db
from werkzeug.security import generate_password_hash

class User(UserMixin):
    def __init__(self, username):
        self.id = username

users = {"admin": {"password": generate_password_hash("admin202507")}}
# 一旦不使用
class AccountInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(255)) # ハッシュ値前提
