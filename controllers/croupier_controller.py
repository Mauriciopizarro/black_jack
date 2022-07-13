from controllers.utils import ClientErrorResponse
from services.croupier_service import (
    CroupierService,
    NotCroupierTurnError,
    CroupierCantPlayFinishedGameError,
    NotCreatedGame,
)
from flask.views import View

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
        except CroupierCantPlayFinishedGameError:
            return ClientErrorResponse(
                description='Croupier cant play because the game is finished',
                code='FINISHED_GAME',
            )
        except NotCreatedGame:
            return ClientErrorResponse(
                description='There is not game created',
                code='NO_GAME_CRATED',
            )

        return {'message': "Croupier is playing"}
