import os
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import FileUploadField
from wtforms.fields import SelectField
from flask import current_app
from .models import News, Transport, Weapon, Character
from .extensions import db, admin
from slugify import slugify


class NewsAdminView(ModelView):
    column_exclude_list = ['slug']  # Исключить slug из списка отображения
    form_excluded_columns = ['slug']  # Исключить slug из формы редактирования

    form_overrides = {
        'image_url': FileUploadField
    }

    form_args = {
        'title': {
            'label': 'Название'
        },
        'content': {
            'label': 'Описание'
        },
        'date': {
            'label': 'Дата'
        },
        'image_url': {
            'label': 'Изображение',
            'base_path': lambda: os.path.join(current_app.config['UPLOAD_FOLDER'], 'images', 'news'),
            'allow_overwrite': True
        }
    }

    def on_model_change(self, form, model, is_created):
        if not model.slug:
            model.slug = slugify(model.title)


class TransportAdminView(ModelView):
    # Переопределяем поле для загрузки файлов
    form_overrides = {
        'image_url': FileUploadField,
        'type': SelectField
    }

    # Настраиваем параметры для поля загрузки изображений
    form_args = {
        'title': {
            'label': 'Название'
        },
        'type': {
            'label': 'Тип',
            'choices': [
                ('Trucks and minivans', 'Грузовики и минивэны'),
                ('Gangster rydvans', 'Гангстерские рыдваны'),
                ('All-wheel drive SUVs', 'Полноприводные внедорожники'),
                ('Classic cars', 'Классические автомобили'),
                ('Sports cars', 'Спортивные автомобили'),
                ('Family station wagons and buses', 'Семейные универсалы и автобусы'),
                ('Transport of city services', 'Транспорт городских служб'),
                ('Law enforcement vehicles', 'Транспорт служителей закона'),
                ('Other types of transport', 'Прочие виды транспорта'),
            ]
        },
        'content': {
            'label': 'Описание'
        },
        'image_url': {
            'label': 'Изображение',
            'base_path': lambda: os.path.join(current_app.config['UPLOAD_FOLDER'], 'images', 'transports'),
            'allow_overwrite': True
        }
    }


class WeaponAdminView(ModelView):
    form_overrides = {
        'image_url': FileUploadField,
        'icon_url': FileUploadField,
        'type': SelectField
    }

    form_args = {
        'title': {
            'label': 'Название'
        },
        'type': {
            'label': 'Тип',
            'choices': [
                ('Hand-to-hand combat', 'Рукопашная схватка'),
                ('Melee weapons', 'Холодное оружие'),
                ('Explosives', 'Взрывчатка'),
                ('Pistols', 'Пистолеты'),
                ('Shotguns', 'Дробовики'),
                ('Light automatic weapons', 'Легкое автоматическое оружие'),
                ('Submachine guns', 'Автоматы'),
                ('Heavy weapons', 'Тяжелое оружие'),
                ('Sniper rifles', 'Снайперские винтовки'),
            ]
        },
        'content': {
            'label': 'Описание'
        },
        'image_url': {
            'label': 'Изображение',
            'base_path': lambda: os.path.join(current_app.config['UPLOAD_FOLDER'], 'images', 'weapons'),
            'allow_overwrite': True
        },
        'icon_url': {
            'label': 'Иконка',
            'base_path': lambda: os.path.join(current_app.config['UPLOAD_FOLDER'], 'images', 'weapons', 'icons'),
            'allow_overwrite': True
        }
    }


class CharacterAdminView(ModelView):
    form_overrides = {
        'image_url': FileUploadField,
        'role': SelectField
    }

    form_args = {
        'name': {
            'label': 'Имя'
        },
        'role': {
            'label': 'Роль',
            'choices': [
                ('Protagonist', 'Главный герой'),
                ('Major characters', 'Главные персонажи'),
                ('Minor characters', 'Второстепенные персонажи'),
            ]
        },
        'description': {
            'label': 'Описание'
        },
        'image_url': {
            'label': 'Изображение',
            'base_path': lambda: os.path.join(current_app.config['UPLOAD_FOLDER'], 'images', 'characters'),
            'allow_overwrite': True
        }
    }


def init_admin(app):
    # Подключаем Flask-Admin к приложению Flask
    admin.init_app(app)
    admin.add_view(NewsAdminView(News, db.session))
    admin.add_view(TransportAdminView(Transport, db.session))
    admin.add_view(WeaponAdminView(Weapon, db.session))
    admin.add_view(CharacterAdminView(Character, db.session))
