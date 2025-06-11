from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from src.core.config import settings
from src.core.database import get_db
from src.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[
                settings.ALGORITHM])
        email: str = payload.get("sub")
        user_type: bool = payload.get("type")
        user_state: bool = payload.get("state")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise credentials_exception

    user.type = user_type
    user.state = user_state
    return user


def get_current_admin_user(current_user: User = Depends(get_current_user)):
    if not current_user.type:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin privileges required"
        )
    return current_user


def get_current_user_state(current_user: User = Depends(get_current_user)):
    if not current_user.state:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User activation required"
        )
    return current_user
