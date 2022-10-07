from repositories.game_pyson_repository import GamePysonRepository
from services.exceptions import NotCreatedGame


class StatusService:

    def __init__(self):
        self.game_repository = GamePysonRepository.get_instance()

    def players_status(self, game_id):

        game = self.game_repository.get_game(game_id)

        if not game:
            raise NotCreatedGame()

        return game.get_status()
