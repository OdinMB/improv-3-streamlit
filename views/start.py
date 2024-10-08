import streamlit as st

import time
from time import mktime

from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain.schema import HumanMessage
from typing import List, Dict
import json

import PyPDF2
import io

import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import partial

from authentication import authorize, authorized
from utils import get_llm, get_embedding, log_message
from settings import APP_NAME, FILES_DIR, SCRIPT_DIR

# Create a JSON output parser
json_parser = JsonOutputParser()

def generate_report_section(input_text: str, guidance: str, pdf_content: str = "") -> Dict[str, str]:
    # Combine input_text and pdf_content if pdf_content is provided
    combined_input = input_text + "\n\n" + pdf_content if pdf_content else input_text
    
    prompt_template = """\
    Input: {input}
    Guidance: {guidance}
    
    Write a report section based on the input and guidance provided above.

    The report section should be structured as follows:
    - Introduction (2 paragraphs): Highlight at least 2 specific achievements or events. Thank our donors and sponsors for making these achievements possible.
    - Nursing Service updates (2 paragraphs)
    - Half Way House / NEST updates (2 paragraphs)
    - Volunteering updates (2 paragraphs)
    - Other updates (2 paragraphs): Highlight at least 2 specific stories that lift the mood and give an impression of our culture.

    For each section, give a high-level summary of the year's most important events and achievements in that area.

    Here are some of our core values and principles. Try to incorporate these into your response.
    - Safe environment that allows people to grow
    - Focus on positive interpersonal relationships
    - Focus on people over process

    Format your response as a JSON object with the following keys (don't change the language of these keys):
    'introduction', 'nursing_service', 'halfway_house', 'volunteering', 'other'

    Put the entire section in one string (as opposed to a list of paragraphs). Use "\n\n" to demarcate paragraphs.
    """

    formatted_prompt = prompt_template.format(input=combined_input, guidance=guidance)
    messages = [HumanMessage(content=formatted_prompt)]
    model = get_llm(large=True, max_tokens=2000, temperature=0.2)
    response = model.invoke(messages)

    log_message(f"Generated report section: {response.content}")
    report_sections = json_parser.parse(response.content)
    return report_sections

# --- "main" ---

st.html("<h1 style='text-align: center'>" + APP_NAME + "</h1>")
authorize()

if authorized():
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        input_text = st.text_area("Input", height=150)
        guidance_text = st.text_area("Guidance", height=100)
        
        # Add PDF upload field
        uploaded_file = st.file_uploader("Upload a PDF file (optional)", type="pdf")
        
        submit_button = st.button(label='Go', type='primary', use_container_width=True)

    if submit_button:
        st.markdown("---")
        
        pdf_content = ""
        if uploaded_file is not None:
            # Read and extract text from the uploaded PDF
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.getvalue()))
            pdf_content = "\n".join(page.extract_text() for page in pdf_reader.pages)
        
        with st.spinner("Generating report sections..."):
            report_sections = generate_report_section(input_text, guidance_text, pdf_content)
            log_message(f"Report sections generated successfully")
            st.subheader("Generated Report Sections")
            
            st.markdown("### Introduction")
            st.markdown(report_sections['introduction'])
            
            st.markdown("### Nursing Service Updates")
            st.markdown(report_sections['nursing_service'])
            
            st.markdown("### Half Way House / NEST Updates")
            st.markdown(report_sections['halfway_house'])
            
            st.markdown("### Volunteering Updates")
            st.markdown(report_sections['volunteering'])
            
            st.markdown("### Other Updates")
            st.markdown(report_sections['other'])
            
            st.success("Done!")

