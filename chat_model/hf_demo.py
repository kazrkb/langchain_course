from langchain_huggingface import HuggingFacePipeline
from dotenv import load_dotenv
import os
load_dotenv()

model = HuggingFacePipeline.from_model_id(
    model_id="meta-llama/Meta-Llama-3.1-8B-Instruct",
    task="conversational",
    max_new_tokens=512,
)

result = model.invoke("What is the capital of Bangladesh?")
print(result)