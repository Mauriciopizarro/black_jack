
from controllers.utils import authenticate_with_token
from models.user import User
from services.stand_service import StandService, NoTurnsToStand, EmptyPlayerID, IncorrectPlayerTurn
from fastapi import APIRouter, HTTPException, Depends
from services.exceptions import NotCreatedGame, GameFinishedError

router = APIRouter()
stand_service = StandService()


class StandController:

    @router.post("/stand")
    async def stand_controller(current_user: User = Depends(authenticate_with_token)):
        try:
            stand_service.stand(current_user.user_id)
        except NoTurnsToStand:
            raise HTTPException(
                status_code=400, detail='There arent turns to stand',
            )
        except NotCreatedGame:
            raise HTTPException(
                status_code=400, detail='There is not game created',
            )
        except GameFinishedError:
            raise HTTPException(
                status_code=400, detail='The game is finished',
            )
        except EmptyPlayerID:
            raise HTTPException(
                status_code=400, detail='To use this resource is necessary to enter the player_id',
            )
        except IncorrectPlayerTurn:
            raise HTTPException(
                status_code=400, detail='Is not a turn to player entered',
            )
        return {'message': "Player stand"}
