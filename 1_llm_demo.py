from langchain_openai import OpenAI # langchain_openai is a module that provides an interface to OpenAI's language models
from dotenv import load_dotenv # load_dotenv is a function that loads environment variables from a .env file

load_dotenv()   
llm = OpenAI(model="gpt-3.5-turbo-instruct")  # OpenAI is a object we kept in a variable

result = llm.invoke("What is the capital of India?")  # invoke is a method that takes a string input and returns a string output

print(result)  # print the result
