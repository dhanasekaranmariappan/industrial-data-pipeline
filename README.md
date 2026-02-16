# Industrial Data Pipeline & Analytics System

## Business Problem

Industrial environments generate high-frequency machine telemetry.
This project simulates how manufacturing companies monitor equipment
health, detect anomalies, and support predictive maintenance decisions.

## Solution

Built an end-to-end data pipeline that:

1. Ingests machine telemetry datasets
2. Cleans and transforms using Pandas
3. Stores structured data in MySQL
4. Performs exploratory analytics (EDA)
5. Generates operational visualizations
6. Prepares foundation for ML-based anomaly detection

## Tech Stack

Python | Pandas | MySQL | Matplotlib | Plotly | SQL | Data Engineering Concepts

## Overview
This project demonstrates a production-style data engineering workflow built using Python, MySQL, and analytical visualization tools.  
It simulates an Industry 4.0 environment where operational machine data is ingested, cleaned, stored, analyzed, and visualized to support data-driven decision-making.

The goal is to showcase practical skills in:
- Data pipeline development
- Data cleaning and transformation
- SQL database integration
- Analytical querying
- Visualization for operational insights

This project is intentionally designed to reflect real-world engineering workflows rather than notebook-based analysis.

---

## Architecture


Project Structure:

industrial-data-pipeline/
│
├── data/ # Raw dataset
├── src/
│ ├── ingest.py # Data loading
│ ├── clean.py # Data preprocessing
│ ├── transform.py # Feature engineering
│ ├── db.py # MySQL integration
│ ├── analysis.py # Analytical queries
│ └── visualize.py # Charts & insights
│
├── sql/
│ └── schema.sql # Database schema
│
├── main.py # Pipeline runner
├── requirements.txt
└── README.md





---

## Dataset

This project uses the **AI4I Predictive Maintenance Dataset**, which contains simulated industrial machine data such as:

- Air temperature
- Process temperature
- Rotational speed
- Torque
- Tool wear
- Machine failure indicators

It represents real manufacturing telemetry used in predictive analytics systems.

---

## Features Implemented

### 1. Data Ingestion
Loads structured CSV data into the pipeline.

### 2. Data Cleaning
- Removes duplicates  
- Handles missing values  
- Standardizes column naming  
- Ensures consistent formatting

### 3. Feature Engineering
Creates derived metrics such as:
- Machine power estimation  
- Temperature differential analysis  

These simulate real operational KPIs used in monitoring environments.

### 4. Database Integration
Stores processed data into a relational MySQL database to support:
- Persistent storage
- Query-based analytics
- Scalable backend integration

### 5. Analytical Layer
Performs grouped analysis to identify:
- Wear-based performance trends
- Operational behavior patterns

### 6. Visualization
Generates engineering-style plots using Matplotlib to visualize:
- Temperature relationships
- Performance distributions
- Machine condition indicators

---

## Technologies Used

| Category | Tools |
|----------|--------|
Programming | Python |
Data Processing | Pandas |
Database | MySQL |
Visualization | Matplotlib |
Workflow | Modular Python Architecture |

---

## How to Run the Project

### 1️⃣ Clone the Repository

git clone https://github.com/dhanasekaranmariappan/industrial-data-pipeline.git

cd industrial-data-pipeline


### 2️⃣ Install Dependencies

pip install -r requirements.txt


### 3️⃣ Configure MySQL

Create database using:

mysql -u root -p < sql/schema.sql


Update credentials inside:

src/db.py


### 4️⃣ Run the Pipeline

python main.py


The system will:
✔ Process the dataset  
✔ Store results in MySQL  
✔ Run analytics  
✔ Display visual insights

---

## Why This Project Matters

This project demonstrates understanding of the **complete data lifecycle**:

- Raw data ingestion  
- Transformation pipelines  
- Structured storage  
- Analytical querying  
- Visualization for decisions  

It reflects the type of data engineering and analytics workflows used in industrial digitalization, predictive maintenance, and operational intelligence systems.

---

## Future Enhancement (Planned)

Next phase will introduce:
- Machine Learning–based anomaly detection
- Predictive maintenance modeling
- Automated alert generation

This will extend the system from analytics → intelligent decision support.

---

## Author

**Dhanasekaran Mariappan**  
Python Data Engineer | Data Pipeline Development | Applied Analytics
