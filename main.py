from fastapi import FastAPI, Path

app = FastAPI()

# First
@app.get("/users/admin")
def admin():
    return {"message": "Hello admin"}

# Second
@app.get("/users/{name}")
def users(name:str  = Path(min_length=3, max_length=9)):
    return {"name": name}

