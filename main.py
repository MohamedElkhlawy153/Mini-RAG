from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome_message():
    return {
        "message": "Welcome to Mini-RAG-APP!"
        }