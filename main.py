from flask import Flask, render_template
app = Flask(__name__)


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
