from dependency_injector.wiring import inject, Provide
from shared.injector import Injector
from game_service.domain.player import Player
from game_service.domain.interfaces.game_repository import GameRepository


class EnrollPlayerService:

    @inject
    def __init__(self, game_repository: GameRepository = Provide[Injector.game_repo]):
        self.game_repository = game_repository
        self.player_id_created = None

    def enroll_player(self, player_name, player_id, game_id):
        game = self.game_repository.get(game_id)
        player = Player(cards=[], name=player_name, player_id=player_id, status="waiting_turn")
        game.enroll_player(player)
        self.game_repository.update(game)
        return player.player_id
