from controllers.utils import ClientErrorResponse
from services.exceptions import NotCreatedGame
from services.status_service import StatusService
from flask.views import View


get_status_service = StatusService()


class StatusController(View):
    methods = ['GET']

    def dispatch_request(self):
        try:
            player_status_json = get_status_service.players_status()
            return player_status_json
        except NotCreatedGame:
            return ClientErrorResponse(
                description='There is not game created',
                code='GAME_NOT_CRATED',
            )
