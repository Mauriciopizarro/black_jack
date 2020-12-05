import random

from model.card import CardTwo, CardThree, CardFour, CardFive, CardSix, CardSeven, CardEight, CardNine, CardJ, CardQ, \
    CardK, CardAce


class Deck:

    def __init__(self):
        self.cards = []
        self.create_deck()
        self.suffle()

    def create_deck(self):
        for i in range(4):
            self.cards.append(CardTwo())
            self.cards.append(CardThree())
            self.cards.append(CardFour())
            self.cards.append(CardFive())
            self.cards.append(CardSix())
            self.cards.append(CardSeven())
            self.cards.append(CardEight())
            self.cards.append(CardNine())
            self.cards.append(CardJ())
            self.cards.append(CardQ())
            self.cards.append(CardK())
            self.cards.append(CardAce())

    def suffle(self):
        random.shuffle(self.cards)

    def get_card(self):
        return self.cards.pop()