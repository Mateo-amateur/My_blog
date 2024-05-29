from flask import render_template, url_for, flash, redirect
from app import app
# from app.forms import RegistrationForm, LoginForm, PostForm
# from app.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    return render_template('register.html', title='Register')

@app.route("/login")
def login():
    return render_template('login.html', title='Login')

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/post/new")
@login_required
def new_post():
    return render_template('create_post.html', title='New Post')