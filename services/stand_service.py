from repositories.player_repository import PlayerRepository
from repositories.game_repository import GameRepository
from services.exceptions import NotCreatedGame, GameFinishedError


class StandService:

    def __init__(self):
        self.player_repository = PlayerRepository.get_instance()
        self.game_repository = GameRepository.get_instance()

    def stand(self):
        game = self.game_repository.get()
        player_1 = self.player_repository.get_player()

        if not game:
            raise NotCreatedGame()

        if game.is_finished():
            raise GameFinishedError()

        if not game.is_player_turn(player_1):
            raise NoTurnsToStand()

        player_1.stand()
        game.change_turn()


class NoTurnsToStand(Exception):
    pass



