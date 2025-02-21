import pandas as pd
import ollama
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load the CSV data
csv_file = 'amazon.csv'
data = pd.read_csv(csv_file)

# Initialize the embedding model (e.g., Sentence Transformers)
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate embeddings for the CSV data
def generate_embeddings(texts):
    return embedding_model.encode(texts)

# Convert the CSV data into embeddings
data['combined_text'] = data.apply(lambda row: ' '.join(row.astype(str)), axis=1)  # Combine all columns into a single text
data_embeddings = generate_embeddings(data['combined_text'].tolist())

# Function to retrieve relevant rows based on the query
def retrieve_relevant_data(query, top_k=3):
    query_embedding = generate_embeddings([query])
    similarities = cosine_similarity(query_embedding, data_embeddings)[0]
    top_indices = np.argsort(similarities)[-top_k:][::-1]  # Get top-k most similar rows
    return data.iloc[top_indices]

# Function to query the Ollama model with RAG
def query_ollama_with_rag(prompt, relevant_data):
    try:
        # Simplify the prompt and include relevant data
        simplified_prompt = f"Answer the user's question based on the following relevant data:\n{relevant_data}\n\nUser's question: {prompt}"
        response = ollama.generate(model='llama2', prompt=simplified_prompt)
        return response['response']
    except Exception as e:
        return f"Error: {str(e)}"

# Main chatbot loop
def chatbot():
    print("Welcome to the CSV Chatbot with RAG! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        # Retrieve relevant data using RAG
        relevant_data = retrieve_relevant_data(user_input)
        relevant_data_str = relevant_data.to_string(index=False)

        # Debug: Print the retrieved data
        print("Debug - Retrieved Relevant Data:")
        print(relevant_data_str)

        # Get the response from Ollama with RAG
        response = query_ollama_with_rag(user_input, relevant_data_str)

        print(f"Bot: {response}")

if __name__ == "__main__":
    chatbot()