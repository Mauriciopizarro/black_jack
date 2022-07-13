from repositories.deck_repository import DeckRepository
from repositories.player_repository import PlayerRepository
from repositories.game_repository import GameRepository
from services.exceptions import NotCreatedGame


class CroupierService:

    def __init__(self):
        self.deck_repository = DeckRepository.get_instance()
        self.player_repository = PlayerRepository.get_instance()
        self.game_repository = GameRepository.get_instance()

    def is_there_winner(self, croupier, player_1):

        player_points = player_1.get_total_points()
        croupier_points = croupier.get_total_points()

        if croupier.is_over_limit():
            player_1.set_as_winner()
            croupier.set_as_looser()
            return True

        if croupier_points == player_points:
            player_1.set_as_winner()
            croupier.set_as_winner()
            return True

        if croupier_points > player_points:
            croupier.set_as_winner()
            player_1.set_as_looser()
            return True

        return False

    def croupier_play(self):
        player_1 = self.player_repository.get_player()
        croupier = self.player_repository.get_croupier()
        game = self.game_repository.get()

        if not game:
            raise NotCreatedGame()

        if not player_1.is_stand() or game.get_current_turn() != 'croupier':
            raise NotCroupierTurnError()

        if croupier.get_status().get('status') != 'playing':
            raise CroupierCantPlayFinishedGameError()

        croupier.has_hidden_card = False
        while not self.is_there_winner(croupier, player_1):
            deck = self.deck_repository.get()
            card = deck.get_cards(1)
            croupier.recive_cards(card)


class NotCroupierTurnError(Exception):
    pass


class CroupierCantPlayFinishedGameError(Exception):
    pass
