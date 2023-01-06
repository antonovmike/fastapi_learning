from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Any time you call /static app gonna send you files from "public"
# app.mount("/static", StaticFiles(directory="public"))

# Set main page
app.mount("/static", StaticFiles(directory="public", html=True))
