from langchain_anthropic import ChatAnthropic  # langchain_anthropic is a module that provides an interface to Anthropic's chat models
from dotenv import load_dotenv  # load_dotenv is a function that loads environment variables from a .env file

load_dotenv()
anthropic_model = ChatAnthropic(model="claude-3", temperature=1, max_tokens=10)  
anthropic_result = anthropic_model.invoke("What is the capital of India?")

print(anthropic_result.content)  # print the result