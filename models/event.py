from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import UniqueConstraint
from website import db


class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    transaction_hash = db.Column(db.String(66), unique=True, nullable=False)

    def __init__(self, user_id, transaction_hash):
        self.user_id = user_id
        self.transaction_hash = transaction_hash
