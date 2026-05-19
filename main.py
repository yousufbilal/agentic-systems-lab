from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.chat_history import InMemoryChatMessageHistory
import time

# 1. Initialize our two distinct agents
agent_a = ChatOllama(model="qwen2.5:3b", temperature=0.7)
agent_b = ChatOllama(model="qwen2.5:3b", temperature=0.7)

# 2. Give them separate memory histories so they keep track of the conversation
history_a = InMemoryChatMessageHistory()
history_b = InMemoryChatMessageHistory()

# 3. The Starting Trigger (The topic they will discuss)
starting_topic = "you two agent AI models just have a converstaion"
print(f"Starting Prompt: {starting_topic}\n")

# Setup the initial message to kick off the loop
current_message = starting_topic

while True:
    # --- Agent A's Turn ---
    history_a.add_message(HumanMessage(content=current_message))
    response_a = agent_a.invoke(history_a.messages)
    history_a.add_message(AIMessage(content=response_a.content))
    
    print(f"Agent A: {response_a.content}\n")
    print("-" * 50)
    time.sleep(1) # Pause for 2 seconds so you can read it in real-time
    
    # Pass Agent A's output as the input for Agent B
    current_message = response_a.content
    
    # --- Agent B's Turn ---
    history_b.add_message(HumanMessage(content=current_message))
    response_b = agent_b.invoke(history_b.messages)
    history_b.add_message(AIMessage(content=response_b.content))
    
    print(f"Agent B: {response_b.content}\n")
    print("-" * 50)
    time.sleep(1)
    
    # Pass Agent B's output back as the input for Agent A
    current_message = response_b.content