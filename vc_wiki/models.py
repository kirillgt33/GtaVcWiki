from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .extensions import db
from slugify import slugify


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(22), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    image_url = db.Column(db.String(255))
    slug = db.Column(db.String(150), unique=True, nullable=False)
    __table_args__ = (
        db.UniqueConstraint('slug', name='uq_slug'),
    )

    def __init__(self, title, content, date, image_url=None):
        self.title = title
        self.content = content
        self.date = date
        self.image_url = image_url
        self.slug = slugify(title)  # Генерируем slug автоматически


class Transport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50))
    content = db.Column(db.Text)
    image_url = db.Column(db.String(255))


class Weapon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50))
    content = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    icon_url = db.Column(db.String(255))


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50))
    description = db.Column(db.Text)
    image_url = db.Column(db.String(255))
