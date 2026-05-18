from langchain_ollama import ChatOllama

# Initialize the  LangChain wrapper for your local model
model = ChatOllama(model="llama3.2:latest", temperature=0.7)

# 2. Send the prompt and print the response text
response = model.invoke("Your prompt goes here")
print(response.content)