import flask 
from flask import request, jsonify
from web_scraper import web_scrape
from web_scraper.web_scrape import web_scrape
from ai_token.ai_tokenizer import ai_tokenizer
from ai.ai_process import ai_process
from settings.settings import settings
from flask_cors import CORS 
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os
from extensions import db,migrate
from models import Settings
# db = SQLAlchemy()
# migrate = Migrate()
app = flask.Flask(__name__)
# db = SQLAlchemy()
# migrate = Migrate()
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
settings_instance = settings()
CORS(app)
db.init_app(app)
migrate.init_app(app, db)

@app.route('/summary', methods=['POST'])
def summary():
    url = request.json['url']
    ai_process = ai_process(url)
    summary = ai_process.summary()
    return jsonify({'summary': summary})

@app.route('/tokenize', methods=['POST'])
def tokenize():
    url = request.json['url']
    tokens_instance = ai_tokenizer()
    tokens = tokens_instance.tokenize_text(url)
    # tokenize = ai_tokenizer.tokenize()
    return jsonify({'tokenize': tokens})

@app.route('/settings_save', methods=['POST'])
def settings_save():
    # settings_instance = settings()

    return jsonify(settings_instance.set_settings(request.json['Name'],request.json['API_KEY'],request.json['URL']))
    # return jsonify({'settings': settings_instance.get_settings()})

@app.route('/settings_get', methods=['GET'])
def settings_get():
    # settings_instance = settings()
    settings_instance.get_settings()
    return jsonify(settings_instance.get_settings())

@app.route('/ai_process', methods=['POST'])
def ai():
    url = request.json['url']
    ai_process_instance = ai_process()
    ai_response = ai_process_instance.summary(url)
    return jsonify({'ai_process': ai_response})

if __name__ == '__main__':
    app.run(debug=True)