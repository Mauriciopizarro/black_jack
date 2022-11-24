from game_management_service.domain.interfaces.game_repository import GameRepository
from game_management_service.domain.player import Player
from dependency_injector.wiring import Provide, inject
from shared.injector import Injector


class EnrollPlayerService:

    @inject
    def __init__(self, game_repository: GameRepository = Provide[Injector.game_management_repo]):
        self.game_repository = game_repository
        self.player_id_created = None

    def enroll_player(self, username, user_id, game_id):
        game = self.game_repository.get(game_id)
        player = Player(name=username, user_id=user_id)
        game.enroll_player(player)
        self.game_repository.update(game)
        return player.user_id
