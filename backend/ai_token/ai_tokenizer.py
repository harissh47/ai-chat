from transformers import BertTokenizer
from web_scraper.web_scrape import web_scrape

class ai_tokenizer:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-uncased')
        self.scraper = web_scrape()
        # self.url="https://timesofindia.indiatimes.com/"
    def tokenize_text(self,url):
        text=self.scraper.extract_text_only(url)
        tokens=self.tokenizer.tokenize(text)
        tokens_id=self.tokenizer.convert_tokens_to_ids(tokens)

        encoding = self.tokenizer (
            text,
            add_special_tokens=True,
            max_length=128,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )
        print(text)

        print(encoding)
        return text
# if __name__ == "__main__":
#     tokenizer = ai_tokenizer()
#     tokenizer.tokenize_text()




