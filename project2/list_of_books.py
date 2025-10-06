from pydantic import BaseModel, Field
from typing import Optional

class Book: 
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id: int, title: str, author: str, description: str, rating: int, published_date: int):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

class BookRequest(BaseModel): # Pydantic model for book request validation
    id: Optional[int] = Field(description='ID is not needed on create', default=None)  # Optional ID, will be set by the server
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6) # between 1 and 5
    published_date: int = Field(gt=1999, lt=2025)
    # Pydantic model configuration for Swagger documentation
    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "New Book Title",
                "author": "Author Name",
                "description": "A brief description of the book.",
                "rating": 5,
                "published_date": 2019
            }   
        }
    }

BOOKS = [
    Book(id=1, title="1984", author="George Orwell", description="Dystopian novel", rating=5, published_date=2012),
    Book(id=2, title="To Kill a Mockingbird", author="Harper Lee", description="Classic novel", rating=4, published_date=2000),
    Book(id=3, title="The Great Gatsby", author="F. Scott Fitzgerald", description="Tragic love story", rating=4, published_date=1990),
    Book(id=4, title="Someone Like You", author="Cecelia Ahern", description="Romantic novel", rating=5, published_date=1994),
    Book(id=5, title="The Catcher in the Rye", author="J.D. Salinger", description="Coming-of-age story", rating=4, published_date=1996),
]

def find_book_id(book: Book): # Function to find the next available ID for a new book
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book
