import random

from Card import Card


class DeckManager:

    def __init__(self):
        self.deck = [
            Card(11),
            Card(11),
            Card(1),
            Card(1),
            Card(10),
            Card(10),
            Card(10),
            Card(10),
            Card(10),
            Card(10),
            Card(2),
            Card(2),
            Card(3),
            Card(3),
            Card(4),
            Card(4),
            Card(5),
            Card(5),
            Card(6),
            Card(6),
            Card(7),
            Card(7),
            Card(8),
            Card(8),
            Card(9),
            Card(9),
        ]

        random.shuffle(self.deck)

    def get_cards(self, cards_to_return):
        cards = []
        for i in range(cards_to_return):
            card = self.deck.pop()
            cards.append(card)

        return cards
