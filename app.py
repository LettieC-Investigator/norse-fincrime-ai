import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

# Your API Key
os.environ["OPENAI_API_KEY"] = " os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY_HERE"




print("Loading your FinCrime Library... Please wait.")
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

print("\n--- Project Norse: Interactive Study Mode ---")
print("Type 'exit' to quit.")

while True:
    user_question = input("\nAsk a question about your documents: ")
    if user_question.lower() == 'exit':
        break
    
    response = query_engine.query(user_question)
    print(f"\nAI Answer:\n{response}")