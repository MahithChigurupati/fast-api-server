from sqlalchemy import Column, Integer, String
from database import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)


# class Questions(Base):
#     __tablename__ = "questions"

#     id = Column(Integer, primary_key=True, index=True)
#     question_text = Column(String, index=True)

# class Choices(Base):
#     __tablename__ = "choices"

#     id = Column(Integer, primary_key=True, index=True)
#     choice_text = Column(String, index=True)
#     is_correct = Column(Boolean, index=True)
#     question_id = Column(Integer, ForeignKey("questions.id"))