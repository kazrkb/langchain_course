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
    if user_input.strip().lower() == "exit":
        st.stop()

    st.session_state.chat_history.append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.write(user_input)

    messages = [
        SystemMessage(content="You are a helpful assistant."),
        *st.session_state.chat_history,
    ]
    response = model.invoke(messages)
    st.session_state.chat_history.append(AIMessage(content=response.content))

    with st.chat_message("assistant"):
        st.write(response.content)

# Print chat history for debugging
with st.sidebar:
    st.subheader("Chat History")
    if not st.session_state.chat_history:
        st.write("No messages yet.")
    else:
        for message in st.session_state.chat_history:
            role = "assistant" if isinstance(message, AIMessage) else "user"
            st.write(f"{role}: {message.content}")
        
        
        
        
        
        
        
        
        
        
        
        
        