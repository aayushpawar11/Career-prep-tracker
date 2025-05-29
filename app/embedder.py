from sentence_transformers import SentenceTransformer
from parser import parse_resume

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_resume_embedding(resume_path):
    parsed = parse_resume(resume_path)
    combined_text = "\n".join([
        parsed["education"],
        parsed["experience"],
        parsed["projects"],
        parsed["coursework"],
        ", ".join(parsed["skills"])
    ])

    embedding = model.encode(combined_text, convert_to_tensor=False)
    return embedding
if __name__ == "__main__":
    emb = get_resume_embedding("sample_resume.pdf")
    print("Embedding shape:", len(emb))
    print("Sample values:", emb[:10])
