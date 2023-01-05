from fastapi import FastAPI, Response

app = FastAPI()


# Response
@app.get("/")
def root():
    data = "Hello FastAPI"
    return Response(content=data, media_type="text/plain")

@app.get("/about")
def about():
    return {"message": "FastAPI framework, high performance, easy to learn, fast to code, ready for production"}


@app.get("/documentation")
def about():
    return {"message": "Documentation: https://fastapi.tiangolo.com"}

