from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field


class Person(BaseModel):
    name: str = Field(default="Undefined", min_length=3, max_length=9)
    age: int = Field(default=18, ge=18, lt=111)
    languages: list = Field(default="Undefined")


app = FastAPI()


@app.get("/")
def root():
    return FileResponse("public/index.html")


@app.post("/hello")
def hello(person: Person):
    return {"message": f"Hello, {person.name}, your age is {person.age}. Languages: {person.languages}"}
