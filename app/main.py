from fastapi import FastAPI
from pymongo import MongoClient
from sqlalchemy import create_engine
import pandas as pd

app = FastAPI(title="Student Performance Early Warning System")

# ---------------- DATABASE CONNECTIONS ----------------
engine = create_engine(
    "postgresql://postgres:admin123@localhost:5432/student_performance"
)

client = MongoClient("mongodb://localhost:27017/")
db = client["student_bigdata"]
collection = db["students"]

# ---------------- HOME ----------------
@app.get("/")
def home():
    return {
        "message": "Student Performance API is running"
    }

# ---------------- RUN PIPELINE (OPTIONAL TRIGGER) ----------------
@app.get("/data")
def get_data():
    df = pd.read_sql("SELECT * FROM students", engine)
    return df.to_dict(orient="records")

# ---------------- AT-RISK STUDENTS ----------------
@app.get("/at-risk")
def at_risk():
    df = pd.read_sql("SELECT * FROM students", engine)
    risky = df[df["Performance_Level"] == "At-Risk"]
    return risky.to_dict(orient="records")

# ---------------- SUMMARY STATS ----------------
@app.get("/stats")
def stats():
    df = pd.read_sql("SELECT * FROM students", engine)

    return {
        "total_students": len(df),
        "at_risk": len(df[df["Performance_Level"] == "At-Risk"]),
        "average": len(df[df["Performance_Level"] == "Average"]),
        "high": len(df[df["Performance_Level"] == "High"])
    }