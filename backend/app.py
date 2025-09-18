import flask 
from flask import request, jsonify
from web_scraper import web_scrape
from web_scraper.web_scrape import web_scrape
from ai_token.ai_tokenizer import ai_tokenizer
from ai.ai_process import ai_process
from flask_cors import CORS 

app = flask.Flask(__name__)
CORS(app)
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

@app.route('/ai_process', methods=['POST'])
def ai():
    url = request.json['url']
    ai_process_instance = ai_process()
    ai_response = ai_process_instance.summary(url)
    return jsonify({'ai_process': ai_response})

if __name__ == '__main__':
    app.run(debug=True)