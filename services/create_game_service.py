from models.deck import Deck
from models.game import Game
from models.player import Croupier
from repositories.game_repository import GameRepository


class CreateGameService:

    def __init__(self):
        self.game_repository = GameRepository.get_instance()

    def create_game(self):
        deck = Deck()
        croupier = Croupier()
        game = Game(croupier, deck)
        self.game_repository.save(game)
