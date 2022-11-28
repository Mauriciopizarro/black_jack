from game_service.application.exceptions import IncorrectGameID, GameFinishedError
from game_service.application.stand_service import StandService
from game_service.domain.game import IncorrectPlayerTurn
from api_gateway.domain.user import User
from fastapi import APIRouter, HTTPException, Depends
from api_gateway.infrastructure.authentication.fast_api_authentication import authenticate_with_token

router = APIRouter()
stand_service = StandService()


@router.post("/stand/{game_id}")
async def stand_controller(game_id: str, current_user: User = Depends(authenticate_with_token)):
    try:
        stand_service.stand(current_user.id, game_id)
    except IncorrectGameID:
        raise HTTPException(
            status_code=404, detail='game_id not found',
        )
    except GameFinishedError:
        raise HTTPException(
            status_code=400, detail='The game_id entered is finished',
        )
    except IncorrectPlayerTurn:
        raise HTTPException(
            status_code=400, detail='Is not a turn to player entered',
        )
    return {'message': "Player stand"}
