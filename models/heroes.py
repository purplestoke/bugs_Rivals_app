from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import UniqueConstraint
from website import db


class Heroes(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(25), nullable=True)
    rival_id = db.Column(db.String(4), nullable=True)
