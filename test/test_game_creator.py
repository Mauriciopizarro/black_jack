from unittest.mock import MagicMock, patch

from model.card import CardFive, CardK, CardSeven
from model.player import Player, Bank
from services.game_creator import GameCreator

@patch.object(
    GameCreator, "_get_game_info"
)
@patch.object(
    GameCreator, "_deal_cards_to_player"
)
def test_create_game (mock__deal_cards_to_player, mock_get_game_info):
    mock_get_game_info.return_value = {
        'players': [
            {
                'name': 'juan',
                'cards': ['Seven', 'K'],
            },
            {
                'name': 'mauri',
                'cards': ['Five', 'hide_name']
            }
        ],
    }
    game_creator = GameCreator()

    result = game_creator.create_game()

    assert result == {
        'players': [
            {
                'name': 'juan',
                'cards': ['Seven', 'K'],
            },
            {
                'name': 'mauri',
                'cards': ['Five', 'hide_name']
            }
        ],
    }

    assert  len(game_creator.players) == 2
    assert type(game_creator.players[0]) == Player
    assert type(game_creator.players[1]) == Bank
    assert mock__deal_cards_to_player.call_count == 2


def test_deal_cards_to_player():
    player = MagicMock()
    deck = MagicMock()
    game_creator = GameCreator()
    game_creator.deck = deck
    game_creator._deal_cards_to_player(player)
    assert player.recive_card.call_count == 2
    assert deck.get_card.call_count == 2


def test_get_game_info():
    player = Player("juan")
    bank = Bank("mauri")
    player.cards = [CardSeven(),CardK()]
    bank.cards = [CardFive(),CardK()]
    game_creator = GameCreator()
    game_creator.player = player
    game_creator.bank = bank
    result = game_creator._get_game_info()

    assert result == {
        'players': [
            {
                'name': 'juan',
                'cards': ['Seven', 'K'],
            },
            {
                'name': 'mauri',
                'cards': ['Five', 'hide_name']
            }
        ],
    }