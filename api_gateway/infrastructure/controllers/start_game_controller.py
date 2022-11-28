from fastapi import APIRouter, HTTPException, Depends
from api_gateway.domain.user import User
from api_gateway.infrastructure.authentication.fast_api_authentication import authenticate_with_token
from api_gateway.infrastructure.controllers.exceptions import IncorrectGameID
from game_management_service.domain.exceptions import IncorrectAdminId, GameAlreadyStarted
from game_management_service.application.start_game_service import StartGameService


router = APIRouter()
star_game_service = StartGameService()


@router.post("/start_game/{game_id}")
def start_game(game_id: str, current_user: User = Depends(authenticate_with_token)):
    try:
        star_game_service.start_game(game_id, current_user.id)
    except IncorrectGameID:
        raise HTTPException(
            status_code=404, detail='game_id not found',
        )
    except GameAlreadyStarted:
        raise HTTPException(
            status_code=400, detail='Game already started'
        )
    except IncorrectAdminId:
        raise HTTPException(
            status_code=400, detail='User not enabled for this action'
        )
    return {'message': "Game started"}
