# API Contract

## Users API

| Method | Endpoint | Description | Status Code |
|---|---|---|---|
| GET | /users | Get all users | 200 |
| GET | /users/{id} | Get a user | 200 |
| POST | /users | Create a user | 201 |
| PUT | /users/{id} | Update a user | 200 |
| DELETE | /users/{id} | Delete a user | 204 |

## Tasks API

| Method | Endpoint | Description | Status Code |
|---|---|---|---|
| GET | /tasks | Get all tasks | 200 |
| GET | /tasks/{id} | Get a task | 200 |
| POST | /tasks | Create a task | 201 |
| PUT | /tasks/{id} | Update a task | 200 |
| DELETE | /tasks/{id} | Delete a task | 204 |

## Error Status Codes

- 400: Bad Request
- 404: Not Found
- 500: Internal Server Error
