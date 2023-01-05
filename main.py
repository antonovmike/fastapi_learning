from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, JSONResponse, HTMLResponse

app = FastAPI()


# response_class
@app.get("/text", response_class = PlainTextResponse)
def root_text():
    return "Hello FastAPI"


@app.get("/html", response_class = HTMLResponse)
def root_html():
    return "<h2>Hello Hello FastAPI</h2>"


@app.get("/about")
def about():
    return {"message": "FastAPI framework, high performance, easy to learn, fast to code, ready for production"}


@app.get("/documentation")
def about():
    return {"message": "Documentation: https://fastapi.tiangolo.com"}

