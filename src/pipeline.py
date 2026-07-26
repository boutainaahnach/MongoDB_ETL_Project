from extract import extract_csv, extract_api, extract_sqlite
from transform import transform_sales, transform_products, transform_employees
from load import load_collection
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["ETL_Project"]

def run_pipeline():

    # Extraction
    sales = transform_sales(extract_csv())
    products = transform_products(extract_api())
    employees = transform_employees(extract_sqlite())

    # Collections originales
    load_collection("sales", sales)
    load_collection("products", products)
    load_collection("employees", employees)

    # Collection unifiée
    unified = db["unified_data"]
    unified.delete_many({})

    data = []

    # CSV
    for row in sales.to_dict("records"):
        row["source"] = "CSV"
        data.append(row)

    # API
    for row in products.to_dict("records"):
        row["source"] = "API"
        data.append(row)

    # SQLite
    for row in employees.to_dict("records"):
        row["source"] = "SQLite"
        data.append(row)

    unified.insert_many(data)

    print("Unified collection créée.")
    print("Pipeline terminé.")


if __name__ == "__main__":
    run_pipeline()