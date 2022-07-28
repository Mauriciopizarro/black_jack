class PlayerRepository:

    players = []
    croupier = None
    instance = None

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = cls()
        return cls.instance

    def save_players(self, player):
        self.players.append(player)

    def save_croupier(self, croupier):
        self.croupier = croupier

    def get_players(self):
        return self.players

    def get_croupier(self):
        return self.croupier

