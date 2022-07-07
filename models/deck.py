import random
from models.card import Card, As, LetterCard, NumberCard


class Deck:
    def __init__(self):
        self.cards = [
            As(), #As
            As(), #As
            As(),  #As
            As(),  #As
            LetterCard('J'), #J
            LetterCard('J'), #J
            LetterCard('J'), #J
            LetterCard('J'), #J
            LetterCard('Q'), #Q
            LetterCard('Q'), #Q
            LetterCard('Q'), #Q
            LetterCard('Q'), #Q
            LetterCard('K'), #K
            LetterCard('K'), #K
            LetterCard('K'), #K
            LetterCard('K'), #K
            NumberCard(2),
            NumberCard(2),
            NumberCard(2),
            NumberCard(2),
            NumberCard(3),
            NumberCard(3),
            NumberCard(3),
            NumberCard(3),
            NumberCard(4),
            NumberCard(4),
            NumberCard(4),
            NumberCard(4),
            NumberCard(5),
            NumberCard(5),
            NumberCard(5),
            NumberCard(5),
            NumberCard(6),
            NumberCard(6),
            NumberCard(6),
            NumberCard(6),
            NumberCard(7),
            NumberCard(7),
            NumberCard(7),
            NumberCard(7),
            NumberCard(8),
            NumberCard(8),
            NumberCard(8),
            NumberCard(8),
            NumberCard(9),
            NumberCard(9),
            NumberCard(9),
            NumberCard(9),
            NumberCard(10),
            NumberCard(10),
            NumberCard(10),
            NumberCard(10),
        ]

        random.shuffle(self.cards)

    def get_cards(self, cards_to_return):
        cards = []
        for i in range(cards_to_return):
            card = self.cards.pop()
            cards.append(card)

        return cards
