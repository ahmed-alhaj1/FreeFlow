#from driver import db
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import uuid
import os
from flask import current_app, url_for
from flask_login import UserMixin
from hashlib import md5
import datetime
from app import db, login_manager

#from flask_image_alchemy.storages import S3Storage
#from flask_image_alchemy.fields import StdImageField

class Permission:
	FOLLOW = 1
	COMMENT = 2
	WRITE = 4
	MODERATE = 8
	ADMIN = 16



friends = db.Table('friends',
	db.Column('friend_id',db.Integer, db.ForeignKey('user.id')),
	db.Column('user_id',db.Integer, db.ForeignKey('user.id'))
	)



class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(32), index=True, unique = True)
	password = db.Column(db.String(32), index=True, unique=True )

	first_name = db.Column(db.String(64), index=True, unique = True)
	last_name = db.Column(db.String(64), index=True, unique = True)
	#remember = db.Column(db.Boolean , index = True , default = True)
	profile_img =db.column(db.Integer)
	about_me = db.Column(db.String(140))
	location = db.Column(db.String(64))
	#img = db.Column(STdImageField(storage = S3Storage(), validation={'thumbnail': {"width": 100, "height": 100, "crop": True}}), nullabl=True)
	img = db.column(db.LargeBinary)
	img_path = db.Column(db.String(32) , nullable = True)
	last_seen = db.Column(db.DateTime, default= datetime.datetime.utcnow())
	email = db.Column(db.String(64), index=True, unique = True)
	files = db.relationship('FileContents', backref ='owner', lazy= 'dynamic')
	his_friends = db.relationship('User', secondary=friends, primaryjoin=(friends.c.friend_id==id),
	secondaryjoin=(friends.c.user_id==id), backref=db.backref('friends', lazy='dynamic'),
	lazy = 'dynamic')
	#avatar_hash = db.Column(db.LargeBinary())

	def __init__(self, username, password, first_name, last_name, email):
		self.username = username
		#self.Id = Id
		self.password = generate_password_hash(password)
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
	def __repr__(self):
		return '<User %r>' %self.username
	def get_id(self):
		try:
			return unicode(self.id)
		except:
			return str(self.id)
	def check_password(self, password):
			return check_password_hash(self.password, password)
	def avatar_hash(self, size):
		digest = md5(self.email.lower().encode('utf-8')).hexdigest()
		return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)
	#def avater(self):
	#	url = 'https://secure.gravatar.com/avatar'
    #    hash = self.avatar_hash
        #hash = self.avatar_hash or self.gravatar_hash()
    #    return '{url}/{hash}?s={size}&d={default}&r=
    #    {rating}'.format(
    #    url=url, hash=hash, size=size, default=default,
    #    rating=rating)

	def get_password(self):
		return self.password
	def get_email(self):
		return self.email
	#@property
	def is_authenticated(self):
		return True
	#@property
	def is_active(self):
		return True
	def get_username(self):
		return self.username
#def rep_user_info():
	#user = db.query.filter_by(username='ahmed')
class Img_pfl(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key = True )
	data = db.Column(db.LargeBinary(), nullable=True)
	filename = db.Column(db.String(30), nullable=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<img_pfl %r>' % self.filename

class FileContents(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	data = db.Column(db.LargeBinary(), nullable=True)
	#size = db.Column(db.Integer, nullable=False)
	filename = db.Column(db.String(30), nullable=True)
	user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
	#friends = db.relationship('User', secondary =friends, primaryjoin = (friends.c.user_id= id))
	def __repr__(self):
			return '<FileContents %r>' % self.filename
	"""
	def __init__(data = None, filename = None , user_id= None):
		self.data = data
		self.filename = filename
	"""

def prepare_info(username):
	Id = make_id()
	date = get_date()
	dirname = 'uploads/'+username[0:3]+ str(date.year ) +Id[0:4]
	make_dir(dirname)
	return dirname


def make_id():
	return str(uuid.uuid4().fields[-1])[:5]
def get_date():
	return datetime.datetime.now()
def make_dir(path):
	os.mkdir(path)

def init_db():
	db.create_all()
