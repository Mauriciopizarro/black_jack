from models.game import NotCroupierTurnError, NotStartedGame
from services.croupier_service import (
    CroupierService,
    NotCreatedGame,
)

from fastapi import APIRouter, HTTPException
from services.exceptions import GameFinishedError

croupier_service = CroupierService()
router = APIRouter()


@router.post("/croupier_play/{game_id}")
async def croupier_controller(game_id: int):
    try:
        croupier_service.croupier_play(game_id)
    except NotCroupierTurnError:
        raise HTTPException(
            status_code=400, detail='Is not the croupier turn',
        )
    except NotCreatedGame:
        raise HTTPException(
            status_code=400, detail='There is not game created',
        )
    except GameFinishedError:
        raise HTTPException(
            status_code=400, detail='The game is finished',
        )
    except NotStartedGame:
        raise HTTPException(
            status_code=400, detail='The game is not started',
        )
    return {'message': "Croupier is playing"}
