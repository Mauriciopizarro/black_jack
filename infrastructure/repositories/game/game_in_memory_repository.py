from domain.interfaces.game_repository import GameRepository


class GameInMemoryRepository(GameRepository):
    game = None
    instance = None

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = cls()
        return cls.instance

    def save(self, game):
        self.game = game

    def get(self, game_id):
        return self.game

    def update(self, game):
        return self.game
