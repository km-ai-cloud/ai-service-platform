from fastapi import FastAPI
from routes.todo import todo_router
# from routes.book import book_router

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {
        "message": "welcome ch03!!"
    }


app.include_router(todo_router) # todo 애플리케이션
# app.include_router(book_router) # 도서관리 애플리케이션