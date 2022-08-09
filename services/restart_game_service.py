
from repositories.game_repository import GameRepository
from repositories.player_repository import PlayerRepository
from services.exceptions import NotCreatedGame


class RestartGameService:

    def __init__(self):
        self.player_repository = PlayerRepository.get_instance()
        self.game_repository = GameRepository.get_instance()

    def restart_game(self):

        players = self.player_repository.get_players()
        game = self.game_repository.get_game()
        croupier = self.player_repository.get_croupier()

        if game is None:
            raise NotCreatedGame()

        if game.get_game_status() == "started":
            raise StartedGameCantRestart()

        game.empty_game(players, croupier)


class StartedGameCantRestart(Exception):
    pass
