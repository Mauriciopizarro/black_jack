import player_manager
from deck_manager import DeckManager
from player_manager import PlayerManager


class GameManager:

    current_turn = "player"

    def __init__(self, player_name):
        self.deck_manager = DeckManager()
        self.player_manager = PlayerManager(player_name)

    def deal_initial_two_cards(self): #deal cards and return current cards and points
        player1_cards = self.deck_manager.get_cards(2)
        croupier_cards = self.deck_manager.get_cards(2)
        self.player_manager.deal_cards_to_players(player1_cards, croupier_cards)
        response = self.player_manager.get_players_status()
        return response

    def deal_extra_card(self, player):
        if player == "player":
            other_card = self.deck_manager.get_cards(1)
            self.player_manager.deal_cards_to_players(other_card, [])
            response = self.player_manager.get_players_status()
            return response
        if player == "croupier":
            other_card = self.deck_manager.get_cards(1)
            self.player_manager.deal_cards_to_players([], other_card)
            response = self.player_manager.get_players_status()
            return response

    def stand_and_change_turn(self):
        if self.player_manager.croupier.has_hidden_card:
            self.player_manager.expose_croupier_hidden_card()
            response = self.player_manager.get_players_status()
            return response
