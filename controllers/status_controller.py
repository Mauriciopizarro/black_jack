from services.status_service import StatusService
from flask.views import View


get_status_service = StatusService()


class StatusController(View):
    methods = ['GET']

    def dispatch_request(self):
        player_status_json = get_status_service.players_status()
        return player_status_json
