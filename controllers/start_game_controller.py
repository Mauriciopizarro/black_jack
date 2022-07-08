from services.start_game_service import StartGameService
from flask.views import View
from flask import request


star_game_service = StartGameService()


class StartGameController(View):
    methods = ['POST']

    def dispatch_request(self):
        player_name = request.form.get('player_name', 'Need player name to play')
        star_game_service.start_game(player_name)
        return {'message': "Game started"}
