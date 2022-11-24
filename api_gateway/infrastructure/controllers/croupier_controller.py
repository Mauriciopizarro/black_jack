from fastapi import APIRouter, HTTPException
from game_service.application.croupier_service import CroupierService
from game_service.application.exceptions import IncorrectGameID, GameFinishedError
from game_service.domain.game import NotCroupierTurnError, NotStartedGame

croupier_service = CroupierService()
router = APIRouter()


@router.post("/croupier_play/{game_id}")
async def croupier_controller(game_id: str):
    try:
        croupier_service.croupier_play(game_id)
    except NotCroupierTurnError:
        raise HTTPException(
            status_code=400, detail='Is not the croupier turn',
        )
    except IncorrectGameID:
        raise HTTPException(
            status_code=404, detail='game_id not found',
        )
    except GameFinishedError:
        raise HTTPException(
            status_code=400, detail='The game_id entered is finished',
        )
    except NotStartedGame:
        raise HTTPException(
            status_code=400, detail='Game not started',
        )
    return {'message': "Croupier is playing"}
