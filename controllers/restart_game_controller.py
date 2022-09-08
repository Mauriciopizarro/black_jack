
from services.exceptions import NotCreatedGame
from services.restart_game_service import RestartGameService, StartedGameCantRestart
from fastapi import APIRouter, HTTPException


restart_game_service = RestartGameService()
router = APIRouter()


class RestartGameController:

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
