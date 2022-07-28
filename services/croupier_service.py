
from repositories.deck_repository import DeckRepository
from repositories.player_repository import PlayerRepository
from repositories.game_repository import GameRepository
from services.exceptions import NotCreatedGame, GameFinishedError


def is_there_winner(croupier, players, game):

    croupier_points = croupier.get_total_points()
    need_another_card = False

    if game.all_players_over_the_limit():
        croupier.set_as_winner()
        game.end_game()
        return True

    if croupier.is_over_limit():
        for player in players:
            if player.get_total_points() <= 21:
                player.set_as_winner()
        croupier.set_as_looser()
        game.end_game()
        return True

    if croupier_points > 16:
        for player in players:
            if player.get_total_points() > croupier_points and not player.is_over_limit():
                need_another_card = True
        if not need_another_card:
            croupier.set_as_winner()
            for player in players:
                if player.get_total_points() == croupier_points:
                    player.set_as_winner()
                player.set_as_looser()
            game.end_game()
            return True

    return False


class CroupierService:

    def __init__(self):
        self.deck_repository = DeckRepository.get_instance()
        self.player_repository = PlayerRepository.get_instance()
        self.game_repository = GameRepository.get_instance()

    def croupier_play(self):
        players = self.player_repository.get_players()
        croupier = self.player_repository.get_croupier()
        game = self.game_repository.get_game()

        if not game:
            raise NotCreatedGame()

        if game.is_finished():
            raise GameFinishedError()

        if not game.get_playerId_of_current_turn() == str(croupier.player_id):
            raise NotCroupierTurnError()

        croupier.has_hidden_card = False
        while not is_there_winner(croupier, players, game):
            deck = self.deck_repository.get_deck()
            card = deck.get_cards(1)
            croupier.receive_cards(card)


class NotCroupierTurnError(Exception):
    pass
