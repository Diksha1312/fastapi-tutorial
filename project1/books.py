from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "Science"},
    {"title": "Title Two", "author": "Author Two", "category": "Science"},
    {"title": "Title Three", "author": "Author Three", "category": "History"},
    {"title": "Title Four", "author": "Author Four", "category": "Math"},
    {"title": "Title Five", "author": "Author Five", "category": "Math"},
    {"title": "Title Six", "author": "Author Six", "category": "Math"},
    {"title": "Title Seven", "author": "Author Two", "category": "History"}
]

@app.get("/books") 
def read_all_books():
    return BOOKS

@app.get("/books/{title}")
def read_all_books(title: str):
    for book in BOOKS:
        if book.get("title").casefold() == title.casefold():
            return book
    return {"error": "Book not found"}

@app.get('/books/')
def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

#moved this end point here to avoid conflict with the one below - ORDER MATTERS!
@app.get("/books/byauthor/")
def read_books_by_author_query(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get('/books/{author}/')
def read_author_category_by_query(author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold() and \
            book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.post("/books/create_book")      
def create_book(new_book=Body()): # get request cannot have a body like post request
    BOOKS.append(new_book)

@app.put("/books/update_book")
def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == updated_book.get("title").casefold():
            BOOKS[i] = updated_book

@app.delete("/books/delete_book/{title}")
def delete_book(title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == title.casefold():
            BOOKS.pop(i)
            break


"""
Assignment:
1. Create a new API Endpoint that can fetch all books from a 
specific author using either Path Parameters or Query Parameters.
"""
# using path parameters
@app.get("/books/byauthor/{author}/")
def read_books_by_author(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return
# using query parameters - this wont work because the endpoint is already defined so we move this before the other endpoint
"""@app.get("/books/byauthor/")
def read_books_by_author_query(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return"""