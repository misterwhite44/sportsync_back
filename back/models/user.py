from database.db import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    tennis_profile = db.relationship('UserTennisProfile', backref='user', uselist=False)

class UserMatch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    sport = db.Column(db.String(20), nullable=False)
    opponent = db.Column(db.String(100))
    score = db.Column(db.String(50))
    result = db.Column(db.String(10))
    match_date = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)