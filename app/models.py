import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import app, app.database

class Product(app.database.Base):
    __tablename__ = "products"
    id = _sql.Column(_sql.Integer, primary_key= True, index= True)
    name = _sql.Column(_sql.String, unique= False, index= True)
    description = _sql.Column(_sql.String, unique= False, index= True)

    offers = _orm.relationship("Offer", back_populates="context")

class Offer(app.database.Base):
    __tablename__ = "offers"
    id = _sql.Column(_sql.Integer, primary_key= True, index= True)
    price = _sql.Column(_sql.Integer, unique= False, index= True)
    items_in_stock = _sql.Column(_sql.Integer, unique= False, index= True)
    context_id = _sql.Column(_sql.Integer, _sql.ForeignKey("products.id"))

    context = _orm.relationship("Product", back_populates="offers")



