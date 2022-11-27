from sqlalchemy import event
from src import db


class Kpi(db.Model):
    __tablename__ = 'kpi'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(1000))
    description = db.Column(db.String(1000))


# @event.listens_for(Kpi.__table__, 'after_create')
# def create_departments(*args, **kwargs):
#     db.session.add(Kpi(name='turnover', description='The employee attrition rate'))
#     db.session.add(Kpi(name='cdiff', description='Clostridium difficile infections'))
#     db.session.commit()