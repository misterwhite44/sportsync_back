from database.db import db

class Match(db.Model):
    __tablename__ = "matches"

    id = db.Column(db.Integer, primary_key=True)
    competition_id = db.Column(db.Integer)
    sport_id = db.Column(db.Integer)
    match_date = db.Column(db.DateTime)
    status = db.Column(db.String(20))
    venue = db.Column(db.String(100))