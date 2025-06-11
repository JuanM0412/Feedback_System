from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    username: str
    type: bool
    state: Optional[bool] = None


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    username: str | None = None
    evaluation_rubric: str | None = None
    business_summary: str | None = None
    folder_id: str | None = None
    sheet_id: str | None = None
    state: bool | None = None


class UserInDB(UserBase):
    id: int
    evaluation_rubric: str | None = None
    business_summary: str | None = None
    folder_id: str | None = None
    sheet_id: str | None = None

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
    type: bool | None = None
    state: bool | None = None
