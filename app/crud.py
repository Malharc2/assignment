from sqlalchemy.orm import Session
from . import models, schemas  # Import schemas module

def create_product(db: Session, product: schemas.ProductCreate):
    print(f"Creating product: {product}")
    db_product = models.Product(name=product.name, price=product.price, retailer_name=product.retailer_name)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    print(f"Created product in DB: {db_product}")
    return db_product

def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Product).offset(skip).limit(limit).all()
