from controllers.utils import ClientErrorResponse
from services.start_game_service import StartGameService, CantPlayersIncorrect
from flask.views import View
from flask import request


star_game_service = StartGameService()


class StartGameController(View):
    methods = ['POST']

    def dispatch_request(self):
        try:
            player_name = request.json.get('player_name', 'Player')
            cant_players = request.json.get('players_quantity', 1)
            star_game_service.start_game(player_name, cant_players)
        except CantPlayersIncorrect:
            return ClientErrorResponse(
                description='Quantity of players incorrect, max 3',
                code='QUANTITY_PLAYERS_ERROR',
            )
        return {'message': "Game started"}
