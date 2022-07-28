# El objetivo es simple: ganarle al Croupier obteniendo el puntaje más cercano a 21.
# Las figuras (el Valet, la Reina y el Rey) valen 10, el As vale 11 o 1 y todas las otras cartas conservan su valor.
# El Black Jack se produce cuando las dos (2) primeras cartas son un diez o cualquier figura más un As.
import requests
from colorama import Fore
from colorama import Style


def get_player_selection():
    selection = input(
        "Choose your next step. if you wanna other card, please type 'deal' else, type 'stand': "
    )
    return selection


def print_game_status(status_response):
    croupier = status_response.get_game('croupier')
    croupier_cards = str(f'Cards player {croupier.get_game("name")} = {croupier.get_game("cards")}\n')
    croupier_total_points = str(f'Total points = {croupier.get_game("total_points")}\n')
    croupier_status = str(f'¿Is stand? = {croupier.get_game("is_stand")}\n Status = {croupier.get_game("status")}\n')
    print(Fore.BLUE + Style.DIM + croupier_cards, croupier_total_points, croupier_status + Style.RESET_ALL)
    for player in status_response.get_game('players'):
        cards = str(f'Cards player {player.get_game("name")} = {player.get_game("cards")}\n')
        total_points = str(f'Total points = {player.get_game("total_points")}\n')
        status = str(f'¿Is stand? = {player.get_game("is_stand")}\n Status = {player.get_game("status")}\n')
        print(Fore.CYAN + Style.DIM + cards, total_points, status + Style.RESET_ALL)


def start_game():
    url = 'http://localhost:5000/start_game'
    requests.post(url)


def is_game_finished(status_response):
    if status_response.get_game('status_game') == "finished":
        return True
    return False


def croupier_play():
    url = 'http://localhost:5000/stand'
    requests.post(url)

    url = 'http://localhost:5000/croupier_play'
    requests.post(url)


def play():
    url = 'http://localhost:5000/player_status'
    response = requests.get(url).json()
    print_game_status(response)
    while not is_game_finished(response):
        is_croupier_turn = False
        if response.get_game('croupier').get_game('status') == "playing":
            is_croupier_turn = True
        if is_croupier_turn:
            croupier_play()
            url = 'http://localhost:5000/player_status'
            response = requests.get(url).json()
            print_game_status(response)
            quit()

        selection = get_player_selection()
        if selection == "deal":
            url = 'http://localhost:5000/deal_card'
            requests.post(url)
        else:
            croupier_play()

        url = 'http://localhost:5000/player_status'
        response = requests.get(url).json()
        print_game_status(response)
    quit()


start_game()
play()
