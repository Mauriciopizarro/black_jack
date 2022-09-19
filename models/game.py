class Game:

    def __init__(self, croupier, deck):
        self.turn_order = []
        self.deck = deck
        self.croupier = croupier
        self.game_status = "created"
        self.players = []
        self.turn_position = 0

    def change_turn(self):
        self.turn_position += 1
        player = self.turn_order[self.turn_position]
        player.set_as_playing()

    def enroll_player(self, player):
        list_of_ids = [str(saved_player.player_id) for saved_player in self.players]

        if str(player.player_id) in list_of_ids:
            raise AlreadyEnrolledPlayer()

        if len(self.players) >= 3:
            raise IncorrectPlayersQuantity()

        self.players.append(player)
        self.turn_order.append(player)

    def all_players_over_the_limit(self):
        for player in self.players:
            if not player.is_over_21_points():
                return False
        return True

    def get_playerId_of_current_turn(self):
        player = self.turn_order[self.turn_position]
        return str(player.player_id)

    def is_finished(self):
        return self.game_status == "finished"

    def start(self):
        if len(self.players) == 0:
            raise NotPlayersCreated()

        if self.game_status == "started":
            raise GameAlreadyStarted()

        if self.game_status == "finished":
            raise GameNeedToBeRestarted()

        for player in self.players:
            player.receive_cards(self.deck.get_cards(2))

        self.croupier.receive_cards(self.deck.get_cards(2))
        self.turn_order.append(self.croupier)
        self.game_status = "started"
        self.turn_order[0].set_as_playing()

    def is_player_turn(self, player_id):
        return str(player_id) == self.get_playerId_of_current_turn()

    def deal_card_to_current_turn_player(self):
        player = self.turn_order[self.turn_position]
        player.receive_cards(self.deck.get_cards(1))

        if player.is_over_limit():
            player.set_as_looser()
            self.change_turn()

        if self.all_players_over_the_limit():
            self.croupier.set_as_winner()
            self.game_status = "finished"

    def stand_current_turn_player(self):
        player = self.turn_order[self.turn_position]
        player.stand()
        player.set_as_waiting_croupier()
        self.change_turn()

    def is_there_winner(self):

        croupier_points = self.croupier.get_total_points()
        need_another_card = False

        if self.all_players_over_the_limit():
            self.croupier.set_as_winner()
            self.game_status = "finished"
            return True

        if self.croupier.is_over_limit():
            for player in self.players:
                if player.get_total_points() <= 21:
                    player.set_as_winner()
            self.croupier.set_as_looser()
            self.game_status = "finished"
            return True

        if croupier_points > 16:
            for player in self.players:
                if player.get_total_points() > croupier_points and not player.is_over_limit():
                    need_another_card = True
            if not need_another_card:
                self.croupier.set_as_winner()
                for player in self.players:
                    if player.get_total_points() == croupier_points:
                        player.set_as_winner()
                    player.set_as_looser()
                self.game_status = "finished"
                return True

        return False

    def croupier_play(self):
        if self.game_status != "started":
            raise NotStartedGame()
        current_player_id = self.get_playerId_of_current_turn()
        if not current_player_id == str(self.croupier.player_id):
            raise NotCroupierTurnError()

        self.croupier.has_hidden_card = False
        while not self.is_there_winner():
            self.croupier.receive_cards(self.deck.get_cards(1))

    def get_status(self):
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


class NotPlayersCreated(Exception):
    pass


class GameAlreadyStarted(Exception):
    pass


class GameNeedToBeRestarted(Exception):
    pass


class AlreadyEnrolledPlayer(Exception):
    pass
