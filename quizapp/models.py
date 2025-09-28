from sqlalchemy import String, Integer, Boolean, ForeignKey, Column

from database import Base


class Questions(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String, index=True)


class Choice(Base):
    __tablename__ = "choices"
    is_correct = Column(Boolean, index=True)
    id = Column(Integer, primary_key=True, index=True)
    choice_text = Column(String, index=True)
    question_id = Column(Integer, ForeignKey("questions.id"))
