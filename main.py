# # print("welcome to python")

# from fastapi import FastAPI
# apps = FastAPI()
# @apps.get("/")

# async def read_root():
#     return {"Hello": "World"}

# # @app.get("/home")
# @app.get("/{name}")

# def read_root(name: str):
#     return{"message": name}

from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()


class main(
    BaseModel
):  # create a class that inherits from BaseModel, you can change name of class to anything like Book, Item etc
    id: UUID
    title: str = Field(min_length=1, max_Length=100)
    author: str = Field(min_length=1, max_length=100)

    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=100)


BOOKS = []  # AN EMPTY LIST


# @app.get("/")
@app.get("/")
def read_root():
    return BOOKS


@app.post("/")
def create_book(book: main):
    BOOKS.append(book)
    return book


@app.put("/{book_id}")
def update_book(
    book_id: UUID, book: main
):  #  we want to update a book by its id, so we need to pass the id as a path parameter
    for index, b in enumerate(
        BOOKS
    ):  #  we need to loop through the list of books to find the book with the given id. #  use enumerate to get the index of the book in the list #  then we can update the book at that index #  then return the updated book #  if the book is not found, return an error message
        if b.id == book_id:
            BOOKS[index] = book
            return BOOKS[index]
    return {"error": "Book not found"}
    #  we want to create a book, so we need to define a path operation function that will handle the post request
    #  while condition: we want to create a book, we also

    #  want the data to be a post request, which will accept data in the body of the request
    #  use pydantic model to define the structure of the data s our data validation  first import BaseModel from pydantic
    #  then create a class that inherits from BaseModel and define the fields of the model
    #  then use the model as the type of the parameter in the path operation function
    #  then use the model to access the data in the body of the request
