import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FCM_SERVER_KEY = os.environ.get("FCM_SERVER_KEY")
