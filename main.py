from fastapi import FastAPI, Query, Path

app = FastAPI()

# v1
# @app.get("/users")
# def get_model(name, age):
#     return {"user_name": name, "user_age": age}

# v2
# @app.get("/users")
# def get_model(name: str, age: int = 18):
#     return {"user_name": name, "user_age": age}

# v3
# @app.get("/users")
# def users(name: str = Query(min_length=3, max_length=9), age: int = 18):
#     return {"name": name, "user_age": age}


# Validation by regular value
# @app.get("/users/{phone}")
# def users(phone: str = Query(regex="^\d{11}$")):
#     return {"phone": phone}

# Default value - "Undefined"
# @app.get("/users")
# def users(name: str = Query(default="Undefined", min_length=2)):
#     return {"name": name}

# Path parameters and query string
# http://127.0.0.1:8000/users/Mike?age=39
@app.get("/users/{name}")
def users(name: str = Path(min_length=3, max_length=9), age: int = Query(ge=18, lt=111)):
    return {"name": name, "age": age}
