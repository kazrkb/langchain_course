from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

result = model.invoke("what is 4+5i and 2-3i ?")
print(result.content)