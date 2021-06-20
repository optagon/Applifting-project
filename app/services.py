import sqlalchemy.orm as _orm

import app.models as _models 
import app.schemas as _schemas
import app.database as _database


def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_product(db: _orm.Session, product_id: int):
    return db.query(_models.Product).filter(_models.Product.id == product_id).first()


def get_product_by_name(db: _orm.Session, name: str):
    return db.query(_models.Product).filter(_models.Product.name == name).first()


def get_products(db: _orm.Session, skip: int = 0, limit: int = 100):
    return db.query(_models.Product).offset(skip).limit(limit).all()


def create_product(db: _orm.Session, product: _schemas.ProductCreate):
    description = product.description
    db_product = _models.Product(name=product.name, description=description)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: _orm.Session, product_id: int):
    db.query(_models.Offer).filter(_models.Offer.id == product_id).delete()
    db.commit()


def update_product(db: _orm.Session, product_id: int, product: _schemas.ProductCreate):
    db_product = get_product(db=db, product_id=product_id)
    db_product.name = product.name
    db_product.description = product.description
    db.commit()
    db.refresh(db_product)
    return db_product










def get_offers(db: _orm.Session, skip: int = 0, limit: int = 10):
    return db.query(_models.Offer).offset(skip).limit(limit).all()


def create_offer(db: _orm.Session, offer: _schemas.OfferCreate, product_id: int):
    offer = _models.Offer(**offer.dict(), context_id=product_id)
    db.add(offer)
    db.commit()
    db.refresh(offer)
    return offer


def get_offer(db: _orm.Session, offer_id: int):
    return db.query(_models.Offer).filter(_models.Offer.id == offer_id).first()


def delete_offer(db: _orm.Session, offer_id: int):
    db.query(_models.Offer).filter(_models.Offer.id == offer_id).delete()
    db.commit()


def update_offer(db: _orm.Session, offer_id: int, offer: _schemas.OfferCreate):
    db_offer = get_offer(db=db, offer_id=offer_id)
    db_offer.price = offer.price
    db_offer.items_in_stock = offer.items_in_stock
    db.commit()
    db.refresh(db_offer)
    return db_offer