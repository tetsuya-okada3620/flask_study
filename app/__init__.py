from flask import Flask
from app.extensions import db, login_manager
from dotenv import load_dotenv
import os

def create_app():
    app = Flask(__name__)

    load_dotenv("config.env")
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:admin@localhost:5432/study_record"
    
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Falseでクエリ発行時の余計な処理を防ぐ
    app.secret_key = "secrets" #os.getenv("SECRET_KEY")  # CSRFトークンの検証キー
    db.init_app(app)

    login_manager.login_view = "login"
    login_manager.login_message = "先にログインしてください!!!"
    login_manager.session_protection = "strong"  # (要確認)
    login_manager.init_app(app)

    from app.view import main
    app.register_blueprint(main)



    return app