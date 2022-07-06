
class Player:

    def __init__(self, name):
        self.cards = []
        self.name = name
        self.__stand = False
        self.__is_winner = False
        self.__is_looser = False

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
        return self.__stand

    def stand(self):
        self.__stand = True

    def set_as_winner(self):
        self.__is_winner = True

    def set_as_looser(self):
        self.__is_looser = True

    def is_over_limit(self):
        points = self.get_total_points()
        if points > 21:
            return True
        return False

    def get_status(self):
        status = 'playing'
        if self.__is_looser:
            status = 'looser'
        if self.__is_winner:
            status = 'winner'

        return {
            'name': self.name,
            'cards': self.get_cards_values(),
            'total_points': self.get_total_points(),
            'status': status,
            'is_stand': self.is_stand()
        }


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
