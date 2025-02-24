# Toy Librarian CRUD App
A Flask REST API for managing users with MongoDB, built with Docker.

## Prerequisites
- Docker
- Docker Compose
- Postman (for testing)

## Setup and Run
1. Clone the repo: `git clone https://github.com/srivanij23/CRUD`
2. Navigate to the directory: `cd CRUD`
3. Build and run: `docker-compose up --build`
4. Access at `http://localhost:5000`.

## Testing
- Use Postman to test endpoints.
- Example: `POST http://localhost:5000/users` with body:
  ```json
  {"name": "johnie", "email": "johnie@gmail.com", "password": "123"}

Endpoints: 
GET /users: List all users
POST /users: Create a user
GET /users/<id>: Get a user
PUT /users/<id>: Update a user
DELETE /users/<id>: Delete a use