from flask import Blueprint, render_template
from .models import News, Transport, Weapon, Character
from .admin import CharacterAdminView

main = Blueprint('main', __name__)


@main.route('/')
def index():
    news_list = News.query.order_by(News.date.desc()).all()
    return render_template('index.html', news_list=news_list)


@main.route('/news/<slug>')
def news_detail(slug):
    news_item = News.query.filter_by(slug=slug).first_or_404()
    return render_template('news_detail.html', news_item=news_item)


@main.route('/transports')
def transports():
    transports_list = Transport.query.order_by(Transport.title.asc()).all()
    return render_template('transports.html', transports_list=transports_list)


@main.route('/weapons')
def weapons():
    weapons_list = Weapon.query.order_by(Weapon.title.asc()).all()
    return render_template('weapons.html', weapons_list=weapons_list)


@main.route('/characters')
def characters():
    characters_list = Character.query.all()

    role_choices = CharacterAdminView.form_args['role']['choices']

    for character in characters_list:
        character.role_label = next((label for value, label in role_choices if value == character.role), 'Неизвестная роль')
    return render_template('characters.html', characters_list=characters_list)


@main.route('/missions')
def missions():
    return render_template('missions.html')
