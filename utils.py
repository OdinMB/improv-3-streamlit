import streamlit as st

import os
import logging
import io
from datetime import datetime

from contextlib import contextmanager
from openai import OpenAI
from typing import List, Dict
from langchain_openai import ChatOpenAI
# from langchain_anthropic import ChatAnthropic

from settings import CREATE_LOG_FILES, LOGS_DIR
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.ERROR)

################

def get_llm(large: bool = True, max_tokens: int = 2000, temperature: int = 0) -> ChatOpenAI:
    if large:
        return ChatOpenAI(model="gpt-4o-2024-08-06", max_tokens=max_tokens, temperature=temperature)
        # return ChatAnthropic(model="claude-3-5-sonnet-20240620", max_tokens=max_tokens, temperature=temperature)
    else:
        return ChatOpenAI(model="gpt-4o-mini", max_tokens=max_tokens, temperature=temperature)

################

# Initialize OpenAI client
client = OpenAI()

def get_embedding(text: str) -> List[float]:
    try:
        response = client.embeddings.create(
            model="text-embedding-ada-002",
            input=text
        )
        return response.data[0].embedding
    except Exception as e:
        logging.error(f"Error getting embedding: {e}")
        return []

##############

# Set up logging to write to a file
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

# Create a new log file for this session
if CREATE_LOG_FILES:
    log_file = os.path.join(LOGS_DIR, f"search_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")

def log_message(message):
    print(message)
    if CREATE_LOG_FILES:
        with io.open(log_file, 'a', encoding='utf-8') as f:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write(f"{timestamp} - {message}\n")
            f.flush()  # Ensure the message is written immediately

@contextmanager
def conditional_spinner(text, condition):
    if condition:
        with st.spinner(text=text):
            yield
    else:
        yield
