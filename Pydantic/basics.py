from pydantic import BaseModel, Field, StrictInt

class user_input(BaseModel):

    x : StrictInt = Field(..., description="This is a integer variable x")
    y : str = Field(default="Aks")

pyd_input = user_input(**{"x": 1})


def main_fun(para_1:user_input):
    print("Hello Akshay")

main_fun(pyd_input)