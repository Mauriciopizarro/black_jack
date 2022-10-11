from models.game import NotPlayersEnrolled, GameAlreadyStarted
from services.exceptions import GameFinishedError, IncorrectGameID
from services.start_game_service import StartGameService
from fastapi import APIRouter, HTTPException

router = APIRouter()
star_game_service = StartGameService()


@router.post("/start_game/{game_id}")
def start_game(game_id: int):
    try:
        star_game_service.start_game(game_id)
    except NotPlayersEnrolled:
        raise HTTPException(
            status_code=400, detail='There is not players enrolled'
        )
    except IncorrectGameID:
        raise HTTPException(
            status_code=404, detail='game_id not found',
        )
    except GameAlreadyStarted:
        raise HTTPException(
            status_code=400, detail='Game already started'
        )
    except GameFinishedError:
        raise HTTPException(
            status_code=400, detail='The game_id entered are finished'
        )
    return {'message': "Game started"}
