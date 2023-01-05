from fastapi import FastAPI, Path

app = FastAPI()

# First
@app.get("/users/admin")
def admin():
    return {"message": "Hello admin"}

# Second
@app.get("/users/{name}/{age}")
def users(name: str = Path(min_length=3, max_length=9), age: int = Path(ge=22, lt=111)):
    return {"name": name, "age": age}


@app.get("/users_2/{phone}")
def users(phone: str = Path(regex="^\d{11}$")):
    return {"phone": phone}
