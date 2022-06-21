
# El objetivo es simple: ganarle al Croupier obteniendo el puntaje más cercano a 21.
# Las figuras (el Valet, la Reina y el Rey) valen 10, el As vale 11 o 1 y todas las otras cartas conservan su valor.
# El Black Jack se produce cuando las dos (2) primeras cartas son un diez o cualquier figura más un As.

from game_manager import GameManager

if __name__ == '__main__':

    player_name = input('Select your nickname : ')
    game_manager = GameManager(player_name)
    response = game_manager.start_game()
    print(f'Player {player_name} cards: {response.get("player")}')
    print(f'Croupier cards: {response.get("croupier")}')
