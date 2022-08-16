from repositories.player_repository import PlayerRepository
from repositories.game_repository import GameRepository
from services.exceptions import NotCreatedGame, GameFinishedError


class StandService:

    def __init__(self):
        self.player_repository = PlayerRepository.get_instance()
        self.game_repository = GameRepository.get_instance()

    def stand(self, player_id):
        game = self.game_repository.get_game()
        player = self.player_repository.get_by_id(player_id)

        if not game:
            raise NotCreatedGame()

        if game.is_finished():
            raise GameFinishedError()

        if not player:
            raise EmptyPlayerID()

        if not game.get_playerId_of_current_turn() == str(player.player_id):
            raise IncorrectPlayerTurn()

        player.stand()
        player.set_as_waiting_croupier()
        game.change_turn()


class NoTurnsToStand(Exception):
    pass


class EmptyPlayerID(Exception):
    pass


class IncorrectPlayerTurn(Exception):
    pass

