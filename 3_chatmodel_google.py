from langchain_google_genai import ChatGoogleGenerativeAI  # langchain_google is a module that provides an interface to Google's chat models
from dotenv import load_dotenv  # load_dotenv is a function that loads environment variables from a .env file

load_dotenv()
google_model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=1, max_tokens=10)  # ChatGoogle is an object we kept in a variable
google_result = google_model.invoke("What is the capital of India?")

print(google_result.content)  # print the result
