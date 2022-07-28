class GameRepository:
    game = None
    instance = None

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = cls()
        return cls.instance

    def save(self, game):
        self.game = game

    def get_game(self):
        return self.game
