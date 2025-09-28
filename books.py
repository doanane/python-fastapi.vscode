# from fastapi import FastAPI, HTTPException
# from uuid import UUID
# from pydantic import BaseModel, Field

# app = FastAPI()


# class Books(BaseModel):
#     id: UUID
#     title: str = Field(min_length=1, max_length=100)
#     description: str = Field(max_length=100, min_length=1)
#     rating: int = Field(gt=-1, lt=100)


# BOOKS = []


# @app.get("/")
# def get_books():
#     return BOOKS


# @app.post("/")
# def create_book(book: Books):
#     BOOKS.append(book)
#     return book


# @app.put("/{book_id}")
# def update_book(book_id: UUID, book: Books):
#     counter = 0
#     for x in BOOKS:
#         counter += 1
#         if x.id == book_id:
#             BOOKS[counter - 1] = book
#             return BOOKS[counter - 1]
#     raise HTTPException(status_code=404, detail=f"Id: {book_id} not found")


# @app.put("/")
# def upadte2(book_id: UUID, book: Books):
#     counter = 0
#     for x in BOOKS:
#         counter += 1
#         if x.id == book_id:
#             BOOKS[counter - 1] = book
#             return BOOKS[counter - 1]

#     raise HTTPException(status_id=404, detail=f"ID {book_id} not found")


# @app.put("/{booking}")
# def update3(book_id: UUID, booker: Books):
#     counter = 0
#     for x in BOOKS:
#         counter += 1
#         if x.id == book_id:
#             BOOKS[counter - 1] = booker
#             return BOOKS[counter - 1]
#     raise HTTPException(status_id=404, detail=f"ID {book_id} not found")


# @app.delete("/{book_id}")
# def delete_book(book_id: UUID):
#     counter = 0
#     for x in BOOKS:
#         counter += 1
#         if x.id == book_id:
#             del BOOKS[counter - 1]
#             return f"ID {book_id} deleted"

#     raise HTTPException(status_code=404, detail=f" book with id{book_id} not found")


from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

#
import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# db_dependency = Annotated


class Books(BaseModel):
    # id: UUID
    title: str = Field(min_length=1, max_length=100)
    author: str = Field(max_length=100, min_length=1)
    description: str = Field(max_length=100, min_length=1)
    rating: int = Field(gt=-1, lt=100)


# BOOKS = []


# updating my get request to use database
@app.get("/")
def get_books(db: Session = Depends(get_db)):
    return db.query(
        models.Books
    ).all()  # this line means get all the books from the database


@app.post("/")
def create_book(book: Books, db: Session = Depends(get_db)):
    book_model = models.Books()
    book_model.title = book.title
    book_model.author = book.author
    book_model.description = book.description
    book_model.rating = book.rating
    db.add(book_model)  # adding the book to the database session
    db.commit()  # saving the book to the database
    return book


@app.put("/{book_id}")
def update_book(book_id: int, book: Books, db: Session = Depends(get_db)):
    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()
    if book_model is None:
        raise HTTPException(status_code=404, detail=f"Id: {book_id} not found")
    book_model.title = book.title
    book_model.description = book.description
    book_model.rating = book.rating
    # db.add(book_model)  # adding the book to the database session
    db.commit()
    return book


@app.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()
    if book_model is None:
        raise HTTPException(status_code=404, detail=f" book with id{book_id} not found")

    db.query(models.Books).filter(models.Books.id == book_id).delete()
    db.commit()
    return {"message": f"Book with id {book_id} deleted successfully"}
