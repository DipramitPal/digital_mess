import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    # DATABASE_URI = 'sqlite://:memory:'

class DevelopmentConfig(Config):
	DEBUG = True
	MYSQL_DATABASE_USER = 'root'
	MYSQL_DATABASE_PASSWORD = 'password'
	MYSQL_DATABASE_DB = 'digital_mess'
	MYSQL_DATABASE_HOST = 'localhost'


class ProductionConfig(Config):
	DEBUG = False
	MYSQL_DATABASE_USER = 'dipramit'
	MYSQL_DATABASE_PASSWORD = 'password'
	MYSQL_DATABASE_DB = 'livdemy'
	MYSQL_DATABASE_HOST = 'db4free.net'
	
