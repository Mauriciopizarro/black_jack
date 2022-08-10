
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel

from models.user import IncorrectPasswordError
from repositories.user_repository import NotExistentUser
from services.login_service import LoginService
from services.token_service import TokenService

router = APIRouter()
login_service = LoginService()


class Token(BaseModel):
    access_token: str
    token_type: str


class LoginRequestData(BaseModel):
    username: str
    password: str


@router.post("/login", response_model=Token)
async def login_for_access_token(json_data: LoginRequestData):
    try:
        user = login_service.authenticate_user(json_data.username, json_data.password)
    except NotExistentUser:
        raise HTTPException(
            status_code=404,
            detail="User does not exist",
        )
    except IncorrectPasswordError:
        raise HTTPException(
            status_code=400,
            detail="Incorrect password",
        )
    access_token = TokenService.generate_token(user)
    return {"access_token": access_token, "token_type": "bearer"}
