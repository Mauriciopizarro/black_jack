from repositories.deck_repository import DeckRepository
from repositories.player_repository import PlayerRepository


class DealCardService:

    def __init__(self):
        self.deck_repository = DeckRepository.get_instance()
        self.player_repository = PlayerRepository.get_instance()

    def deal_card(self):
        deck = self.deck_repository.get()
        card = deck.get_cards(1)
        player_1 = self.player_repository.get_player()
        player_1.recive_cards(card)