
class Player:

    def __init__(self, name):
        self.cards = []
        self.stand = False
        self.name = name

    def recive_cards(self, new_cards):
        self.cards.extend(new_cards)

    def get_cards_values(self):
        return [card.value for card in self.cards]

    def get_total_points(self):
        total_points = 0

        for card in self.cards:
            total_points += card.value

        return total_points

    def is_stand(self):
        return self.stand


class Croupier(Player):
    def __init__(self, *args):
        super(Croupier, self).__init__('Croupier')
        self.has_hidden_card = True

    def get_cards_values(self):
        cards_values = super(Croupier, self).get_cards_values()
        if self.has_hidden_card:
            cards_values[1] = 'hidden card'

        return cards_values
    
    def get_total_points(self):
        total_points = super(Croupier, self).get_total_points()
        if self.has_hidden_card:
            total_points -= self.cards[1].value

        return total_points
