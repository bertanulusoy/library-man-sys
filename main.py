from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import *

app = FastAPI()

origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_method=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/books")
async def books():
    response = await fetch_all_books()
    return response


@app.get("/api/books{book_id}", response_model=Book)
async def get_book_by_id(book_id: int):
    response = await fetch_one_book(book_id)
    if response:
        return response
    raise HTTPException(404, f"There is no book item with this book id {book_id}.")


@app.post("/api/books", response_model=Book)
async def post_book(book: Book):
    response = await create_book(book.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong. Bad request")


@app.put("/api/books{book_id}", response_model=Book)
async def update_book_by_id(book_id: int, book: Book):
    response = await update_book(book_id, book)
    if response:
        return response
    raise HTTPException(404, f"There is no book item with this book id {book_id}.")


@app.delete("/api/books{book_id}")
async def delete_book_by_id(book_id: int):
    response = await remove_book(book_id)
    if response:
        return "Successfully deleted book item"
    raise HTTPException(404, f"There is no book item with this book id {book_id}.")


@app.put("/api/books{book_id}")
async def borrow_book_by_id(book_id: int, user_data):
    return f"Borrow a book with the book id.{book_id}"

