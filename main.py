
# El objetivo es simple: ganarle al Croupier obteniendo el puntaje más cercano a 21.
# Las figuras (el Valet, la Reina y el Rey) valen 10, el As vale 11 o 1 y todas las otras cartas conservan su valor.
# El Black Jack se produce cuando las dos (2) primeras cartas son un diez o cualquier figura más un As.

from game_manager import GameManager

if __name__ == '__main__':

    player_name = input('Select your nickname : ')
    game_manager = GameManager(player_name)
    response = game_manager.deal_initial_two_cards()
    print(f'Player {response.get("player").get("name")} cards: {response.get("player").get("cards")} puntos totales = {response.get("player").get("total_points")}')
    print(f'Player {response.get("croupier").get("name")} cards: {response.get("croupier").get("cards")} puntos totales = {response.get("croupier").get("total_points")}')
    selection = input("Choose your next step. if you wanna other card, please type 'other_card' else, type 'stand': ")

    while selection == "other_card":
        response = game_manager.deal_extra_card("player")
        print(f'Player {response.get("player").get("name")} cards: {response.get("player").get("cards")} puntos totales = {response.get("player").get("total_points")}')
        print(f'Player {response.get("croupier").get("name")} cards: {response.get("croupier").get("cards")} puntos totales = {response.get("croupier").get("total_points")}')
        if game_manager.player_manager.get_players_status().get("player").get("total_points") > 21:
            print("You loose, Croupier wins the round")
            quit()
        selection = input("Choose your next step. if you wanna other card, please type 'other_card' else, type 'stand': ")

    if selection == "stand":
        response = game_manager.stand_and_change_turn()
        print("************* Change turn, now Croupier plays *************")
        print(f'Player {response.get("player").get("name")} cards: {response.get("player").get("cards")} puntos totales = {response.get("player").get("total_points")}')
        print(f'Player {response.get("croupier").get("name")} cards: {response.get("croupier").get("cards")} puntos totales = {response.get("croupier").get("total_points")}')
        selection = input("Choose your next step. if you wanna other card, please type 'other_card' else, type 'stand': ")
        while selection == "other_card":
            response = game_manager.deal_extra_card("croupier")
            print(f'Player {response.get("player").get("name")} cards: {response.get("player").get("cards")} puntos totales = {response.get("player").get("total_points")}')
            print(f'Player {response.get("croupier").get("name")} cards: {response.get("croupier").get("cards")} puntos totales = {response.get("croupier").get("total_points")}')
            if game_manager.player_manager.get_players_status().get("croupier").get("total_points") > 21:
                print(f'{response.get("player").get("name")} wins the round')
                quit()
            selection = input("Choose your next step. if you wanna other card, please type 'other_card' else, type 'stand': ")
        if game_manager.player_manager.get_players_status().get("croupier").get("total_points") <= 21:
            if game_manager.player_manager.get_players_status().get("croupier").get("total_points") > game_manager.player_manager.get_players_status().get("player").get("total_points"):
                print("You loose, Croupier wins the round")
