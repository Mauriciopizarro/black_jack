class Player:

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_sum_of_cards(self):

        sum_of_cards = 0

        for card in self.cards:
            sum_of_cards += card.value
        return sum_of_cards

    def recive_card(self, card):
        self.cards.append(card)

    def get_card_names(self):
        return [card.name for card in self.cards]

class Bank(Player):

    def get_card_names(self):
        names = [card.name for card in self.cards if card != self.cards[-1]]
        names.append('hide_name')
        return names
