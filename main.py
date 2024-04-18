from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/users/{name}")
def users(name: str = Path(min_length=3, max_length=20),
          age: int = Query(ge=18, lt=111)):
    return {"name": name, "age": age}