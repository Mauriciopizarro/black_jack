from pydantic import BaseModel
from typing import Optional, List
from game_management_service.domain.exceptions import CantEnrollPlayersStartedGame, AlreadyEnrolledPlayer, \
    IncorrectAdminId, GameAlreadyStarted
from game_management_service.domain.player import Player


class Game(BaseModel):
    id: Optional[str] = None
    status: str
    admin: Player
    players: List[Player]

    def enroll_player(self, player):
        if self.status != "created":
            raise CantEnrollPlayersStartedGame()

        list_of_ids = [str(saved_player.user_id) for saved_player in self.players]

        if str(player.user_id) in list_of_ids:
            raise AlreadyEnrolledPlayer()

        self.players.append(player)

    def start(self, user_id):

        if self.admin.user_id != user_id:
            raise IncorrectAdminId()

        if self.status == "started":
            raise GameAlreadyStarted()

        self.status = "started"

    def dict(self, *arg, **kwargs):
        game_dict = super(Game, self).dict()
        if not self.id:
            game_dict.pop("id")
        return game_dict
