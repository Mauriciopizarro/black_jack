from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, Depends
from controllers.utils import authenticate_with_token
from models.game import IncorrectPlayersQuantity, AlreadyEnrolledPlayer, CantEnrollPlayersStartedGame
from models.user import User
from services.enroll_player_service import EnrollPlayerService
from services.exceptions import NotCreatedGame

enroll_player_service = EnrollPlayerService()
router = APIRouter()


class EnrollPlayerResponse(BaseModel):
    message: str
    name: str
    player_id: str


@router.post("/enroll_player/{game_id}", response_model=EnrollPlayerResponse)
async def enroll_player(game_id: int, current_user: User = Depends(authenticate_with_token)):
    try:
        player_id = enroll_player_service.enroll_player(current_user.username, current_user.id, game_id)
        return EnrollPlayerResponse(
            message="Player enrolled successfully",
            name=str(current_user.username),
            player_id=str(player_id)
        )
    except IncorrectPlayersQuantity:
        raise HTTPException(
            status_code=400, detail='Only 3 players be allowed to play'
        )
    except CantEnrollPlayersStartedGame:
        raise HTTPException(
            status_code=400, detail='Can not enroll players in game started'
        )
    except NotCreatedGame:
        raise HTTPException(
            status_code=400, detail='Not game created'
        )
    except AlreadyEnrolledPlayer:
        raise HTTPException(
            status_code=400, detail='Player already enrolled'
        )
