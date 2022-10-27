from dependency_injector.wiring import Provide, inject
from infrastructure.injector import Injector
from domain.interfaces.game_repository import GameRepository


class CroupierService:

    @inject
    def __init__(self, game_repository: GameRepository = Provide[Injector.game_repo]):
        self.game_repository = game_repository

    def croupier_play(self, game_id):
        game = self.game_repository.get(game_id)
        game.croupier_play()
        self.game_repository.update(game)
