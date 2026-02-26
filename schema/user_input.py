from pydantic import BaseModel, Field
from typing import Annotated, Literal, Optional

class UserInput(BaseModel):
    rollno: Annotated[int, Field(..., description="primary each unique id for every user")]
    name: Annotated[str, Field(..., description="user name", examples=["nithin"])]
    age: Annotated[int, Field(..., gt=0, lt=80, description="age of the user")]
    college: Annotated[str, Field(..., description="user college name")]
    branch: Annotated[Literal["csm", "cse", "csd"], Field(..., description="user branch course name")]

class StudentUpdate(BaseModel):
    rollno : Annotated[Optional[int], Field(default=None)]
    name : Annotated[Optional[str], Field(default=None)]
    age : Annotated[Optional[int], Field(default=None)]
    college : Annotated[Optional[str], Field(default=None)]
    branch : Annotated[Optional[str], Field(default=None)]
    