from pydantic import BaseModel, Field
from typing import Annotated, Literal, Optional

class UserInput(BaseModel):
    rollno: Annotated[int, Field(..., description="primary each unique id for every user")]
    fullname: Annotated[str, Field(..., description="user fullname", examples=["nithin"])]
    age: Annotated[int, Field(..., gt=0, lt=80, description="age of the user")]
    college: Annotated[str, Field(..., description="user college fullname")]
    branch: Annotated[Literal["csm", "cse", "csd"], Field(..., description="user branch course fullname")]

class StudentUpdate(BaseModel):
    rollno : Annotated[Optional[int], Field(default=None)]
    fullname : Annotated[Optional[str], Field(default=None)]
    age : Annotated[Optional[int], Field(default=None)]
    college : Annotated[Optional[str], Field(default=None)]
    branch : Annotated[Optional[str], Field(default=None)]
    
class StudentCreate(BaseModel):
    rollno: int
    fullname: str
    age: int
    college: str
    branch: str

    class Config:
        from_attributes = True   # For Pydantic v2