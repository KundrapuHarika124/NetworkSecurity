import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

import certifi
ca = certifi.where()

# ✅ Grab the MongoDB URI from .env
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print("Connecting to:", MONGO_DB_URL)

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, database, collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            # ✅ Add TLS + CA file to enforce secure connection
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL, tls=True, tlsCAFile=ca)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]

            self.collection.insert_many(self.records)
            return len(self.records)

        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == '__main__':
    FILE_PATH = "Network_Data\\phisingData.csv"  # 👈 Double backslashes for Windows
    DATABASE = "HARIKAAI"
    Collection = "NetworkData"

    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    print(f"✅ Total records read: {len(records)}")

    no_of_records = networkobj.insert_data_mongodb(records, DATABASE, Collection)
    print(f"✅ Successfully inserted {no_of_records} records into MongoDB.")
