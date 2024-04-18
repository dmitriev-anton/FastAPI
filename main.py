from fastapi import FastAPI

app = FastAPI()


@app.get("/users/{id}")
def users(id: int):
    return {"user_id": id}