from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship

class CategoryLink(SQLModel, table=True):
    __tablename__ = 'category_links'
    top_category_id: Optional[int] = Field(
        default=None, foreign_key="categories.id", primary_key=True
    )
    sub_category_id: Optional[int] = Field(
        default=None, foreign_key="categories.id", primary_key=True
    )

class CategoryBase(SQLModel):
    title: str = Field(max_length=50, unique=True, index=True)
    slug: str = Field(max_length=50, unique=True, index=True)
    description: Optional[str] = Field(default=None)
    is_subcategory: bool = Field(default=False)

class Category(CategoryBase, table=True):
    __tablename__ = 'categories'
    id: Optional[int] = Field(default=None, primary_key=True)
    sub_categories: List["Category"] = Relationship(
        back_populates="top_category",
        link_model=CategoryLink,
        sa_relationship_kwargs={"primaryjoin": "Category.id == CategoryLink.top_category_id", "secondaryjoin": "Category.id == CategoryLink.sub_category_id"}
    )
    top_category: List["Category"] = Relationship(
        back_populates="sub_categories",
        link_model=CategoryLink,
        sa_relationship_kwargs={"primaryjoin": "Category.id == CategoryLink.sub_category_id", "secondaryjoin": "Category.id == CategoryLink.top_category_id"}
    )
    products: List["Product"] = Relationship(back_populates="category")

    def __str__(self):
        return self.title
