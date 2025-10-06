Creating and enhancing books to learn the basics of FastAPI
Also be using CRUD operations - create, read, update and delete

# Request and Response
- Web page requests (crud) using http requests to fastapi server.
- fastapi has swagger ui implemented within the application already., this has list of all swagger methods which fastapi can call.
- create is post, read is get, update is put, delete is delete request method

api-endpoint is the path for the API

# run fast api
uvicorn is a web server used to access fastapi endpoints.
uvicorn <file_name>:<app> --reload
Ex - uvicorn books:app --reload

async is optional for fastapi

# Path Parameters

- Path parameters are reqeust parameters that are part of the URL path.
- It is used to identify a specific resource or resources in the URL.
- For example, if you want to get a specific book by its title, you can use a path parameter like this: /books/{title}.
- You can also use path parameters to filter resources, like getting all books by a specific author.
- You can also use path parameters to get a specific book by its year.
For example, if you want to get all books by a specific author, you can use a path parameter like this: /books/author/{author_name}.
- Order matters with Path params - have APIs in chronological order (small to big)

# Query Parameters

- Query Parameters are request parameters that are appended to the URL after a question mark (?).
- They are used to filter or modify the response of an API endpoint. In this case, we are using a query parameter to filter books by their title.
- For example, if you want to get details of a specific book, you can use the URL:
http://localhost:8000/books?title=Book%20One (%20 -> space)
This will return the details of "Book One" if it exists in the BOOKS list.

# Post Request

- Post methods are used to add new data to the server.
- They can have a body with the data to be added unlike get methods which only retrieve data.
- Example of a post method to add a new book.
@app.post("/books/")
def add_book(book: dict):
    BOOKS.append(book)
    return {"message": "Book added successfully", "book": book}
This method would allow you to add a new book by sending a POST request with the book data in the body of the request.

# Put Request

- Put request is used to update an existing resource
- It can have a body like post request
Example: update a book's title or author

# Delete Request

- It is used to delete a resource.