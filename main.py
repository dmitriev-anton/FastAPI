from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/users/{name}/{age}")
def users(name: str = Path(min_length=3, max_length=20),
          age: int = Path(ge=18, lt=111)):
    return {"name": name, "age": age}

@app.get("/users/{phone}")
def users(phone:str  = Path(pattern=r"^\d{10}$")):
    return {"phone": phone}