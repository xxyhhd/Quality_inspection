from app.extensions import db
from datetime import datetime
from .db_base import DB


class Ticket(db.Model, DB):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(20), index=True)
    summary = db.Column(db.Text)
    ticket_type = db.Column(db.String(10))
    assinge_date = db.Column(db.Date)  # 到组时间
    death_date = db.Column(db.Date, default=datetime.utcnow())  # 检查时间
    assigne_id = db.Column(db.Integer)
