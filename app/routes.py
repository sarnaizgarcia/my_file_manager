from flask import render_template, flash, redirect, url_for

from app import app, db
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Silvia'}
    files = [
        {
            'author': {'username': 'Silvia'},
            'file_name': 'file1'
        },
        {
            'author': {'username': 'Roberto'},
            'file_name': 'file2'
        },
    ]
    return render_template('index.html', title='Home', user=user, files=files)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign in', form=form)
