from fastapi import FastAPI, Path, Query, HTTPException
from list_of_books import *
from starlette import status # we can dictate exactly what status response needs to be returned

app = FastAPI()

@app.get("/books", status_code=status.HTTP_200_OK)
def read_books():
    return BOOKS

# fetch all books api endpoint
@app.get('/books/{book_id}', status_code=status.HTTP_200_OK)
def read_book(book_id: int = Path(gt=0)): # validation on path params
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Item not found")

# fetch book by rating using query parameter        
@app.get('/books/', status_code=status.HTTP_200_OK)
def read_books_by_rating(book_rating: int = Query(gt=0, lt=6)): # order does not matter in case of query params
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return

# fetch books by published date using query parameter
@app.get('/books/publish/', status_code=status.HTTP_200_OK)
def read_books_published_date(published_date: int = Query(gt=1999, lt=2025)):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return

"""@app.post("/create-book")
def create_book(book_request=Body()): # using body doesnt add any kind of data validation
    BOOKS.append(book_request)"""

@app.post("/create-book", status_code=status.HTTP_201_CREATED)
def create_book(book_request: BookRequest):
    # Validate the book request using Pydantic model
    new_book = Book(**book_request.dict())
    BOOKS.append(find_book_id(new_book))

@app.put("/books/update-book")
def update_book(book: BookRequest, status_code=status.HTTP_204_NO_CONTENT):
    book_changed=False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = Book(**book.dict())
            book_changed=True
    if not book_changed:
        raise HTTPException(status_code=404, detail="Item not found")

@app.delete('/books/{book_id}')
def delete_books(book_id: int = Path(gt=0), status_code=status.HTTP_204_NO_CONTENT):
    book_changed=False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed=True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail="Item not found")

