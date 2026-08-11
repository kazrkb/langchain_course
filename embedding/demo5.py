from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

documents = [
    "What is machine learning?",
    "Machine learning is a branch of artificial intelligence.",
    "What is deep learning?",
    "Deep learning uses neural networks with multiple layers.",
    "What is RAG?",
    "RAG stands for Retrieval-Augmented Generation.",
    "How does a vector database work?",
    "A vector database stores and searches numerical embeddings.",
    "What is an embedding?",
    "An embedding converts text into a numerical vector.",
    "Python is a popular programming language.",
    "PyTorch is a framework for deep learning.",
    "Transformers are widely used in modern natural language processing.",
    "Natural language processing allows computers to understand human language.",
    "Cosine similarity measures the similarity between two vectors."
]


query = "What is an embedding?"

doc_vector = embedding.embed_documents(documents)
query_vector = embedding.embed_query(query)

similarities = cosine_similarity([query_vector], doc_vector)
print("Similarities between the query and documents:")
for i, similarity in enumerate(similarities[0]):
    print(f"Document: {documents[i]} - Similarity: {similarity}")   
    
    
