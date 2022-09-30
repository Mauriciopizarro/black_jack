from repositories.game_repository import GameRepository
from services.exceptions import NotCreatedGame


class DealCardService:

    def __init__(self):
        self.game_repository = GameRepository.get_instance()

    def deal_card(self, player_id):
        game = self.game_repository.get_game()

        if not player_id:
            raise EmptyPlayerID()

        if not game:
            raise NotCreatedGame()

        game.deal_card_to_current_turn_player(player_id)


class EmptyPlayerID(Exception):
    pass
