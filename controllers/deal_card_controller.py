from flask import request

from controllers.utils import ClientErrorResponse
from services.deal_card_service import DealCardService, NotPlayerTurn, CroupierTurn, IncorrectPlayerTurn, EmptyPlayerID
from flask.views import View

from services.exceptions import NotCreatedGame, GameFinishedError

deal_card_service = DealCardService()


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
