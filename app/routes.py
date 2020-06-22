import os
import sys
from datetime import datetime

from flask import render_template, flash, redirect, url_for, request, send_from_directory
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
    page = request.args.get('page', 1, type=int)
    files = File.query.order_by(File.upload_date.desc()).paginate(
        page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for(
        'index', page=files.next_num) if files.has_next else None
    prev_url = url_for(
        'index', page=files.prev_num) if files.has_prev else None
    return render_template('index.html', title='Home', files=files.items,
                           next_url=next_url, prev_url=prev_url)


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
        file_name = f.filename
        file_name = secure_filename(f.filename)  # Real filename
        file = File.query.filter_by(file_name=file_name).first()
        if file in File.query.all():
            flash('Ya existe un archivo con ese nombre.')
            return render_template('500.html'), 500
        upload_folder = app.config['UPLOAD_FOLDER']
        if os.path.isdir(upload_folder) == False:
            os.makedirs(upload_folder)
        file_path = os.path.join(upload_folder, file_name)  # filename
        f.save(file_path)
        new_file = File(file_name=file_name, upload_date=datetime.utcnow())
        new_file.path = os.path.abspath(file_path)
        new_file.size = os.path.getsize(file_path)
        new_file.user_id = current_user.id
        new_file.description = form.description.data
        new_file.hash_sha = new_file.encrypt_string(new_file.file_name)
        db.session.add(new_file)
        db.session.commit()
        flash(f'{file_name} was successfully uploaded!!')
        return redirect(url_for('index'))
    return render_template('upload.html', form=form)


@app.route('/download/<filename>')
@login_required
def download_file(filename):
    full_path = os.path.join(
        app.config['ROOT_PATH'], app.config['UPLOAD_FOLDER'])
    return send_from_directory(full_path, filename, as_attachment=True)


@app.route('/delete/<filename>', methods=['GET', 'POST'])
@login_required
def delete_file(filename):
    file = File.query.filter_by(file_name=filename).first()
    full_path = os.path.join(
        app.config['ROOT_PATH'], app.config['UPLOAD_FOLDER'], file.file_name)
    os.remove(full_path)

    db.session.delete(file)
    db.session.commit()
    flash(f'File {file.file_name} has been removed')
    return redirect(url_for('index'))
