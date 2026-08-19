from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict

import os

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b")

# define the schema
class ResumeAnalysisSchema(TypedDict):
    candiate_name: str
    
    
# create structured output
structured_model = model.with_structured_output(ResumeAnalysisSchema)

# invoke the model with structured output
response = structured_model.invoke(
    "Analyze the following resume and extract the candidate's name: John Doe, experienced software engineer with a background in AI and machine learning."
)

print(response)