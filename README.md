Design and Development of a Big Data Analytics Early Warning System Dashboard for Student Performance and At-Risk Student Detection 

Project Overview
This project is a data-driven Student Performance Early Warning System that analyzes student academic behavior and predicts performance levels using rule-based classification and machine learning. It identifies at-risk students based on key indicators such as absences, class failures, and study time. The system integrates Python for data processing, PostgreSQL and MongoDB for data storage, FastAPI for API access, and Power BI for data visualization and reporting.

---

Objectives
- To analyze student performance using structured datasets
- To apply rule-based and machine learning classification techniques
- To identify students at risk of academic failure
- To store processed data in PostgreSQL and MongoDB
- To expose data through a FastAPI backend
- To visualize insights using Power BI dashboards
- To support early academic intervention and decision-making

---

System Architecture
CSV Dataset
↓
Python ETL Pipeline (Data Cleaning + ML Model)
↓
PostgreSQL (Structured Database)
↓
MongoDB (NoSQL Backup Storage)
↓
Power BI (Dashboard & Visualization)


---

Features

✔ Data Processing
- Data cleaning and preprocessing
- Handling missing values

✔ Classification System
- Rule-based student classification (High / Average / At-Risk)

✔ Database Integration
- PostgreSQL for structured data storage
- MongoDB for NoSQL backup storage

✔ Visualization
- Power BI dashboard for performance monitoring
- Early warning system visualization

---

Early Warning System Logic
Students are classified as **At-Risk** if:
- Class failures ≥ 2  
- OR absences > 20  

These students are highlighted in the system for early academic intervention.

---

Power BI Dashboard Includes
- Total Students KPI
- At-Risk Students KPI
- Performance Distribution (Pie Chart)
- Risk Factor Analysis (Bar Chart)
- At-Risk Student Table
- Performance Trend Analysis
- Risk Level Indicator (Gauge)

---

Technologies Used
- Python
- Pandas
- PostgreSQL
- MongoDB
- Power BI

---

Project Structure
student_project/
│
├── app/ 
├── scripts/ # ETL + ML pipeline
├── data/ # Dataset files
├── dashboard/ # Power BI files
├── requirements.txt # Dependencies
└── README.md


---

How to Run the Project

1. Install dependencies
```bash
pip install -r requirements.txt# Student Performance Early Warning System

## Overview
A Big Data Analytics system designed to identify at-risk students using rule-based classification and propose machine learning models for future enhancement.

## Tech Stack
- Python
- Pandas
- PostgreSQL
- MongoDB

## Features
- Data cleaning and preprocessing
- Rule-based student classification
- Dual database storage (SQL + NoSQL)
- Proposed ML model integration (future work)

## Proposed ML Models
- Decision Tree Classifier
- Random Forest Classifier
- Logistic Regression

## How to Run
```bash
pip install -r requirements.txt
python scripts/pipeline.py
 

