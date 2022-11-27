from src import db


class KpiData(db.Model):
    __tablename__ = 'kpi_data'
    user_id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    kpi_id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
