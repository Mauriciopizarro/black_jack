from repositories.deck_repository import DeckRepository
from repositories.player_repository import PlayerRepository


class CroupierService:

    def __init__(self):
        self.deck_repository = DeckRepository.get_instance()
        self.player_repository = PlayerRepository.get_instance()

    def check_croupier_game_over(self, croupier):
        player_1 = self.player_repository.get_player()
        player_points = player_1.get_total_points()
        croupier_points = croupier.get_total_points()
        if croupier_points > 21:
            croupier.game_over()
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

    def croupier_play(self):
        croupier = self.player_repository.get_croupier()
        croupier.has_hidden_card = False
        status = self.check_croupier_game_over(croupier)
        if status is not None:
            return status
        while croupier.get_total_points() < 21:
            deck = self.deck_repository.get()
            card = deck.get_cards(1)
            croupier.recive_cards(card)
            status = self.check_croupier_game_over(croupier)
            if status is not None:
                return status
