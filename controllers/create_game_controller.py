from fastapi import APIRouter

from services.create_game_service import CreateGameService

router = APIRouter()
game_service = CreateGameService()


@router.post("/create_game")
async def create_game():
    game_service.create_game()
    return {
        "message": "Game created"
    }
