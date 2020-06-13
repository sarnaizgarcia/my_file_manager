from os import environ

from flask import Flask, render_template, flash, redirect, url_for

from config import Config
from forms import LoginForm

app = Flask(__name__)
app.config.from_object(Config)


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
            f'Ha iniciado sesión el usuario {form.username.data}, recuerdame={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Iniciar sesión', form=form)


if __name__ == '__main__':
    app.run(port=5001)
