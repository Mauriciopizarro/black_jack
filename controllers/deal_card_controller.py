from controllers.utils import ClientErrorResponse
from services.deal_card_service import DealCardService, NotPlayerTurn, CroupierTurn
from flask.views import View

from services.exceptions import NotCreatedGame, GameFinishedError

deal_card_service = DealCardService()


class DealCardController(View):
    methods = ['POST']

    def dispatch_request(self):
        try:
            deal_card_service.deal_card()
        except NotCreatedGame:
            return ClientErrorResponse(
                description='There is not game created',
                code='NO_GAME_CRATED',
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

        return {'message': "Card dealed to player"}
