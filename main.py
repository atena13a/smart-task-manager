from fastapi import FastAPI

app = FastAPI(title="Smart Task Manager")

users = []
tasks = []

@app.get("/")
def home():
    return {"message": "Smart Task Manager API"}

@app.get("/users")
def get_users():
    return users

@app.post("/users")
def create_user(user: dict):
    users.append(user)
    return user

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: dict):
    tasks.append(task)
    return task
