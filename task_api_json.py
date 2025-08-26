from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI(title='Простой CRUD с JSON')
DATA_FILE='user.json'
@app.get("/")
def home():
    """ Главная страница"""
    return {"message": "Простой CURUD API","документация ": "/docs"}






if __name__ == "__main__":
    uvicorn.run("task_api_json:app", host="127.0.0.1", port=8000, reload=True)