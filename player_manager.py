from Player import Player, Croupier


class PlayerManager:

    def __init__(self, player_name):
        self.player_1 = Player(player_name)
        self.croupier = Croupier()

    def deal_cards_to_players(self, cards_to_player_1, cards_to_player_2):
        self.player_1.recive_cards(cards_to_player_1)
        self.croupier.recive_cards(cards_to_player_2)

    def get_players_status(self):
        return {
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
