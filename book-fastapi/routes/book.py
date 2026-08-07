from fastapi import APIRouter, Depends
from schemas.book import BookItem, Book
from models.book import BookModel
from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter()

# Middleware 

books = []

# C: Insert
@router.post("/book", response_model= Book)
async def addBook(bookItem: BookItem,                    
                    db: Session=Depends(get_db)) -> dict:
    
    # 1. BookModel 생성 및 입력 데이터 추가
    bookModel = BookModel(
        title = bookItem.title,
        author = bookItem.author,
        publisher = bookItem.publisher,
        year = bookItem.year,
        status = bookItem.status
    )

    # 2. db.add() - SQL 생성 
    db.add(bookModel)

    # 3. db.commit() - Transaction 실행
    db.commit()

    # 4. db.refresh(모델타입) - 실행 결과 가져오기
    db.refresh(bookModel)

    return bookModel


# R: Select All
