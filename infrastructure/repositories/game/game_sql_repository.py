import sqlalchemy as db
from sqlalchemy.orm import relationship, Session
from application.exceptions import IncorrectGameID
from domain.card import Card, NumberCard, LetterCard, As
from domain.game import Game
from domain.player import Croupier
from domain.player import Player as DomainPlayer
from domain.interfaces.game_repository import GameRepository
from sqlalchemy import Column, ForeignKey, select
from sqlalchemy.sql.sqltypes import String, Integer, BOOLEAN
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class GameSqlRepository(GameRepository):

    instance = None

    def __init__(self):
        self.engine = self.get_database()

    # Patron singleton
    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = cls()

        return cls.instance

    @staticmethod
    def get_database():
        engine = db.create_engine('mysql+pymysql://user:password@mysql/blackjack')
        Base.metadata.create_all(engine)
        return engine

    def get(self, game_id: str) -> Game:
        deck = []
        players = []

        session = Session(self.engine)
        query = select(DbGame).where(DbGame.id == int(game_id))
        gamedb = session.scalars(query).first()

        if gamedb is None:
            raise IncorrectGameID()

        for card_db in gamedb.cards:
            card = self.get_card_object(card_db)
            deck.append(card)

        for player_db in gamedb.players:
            if player_db.name != "Croupier":
                player = self.get_player_object(player_db, False, session)
                players.insert(0, player)

            if player_db.name == "Croupier":
                croupier = self.get_player_object(player_db, True, session)
                players.append(croupier)

        game = Game(turn_order=players, deck=deck, game_status=gamedb.game_status, turn_position=gamedb.turn_position, game_id=gamedb.id)
        return game

    def save(self, game: Game) -> Game:
        with Session(self.engine) as session:
            players = []
            deck = []

            for player in game.turn_order:
                player_cards = []
                for card in player.cards:
                    player_cards.append(
                        PlayerCard(value=card.value, symbol=card.symbol, type=card.__class__.__name__)
                    )
                players.append(Player(status=player.status, name=player.name, cards=player_cards, player_id=player.player_id, has_hidden_card=player.has_hidden_card))

            for card in game.deck:
                deck.append(GameCard(value=card.value, symbol=card.symbol, type=card.__class__.__name__))

            db_game = DbGame(
                game_status=game.game_status, turn_position=game.turn_position, players=players, cards=deck
            )

            session.add(db_game)
            session.commit()
            session.refresh(db_game)

        return Game(turn_order=game.turn_order, deck=game.deck, game_status=game.game_status, turn_position=game.turn_position, game_id=db_game.id)

    def update(self, game: Game):
        players = []
        deck = []
        session = Session(self.engine)
        deck_db = session.query(GameCard).filter_by(game_id=game.game_id)
        players_db = session.query(Player).filter_by(game_id=game.game_id)

        for player in players_db:
            player_cards_db = session.query(PlayerCard).filter_by(player_id=player.id)
            player_cards_db.delete()

        deck_db.delete()
        players_db.delete()

        game_db = session.execute(select(DbGame).filter_by(id=game.game_id)).scalar_one()
        game_db.game_status = game.game_status
        game_db.turn_position = game.turn_position

        for player in game.turn_order:
            player_cards = []
            for card in player.cards:
                player_cards.append(
                    PlayerCard(value=card.value, symbol=card.symbol, type=card.__class__.__name__)
                )
            players.append(
                Player(status=player.status, name=player.name, cards=player_cards, player_id=player.player_id,
                       has_hidden_card=player.has_hidden_card))

        for card in game.deck:
            deck.append(GameCard(value=card.value, symbol=card.symbol, type=card.__class__.__name__))

        game_db.cards = deck
        game_db.players = players

        session.flush()
        session.commit()

    @staticmethod
    def get_card_object(db_card) -> Card:
        if db_card.type == "NumberCard":
            return NumberCard(db_card.value)
        elif db_card.type == "LetterCard":
            return LetterCard(db_card.symbol)
        elif db_card.type == "As":
            return As()

    def get_player_object(self, player_db, is_croupier, session):
        player_cards_db = select(PlayerCard).where(PlayerCard.player_id == player_db.id)
        cards_db = session.scalars(player_cards_db)
        cards = []

        for card in cards_db:
            card_object = self.get_card_object(card)
            cards.append(card_object)

        has_hidden_card = False
        if player_db.has_hidden_card:
            has_hidden_card = True
        if not is_croupier:
            return DomainPlayer(name=player_db.name, player_id=player_db.player_id, cards=cards, status=player_db.status, has_hidden_card=False)

        return Croupier(name=player_db.name, player_id=player_db.player_id, cards=cards, status=player_db.status, has_hidden_card=has_hidden_card)


class DbGame(Base):
    __tablename__ = "game"

    id = Column("id", Integer, primary_key=True)
    game_status = Column("game_status", String(255))
    turn_position = Column("turn_position", Integer)
    players = relationship("Player", back_populates="game")
    cards = relationship("GameCard", back_populates="game")


class Player(Base):
    __tablename__ = "player"

    id = Column("id", Integer, primary_key=True)
    player_id = Column("player_id", String(255))
    status = Column("status", String(255))
    has_hidden_card = Column("has_hidden_card", BOOLEAN)
    name = Column("name", String(255))
    game_id = Column(Integer, ForeignKey("game.id"))
    game = relationship("DbGame", back_populates="players")
    cards = relationship("PlayerCard", back_populates="player")


class GameCard(Base):
    __tablename__ = "game_card"

    id = Column("id", Integer, primary_key=True)
    value = Column("value", Integer)
    symbol = Column("symbol", String(255))
    type = Column("type", String(255))
    game_id = Column(Integer, ForeignKey("game.id"))
    game = relationship("DbGame", back_populates="cards")


class PlayerCard(Base):
    __tablename__ = "player_card"

    id = Column("id", Integer, primary_key=True)
    value = Column("value", Integer)
    symbol = Column("symbol", String(255))
    type = Column("type", String(255))
    player_id = Column(Integer, ForeignKey("player.id"))
    player = relationship("Player", back_populates="cards")

