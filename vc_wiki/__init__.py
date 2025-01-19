from flask import Flask
import os
from .admin import init_admin
from .extensions import db, migrate, babel, login_manager
from .models import User
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
    babel.init_app(app)
    init_admin(app)

    login_manager.init_app(app)
    login_manager.login_view = 'main.login'

    # Указываем, как Flask-Login должен загружать пользователя
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(main)

    return app
