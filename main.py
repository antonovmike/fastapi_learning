import mimetypes
from fastapi import FastAPI
from fastapi.responses import RedirectResponse, PlainTextResponse

app = FastAPI()

# Redirect
# @app.get("/old")
# def old():
#     return RedirectResponse("/new")

# OR 302 instead of default code 307 (v1)
# @app.get("/old")
# def old():
#     return RedirectResponse("/new", status_code=302)

# OR 302 instead of default code 307 (v1)
# @app.get("/old", response_class= RedirectResponse, status_code=302)
# def old():
#     return "/new"

# OR
# @app.get("/old", response_class= RedirectResponse)
# def old():
#     return "/new"

# OR
@app.get("/old")
def old():
    return RedirectResponse("http://127.0.0.1:8000/new")


@app.get("/new")
def new():
    return PlainTextResponse("New page")
