from fastapi import FastAPI
import requests
import string
import random

from starlette.testclient import TestClient
from pydantic import BaseModel
from app.app import *
from main import *

client = TestClient(app)


product_data = {
    "name": "".join(random.choice(string.ascii_lowercase) for i in range(15)),
    "description":"".join(random.choice(string.ascii_lowercase) for i in range(15))
}

offer_data = {
    "price": random.randint(1,1000),
    "items_in_stock": random.randint(1,1000)
}


def test_create_product():
    response = client.post("/products/", json=product_data)
    assert response.status_code == 200

def test_read_product():
    response = client.get("/products/")
    assert response.status_code == 200
def test_update_product():
    response = client.put("/products/5", json=product_data)
    assert response.status_code == 200
def test_delete_product():
    response = client.put("/products/5", json=product_data)
    assert response.status_code == 200


def test_read_offers():
    response = client.get("/offers/4")
    assert response.status_code == 200
def test_update_offers():
    response = client.put("/offers/4", json=offer_data)
    assert response.status_code == 200
def test_delete_offers():
    response = client.put("/offers/4", json=offer_data)
    assert response.status_code == 200


