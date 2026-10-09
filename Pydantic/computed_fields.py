from pydantic import BaseModel, computed_field, Field
from typing import Optional, Dict, Any, List, Literal

class orders(BaseModel):
    order_id: int = Field(..., description="This is order_id")
    units : int = Field(..., description="This is unit_price")
    amount: int = Field(..., description="This is amount per unit")
    

    @computed_field
    @property
    def total_amount(self)-> int:
        return self.units*self.amount

pyd_ins = orders(**{"order_id": "1","units": "10", "amount": "800"})

print(pyd_ins)


