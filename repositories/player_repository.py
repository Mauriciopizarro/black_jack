class PlayerRepository:

    player = None
    croupier = None
    instance = None

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = cls()
        return cls.instance

    def save_player(self, player):
        self.player = player

    def save_croupier(self, croupier):
        self.croupier = croupier

    def get_player(self):
        return self.player

    def get_croupier(self):
        return self.croupier

