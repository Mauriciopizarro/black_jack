from repositories.player_repository import PlayerRepository
from repositories.game_repository import GameRepository
from services.exceptions import NotCreatedGame


class StandService:

    def __init__(self):
        self.player_repository = PlayerRepository.get_instance()
        self.game_repository = GameRepository.get_instance()

    def stand(self):
        game = self.game_repository.get()

        if not game:
            raise NotCreatedGame()

        current_turn = game.get_current_turn()

        if not current_turn == 'player':
            raise NoTurnsToStand()

        player_1 = self.player_repository.get_player()
        player_1.stand()
        game.change_turn()


class NoTurnsToStand(Exception):
    pass
