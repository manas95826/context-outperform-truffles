import streamlit as st
import sys
import os
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from LLMs.llm import LLM 
from graph import create_workflow  

load_dotenv()

app = create_workflow(LLM)

st.title("Custom Content Generator")

word_limit = st.number_input("Enter the word limit for the output", min_value=100, step=100)
topic = st.text_area("Enter the topic or instruction for the content")

generated_content = ""

if st.button("Generate Content"):
    if topic:
        instruction = f"Write a {word_limit}-word analysis on the topic: {topic}"
        
        inputs = {"initial_prompt": instruction,  
                  "num_steps": 0,
                  "llm_name": "llama3.1-8b-groq"}  
        
        # Run the workflow
        output = app.invoke(inputs)

        # Display the generated content
        generated_content = output.get('final_doc', "No content generated.")
        st.text_area("Generated Content", value=generated_content, height=300)
    else:
        st.warning("Please enter a topic to generate content.")
