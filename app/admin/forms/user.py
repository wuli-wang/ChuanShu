#coding: utf-8
from flask_wtf import Form
from wtforms import StringField, PasswordField,SubmitField,ValidationError
from wtforms.validators import DataRequired, Length,EqualTo
from app.models.user import User


class UserForm(Form):
    username = StringField("用户名", validators=[DataRequired("用户名不能为空"),
        Length(3, 50, "用户名长度在3到50个字符之间")])
    password = PasswordField("密码", validators=[DataRequired("密码不能为空"), 
        Length(6, 128, "密码长度应该在6到128个字符之间")])


class SettingForm(Form):
    nickname = StringField("昵称", validators=[DataRequired("昵称不能为空"),
        Length(1, 50, "昵称长度在1到50个字符之间")])

class RegisterForm(Form):
    username = StringField('用户名', validators=[DataRequired(), Length(3, 50, message='用户名必须在3~50个字符之间')])
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 128, message='密码长度必须在6~128个字符之间')])
    confirm = PasswordField('确认密码', validators=[EqualTo('password', message='两次密码不一致')])
    submit = SubmitField('注册')

    # 自定义验证器，验证用户名
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('该用户名已存在，请选用其它用户名')



