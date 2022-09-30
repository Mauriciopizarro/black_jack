from repositories.game_repository import GameRepository
from services.exceptions import NotCreatedGame


class StandService:

    def __init__(self):
        self.game_repository = GameRepository.get_instance()

    def stand(self, player_id):
        game = self.game_repository.get_game()

        if not game:
            raise NotCreatedGame()

        if not player_id:
            raise EmptyPlayerID()

        game.stand_current_turn_player(player_id)


class EmptyPlayerID(Exception):
    pass

