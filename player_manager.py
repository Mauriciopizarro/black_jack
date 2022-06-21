from Player import Player, Croupier


class PlayerManager:

    def __init__(self, player_name):
        self.player_1 = Player(player_name)
        self.croupier = Croupier()

    def deal_cards_to_players(self, cards_to_player_1, cards_to_player_2):
        self.player_1.recive_cards(cards_to_player_1)
        self.croupier.recive_cards(cards_to_player_2)

    def get_current_cards(self):
        return {
            'player': self.player_1.get_cards_values(),
            'croupier': self.croupier.get_cards_values(),
        }
