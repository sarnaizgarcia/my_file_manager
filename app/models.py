from datetime import datetime
from random import randint

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    can_delete = db.Column(db.Boolean, default=False)
    files = db.relationship('File', backref='author', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.username}>'


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(60), index=True, unique=True)
    upload_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    size = db.Column(db.Integer, default=randint(200, 900))
    hash_sha = db.Column(db.Integer, default=randint(200, 900))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<File {self.file_name}>'
