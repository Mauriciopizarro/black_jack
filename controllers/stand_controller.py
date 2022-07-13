from controllers.utils import ClientErrorResponse
from services.exceptions import NotCreatedGame, GameFinishedError
from services.stand_service import StandService, NoTurnsToStand
from flask.views import View


stand_service = StandService()


class StandController(View):
    methods = ['POST']

    def dispatch_request(self):
        try:
            stand_service.stand()
        except NoTurnsToStand:
            return ClientErrorResponse(
                description='There arent turns to stand',
                code='NOT_TURNS_TO_STAND',
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

        return {'message': "Stand"}
