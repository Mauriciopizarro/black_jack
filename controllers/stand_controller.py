from flask import request
from uuid import UUID
from controllers.utils import ClientErrorResponse, authenticate_with_token
from models.user import User
from services.stand_service import StandService, NoTurnsToStand, EmptyPlayerID, IncorrectPlayerTurn
from flask.views import View
from fastapi import APIRouter, HTTPException, Body, Depends
from services.exceptions import NotCreatedGame, GameFinishedError

router = APIRouter()
stand_service = StandService()


class StandController(View):
    methods = ['POST']

    def dispatch_request(self):
        try:
            player_id = request.json.get('player_id')
            stand_service.stand(player_id)
        except NoTurnsToStand:
            return ClientErrorResponse(
                description='There arent turns to stand',
                code='NOT_TURNS_TO_STAND',
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
        except EmptyPlayerID:
            return ClientErrorResponse(
                description='To use this resource is necessary to enter the player_id',
                code='EMPTY_PLAYER_ID',
            )
        except IncorrectPlayerTurn:
            return ClientErrorResponse(
                description='Is not a turn to player entered',
                code='NOT_PLAYER_TURN',
            )

        return {'message': "Player stand"}


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
