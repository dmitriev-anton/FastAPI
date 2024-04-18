from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/users")
def users(name: str | None = Query(default=None, min_length=2),
          age: int = Query(ge=18, lt=111)):
    if name == None:
        return {"name": "Undefined", "age": age}
    else:
        return {"name": name, "age": age}