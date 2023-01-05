from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


# HTMLResponse
@app.get("/")
def root():
    data = "<h2>Hello FastAPI</h2>"
    return HTMLResponse(content=data)


@app.get("/about")
def about():
    return {"message": "FastAPI framework, high performance, easy to learn, fast to code, ready for production"}


@app.get("/documentation")
def about():
    return {"message": "Documentation: https://fastapi.tiangolo.com"}

