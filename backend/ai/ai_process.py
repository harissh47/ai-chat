from transformers import AutoModelForCausalLM, AutoTokenizer
# from ai_token import ai_tokenizer
from web_scraper.web_scrape import web_scrape
import json 
import subprocess
from openai import OpenAI
import os
from settings.settings import settings
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class ai_process():
    def __init__(self):
        print("web_scraper initialized")
        self.scraper=web_scrape()
        self.settings=settings()
        # self.text=self.scraper.extract_text_only(url)
        Name,API_KEY,URL=self.settings.get_settings()
    def summary(self,url):
        data = self.scraper.extract_text_only(url)
        if Name!="ollama":
            client = OpenAI(api_key=API_KEY)
        else:
        
            prompt=f"Summarize the following text in a concise report:\n\n{data}"
            print(prompt)
            result=subprocess.run(
            ["ollama","run","summarizer"],
            input=prompt.encode("utf-8"),
            capture_output=True,
             )
            print("result-------------------------------------------------------------------------------")
            print(result.stdout.decode("utf-8"))
        self.settings.set_settings(Name,API_KEY,URL)
        return result.stdout.decode("utf-8")
        # print(prompt)
        # result=client.chat.completions.create(
        #     model="gpt-4o-mini",
        #     messages=[{"role": "user", "content": prompt}]
        # )
        # return result.choices[0].message.content

# if __name__ == "__main__":
#     ai_process=ai_process("https://timesofindia.indiatimes.com/")
#     print(ai_process.summary())
