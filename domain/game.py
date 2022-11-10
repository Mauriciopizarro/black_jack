from domain.card import Card
from domain.player import Player
from application.exceptions import GameFinishedError
from typing import Optional, List
from pydantic import BaseModel


class Game(BaseModel):
    turn_order: List[Player]
    deck: List[Card]
    game_status: str
    turn_position: int
    game_id: Optional[str] = None

    @property
    def players(self):
        if len(self.turn_order) == 1:
            return []
        return self.turn_order[:-1]

    @property
    def croupier(self):
        return self.turn_order[-1]

    def dict(self, *arg, **kwargs):
        game_dict = super(Game, self).dict()
        game_dict.pop("game_id")
        return game_dict

    def get_cards(self, quantity_cards):
        cards = []
        for i in range(quantity_cards):
            card = self.deck.pop()
            cards.append(card)

        return cards

    def change_turn(self):
        self.turn_position += 1
        player = self.turn_order[self.turn_position]
        player.set_as_playing()

    def enroll_player(self, player):
        if self.game_status == "finished":
            raise GameFinishedError()
        if self.game_status != "created":
            raise CantEnrollPlayersStartedGame()

        list_of_ids = [str(saved_player.player_id) for saved_player in self.players]

        if str(player.player_id) in list_of_ids:
            raise AlreadyEnrolledPlayer()

        if len(self.players) >= 3:
            raise IncorrectPlayersQuantity()

        self.turn_order.insert(0, player)

    def all_players_over_the_limit(self):
        for player in self.players:
            if not player.is_over_21_points():
                return False

        self.croupier.set_as_winner()
        self.game_status = "finished"
        return True

    def check_croupier_victory(self):
        if self.all_players_over_the_limit():
            return True

        croupier_points = self.croupier.get_total_points()
        if croupier_points < 17:
            return False # The croupier can not stand with less than 17

        for player in self.players:
            if player.get_total_points() > croupier_points and not player.is_over_limit():
                return False

        self.croupier.set_as_winner()
        for player in self.players:
            if player.get_total_points() == croupier_points:
                player.set_as_winner()
                continue
            player.set_as_looser()
        self.game_status = "finished"
        return True

    def check_croupier_defeat(self):
        if self.croupier.is_over_limit():
            for player in self.players:
                if player.get_total_points() <= 21:
                    player.set_as_winner()
            self.croupier.set_as_looser()
            self.game_status = "finished"
            return True

        return False

    def get_playerId_of_current_turn(self):
        player = self.turn_order[self.turn_position]
        return str(player.player_id)

    def start(self):
        if self.game_status == "finished":
            raise GameFinishedError()

        if len(self.players) == 0:
            raise NoPlayersEnrolled()

        if self.game_status == "started":
            raise GameAlreadyStarted()

        for player in self.turn_order:
            player.receive_cards(self.get_cards(2))

        self.game_status = "started"
        self.turn_order[0].set_as_playing()

    def is_player_turn(self, player_id):
        return str(player_id) == self.get_playerId_of_current_turn()

    def deal_card_to_current_turn_player(self, player_id):

        if self.game_status == "finished":
            raise GameFinishedError()

        if self.game_status != "started":
            raise NotStartedGame()

        if not self.is_player_turn(player_id):
            raise IncorrectPlayerTurn()

        player = self.turn_order[self.turn_position]
        player.receive_cards(self.get_cards(1))

        if player.is_over_limit():
            player.set_as_looser()
            self.change_turn()

        self.all_players_over_the_limit()

    def stand_current_turn_player(self, player_id):
        if self.game_status == "finished":
            raise GameFinishedError()

        if self.game_status != "started":
            raise NotStartedGame()

        if not self.is_player_turn(player_id):
            raise IncorrectPlayerTurn()

        player = self.turn_order[self.turn_position]
        player.stand()
        self.change_turn()

    def is_there_winner(self):
        if self.check_croupier_defeat():
            return True

        if self.check_croupier_victory():
            return True

        return False

    def croupier_play(self):
        if self.game_status == "finished":
            raise GameFinishedError()
        if self.game_status != "started":
            raise NotStartedGame()
        current_player_id = self.get_playerId_of_current_turn()
        if not current_player_id == str(self.croupier.player_id):
            raise NotCroupierTurnError()

        self.croupier.has_hidden_card = False
        while not self.is_there_winner():
            self.croupier.receive_cards(self.get_cards(1))

    def get_status(self):
        if self.game_status == "created":
            raise NotStartedGame()
        players_status_list = []
        for player in self.players:
            players_status_list.append(player.get_status())

        player_status_json = {
            'players_quantity': len(self.players),
            'status_game': self.game_status,
            'players': players_status_list,
            'croupier': self.croupier.get_status()
        }
        return player_status_json


class NotStartedGame(Exception):
    pass


class IncorrectPlayersQuantity(Exception):
    pass


class NotCroupierTurnError(Exception):
    pass


class NoPlayersEnrolled(Exception):
    pass


class GameAlreadyStarted(Exception):
    pass


class AlreadyEnrolledPlayer(Exception):
    pass


class IncorrectPlayerTurn(Exception):
    pass


class CantEnrollPlayersStartedGame(Exception):
    pass
