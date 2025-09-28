# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel, Field
# from uuid import UUID

# app = FastAPI()


# class put_request(
#     BaseModel
# ):  # create a class that inherits from BaseModel, you can change name of class to anything like Book, Item etc
#     id: UUID
#     title: str = Field(min_length=1, max_Length=100)
#     author: str = Field(min_length=1, max_length=100)

#     description: str = Field(min_length=1, max_length=100)
#     rating: int = Field(gt=-1, lt=100)


# BOOKS = []  # AN EMPTY LIST


# @app.put("/car_id}")
# def car_id(
#     car_id: UUID, book: put_request
# ):  #  we want to update a book by its id, so we need to pass the id as
#     for x in BOOKS:
#         counter = 0
#         if x.id == car_id:
#             BOOKS[counter - 1] = book
#             raise HTTPException(
#                 Status_code=404, detail=f"book with id {car_id} not found"
#             )


from fastapi import FastAPI, HTTPException
from uuid import UUID
from pydantic import BaseModel, Field

app = FastAPI()


class Cars(BaseModel):
    id: UUID
    # car_id: UUID
    car_name: str = Field(min_length=1, max_length=100)
    car_model: str = Field(min_length=1, max_length=100)
    car_color: str = Field(min_length=1, max_length=100)
    car_price: int = Field(gt=10000, lt=1000000)


CARS = []


@app.get("/{name}")
def get_cars():
    return CARS


@app.post("/")
def create_cars(car: Cars):
    CARS.append(car)
    return car


@app.put("/{car_id}")
def update_cars(car_id: UUID, car: Cars):
    counter = 0
    for x in CARS:
        counter += 1
        if x.id == car_id:
            CARS[counter - 1] = car
            return CARS[counter - 1]
    raise HTTPException(status_code=404, detail=f"car with id {car_id} not found")


@app.delete("/{car_id}")
def delete_car(car_id: UUID):
    counter = 0
    for x in CARS:
        counter += 1
        if x.id == car_id:
            del CARS[counter - 1]
            return f"ID:{car_id} deleted"
    raise HTTPException(status_code=404, detail=f"cr whith id {car_id} not found")
