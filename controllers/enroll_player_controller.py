from flask import request
from flask.views import View

from controllers.utils import ClientErrorResponse
from services.enroll_player_service import EnrollPlayerService, CantEnrollPlayersStartedGame
from services.enroll_player_service import IncorrectPlayersQuantity

enroll_player_service = EnrollPlayerService()


class EnrollPlayerController(View):

    methods = ['POST']

    def dispatch_request(self):
        try:
            player_name = request.json.get('player_name', 'Player')
            enroll_player_service.enroll_player(player_name)
        except IncorrectPlayersQuantity:
            return ClientErrorResponse(
                description='Only 3 players be allowed to play',
                code='QUANTITY_PLAYERS_ERROR',
            )
        except CantEnrollPlayersStartedGame:
            return ClientErrorResponse(
                description='Can not enroll players in game started',
                code='CAN_NOT_ENROLL_PLAYERS',
            )
        message = "Player " + str(player_name) + " created"
        return {'message': message}
