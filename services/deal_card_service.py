from repositories.deck_repository import DeckRepository
from repositories.game_repository import GameRepository
from repositories.player_repository import PlayerRepository
from services.exceptions import NotCreatedGame, GameFinishedError


class DealCardService:

    def __init__(self):
        self.deck_repository = DeckRepository.get_instance()
        self.player_repository = PlayerRepository.get_instance()
        self.game_repository = GameRepository.get_instance()

    def deal_card(self, player_id):
        player = self.player_repository.get_by_id(player_id)
        game = self.game_repository.get_game()

        if not player:
            raise EmptyPlayerID()

        if not game:
            raise NotCreatedGame()

        if game.is_finished():
            raise GameFinishedError()

        if game.is_croupier_turn():
            raise CroupierTurn()

        if not game.get_playerId_of_current_turn() == str(player.player_id):
            raise IncorrectPlayerTurn()

        deck = self.deck_repository.get_deck()
        card = deck.get_cards(1)
        player.receive_cards(card)

        if player.is_over_limit():
            player.set_as_looser()
            game.change_turn()


class NotPlayerTurn(Exception):
    pass


class CroupierTurn(Exception):
    pass


class IncorrectPlayerTurn(Exception):
    pass


class EmptyPlayerID(Exception):
    pass
