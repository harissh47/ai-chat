import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify

class web_scrape:
    def data_extract(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    
    def extract_text_only(self, url):
        """Extract only text content from the webpage"""
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        
        # Get text and clean it
        text = soup.get_text()
        
        # Clean up whitespace
        # lines = (line.strip() for line in text.splitlines())
        # chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # text = ' '.join(chunk for chunk in chunks if chunk)
        
        return text
    
    def extract_article_text(self, url):
        """Extract text from article content specifically"""
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find article content (common selectors)
        article_selectors = [
            'article',
            '.article-content',
            '.post-content',
            '.entry-content',
            'main',
            '.content'
        ]
        
        article_text = ""
        for selector in article_selectors:
            article = soup.select_one(selector)
            if article:
                # Remove script and style elements
                for script in article(["script", "style"]):
                    script.decompose()
                
                article_text = article.get_text()
                break
        
        if not article_text:
            # Fallback to body text
            body = soup.find('body')
            if body:
                for script in body(["script", "style"]):
                    script.decompose()
                article_text = body.get_text()
        
        # Clean up whitespace
        lines = (line.strip() for line in article_text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        
        return text

# app = Flask(__name__)
# @app.route('/text', methods=['POST'])
# def text():
#     url = request.json['url']
#     web_scraper = web_scrape()
#     text = web_scraper.extract_text_only(url)
#     return jsonify({'text': text})
# @app.route('/article', methods=['POST'])
# def article():
#     url = request.json['url']
#     web_scraper = web_scrape()
#     article = web_scraper.extract_article_text(url)
#     return jsonify({'article': article})


# # if __name__ == "__main__":
#     app.run(debug=True)
    
    # url = "https://www.moneycontrol.com"
    # web_scraper = web_scrape()
    
    # print("=== Original method (returns soup object) ===")
    # soup = web_scraper.data_extract(url)
    # print(f"Type: {type(soup)}")
    # print(f"Length: {len(str(soup))} characters")
    
    # print("\n=== Text only extraction ===")
    # text_only = web_scraper.extract_text_only(url)
    # print(f"Text length: {len(text_only)} characters")
    # print(f"First 500 characters: {text_only[:500]}...")
    
    # print("\n=== Article text extraction ===")
    # article_text = web_scraper.extract_article_text(url)
    # print(f"Article text length: {len(article_text)} characters")
    # print(f"First 500 characters: {article_text[:500]}...")
