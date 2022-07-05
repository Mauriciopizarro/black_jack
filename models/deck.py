import random
from models.card import Card


class Deck:
    def __init__(self):
        self.cards = [
            Card(11), #As
            Card(11), #As
            Card(1),  #As
            Card(1),  #As
            Card(10), #J
            Card(10), #J
            Card(10), #J
            Card(10), #J
            Card(10), #Q
            Card(10), #Q
            Card(10), #Q
            Card(10), #Q
            Card(10), #K
            Card(10), #K
            Card(10), #K
            Card(10), #K
            Card(2),
            Card(2),
            Card(2),
            Card(2),
            Card(3),
            Card(3),
            Card(3),
            Card(3),
            Card(4),
            Card(4),
            Card(4),
            Card(4),
            Card(5),
            Card(5),
            Card(5),
            Card(5),
            Card(6),
            Card(6),
            Card(6),
            Card(6),
            Card(7),
            Card(7),
            Card(7),
            Card(7),
            Card(8),
            Card(8),
            Card(8),
            Card(8),
            Card(9),
            Card(9),
            Card(9),
            Card(9),
            Card(10),
            Card(10),
            Card(10),
            Card(10),
        ]

        random.shuffle(self.cards)

    def get_cards(self, cards_to_return):
        cards = []
        for i in range(cards_to_return):
            card = self.cards.pop()
            cards.append(card)

        return cards
