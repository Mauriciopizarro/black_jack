from models.player import Player, Croupier
from models.deck import Deck
from repositories.deck_repository import DeckRepository
from repositories.player_repository import PlayerRepository
from models.game import Game
from repositories.game_repository import GameRepository


class StartGameService:

    def __init__(self):
        self.deck_repository = DeckRepository.get_instance()
        self.player_repository = PlayerRepository.get_instance()
        self.game_repository = GameRepository.get_instance()

    def start_game(self, player_name, cant_players):
        deck = Deck()
        croupier = Croupier()
        list_of_players = []

        for x in range(cant_players):
            player = Player(player_name)
            list_of_players.append(player)

        for player in list_of_players:
            player_cards = deck.get_cards(2)
            player.receive_cards(player_cards)

        game = Game(list_of_players, croupier)
        game.set_num_players(cant_players)
        croupier_cards = deck.get_cards(2)
        croupier.receive_cards(croupier_cards)

        if game.quantity_players > 3:
            raise CantPlayersIncorrect()

        for player in list_of_players:
            if game.get_playerId_of_current_turn() == str(player.player_id):
                player.set_as_playing()

        self.game_repository.save(game)
        self.player_repository.save_players(list_of_players)
        self.player_repository.save_croupier(croupier)
        self.deck_repository.save(deck)


class CantPlayersIncorrect(Exception):
    pass

