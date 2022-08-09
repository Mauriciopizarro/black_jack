from flask import request

from controllers.utils import ClientErrorResponse
from services.exceptions import NotCreatedGame, GameFinishedError
from services.stand_service import StandService, NoTurnsToStand, EmptyPlayerID, IncorrectPlayerTurn
from flask.views import View


stand_service = StandService()


class StandController(View):
    methods = ['POST']

    def dispatch_request(self):
        try:
            player_id = request.json.get('player_id')
            stand_service.stand(player_id)
        except NoTurnsToStand:
            return ClientErrorResponse(
                description='There arent turns to stand',
                code='NOT_TURNS_TO_STAND',
            )
        except NotCreatedGame:
            return ClientErrorResponse(
                description='There is not game created',
                code='GAME_NOT_CRATED',
            )
        except GameFinishedError:
            return ClientErrorResponse(
                description='The game is finished',
                code='GAME_FINISHED',
            )
        except EmptyPlayerID:
            return ClientErrorResponse(
                description='To use this resource is necessary to enter the player_id',
                code='EMPTY_PLAYER_ID',
            )
        except IncorrectPlayerTurn:
            return ClientErrorResponse(
                description='Is not a turn to player entered',
                code='NOT_PLAYER_TURN',
            )

        return {'message': "Player stand"}
