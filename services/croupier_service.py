
from repositories.game_repository import GameRepository
from services.exceptions import NotCreatedGame


class CroupierService:

    def __init__(self):
        self.game_repository = GameRepository.get_instance()

    def croupier_play(self):
        game = self.game_repository.get_game()

        if not game:
            raise NotCreatedGame()

        game.croupier_play()
