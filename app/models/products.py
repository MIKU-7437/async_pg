from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime

class ProductBase(SQLModel):
    title: str = Field(max_length=50, unique=True)
    slug: str = Field(max_length=50, unique=True)
    price: int = Field()
    is_available: bool = Field(default=True)
    description: Optional[str] = Field(default=None, max_length=500)
    stock: int = Field()
    created_date: datetime = Field(default_factory=datetime.utcnow)
    modified_date: datetime = Field(default_factory=datetime.utcnow)
    photo: Optional[str] = Field(default=None)

class Product(ProductBase, table=True):
    __tablename__ = 'products'
    id: Optional[int] = Field(default=None, primary_key=True)
    category_id: Optional[int] = Field(default=None, foreign_key="categories.id")
    category: Optional["Category"] = Relationship(back_populates="products")

    def __str__(self):
        return self.title
