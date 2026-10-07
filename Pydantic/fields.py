from pydantic import BaseModel, Field, EmailStr
from typing import Literal

class personal_info(BaseModel):
    name : str = Field(...,min_length=3,max_length=20,description="This is name")
    age : int | None = Field(ge=0,description="This is age")
    email : EmailStr = Field(...,description="This is email")
    gender : Literal["male", "female", "othelp-r "] = Field(...,description="This is gender")
    salaries : list[int] = Field(...,description="This is salaries")

p_info = personal_info(**{"name": "Akshay", "age": 24, "email": "akshayksgowda@gmail.com", "gender": "male", "salaries": [0,0]})

def info_retrieval(para_1:personal_info):
    print("name:", para_1.name)
    print("email:", para_1.email)
    print("age:", para_1.age)
    print("gender:", para_1.gender)
    print("salaries:", para_1.salaries)

info_retrieval(p_info)