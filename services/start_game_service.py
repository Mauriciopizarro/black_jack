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

    def start_game(self, player_name):
        deck = Deck()
        player_1 = Player(player_name)
        croupier = Croupier()
        game = Game(player_1, croupier)
        player1_cards = deck.get_cards(2)
        croupier_cards = deck.get_cards(2)

        player_1.recive_cards(player1_cards)
        croupier.recive_cards(croupier_cards)

        self.game_repository.save(game)
        self.player_repository.save_player(player_1)
        self.player_repository.save_croupier(croupier)
        self.deck_repository.save(deck)
