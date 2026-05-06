import pandas as pd
from sqlalchemy import create_engine
from pymongo import MongoClient

# ML imports
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# ---------------- LOAD DATA ----------------
df = pd.read_csv("../data/students.csv")

# ---------------- CLEAN DATA ----------------
df.dropna(inplace=True)

# ---------------- RULE-BASED CLASSIFICATION ----------------
def classify(row):
    if row["class_failures"] >= 2 or row["absences"] > 20:
        return "At-Risk"
    elif str(row["study_time"]) == "<2 hours":
        return "Average"
    else:
        return "High"

df["Performance_Level"] = df.apply(classify, axis=1)

print("✔ Rule-based classification done")

# ---------------- MACHINE LEARNING SECTION ----------------

df_ml = df.copy()

# Encode categorical data
le = LabelEncoder()

df_ml["sex"] = le.fit_transform(df_ml["sex"])
df_ml["school"] = le.fit_transform(df_ml["school"])
df_ml["address_type"] = le.fit_transform(df_ml["address_type"])

# Features and target
X = df_ml[["age", "absences", "class_failures", "sex"]]
y = df_ml["Performance_Level"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("✔ ML Model Accuracy:", accuracy)

# ---------------- POSTGRESQL ----------------
engine = create_engine(
    "postgresql://postgres:admin123@localhost:5432/student_performance"
)

df.to_sql("students", engine, if_exists="replace", index=False)

print("✔ Data saved to PostgreSQL")

# ---------------- MONGODB ----------------
client = MongoClient("mongodb://localhost:27017/")
db = client["student_bigdata"]
collection = db["students"]

collection.delete_many({})
collection.insert_many(df.to_dict(orient="records"))

print("✔ Data saved to MongoDB")

# ---------------- FINAL OUTPUT ----------------
print("\n📊 Performance Distribution:")
print(df["Performance_Level"].value_counts().to_string())