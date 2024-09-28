import os
from dotenv import load_dotenv

from langchain_anthropic import ChatAnthropic

LLM = ChatAnthropic(model='claude-3-opus-20240229',anthropic_api_key=api_key)
# from langchain_fireworks import ChatFireworks
# from langchain_ollama import ChatOllama

# Load environment variables from .env file
load_dotenv()

# Initialize LLM
# LLM = ChatGroq(model="llama-3.1-8b-instant",
#                     temperature=0)

# LLM = ChatOpenAI(model="gpt-4o-2024-08-06",
#                         temperature=0)


# LLM = ChatGoogleGenerativeAI(
#     model="gemini-1.5-flash-exp-0827",
#     temperature=0,
#     )


# FIREWORKS_LLM = ChatFireworks(model="accounts/fireworks/models/llama-v3-70b-instruct")

# OLLAMA_LLM = ChatOllama(model="llama3.1",
#                         temperature=0,
#                         # format="json"
#                         )
