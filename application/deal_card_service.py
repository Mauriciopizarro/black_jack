from dependency_injector.wiring import Provide, inject
from infrastructure.injector import Injector
from domain.interfaces.game_repository import GameRepository


class DealCardService:

    @inject
    def __init__(self, game_repository: GameRepository = Provide[Injector.game_repo]):
        self.game_repository = game_repository

    def deal_card(self, player_id, game_id):
        game = self.game_repository.get(game_id)
        game.deal_card_to_current_turn_player(player_id)
        self.game_repository.update(game)
