from fastapi import FastAPI

app = FastAPI()

# First
@app.get("/users/admin")
def admin():
    return {"message": "Hello admin"}

# Second
@app.get("/users/{id}")
def users(id: int):
    return {"user_id": id}

