import os
#from flask_image_alchemy.storages import S3Storage
#from flask_image_alchemy.fields import StdImageField

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'freeflow.db')
        SQLALCHEMY_TRACK_MODIFICATIONS = False

	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
	#AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
	#AWS_SECRET_ACCESS_KEY =os.environ.get('AWS_SECRET_ACCESS_KEY')
	#AWS_REGION_NAME = os.environ.get('AWS_REGION_NAME', 'eu-central-1')
	#S3_BUCKET_NAME =  os.environ.get('AWS_REGION_NAME', 'haraka-local')
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	#LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
	MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    	#ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
	#REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
	#POST_PER_PAGE = 25
