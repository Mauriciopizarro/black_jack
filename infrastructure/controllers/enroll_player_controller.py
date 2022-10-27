from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, Depends
from application.enroll_player_service import EnrollPlayerService
from application.exceptions import IncorrectGameID, GameFinishedError
from domain.game import IncorrectPlayersQuantity, CantEnrollPlayersStartedGame, AlreadyEnrolledPlayer
from domain.user import User
from infrastructure.authentication.fast_api_authentication import authenticate_with_token

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
    except IncorrectGameID:
        raise HTTPException(
            status_code=404, detail='game_id not found',
        )
    except GameFinishedError:
        raise HTTPException(
            status_code=400, detail='The game_id entered is finished',
        )
    except CantEnrollPlayersStartedGame:
        raise HTTPException(
            status_code=400, detail='Can not enroll players in game started'
        )
    except AlreadyEnrolledPlayer:
        raise HTTPException(
            status_code=400, detail='Player already enrolled'
        )
