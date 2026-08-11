from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st



load_dotenv()

model = ChatGroq(
    model_name="llama-3.1-8b-instant"
)

st.header("Chat with LLaMA 3.1-8B Instant")

user_input = st.text_input("Enter your prompt: ", "")
if st.button("Click to get response"):
    if user_input:
        result = model.invoke(user_input)
        st.write(result.content)
    else:
        st.write("Please enter a prompt to summarize.")