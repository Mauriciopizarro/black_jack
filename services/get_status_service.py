from repositories.player_repository import PlayerRepository


class GetStatusService:

    def __init__(self):
        self.player_repository = PlayerRepository.get_instance()

    def get_players_status(self):
        tied_game = False
        player_1 = self.player_repository.get_player()
        croupier = self.player_repository.get_croupier()
        croupier_points = croupier.get_total_points()
        player_points = player_1.get_total_points()

        if player_points > 21:
            player_1.game_over()

        elif croupier_points > 21:
            croupier.game_over()

        elif player_1.is_stand() and croupier_points > player_points:
            player_1.game_over()

        elif 16 < player_points == croupier_points > 16:
            tied_game = True

        player_status_json = {
            'player': {
                'name': player_1.name,
                'cards': player_1.get_cards_values(),
                'total_points': player_points,
                'is_game_over': player_1.is_game_over(),
                'is_tied_game': tied_game
            },
            'croupier': {
                'name': croupier.name,
                'cards': croupier.get_cards_values(),
                'total_points': croupier_points,
                'is_game_over': croupier.is_game_over(),
                'is_tied_game': tied_game
            }
        }
        return player_status_json
