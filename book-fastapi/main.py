from fastapi import FastAPI
from routes.book import router

app = FastAPI()

app.include_router(router)