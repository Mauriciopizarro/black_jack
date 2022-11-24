from game_service.application.exceptions import IncorrectGameID, GameFinishedError
from game_service.application.start_game_service import StartGameService
from fastapi import APIRouter, HTTPException
from game_service.domain.game import NoPlayersEnrolled, GameAlreadyStarted

router = APIRouter()
star_game_service = StartGameService()


@router.post("/start_game/{game_id}")
def start_game(game_id: str):
    try:
        star_game_service.start_game(game_id)
    except NoPlayersEnrolled:
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
            status_code=400, detail='The game_id entered is finished'
        )
    return {'message': "Game started"}
