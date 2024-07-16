from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional


class Book:
    id: Optional[id] = None
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: int
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)


Books = [
    Book(1, "Book Title 1", "Author 1", "Book Description 1", 4),
    Book(2, "Book Title 2", "Author 2", "Book Description 2", 5),
    Book(3, "Book Title 3", "Author 3", "Book Description 3", 3),
    Book(4, "Book Title 4", "Author 4", "Book Description 4", 1),
    Book(5, "Book Title 5", "Author 5", "Book Description 5", 5),
    Book(6, "Book Title 6", "Author 6", "Book Description 6", 4),
]

app = FastAPI()


@app.get("/books")
async def read_all_books():
    print("Got it!")
    return Books


@app.get("/book/{book_id}")
async def read_book_by_id(book_id: int):
    for book in Books:
        if book.id == book_id:
            return book


@app.get("/books/")
async def read_book_by_rating(rating: int):
    books_to_return = []
    for book in Books:
        if book.rating == rating:
            books_to_return.append(book)
    return books_to_return


@app.put("/books/update_book")
async def update_book(book: BookRequest):
    for i in range(len(Books)):
        if Books[i].id == book.id:
            Books[i] = Book(**book.dict())


@app.post("/create-book")
async def create_book(book_request: BookRequest):
    print(f"Book: {book_request}")
    new_book = Book(**book_request.dict())
    Books.append(find_book_id(new_book))


def find_book_id(book: Book):
    book.id = 1 if len(Books) == 0 else Books[-1].id + 1
    return book
