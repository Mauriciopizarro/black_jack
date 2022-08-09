
from models.player import Croupier
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

    def start_game(self):
        deck = Deck()
        croupier = Croupier()
        list_of_players = self.player_repository.get_players()
        cant_players = len(list_of_players)

        if cant_players == 0:
            raise NotPlayersCreated()

        game = self.game_repository.get_game()

        if game is not None:
            if game.game_status == "started":
                raise GameAlreadyStarted()

        if game is not None:
            if game.game_status == "finished":
                raise GameNeedToBeRestarted()

        for player in list_of_players:
            player_cards = deck.get_cards(2)
            player.receive_cards(player_cards)

        croupier_cards = deck.get_cards(2)
        croupier.receive_cards(croupier_cards)

        game = Game(list_of_players, croupier)
        game.set_num_players(cant_players)
        game.set_started_game_status()

        for player in list_of_players:
            if game.get_playerId_of_current_turn() == str(player.player_id):
                player.set_as_playing()

        self.game_repository.save(game)
        self.player_repository.save_croupier(croupier)
        self.deck_repository.save(deck)


class NotPlayersCreated(Exception):
    pass


class GameAlreadyStarted(Exception):
    pass


class GameNeedToBeRestarted(Exception):
    pass
