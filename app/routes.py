# Import modeles requireds
from flask import render_template, url_for, flash, redirect, request
from app import app
from app.forms import RegisterForm, LogInForm, ValidateNameLogIn, NewPostForm
from flask_login import login_user, current_user, logout_user, login_required
from app.models import insertDataToForm, getNameList, getPassword, insertDataToPost, getPosts, configPreferens, getPreferens, clearPreferent

# Creating class to control if is login and keep the data of user after
class Profile:
    def __init__(self) -> None:
        self.isLogIn = False
        self.username = None
    
    def defineUsername(self, username):
        self.username = username

def updateMode(req):
    mode = req.args.get('mode')
    if mode == None:
        pass
    else:
        configPreferens(mode, profile.username)
        
# Instantiate from Prosfile
profile = Profile()

# Creating rout root
@app.route("/")
@app.route("/home")
def home():
    updateMode(request)
    return render_template('home.html', title = "Home", profile = profile)

# Creating rout about
@app.route("/about")
def about():
    updateMode(request)
    return render_template('about.html', title='About', profile = profile)

# Creating rout register
@app.route("/register", methods = ['GET', 'POST'])
def register():
    updateMode(request)
    # Creating Form
    form = RegisterForm()
    error = None
    # Validating the data from the form
    if form.validate_on_submit():
        error = insertDataToForm(form)
        if error == None:
            profile.isLogIn = True
            profile.defineUsername(form.username.data)
            return redirect(url_for('home'))
        else:
            return render_template('register.html', title='Register', form = form, profile = profile, error = error)
    return render_template('register.html', title='Register', form = form, profile = profile, error = error)

# Creating rout register
@app.route("/login", methods = ['GET', 'POST'])
def login():
    updateMode(request)
    # Creating Form
    form = LogInForm()
    error = None
    # Validating the data from the form
    if form.validate_on_submit():
        error = None
        username = form.username.data
        password = int(form.password.data)
        listName = getNameList()
        if ValidateNameLogIn(listName, username):
            passwordUser = int(getPassword(username))
            if  passwordUser == password:
                profile.defineUsername(form.username.data)
                profile.isLogIn = True
                getPreferens(profile.username)
                return redirect(url_for('home'))
            else:
                error = 'The password is wrong'
                return render_template('login.html', title='Login', form = form, error= error, profile = profile)
        else:
            error = 'The username is wrong'
            return render_template('login.html', title='Login', form = form, error= error, profile = profile)
    return render_template('login.html', title='Login', form = form, error= error, profile = profile)

# Creating rout to logout
@app.route("/logout")
def logout():
    profile.isLogIn = False
    clearPreferent()
    return redirect(url_for('home'))

# Creating rout to search posts
@app.route("/post/all")
def post_all():
    updateMode(request)
    if profile.isLogIn == False:
        return redirect(url_for('home'))
    else:
        posts = getPosts()
        return render_template('postMenu.html', title="Posts", profile = profile, posts = posts)

# Creating rout create new post
@app.route("/post/new", methods = ['GET', 'POST'])
def new_post():
    updateMode(request)
    if profile.isLogIn == False:
        return redirect(url_for('home'))
    else:
        # Creating Form
        form = NewPostForm()
        error = None
        if form.validate_on_submit():
            insertDataToPost(form, profile.username)
            return render_template('create_post.html', title='New Post', profile = profile, form = form)
        else: 
            return render_template('create_post.html', title='New Post', profile = profile, form = form)
            
        return render_template('create_post.html', title='New Post', profile = profile, form = form)