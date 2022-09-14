
from services.croupier_service import (
    CroupierService,
    NotCroupierTurnError,
    NotCreatedGame,
)

from fastapi import APIRouter, HTTPException
from services.exceptions import GameFinishedError

croupier_service = CroupierService()
router = APIRouter()


class CroupierPlayController:

    @router.post("/croupier_play")
    async def croupier_controller():
        try:
            croupier_service.croupier_play()
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
        return {'message': "Croupier is playing"}
