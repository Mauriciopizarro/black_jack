from controllers.utils import ClientErrorResponse
from services.croupier_service import (
    CroupierService,
    NotCroupierTurnError,
    NotCreatedGame,
)
from flask.views import View

from services.exceptions import GameFinishedError

croupier_service = CroupierService()


class CroupierPlayController(View):
    methods = ['POST']

    def dispatch_request(self):
        try:
            croupier_service.croupier_play()
        except NotCroupierTurnError:
            return ClientErrorResponse(
                description='Is not the croupier turn',
                code='NOT_CROUPIER_TURN',
            )
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

        return {'message': "Croupier is playing"}
