from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class RegisterForm(FlaskForm):
    username = StringField('Name of user: ', validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField('Password: ', validators=[DataRequired(), Length(min=6, max=40)])
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    submit = SubmitField('Register')
    
class LogInForm(FlaskForm):
    username = StringField('Name of user: ', validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField('Password: ', validators=[DataRequired(), Length(min=6, max=40)])
    submit = SubmitField('Log In')
    
class NewPostForm(FlaskForm):
    title = StringField('Title of your post: ', validators=[DataRequired(), Length(min=4, max=25)])
    contentPost = TextAreaField('The content with your post: ', validators=[DataRequired(), Length(min=60, max=1000)])
    submit = SubmitField('Crate Post')
    
def ValidateNameLogIn(listName, username):
    for name in listName:
        if name == username:
            return True
        else:
            return False
