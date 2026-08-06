# ----------------------------------------------
#  도서 관리 애플리케이션 - CRUD
# ----------------------------------------------
from fastapi import APIRouter, Depends, HTTPException, status
from schemas.book_schema import Book, Book_Item

from database import get_db
from sqlalchemy.orm import Session
from models.book_model import BookModel


book_router = APIRouter()

# C: Insert
@book_router.post("/book", 
                    response_model=Book,
                    status_code=status.HTTP_201_CREATED)
async def add_book(book_data: Book_Item,
                    db:Session = Depends(get_db)) -> dict:
    bookModel = BookModel(
        title = book_data.title,
        price = book_data.price,
        isbn = book_data.isbn
        )

    db.add(bookModel)   # SQL 생성 -> Insert into books values(?,?,?)
    db.commit()         # DB에 SQL 전송 및 실행
    db.refresh(bookModel)    # 실행 결과(title, price, isbn) 받기
    
    return bookModel


# R: Select All
# R: Select Id
# U: Update
# D: Delete All
# D: Delete Id

