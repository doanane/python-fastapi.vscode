from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/")
async def root():
    return {"data": "blog list"}


@app.get("/myroot/{id}")
async def mroot(id: int):
    # fetcth the blog with id = id
    return {"data": id}


@app.get("/blog/{id}/comments")
async def comments(id: int):
    # fetch comments of blog with id = id
    return {"data": {id}}


@app.get("/blog")
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"data": f"{limit} published blogs"}
    else:
        return {"data": f"{limit} blogs"}


# from fastapi import FastAPI
# from uuid import UUID
# from pydantic import BaseModel, Field

# app = FastAPI()


# class main(BaseModel):
#     id: UUID
#     Title: str = Field(min_Length=1, max_Length=100)
#     Author: str = Field(min_Length=1, max_Length=100)
#     Description: str = Field(min_Length=1, max_Length=100)
#     Rating: int = Field(gt=-1, lt=100)


# BOOKS = []


# @app.get("/")
# def root_get():
#     return BOOKS


# @app.post("/")
# def create_pose(book: main):
#     BOOKS.append(book)
#     return book
