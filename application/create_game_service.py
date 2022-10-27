import random
from dependency_injector.wiring import Provide, inject
from infrastructure.injector import Injector
from domain.card import As, LetterCard, NumberCard
from domain.game import Game
from domain.player import Croupier
from domain.interfaces.game_repository import GameRepository


class CreateGameService:

    @inject
    def __init__(self, game_repository: GameRepository = Provide[Injector.game_repo]):
        self.game_repository = game_repository

    def create_game(self):
        croupier = Croupier(name="Croupier", cards=[], status="waiting_turn", has_hidden_card=True)
        turn_order = [croupier]
        game = Game(turn_order=turn_order, deck=self.create_deck(), game_status="created", turn_position=0)
        response_game = self.game_repository.save(game)
        return response_game

    @staticmethod
    def create_deck():
        cards = [
            As(),  # As
            As(),  # As
            As(),  # As
            As(),  # As
            LetterCard('J'),  # J
            LetterCard('J'),  # J
            LetterCard('J'),  # J
            LetterCard('J'),  # J
            LetterCard('Q'),  # Q
            LetterCard('Q'),  # Q
            LetterCard('Q'),  # Q
            LetterCard('Q'),  # Q
            LetterCard('K'),  # K
            LetterCard('K'),  # K
            LetterCard('K'),  # K
            LetterCard('K'),  # K
            NumberCard(2),
            NumberCard(2),
            NumberCard(2),
            NumberCard(2),
            NumberCard(3),
            NumberCard(3),
            NumberCard(3),
            NumberCard(3),
            NumberCard(4),
            NumberCard(4),
            NumberCard(4),
            NumberCard(4),
            NumberCard(5),
            NumberCard(5),
            NumberCard(5),
            NumberCard(5),
            NumberCard(6),
            NumberCard(6),
            NumberCard(6),
            NumberCard(6),
            NumberCard(7),
            NumberCard(7),
            NumberCard(7),
            NumberCard(7),
            NumberCard(8),
            NumberCard(8),
            NumberCard(8),
            NumberCard(8),
            NumberCard(9),
            NumberCard(9),
            NumberCard(9),
            NumberCard(9),
            NumberCard(10),
            NumberCard(10),
            NumberCard(10),
            NumberCard(10),
        ]
        random.shuffle(cards)
        return cards
