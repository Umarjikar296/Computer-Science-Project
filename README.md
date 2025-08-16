# Freelance Job Matcher

This project is a prototype freelance job recommendation system.  
It matches freelancers to jobs using **TF-IDF** vectorization and **cosine similarity**.

## 🚀 Features
- Match freelancers and jobs based on skill-job similarity.
- Uses NLP (TF-IDF + cosine similarity).
- Simple, extensible, and easy to test.

## 📂 Files
- `matcher.py` → Main script for recommendations.
- `freelancers.csv` → Sample freelancer profiles.
- `jobs.csv` → Sample job postings.
- `requirements.txt` → Dependencies.

## ▶️ Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the matcher:
   ```bash
   python matcher.py
   ```

## 📊 Example Output
```
Top 2 job recommendations for Alice (Python, Machine Learning, Data Analysis):
  - Machine Learning Engineer (Score: 0.66)
  - Database Administrator (Score: 0.12)
```

---
This is Phase-2 of the Computer Science project. More features and a web interface will be added in later phases.
