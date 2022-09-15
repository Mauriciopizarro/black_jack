from models.game import NotStartedGame
from repositories.game_repository import GameRepository
from services.exceptions import NotCreatedGame, GameFinishedError


class DealCardService:

    def __init__(self):
        self.game_repository = GameRepository.get_instance()

    def deal_card(self, player_id):
        game = self.game_repository.get_game()

        if not player_id:
            raise EmptyPlayerID()

        if not game:
            raise NotCreatedGame()

        if game.game_status != "started":
            raise NotStartedGame()

        if game.is_finished():
            raise GameFinishedError()

        if game.is_croupier_turn():
            raise CroupierTurn()

        if not game.is_player_turn(player_id):
            raise IncorrectPlayerTurn()

        game.deal_card_to_current_turn_player()


class NotPlayerTurn(Exception):
    pass


class CroupierTurn(Exception):
    pass


class IncorrectPlayerTurn(Exception):
    pass


class EmptyPlayerID(Exception):
    pass
