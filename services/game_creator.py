from model.deck import Deck
from model.player import Player, Bank


class GameCreator:

    def create_game(self):
        self.deck = Deck()
        self.player = Player('Player')
        self.bank = Bank('Bank')
        self.players = [self.player, self.bank]
        for player in self.players:
            self._deal_cards_to_player(player)
        return self._get_game_info()


    def _deal_cards_to_player(self, player):
        for i in range(2):
            card = self.deck.get_card()
            player.recive_card(card)

    def _get_game_info(self):
        return {
            'players': [
                {
                    'name': self.player.name,
                    'cards': self.player.get_card_names(),
                },
                {
                    'name': self.bank.name,
                    'cards': self.bank.get_card_names()
                }
            ],
        }