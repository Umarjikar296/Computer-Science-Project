from flask import Flask, render_template, request
import sqlite3
from recommender import get_recommendations

app = Flask(__name__)

def get_jobs_from_db():
    conn = sqlite3.connect("database/jobs.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, description FROM jobs")
    jobs = cursor.fetchall()
    conn.close()
    return jobs

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    skills = request.form["skills"]
    jobs = get_jobs_from_db()
    recommendations = get_recommendations(skills, jobs, top_n=5)
    return render_template("results.html", skills=skills, recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
