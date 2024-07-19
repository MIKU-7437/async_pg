from sqlmodel import SQLModel, Field
from .base import Base, IdMixin, TimestampMixin


class ProductBase(Base):
    name:str = None
    description: str = None
    price: float = None
    in_stock: bool = None
    is_active: bool = None


class Product(ProductBase, IdMixin, TimestampMixin, table=True):
    __tablename__ = 'products'