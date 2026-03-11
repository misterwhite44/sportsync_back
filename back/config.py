import os

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/sport_tracker"
    SQLALCHEMY_TRACK_MODIFICATIONS = False