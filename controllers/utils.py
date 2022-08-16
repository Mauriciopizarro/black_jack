from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from services.token_service import TokenService, InvalidTokenError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def ClientErrorResponse(code, description=''):
    description_dict = {
        'description': description,
        'code': code
    }
    return description_dict, 400


async def authenticate_with_token(token: str = Depends(oauth2_scheme)):
    try:
        return TokenService.get_user_by_token(token)
    except InvalidTokenError:
        raise HTTPException(
            status_code=400,
            detail="Invalid Token",
        )
