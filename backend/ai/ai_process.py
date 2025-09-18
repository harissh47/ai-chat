from transformers import AutoModelForCausalLM, AutoTokenizer
# from ai_token import ai_tokenizer
from web_scraper.web_scrape import web_scrape
import json 
import subprocess

class ai_process():
    def __init__(self):
        self.scraper=web_scrape()
        # self.text=self.scraper.extract_text_only(url)
        
    def summary(self,text):
        data = self.scraper.extract_text_only(text)
        prompt=f"Summarize the following text in a concise report:\n\n{data}"
        result=subprocess.run(
            ["ollama","run","summarizer"],
            input=prompt.encode("utf-8"),
            capture_output=True,
        )
        return result.stdout.decode("utf-8")

# if __name__ == "__main__":
#     ai_process=ai_process("https://timesofindia.indiatimes.com/")
#     print(ai_process.summary())
