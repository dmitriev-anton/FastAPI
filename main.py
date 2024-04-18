from fastapi import FastAPI

app = FastAPI()


@app.get("/users")
def get_model(name: str, age: int = 18):
    return {"user_name": name, "user_age": age}