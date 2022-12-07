from pydantic import BaseModel
from datetime import datetime


class Book(BaseModel):
    book_id: int
    title: str
    author: str
    copyright: str
    no_pages: int
    stock: int
    created_at: datetime
    updated_at: datetime


class Borrower(BaseModel):
    borrow_id: int
    full_name: str
    gender: str
    address: str
    created_at: datetime
    updated_at: datetime


class Transaction(BaseModel):
    transaction_id: int
    book_id: int
    borrower_id: int
    date_borrowed: datetime
    due_date_returned: datetime
    created_at: datetime
    updated_at: datetime





