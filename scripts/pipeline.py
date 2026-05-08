import pandas as pd
from sqlalchemy import create_engine
from pymongo import MongoClient

# ---------------- LOAD DATA ----------------
df = pd.read_csv("../data/students.csv")

print("✔ Data loaded")

# ---------------- CLEAN DATA ----------------
df.dropna(inplace=True)

print("✔ Missing values removed")

# ---------------- RULE-BASED CLASSIFICATION ----------------
def classify(row):
    if row["class_failures"] >= 2 or row["absences"] > 20:
        return "At-Risk"
    elif str(row["study_time"]) == "<2 hours":
        return "Average"
    else:
        return "High"

df["Performance_Level"] = df.apply(classify, axis=1)

print("✔ Rule-based classification completed")

# ---------------- PROPOSED ML MODELS (NO TRAINING) ----------------
print("\n📌 Proposed Machine Learning Models for Future Implementation:")
print("1. Decision Tree Classifier - interpretable, matches rule-based logic")
print("2. Random Forest Classifier - higher accuracy, handles noisy data")
print("3. Logistic Regression - baseline classification model")

# ---------------- POSTGRESQL STORAGE ----------------
try:
    engine = create_engine(
        "postgresql://postgres:admin123@localhost:5432/student_performance"
    )

    df.to_sql("students", engine, if_exists="replace", index=False)
    print("✔ Data saved to PostgreSQL")

except Exception as e:
    print("❌ PostgreSQL Error:", e)

# ---------------- MONGODB STORAGE ----------------
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["student_bigdata"]
    collection = db["students"]

    collection.delete_many({})
    collection.insert_many(df.to_dict(orient="records"))

    print("✔ Data saved to MongoDB")

except Exception as e:
    print("❌ MongoDB Error:", e)

# ---------------- FINAL OUTPUT ----------------
print("\n📊 Performance Distribution:")
print(df["Performance_Level"].value_counts().to_string())

print("\n✔ Pipeline completed successfully")
