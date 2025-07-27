from flask_login import UserMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import column_property
from app.extensions import db
from werkzeug.security import generate_password_hash

class User(UserMixin):
    def __init__(self, username):
        self.id = username
        self.is_guest = False

class Guest(UserMixin):
    def __init__(self):
        self.id = "Guest"
        self.is_guest = True

users = {"admin": {"password": generate_password_hash("admin202507")}}
# 一旦不使用
class AccountInfo(db.Model):
    __tablename__ = "account_info"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(255)) # ハッシュ値前提

class Records(db.Model):
    __tablename__ = "records"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_id = db.Column(db.Integer, ForeignKey("categories.category_id"))
    confirm = db.Column(db.Text, nullable=True)
    study_date_start = db.Column(db.DateTime)
    study_date_end = db.Column(db.DateTime)
    write_date = db.Column(db.DateTime)
    remark = db.Column(db.Text)

    duration = column_property(study_date_end - study_date_start)

    categories = db.relationship("Categories", back_populates="records")

    def __repr__(self):
        # 文字化けやNone対策済み
        return f"<Records id={self.id} confirm={self.confirm or ''}>"

class Categories(db.Model):
    __tablename__ = "categories"
    category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(20))

    records = db.relationship("Records", back_populates="categories")

    def __repr__(self):
        return f"<Category id={self.category_id} name={self.category_name}>"