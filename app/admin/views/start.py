#coding:utf-8
from flask import current_app, render_template, request, redirect, url_for, flash
from app.models.model import db
from flask_login import login_user, logout_user, login_required, current_user
from app.admin import admin
from app.admin.forms.start import *
from app.includes.start import *
from app.admin.forms.user import *
from app.models.user import *


@admin.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("admin.index"))
    from app.models.user import User
    form = LoginForm()
    if form.validate_on_submit():
        user = User.getbyname(form.username.data)
        if user is not None and user.verify_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for("admin.index"))
        flash("账号或密码错误")
    form.remember.data=True
    return render_template("admin/start/login.html", form = form)

@admin.route("/regist", methods=["GET", "POST"])
def regist():
    form = RegisterForm()
    if form.validate_on_submit():
        User.add(form.username.data, form.password.data)
        flash("注册成功")
        return redirect(url_for("admin.login"))
    return render_template("admin/start/regist.html", form = form)

@admin.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("admin.login"))


