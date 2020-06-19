from flask import render_template

from app.app import app, db


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.htlm'), 500
