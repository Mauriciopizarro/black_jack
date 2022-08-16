class Game:

    def __init__(self, list_of_players, croupier):
        self.turn_order = []
        self.list_of_players = list_of_players
        for player in list_of_players:
            self.turn_order.append(player)
        self.croupier = croupier
        self.turn_order.append(croupier)
        self.turn_position = 0
        self.quantity_players = 1
        self.game_status = "to_start"

    def change_turn(self):
        self.turn_position += 1
        player = self.turn_order[self.turn_position]
        player.set_as_playing()

    def set_started_game_status(self):
        self.game_status = "started"

    def empty_game(self, list_of_players, croupier):
        self.__init__(list_of_players, croupier)
        for player in list_of_players:
            player.clear_status()
        croupier.clear_status()

    def is_croupier_turn(self):
        if self.get_playerId_of_current_turn() == str(self.croupier.player_id):
            return True
        return False

    def all_players_over_the_limit(self):
        players_over_the_limit = 0
        for player in self.list_of_players:
            if player.get_total_points() > 21:
                players_over_the_limit += 1
        if players_over_the_limit == self.quantity_players:
            return True
        return False

    def get_playerId_of_current_turn(self):
        player = self.turn_order[self.turn_position]
        return str(player.player_id)

    def set_num_players(self, num_players):
        self.quantity_players = num_players

    def end_game(self):
        self.game_status = "finished"

    def get_game_status(self):
        return self.game_status

    def is_finished(self):
        return self.game_status == "finished"
