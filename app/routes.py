from flask import render_template, url_for, flash, redirect
from app import app
from app.forms import RegisterForm, LogInForm, ValidateNameLogIn
from flask_login import login_user, current_user, logout_user, login_required
from app.models import insertDataToForm, getNameList, getPassword

class Profile:
    def __init__(self):
        self.isLogIn = False
        
profile = Profile()

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', profile = profile)

@app.route("/about")
def about():
    return render_template('about.html', title='About', profile = profile)

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        insertDataToForm(form)
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form = form, profile = profile)

@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LogInForm()
    error = None
    if form.validate_on_submit():
        error = None
        username = form.username.data
        password = int(form.password.data)
        listName = getNameList()
        if ValidateNameLogIn(listName, username):
            passwordUser = int(getPassword(username))
            if  passwordUser == password:
                profile.isLogIn = True
                return redirect(url_for('home', profile = profile))
            else:
                error = 'The password is wrong'
                return render_template('login.html', title='Login', form = form, profile = profile, error= error)
        else:
            error = 'The username is wrong'
            return render_template('login.html', title='Login', form = form, profile = profile, error= error)
    return render_template('login.html', title='Login', form = form, profile = profile, error= error)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/post/new")
@login_required
def new_post():
    return render_template('create_post.html', title='New Post', profile = profile)