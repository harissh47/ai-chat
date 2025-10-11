import os 
from flask import request, jsonify
from extensions import db
from models import Settings

class settings:
    def __init__(self):
        self.Name="ollama"
        self.API_KEY="NIL"
        self.URL="local ollama"
    def get_settings(self):
        settings = db.session.query(Settings).first()
        if settings:
            self.Name = settings.name
            self.API_KEY = settings.api_key
            self.URL = settings.url
        else:
            self.Name = "ollama"
            self.API_KEY = "NIL"
            self.URL = "local ollama"
        return {"Name":self.Name,"API_KEY":self.API_KEY,"URL":self.URL}
    
    def set_settings(self,Name,API_KEY,URL):
        self.Name=request.json['Name']
        self.API_KEY=request.json['API_KEY']
        self.URL=request.json['URL']
        settings = db.session.query(Settings).first()
        if settings:
            settings.name = self.Name
            settings.api_key = self.API_KEY
            settings.url = self.URL
            db.session.commit()
        else:
            settings = Settings(name=self.Name,api_key=self.API_KEY,url=self.URL)
            db.session.add(settings)
            db.session.commit()
        return {"message":"these are the new settings","Name":self.Name,"API_KEY":self.API_KEY,"URL":self.URL}
            
            