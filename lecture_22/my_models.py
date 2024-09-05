# Приклад використання SQLAlchemy для створення базового класу
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user_db'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)