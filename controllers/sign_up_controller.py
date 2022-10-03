from pydantic import BaseModel
from fastapi import HTTPException, APIRouter

from models.user import EmptyPasswordError
from repositories.user_pyson_repository import UserExistent
from services.sign_up_service import SignUpService

router = APIRouter()
sign_up_service = SignUpService()


class SignUpRequestData(BaseModel):
    username: str
    password: str


class SignUpResponseData(BaseModel):
    token: str
    username: str
    user_id: str


@router.post("/sign_up", response_model=SignUpResponseData)
async def sign_up_controller(request: SignUpRequestData):
    try:
        return sign_up_service.sign_up(request.username, request.password)
    except EmptyPasswordError:
        raise HTTPException(
            status_code=400,
            detail="Empty password, please complete the password field",
        )
    except UserExistent:
        raise HTTPException(
            status_code=400,
            detail="Username already in use, try another",
        )
