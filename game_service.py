
from Player import Player, Croupier
from deck import Deck
from deck_repository import DeckRepository


class GameService:
    turn_order = ['player', 'croupier']
    turn_position = 0

    def __init__(self):
        self.deck_repository = DeckRepository.get_instance()
        self.player_1 = None
        self.croupier = Croupier()

    def deal_initial_cards_to_players(self, cards_to_player_1, cards_to_player_2):
        self.player_1.recive_cards(cards_to_player_1)
        self.croupier.recive_cards(cards_to_player_2)

    def start_game(self, player_name): #deal cards and return current cards and points
        deck = Deck()
        self.deck_repository.save(deck)
        self.player_1 = Player(player_name)
        player1_cards = deck.get_cards(2)
        croupier_cards = deck.get_cards(2)
        self.deal_initial_cards_to_players(player1_cards, croupier_cards)

    def deal_card(self):
        player_name = self.turn_order[self.turn_position]
        deck = self.deck_repository.get()
        card = deck.get_cards(1)
        if player_name == 'player':
            self.player_1.recive_cards(card)
        else:
            self.croupier.recive_cards(card)

    def stand(self):
        player_name = self.turn_order[self.turn_position]
        if player_name == 'player':
            self.player_1.stand()
        self.turn_position += 1

    def get_players_status(self):
        player_status_json = {
            'player': {
                'name': self.player_1.name,
                'cards': self.player_1.get_cards_values(),
                'total_points': self.player_1.get_total_points()
            },
            'croupier': {
                'name': self.croupier.name,
                'cards': self.croupier.get_cards_values(),
                'total_points': self.croupier.get_total_points()
            }
        }
        return player_status_json

    def check_game_over(self):
        # Add more game-over validations here
        croupier_points = self.get_players_status().get("croupier").get("total_points")
        player_points = self.get_players_status().get("player").get("total_points")

        if croupier_points > 21:
            self.croupier.game_over()
            status = {
                'player': {
                    'name': self.player_1.name,
                    'game_over_status': self.player_1.is_game_over()
                },
                'croupier': {
                    'name': self.croupier.name,
                    'game_over_status': self.croupier.is_game_over()
                }
            }
            return status

        elif player_points > 21:
            self.player_1.game_over()
            status = {
                'player': {
                    'name': self.player_1.name,
                    'game_over_status': self.player_1.is_game_over()
                },
                'croupier': {
                    'name': self.croupier.name,
                    'game_over_status': self.croupier.is_game_over()
                }
            }
            return status

        elif self.player_1.is_stand() and croupier_points > player_points:
            self.player_1.game_over()
            status = {
                'player': {
                    'name': self.player_1.name,
                    'game_over_status': self.player_1.is_game_over()
                },
                'croupier': {
                    'name': self.croupier.name,
                    'game_over_status': self.croupier.is_game_over()
                }
            }
            return status

        return None

    def croupier_play(self):
        self.croupier.has_hidden_card = False
        status = self.check_game_over()
        if status is not None:
            return status
        while self.get_players_status().get("croupier").get("total_points") < 21:
            self.deal_card()
            status = self.check_game_over()
            if status is not None:
                return status
