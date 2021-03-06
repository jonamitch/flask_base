import os
from secrets import secrets
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or secrets['SECRET_KEY']

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or secrets['MAIL_USERNAME']
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or secrets['MAIL_PASSWORD']
    ADMINS = ['joy.food.earth@gmail.com']

    MAX_CONTENT_LENGTH = 1024*1024
    UPLOAD_EXTENSIONS = ['.jpg', '.png', '.gif', '.bmp']
    STATIC_UPLOAD_FOLDER = "images"

