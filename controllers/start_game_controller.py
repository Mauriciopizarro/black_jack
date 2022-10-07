from models.game import NotPlayersCreated, GameAlreadyStarted, GameNeedToBeRestarted
from services.start_game_service import StartGameService, NotGameCreated
from fastapi import APIRouter, HTTPException

router = APIRouter()
star_game_service = StartGameService()


@router.post("/start_game/{game_id}")
def start_game(game_id: int):
    try:
        star_game_service.start_game(game_id)
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
    except NotGameCreated:
        raise HTTPException(
            status_code=400, detail='The game needs to be created'
        )
    return {'message': "Game started"}

