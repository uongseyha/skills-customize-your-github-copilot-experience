# 📘 Assignment: Persisting FastAPI Data with SQLite

## 🎯 Objective

Extend the book catalog REST API to store books in a SQLite database instead of temporary in-memory storage. Practice creating a database table, connecting API endpoints to stored records, and verifying that data remains available after the server restarts.

## 📝 Tasks

### 🛠️ Create a SQLite Database

#### Description
Set up a SQLite database for the book catalog. Create a table for books and initialize it when the FastAPI application starts.

#### Requirements
Completed program should:

- Create a database file named `books.db` using Python's `sqlite3` module
- Create a `books` table with columns for `id`, `title`, `author`, and `year`
- Initialize the table when the application starts without deleting existing records
- Insert values into SQL statements using parameters rather than string formatting


### 🛠️ Connect the API to Stored Books

#### Description
Replace the in-memory book collection in the FastAPI book catalog with database operations. Keep the existing REST endpoints and their response behavior.

#### Requirements
Completed program should:

- Make `GET /books` and `GET /books/{book_id}` read books from SQLite
- Make `POST /books` insert a book into the database and return the created book
- Make `PUT /books/{book_id}` update a stored book
- Make `DELETE /books/{book_id}` remove a stored book
- Return `404 Not Found` when an update, delete, or lookup targets a book that does not exist
- Close database connections reliably after each operation


### 🛠️ Verify Data Persists

#### Description
Test that the API can retrieve and manage books after the application has been stopped and restarted.

#### Requirements
Completed program should:

- Add a book through `POST /books` and confirm it appears in `GET /books`
- Stop and restart the application, then confirm the book is still available
- Update and delete a book, then confirm each change is reflected by subsequent requests
- Demonstrate a request for a nonexistent book and confirm the API returns `404 Not Found`
