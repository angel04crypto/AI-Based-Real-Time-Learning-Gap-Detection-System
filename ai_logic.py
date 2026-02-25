from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load pre-trained NLP model (local, free)
model = SentenceTransformer("all-MiniLM-L6-v2")

def analyze_explanation(student_text, reference_text):
    embeddings = model.encode([student_text, reference_text])
    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    if similarity >= 0.75:
        level = "Good Understanding"
        feedback = (
            "Your explanation matches the core idea of the concept."
        )

    elif similarity >= 0.5:
        level = "Partial Understanding"
        feedback = (
            "Your explanation is partially correct but misses important details."
        )

    else:
        level = "Learning Gap Detected"
        feedback = (
            "Your explanation does not align with the expected concept meaning."
        )

    return similarity, level, feedback
def find_missing_keywords(student_text, reference_text):
    student_words = set(student_text.lower().split())
    ref_words = set(reference_text.lower().split())
    missing = ref_words - student_words
    return list(missing)[:5]
