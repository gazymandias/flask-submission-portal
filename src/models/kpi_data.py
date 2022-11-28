from src import db
from sqlalchemy import ForeignKey, DateTime, func

class KpiData(db.Model):
    __tablename__ = 'kpi_data'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, ForeignKey("user.id"), nullable=False)
    kpi_id = db.Column(db.Integer, ForeignKey("kpi.id"), nullable=False)
    numerator = db.Column(db.Integer, nullable=False)
    denominator = db.Column(db.Integer, nullable=False)
    submitted_at = db.Column(DateTime(timezone=True), nullable=False)

