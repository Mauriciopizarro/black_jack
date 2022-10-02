from pydantic import BaseModel
from fastapi import HTTPException, APIRouter
from services.sign_up_service import SignUpService, EmptyPasswordError, UserExistent

router = APIRouter()
sign_up_service = SignUpService()


class SignUpRequestData(BaseModel):
    username: str
    password: str


@router.post("/sign_up")
async def sign_up_controller(json_data: SignUpRequestData):
    try:
        sign_up_service.sign_up(json_data.username, json_data.password)
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
    return {"User created succesfully"}
