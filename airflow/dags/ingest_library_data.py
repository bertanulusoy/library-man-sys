import os
from time import time

import pandas as pd
# Mongo DB Driver
import pymongo
from pymongo import MongoClient


def ingest_data_callable(user, password, host, port, db, table_name: str, csv_file_url: str, data_interval_start):

    # client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://root:root@mongo:27017')
    client = MongoClient('mongodb://root:root@mongo:27017')
    mongo_db = client.Library

    if table_name == 'Book':
        book_data = pd.read_csv(csv_file_url).to_dict(orient='records')
        collection = mongo_db.Book
        for bd in book_data:
            book = collection.find_one({"book_id": bd["book_id"]})
            if book is None:
                collection.insert_one(bd)
    elif table_name == 'Borrower':
        borrower_data = pd.read_csv(csv_file_url).to_dict(orient='records')
        collection = mongo_db.Borrower
        for bd in borrower_data:
            borrower = collection.find_one({"borrower_id": bd["borrower_id"]})
            if borrower is None:
                collection.insert_one(bd)
    elif table_name == 'Transaction':
        transaction_data = pd.read_csv(csv_file_url).to_dict(orient='records')
        collection = mongo_db.Transaction
        for td in transaction_data:
            transaction = collection.find_one({
                "transac_id": td["transac_id"],
                "book_id": td["book_id"],
                "borrower_id": td["borrower_id"]
            })
            if transaction is None:
                collection.insert_one(td)
