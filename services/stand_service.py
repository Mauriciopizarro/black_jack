from repositories.player_repository import PlayerRepository
from repositories.turn_repository import TurnRepository


class StandService:

    def __init__(self):
        self.player_repository = PlayerRepository.get_instance()
        self.turn_repository = TurnRepository.get_instance()

    def stand(self):
        turn = self.turn_repository.get()
        numbers_of_players = turn.get_number_of_players()
        turn_position = turn.get_turn_position()
        if turn_position >= numbers_of_players:
            raise NoTurnsToStand()
        current_turn = turn.get_current_turn()
        if current_turn == 'player':
            player_1 = self.player_repository.get_player()
            player_1.stand()
        turn.change_turn()


class NoTurnsToStand(Exception):
    pass
