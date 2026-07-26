# MongoDB ETL Project

## Project Description

This project implements an ETL (Extract, Transform, Load) pipeline using MongoDB as a data warehouse.

The objective is to collect data from multiple sources, process and clean it, then store it in MongoDB for analysis.

Data is extracted from three different sources:

- CSV File (Sales Data)
- REST API (FakeStore API)
- SQLite Database (Employees)

The extracted data is transformed using Pandas by cleaning and standardizing the datasets. 
Finally, the processed data is loaded into MongoDB collections and unified into a single collection for analytics.

---

## Technologies

- Python
- MongoDB
- Pandas
- PyMongo
- SQLite
- REST API
- Schedule

---

## Project Structure

```
MongoDB_ETL_Project/

│

├── data/

├── notebooks/

├── src/

├── logs/

├── requirements.txt

├── README.md

└── .gitignore
```

---

## ETL Process

### Extract

- CSV
- REST API
- SQLite

### Transform

- Remove duplicates
- Remove null values
- Standardize data

### Load

Data is inserted into:

- sales
- products
- employees
- unified_data

Pipeline execution logs are stored in:

pipeline_logs

---

## Aggregation Examples

- Total sales per product
- Average product price
- Employees per department

---

## Scheduler

The pipeline can run automatically every minute using the Schedule library.

---

## Author

Student: Boutaina Ahnach
Master GLCC
