from pydantic import BaseModel, Field, field_validator
from typing import Literal

class info(BaseModel):
    name : str = Field(...,description="This is name")
    email : str = Field(...,description="This is email")

    @field_validator("email")
    def email_check(cls, value):
        if "@" not in value:
            raise ValueError("Email Error")
        else:
            return value

pyd_obj = info(**{"name": "Akshay", "email": "akshayks@gmail.com"})

def main(para_1:info):
    print("name", para_1.name)
    print("email", para_1.email)

main(pyd_obj)