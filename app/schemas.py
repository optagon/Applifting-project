import pydantic as _pydantic
from typing import List

class _OfferBase(_pydantic.BaseModel):
    price: int
    items_in_stock: int

{
    "price": 10,
    "items_in_stock": 15
}

class OfferCreate(_OfferBase):
    pass

{
    "id": 1,
    "context_id": 23,
    "price": 10,
    "items_in_stock": 15,
}

class Offer(_OfferBase):
    id: int
    price: int
    items_in_stock: int

    class Config:
        orm_mode = True



class _ProductBase(_pydantic.BaseModel):
    name: str
    description: str

class ProductCreate(_ProductBase):
    description: str

class Product(_ProductBase):
    id: int
    offers: List[Offer] = []

    class Config:
        orm_mode = True

