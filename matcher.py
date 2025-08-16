import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets
freelancers = pd.read_csv("freelancers.csv")
jobs = pd.read_csv("jobs.csv")

# Combine job title + description for better representation
jobs["text"] = jobs["title"] + " " + jobs["description"]

# Vectorize freelancer skills and job text
vectorizer = TfidfVectorizer(stop_words="english")

# Fit on combined corpus (skills + job descriptions)
corpus = freelancers["skills"].tolist() + jobs["text"].tolist()
vectorizer.fit(corpus)

# Transform freelancers and jobs into vectors
freelancer_vectors = vectorizer.transform(freelancers["skills"])
job_vectors = vectorizer.transform(jobs["text"])

# Compute similarity
similarity_matrix = cosine_similarity(freelancer_vectors, job_vectors)

# Display top job matches for each freelancer
top_n = 2  # number of jobs to recommend

for i, freelancer in freelancers.iterrows():
    scores = list(enumerate(similarity_matrix[i]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    print(f"\nTop {top_n} job recommendations for {freelancer['name']} ({freelancer['skills']}):")
    for j, score in scores[:top_n]:
        print(f"  - {jobs.iloc[j]['title']} (Score: {score:.2f})")
