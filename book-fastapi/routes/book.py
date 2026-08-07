from fastapi import APIRouter, Depends
from schemas.book import BookItem, Book, Books
from models.book import BookModel
from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter()

# Middleware 

books = []

# C: Insert
@router.post("/book")
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

    return {
        "message": "등록 성공!!",
        "book": {
            "id": bookModel.id,
            "title": bookModel.title,
            "author": bookModel.author,
            "publisher": bookModel.publisher,
            "year": bookModel.year,
            "status": bookModel.status,
        }
    }


# R: Select All
@router.get("/books", response_model=Books)
async def getAll(db: Session=Depends(get_db)) -> list:
    init_books = db.execute(
        select(BookModel).order_by(BookModel.id)
    )
    books = init_books.scalars().all()  # [{id:1 ...}, {...}...]

    return {
        "books": books
    }