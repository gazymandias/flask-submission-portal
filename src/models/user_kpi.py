from src import db
from sqlalchemy import event, ForeignKey

class UserKpi(db.Model):
    __tablename__ = 'user_kpi'
    # test = db.Column(db.String(100))
    # id = db.Column(db.Integer,autoincrement=True,nullable=False,unique=True)
    user_id = db.Column(db.Integer, ForeignKey("user.id"), primary_key=True) # primary keys are required by SQLAlchemy
    kpi_id = db.Column(db.Integer, ForeignKey("kpi.id"), primary_key=True) # primary keys are required by SQLAlchemy

# @event.listens_for(UserKpi.__table__, 'after_create')
# def create_dummy_user_kpis(*args, **kwargs):
# #     db.session.add(UserKpi(user_id=1, kpi_id=1))
# #     db.session.add(UserKpi(user_id=2, kpi_id=2))
#     db.session.add(UserKpi(test='123',user_id=2, kpi_id=2))
#     db.session.commit()