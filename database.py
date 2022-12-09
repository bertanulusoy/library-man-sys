from model import Book
from model import Borrower
from model import Transaction

# Mongo DB Driver
import motor.motor_asyncio

import pymongo
from pymongo import MongoClient

# client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://root:root@mongo:27017')

# client = MongoClient('mongodb://root:root@mongo:27017')
client = MongoClient('mongodb://root:root@mongo:27017')
database = client.Library


# BOOK COLLECTION ***
async def fetch_one_book(book_id):
    collection = database.Book
    document = collection.find_one({"book_id": book_id})
    return document


async def fetch_all_books():
    collection = database.Book
    books = []
    cursor = collection.find()
    for document in cursor:
        books.append(Book(**document))
    return books


async def create_book(book: Book):
    collection = database.Book
    return collection.insert_one(book)


async def update_book(book_id: int, book: Book):
    collection = database.Book
    collection.update_one({"book_id": book_id}, {"$set": {
        "title": book.title,
        "author": book.author,
        "copyright": book.copyright,
        "no_pages": book.no_pages,
        "stock": book.stock,
        "updated_at": book.updated_at
    }})
    document = collection.find_one({"book_id": book.book_id})
    return document


async def remove_book(book_id: int):
    collection = database.Book
    collection.delete_one({"book_id": book_id})
    return True


# BORROWER COLLECTION
async def fetch_one_borrower(borrower_id):
    collection = database.Borrower
    document = collection.find_one({"borrower_id": borrower_id})
    return document


async def fetch_all_borrowers():
    collection = database.Borrower
    borrowers = []
    cursor = collection.find()
    for document in cursor:
        borrowers.append(Borrower(**document))
    return borrowers


async def create_borrower(borrower: Borrower):
    collection = database.Borrower
    return collection.insert_one(borrower)


async def update_borrower(borrower_id: int, borrower: Borrower):
    collection = database.Borrower
    collection.update_one({"borrower_id": borrower_id}, {"$set": {
        "title": borrower.fullname,
        "author": borrower.gender,
        "copyright": borrower.address,
        "no_pages": borrower.vio_count,
        "updated_at": borrower.updated_at
    }})
    document = collection.find_one({"borrower_id": borrower.borrower_id})
    return document


async def remove_borrower(borrower_id: int):
    collection = database.Borrower
    collection.delete_one({"borrower_id": borrower_id})
    return True


# TRANSACTION COLLECTION
async def fetch_one_transaction(transaction_id):
    collection = database.Transaction
    document = collection.find_one({"transac_id": transaction_id})
    return document


async def fetch_all_transactions():
    collection = database.Transaction
    transactions = []
    cursor = collection.find()
    for document in cursor:
        transactions.append(Transaction(**document))
    return transactions


async def create_transaction(transaction: Transaction):
    collection = database.Transaction
    return collection.insert_one(transaction)


async def update_transaction(transaction_id: int, transaction: Transaction):
    collection = database.Transaction
    collection.update_one({"transac_id": transaction_id}, {"$set": {
        "title": transaction.fullname,
        "author": transaction.booktitle,
        "updated_at": transaction.updated_at
    }})
    document = collection.find_one({"transac_id": transaction.transaction_id})
    return document


async def remove_transaction(transaction_id: int):
    collection = database.Transaction
    collection.delete_one({"transac_id": transaction_id})
    return True
