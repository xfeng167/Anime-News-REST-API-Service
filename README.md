# Anime News REST API Service

A lightweight REST API service built with FastAPI for managing anime news records stored in a CSV file.

This project demonstrates an important backend engineering concept:

> The API layer and the data storage layer should be separated.

Instead of using a real database such as MySQL or PostgreSQL, this project uses a CSV file as a mock database. The API communicates with a dedicated storage layer that handles CSV operations, simulating how real backend systems interact with databases through repository or service layers.

---

# Features

* Build a REST API using FastAPI
* Perform CRUD operations
* Use CSV as a mock database
* Understand HTTP methods and status codes
* Separate API logic from storage logic
* Practice backend project structure

---

# Technologies Used

* Python 3
* FastAPI
* Pydantic
* Uvicorn
* CSV File Storage

---

# Project Structure

```plaintext
anime-news-api/
├── main.py
├── schemas.py
├── add_id_to_csv.py
├── anime_news.csv
├── storage_pkg/
│   ├── __init__.py
│   └── storage.py
├── README.md
└── requirements.txt
```

---

# Project Structure Explanation

## main.py

The FastAPI application entry point.

Responsibilities:

* Define API routes
* Handle HTTP requests and responses
* Connect the API layer to the storage layer

---

## schemas.py

Defines request and response models using Pydantic.

Responsibilities:

* Validate request data
* Define response structure
* Improve API type safety

---

## add_id_to_csv.py

A preprocessing script that adds an `id` column to the CSV file.

Responsibilities:

* Read CSV data
* Generate unique IDs
* Save updated CSV records

---

## storage_pkg/storage.py

The CSV-based storage layer.

Responsibilities:

* Read records from CSV
* Write records to CSV
* Perform CRUD operations

This simulates using an external repository or database package.

---

## anime_news.csv

Acts as the mock database.

Each record contains:

* id
* title
* link
* image_url

---

# Functional Requirements

## 1. Get All News Records

### Endpoint

```http
GET /news
```

Returns all anime news records.

---

## 2. Get One News Record by ID

### Endpoint

```http
GET /news/{id}
```

Returns one anime news record by ID.

---

## 3. Create a New News Record

### Endpoint

```http
POST /news
```

Accepts a JSON request body and appends a new record to the CSV file.

### Example Request Body

```json
{
  "title": "New Anime Announced",
  "link": "https://example.com/anime-news",
  "image_url": "https://example.com/image.jpg"
}
```

---

## 4. Update an Existing News Record

### Endpoint

```http
PUT /news/{id}
```

Updates an existing news record by ID.

---

## 5. Delete a News Record

### Endpoint

```http
DELETE /news/{id}
```

Deletes a news record by ID.

---

# Setup Instructions

## 1. Clone the Repository

```bash
git clone <your-github-repo-url>
cd anime-news-api
```

---

## 2. Create a Virtual Environment

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Example requirements.txt

```txt
fastapi
uvicorn
pydantic
```

---

# Run the CSV Preprocessing Script

Before starting the API, run:

```bash
python add_id_to_csv.py
```

This script adds an `id` column to the CSV file.

---

# Run the FastAPI Server

```bash
uvicorn main:app --reload
```

Server URL:

```plaintext
http://127.0.0.1:8000
```

---

# API Documentation

FastAPI automatically generates interactive API documentation.

## Swagger UI

```plaintext
http://127.0.0.1:8000/docs
```

## ReDoc

```plaintext
http://127.0.0.1:8000/redoc
```

---

# HTTP Methods Used

| Method | Purpose       |
| ------ | ------------- |
| GET    | Retrieve data |
| POST   | Create data   |
| PUT    | Update data   |
| DELETE | Remove data   |

---

# HTTP Status Codes

| Status Code | Meaning               |
| ----------- | --------------------- |
| 200         | Success               |
| 201         | Resource created      |
| 400         | Bad request           |
| 404         | Resource not found    |
| 500         | Internal server error |

---

# Minimum Completion Standard

The project is considered complete when:

* The CSV file contains an `id` column
* The FastAPI server runs successfully
* `GET /news` works
* `GET /news/{id}` works
* `POST /news` works
* `PUT /news/{id}` works
* `DELETE /news/{id}` works
* All operations correctly update the CSV file
* The project is uploaded to GitHub

---

# Future Improvements

Possible future upgrades:

* Replace CSV storage with PostgreSQL or MySQL
* Add pagination
* Add authentication
* Add search and filtering
* Add Docker deployment
* Add async database support

---

# License

This project is for educational purposes.

