# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API with FastAPI and Python to manage a small book catalog. Practice defining endpoints, using HTTP methods and status codes, and validating request data.

## 📝 Tasks

### 🛠️ Create the API and List Books

#### Description
Set up a FastAPI application for a book catalog and create an endpoint that returns the books currently in the catalog.

#### Requirements
Completed program should:

- Create a `main.py` file with a FastAPI application
- Run the application locally with Uvicorn
- Define a `GET /books` endpoint that returns a JSON list of books
- Include at least two books, each with an `id`, `title`, `author`, and `year`
- Confirm the endpoint works in the interactive documentation at `/docs`


### 🛠️ Add Book Management Endpoints

#### Description
Extend the API so clients can add a book, look up one book, update its details, and remove it. Store the books in a Python list or dictionary; data does not need to persist after the server stops.

#### Requirements
Completed program should:

- Define `GET /books/{book_id}` to return one book by ID
- Define `POST /books` to add a book and return the created book
- Define `PUT /books/{book_id}` to update a book by ID
- Define `DELETE /books/{book_id}` to remove a book by ID
- Use appropriate HTTP methods and return a `404 Not Found` response when a requested book does not exist
- Demonstrate each endpoint using `/docs` or an HTTP client


### 🛠️ Validate Requests and Handle Responses

#### Description
Use a Pydantic model to validate book data sent by clients and make the API responses clear and consistent.

#### Requirements
Completed program should:

- Define a request model with required `title` and `author` fields and a valid `year`
- Reject requests with missing or invalid field values using FastAPI's validation response
- Return `201 Created` when a book is added successfully
- Return a successful response when a book is updated or deleted
- Verify at least one invalid request and one missing-book request in `/docs` or an HTTP client
