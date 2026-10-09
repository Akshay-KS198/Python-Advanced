from pydantic import BaseModel, Field, model_validator
from typing import Optional, Dict, Any, List, Literal

class api_auth(BaseModel):
    email: str = Field(...,description="This is the email")
    password: str = Field(...,description="This is password")
    confirm_password: str = Field(...,description="This is confirm password")

    @model_validator(mode="after")
    def password_check(cls,values):
        if values.password != values.confirm_password:
            raise ValueError("Passwords Didnt Match")
        return values
pyd_ins = api_auth(**{"email": "akshayksgowda@gmail.com", "password": "test1", "confirm_password": "test1"})
print(pyd_ins)