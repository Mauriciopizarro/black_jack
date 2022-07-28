
from repositories.game_repository import GameRepository
from repositories.player_repository import PlayerRepository
from services.exceptions import NotCreatedGame


class StatusService:

    def __init__(self):
        self.player_repository = PlayerRepository.get_instance()
        self.game_repository = GameRepository.get_instance()

    def players_status(self):
        list_players = self.player_repository.get_players()
        croupier = self.player_repository.get_croupier()
        game = self.game_repository.get_game()
        players_status_list = []

        if not game:
            raise NotCreatedGame()

        for player in list_players:
            players_status_list.append(player.get_status())

        player_status_json = {
            'players_quantity': game.quantity_players,
            'status_game': game.game_status,
            'players': players_status_list,
            'croupier': croupier.get_status()
        }
        return player_status_json
