class Card:
    value = None
    symbol = None

    def to_json(self):
        return {
            "value": self.value,
            "symbol": self.symbol,
            "type": self.__class__.__name__
        }


class NumberCard(Card):
    def __init__(self, value):
        self.value = value
        self.symbol = str(value)


class LetterCard(Card):
    def __init__(self, symbol):
        self.value = 10
        self.symbol = symbol


class As(Card):
    value = 1
    special_value = 10
    symbol = 'A'
