from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models
from .database import SessionLocal, engine
from typing import List

from pydantic import BaseModel

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


class ChoiceBase(BaseModel):
    choice_text: str
    is_correct: bool


class QuestionBase(BaseModel):
    question_text: str
    choices: List[ChoiceBase]


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.get("/")
# def create_app():
#     return {"message: welcome"}


@app.get("/questions/{question_id}")
def read_questions(question_id: int, db: Session = Depends(get_db)):
    result = (
        db.query(models.Questions).filter(models.Questions.id == question_id).first()
    )
    if not result:
        raise HTTPException(
            status_code=404, detail=f"question with id {question_id} not found"
        )
    return result


@app.get("/choices/{question_id}")
def read_choice(question_id: int, db: Session = Depends(get_db)):
    result = (
        db.query(models.Questions).filter(models.Questions.id == question_id).first()
    )
    if not result:
        raise HTTPException(
            status_code=404, detail=f"question with id {question_id} not found"
        )
    return result


@app.post("/questions/")
def create_questions(quest: QuestionBase, db: Session = Depends(get_db)):
    db_question = models.Questions()
    db_question.question_text = quest.question_text
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    for choice in quest.choices:
        db_choice = models.Choice()
        db_choice.choice_text = choice.choice_text
        db_choice.is_Correct = choice.is_correct
        db_choice.question_id = db_question.id
        db.add(db_choice)
    db.commit()
    return quest
