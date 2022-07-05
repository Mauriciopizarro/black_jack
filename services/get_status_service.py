from repositories.player_repository import PlayerRepository


class GetStatusService:

    def __init__(self):
        self.player_repository = PlayerRepository.get_instance()

    def get_players_status(self):
        player_1 = self.player_repository.get_player()
        croupier = self.player_repository.get_croupier()
        player_status_json = {
            'player': {
                'name': player_1.name,
                'cards': player_1.get_cards_values(),
                'total_points': player_1.get_total_points()
            },
            'croupier': {
                'name': croupier.name,
                'cards': croupier.get_cards_values(),
                'total_points': croupier.get_total_points()
            }
        }
        return player_status_json
