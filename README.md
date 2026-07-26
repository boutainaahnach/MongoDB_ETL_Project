# MongoDB ETL Project

## Project Description

This project demonstrates an ETL (Extract, Transform, Load) pipeline using MongoDB as a data warehouse.

Data is extracted from three different sources:

- CSV File (Sales Data)
- REST API (FakeStore API)
- SQLite Database (Employees)

The extracted data is cleaned using Pandas, then loaded into MongoDB. Finally, all data is consolidated into a unified MongoDB collection for analytics.

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

Student: Your Name