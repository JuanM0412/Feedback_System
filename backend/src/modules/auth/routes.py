from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse

from src.models.user import User
from src.modules.auth.schemas import UserCreate, UserInDB, UserUpdate, Token
from src.modules.auth.service import AuthService
from src.modules.auth.dependencies import get_current_user
from src.core.database import get_db

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
def register(user: UserCreate, auth_service: AuthService = Depends()):
    try:
        db_user = auth_service.create_user(user)
        access_token = auth_service.create_access_token_for_user(db_user)
        refresh_token = auth_service.create_refresh_token_for_user(db_user)

        return JSONResponse(
            status_code=201,
            content={
                "status": "success",
                "message": "User registered successfully",
                "data": {
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "token_type": "bearer",
                    "user": db_user.dict()
                }
            }
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.post("/token", response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends()
):
    user = auth_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth_service.create_access_token_for_user(user)
    refresh_token = auth_service.create_refresh_token_for_user(user)
    return JSONResponse(
            status_code=201,
            content={
                "status": "success",
                "message": "User registered successfully",
                "data": {
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "token_type": "bearer"
                }
            }
        )

@router.get("/me", response_model=UserInDB)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.put("/me", response_model=UserInDB)
def update_user_me(
    user_update: UserUpdate,
    current_user: User = Depends(get_current_user),
    auth_service: AuthService = Depends()
):
    return auth_service.update_user(current_user.id, user_update)

@router.delete("/me")
def delete_user_me(
    current_user: User = Depends(get_current_user),
    auth_service: AuthService = Depends()
):
    success = auth_service.delete_user(current_user.id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return {"message": "User deleted successfully"}