from repositories.game_repository import GameRepository
from services.exceptions import NotCreatedGame


class StatusService:

    def __init__(self):
        self.game_repository = GameRepository.get_instance()

    def players_status(self):

        game = self.game_repository.get_game()

        if not game:
            raise NotCreatedGame()

        return game.get_status()
