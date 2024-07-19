from pydantic import EmailStr
from sqlmodel import SQLModel, Field

from .base import Base, IdMixin, TimestampMixin


class UserBase(Base):
    first_name: str = Field(default=None)
    last_name: str = Field(default=None)
    email: EmailStr = Field(nullable=False, index=True, sa_column_kwargs={"unique": True})
    is_active: bool = Field(default=True)


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    first_name: str = Field(default=None)
    last_name: str = Field(default=None)
    email: EmailStr = Field(default=None)
    is_active: bool = Field(default=None)


class User(IdMixin, TimestampMixin, UserBase, table=True):
    __tablename__ = "users"


class UserResponse(User, table=False):
    pass
