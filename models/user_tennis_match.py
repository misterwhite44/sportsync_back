from database.db import db
from datetime import date

class UserTennisMatch(db.Model):
    __tablename__ = 'user_tennis_matches'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    opponent_name = db.Column(db.String(100))
    match_date = db.Column(db.Date)
    score = db.Column(db.String(20))
    competition = db.Column(db.String(100))
    location = db.Column(db.String(100))
