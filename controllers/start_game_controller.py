from controllers.utils import ClientErrorResponse
from services.start_game_service import StartGameService, NotPlayersCreated, GameAlreadyStarted
from flask.views import View


star_game_service = StartGameService()


class StartGameController(View):
    methods = ['POST']

    def dispatch_request(self):
        try:
            star_game_service.start_game()
        except NotPlayersCreated:
            return ClientErrorResponse(
                description='There is not players enrolled',
                code='NO_PLAYERS_ENROLLED_TO_GAME',
            )
        except GameAlreadyStarted:
            return ClientErrorResponse(
                description='There are a current game started',
                code='CURRENT_STARTED_GAME',
            )
        return {'message': "Game started"}
