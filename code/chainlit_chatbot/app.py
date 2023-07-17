import os
from langchain import PromptTemplate, OpenAI, LLMChain
import chainlit as cl

from dotenv import load_dotenv, find_dotenv
import os

if os.getenv("OPENAI_API_KEY") is None:
    if not load_dotenv(find_dotenv()):
        raise Exception(".env not found and OPENAI_API_KEY not set") 

import sys
sys.path.append('../chat_bot')
from chat_bot import getBot

@cl.langchain_factory(use_async=True)
def factory():
    return getBot()