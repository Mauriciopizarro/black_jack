from models.game import NotStartedGame
from repositories.game_repository import GameRepository
from services.exceptions import NotCreatedGame, GameFinishedError


class StandService:

    def __init__(self):
        self.game_repository = GameRepository.get_instance()

    def stand(self, player_id):
        game = self.game_repository.get_game()

        if not game:
            raise NotCreatedGame()

        if game.game_status != "started":
            raise NotStartedGame()

        if game.is_finished():
            raise GameFinishedError()

        if not player_id:
            raise EmptyPlayerID()

        if not game.is_player_turn(player_id):
            raise IncorrectPlayerTurn()

        game.stand_current_turn_player()


class NoTurnsToStand(Exception):
    pass


class EmptyPlayerID(Exception):
    pass


class IncorrectPlayerTurn(Exception):
    pass
