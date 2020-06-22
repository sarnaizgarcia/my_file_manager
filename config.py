import os
import platform

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'marramiau'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 8
    ROOT_PATH = basedir
    ALLOWED_EXTENSIONS = ['jpg', 'png', 'pdf', 'txt', 'py', 'doc']
    if platform.system() == 'Linux':
        UPLOAD_FOLDER = 'opt/SGDF'
    if platform.system() == 'Windows':
        UPLOAD_FOLDER = 'C:\SGDF'
