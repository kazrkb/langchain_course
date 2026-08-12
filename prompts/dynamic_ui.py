from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate


load_dotenv()

model = ChatGroq(
    model_name="llama-3.1-8b-instant"
)

st.header("Chat with LLaMA 3.1-8B Instant")

paper_input = st.selectbox(
    "Select a paper to summarize:",
    ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding", 
     "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis", 
     "AlphaFold: A Solution to a 50-Year-Old Grand Challenge in Biology"]
)

style_input = st.selectbox(
    "Select a style for the summary:",
    ["Concise", "Detailed", "Technical", "Code_Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select a length for the summary:",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (6-10 paragraphs)"]
)

template = PromptTemplate(
    input_variables=["paper_input", "style_input", "length_input"],
    template=(
        """ You are a research assistant. Your task is to summarize the following paper: {paper_input}.
            The summary should be written in a {style_input} style and should be {length_input}"""
    )
)

if st.button("Click to get summary"):
    if paper_input and style_input and length_input:
        prompt = template.format(
            paper_input=paper_input,
            style_input=style_input,
            length_input=length_input
        )
        result = model.invoke(prompt)
        st.write(result.content)
    else:
        st.write("Please select a paper, style, and length for the summary.")