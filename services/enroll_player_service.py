
from models.player import Player
from repositories.game_repository import GameRepository
from repositories.player_repository import PlayerRepository


class EnrollPlayerService:

    def __init__(self):
        self.player_repository = PlayerRepository.get_instance()
        self.game_repository = GameRepository.get_instance()
        self.player_id_created = None

    def enroll_player(self, player_name):
        list_of_players = self.player_repository.get_players()

        if len(list_of_players) >= 3:
            raise IncorrectPlayersQuantity()

        game = self.game_repository.get_game()

        if game is not None:
            if game.game_status == "started":
                raise CantEnrollPlayersStartedGame()

        player = Player(player_name)
        self.player_repository.save_players(player)
        self.player_id_created = player.player_id

    def get_player_id_created(self):
        return self.player_id_created


class IncorrectPlayersQuantity(Exception):
    pass


class CantEnrollPlayersStartedGame(Exception):
    pass
