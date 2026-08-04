from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os




load_dotenv()

llm = GoogleGenerativeAI(
    model="gemini-flash-latest",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

result = llm.invoke("Write a poem about a lonely robot in the style of Shakespeare.")

print(result)