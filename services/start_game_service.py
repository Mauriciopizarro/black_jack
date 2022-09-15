
from repositories.game_repository import GameRepository


class StartGameService:

    def __init__(self):
        self.game_repository = GameRepository.get_instance()

    def start_game(self):
        game = self.game_repository.get_game()

        if game is None:
            raise NotGameCreated()

        game.start()
        self.game_repository.save(game)


class NotGameCreated(Exception):
    pass
