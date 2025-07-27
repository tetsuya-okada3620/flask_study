from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateTimeField
from wtforms.validators import DataRequired
from datetime import datetime

class LoginForm(FlaskForm):
    username = StringField("ユーザー名", validators=[DataRequired()])
    password = PasswordField("パスワード", validators=[DataRequired()])
    submit_login = SubmitField("ログイン")

class GuestForm(FlaskForm):
    submit_guest = SubmitField("ゲストでログイン(閲覧用)")

class RecordForm(FlaskForm):
    category = SelectField("カテゴリー", validators=[DataRequired()])
    confirm = StringField("内容", validators=[DataRequired()])
    study_date_start = DateTimeField("日付", validators=[DataRequired()], default=datetime.now)
    study_date_end = DateTimeField("日付", validators=[DataRequired()], default=datetime.now)
    remark = StringField("備考")
    submit = SubmitField("入力実行")