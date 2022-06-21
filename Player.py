from Card import *


class Player:

    def __init__(self, name):
        self.cards = []
        self.name = name

    def recive_cards(self, new_cards):
        self.cards.extend(new_cards)

    def get_cards_values(self):
        return [card.value for card in self.cards]


class Croupier(Player):
    def __init__(self, *args):
        super(Croupier, self).__init__('Croupier')
        self.has_hidden_card = True

    def get_cards_values(self):
        if not self.has_hidden_card:
            return [str(card.value) for card in self.cards]

        card_values = []

        for card in self.cards:
            card_values.append(str(card.value))

        card_values[1] = 'hidden card'

        return card_values
