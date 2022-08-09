
from flask.views import View
from controllers.utils import ClientErrorResponse
from services.exceptions import NotCreatedGame
from services.restart_game_service import RestartGameService, StartedGameCantRestart

restart_game_service = RestartGameService()


class RestartGameController(View):

    methods = ['POST']

    def dispatch_request(self):
        try:
            restart_game_service.restart_game()
        except StartedGameCantRestart:
            return ClientErrorResponse(
                description='Started game can not be restarted',
                code='STARTED_GAME_CANT_RESTART',
            )
        except NotCreatedGame:
            return ClientErrorResponse(
                description='There is not game created',
                code='GAME_NOT_CRATED',
            )
        return {'message': "Game status restarted"}
