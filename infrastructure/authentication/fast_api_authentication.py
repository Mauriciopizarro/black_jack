from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from application.token_service import TokenService, InvalidTokenError
from domain.user import UserInDB
from infrastructure.repositories.user.user_pyson_repository import NotExistentUser


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def authenticate_with_token(token: str = Depends(oauth2_scheme)) -> UserInDB:
    try:
        return TokenService.get_user_by_token(token)
    except NotExistentUser:
        raise HTTPException(
            status_code=404, detail='User not found',
        )
    except InvalidTokenError:
        raise HTTPException(
            status_code=400,
            detail="Invalid Token",
        )
