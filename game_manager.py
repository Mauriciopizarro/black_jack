from deck_manager import DeckManager
from player_manager import PlayerManager


class GameManager:

    def __init__(self, player_name):
        self.deck_manager = DeckManager()
        self.player_manager = PlayerManager(player_name)

    def start_game(self):
        player1_cards = self.deck_manager.get_cards(2)
        player2_cards = self.deck_manager.get_cards(2)
        self.player_manager.deal_cards_to_players(player1_cards, player2_cards)

        response = self.player_manager.get_players_status()
        return response
