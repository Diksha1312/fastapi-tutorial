- get, post, put, delete requests
- new: 
    - Data validation
    - Exception Handling
    - Status Codes
    - Swagger Configuration
    - Python Request Objects

- Pydantic v1 vs Pydantic v2
FastAPI is compatible with both Pydantic v1 and Pydantic v2.

The three biggest changes are:

    - .dict() function is now renamed to .model_dump()

    - schema_extra function within a Config class is now renamed to json_schema_extra

    - Optional variables need a =None example: id: Optional[int] = None

- Pydantics and Data Validation 
    - Pydantic is used for data validation and settings management using Python type annotations.
    - It allows you to define data models with type hints, and it automatically validates the data against these models.
    - Pydantic models can be used to validate request bodies in FastAPI endpoints.
    - You can define a Pydantic model by creating a class that inherits from `BaseModel` and defining its attributes with type annotations.
    - FastAPI will automatically validate incoming request data against the Pydantic model and return a 422 Unprocessable Entity error if the data does not match the model.
    - You can also use Pydantic's `Field` class to add additional validation rules
  such as minimum and maximum values, regex patterns, and more.

- Swagger configuration is automatically handled by FastAPI, so no additional code is needed here.
You can access the Swagger UI at http://localhost:8000/docs after running the FastAPI application.

- Status codes - used to help Client to understand what happened on the server side application
Common status codes 
    - 1xx -> Information Responses: Request Processing
    - 2xx -> Success: Request Successfully Completed
    - 3xx -> Redirection: Further action must be complete
    - 4xx -> Client Errors: An error was caused by client (Very popular)
    - 5xx -> Server Errors: An error was occured on the server.

- Http Exceptions

