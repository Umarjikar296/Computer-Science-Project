import sqlite3
import os

def init_db():
    os.makedirs("database", exist_ok=True)  # ensure folder exists
    conn = sqlite3.connect("database/jobs.db")
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS jobs")
    cursor.execute("""
        CREATE TABLE jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            description TEXT
        )
    """)

    jobs = [
        ("Python Developer", "Looking for Python developer with NLP experience"),
        ("Frontend Developer", "React-based UI development for e-commerce website"),
        ("Data Scientist", "Data analysis, machine learning, and model deployment"),
        ("Java Engineer", "Backend APIs using Java and Spring Boot"),
        ("UI/UX Designer", "Designing Figma wireframes and user flows")
    ]

    cursor.executemany("INSERT INTO jobs (title, description) VALUES (?, ?)", jobs)
    conn.commit()
    conn.close()
    print("Database initialized with sample jobs!")

if __name__ == "__main__":
    init_db()
