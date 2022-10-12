from repositories.game_pyson_repository import GamePysonRepository


class StartGameService:

    def __init__(self):
        self.game_repository = GamePysonRepository.get_instance()

    def start_game(self, game_id):
        game = self.game_repository.get_game(game_id)
        game.start()
        self.game_repository.update(game)
