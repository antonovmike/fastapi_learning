from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


# @app.get("/")
# def read_root():
#     html_content = "<h2>Hello FastAPI</h2>"
#     return HTMLResponse(content=html_content)

@app.get("/")
def root():
    return {"message": "Hello FastAPI"}


@app.get("/about")
def about():
    return {"message": "FastAPI framework, high performance, easy to learn, fast to code, ready for production"}


@app.get("/documentation")
def about():
    return {"message": "Documentation: https://fastapi.tiangolo.com"}

