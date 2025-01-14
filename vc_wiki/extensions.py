from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_babel import Babel

db = SQLAlchemy()
migrate = Migrate()
admin = Admin(name='GTA Vice City Wiki | Admin', template_mode='bootstrap4')
babel = Babel()
