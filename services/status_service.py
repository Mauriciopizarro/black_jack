from repositories.game_repository import GameRepository
from repositories.player_repository import PlayerRepository
from services.exceptions import NotCreatedGame


class StatusService:

    def __init__(self):
        self.player_repository = PlayerRepository.get_instance()
        self.game_repository = GameRepository.get_instance()

    def players_status(self):
        player_1 = self.player_repository.get_player()
        croupier = self.player_repository.get_croupier()
        game = self.game_repository.get()

        if not game:
            raise NotCreatedGame()

        player_status_json = {
            'player': player_1.get_status(),
            'croupier': croupier.get_status()
        }
        return player_status_json
