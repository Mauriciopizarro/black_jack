from repositories.game_pyson_repository import GamePysonRepository


class CroupierService:

    def __init__(self):
        self.game_repository = GamePysonRepository.get_instance()

    def croupier_play(self, game_id):
        game = self.game_repository.get_game(game_id)
        game.croupier_play()
        self.game_repository.update(game)
