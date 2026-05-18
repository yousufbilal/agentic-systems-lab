import ollama
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.chat_history import InMemoryChatMessageHistory

# how to generate a response from a model
response = ollama.generate(model='llama3.2:latest', prompt='what is your favorite color?')

print(response['response'])