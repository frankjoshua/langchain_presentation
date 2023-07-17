---
marp: true
---
# Unlocking the Potential of Langchain: Exploring the Capabilities of Artificial Intelligence in Language Processing
---
# Why Langchain is bad.
- Langchain's code makes it hard to customize or alter prompts.
- High dependence on model intelligence can cause issues with less advanced LLMs.
- Updates to models can invalidate all tuned prompts, complicating maintenance.
- Difficulty in allowing non-technical colleagues to work with prompts.
- Future LLM prompting will likely involve highly specialized prompts, potentially making current prompts obsolete.
---
# Why use Langchain
- Fast prototyping
- Improving rapidly
---
# Demo LLM
- The first basic building block of Langchain
---
# Divergence from Langchain
- The concept is challenging to describe without specific examples or concrete context.
- Lacks sufficient introspection,
- Incorporating a user interface (UI) would greatly enhance the user experience and make it more intuitive for users to interact with the LangChain software.
---
# In the spirit of quick prototyping

![](https://avatars.githubusercontent.com/u/128686189?s=48&v=4) Chainlit

Chainlit lets you create ChatGPT-like UIs on top of any Python code in minutes! Some of the key features include intermediary steps visualisation, element management & display (images, text, carousel, etc.) as well as cloud deployment.

https://docs.chainlit.io/overview

---
# ![](https://avatars.githubusercontent.com/u/128686189?s=48&v=4) Chainlit
- Build LLM Apps fast: Integrate seamlessly with an existing code base or start from scratch in minutes

- Visualize multi-steps reasoning: Understand the intermediary steps that produced an output at a glance

- Iterate on prompts: Deep dive into prompts in the Prompt Playground to understand where things went wrong and iterate

- Collaborate with teammates: Invite your teammates, create annotated datasets and run experiments together

- Share your app: Publish your LLM app and share it with the world (coming soon)

---
# Demo Chainlit
- Prompt playground
- Conversational Memory

---
# Question Answering Over Documents
## Steps
1. Search Data
    - Text
    - Vector Stores
2. Add Data to the Prompt
3. Send to the LLM (ChatGPT)

---
# Chainlit Concepts (brief overview)
- Elements
    - Images
    - Sources
- Actions
    - Buttons
- Ask User
    - Prompt for files
    - Ask for variables
- User Session
    - Keep documents in memory
---
# Demo Chainlit:
# Question Answering Over Documents
---

https://integrations.langchain.com/

---

# Modular Reasoning, Knowledge and Language (MRKL) system

---
https://www.llamaindex.ai/

LlamaIndex is a data framework designed to connect custom data sources to large language models (LLMs). It offers the following features:

Data Ingestion: It allows you to connect your existing data sources and formats (such as APIs, PDFs, documents, SQL, etc.) to use with a large language model application.

Data Indexing: LlamaIndex can store and index your data for different use cases. It can integrate with downstream vector store and database providers.

Query Interface: LlamaIndex provides a query interface that accepts any input prompt over your data and returns a knowledge-augmented response.

This makes LlamaIndex a simple and flexible tool for enhancing the capabilities of LLM applications by integrating them with custom data sources.

