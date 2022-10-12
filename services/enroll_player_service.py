
from models.player import Player
from repositories.game_pyson_repository import GamePysonRepository


class EnrollPlayerService:

    def __init__(self):
        self.game_repository = GamePysonRepository.get_instance()
        self.player_id_created = None

    def enroll_player(self, player_name, player_id, game_id):
        game = self.game_repository.get_game(game_id)
        player = Player.create(player_name, player_id)
        game.enroll_player(player)
        self.game_repository.update(game)
        return player.player_id
