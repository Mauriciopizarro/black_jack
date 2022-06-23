from deck_manager import DeckManager
from player_manager import PlayerManager


class GameManager:

    def __init__(self, player_name):
        self.deck_manager = DeckManager()
        self.player_manager = PlayerManager(player_name)

    def start_game(self):
        player1_cards = self.deck_manager.get_cards(2)
        croupier_cards = self.deck_manager.get_cards(2)
        self.player_manager.deal_cards_to_players(player1_cards, croupier_cards)

        response = self.player_manager.get_players_status()
        print(f'Player {response.get("player").get("name")} cards: {response.get("player").get("cards")} puntos totales = {response.get("player").get("total_points")}')
        print(f'Player {response.get("croupier").get("name")} cards: {response.get("croupier").get("cards")} puntos totales = {response.get("croupier").get("total_points")}')

    def choise_next_step(self, selection):

        if selection == "other_card":
            other_card = self.deck_manager.get_cards(1)
            self.player_manager.deal_cards_to_players(other_card, [])
            response = self.player_manager.get_players_status()
            print(f'Player {response.get("player").get("name")} cards: {response.get("player").get("cards")} puntos totales = {response.get("player").get("total_points")}')
            print(f'Player {response.get("croupier").get("name")} cards: {response.get("croupier").get("cards")} puntos totales = {response.get("croupier").get("total_points")}')

        if selection == "stand":
            pass

    def status_game(self):
        pass
