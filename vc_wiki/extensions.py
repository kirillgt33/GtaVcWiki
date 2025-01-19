from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_babel import Babel
from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()
admin = Admin(name='GTA Vice City Wiki | Admin', template_mode='bootstrap4')
babel = Babel()
login_manager = LoginManager()
