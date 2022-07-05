class DeckRepository:
    deck = None
    instance = None

    # Patron singleton
    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = cls()

        return cls.instance

    def save(self, deck):
        self.deck = deck

    def get(self):
        return self.deck
