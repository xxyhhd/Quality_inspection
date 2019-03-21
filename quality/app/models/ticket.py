# from app.extensions import db
# from datetime import datetime
# from .db_base import DB


# class Ticket(db.Model, DB):
#     id = db.Column(db.Integer, primary_key=True)
#     number = db.Column(db.String(20), index=True)
#     summary = db.Column(db.Text)
#     tike_type = db.Column(db.String(10))
#     check_date = db.Column(db.Date)  # 检查时间
#     death_date = db.Column(db.Date, default=datetime.utcnow())  # 到期时间
#     assigned_id = db.Column(db.Integer)
