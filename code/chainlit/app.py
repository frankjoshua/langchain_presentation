from dotenv import load_dotenv, find_dotenv
import os

if os.getenv("OPENAI_API_KEY") is None:
    if not load_dotenv(find_dotenv()):
        raise Exception(".env not found and OPENAI_API_KEY not set") 

import chainlit as cl
import asyncio 
import openai

import sys
sys.path.append('../basic_bot')
import basic_bot
sys.path.append('../qa_bot')
import qa_bot
sys.path.append('../chat_bot')
import chat_bot

bot = chat_bot

@cl.on_chat_start
async def start_chat():
    cl.user_session.set(
        "message_history",
        [{"role": "system", 
          "content": "Characters from the silicon valley tv show are acting. Gilfoyle (sarcastic) wants to push to production. Dinesh (scared) wants to write more tests. Richard asks the question."}],
    )
    await cl.Avatar(name="Gilfoyle", url="https://static.wikia.nocookie.net/silicon-valley/images/2/20/Bertram_Gilfoyle.jpg").send()
    await cl.Avatar(name="Dinesh", url="https://static.wikia.nocookie.net/silicon-valley/images/e/e3/Dinesh_Chugtai.jpg").send()


async def callback(message):
    await cl.Message(content=message).send()

@cl.on_message
async def main(message: str):
    global bot
    if message == "basic_bot":
        bot = basic_bot
        return
    if message == "qa_bot":
        bot = qa_bot
        return
    if message == "chat_bot":
        bot = chat_bot
        return

    await bot.onMessage(message, callback)