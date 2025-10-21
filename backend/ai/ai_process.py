from transformers import AutoModelForCausalLM, AutoTokenizer
# from ai_token import ai_tokenizer
from web_scraper.web_scrape import web_scrape
import json 
import subprocess
from openai import OpenAI
import os
from settings.settings import settings
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
from google import genai

class ai_process():
    def __init__(self):
        print("web_scraper initialized")
        self.scraper=web_scrape()
        self.settings=settings()
        # self.text=self.scraper.extract_text_only(url)
        
        self.Name,self.API_KEY,self.URL=self.settings.get_settings().values()
        print(self.Name,self.API_KEY,self.URL)
        

    def summary(self,url):
        data = self.scraper.extract_text_only(url)
        print(self.Name)
        if self.Name=="other":
            print("other is selected")
        elif self.Name=="google":
            print("google is selected")
            client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
            response = client.models.generate_content(
                model="gemini-2.5-pro",
                contents=f"""Summarize the following text in a concise report ,
                            give me a point by point summary , 
                            give me the recommendations of the stocks to buy or sell  with proper reasoning and based on the following text :
                            {data}"""
            )
            print(response.text)
            return response.text
        elif self.Name=="ollama":
            print("ai process is starting with ollama")
            prompt=f"Summarize the following text in a concise report:\n\n{data}"
            print(prompt)
            result=subprocess.run(
            ["ollama","run","summarizer"],
            input=prompt.encode("utf-8"),
            capture_output=True,
             )
            print("result-------------------------------------------------------------------------------")
            print(result.stdout.decode("utf-8"))
            print("ai process is done with ollama")
            return result.stdout.decode("utf-8")
        # self.settings.set_settings(self.Name,self.API_KEY,self.URL)
        
        # return result.stdout.decode("utf-8")
        # print(prompt)
        # result=client.chat.completions.create(
        #     model="gpt-4o-mini",
        #     messages=[{"role": "user", "content": prompt}]
        # )
        # return result.choices[0].message.content

# if __name__ == "__main__":
#     ai_process=ai_process("https://timesofindia.indiatimes.com/")
#     print(ai_process.summary())
