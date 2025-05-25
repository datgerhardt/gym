
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base  = declarative_base()

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)

