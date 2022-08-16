from flask import request
from controllers.utils import ClientErrorResponse, authenticate_with_token
from models.user import User
from services.deal_card_service import DealCardService, NotPlayerTurn, CroupierTurn, IncorrectPlayerTurn, EmptyPlayerID
from flask.views import View
from fastapi import APIRouter, HTTPException, Depends
from services.exceptions import NotCreatedGame, GameFinishedError


deal_card_service = DealCardService()
router = APIRouter()


class DealCardController(View):
    methods = ['POST']

    def dispatch_request(self):
        try:
            player_id = request.json.get('player_id')
            deal_card_service.deal_card(player_id)
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
        except NotPlayerTurn:
            return ClientErrorResponse(
                description='Is not player turn',
                code='ANOTHER_PLAYER_TURN',
            )
        except CroupierTurn:
            return ClientErrorResponse(
                description='Is turn to croupier',
                code='TURN_TO_CROUPIER',
            )
        except IncorrectPlayerTurn:
            return ClientErrorResponse(
                description='Is not a turn to player entered or id may be incorrect',
                code='NOT_PLAYER_TURN',
            )
        except EmptyPlayerID:
            return ClientErrorResponse(
                description='To use this resource is necessary to enter the player_id',
                code='EMPTY_PLAYER_ID',
            )

        return {'message': "Card dealed to player"}


@router.post("/deal_card")
async def deal_card_controller(current_user: User = Depends(authenticate_with_token)):
    try:
        deal_card_service.deal_card(current_user.user_id)
    except NotCreatedGame:
        raise HTTPException(
            status_code=400, detail='There is not game created',
        )
    except GameFinishedError:
        raise HTTPException(
            status_code=400, detail='The game is finished'
        )
    except NotPlayerTurn:
        raise HTTPException(
            status_code=400, detail='Is not player turn'
        )
    except CroupierTurn:
        raise HTTPException(
            status_code=400, detail='Is turn to croupier'
        )
    except IncorrectPlayerTurn:
        raise HTTPException(
            status_code=400, detail='Is not a turn to player entered or id may be incorrect'
        )
    except EmptyPlayerID:
        raise HTTPException(
            status_code=400, detail='To use this resource is necessary to enter the player_id'
        )
    return {'message': "Card dealed to player"}
