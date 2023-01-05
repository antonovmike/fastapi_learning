from fastapi import FastAPI, Query

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
@app.get("/users")
def users(name:str  = Query(min_length=3, max_length=9), age: int = 18):
    return {"name": name, "user_age": age}
