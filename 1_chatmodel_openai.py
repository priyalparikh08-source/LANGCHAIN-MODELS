from langchain_openai import ChatOpenAI  # langchain_openai is a module that provides an interface to OpenAI's chat models
from dotenv import load_dotenv  # load_dotenv is a function that loads environment variables from a .env file

load_dotenv()
chat_model = ChatOpenAI(model="gpt-4", temperature=1, max_completion_tokens=10)  # ChatOpenAI is an object we kept in a variable
chat_result = chat_model.invoke("suggest three names for a tech company")  

print(chat_result.content)  # print the result

