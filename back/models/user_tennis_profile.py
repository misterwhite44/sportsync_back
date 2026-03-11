from database.db import db
from datetime import datetime

class UserTennisProfile(db.Model):
    __tablename__ = 'user_tennis_profile'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    fft_id = db.Column(db.String(50))
    ranking = db.Column(db.String(20))
    club = db.Column(db.String(100))
