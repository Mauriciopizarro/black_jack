from repositories.deck_repository import DeckRepository
from repositories.player_repository import PlayerRepository


class DealCardService:

    def __init__(self):
        self.deck_repository = DeckRepository.get_instance()
        self.player_repository = PlayerRepository.get_instance()

    def deal_card(self):
        player_1 = self.player_repository.get_player()
        player_status = player_1.get_status().get('status')
        if player_1.is_stand():
            raise StandPlayerCantReciveCardsError()
        if player_status == 'looser':
            raise PlayerOverLimitDealCardError()
        deck = self.deck_repository.get()
        card = deck.get_cards(1)
        player_1.recive_cards(card)
        if player_1.is_over_limit():
            croupier = self.player_repository.get_croupier()
            croupier.set_as_winner()
            player_1.set_as_looser()


class StandPlayerCantReciveCardsError(Exception):
    pass


class PlayerOverLimitDealCardError(Exception):
    pass
