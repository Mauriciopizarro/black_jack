from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, Depends
from controllers.utils import authenticate_with_token
from models.user import User
from services.enroll_player_service import EnrollPlayerService, CantEnrollPlayersStartedGame
from services.enroll_player_service import IncorrectPlayersQuantity

enroll_player_service = EnrollPlayerService()
router = APIRouter()


class EnrollPlayerResponse(BaseModel):
    message: str
    name: str
    player_id: str


class EnrollPlayerController:

    @router.post("/enroll_player", response_model=EnrollPlayerResponse)
    async def enroll_player(current_user: User = Depends(authenticate_with_token)):
        try:
            enroll_player_service.enroll_player(current_user.username, current_user.user_id)
            player_id = enroll_player_service.get_player_id_created()
        except IncorrectPlayersQuantity:
            raise HTTPException(
                status_code=400, detail='Only 3 players be allowed to play'
            )
        except CantEnrollPlayersStartedGame:
            raise HTTPException(
                status_code=400, detail='Can not enroll players in game started'
            )
        return EnrollPlayerResponse(
            message="Player created successfully", name=str(current_user.username), player_id=str(player_id)
        )
