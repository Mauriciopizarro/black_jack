import player_manager
from deck_manager import DeckManager
from player_manager import PlayerManager


class GameManager:

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
        self.player_manager.player_1.stand = True
        if self.player_manager.croupier.has_hidden_card:
            self.player_manager.expose_croupier_hidden_card()
            response = self.player_manager.get_players_status()
            return response

    def check_winner(self):
        croupier_points = self.player_manager.get_players_status().get("croupier").get("total_points")
        player_points = self.player_manager.get_players_status().get("player").get("total_points")

        if 21 > croupier_points > player_points:
            if self.player_manager.player_1.is_stand():
                return "croupier_wins"

        elif 21 > player_points > croupier_points:
            if self.player_manager.croupier.is_stand():
                return "player_wins"

        elif croupier_points > 21:
            return "player_wins"

        elif player_points > 21:
            return "croupier_wins"

        elif croupier_points == 21 and self.player_manager.player_1.is_stand():
            return "croupier_wins"
