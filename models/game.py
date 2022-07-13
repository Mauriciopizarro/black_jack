class Game:

    #Mati comment

    def __init__(self):
        self.turn_order = ['player', 'croupier']
        self.turn_position = 0

    def get_current_turn(self):
        return self.turn_order[self.turn_position]

    def change_turn(self):
        self.turn_position += 1

    def get_number_of_players(self):
        quantity_players = len(self.turn_order)
        return quantity_players - 1

    def get_turn_position(self):
        return self.turn_position
