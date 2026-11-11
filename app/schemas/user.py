from pydantic import BaseModel,EmailStr,ConfigDict
from typing import Optional


class UserBase(BaseModel):
    first_name: Optional[str] = None
    surname: Optional[str] = None
    email: Optional[EmailStr] = None
    is_superuser: bool = False


class UserCreate(UserBase):
    email: EmailStr


class UserUpdate(UserBase):
    ...


class UserInDBBase(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: Optional[int] = None


class User(UserInDBBase):
    pass 