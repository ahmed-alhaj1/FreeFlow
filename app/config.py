import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'freeflow.db')
        SQLALCHEMY_TRACK_MODIFICATIONS = False

	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
	MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    	#ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
	#REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
	#POST_PER_PAGE = 25
