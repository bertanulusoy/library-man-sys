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

    class Config:
        orm_mode = True


class Borrower(BaseModel):
    borrower_id: int
    fullname: str
    gender: str
    address: str
    vio_count: int
    created_at: datetime
    updated_at: datetime
    resetmonth: int

    class Config:
        orm_mode = True


class Transaction(BaseModel):
    transaction_id: int
    book_id: int
    borrower_id: int
    dateborrowed: datetime
    duedatereturned: datetime
    fullname: str
    booktitle: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True





