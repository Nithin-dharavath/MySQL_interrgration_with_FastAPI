from sqlalchemy import Column, Integer, String
from database import Base

class Student(Base):
    __tablename__ = "students"

    rollno = Column(Integer, primary_key=True, index=True)
    fullname = Column(String(225))
    age = Column(Integer)
    college = Column(String(225))
    branch = Column(String(225))