
from controllers.utils import authenticate_with_token
from models.game import NotStartedGame, IncorrectPlayerTurn
from models.user import User
from services.stand_service import StandService
from fastapi import APIRouter, HTTPException, Depends
from services.exceptions import GameFinishedError, IncorrectGameID

router = APIRouter()
stand_service = StandService()


@router.post("/stand/{game_id}")
async def stand_controller(game_id: int, current_user: User = Depends(authenticate_with_token)):
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
    except NotStartedGame:
        raise HTTPException(
            status_code=400, detail='The game is not started',
        )
    return {'message': "Player stand"}
