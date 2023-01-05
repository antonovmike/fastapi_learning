from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()


# @app.get("/")
# def read_root():
#     html_content = "<h2>Hello FastAPI</h2>"
#     return HTMLResponse(content=html_content)

# Data serialization v1
# @app.get("/")
# def root():
#     data = {"message": "Hello FastAPI"}
#     json_data = jsonable_encoder(data)
#     return JSONResponse(content=json_data)

# Data serialization v2
# If we need to send some custom non-serializable data, or if we
# need custom  serialization, we can define our own serializer
@app.get("/")
def root():
    return JSONResponse(content={"message": "Hello FastAPI"})

@app.get("/about")
def about():
    return {"message": "FastAPI framework, high performance, easy to learn, fast to code, ready for production"}


@app.get("/documentation")
def about():
    return {"message": "Documentation: https://fastapi.tiangolo.com"}

