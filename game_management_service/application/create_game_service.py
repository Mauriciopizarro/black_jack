from game_management_service.domain.game import Game
from game_management_service.domain.interfaces.game_repository import GameRepository
from game_management_service.domain.player import Player
from dependency_injector.wiring import Provide, inject
from shared.injector import Injector


class CreateGameService:

    @inject
    def __init__(self, game_repository: GameRepository = Provide[Injector.game_management_repo]):
        self.game_repository = game_repository

    def create_game(self, user_id: str, username: str):
        admin = Player(name=username, user_id=user_id)
        game = Game(status="created", players=[admin], admin=admin)
        response_game = self.game_repository.save(game)
        return response_game
