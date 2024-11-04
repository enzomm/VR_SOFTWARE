from app.ext.database import db
from decimal import Decimal


class Product(db.Model):
    __table_name__ = "Product"

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.Text, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    cost = db.Column(db.Numeric(10, 2), nullable=False, default=Decimal('0.00'))
    type = db.Column(db.String(64), nullable=False)

    def serialize(self):
        return {
            'id': str(self.id),
            'image': self.image,
            'description': self.description,
            'cost': str(self.cost),
            'type': self.type
        }


class Store(db.Model):
    __table_name__ = "Store"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)


class StoreProduct(db.Model):
    __table_name__ = "StoreProduct"

    id = db.Column(db.Integer, primary_key=True)  
    product_id = db.Column("product_id", db.Integer, db.ForeignKey(Product.id))
    store_id = db.Column("store_id", db.Integer, db.ForeignKey(Store.id))
    price = db.Column(db.Numeric(10, 2), nullable=False, default=Decimal('0.00'))
