from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()


# Response
@app.get("/")
def root():
    data = "Hello FastAPI"
    return PlainTextResponse(content=data)


@app.get("/about")
def about():
    return {"message": "FastAPI framework, high performance, easy to learn, fast to code, ready for production"}


@app.get("/documentation")
def about():
    return {"message": "Documentation: https://fastapi.tiangolo.com"}

