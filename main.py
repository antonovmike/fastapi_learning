from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

# v1
@app.get("/")
def root():
    return FileResponse("public/index.html")

# v2
# @app.get("/file", response_class=FileResponse)
# def root_html():
#     return "public/index.html"