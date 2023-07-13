from dotenv import load_dotenv, find_dotenv
import os

if os.getenv("OPENAI_API_KEY") is None:
    if not load_dotenv(find_dotenv()):
        raise Exception(".env not found and OPENAI_API_KEY not set") 

import os
import openai

from llama_index.callbacks.base import CallbackManager
from llama_index import (
    LLMPredictor,
    ServiceContext,
    StorageContext,
    load_index_from_storage,
)
from langchain.chat_models import ChatOpenAI
import chainlit as cl

openai.api_key = os.environ.get("OPENAI_API_KEY")

STREAMING = True

try:
    # rebuild storage context
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    # load index
    index = load_index_from_storage(storage_context)
except:
    from llama_index import GPTVectorStoreIndex, SimpleWebPageReader

    documents = SimpleWebPageReader(html_to_text=True).load_data(
        [
            "https://wiki.monai.art/en/home/faq",
            "https://wiki.monai.art/en/tutorials/negative_embeddings",
            "https://wiki.monai.art/en/tutorials/prompt_weighting",
            "https://wiki.monai.art/en/tutorials/tokens"
        ]
    )
    index = GPTVectorStoreIndex.from_documents(documents)
    index.storage_context.persist()


@cl.llama_index_factory
async def factory():
    llm_predictor = LLMPredictor(
        llm=ChatOpenAI(
            temperature=0,
            model_name="gpt-3.5-turbo",
            streaming=STREAMING,
        ),
    )
    service_context = ServiceContext.from_defaults(
        llm_predictor=llm_predictor,
        chunk_size=512,
        callback_manager=CallbackManager([cl.LlamaIndexCallbackHandler()]),
    )

    query_engine = index.as_query_engine(
        service_context=service_context,
        streaming=STREAMING,
    )

    return query_engine