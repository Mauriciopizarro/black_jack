class Game:

    def __init__(self, player, croupier):
        self.turn_order = [player, croupier]
        self.turn_position = 0
        self.game_status = "started"

    def change_turn(self):
        self.turn_position += 1

    def is_player_turn(self, player):
        if self.turn_order[self.turn_position] == player:
            return True
        return False

    def end_game(self):
        self.game_status = "finished"

    def is_finished(self):
        return self.game_status == "finished"
