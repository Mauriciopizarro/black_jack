from models.game import Game
from repositories.game_pyson_repository import GamePysonRepository


class CreateGameService:

    def __init__(self):
        self.game_repository = GamePysonRepository.get_instance()

    def create_game(self):
        game = Game.create()
        game_id = self.game_repository.save(game)
        return game_id
