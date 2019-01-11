
import os
from flask import Flask, render_template, flash, redirect, url_for, abort, g, session, request
from config import Config
from flask_script import Manager
from flask_dropzone import Dropzone
from flask_bcrypt import check_password_hash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy as sql
from flask_migrate import Migrate, MigrateCommand
from models import prepare_info
from wtforms import StringField, PasswordField,BooleanField, SubmitField
from flask_wtf import FlaskForm
from Forms import LoginForm,RegisterForm, ProfileForm
import base64
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECURITY_KEY'] = 'secret'
app.config['DEBUG'] = True
app.config['ALLOWED_EXTENSIONS'] = set(["pdf", "docx", "doc"])
app.config.update(
	 UPLOADED_PATH=os.path.join(basedir, 'uploads'),
         DROPZONE_MAX_FILES=300,

)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))
dropzone = Dropzone(app)

db = sql(app)
Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='load_login'




def create_db():
	db.drop_all()
	db.create_all()


@login_manager.user_loader
def load_user(id):
	print(id)
	from models import User
	curr_user =  User.query.filter(User.id== int(id)).first()
	print("current user", type(curr_user))
	return curr_user

@app.route('/create_db')
def createdb():
	create_db()
	return redirect(url_for('home'))
@app.route('/')

def home():

        return render_template('home.html')
#########################################################
@app.route('/options', methods=['GET','POST'])
def options():

        if request.method == 'GET':
                if request.args['submit'] == 'login':
                        return redirect(url_for('load_login'))
                elif request.args['submit'] == 'register':
						return redirect(url_for('register'))
                else:
                        return None
        else:
                return render_template('home.html')


##########################################################
@app.route('/login', methods=['GET', 'POST'])
def load_login():
	from models import FileContents, User
	#if current_user.is_authenticated():
	#	return redirect(url_for('uploads'))

        #owner = User.query.filter_by(username='sofianx12').first()
	form = LoginForm()
	if form.validate_on_submit():
		userx = User.query.filter_by(username= form.username.data).first()

		if userx is None or userx.check_password(form.password.data) == False:
			flash('wrong password')
			return redirect(url_for('load_login'))
		print("I about set up login manager ")
		login_user(userx)
		return redirect(url_for('pre_upload'))
	return render_template('login1.html', title='Sign In', form=form)

##########################################################
@app.route('/logout')
@login_required
def sign_out():
	logout()
	flash("you have logged out ")
	return redirect(url_for('options'))




##########################################################
@app.route('/register', methods=['GET','POST'])
def register():

	from models import User

	form = RegisterForm()
	if form.validate_on_submit():
		user = User(form.username.data,form.password.data, form.firstname.data, form.lastname.data, form.email.data)
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('load_login'))
	return render_template('register1.html', title='Register', form=form)




###########################################################
@app.route('/EditProfile', methods=['GET','POST'])
def edit_profile():
	form = ProfileForm()
	if form.validate_on_submit():
		current_user.avatar_hash = form.profile_img.data
		if form.username.data !=None:
			current_user.username = form.username.data
		if form.about_me != None:
			current_user.about_me = form.about_me.data
		if form.location.data != None:
			current_user.location = form.location.data
		db.session.commit()
		flash('You have you changed your profile')
		#print(img.filename)
		return redirect(url_for('profile'))
	return render_template('EditProfile.html', form=form)

@app.route('/user_profile')
@login_required
def profile():
	from models import User, FileContents

	#user_files= fileCoentent.query.filter_by(use_id=username).first_or_404()
	return render_template('home_profile.html')

@app.route('/uploads')
def pre_upload():
	print(current_user.username)
	return render_template('upload.html')


@app.route('/upload_file', methods=['POST','GET'])
def upload_file():
	from models import FileContents, User

	#owner = User.query.filter_by(username=current_user.username).first()
	#print(owner.id , owner.username)

	if request.method == 'POST':


		input_file = request.files['file']
		print(input_file.filename, current_user.username)
		encoded_string = base64.b64encode(input_file.read())
		new_file = FileContents(data= encoded_string, filename=input_file.filename, user_id =current_user.id)
		db.session.add(new_file)
		db.session.commit()
		return (input_file.filename, "this file has been upload successfully")

@app.route('/profile')
def view_profile():

	return render_template('home_profile.html')



if __name__ == "__main__":
	#app.run(debug=True, host= '0.0.0.0', port =4000)
	manager.run()
