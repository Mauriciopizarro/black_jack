import json
from pysondb import db
from models.card import NumberCard, As, LetterCard
from models.game import Game
from models.player import Player, Croupier
from services.exceptions import IncorrectGameID


class GamePysonRepository:
    instance = None

    # Patron singleton
    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = cls()
            cls.db = db.getDb("black_jack_game.json")

        return cls.instance

    def get_game(self, _id):
        query_result = self.db.getBy({"id": _id})
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
        game = Game(turn_order, deck, game_status, turn_position, _id)
        return game

    def get_player_object(self, player_dict, is_croupier):
        if not is_croupier:
            player_cards = []
            for card in player_dict["cards"]:
                player_cards.append(self.get_card_object(card))
            return Player(player_dict["name"], player_dict["player_id"], player_cards, player_dict["status"])

        player_cards = []
        for card in player_dict["cards"]:
            player_cards.append(self.get_card_object(card))
        return Croupier(player_dict["name"], player_dict["player_id"], player_cards, player_dict["status"], player_dict["has_hidden_card"])

    def get_card_object(self, card_dict):
        if card_dict["type"] == "NumberCard":
            return NumberCard(card_dict["value"])
        elif card_dict["type"] == "LetterCard":
            return LetterCard(card_dict["symbol"])
        elif card_dict["type"] == "As":
            return As()

    def save(self, game: Game) -> Game:
        game_id = self.db.add(game.to_json())
        return Game(game.turn_order, game.deck, game.game_status, game.turn_position, game_id)

    def update(self, game: Game) -> Game:
        self.db.updateById(game._id, game.to_json())
        return Game(game.turn_order, game.deck, game.game_status, game.turn_position, game._id)
