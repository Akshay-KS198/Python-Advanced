from pydantic import BaseModel, Field, model_validator
from typing import Optional, Dict, Any, List, Literal

class input(BaseModel):
    query: str = Field("This is the Query")

class output(BaseModel):
    input_query: str = Field("This is Input Query")
    answer: str = Field("This is answer")

def query_results(para_1: input)-> output:
    mod_1_query = para_1.query
    mod_2_ans = "Akshay"

    return output(**{"input_query": "mod_1_query", "answer": "mod_2_ans"})

pyd_ins = input(**{"query": "Who are You"})
print(query_results(pyd_ins))