
# El objetivo es simple: ganarle al Croupier obteniendo el puntaje más cercano a 21.
# Las figuras (el Valet, la Reina y el Rey) valen 10, el As vale 11 o 1 y todas las otras cartas conservan su valor.
# El Black Jack se produce cuando las dos (2) primeras cartas son un diez o cualquier figura más un As.
import time

from game_manager import GameManager

if __name__ == '__main__':

    #Comienza el juego, se le asignan 2 cartas a cada jugador y se muestran las mismas, el croupier muestra solo 1

    player_name = input('Select your nickname : ')
    game_manager = GameManager(player_name)
    response = game_manager.deal_initial_two_cards()
    print(f'Player {response.get("player").get("name")} cards: {response.get("player").get("cards")} puntos totales = {response.get("player").get("total_points")}')
    print(f'Player {response.get("croupier").get("name")} cards: {response.get("croupier").get("cards")} puntos totales = {response.get("croupier").get("total_points")}')
    selection = input("Choose your next step. if you wanna other card, please type 'other_card' else, type 'stand': ")

    # Se le da a elegir al usuario entre plantarse (stand) o seguir recibiendo cartas (other_card)

    while selection == "other_card":
        response = game_manager.deal_extra_card("player")
        print(f'Player {response.get("player").get("name")} cards: {response.get("player").get("cards")} puntos totales = {response.get("player").get("total_points")}')
        print(f'Player {response.get("croupier").get("name")} cards: {response.get("croupier").get("cards")} puntos totales = {response.get("croupier").get("total_points")}')
        game_manager.check_winner()
        check_winner_game = game_manager.check_winner()

        if check_winner_game == "player_wins":
            print(f'{response.get("player").get("name")} wins the round')
            quit()

        if check_winner_game == "croupier_wins":
            print("You loose, Croupier wins the round")
            quit()
        selection = input("Choose your next step. if you wanna other card, please type 'other_card' else, type 'stand': ")

    # Sale del bucle while cuando el usuario elige la opción stand

    response = game_manager.stand_and_change_turn()
    print("************* Change turn, now Croupier plays *************")
    time.sleep(2)
    print("************* Croupier is exposing his hidden card *************")
    time.sleep(2)
    print(f'Player {response.get("player").get("name")} cards: {response.get("player").get("cards")} puntos totales = {response.get("player").get("total_points")}')
    print(f'Player {response.get("croupier").get("name")} cards: {response.get("croupier").get("cards")} puntos totales = {response.get("croupier").get("total_points")}')
    check_winner_game = game_manager.check_winner()

    if check_winner_game == "player_wins":
        print(f'{response.get("player").get("name")} wins the round')
        quit()

    if check_winner_game == "croupier_wins":
        print("You loose, Croupier wins the round")
        quit()

    while game_manager.player_manager.get_players_status().get("croupier").get("total_points") < 21:
        response = game_manager.deal_extra_card("croupier")
        print("************* The Croupier is receiving cards *************")
        time.sleep(3)
        print(f'Player {response.get("player").get("name")} cards: {response.get("player").get("cards")} puntos totales = {response.get("player").get("total_points")}')
        print(f'Player {response.get("croupier").get("name")} cards: {response.get("croupier").get("cards")} puntos totales = {response.get("croupier").get("total_points")}')

        check_winner_game = game_manager.check_winner()

        if check_winner_game == "player_wins":
            print(f'{response.get("player").get("name")} wins the round')
            quit()

        if check_winner_game == "croupier_wins":
            print("You loose, Croupier wins the round")
            quit()
