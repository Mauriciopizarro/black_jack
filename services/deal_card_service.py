from repositories.game_pyson_repository import GamePysonRepository


class DealCardService:

    def __init__(self):
        self.game_repository = GamePysonRepository.get_instance()

    def deal_card(self, player_id, game_id):
        game = self.game_repository.get_game(game_id)
        game.deal_card_to_current_turn_player(player_id)
        self.game_repository.update(game)
