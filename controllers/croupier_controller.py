from controllers.utils import ClientErrorResponse
from services.croupier_service import (
    CroupierService,
    NotCroupierTurnError,
    NotCreatedGame,
)
from flask.views import View
from fastapi import APIRouter, HTTPException
from services.exceptions import GameFinishedError

croupier_service = CroupierService()
router = APIRouter()


class CroupierPlayController(View):
    methods = ['POST']

    def dispatch_request(self):
        try:
            croupier_service.croupier_play()
        except NotCroupierTurnError:
            return ClientErrorResponse(
                description='Is not the croupier turn',
                code='NOT_CROUPIER_TURN',
            )
        except NotCreatedGame:
            return ClientErrorResponse(
                description='There is not game created',
                code='GAME_NOT_CRATED',
            )
        except GameFinishedError:
            return ClientErrorResponse(
                description='The game is finished',
                code='GAME_FINISHED',
            )

        return {'message': "Croupier is playing"}


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
