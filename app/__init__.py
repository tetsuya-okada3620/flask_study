from flask import Flask
from app.extensions import db, login_manager
from dotenv import load_dotenv
import os

def create_app():
    app = Flask(__name__)

    load_dotenv("config.env")
    # app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_DATABASE_URI"] ="postgresql://nemui3620:8pweKIdOvLU8QAv6EV7AIBIQYuVssRUp@dpg-d22cns2dbo4c73f32nmg-a/study_record"
    
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = os.getenv("SECRET_KEY")
    db.init_app(app)

    login_manager.login_view = "login"
    login_manager.login_message = "先にログインしてください!!!"
    login_manager.session_protection = "strong"
    login_manager.init_app(app)

    from app.view import main
    app.register_blueprint(main)



    return app