class TurnRepository:
    turn = None
    instance = None

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = cls()
        return cls.instance

    def save(self, turn):
        self.turn = turn

    def get(self):
        return self.turn
