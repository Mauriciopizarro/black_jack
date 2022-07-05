
from services.deal_card_service import DealCardService


class PlayerService:

    def __init__(self):
        self.deal_card_service = DealCardService()

    def player_play(self):
        self.deal_card_service.deal_card()
