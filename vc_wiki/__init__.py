from flask import Flask
import os
from .admin import init_admin
from .extensions import db, migrate, babel
from .routes import main


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.config['UPLOAD_FOLDER'] = os.path.join('vc_wiki', 'static')

    # Настройки для Flask-Babel
    app.config['BABEL_DEFAULT_LOCALE'] = 'ru'
    app.config['BABEL_DEFAULT_TIMEZONE'] = 'Europe/Moscow'

    db.init_app(app)
    migrate.init_app(app, db)
    init_admin(app)
    babel.init_app(app)

    app.register_blueprint(main)

    return app
