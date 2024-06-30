# main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import models, crud, database, schemas

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create initial tables in the database
models.Base.metadata.create_all(bind=database.engine)

# FastAPI endpoints

@app.post("/api/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    print("Received product:", product)
    created_product = crud.create_product(db=db, product=product)
    print("Created product:", created_product)
    return created_product

@app.get("/api/products/", response_model=List[schemas.Product])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_products(db, skip=skip, limit=limit)
