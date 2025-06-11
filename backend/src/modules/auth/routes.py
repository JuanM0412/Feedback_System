from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from src.models.user import User
from src.modules.auth.dependencies import (
    get_current_admin_user,
    get_current_user,
    get_current_user_state,
)
from src.modules.auth.schemas import Token, UserCreate, UserInDB, UserUpdate
from src.modules.auth.service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/admin/create_user")
def register(user: UserCreate, auth_service: AuthService = Depends(),
             current_user: User = Depends(get_current_admin_user)):
    try:
        db_user = auth_service.create_user(user)

        return JSONResponse(
            status_code=201,
            content={
                "status": "success",
                "message": "User registered successfully",
                "data": {
                    "user": db_user.dict()
                }
            }
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.get("/admin/users")
def get_users(auth_service: AuthService = Depends(),
              current_user: User = Depends(get_current_admin_user)):
    users = auth_service.get_users()
    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No users found")
    return users


@router.post("/token", response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(),
):
    user = auth_service.authenticate_user(
        form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth_service.create_access_token_for_user(user)
    refresh_token = auth_service.create_refresh_token_for_user(user)
    print(f"Access Token: {access_token}")
    print(f"Refresh Token: {refresh_token}")
    print(f"User Type: {user.type}")
    return JSONResponse(
        status_code=201,
        content={
            "status": "success",
            "message": "User registered successfully",
            "data": {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "type": user.type,
                "state": user.state,
                "token_type": "bearer"
            },
        }
    )


@router.get("/me", response_model=UserInDB)
def read_users_me(current_user: User = Depends(get_current_user),
                  user_state: User = Depends(get_current_user_state)):
    return current_user


@router.put("/me", response_model=UserInDB)
def update_user_me(
    user_update: UserUpdate,
    current_user: User = Depends(get_current_user),
    auth_service: AuthService = Depends(),
    user_state: User = Depends(get_current_user_state)
):
    return auth_service.update_user(current_user.id, user_update)


@router.put("/admin/users/{user_id}")
def update_user_state(
    user_id: int,
    user_update: UserUpdate,
    auth_service: AuthService = Depends(),
    current_user: User = Depends(get_current_admin_user)
):
    updated_user = auth_service.update_user(user_id, user_update)
    if updated_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found")

    return JSONResponse(
        status_code=200,
        content={
            "status": "success",
            "message": f"User {'activated' if user_update.state else 'deactivated'} successfully",
            "data": updated_user.dict()
        }
    )
