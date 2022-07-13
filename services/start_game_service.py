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

    def start_game(self, player_name): #deal cards and return current cards and points
        game = Game()
        self.game_repository.save(game)
        deck = Deck()
        self.deck_repository.save(deck)
        player_1 = Player(player_name)
        croupier = Croupier()
        self.player_repository.save_player(player_1)
        self.player_repository.save_croupier(croupier)
        player1_cards = deck.get_cards(2)
        croupier_cards = deck.get_cards(2)
        self.deal_initial_cards_to_players(player1_cards, croupier_cards)

    def deal_initial_cards_to_players(self, cards_to_player_1, cards_to_player_2):
        player_1 = self.player_repository.get_player()
        player_1.recive_cards(cards_to_player_1)
        croupier = self.player_repository.get_croupier()
        croupier.recive_cards(cards_to_player_2)
