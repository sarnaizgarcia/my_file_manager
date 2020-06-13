from os import environ

from flask import Flask, render_template

from config import Config

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


if __name__ == '__main__':
    app.run(port=5001)
