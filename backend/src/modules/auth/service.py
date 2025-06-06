from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from typing import Optional

from src.models.user import User
from src.modules.auth.schemas import UserCreate, UserInDB, UserUpdate
from src.utils.security import get_password_hash, verify_password, create_access_token
from src.core.database import get_db
from src.core.config import settings
from datetime import timedelta

class AuthService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_user(self, user_id: int) -> Optional[UserInDB]:
        db_user = self.db.query(User).filter(User.id == user_id).first()
        if db_user is None:
            return None
        return UserInDB.from_orm(db_user)

    def get_user_by_email(self, email: str) -> Optional[User]:
        return self.db.query(User).filter(User.email == email).first()

    def create_user(self, user: UserCreate) -> UserInDB:
        db_user = self.get_user_by_email(user.email)
        if db_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        
        hashed_password = get_password_hash(user.password)
        db_user = User(
            email=user.email,
            password=hashed_password,
            username=user.username
        )
        
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return UserInDB.from_orm(db_user)

    def authenticate_user(self, email: str, password: str) -> Optional[User]:
        user = self.get_user_by_email(email)
        if not user:
            return None
        if not verify_password(password, user.password):
            return None
        return user

    def create_access_token_for_user(self, user: User):
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )
        return access_token
    
    def create_refresh_token_for_user(self, user: User):
        refresh_token_expires = timedelta(days=settings.REFRESH_TOKEN_FOR_USER)
        return create_access_token(
            data={"sub": user.email}, expires_delta=refresh_token_expires
        )

    def update_user(self, user_id: int, user_update: UserUpdate) -> Optional[UserInDB]:
        db_user = self.db.query(User).filter(User.id == user_id).first()
        if db_user is None:
            return None
        
        update_data = user_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_user, key, value)
        
        self.db.commit()
        self.db.refresh(db_user)
        return UserInDB.from_orm(db_user)

    def delete_user(self, user_id: int) -> bool:
        db_user = self.db.query(User).filter(User.id == user_id).first()
        if db_user is None:
            return False
        
        self.db.delete(db_user)
        self.db.commit()
        return True