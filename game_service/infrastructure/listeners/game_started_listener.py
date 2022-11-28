from game_service.application.create_game_service import CreateGameService


def create_game(event):
    create_game_service = CreateGameService()
    create_game_service.create_game(players=event["players"], game_id=event["id"])
