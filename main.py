from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.chat_history import InMemoryChatMessageHistory
import time

# Initialize the  LangChain wrapper for your local model
# model = ChatOllama(model="qwen2.5:3b", temperature=0.0)

# 1. Initialize our two distinct agents
agent_a = ChatOllama(model="qwen2.5:3b", temperature=0.7)
agent_b = ChatOllama(model="qwen2.5:3b", temperature=0.7)

# initializing the history of messages
history_a = InMemoryChatMessageHistory()
history_b = InMemoryChatMessageHistory()

# 3. The Starting Trigger (The topic they will discuss)
starting_topic = "talk "
print(f"Starting Prompt: {starting_topic}\n")

current_message = starting_topic


def main_Function():
    while True:
         
         user_input = input("User: ")

         if user_input.lower() == "exit":
             break
         
         #adding user input to the history of messages
         history_a.add_message(HumanMessage(content=user_input))
         response = agent_a.invoke(history_a.messages)
         history_a.add_message(AIMessage(content=response.content))

         print(f"Agent A: {response.content}\n")
         print("-" * 50)
         time.sleep(2) # Pause for 2 seconds so you can read it in real-time

         history_b.add_message(HumanMessage(content=response.content))
         response = agent_b.invoke(history_b.messages)
         history_b.add_message(AIMessage(content=response.content))

         print(response.content)


if __name__ == "__main__":
    main_Function()