from services.game_creator import GameCreator

def create_game():
    game = GameCreator()
    game_info = game.create_game()

    print('Nombre del jugador '+game_info['players'][0]['name'])
    print('Tus cartas son '+ str(game_info['players'][0]['cards']))
    print('Nombre del jugador ' + game_info['players'][1]['name'])
    print('Tus cartas son '+ str(game_info['players'][1]['cards']))


if __name__ == "__main__":
    create_game()