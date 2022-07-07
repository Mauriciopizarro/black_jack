from models.card import As


class Player:

    def __init__(self, name):
        self.cards = []
        self.name = name
        self.__stand = False
        self.__is_winner = False
        self.__is_looser = False

    def recive_cards(self, new_cards):
        self.cards.extend(new_cards)

    def get_cards_symbols(self):
        return [card.symbol for card in self.cards]

    def get_total_points(self):
        total_point_list = self.get_possible_points()
        return max(total_point_list)

    def get_possible_points(self):
        total_points = 0
        total_points_list = []
        there_is_as = False
        for card in self.cards:
            if isinstance(card, As):
                there_is_as = True
            total_points += card.value
        total_points_list.append(total_points)

        total_points_with_as = total_points + As.special_value
        if there_is_as and total_points_with_as <= 21:
            total_points_list.append(total_points_with_as)

        if 21 in total_points_list:
            total_points_list = [21]

        return total_points_list

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
            'cards': self.get_cards_symbols(),
            'total_points': self.get_possible_points(),
            'status': status,
            'is_stand': self.is_stand()
        }


class Croupier(Player):
    def __init__(self, *args):
        super(Croupier, self).__init__('Croupier')
        self.has_hidden_card = True

    def get_cards_symbols(self):
        cards_values = super(Croupier, self).get_cards_symbols()
        if self.has_hidden_card:
            cards_values[1] = 'hidden card'

        return cards_values

    def get_possible_points(self):
        if not self.has_hidden_card:
            return super(Croupier, self).get_possible_points()

        if isinstance(self.cards[0], As):
            return [self.cards[0].value, self.cards[0].value + As.special_value]

        return [self.cards[0].value]
