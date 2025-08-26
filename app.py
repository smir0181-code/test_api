from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return FileResponse("index.html")


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"ты_ввел": item_id, "q": q}
@app.get('/add/{a}/{b}')
def add(a: float, b: float):
    return (f'{a} + {b} = {a + b}')
@app.get('/sub/{a}/{b}')
def sub(a: float, b: float):
    return (f'{a} - {b} = {a - b}')
@app.get('/mul/{a}/{b}')
def mul(a: float, b: float):
    return (f'{a} * {b} = {a * b}')
@app.get('/div/{a}/{b}')
def div(a: float, b: float):
    if b == 0:
        return ('На ноль делить нельзя')
    return (f'{a} / {b} = {a / b}')


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)