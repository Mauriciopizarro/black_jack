from repositories.player_repository import PlayerRepository


class CheckGameOverService:

    def __init__(self):
        self.player_repository = PlayerRepository.get_instance()

    def check_game_over(self):
        # Add more game-over validations here
        croupier = self.player_repository.get_croupier()
        player_1 = self.player_repository.get_player()
        croupier_points = croupier.get_total_points()
        player_points = player_1.get_total_points()

        if player_points > 21:
            player_1.game_over()
            status = {
                'player': {
                    'name': player_1.name,
                    'game_over_status': player_1.is_game_over()
                },
                'croupier': {
                    'name': croupier.name,
                    'game_over_status': croupier.is_game_over()
                }
            }
            return status

        elif player_1.is_stand() and croupier_points > player_points:
            player_1.game_over()
            status = {
                'player': {
                    'name': player_1.name,
                    'game_over_status': player_1.is_game_over()
                },
                'croupier': {
                    'name': croupier.name,
                    'game_over_status': croupier.is_game_over()
                }
            }
            return status

        return None
