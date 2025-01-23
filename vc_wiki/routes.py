from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, current_user, login_required
from .extensions import db
from .models import User, News, Transport, Weapon, Character, Mission
from .admin import CharacterAdminView

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
@main.route('/index')
def index():
    news_list = News.query.order_by(News.date.desc()).all()
    return render_template('index.html', news_list=news_list)


@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('main.index'))

        flash('Неверное имя пользователя или пароль.', 'error')

    return render_template('auth/login.html')


@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Пароли не совпадают!', 'warning')
            return redirect(url_for('main.register'))

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Пользователь с таким именем уже существует!', 'warning')
            return redirect(url_for('main.register'))

        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash('Регистрация прошла успешно! Войдите в систему.', 'success')
        return redirect(url_for('main.login'))

    return render_template('auth/register.html')


@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Вы вышли из системы.', 'success')
    return redirect(url_for('main.login'))


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
    missions_list = Mission.query.all()
    return render_template('missions.html', missions_list=missions_list)
