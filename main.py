
# El objetivo es simple: ganarle al Croupier obteniendo el puntaje más cercano a 21.
# Las figuras (el Valet, la Reina y el Rey) valen 10, el As vale 11 o 1 y todas las otras cartas conservan su valor.
# El Black Jack se produce cuando las dos (2) primeras cartas son un diez o cualquier figura más un As.
import colorama

from colorama import Fore
from colorama import Style
from game_service import GameService

game_service = GameService()
colorama.init()


def get_player_selection():
    selection = input("Choose your next step. if you wanna other card, please type 'other_card' else, type 'stand': ")
    return selection


def print_game_status(status):
    if status.get("player").get("game_over_status"):
        return print(Fore.RED + Style.DIM + f'{status.get("player").get("name")} loose, Croupier win the round' + Style.RESET_ALL)

    if status.get("croupier").get("game_over_status"):
        return print(Fore.RED + Style.DIM + f'{status.get("player").get("name")} win the round' + Style.RESET_ALL)


def get_current_cards_and_points():
    response = game_service.get_players_status()
    print(Fore.CYAN + Style.DIM + f'Player {response.get("player").get("name")} cards: {response.get("player").get("cards")} total points = {response.get("player").get("total_points")}' + Style.RESET_ALL)
    print(Fore.CYAN + Style.DIM + f'{response.get("croupier").get("name")} cards: {response.get("croupier").get("cards")} total points = {response.get("croupier").get("total_points")}' + Style.RESET_ALL)


def start_game():
    player_name = input(Fore.WHITE + Style.DIM + 'Select your nickname : ' + Style.RESET_ALL)
    game_service.start_game(player_name)
    get_current_cards_and_points()


def player_play():
    selection = get_player_selection()
    while selection == "other_card":
        game_service.deal_card()
        get_current_cards_and_points()
        status = game_service.check_game_over()
        if status is not None:
            print_game_status(status)
            quit()
        if status is None:
            selection = get_player_selection()
    game_service.stand()


def croupier_play():
    status = game_service.croupier_play()
    get_current_cards_and_points()
    print_game_status(status)


start_game()
player_play()
croupier_play()
