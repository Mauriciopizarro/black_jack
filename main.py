
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
from services.croupier_service import CroupierService

croupier_service = CroupierService()
start_game_service = StartGameService()
deal_card_service = DealCardService()
stand_service = StandService()
get_status_service = GetStatusService()
colorama.init()


def get_player_selection():
    selection = input(
        "Choose your next step. if you wanna other card, please type 'other_card' else, type 'stand': "
    )
    return selection


def print_game_status(status_response):
    for player, status in status_response.items():
        status_text = format_status(status)
        print_with_style(status_text)


def format_status(status):
    player_text = f'Player Name {status.get("name")} '
    player_text += f'cards: {status.get("cards")} '
    player_text += f'total points = {status.get("total_points")}'
    return player_text


def print_with_style(text):
    print(Fore.CYAN + Style.DIM + text + Style.RESET_ALL)


def start_game():
    player_name = input(Fore.WHITE + Style.DIM + 'Select your nickname : ' + Style.RESET_ALL)
    start_game_service.start_game(player_name)


def is_game_finished(status_response):
    for player, status in status_response.items():
        if status.get('status') == 'winner':
            return True

    return False


def print_winner_text(status):
    is_player_winner = status.get("player").get("status") == 'winner'
    is_croupier_winner = status.get("croupier").get("status") == 'winner'
    if is_player_winner and is_croupier_winner:
        print(Fore.YELLOW + Style.DIM + 'Tied game')
    elif is_player_winner:
        print(Fore.GREEN + Style.DIM + 'The player won')
    elif is_croupier_winner:
        print(Fore.RED + Style.DIM + 'The croupier won')


def play():
    response = get_status_service.get_players_status()
    print_game_status(response)
    while not is_game_finished(response):
        selection = get_player_selection()
        if selection == "other_card":
            deal_card_service.deal_card()
        else:
            stand_service.stand()
            croupier_service.croupier_play()
        response = get_status_service.get_players_status()
        print_game_status(response)

    print_winner_text(response)
    quit()


start_game()
play()
