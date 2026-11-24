# Smart Task Manager

A simple task management system for managing users and tasks.

## Features
- Manage users
- Create tasks
- Update tasks
- Delete tasks

## Technologies
- Python
- FastAPI
- Docker

## Docker Instructions

Build Docker Image:

docker build -t smart-task-manager .

Run Docker Container:

docker run -d -p 8000:8000 --name task-manager smart-task-manager

Open API Documentation:

http://localhost:8000/docs
