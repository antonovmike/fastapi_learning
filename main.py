from fastapi import FastAPI, Response, Path

app = FastAPI()

# STATUS CODE

# Example 1
# @app.get("/notfound", status_code=404)
# def notfound():
#     return {"message": "Resource Not Found"}

# Example 2
# @app.get("/notfound")
# def notfound():
#     return JSONResponse(content={"message": "Resource Not Found"}, status_code=404)

# CHANGE STATUS CODE
# http://127.0.0.1:8000/users/12
@app.get("/users/{id}", status_code=200)
def users(response: Response, id: int = Path()):
    if id < 1:
        response.status_code = 400
        return {"message": "Incorrect Data"}
    return {"message": f"Id = {id}"}
