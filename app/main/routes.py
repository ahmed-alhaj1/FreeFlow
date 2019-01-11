
from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

from app import db
from app.main.Forms import LoginForm, RegisterForm, ProfileForm, FileForm

from app.models import User, FileContents, prepare_info, Img_pfl
#from app.translate import translate
from app.main import bp
from app import login_manager
from skimage import io
import base64











@login_manager.user_loader
def load_user(id):
	print(id)
	#from models import User
	curr_user =  User.query.filter(User.id== int(id)).first()
	print("current user", type(curr_user))
	return curr_user

@bp.route('/create_db')
def createdb():
    db.drop_all()
    db.create_all()
    return redirect(url_for('main.home'))
@bp.route('/')

def home():

        return render_template('home.html')
#########################################################
@bp.route('/options', methods=['GET','POST'])
def options():

        if request.method == 'GET':
                if request.args['submit'] == 'login':
                        return redirect(url_for('main.load_login'))
                elif request.args['submit'] == 'register':
						return redirect(url_for('main.register'))
                else:
                        return None
        else:
                return render_template('home.html')


##########################################################
@bp.route('/login', methods=['GET', 'POST'])
def load_login():
	#from models import FileContents, User
	#if current_user.is_authenticated():
	#	return redirect(url_for('uploads'))

        #owner = User.query.filter_by(username='sofianx12').first()
	form = LoginForm()
	if form.validate_on_submit():
		userx = User.query.filter_by(username= form.username.data).first()

		if userx is None or userx.check_password(form.password.data) == False:
			flash('wrong password')
			return redirect(url_for('main.load_login'))
		print("I about set up login manager ")
		login_user(userx)
		return redirect(url_for('main.pre_upload'))
	return render_template('login1.html', title='Sign In', form=form)

##########################################################
@bp.route('/logout')
@login_required
def sign_out():
	logout()
	flash("you have logged out ")
	return redirect(url_for('main.options'))




##########################################################
@bp.route('/register', methods=['GET','POST'])
def register():

    form = RegisterForm()
    if form.validate_on_submit():
        user = User(form.username.data,form.password.data, form.firstname.data, form.lastname.data, form.email.data)
        dirname = prepare_info(user.username)
        user.img_path = dirname
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.load_login'))
    return render_template('register1.html', title='Register', form=form)




###########################################################
@bp.route('/EditProfile', methods=['GET','POST'])
def edit_profile():
    form = ProfileForm()
    print("hie ")
    if form.validate_on_submit():

        #if form.profile_img != None
        #    io.imsave(,)
        dirname = None
        if form.username.data !=None:
            current_user.username = form.username.data
            dirname = prepare_info(current_user.username)

        if form.profile_img != None:
            print(type(form.profile_img.data), '/n', dirname)
            io.imsave(dirname+'img1.jpg', io.imread(form.profile_img.data))

        if form.about_me != None:
            current_user.about_me = form.about_me.data
        if form.location.data != None:
            current_user.location = form.location.data
        db.session.commit()
        flash('You have you changed your profile')
		#print(img.filename)
        return redirect(url_for('main.profile'))
    return render_template('EditProfile.html', form=form)


@bp.route('/EditProfilePic', methods = ['POST', 'GET'])
def edit_profile_img():
    if request.method == 'POST':
        input_img = request.files['file']
        print(input_img.filename)
        img_encd = base64.b64encode(io.imread(input_img))
        img = Img_pfl(data = img_encd, filename = input_img.filename, user_id = current_user.id)
        db.session.add(img)
        db.session.commit()
    return render_template('Edit_profile_pic.html')

@bp.route('/user_profile')
@login_required
def profile():

    return render_template('home_profile.html')

@bp.route('/uploads')
def pre_upload():
	print(current_user.username)
	return render_template('upload.html')


@bp.route('/upload_file', methods=['POST','GET'])
def upload_file():

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

@bp.route('/profile')
def view_profile():
	return render_template('home_profile.html', pf_img)



if __name__ == "__main__":
	#app.run(debug=True, host= '0.0.0.0', port =4000)
	manager.run()
