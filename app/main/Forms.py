from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired



#def check_duplicate_email():

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')




class RegisterForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	firstname = StringField('Firstname', validators=[DataRequired()])
	lastname = StringField('Lastname', validators=[DataRequired()])
	email = StringField('Email',validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Register')

class ProfileForm(FlaskForm):
	profile_img = FileField('img')
	username = StringField('username')
	about_me = TextAreaField('about_me')
	location = StringField('location')
	submit = SubmitField('update profile')

class FileForm(FlaskForm):
	img = FileField('img',validators=[FileRequired()])
