import os
from datetime import datetime

from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename

from app.app import app, db
from app.forms import LoginForm, RegistrationForm, UploadForm
from app.models import User, File


@app.route('/')
@app.route('/index')
@login_required
def index():
    files = File.query.all()
    return render_template('index.html', title='Home', files=files)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign in', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are now registered.')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        f = form.file.data
        filename = secure_filename(form.file_name.data)
        file = File.query.filter_by(file_name=filename).first()
        if file in File.query.all():
            return render_template('500.html'), 500
        file_path = os.path.join(os.path.abspath(
            os.path.dirname(__file__)), 'files', filename)
        f.save(file_path)
        new_file = File(file_name=filename, upload_date=datetime.utcnow())
        new_file.path = os.path.abspath(file_path)
        new_file.size = os.path.getsize(file_path)
        new_file.user_id = current_user.id
        new_file.description = form.description.data
        new_file.hash_sha = new_file.encrypt_string(new_file.file_name)
        db.session.add(new_file)
        db.session.commit()
        flash(f'{filename} was successfully uploaded!!')
        return redirect(url_for('index'))
    return render_template('upload.html', form=form)
