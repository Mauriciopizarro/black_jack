
from models.player import Player
from repositories.game_repository import GameRepository
from services.exceptions import NotCreatedGame


class EnrollPlayerService:

    def __init__(self):
        self.game_repository = GameRepository.get_instance()
        self.player_id_created = None

    def enroll_player(self, player_name, player_id):

        game = self.game_repository.get_game()

        if not game:
            raise NotCreatedGame()

        player = Player(player_name, player_id)
        game.enroll_player(player)
        self.game_repository.save(game)
        return player.player_id
