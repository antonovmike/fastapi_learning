from fastapi import FastAPI

app = FastAPI()

# First
@app.get("/users/admin")
def admin():
    return {"message": "Hello admin"}

# Second
@app.get("/users/{name}")
def users(name):
    return {"user_name": name}
