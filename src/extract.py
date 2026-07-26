import pandas as pd
import requests
import sqlite3

def extract_csv():
    return pd.read_csv("../data/sales.csv")


def extract_api():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    return pd.DataFrame(response.json())


def extract_sqlite():
    conn = sqlite3.connect("../data/company.db")
    df = pd.read_sql_query("SELECT * FROM employees", conn)
    conn.close()
    return df