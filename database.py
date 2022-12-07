from model import Book

# Mongo DB Driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
database = client.Library
collection = database.Books


async def fetch_one_book(book_id):
    document = await collection.find_one({"book_id": book_id})
    return document


async def fetch_all_books():
    books = []
    cursor = await collection.find()
    async for document in cursor:
        books.append(Book(**document))
    return books


async def create_book(book: Book):
    return await collection.insert_one(book)


async def update_book(book_id: int, book: Book):
    await collection.update_one({"book_id": book_id}, {"$set": {
        "title": book.title,
        "author": book.author,
        "copyright": book.copyright,
        "no_pages": book.no_pages,
        "stock": book.stock,
        "updated_at": book.updated_at
    }})
    document = await collection.find_one({"book_id": book.book_id})
    return document


async def remove_book(book_id: int):
    await collection.delete_one({"book_id": book_id})
    return True
