from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.chat_history import InMemoryChatMessageHistory

# Initialize the  LangChain wrapper for your local model
model = ChatOllama(model="qwen2.5:3b", temperature=0.0)
history = InMemoryChatMessageHistory()

# 2. Send the prompt and print the response text
response = model.invoke("what is capital of england")

while True:
         
         user_input = input("User: ")

         if user_input.lower() == "exit":
             break
         
         #adding user input to the history of messages
         history.add_message(HumanMessage(content=user_input))

         #sending the history of messages to the model 
         response = model.invoke(history.messages)

         #adding the response from the model to the history of messages
         history.add_message(AIMessage(content=response.content))

         print(response.content)
