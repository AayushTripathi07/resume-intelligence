from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embedding(text):

    if not text.strip():
        text = "empty"

    embedding = model.encode(text)

    return embedding