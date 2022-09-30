from models.game import Game
from repositories.game_repository import GameRepository


class CreateGameService:

    def __init__(self):
        self.game_repository = GameRepository.get_instance()

    def create_game(self):
        game = Game()
        self.game_repository.save(game)
