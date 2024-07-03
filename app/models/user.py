from pydantic import EmailStr
from sqlmodel import SQLModel, Field

from .base import IdMixin, TimestampMixin


class UserBase(SQLModel):
    first_name: str = None
    last_name: str = None
    email: EmailStr = Field(
        nullable=False, index=True, sa_column_kwargs={"unique": True}
    )
    is_active: bool = True


class UserCreate(UserBase):
    ...


class UserUpdate(UserBase):
    first_name: str = None
    last_name: str = None
    email: EmailStr = None
    is_active: bool = None


class User(IdMixin, TimestampMixin, UserBase, table=True):
    __tablename__ = "users"


class UserResponse(User, table=False):
    ...

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
