from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

model = ChatGroq(
    model_name="llama-3.1-8b-instant"
)

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    result = model.invoke(user_input)
    print(f"Ai : {result.content}")