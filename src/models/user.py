# from src.db import db
from src import db
from flask_login import UserMixin
from sqlalchemy import event


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

# @event.listens_for(User.__table__, 'after_create')
# def create_users(*args, **kwargs):
#     db.session.add(User(email='gareth@cadman.com', password='1234', name='Gareth Cadman'))
#     db.session.commit()