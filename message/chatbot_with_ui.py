from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b")

st.title("Chatbot with UI")


user_input = st.chat_input("Type your message here...")
if user_input:
    if user_input.strip().lower() in ["exit", "quit"]:
        st.stop()
    
    with st.chat_message("user"):
        st.write(user_input)

    result = model.invoke(user_input)
    
    with st.chat_message("assistant"):
        st.write(result.content)
