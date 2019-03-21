from app.extensions import db
from .db_base import DB  # 导入模型操作的基类


class Process(db.Model, DB):
    id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.Integer)
    engineer_id = db.Column(db.Integer)
    time = db.Column(db.Date)
    process_one = db.Column(db.Boolean)
    process_two = db.Column(db.Boolean)