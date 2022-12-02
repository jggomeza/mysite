import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '581a109c4de363ddf453943aa35edfb48de47d2c6827220c705143ff2d50f921'
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

class DevelopmentConfig(Config):
    ENV="DEVELOPMENT"
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    DATABASE = os.environ.get('DEV_DATABASE_URL') or os.path.join(basedir, 'flaskr-dev.sqlite')

class TestingConfig(Config):
    ENV="TESTING"
    TESTING = True
    DATABASE = os.environ.get('TEST_DATABASE_URL') or os.path.join(basedir, 'flaskr-test.sqlite')

class ProductionConfig(Config):
    ENV="PRODUCTION"
    DATABASE = os.environ.get('DATABASE_URL') or os.path.join(basedir, 'flaskr.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}