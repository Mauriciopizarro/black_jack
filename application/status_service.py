from dependency_injector.wiring import inject, Provide
from infrastructure.injector import Injector
from domain.interfaces.game_repository import GameRepository


class StatusService:

    @inject
    def __init__(self, game_repository: GameRepository = Provide[Injector.game_repo]):
        self.game_repository = game_repository

    def players_status(self, game_id):
        game = self.game_repository.get(game_id)
        return game.get_status()
