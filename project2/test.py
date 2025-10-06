from fastapi import FastAPI

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
async def read_all_books():
    return BOOKS

@app.get("/books/{dynamic_param}")
async def read_all_books(dynamic_param: str):
    return {"message": f"Hello {dynamic_param}"}

@app.get("/books/{title}")
async def read_book(title: str):
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
    if books_to_return == []:
        return {"error": "No books found"}
    return books_to_return

@app.get("/books/byauthor/")
async def read_books_by_author_query(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    if books_to_return == []:
        return {"error": "No books found"}
    return books_to_return

@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
            book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    if books_to_return == []:
        return {"error": "No books found"}
    return books_to_return


