import streamlit as st

import time
from time import mktime

from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain.schema import HumanMessage
from typing import List, Dict
import json

import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import partial

from authentication import authorize, authorized
from utils import get_llm, get_embedding, log_message
from settings import APP_NAME, FILES_DIR, SCRIPT_DIR

# Create a JSON output parser
json_parser = JsonOutputParser()

# sample LLM function
def generate_query_variations(query: str) -> List[str]:
    prompt_template = """\
    Query: {query}
    Generate 3 variations of this query.
    Format your response as a JSON object that specifies a list 'variations'.
    """

    formatted_prompt = prompt_template.format(query=query)
    # log_message(formatted_prompt)

    messages = [HumanMessage(content=formatted_prompt)]
    model = get_llm(large=False, max_tokens=2000, temperature=0.0)
    response = model.invoke(messages)

    log_message(f"Query variations: {response.content}")
    variations = json_parser.parse(response.content)['variations']
    return variations

# --- "main" ---

st.html("<h1 style='text-align: center'>" + APP_NAME + "</h1>")
authorize()

if authorized():
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        submit_button = st.button(label='Go', type='primary', use_container_width=True)

    if submit_button:
        st.markdown("---")
        
        with st.spinner("Doing things ..."):
            generate_query_variations("Hello")
            log_message(f"Success")
            st.success("Done!")
