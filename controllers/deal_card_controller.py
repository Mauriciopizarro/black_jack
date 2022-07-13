from controllers.utils import ClientErrorResponse
from services.deal_card_service import DealCardService, StandPlayerCantReciveCardsError, PlayerOverLimitDealCardError
from flask.views import View

deal_card_service = DealCardService()


class DealCardController(View):
    methods = ['POST']

    def dispatch_request(self):
        try:
            deal_card_service.deal_card()
        except StandPlayerCantReciveCardsError:
            return ClientErrorResponse(
                description='Player is stand and cant receive cards',
                code='STAND_PLAYERS_CANT_RECEIVE_CARDS',
            )

        except PlayerOverLimitDealCardError:
            return ClientErrorResponse(
                description='Player is over the limit and cant receive cards',
                code='PLAYER_OVER_LIMIT_CANT_RECEIVE_CARDS',
            )

        return {'message': "Card deal!"}
