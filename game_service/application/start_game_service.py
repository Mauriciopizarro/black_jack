from dependency_injector.wiring import Provide, inject
from shared.injector import Injector
from game_service.domain.interfaces.game_repository import GameRepository


class StartGameService:

    @inject
    def __init__(self, game_repository: GameRepository = Provide[Injector.game_repo]):
        self.game_repository = game_repository

    def start_game(self, game_id):
        game = self.game_repository.get(game_id)
        game.start()
        self.game_repository.update(game)
