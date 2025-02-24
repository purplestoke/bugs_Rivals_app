from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
from website import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    eth_address = db.Column(db.String(42), unique=True, nullable=False)
    marvel_username = db.Column(db.String(50), unique=True, nullable=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    last_login = db.Column(db.DateTime, nullable=True)
    nonce = db.Column(db.String(20), nullable=True)

    def __init__(self, eth_address, marvel_username=None):
        self.eth_address = eth_address
        self.marvel_username = marvel_username
        self.created_at = datetime.now(timezone.utc) 
