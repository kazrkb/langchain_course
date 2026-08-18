from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
import os

load_dotenv()
st.title("Chatbot with UI")
model = ChatGroq(model="openai/gpt-oss-20b")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    
#Display previous messages
for message in st.session_state.chat_history:
    role = "assistant" if isinstance(message, AIMessage) else "user"
    with st.chat_message(role):
        st.write(message.content)
        
# Get user input
user_input = st.chat_input("Type your message here...")
if user_input:
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.write(user_input)


