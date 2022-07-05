class Turn:

    def __init__(self):
        self.turn_order = ['player', 'croupier']
        self.turn_position = 0

    def get_current_turn(self):
        return self.turn_order[self.turn_position]

    def change_turn(self):
        self.turn_position += 1
