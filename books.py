from fastapi import FastAPI, Body


class Book:
    id: int
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


Books = [
    Book(1, "Book Title 1", "Author 1", "Book Description 1", 4),
    Book(1, "Book Title 2", "Author 2", "Book Description 2", 5),
    Book(1, "Book Title 3", "Author 3", "Book Description 3", 3),
    Book(1, "Book Title 4", "Author 4", "Book Description 4", 1),
    Book(1, "Book Title 5", "Author 5", "Book Description 5", 5),
    Book(1, "Book Title 6", "Author 6", "Book Description 6", 4),
]

app = FastAPI()


@app.get("/books")
async def read_all_books():
    print("Got it!")
    return Books


@app.post("/create-book")
async def create_book(book_request=Body()):
    Books.append(book_request)
