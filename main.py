
# El objetivo es simple: ganarle al Croupier obteniendo el puntaje más cercano a 21.
# Las figuras (el Valet, la Reina y el Rey) valen 10, el As vale 11 o 1 y todas las otras cartas conservan su valor.
# El Black Jack se produce cuando las dos (2) primeras cartas son un diez o cualquier figura más un As.
import colorama

from colorama import Fore
from colorama import Style

from services.start_game_service import StartGameService
from services.deal_card_service import DealCardService
from services.stand_service import StandService
from services.get_status_service import GetStatusService
from services.check_game_over_service import CheckGameOverService
from services.croupier_service import CroupierService

croupier_service = CroupierService()
start_game_service = StartGameService()
deal_card_service = DealCardService()
stand_service = StandService()
get_status_service = GetStatusService()
check_game_over_service = CheckGameOverService()
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
    response = get_status_service.get_players_status()
    print(Fore.CYAN + Style.DIM + f'Player {response.get("player").get("name")} cards: {response.get("player").get("cards")} total points = {response.get("player").get("total_points")}' + Style.RESET_ALL)
    print(Fore.CYAN + Style.DIM + f'{response.get("croupier").get("name")} cards: {response.get("croupier").get("cards")} total points = {response.get("croupier").get("total_points")}' + Style.RESET_ALL)


def start_game():
    player_name = input(Fore.WHITE + Style.DIM + 'Select your nickname : ' + Style.RESET_ALL)
    start_game_service.start_game(player_name)
    get_current_cards_and_points()


def player_play():
    selection = get_player_selection()
    while selection == "other_card":
        deal_card_service.deal_card()
        get_current_cards_and_points()
        status = check_game_over_service.check_game_over()
        if status is not None:
            print_game_status(status)
            quit()
        if status is None:
            selection = get_player_selection()
    stand_service.stand()


def croupier_play():
    status = croupier_service.croupier_play()
    get_current_cards_and_points()
    print_game_status(status)


start_game()
player_play()
croupier_play()
