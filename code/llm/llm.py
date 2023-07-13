from dotenv import load_dotenv, find_dotenv
import os

if os.getenv("OPENAI_API_KEY") is None:
    if not load_dotenv(find_dotenv()):
        raise Exception(".env not found and OPENAI_API_KEY not set") 
        
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9)
prediction = llm.predict("What would be a good title for an AI presentation on Large Langauge Models?")
print(prediction)