# models.py
from sqlalchemy import Column, Integer, String
# from db import Base
from extensions import db 

class Settings(db.Model):
    __tablename__ = "Settings"

    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String, nullable=False)
    api_key = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
