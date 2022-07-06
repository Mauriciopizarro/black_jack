from repositories.player_repository import PlayerRepository


class GetStatusService:

    def __init__(self):
        self.player_repository = PlayerRepository.get_instance()

    def get_players_status(self):
        player_1 = self.player_repository.get_player()
        croupier = self.player_repository.get_croupier()
        player_status_json = {
            'player': player_1.get_status(),
            'croupier': croupier.get_status()
        }
        return player_status_json
