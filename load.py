from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["ETL_Project"]

logs = db["pipeline_logs"]


def load_collection(name, dataframe):

    collection = db[name]

    collection.delete_many({})

    collection.insert_many(dataframe.to_dict("records"))

    logs.insert_one({
        "collection": name,
        "status": "Success",
        "records": len(dataframe),
        "date": datetime.now()
    })

    print(f"{name} chargé avec succès.")