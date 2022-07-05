
# El objetivo es simple: ganarle al Croupier obteniendo el puntaje más cercano a 21.
# Las figuras (el Valet, la Reina y el Rey) valen 10, el As vale 11 o 1 y todas las otras cartas conservan su valor.
# El Black Jack se produce cuando las dos (2) primeras cartas son un diez o cualquier figura más un As.
import time

import colorama

from colorama import Fore
from colorama import Style

from services.start_game_service import StartGameService
from services.deal_card_service import DealCardService
from services.stand_service import StandService
from services.get_status_service import GetStatusService
from services.croupier_service import CroupierService
from services.player_service import PlayerService

croupier_service = CroupierService()
start_game_service = StartGameService()
deal_card_service = DealCardService()
stand_service = StandService()
get_status_service = GetStatusService()
player_service = PlayerService()
colorama.init()


def get_player_selection():
    selection = input("Choose your next step. if you wanna other card, please type 'other_card' else, type 'stand': ")
    return selection


def print_game_status(status):
    print(Fore.CYAN + Style.DIM + f'Player {status.get("player").get("name")} cards: {status.get("player").get("cards")} total points = {status.get("player").get("total_points")}' + Style.RESET_ALL)
    print(Fore.CYAN + Style.DIM + f'{status.get("croupier").get("name")} cards: {status.get("croupier").get("cards")} total points = {status.get("croupier").get("total_points")}' + Style.RESET_ALL)

    if status.get("player").get("is_game_over"):
        print(Fore.RED + Style.DIM + f'{status.get("player").get("name")} loose, Croupier win the round' + Style.RESET_ALL)
        quit()

    if status.get("croupier").get("is_game_over"):
        print(Fore.RED + Style.DIM + f'{status.get("player").get("name")} win the round' + Style.RESET_ALL)
        quit()

    if status.get("croupier").get("is_tied_game"):
        print(Fore.RED + Style.DIM + f'Tied game, try again' + Style.RESET_ALL)
        quit()

    return None


def start_game():
    player_name = input(Fore.WHITE + Style.DIM + 'Select your nickname : ' + Style.RESET_ALL)
    start_game_service.start_game(player_name)
    status = get_status_service.get_players_status()
    print_game_status(status)


def player_play():
    selection = get_player_selection()
    while selection == "other_card":
        player_service.player_play()
        status = get_status_service.get_players_status()
        if not None:
            print_game_status(status)
        selection = get_player_selection()
    stand_service.stand()


def croupier_play():
    croupier_service.expose_hidden_card()
    status = get_status_service.get_players_status()
    print_game_status(status)
    print('Croupier receving cards')
    time.sleep(2)
    while croupier_service.croupier_in_game():
        croupier_service.croupier_play()
        status = get_status_service.get_players_status()
        print_game_status(status)
        print('Croupier receving cards')
        time.sleep(2)


start_game()
player_play()
croupier_play()
