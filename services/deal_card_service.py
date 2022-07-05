from repositories.deck_repository import DeckRepository
from repositories.player_repository import PlayerRepository
from repositories.turn_repository import TurnRepository


class DealCardService:

    def __init__(self):
        self.deck_repository = DeckRepository.get_instance()
        self.player_repository = PlayerRepository.get_instance()
        self.turn_repository = TurnRepository.get_instance()

    def deal_card(self):
        turn = self.turn_repository.get()
        deck = self.deck_repository.get()
        card = deck.get_cards(1)

        if turn.get_current_turn() == "player":
            player_1 = self.player_repository.get_player()
            player_1.recive_cards(card)
        else:
            croupier = self.player_repository.get_croupier()
            croupier.recive_cards(card)
