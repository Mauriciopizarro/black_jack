
from services.start_game_service import StartGameService, NotPlayersCreated, GameAlreadyStarted, GameNeedToBeRestarted
from fastapi import APIRouter, HTTPException

router = APIRouter()
star_game_service = StartGameService()


class StartGameController:

    @router.post("/start_game")
    def start_game():
        try:
            star_game_service.start_game()
        except NotPlayersCreated:
            raise HTTPException(
                status_code=400, detail='There is not players enrolled'
            )
        except GameAlreadyStarted:
            raise HTTPException(
                status_code=400, detail='There are a current game started'
            )
        except GameNeedToBeRestarted:
            raise HTTPException(
                status_code=400, detail='The game need to be restarted'
            )
        return {'message': "Game started"}
