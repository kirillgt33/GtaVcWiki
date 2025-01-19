import os


class Config:
    SECRET_KEY = 'your_secret_key'
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{BASE_DIR}/wiki.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
