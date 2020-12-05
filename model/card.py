class Card:

    def __init__(self, value, name):
        self.value = value
        self.name = name

class CardTwo(Card):
    def __init__(self):
        self.value = 2
        self.name = 'Two'

class CardThree(Card):
    def __init__(self):
        self.value = 3
        self.name = 'Three'

class CardFour(Card):
    def __init__(self):
        self.value = 4
        self.name = 'Four'

class CardFive(Card):
    def __init__(self):
        self.value = 5
        self.name = 'Five'

class CardSix(Card):
    def __init__(self):
        self.value = 6
        self.name = 'Six'

class CardSeven(Card):
    def __init__(self):
        self.value = 7
        self.name = 'Seven'

class CardEight(Card):
    def __init__(self):
        self.value = 8
        self.name = 'Eight'

class CardNine(Card):
    def __init__(self):
        self.value = 9
        self.name = 'Nine'

class CardTen(Card):
    def __init__(self):
        self.value = 10
        self.name = 'Ten'

class CardJ(Card):
    def __init__(self):
        self.value = 10
        self.name = 'J'

class CardQ(Card):
    def __init__(self):
        self.value = 10
        self.name = 'Q'

class CardK(Card):
    def __init__(self):
        self.value = 10
        self.name = 'K'

class CardAce(Card):
    def __init__(self):
        self.value = 11
        self.special_value = 1
        self.name = 'A'