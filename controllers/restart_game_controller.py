
from flask.views import View
from controllers.utils import ClientErrorResponse
from services.exceptions import NotCreatedGame
from services.restart_game_service import RestartGameService, StartedGameCantRestart
from fastapi import APIRouter, HTTPException


restart_game_service = RestartGameService()
router = APIRouter()


class RestartGameController(View):

    methods = ['POST']

    def dispatch_request(self):
        try:
            restart_game_service.restart_game()
        except StartedGameCantRestart:
            return ClientErrorResponse(
                description='Started game can not be restarted',
                code='STARTED_GAME_CANT_RESTART',
            )
        except NotCreatedGame:
            return ClientErrorResponse(
                description='There is not game created',
                code='GAME_NOT_CRATED',
            )
        return {'message': "Game status restarted"}


@router.post("/restart_game")
async def restart_game_controller():
    try:
        restart_game_service.restart_game()
    except StartedGameCantRestart:
        raise HTTPException(
            status_code=400, detail='Started game can not be restarted',
        )
    except NotCreatedGame:
        raise HTTPException(
            status_code=400, detail='There is not game created',
        )
    return {'message': "Game status restarted"}
