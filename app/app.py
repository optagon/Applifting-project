from fastapi import FastAPI
from typing import List
import fastapi as _fastapi
from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import fields
import app.schemas as _schemas
import app.models as _models
import sqlalchemy.orm as _orm
import app.database as _database
import app.services as _services


app = _fastapi.FastAPI()
_services.create_database()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


@app.post('/token', tags=['Security'])
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return {'access_token': form_data.username + 'token'}
################################################################# Products ###################################################################

@app.post("/products/", response_model = _schemas.Product, tags=['Products'])
async def create_product(product: _schemas.ProductCreate, db: _orm.Session = _fastapi.Depends(_services.get_db), token: str = Depends(oauth2_scheme)):
    db_product = _services.get_product_by_name(db=db, name=product.name)

    if db_product:
        raise _fastapi.HTTPException(status_code=400, detail="this name already exists")
    return _services.create_product(db = db, product=product)


@app.get("/products/", response_model=List[_schemas.Product], tags=['Products'])
def read_products(skip: int = 0, limit: int = 20, db: _orm.Session = _fastapi.Depends(_services.get_db), token: str = Depends(oauth2_scheme)):
    products = _services.get_products(db=db, skip=skip, limit=limit)
    return products


@app.put("/products/{product_id}", response_model=_schemas.Product, tags=['Products'])
def update_product(product_id: int, product: _schemas.ProductCreate, db: _orm.Session = _fastapi.Depends(_services.get_db), token: str = Depends(oauth2_scheme)):
    return _services.update_product(db=db, product=product, product_id=product_id)

@app.delete("/products/{product_id}", tags=['Products'])
def delete_product(product_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db), token: str = Depends(oauth2_scheme)):
    _services.delete_product(db=db, product_id=product_id)
    return {"message": f"successfully deleted product with id: {product_id}"}


#################################################################Offers###################################################################



@app.get("/offers/", response_model=List[_schemas.Offer], tags=['Offers'])
def read_offers(skip: int = 0, limit: int = 20, db: _orm.Session = _fastapi.Depends(_services.get_db),):
    offers = _services.get_offers(db=db, skip=skip, limit=limit)
    return offers

@app.get("/offers/{offer_id}", response_model=_schemas.Offer, tags=['Offers'])
def read_offer(offer_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    offer = _services.get_offer(db=db, offer_id=offer_id)
    if offer is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this offer does not exist"
        )
    return offer

@app.put("/offers/{offer_id}", response_model=_schemas.Offer, tags=['Offers'])
def update_offer(offer_id: int, offer: _schemas.OfferCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return _services.update_offer(db=db, offer=offer, offer_id=offer_id)

@app.delete("/offers/{offer_id}", tags=['Offers'])
def delete_offer(offer_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    _services.delete_offer(db=db, offer_id=offer_id)
    return {"message": f"successfully deleted offer with id: {offer_id}"}







