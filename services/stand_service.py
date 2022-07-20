from repositories.player_repository import PlayerRepository
from repositories.game_repository import GameRepository
from services.exceptions import NotCreatedGame, GameFinishedError


class StandService:

    def __init__(self):
        self.player_repository = PlayerRepository.get_instance()
        self.game_repository = GameRepository.get_instance()

    def stand(self):
        game = self.game_repository.get()
        players = self.player_repository.get_players()
        croupier = self.player_repository.get_croupier()

        if not game:
            raise NotCreatedGame()

        if game.is_finished():
            raise GameFinishedError()

        if game.is_croupier_turn():
            raise NoTurnsToStand()

        for player in players:
            if str(player.player_id) == game.get_playerId_of_current_turn():
                player.stand()
                player.set_as_waiting_croupier()
                game.change_turn()
                break

        for player in players:
            if str(player.player_id) == game.get_playerId_of_current_turn():
                player.set_as_playing()

        if game.is_croupier_turn():
            croupier.set_as_playing()


class NoTurnsToStand(Exception):
    pass
