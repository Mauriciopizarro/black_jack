import json
from pysondb import db
from domain.card import NumberCard, As, LetterCard
from domain.game import Game
from domain.player import Player, Croupier
from domain.interfaces.game_repository import GameRepository
from application.exceptions import IncorrectGameID


class GamePysonRepository(GameRepository):
    instance = None

    def __init__(self):
        self.db = db.getDb("black_jack_game.json")

    # Patron singleton
    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = cls()
            cls.db = db.getDb("black_jack_game.json")

        return cls.instance

    def get(self, game_id) -> Game:
        query_result = self.db.getBy({"id": game_id})
        if not query_result:
            raise IncorrectGameID()
        game_dict = query_result[0]
        json.dumps(game_dict)
        game_status = game_dict["game_status"]
        deck = []
        turn_order = []
        turn_position = game_dict["turn_position"]
        croupier = game_dict["turn_order"].pop()
        for card in game_dict["deck"]:
            deck.append(self.get_card_object(card))
        for player in game_dict["turn_order"]:
            turn_order.append(self.get_player_object(player, False))
        turn_order.append(self.get_player_object(croupier, True))
        game = Game(turn_order=turn_order, deck=deck, game_status=game_status, turn_position=turn_position, game_id=game_id)
        return game

    def save(self, game: Game) -> Game:
        game_id = self.db.add(game.dict())
        return Game(turn_order=game.turn_order, deck=game.deck, game_status=game.game_status, turn_position=game.turn_position, game_id=game_id)

    def update(self, game: Game) -> Game:
        self.db.updateById(game.game_id, game.dict())
        return Game(turn_order=game.turn_order, deck=game.deck, game_status=game.game_status, turn_position=game.turn_position, game_id=game.game_id)

    def get_player_object(self, player_dict, is_croupier):
        if not is_croupier:
            player_cards = []
            for card in player_dict["cards"]:
                player_cards.append(self.get_card_object(card))
            return Player(name=player_dict["name"], player_id=player_dict["player_id"], cards=player_cards, status=player_dict["status"])

        player_cards = []
        for card in player_dict["cards"]:
            player_cards.append(self.get_card_object(card))
        return Croupier(name=player_dict["name"], cards=player_cards, status=player_dict["status"], has_hidden_card=player_dict["has_hidden_card"])

    @staticmethod
    def get_card_object(card_dict):
        if card_dict["type"] == "NumberCard":
            return NumberCard(card_dict["value"])
        elif card_dict["type"] == "LetterCard":
            return LetterCard(card_dict["symbol"])
        elif card_dict["type"] == "As":
            return As()