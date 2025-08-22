from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocessing import preprocess

def get_recommendations(freelancer_skills, jobs, top_n=5):
    job_texts = [preprocess(desc) for _, _, desc in jobs]
    job_titles = [title for _, title, _ in jobs]

    # Add freelancer skills as a document
    documents = job_texts + [preprocess(freelancer_skills)]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    freelancer_vector = tfidf_matrix[-1]
    job_vectors = tfidf_matrix[:-1]

    similarities = cosine_similarity(freelancer_vector, job_vectors).flatten()
    scored_jobs = list(zip(job_titles, similarities))

    ranked = sorted(scored_jobs, key=lambda x: x[1], reverse=True)[:top_n]
    return ranked
