import streamlit as st
import sys
import os
from dotenv import load_dotenv
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from LLMs.llm import LLM 
from graph import create_workflow  

load_dotenv()
app = create_workflow(LLM)

st.title("Custom Content Generator Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
word_limit = st.number_input("Enter the word limit for the output", min_value=100, step=100, value=200)

# Accept user input
if prompt := st.chat_input("What would you like me to write about?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Prepare the instruction with word limit
        instruction = f"Write a {word_limit}-word analysis on the topic: {prompt}"
        
        # Prepare context from previous messages
        context = "\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.messages[-5:]])
        
        inputs = {
            "initial_prompt": instruction,
            "context": context,
            "num_steps": 0,
            "llm_name": "llama3.1-8b-groq"
        }
        
        # Run the workflow
        output = app.invoke(inputs)
        
        full_response = output.get('final_doc', "No content generated.")
        
        message_placeholder.markdown(full_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})