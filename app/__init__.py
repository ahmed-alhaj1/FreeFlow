
import os
from flask import Flask, render_template, flash, redirect, url_for, abort, g, session, request
from config import Config
#from flask_script import Manager
#from flask_dropzone import Dropzone
#from flask_bcrypt import check_password_hash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy as sql
from flask_migrate import Migrate, MigrateCommand
#from models import prepare_info
from wtforms import StringField, PasswordField,BooleanField, SubmitField
from flask_wtf import FlaskForm
#from Forms import LoginForm,RegisterForm, ProfileForm
import os
from flask import Flask, render_template, flash, redirect, url_for, abort, g, session, request
from config import Config
#from flask_script import Manager
from flask_dropzone import Dropzone
#from flask_bcrypt import check_password_hash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy as sql
from flask_migrate import Migrate, MigrateCommand
#from models import prepare_info
from wtforms import StringField, PasswordField,BooleanField, SubmitField
from flask_wtf import FlaskForm
#from app.main.Forms import LoginForm,RegisterForm, ProfileForm
import base64
#from flask_image_alchemy.storages import S3Storage
#from flask_image_alchemy.fields import StdImageField



basedir = os.path.abspath(os.path.dirname(__file__))
#s3_storage = S3Storage()
db = sql()
migrate = Migrate()
login_manager = LoginManager()
#login_manager.view = 'load_login' #######
login_manager.login_message = "You must be logged in to access this page."


def create_app(config_class = Config ):

	app = Flask(__name__)
	#manager.add_command('db', MigrateCommand)
	app.config.from_object(config_class)
	migrate.init_app(app,db)
	#config[config_class].init_app(app)
	db.init_app(app)
	#	s3_storage.init_app(app)
	login_manager.init_app(app)
	login_manager.view = 'load_login'
	from app.main import bp as main_bp
    	app.register_blueprint(main_bp)

	return app

from app import models
