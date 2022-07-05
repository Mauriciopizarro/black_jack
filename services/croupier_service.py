
from repositories.player_repository import PlayerRepository
from services.deal_card_service import DealCardService


class CroupierService:

    def __init__(self):
        self.player_repository = PlayerRepository.get_instance()

    def croupier_in_game(self):
        croupier_total_points = self.player_repository.get_croupier().get_total_points()
        if croupier_total_points < 21:
            return True
        return False

    def expose_hidden_card(self):
        croupier = self.player_repository.get_croupier()
        croupier.has_hidden_card = False

    @staticmethod
    def croupier_play():
        deal_card_service = DealCardService()
        deal_card_service.deal_card()
