from sqlalchemy import Column, Integer, String, Float
from .database import Base

# SQLAlchemy Product model
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    retailer_name = Column(String)