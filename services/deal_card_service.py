from repositories.deck_repository import DeckRepository
from repositories.game_repository import GameRepository
from repositories.player_repository import PlayerRepository
from services.exceptions import NotCreatedGame, GameFinishedError


class DealCardService:

    def __init__(self):
        self.deck_repository = DeckRepository.get_instance()
        self.player_repository = PlayerRepository.get_instance()
        self.game_repository = GameRepository.get_instance()

    def deal_card(self):
        players = self.player_repository.get_players()
        croupier = self.player_repository.get_croupier()
        game = self.game_repository.get_game()

        if not game:
            raise NotCreatedGame()

        if game.is_finished():
            raise GameFinishedError()

        if game.is_croupier_turn():
            raise CroupierTurn()

        deck = self.deck_repository.get_deck()
        card = deck.get_cards(1)

        for player in players:
            if str(player.player_id) == game.get_playerId_of_current_turn():
                player.receive_cards(card)
                if player.is_over_limit():
                    game.change_turn()
                    player.set_as_looser()
                    break

        for player in players:
            if str(player.player_id) == game.get_playerId_of_current_turn():
                player.set_as_playing()

        if game.is_croupier_turn():
            croupier.set_as_playing()


class NotPlayerTurn(Exception):
    pass


class CroupierTurn(Exception):
    pass
