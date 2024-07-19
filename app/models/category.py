from sqlmodel import SQLModel, Field

from .base import Base, IdMixin, TimestampMixin


class CategoryBase(Base):
    name:str = None
    description: str = None


class Category(CategoryBase, IdMixin, TimestampMixin, table=True):
    __tablename__ = 'categories'