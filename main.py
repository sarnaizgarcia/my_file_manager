from app.app import app, db
from app.models import User, File


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'File': File}


if __name__ == '__main__':
    app.run()
