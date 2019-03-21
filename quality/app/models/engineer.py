from app.extensions import db
from .db_base import DB


class Engineer(db.Model, DB):
    id = db.Column(db.Integer, primary_key=True)
    itcode = db.Column(db.String(12), index=True)

